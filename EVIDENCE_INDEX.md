# Evidence index and curation

Source archive: https://github.com/alzaeda19/csaw/tree/5dd10cdb6ebbeba43b5ff6594f4006c2c999f1a3

## Included for submission

- rtl/, tb/, reference/, run_tests.py and SOURCE_HASHES.json: byte-identical frozen simulation inputs.
- evidence/final_runs/ and evidence/portable_reproduction/: saved successful runs, expected-failure controls and traces.
- evidence/development_runs/: actual failed iterations referenced by generation records.
- evidence/historical_recovery/, evidence/original_materials/ and evidence/setup_records/: recovery provenance and AI authorship receipts.
- ai/: all original available generation records, plus a current guide to recovered records.
- addenda/2026-11-12 and 2026-11-12-recovered-records: authentic generation/reviewer/cross-app recovery.
- addenda/2026-11-12-qwen-verification and 2026-11-12-cipher-reconstruction: complete sealed supporting evidence and its AI records.
- addenda/2026-11-13-submission-closeout: recovered tool-output fragments and exact remaining gaps.
- LICENSES/: upstream notices; supplementary reports retain their own attribution.

## Retained only in the source archive

Later detector packages, pretrained model weights, toy datasets, graph tensors and repeated publication/readiness audits are supplemental research, not required generation deliverables. Their reports and AI records remain accessible at the pinned archive commit. The full detector results are at submission/addenda/2026-11-13-detector-miss-investigation/ and submission/addenda/2026-11-13-detector-repair/ there. No omitted file was deleted from the source archive.

Detector reports: [frozen-pair evaluation](https://github.com/alzaeda19/csaw/tree/5dd10cdb6ebbeba43b5ff6594f4006c2c999f1a3/submission/addenda/2026-11-13-detector-repair) and [miss investigation](https://github.com/alzaeda19/csaw/tree/5dd10cdb6ebbeba43b5ff6594f4006c2c999f1a3/submission/addenda/2026-11-13-detector-miss-investigation). These pinned links retain their complete surrounding evidence. No reduction in files establishes stealth or fills missing transcripts.

Historical reports inside the sealed addenda are unchanged. Their original absolute paths identify the original machine and may require relocation for optional historical reruns; the primary run_tests.py uses the bundled relative source files. Cross-references to excluded later audit bundles remain available in the pinned public archive. See [copy provenance](docs/COPY_PROVENANCE.json) for the exact retained bytes.

## Verification quality update

[Review and limitations](docs/QUALITY_REVIEW.md), [model records](ai/quality_review_2026-11-13/) and [fresh replay evidence](evidence/quality_review_2026-11-13/) support the new read-only result checker. This later run preserves all original hardware inputs and adds no stealth claim.

## Independent unchanged-design evaluation

[Report](docs/INDEPENDENT_EVALUATION.md), [model inputs and replies](ai/independent_evaluation_2026-11-13/) and [direct evidence checks](evidence/independent_evaluation_2026-11-13/). This is a source-aware review of existing experimental records; no new detector, simulation or synthesis run was made.
