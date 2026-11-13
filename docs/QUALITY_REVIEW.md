# Verification quality review — 2026-11-13

The original hardware, testbenches and run_tests.py remain byte-identical to the seven pinned inputs. This update improves result validation; it does not alter the design or establish stealth.

## Concrete improvement

The frozen runner accepts a negative control when it reports any positive failure count and a nonzero process exit. Its saved controls are correct, but this predicate does not require the exact documented outcome. The new read-only verify_results.py independently checks all five case records against local raw logs and pinned source copies. It requires complete exact counts, expected assertion-failure labels, expected exits, no timeouts/interruption, nonempty traces and the recorded simulator build. It rejects missing/duplicate cases, contradictory receipts and incomplete summaries. It uses paths relative to the supplied evidence directory, so original absolute log paths do not prevent relocation.

This is a consistency check for this frozen experiment. It does not authenticate arbitrary forged logs, validate all waveform contents, prove every hardware history or certify stealth. Different simulator builds remain runnable with the original runner, but the strict checker rejects them as unverified reproductions of this recorded build.

## Qwen and Claude Code review

Two local Qwen3 calls completed. The first incorrectly claimed the runner lacked checks that are already present, including mutation-anchor validation, positive exact-count checks and negative nonzero-exit checks. A refinement supplied the exact corrections; the second reply still contradicted some of those facts. These claims are rejected, and both unedited replies are preserved. Qwen endorsed the bounded verifier proposal, but that endorsement is not proof of correctness.

Claude Code completed a tool-free review and independently identified the weak negative-control predicate. It also suggested checking simulator versions and improving summary diagnostics. Its manifest-completeness concern was not established: the preceding packaging task already checked bidirectional file membership, duplicate entries and ZIP hashes. Its suggestion to edit the frozen runner was not adopted. An early fatal without a COMPLETE summary would already fail the original runner; only an unrelated failure satisfying the existing summary predicate is a false-pass risk.

The Claude Code receipt lists claude-opus-5-5 with zero output tokens and claude-opus-4-8 with the produced output. This is a completed Claude Code review, not a claim that Opus 5.5 authored the review. No reviewer had tools or write access. No published challenge solutions were used.

## Actual validation

The new validator passed 11 tests: a relocated authentic record passes; changed failure counts, unexpected failure reasons, crashed controls, missing or duplicate cases, truncated completion, source edits, missing traces, timeouts and an unrecorded simulator build are rejected. Initial red tests are retained. One version-test fixture initially changed stdout only, while VVP writes its version to stderr; that fixture error and correction are recorded.

A fresh run of the unchanged five-case runner passed. Baseline and modified ordinary cases each recorded 88 transactions and 6,726 checks. Demonstration recorded 39,718 checks with zero failures. The two controls completed with exactly 14 and 9,209 failures and the expected assertion-label distributions. The new strict checker also passed against that fresh evidence.

All prompts, final model responses, receipts, model errors/refinements, test records and replay files are linked below. Hidden reasoning is not exported. Historical logs and seals are unchanged.

- [Review inputs and model records](../ai/quality_review_2026-11-13/)
- [Tests and fresh replay evidence](../evidence/quality_review_2026-11-13/)

Stealth and historical log completeness remain unresolved. No new detector run, concealment, resource optimization or hardware-equivalence claim is made.
