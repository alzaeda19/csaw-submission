I found **no recovered bodies in these sources.** 0 of 30 gaps are recovered. The new history check found 17 rows by exact ID, but every one holds metadata only.

I read the five named files and checked the rest of the directory. `CLAUDE_BRIEF.md` repeats your instructions. `checks/COMMAND_EVENT_RECOVERY.json`, the file that records the earlier command-output recovery, is not in this directory. I can't re-verify that gain, but nothing here counts it again: the baseline lists 0 missing output ranges. I ran no queries; every database result below comes from Codex's receipts.

## What the new sources cover

**Counts add up.** 12 inbound + 11 outgoing + 4 pin instructions + 3 pin progress = 30. The 44 IDs queried are also accounted for: 23 for the inbound and outgoing gaps, plus 21 for the pin exchanges, which are recorded at both ends.

**Exact-ID check on the history database (`thread_history_1.sqlite`):**
- **17 rows found, 0 bodies.** They cover 10 of the 11 outgoing calls and the 7 pin calls. Every row has `item_type = subAgentActivity` and only these fields: `type, model, reasoningEffort, id, kind, agentThreadId, agentPath`. `ordinary_text_field_present` is false for all of them.
- **27 IDs not found:** all 19 `amsg_*` messages (the 12 inbound plus the 7 pin message ends), all 7 `fc_*` IDs, and `call_5ef0…` (OUT-R03). That one is the aborted call, so a missing row is expected.
- **13 gaps have no row at all:** IN-P01…P07, IN-R01…R05 and OUT-R03.
- **Caveats:**
  - The `field_names` list may cover only top-level keys. The receipt doesn't say whether nested values were checked for text.
  - The receipt only reports matches from `thread_items`. It doesn't confirm that `thread_realtime_items` was searched.
  - An inbound message may be stored under a different item ID on the receiving side, so "no match" only means no row has that exact ID.

**Communication metadata:** the 62 records across the 4 session files hold only `trigger_turn`, and no body.

**Thread metadata:** this is a list of columns only, so no values were read. `first_user_message`, `preview`, `title`, `name` and `thread_attachments.payload` haven't been looked at. Even if they hold text, it may be shortened or derived and must not be treated as a full original prompt.

**Inventory:** the migration and transcript-import folders are empty. `vendor_imports` holds a skills cache, which is not relevant. The single archived session (Sep 2026) predates this work and wasn't opened.

## What must be true before a candidate counts as recovered
1. **Same identity:** the candidate carries the exact `message_id` or `call_id`. Otherwise it needs a fixed link to the exact record: same `thread_id` and `turn_id`, a position that maps to the same original log line, and a timestamp matching to the millisecond. Matching on a time window or on similar content is not enough.
2. **Trustworthy origin:** it was written by ordinary app storage, not by a model summary or a re-run. It was read through read-only access, and the receipt names the database file, table, column, row key and the item's hash.
3. **Complete text:** the field is meant to hold the full body, not a title or preview. It shows no signs of being cut off (an ellipsis or a length cap). The original line sizes are only a loose sanity check because the encoding inflates the stored body.
4. **Pin exchanges:** recover each end of the pair separately. If both ends are found, they must match exactly. Text from one end alone doesn't recover the pair unless the counting rule allows that.
5. **Not derived from the opaque bodies:** the text must not come from decoding them in any way.
6. **OUT-R03 (aborted):** any text found is a draft that was never sent, so label it separately.

Report found rows and recovered bodies as separate numbers.

## Suggested next checks (at most three, read-only)
1. **Inbound turns, by exact turn ID.** For the 12 inbound gaps, look up `thread_turns` using the given thread and `turn_id`. Then fetch the matching `thread_items` row by exact `first_user_item_id` and also check `thread_realtime_items`. First report only the item type, field names (including nested ones), text length and hash. Count a row only if it ties back to the specific message ID and timestamp. This matters most for turns with several messages (IN-P05/06/07, IN-R03/04), where the first item may belong to a different message.
2. **Thread metadata for the three receiving threads.** Read `first_user_message`, `preview`, `title`, `name`, any matching `thread_spawn_edges` row and `thread_attachments.payload` for `01a1d245-26de…`, `01a1d245-3808…` and `01a1d2a9-5b06…`. Record each value's length and hash. At most these could match the first task in each thread (IN-P01, IN-R01, PIN-I1 message end), and only if criteria 1–3 are met. Treat any text as a lead until then.
3. **Nested fields in the 17 found rows.** For the 17 matched rows, list all nested keys and check whether `agentThreadId` points to the expected receiving thread. This can confirm routing, not recover a body. Optionally, list the item types (not contents) in each receiving thread's history within ±2 seconds of each gap's timestamp. Any candidate must still pass criterion 1 by exact link, not by closeness in time.

These checks only bound what this directory and these tables show. They don't prove the bodies are unrecoverable from every source. Final supplemental results from the main audit may not be here yet.
