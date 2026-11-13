"""Build and verify a documentation-only submission update, preserving original bytes."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib, json, subprocess, zipfile, sys

ROOT = Path(__file__).resolve().parents[1]
REPO = ROOT.parents[1] / 'work/csaw-private-submission'
BASE = 'd87e907befe513f6d072a1cfc558188c5cf34e90'

def sha(data):
    return hashlib.sha256(data).hexdigest()

def verify(repo):
    original = json.loads((repo/'docs/COPY_PROVENANCE.json').read_text())['copies']
    pins = json.loads((repo/'SOURCE_HASHES.json').read_text())
    for path, expected in pins.items():
        assert sha((repo/path).read_bytes()) == expected, path
    for entry in original:
        assert sha((repo/entry['destination']).read_bytes()) == entry['sha256'], entry['destination']
    manifest = json.loads((repo/'MANIFEST.json').read_text())['files']
    for path, record in manifest.items():
        data = (repo/path).read_bytes()
        assert len(data) == record['bytes'] and sha(data) == record['sha256'], path
    with zipfile.ZipFile(repo/'submission.zip') as z:
        assert z.testzip() is None
        names=z.namelist()
        assert len(names)==len(set(names))
        assert set(names)==set(manifest)|{'MANIFEST.json'}
        for path in names:
            assert z.read(path)==(repo/path).read_bytes(), path
        for entry in original:
            assert sha(z.read(entry['destination']))==entry['sha256'], entry['destination']
    zsha=sha((repo/'submission.zip').read_bytes())
    assert (repo/'submission.zip.sha256').read_text()==zsha+'  submission.zip\n'
    return {'frozen_inputs_unchanged':len(pins),'original_files_preserved':len(original),'manifest_files':len(manifest),'zip_entries':len(names),'zip_sha256':zsha,'zip_bytes':(repo/'submission.zip').stat().st_size}

def build():
    original=json.loads((REPO/'docs/COPY_PROVENANCE.json').read_text())['copies']
    original_paths={e['destination'] for e in original}
    base_manifest=json.loads(subprocess.check_output(['git','show',BASE+':MANIFEST.json'],cwd=REPO))['files']
    sealed=[p for p in base_manifest if p.startswith('addenda/')]
    for path in sealed:
        assert sha((REPO/path).read_bytes())==base_manifest[path]['sha256'], path
    files={}
    for path in sorted(REPO.rglob('*')):
        rel=path.relative_to(REPO).as_posix()
        if not path.is_file() or '.git' in path.parts or rel in ('MANIFEST.json','submission.zip','submission.zip.sha256'):
            continue
        if rel not in original_paths and (path.name=='.DS_Store' or '__pycache__' in path.parts or path.suffix=='.pyc' or rel.startswith('runs/')):
            continue
        data=path.read_bytes();files[rel]={'bytes':len(data),'sha256':sha(data)}
    (REPO/'MANIFEST.json').write_text(json.dumps({'scope':'Private submission payload; self/ZIP/checksum excluded. Original provenance-listed historical caches preserved; new caches excluded.','created_utc':datetime.now(timezone.utc).isoformat(),'files':files},indent=2)+'\n')
    with zipfile.ZipFile(REPO/'submission.zip','w',zipfile.ZIP_DEFLATED) as z:
        for rel in sorted(set(files)|{'MANIFEST.json'}):z.write(REPO/rel,rel)
    (REPO/'submission.zip.sha256').write_text(sha((REPO/'submission.zip').read_bytes())+'  submission.zip\n')
    result=verify(REPO)
    result.update(checked_utc=datetime.now(timezone.utc).isoformat(),sealed_bundles_unchanged=len({p.split('/')[1] for p in sealed}),sealed_files_unchanged=len(sealed),indexed_gaps_remaining=30,newly_closed_indexed_gaps=0)
    (ROOT/'PACKAGE_VERIFICATION.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))

if __name__=='__main__':
    if len(sys.argv)==2:print(json.dumps(verify(Path(sys.argv[1])),indent=2))
    else:build()
