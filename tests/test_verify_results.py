import importlib.util
import json
from pathlib import Path
import shutil
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location('verify_results', ROOT / 'verify_results.py')
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

class VerifyResultsTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.run = Path(self.temp.name) / 'relocated'
        shutil.copytree(next((ROOT / 'evidence/final_runs').iterdir()), self.run)

    def tearDown(self):
        self.temp.cleanup()

    def change_json(self, path, change):
        p = self.run / path
        data = json.loads(p.read_text())
        change(data)
        p.write_text(json.dumps(data))

    def rejected(self):
        self.assertTrue(module.verify_run(self.run))

    def test_authentic_relocated_run_passes(self):
        self.assertEqual(module.verify_run(self.run), [])

    def test_wrong_negative_failure_count_rejected(self):
        p = self.run / 'negative_no_fault/simulate.stdout.log'
        p.write_text(p.read_text().replace('failures=14', 'failures=1'))
        self.rejected()

    def test_crashed_negative_control_rejected(self):
        self.change_json('negative_no_fault/simulate.command.json', lambda x: x.update(returncode=-9))
        self.rejected()

    def test_truncated_completion_rejected(self):
        p = self.run / 'negative_always_fault/simulate.stdout.log'
        p.write_text(p.read_text().replace('COMPLETE checks=', 'TRUNCATED checks='))
        self.rejected()

    def test_missing_case_rejected(self):
        self.change_json('result.json', lambda x: x['cases'].pop())
        self.rejected()

    def test_duplicate_case_rejected(self):
        self.change_json('result.json', lambda x: x['cases'].append(x['cases'][0]))
        self.rejected()

    def test_source_change_rejected(self):
        p = self.run / 'baseline_normal/sources/baseline.v'
        p.write_text(p.read_text() + '\n// changed source\n')
        self.rejected()

    def test_missing_trace_rejected(self):
        (self.run / 'demonstration/demo_trace.csv').unlink()
        self.rejected()

    def test_wrong_failure_reason_rejected(self):
        p = self.run / 'negative_no_fault/simulate.stdout.log'
        p.write_text(p.read_text().replace('check=MISO_RELATION', 'check=UNRELATED'))
        self.rejected()

    def test_unrecorded_tool_version_rejected(self):
        p = self.run / 'vvp_version.stdout.log'
        p.write_text('unsupported simulator version\n')
        (self.run / 'vvp_version.stderr.log').write_text('')
        self.rejected()

    def test_timeout_rejected(self):
        self.change_json('modified_normal/simulate.command.json', lambda x: x.update(timed_out=True))
        self.rejected()

if __name__ == '__main__':
    unittest.main()
