# CSAW 2026 qualifier submission

This private repository is the focused submission package. Download `submission.zip`, verify it with `submission.zip.sha256`, and extract it into a new directory. The ZIP places README.md, rtl/, tb/ and ai/ at its root, matching the qualifier layout. Supporting reference/evidence files are included because the runner and technical claims depend on them.

**All four deliverable categories are included; complete AI-log coverage and full challenge compliance are not established.** Stealth remains unestablished, and historical AI records have the exact gaps listed below. This package does not claim an approved alternative scope, a grade or staff acceptance.

**Latest independent assessment:** [what remains for submission](SUBMISSION_STATUS.md) and [Qwen/Claude evaluation with corrected findings](docs/INDEPENDENT_EVALUATION.md). Hardware is unchanged.

**Latest record recovery:** [authentic output recovery and exact remaining gaps](docs/AI_LOG_RECOVERY.md).

## Required deliverables

| Deliverable | Entry point |
|---|---|
| AI-generated modified RTL | [rtl/modified_protocol_dut.sv](rtl/modified_protocol_dut.sv), preserved baseline and primitive dependencies in rtl/ |
| Demonstration testbench | [tb/demo_tb.sv](tb/demo_tb.sv), [run_tests.py](run_tests.py), reference/ controls |
| Generation prompts and responses | [AI records guide](ai/GENERATION_RECORDS_GUIDE.md) and linked authentic recovery supplements |
| Technical brief | This README and [verified encryption explanation](ENCRYPTION_EXPLANATION.md) |

## Reproduce saved simulation checks

Python 3 and compatible Icarus Verilog/VVP are required. The recorded tool build is Icarus 14.0 development, s20260301-831-g1cb990b6f-dirty. Other tool versions/platforms have not been validated. Tools are not bundled. From the extracted ZIP:

```sh
python3 run_tests.py --tool-bin /absolute/path/to/iverilog-and-vvp-directory
```

When running from a Git checkout, supply an output directory outside every Git repository:

```sh
python3 run_tests.py --tool-bin /absolute/path/to/tools --output-root /absolute/path/outside-git/csaw-results
```

The unchanged runner checks all seven pinned source hashes, retains tool versions and commands, and checks five expected outcomes. It creates deliberately broken controls only in its output folder. See [evidence index](EVIDENCE_INDEX.md) for exact saved runs. The initial packaging task verified file identity and ZIP relocation. The subsequent quality review below includes a fresh simulation replay.

| Saved test | Result |
|---|---|
| Baseline ordinary operation | 88 transactions, 6,726 checks, zero failures |
| Modified ordinary operation | 88 transactions, 6,726 checks, zero failures |
| Demonstration | 39,718 checks, zero failures; 120 complete reads: 114 normal and 6 faulted |
| Fault removed control | Correctly fails with 14 failures |
| Permanently inverted output control | Correctly fails with 9,209 failures |

These are assertion counts and repeated examples, not thousands of independent cipher vectors. Trace CSV/VCD and exact exit receipts are included. The earlier extracted-source replay reproduced these outcomes using the same toolchain; cross-platform portability is not claimed.

## Stronger result verification

After the runner finishes, check the evidence folder it prints:

```sh
python3 verify_results.py /absolute/path/to/the/printed/evidence-folder
```

The separate checker requires exact negative-control counts and failure reasons, consistent raw logs and receipts, all five completed cases, unchanged source copies, nonempty traces and the recorded simulator build. This prevents an unrelated failure from being accepted merely because a negative test failed. It does not rerun simulation or establish stealth. The frozen original runner and hardware are unchanged.

The [Qwen and Claude Code review](docs/QUALITY_REVIEW.md) records accepted findings, rejected model claims and refinements. A fresh five-case simulation replay passed, the stricter checker accepted it, and all 11 checker tests passed. [Fresh evidence](evidence/quality_review_2026-11-13/) is included. To check the checker itself: `python3 -m unittest discover -s tests -v`.

## Recovery and source provenance


