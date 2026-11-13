# What remains before submission

**Your package is assembled and uploaded to a private GitHub repository. It has not been confirmed as received or accepted by course staff. Full challenge compliance is not established.**

## Already included

- Modified RTL and its preserved baseline/dependencies.
- Demonstration testbench, passing saved simulations, deliberate failing controls and their traces.
- Technical brief covering recovery, AI authorship, the disclosed behavior and encryption explanation.
- Available AI records, including failed drafts, Qwen/Claude reviews and corrections.
- Submission ZIP with README.md, rtl/, tb/ and ai/ at its root, supporting evidence and a checksum.

## Still unresolved

1. **Staff need access.** The repository is private and collaborator invitations remain skipped at your request. Give course staff repository access or deliver the ZIP through the channel they require. You said the course uses GitHub; the original competition page separately names a form. Uploading to GitHub does not prove staff receipt.
2. **Stealth has not been demonstrated.** The modification is visible in the source. In the saved detector comparison, HT2 detects it while passing the clean design; HT1/HT3 miss it and HT4 flags both. These findings do not satisfy the stealth objective by themselves. The report says so clearly; it does not claim an approved alternative or a guaranteed grade.
3. **Complete historical AI logs cannot be established.** The 6,178-character historical output gap has been recovered. Remaining known gaps are 12 incoming reviewer instructions, 11 outgoing reviewer argument fields (one aborted before dispatch), and seven pin-audit exchanges. The [exact inventory](MISSING_AI_RECORDS.md) lists every identified record; this corrects earlier short summaries that omitted the already-documented outgoing fields. The qualifier requires all generation-related prompts and responses; which missing historical material affects acceptance is a staff decision. Existing records and gaps are preserved; nothing is fabricated.

## Limits that should stay visible

Normal-operation evidence covers the saved tests and the formal proof's stated protocol/model conditions. It does not prove every possible malformed input sequence or physical hardware history. Resource increases are measured; negligible overhead is not established. These are evidence limits, not additional missing folders or a claim that ordinary saved tests failed.

## Optional or stronger-scoring work

- Numeric key recovery is a bonus.
- Actual board programming/execution is not required for this simulation-only qualifier. Future-hardware reproduction details still belong in the brief and are included with limitations.
- More sophisticated automation and negligible overhead target higher rubric scores. The project does not claim either has been fully achieved.
- Passing all four particular detectors is not an explicit qualifier requirement.

The [independent evaluation](docs/INDEPENDENT_EVALUATION.md) provides the evidence and model-error corrections. The [official requirements snapshot](QUALIFIER_REQUIREMENTS.md) is the basis for this distinction. The packet is ready for staff to review with these disclosures; it is not certified as fully satisfying every requirement.

The [Jarvis/Claude record follow-up](docs/AI_LOG_RECOVERY_FOLLOWUP.md) adds selected early planning history but closes none of the 30 indexed gaps. It also discloses early solution references preceding the later no-solutions instruction, without asserting influence on the final hardware.
