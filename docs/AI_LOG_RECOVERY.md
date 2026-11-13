# Authentic AI-record recovery — November 13, 2026

**The missing 6,178-character output section is recovered from its original ordinary command-completion event.** No missing instruction or message body was recovered. The [exact remaining-record inventory](../MISSING_AI_RECORDS.md) now enumerates every known gap in this bounded audit, including outgoing-call omissions left out of earlier short summaries.

## Recovered records

| Original record | Result |
|---|---|
| Report-review completion event, native line 99, item exec-84b0552d-5f11-464f-b396-05908175e4f9 | Exact full 46,178-character stdout. Its first 20,000 characters match the prior API prefix; its last 20,000 match the retained native tail. The formerly missing range [20000,26178) contains 6,178 characters and is preserved separately. |
| Report-review completion event, native line 105, item exec-6d9dc924-b32b-4b14-920f-bcc70d5fad38 | Exact full 28,140-character stdout, byte-identical to the earlier assembly of authentic fragments. No additional missing characters were credited for this second record. |

These come directly from `/payload/item/aggregated_output` on original `CommandExecution` completion events. Earlier exports skipped those events as duplicate bookkeeping and retained truncated response-item/API copies. No old command was rerun, text guessed, present-day file concatenation substituted, opaque body decrypted or hidden reasoning inspected. Completion-event line hashes and response-item line hashes differ because they identify different original records.

The [recovery receipt](../evidence/log_recovery_2026-11-13/checks/COMMAND_EVENT_RECOVERY.json) contains exact source paths, event line numbers, timestamps, field pointers, IDs, full-output hashes and comparisons. [Recovered output files](../evidence/log_recovery_2026-11-13/recovered/) preserve the exact ordinary text. Character ranges are zero-based Unicode offsets, not bytes or tokens.

## Still unavailable

- **12 incoming reviewer instructions:** nine task requests and three steering messages.
- **11 outgoing reviewer send_message argument fields:** ten completed call records with empty output receipts, plus one explicitly aborted-before-dispatch call. Empty receipts do not independently establish delivery.
- **7 pin-audit exchanges:** four instructions and three progress messages, counted once per exchange rather than once per endpoint.
- **0 remaining character gaps** in the two audited command outputs.

That is 30 indexed unavailable records, including one aborted call. They are not all confirmed delivered messages. The eleven outgoing omissions were already present in the sealed recovery ledger; earlier short summaries failed to enumerate them. This is a more complete inventory, not new data loss. Intentionally excluded hidden reasoning/internal metadata are not counted as unavailable ordinary messages.

## What was searched and checked

Fresh normal chat reads covered five protocol-review turns, four report-review turns and two pin-review turns. None exposed the missing incoming bodies. Original source-line hashes were checked. Eight matching old app operations were read directly and contain only operation metadata, not prompt/message/arguments. The other three outgoing calls have no old app counterpart. A filename-only exact-ID search of local Claude session JSONL found no match; this is not a search of all Claude cloud history. The seven pin-audit gaps were checked directly at both original endpoints and against the ordinary peer-chat projection.

Native ordinary activity events retain metadata only. The useful additional capture was the full ordinary command-completion output. All absent bodies remain opaque in the sources checked; separate final answers cannot be relabeled as those missing messages without an exact counterpart.

## Claude Code review and Trojan-chat handoff

Claude Code performed two read-only searches/reviews using only Read, Glob and Grep within the curated recovery directory. The first found no identity-matched plaintext in its then-supplied corpus. After Codex found the full completion events, the second reviewed their identifiers and textual boundaries, revised its output-gap conclusion and confirmed the remaining categories. Codex computed hashes and character counts; Claude explicitly did not. Actual model identities, prompts, visible tool traces, final replies and refinements are retained in [AI records](../ai/log_recovery_2026-11-13/).

The handoff to the chat named **trojan** was automatically blocked as a possible cybersecurity risk before a recovery response. No work from that chat is claimed. Codex completed the pin-audit record checks directly. The [observed handoff status](../evidence/log_recovery_2026-11-13/checks/TROJAN_HANDOFF_STATUS.json) preserves the limitation; no further handoff retry followed the observed block.

## Provenance and limitations

Earlier checks and Claude's initial null result are retained as time-scoped observations, explicitly superseded for the recovered output in [check order](../ai/log_recovery_2026-11-13/CHECK_ORDER.md). The native conversation export has a cutoff. All model-visible prompts/tool traces exclude hidden reasoning; no absent dialogue is invented. Historical sealed reports retain their earlier state unchanged.

Hardware, testbenches, the original runner, earlier sealed evidence and the public archive are unchanged. This update adds documentation and authentic records only. It does not establish complete historical generation logs, stealth, staff access or acceptance.