The preserved recovery report describes starting with the original qualifier binary, SHA-256 `5fa5fda9768c36808780398d8e24d125d860aacc62b61af8b4c5124dd759ddbe`. Official Project IceStorm tooling was pinned to commit `00da9c3e6ceff056248e3451dd6fd3210d6ceec9`. `iceunpack` produced an ASC configuration for a 5k device; `icepack` reportedly reproduced the original bytes. This is evidence of an exact packing round trip, not proof of Verilog translation equivalence. Unmodified `icebox_vlog.py` generated the structural Verilog candidate.

Icarus rejected an output declared as a net in the module header and separately declared as a register. The retained derivation script performs two declaration compatibility replacements: `output io_16_31_1` becomes `output reg io_16_31_1`, and `reg io_16_31_1 = 0;` becomes `initial io_16_31_1 = 0;`. The procedural driver and initial value remain. A separate adapter connects inferred protocol roles to recovered ports without substituting data or adding target clocks. The supplied baseline used here has SHA-256 `180b895d9e3ada5f662ee502277db1eedcfd80bd53fbf29d9a612fcc3e1b1765`.

Primitive simulation uses official Yosys `techlibs/ice40/cells_sim.v` from commit `5e740962d0c7b8c21b6701fe7a70a5e7ebe28661`, SHA-256 `b5b2bcd86c0d6eea269015aaebff1d5fb66e7ec3f7eded0bde07406e5ac99527`. Yosys itself was not built or run for that recovery. Functional signal mapping was inferred from recovered connectivity and original interface material; it is not a recovered board pin map. The initial recovery report also retained an optional IceStorm input-enable check failure for the inferred clock pad. This is a historical failure record, not a claim that later validator repairs remain broken. That recovery-stage report did not independently validate physical clock-pin wiring. The later source-and-schematic pin audit is included below; it is not a physical board test.


The later original-source reconstruction identifies the cipher and effective key handling; it supersedes the earlier brief's limited algorithm proposal. No published challenge solution was used.

## Encryption explanation

The recovered system is a custom 32-bit four-round cipher: each forward round uses a fixed-mask XOR, AES byte substitution and one-byte rotation; the inverse reverses these steps. The same hardwired mask is reused, with no runtime key-loading transaction or evolving round-key schedule. This is not AES-128. Source-derived checks and the original Verilog agree on 2,564 transactions and 20,512 round-state comparisons, with zero failures. Full equations, limits and reproduction evidence are in [ENCRYPTION_EXPLANATION.md](ENCRYPTION_EXPLANATION.md).

## AI workflow and authorship


The new generation workflow used local Ollama with Qwen3:8b, through Claude Code as the file-tool client, with model alias `qwen3-csaw-agent:20261112234518`. Codex coordinated the bounded task, reviewed generated files, ran simulation checks, and supplied substantive corrections. The use of Claude Code as a client should not be read as a claim that a Claude model authored the design.

Authorship is mixed AI authorship, not sole-Qwen authorship. Qwen's initial RTL compiled but failed nine ordinary checks. A second Qwen iteration applied a Codex-provided template but introduced code fences and a missing `end`, causing compilation to fail. Codex produced the corrected RTL, including explicit chip-select edge handling after reproducing a frame-boundary failure. Codex also authored the independent pin-level comparison testbench supplied to the subsequent workflow. The final Qwen attempt to save the testbench timed out after 360 seconds without producing the file. Codex then saved its already validated template directly. Retained failed iterations and correction records explain these changes; a final successful run does not erase them. The timeout receipt lists a concurrent report-file change made by the Codex report subagent; that inventory change is not evidence of Qwen authorship.

AI records must distinguish native prompts/responses, tool evidence, authored summaries, and reconstructed indexes. The correction record is supporting provenance, not a replacement for the conversations. Historical transcript incompleteness remains a limitation; no missing dialogue is invented or represented as authentic. The report does not claim comprehensive authentic transcript coverage for all prior recovery work.


## Disclosed trigger and payload


