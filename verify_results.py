#!/usr/bin/env python3
"""Check frozen-run evidence without executing tools or changing hardware.

This checks consistency with the recorded experiment, not authenticity of
untrusted logs, universal hardware correctness, or stealth.
"""
import argparse
from collections import Counter
import hashlib
import json
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parent
RECORDED_BUILD = 's20260301-831-g1cb990b6f-dirty'
NORMAL = {'transactions': 88, 'checks': 6726, 'failures': 0}
DEMO = {'checks': 39718, 'failures': 0, 'reads': 120, 'normal_reads': 114,
        'fault_reads': 6, 'known_operations': 10, 'expected_flips': 7, 'observed_flips': 7}
EXPECTED = {
    'baseline_normal': NORMAL,
    'modified_normal': NORMAL,
    'demonstration': DEMO,
    'negative_no_fault': {**DEMO, 'failures': 14, 'observed_flips': 0},
    'negative_always_fault': {**DEMO, 'failures': 9209, 'observed_flips': 8843},
}
CONTROL_HASHES = {
    'negative_no_fault': 'd0e1a896cb22fda608f6e33db467b05996ebf4415e9b31f8db73be37cd26422a',
    'negative_always_fault': '2ea1f10f1409032b0f1812625784b53afb40f938d10e6032c43b25e0b5a2fb03',
}
FAILURE_LABELS = {
    'negative_no_fault': {'MISO_RELATION': 7, 'WORD_RELATION': 6, 'FAULT_COUNT_MATCH': 1},
    'negative_always_fault': {'MISO_RELATION': 8836, 'CS_HIGH_PASSTHROUGH': 242,
                             'WORD_RELATION': 120, 'ORIGINAL_MODIFIED_VALUE': 10, 'FAULT_COUNT_MATCH': 1},
}


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def read_json(path):
    return json.loads(path.read_text())


def verify_run(folder):
    """Return failures; an empty list means the bounded record checks passed."""
    folder = Path(folder).resolve()
    errors = []

    def check(condition, message):
        if not condition:
            errors.append(message)

    try:
        pins = read_json(ROOT / 'SOURCE_HASHES.json')
        for name, expected in pins.items():
            check(digest(ROOT / name) == expected, 'Frozen input changed: ' + name)
        for tool in ('iverilog', 'vvp'):
            version_text = (folder / (tool + '_version.stdout.log')).read_text() + (folder / (tool + '_version.stderr.log')).read_text()
            check(RECORDED_BUILD in version_text, tool + ': differs from recorded simulator build')
        result = read_json(folder / 'result.json')
        check(result['status'] == 'PASS' and result.get('sources_preserved') is True,
              'Runner did not finish with preserved sources and PASS')
        check(result['source_checks'] == {
            name: {'expected': h, 'actual': h, 'matches': True} for name, h in pins.items()
        }, 'Runner source-check receipt differs from pinned inputs')
        cases = result['cases']
        check(Counter(c['name'] for c in cases) == Counter(EXPECTED.keys()),
              'Missing, duplicate, or unexpected test cases')
        by_name = {c['name']: c for c in cases}
        for name, counts in EXPECTED.items():
            case = by_name[name]
            case_dir = folder / name
            negative = name in CONTROL_HASHES
            check(case == read_json(case_dir / 'RESULT.json'), name + ': conflicting result receipts')
            check(case.get('meets_expectation') is True and case.get('negative_control') is negative,
                  name + ': incorrect result classification')
            for phase in ('compile', 'simulate'):
                receipt = read_json(case_dir / (phase + '.command.json'))
                check(receipt == case[phase], name + ': conflicting ' + phase + ' receipt')
                expected_exit = 1 if negative and phase == 'simulate' else 0
                check(receipt['returncode'] == expected_exit and receipt.get('timed_out') is False
                      and not receipt.get('interrupted', False), name + ': unexpected ' + phase + ' termination')
                for stream in ('stdout', 'stderr'):
                    check((case_dir / (phase + '.' + stream + '.log')).is_file(),
                          name + ': missing ' + phase + ' ' + stream)
            stdout = (case_dir / 'simulate.stdout.log').read_text()
            summaries = re.findall(r'^COMPLETE (.+)$', stdout, re.M)
            check(len(summaries) == 1, name + ': expected one complete summary')
            parsed = {}
            if len(summaries) == 1:
                fields = summaries[0].split()
                check(all(re.fullmatch(r'\w+=\d+', f) for f in fields), name + ': malformed summary')
                pairs = [f.split('=', 1) for f in fields]
                parsed = {k: int(v) for k, v in pairs}
                check(len(parsed) == len(fields), name + ': duplicate summary fields')
            check(parsed == counts == case.get('counts'), name + ': unexpected completion counts')
            check(case.get('summary_lines') == summaries, name + ': raw and recorded summaries differ')
            failures = re.findall(r'^FAIL .* check=(\w+)', stdout, re.M)
            check(len(failures) == len(re.findall(r'^FAIL ', stdout, re.M)), name + ': malformed assertion failure record')
            check(Counter(failures) == Counter(FAILURE_LABELS.get(name, {})),
                  name + ': unexpected assertion failure signature')
            fatals = [line for line in stdout.splitlines() if line.startswith('FATAL:')]
            check((len(fatals) == 1 and fatals[0].endswith(': demonstration checks failed'))
                  if negative else not fatals, name + ': unexpected fatal diagnostic')
            normal_tb = name.endswith('_normal')
            wrapper = 'reference/baseline_protocol_dut.sv' if name == 'baseline_normal' else 'rtl/modified_protocol_dut.sv'
            tb = 'reference/paired_normal_tb.sv' if normal_tb else 'tb/demo_tb.sv'
            sources = {Path(rel).name: pins[rel] for rel in ['rtl/baseline.v', 'rtl/cells_sim.v', wrapper, tb]}
            if negative:
                sources['modified_protocol_dut.sv'] = CONTROL_HASHES[name]
            check(case['source_hashes'] == sources, name + ': recorded source hashes differ')
            actual = {p.name: digest(p) for p in (case_dir / 'sources').iterdir() if p.is_file()}
            check(actual == sources, name + ': source copies differ')
            traces = ['io_trace.csv', 'pins.vcd'] if normal_tb else ['demo_trace.csv', 'demo_pins.vcd']
            for trace in traces:
                p = case_dir / trace
                check(p.is_file() and p.stat().st_size > 0, name + ': missing or empty ' + trace)
    except (OSError, ValueError, KeyError, TypeError, AttributeError) as exc:
        errors.append('Incomplete or malformed evidence: ' + str(exc))
    return errors


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('run_directory', type=Path, help='One runner evidence directory containing result.json')
    args = parser.parse_args()
    errors = verify_run(args.run_directory)
    print(json.dumps({'status': 'FAIL' if errors else 'PASS', 'errors': errors,
                      'scope': 'Recorded experiment consistency only; no new simulation or stealth proof.'}, indent=2))
    return 1 if errors else 0


if __name__ == '__main__':
    raise SystemExit(main())
