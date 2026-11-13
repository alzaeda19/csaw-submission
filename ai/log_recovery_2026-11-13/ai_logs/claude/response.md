# Recovery audit result: nothing recovered

I recovered no plaintext. None of the 12 inbound instruction bodies, none of the 11 outbound `send_message` arguments and none of the missing output range has an exact, identity-matched readable copy in this directory.

## 1. Exact recoveries
None.

- **`inputs/api_protocol_fresh.json` and `inputs/api_report_fresh.json`:** all 9 turns (5 protocol, 4 report) have `"userMessagePresent": false`. They contain only 9 final-answer items (`msg_01ef633e…` and `msg_07d724c3…`) and two command items (`exec-84b0552d…`, `exec-6d9dc924…`). None of the 12 inbound message IDs (`amsg_…`) or 11 outbound call IDs (`call_…`) appears in either file.
- **`inputs/previous_VISIBLE_REVIEWER_TRANSCRIPT.md`:** the 12 inbound records show only the routing wrapper, ending at an empty `Payload:`. All 11 outbound calls read `[Tool arguments unavailable; see exact omission ledger.]`.
- **`checks/INBOUND_NATIVE_RECHECK.json`:** all 12 entries have `fresh_plaintext_body_recovered: false`.
- **`checks/OUTPUT_GAP_RECHECK.json`:** `new_text_recovered: 0`.

## 2. Remaining gaps
| Category | Count | Detail |
|---|---|---|
| Inbound reviewer instructions | **12 of 12 unrecovered** | 9 new-task requests, 3 follow-up messages. Protocol review lines 13, 36, 57, 80, 108, 162, 178; report review lines 13, 34, 55, 68, 96. |
| Outbound `send_message` arguments, delivered | **10 unrecovered** | Protocol review lines 21, 44, 65, 88, 95, 132, 179; report review lines 19, 42, 83. |
| Outbound `send_message` arguments, aborted | **1 unrecovered** | Report review line 63, `call_5ef0f9495e984fbbb802bc57cf7bd6b1`. Its result record (line 65, transcript line 2126) reads `aborted before dispatch`. |
| Command output gap | **1 range, 6,178 characters** | `exec-84b0552d-5f11-464f-b396-05908175e4f9`, characters [20000, 26178) of 46,178. Characters [0, 20000) and [26178, 46178) are already covered. I did not rerun the command or reconstruct the text. |

**Total: 23 unrecovered message bodies (12 inbound + 10 delivered + 1 aborted) and one output range.** These are gaps that were already documented, not new data loss.

**Status conflict:** `inputs/OUTBOUND_GAPS.json` lists line 63 as `"native_status": "completed"`, but its line-65 result says `aborted before dispatch`. The "completed" status probably describes the call record, not delivery. I kept it separate as you asked.

## 3. Are the visible candidates good enough?
No. At most they are about the same topic.

- **The 9 fresh-API final answers** are separate items with their own IDs. They are the reviewers' replies, not the instructions they received or the messages they sent. Even where a turn matches, they are not exact counterparts.
- **8 of the outbound call IDs** appear in `inputs/previous_APP_EXPORT_COMPARISON.json` as matching saved app items (e.g. JSON lines 292 and 302 for `call_19d3992a…`). That only links the records to each other. The saved app items themselves are not in this directory, and nothing visible shows they contain readable arguments.
- **The other 3 outbound calls** (protocol lines 132 and 179, report line 63) have no saved app counterpart. That matches the "three encrypted-call metadata records" noted in `previous_README.md`.

## 4. Limitations
- I used only Read, Glob and Grep inside this directory. I did not open native session files, encrypted content, hidden reasoning, account data or solutions, and I made no network calls, ran no commands and wrote nothing.
- I didn't verify the native line hashes myself. They come from the supplied check files and receipts.
- I deliberately didn't print the full text of the `exec-84b0552d` command item.
- The four pin-audit exchanges and three progress messages belong to the Trojan chat's audit and are not counted here. Internal-metadata index counts are also not counted as missing messages.
