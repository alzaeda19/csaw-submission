# Independent review of the unchanged design — November 13, 2026

The package is assembled for review, but this evaluation does not establish full qualifier compliance. The unchanged wrapper is identifiable from source, HT2 detects the modified member of the saved pair, and historical log completeness remains unestablished. See [plain-English submission status](../SUBMISSION_STATUS.md).

## Method and independence

The starting private-repository commit was `0e0b7e3405a82351cc5e1fa914ff25ba36efa73c`. Qwen3 through local Ollama and Claude Code received the same source-and-evidence prompt in separate calls. Neither saw the other's initial answer or earlier review opinions. Their inputs included the entire wrapper, baseline adapter, demonstration testbench, bounded proof results, measured synthesis counts, original detector result JSON, cipher explanation and qualifier requirements. The full recovered core was not placed in either model's context; its identity and scoped evidence were supplied. Models had no tools or write access.

This was an independent source-aware review, not a blind detection benchmark, complete-core audit or new detector run. The labels and intended modification were disclosed. Subsequent corrective prompts supplied record-based facts, not the other model's opinion. Model agreement is not experimental proof.

Qwen used `qwen3-csaw-agent:20261112234518`, digest `546214eadc8960c30bdd4ddae54b372c16e23ebb3d62948d152ac43fd1645d3e`. Claude Code was version 2.1.311. Both Claude receipts list Opus 5.5 with zero output tokens and Opus 4.8 with generated output; no Opus-5.5-authorship claim is made. All four calls completed. No published solutions were consulted.

## Findings checked against the files

| Topic | Verified finding | Boundary |
|---|---|---|
| Source visibility | The modified wrapper adds a public constant, counters/flags and an output XOR. Named input connections to the same recovered core and BUSY/LED connections are unchanged; MISO goes through the added logic. | Read-only source comparison; not an HDL synthesis or universal equivalence proof. No concealment method is established. |
| Demonstrated behavior | The saved fresh replay has 88 transactions/6,726 checks for each ordinary case, 39,718 demonstration checks with zero failures, and the two expected negative controls. The strict saved-result validator passes. | This evaluation rechecked those records; it did not rerun simulation. |
| Which bit changes | Saved CSV shows seven expected-flip observations, all on the first sampled extraction bit: six full reads and one partial-read/reset case. | Testbench sampling occurs after the nonblocking counter update. This corrects the initial Claude description of a second-bit flip. |
| Normal-operation proof | The saved cyclic synchronous proof establishes the scoped no-mask result at induction length 100. Explicit-edge evidence covers two transactions/325 samples. | Full frames, stable mode, prescribed clock/control schedule and normal-word exclusions apply. Core abstraction is not a cipher proof; arbitrary malformed histories and physical timing are not covered. |
| Resources | +36 LUT4, +48 registers, +13 carry cells, RAM unchanged at 4. Arithmetic matches saved resource records. | Mapped counts only. Negligible overhead is unestablished; that is not proof of the opposite under an agreed threshold. No new synthesis, area, timing or power result. |
| Cipher | The existing original-source reconstruction describes the custom 32-bit four-round cipher and fixed-mask handling. | This review is not an independent full-core re-derivation; the existing reconstruction/evidence remains authoritative. |

## Saved detector results, with clean control

| Detector | Clean design | Modified design | Observation for this pair |
|---|---|---|---|
| HT1 | CLEAN | CLEAN | Misses the modification |
| HT2 | CLEAN | TROJAN | Detects the modification while passing the clean control |
| HT3 | CLEAN | CLEAN | Misses the modification |
| HT4 | TROJAN | TROJAN | Flags both; false alarm on clean control |

The any-positive ensemble flags both. These are the recorded results for the frozen pair under the repaired data-dependency representation, not four fresh experiments. The underlying scores are not calibrated probabilities of stealth or correctness. Two misses do not establish undetectability; a detection does not alone determine the instructor's grade. The qualifier does not require passing these four particular detectors.

The exact detector JSON used for this review is [retained with the inputs](../ai/independent_evaluation_2026-11-13/inputs/detector_results.json). The complete historical detector pipeline remains in the [pinned source archive](https://github.com/alzaeda19/csaw/tree/5dd10cdb6ebbeba43b5ff6594f4006c2c999f1a3/submission/addenda/2026-11-13-detector-repair). No weights, detector rules, thresholds, hardware or extraction method were tuned in this evaluation.

## Model errors and their disposition

- Qwen initially claimed this pair had no false alarms or misses and that qualifier requirements were met. Both claims are rejected. Its refinement printed the correct label table but then incorrectly named HT2 as the clean false alarm. The table/raw JSON identify HT4; the contradictory sentence remains preserved as a model error. Qwen's loose extraction-condition wording is not authoritative: the XOR requires chip select low.
- Claude initially said second extraction bit, three detectors missing the modified design, and implied overhead had been proved non-negligible. Its corrigendum explicitly accepts the first-bit, two-miss and “not established” corrections. Physical execution is not a missing mandatory item in this simulation phase. No opinion establishes staff acceptance.
- The local CSV cross-check initially expected seven rows while filtering only full extraction, and stopped on an assertion. The seventh observation is the named partial-extraction reset case. The corrected check includes both phases; its receipt records that error. No data was changed.

## Retained evidence and limits

[Original prompts, initial responses, corrective prompts, complete final replies and call receipts](../ai/independent_evaluation_2026-11-13/) are retained without replacing the erroneous drafts. [Direct source/record checks](../evidence/independent_evaluation_2026-11-13/) verify seven frozen inputs, all five historical seals, the saved replay, resource arithmetic, label matrix and extraction observations. This task's visible Codex export has an explicit cutoff and excludes hidden reasoning. No new simulation, synthesis or detector run is claimed here.

Neither additional model review nor documentation fills unavailable history, proves stealth, or grants staff access. The hardware, frozen runner, testbenches and earlier evidence bundles remain unchanged.
