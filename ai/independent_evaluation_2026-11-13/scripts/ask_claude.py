from pathlib import Path
from datetime import datetime, timezone
import subprocess, json, hashlib
root=Path(__file__).resolve().parents[1]
out=root/'ai_logs/claude'; out.mkdir(exist_ok=False)
argv=['/opt/homebrew/bin/claude','--print','--safe-mode','--tools','','--strict-mcp-config','--mcp-config','{"mcpServers":{}}','--disable-slash-commands','--no-session-persistence','--permission-mode','default','--system-prompt','You are a bounded verification reviewer. Only the supplied text is evidence. No tools, file writes, hardware changes, evasion advice, or published solutions. Return actionable final findings, not a plan to inspect.','--output-format','json','--max-budget-usd','4']
prompt=(root/'review_prompt.txt').read_text()
(out/'prompt.txt').write_text(prompt)
r={'argv':argv,'cwd':str(root),'started_utc':datetime.now(timezone.utc).isoformat(),'input_sha256':hashlib.sha256(prompt.encode()).hexdigest(),'tools_granted':[]}
try:
 with (out/'response.json').open('w') as stdout,(out/'stderr.txt').open('w') as stderr:
  done=subprocess.run(argv,input=prompt,text=True,cwd=root,stdout=stdout,stderr=stderr,timeout=240)
 r['returncode']=done.returncode
except Exception as exc:
 r['error']=repr(exc)
r['ended_utc']=datetime.now(timezone.utc).isoformat()
(out/'receipt.json').write_text(json.dumps(r,indent=2)+'\n')
print(json.dumps(r,indent=2))
