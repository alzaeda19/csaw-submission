# Independent Evaluation — CSAW Preliminary Trojan Package

## 1. Visible source changes a reviewer would identify
Comparing `baseline_adapter.sv` to `modified_wrapper.sv`, both declare `module protocol_dut` wrapping the same `chip recovered` with identical core input connections. The modified version adds, outside the core:
- A localparam trigger constant `DEMO_WORD = 32'hC5A02026` (line 7).
- An XOR on the MISO output: `assign MISO = raw_miso ^ (fault_active && !NORM_CS_N && read_count == 6'd1)` (line 20) — inverts sampled bit31 on the second extraction bit.
- Added state: `ingress_word`, two 6-bit counters, and flags `frame_complete/read_pending/fault_active` (lines 9–11).
- A CS-asynchronous ingress counter (lines 24–31) and a synchronous SCK block building the ingress word and arming the fault only when a rising START edge occurs with CS high, the frame is complete, `ENC_DEC==0`, and `ingress_word==DEMO_WORD` (lines 51–52).
The recovered core instance's input/BUSY/LED connections are unchanged; only MISO is routed through added logic. This is a wrapper-level, single-bit MISO corruption Trojan, self-labeled and not concealed.

## 2. What simulation/proof evidence establishes, and gaps
`demonstration_tb.sv` compares the DUT against an independent `reference_core` with an oracle that derives expected faults from test cases, not DUT internals (lines 2–3). `simulation_summary.json` reports the demonstration at 39,718 checks / 0 failures, 114 normal_reads, 6 fault_reads, 7 expected==7 observed flips; two negative controls behave as designed (no-fault→0 observed, always-fault→8,843). `proof_results.json` reports SAT equivalence for normal behavior, SAT-found counterexamples for fault controls, and an inductive proof of unbounded cyclic normal transactions at length 100.
Covered: documented reset, full 32-bit frames, stable mode, prescribed launch/readout. Outside coverage (per its own `limits`, lines 133–138): malformed frames, arbitrary clock/control glitches, metastability, real board timing, cipher identity. The core is abstracted, not cryptographically verified. The explicit-edge model is bounded to 325 samples.

## 3. What resource counts establish
`overhead.json` reports Yosys `synth_ice40` mapped primitive counts only (method, line 2), no placement/route/timing/power. Modified vs baseline: LUT4 1439→1475 (+36), flip-flops 71→119 (+48), RAM4K 4→4 (0), carry 0→13 (+13), total cells 1514→1611 (+97, 6.41%). The file itself sets `negligible_overhead_established: false` (line 35). These are cell counts only — no physical power, timing, or area may be inferred, and unlike cell types (LUT vs FF vs carry) must not be summed as equivalent area. The +67.6% flip-flop figure is a count ratio, not an area claim.

## 4. What detector results establish for this exact pair
`detector_results.json` covers two candidates under a 4-model ensemble with "any model votes 1" rule.
- `flat_clean` (baseline): HT1–HT3 CLEAN, HT4 TROJAN → ensemble TROJAN. This is a **false alarm** on the clean design (HT4 prob_trojan 0.926).
- `flat_modified`: HT2 and HT4 TROJAN → ensemble TROJAN (correct), but HT1 and HT3 individually **miss** it (CLEAN).
So for this one pair, the permissive ensemble flags both designs as TROJAN, meaning it does not discriminate clean from modified here, and three of four models miss the real Trojan at least once. Scope statements disclaim calibration and universal-stealth claims (lines 72, 144). No inference to other circuits or unseen detectors is supportable.

## 5. Missing-file categories vs incomplete-evidence/bonus/stronger goals
Against `qualifier_requirements.md`:
- **Deliverable categories present** in the repo per Q6: Modified RTL (rtl/), Exploit Testbench (tb/), AI records (ai/), Technical README, ZIP.
- **Known missing log content** (do not overstate): twelve historical reviewer-instruction bodies, 6,178 characters of one historical output, and some unreadable pin-audit peer exchanges. This is partial GenAI-transcript loss — the mandatory "GenAI Transcripts" deliverable (line 33) is present as a category but has incomplete evidence, not a total absence. Total generation logs are **not** established as absent, and staff rejection is **not** certain.
- **Requirements with incomplete evidence**: stealth/overhead claims (overhead explicitly not negligible; detector results mixed), physical/in-hardware exploitability (sim-only), and automation pipeline detail.
- **Optional bonus**: key recovery (lines 95–96). `encryption_explanation.md` describes fixed-mask handling but states (line 26) **no numeric key value** is supplied — so the 10-point bonus is not substantiated.
- **Stronger-scoring goals** (not pass/fail gates): "Exemplary" stealth with negligible overhead (Trojan Quality, line 70), advanced AI pipeline/AST manipulation (line 63), and one-click automation (line 78) — these are rubric maxima, not missing files.

## 6. Plain-English status and open items
The package is **assembled**: a frozen baseline adapter, a modified wrapper with a single-bit MISO Trojan, a self-checking dual-core testbench, simulation/proof/overhead/detector result JSONs, a cipher explanation, and the qualifier snapshot — in a private repo with RTL, tb, AI records, README, and ZIP. The submission has a plausible trigger (specific 32-bit word + START/mode conditions) and a payload (deterministic bit31 corruption), with passing functional and negative-control evidence.
**Unresolved, per the files themselves:** overhead is explicitly not negligible; the detector ensemble flags the clean design too (no clean/modified discrimination on this pair); correctness is bounded to well-formed, documented-protocol histories (malformed frames, glitches, metastability, real timing uncentered); the numeric key bonus is not supplied; and portions of historical AI logs/peer exchanges are missing, leaving the transcript deliverable with incomplete evidence. Staff access has not been granted per your instruction, and the GitHub destination/competition form remain yours to act on — no transmission is made or advised here.