The public demonstration word is `32'hC5A02026`. Qualification requires a completed 32-clock ingress frame while chip select is low, followed by a newly sampled START assertion while chip select is high and `ENC_DEC` is 0. The wrapper tracks ingress length and excludes the first 32 selected extraction clocks after START from ingress qualification. Chip-select deassertion clears the ingress counter even when no SCK edge occurs while chip select is high. Reset of the remaining wrapper state is synchronous to SCK.

For a qualifying operation, the wrapper inverts only the first sampled MISO bit of extraction. With the testbench's MSB-first convention, the resulting word must equal the unmodified core's result XOR `32'h80000000`. The other sampled output bits, BUSY, and LED must match the independent reference. The fault state clears after the 32 extraction clocks or a sampled reset. Partial extraction cancellation is demonstrated with reset; arbitrary partial-read abort and resume behavior is not established.

To reproduce the positive case in simulation: reset, shift the public word in MSB-first over 32 selected clocks, deassert chip select, select mode 0, assert START for one sampled rising edge, deassert START, supply seven completion clocks, then select and sample 32 output bits one nanosecond after their rising edges. Compare against an unmodified core receiving identical pins. The expected word difference is exactly `80000000`. Changing one input bit or using mode 1 is tested as a negative case.


## Normal-operation evidence and stealth

The wrapper is openly documented; no concealment or detector-evasion result is claimed. The measured detector investigation found HT2 detecting the frozen modified CSAW design while passing its clean control; HT4 flagged both, and HT1/HT3 missed the modification. These are limited results, not proof of stealth.

The saved cyclic proof covers the encoded 80-cycle host schedule, complete frames, stable transaction mode, prescribed reset/start/readout sequence, and normal-case word exclusions. Its base and induction steps pass at length 100. The separate explicit-clock check covers two transactions over 325 samples. This compositional proof abstracts the common core; it is not universal cryptographic, malformed-protocol or physical-timing verification. See the preserved [verification report](addenda/2026-11-12-qwen-verification/README.md).

Identical synthesis settings give +36 LUT4 cells, +48 registers and +13 carry cells, with unchanged RAM. Negligible hardware overhead is not established. Full historical generation automation is not established; automated verification does not retroactively prove it.

## Future hardware reproduction

The [reference-board pin audit](addenda/2026-11-12-qwen-verification/pin_audit/REPORT.md) gives the board revision, schematic sources and nine mappings. Physical BUSY is pin 23 and LED pin 38; the simulation adapter uses opposite names for these equal-valued outputs. A future board build must use the audited physical mapping rather than treat the simulation adapter as a constraints file. The disclosed interface sequence above is the simulation reproduction procedure. No physical board execution, placed/routed timing or power test is claimed. Preliminary board execution is not required by the qualifier.

## Exact remaining gaps and delivery

- Stealth remains unestablished; the evidence includes detection of the frozen modification.
- The 6,178-character historical output gap is now fully recovered. Remaining known gaps are 12 incoming reviewer instructions, 11 outgoing reviewer argument fields (including one aborted call), and seven pin-audit exchanges. The [exact inventory](MISSING_AI_RECORDS.md) identifies each record. Comprehensive generation-log coverage remains unestablished; the qualifier warns that missing logs can disqualify a submission. No absent dialogue is fabricated.
- Normal behavior is verified only within the saved simulations and encoded proof conditions, not every possible hardware history.
- Numeric key recovery is a bonus, not claimed here. Negligible overhead and complete generation automation are higher-score targets, not additional missing file categories.

The user requested a private GitHub submission repository. Collaborator invitations remain skipped: staff cannot access this private repository unless access is separately granted or the ZIP is provided through the required channel. The live competition qualifier specifies a form, documented in [requirements](QUALIFIER_REQUIREMENTS.md); this task does not submit that form or claim staff receipt.

Historical reports retain dated statements and known model mistakes. This README and ENCRYPTION_EXPLANATION.md are the current brief; the original technical brief is preserved in docs/ for provenance, not as the current readiness claim.
