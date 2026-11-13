# Check order and supersession

1. INBOUND_NATIVE_RECHECK, ORIGINAL_APP_COUNTERPART_CHECK and PIN_GAPS_RECHECK concern the ordinary-message gaps; these remain current.
2. OUTPUT_GAP_RECHECK records the fresh normal API projection BEFORE the full native command-completion event was inspected. It correctly reports that the API projection added no characters, but its 6,178-character remaining-gap field is superseded by COMMAND_EVENT_RECOVERY.
3. COMMAND_EVENT_RECOVERY is the current output status: exact original ordinary command-result fields contain both full outputs, with zero remaining character gaps.
4. Claude's first audit precedes that discovery. The second audit explicitly revises its output conclusion and distinguishes its textual inspection from Codex-computed hashes. Native completion-event lines 99/105 and truncated response-item lines 100/107 are different original records; their hashes are not expected to match.
5. The initial Claude audit called ten outgoing calls delivered. That is unsupported by their empty output receipts. The second review corrects this wording. Three outgoing calls lack old app metadata counterparts: two protocol packaging calls and the aborted report call; eight have metadata-only counterparts. No missing body is replaced with a semantically similar final answer.

These are ordered observations, not deleted errors or silently overwritten history. MISSING_RECORDS.json is the current exact inventory.
