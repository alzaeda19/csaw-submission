# CSAW follow-up audit: recovery of the 30 indexed gaps (read-only)

**None of the 30 indexed gaps is recovered.** The new receipts and the Jarvis captures add some early planning history, but no exact message or call ID in them matches any of the 44 target IDs.

## 1. Recovery counts

| Category | Indexed | Recovered | What exists instead |
|---|---|---|---|
| Inbound reviewer instructions (IN-P01…07, IN-R01…05) | 12 | **0** | Each turn row exists, but `first_user_item_id` is null in all 12 and no exact-ID item row was found |
| Outgoing reviewer arguments (OUT-P01…07, OUT-R01…04) | 11 | **0** | 10 metadata-only rows. OUT-R03 (aborted call) has no row |
| Pin-audit instructions (PIN-I1…I4) | 4 | **0** | Both ends found in the earlier exports. They hold only short routing labels (82–83 characters) or no text fields |
| Pin-audit progress messages (PIN-P1…P3) | 3 | **0** | Same as the pin-audit instructions |
| **Total** | **30** | **0** | |

Supporting counts:
- **Exact-ID search of the 44 target IDs:** 17 rows found, 27 not found, 0 message bodies. All 17 found rows are `subAgentActivity` items with no nested containers. No rows were found in `thread_realtime_items`.
- **The 14 pin-message endpoint records:** all 14 found. None is marked as possibly containing a plaintext body, and 0 message bodies were recovered.
- **Jarvis captures:** 61 rows (34 + 27), 60 unique IDs. One ID (`Sentinel_1dcfe7d2…`) appears in both excerpts, and one row is the "Loading" placeholder. That leaves 59 real messages, with 0 matching a target ID.
- **Planning task capture:** 5 turns, 17 agent messages and 2 browser tool calls. 0 match a target ID.
- **Thread metadata for the three threads that received the messages:** the first message, title and preview fields are all empty (0 characters), names are null, there are no attachments, and `has_user_event = 0`. The only thread links found are spawn edges from the parent session.

The Jarvis and planning records also can't close a gap on timing. The planning task ran on 5 Nov 2026, about 12:57–13:31 UTC. All 30 gaps fall between 00:18 and 02:11 UTC on 13 Nov. Their IDs also use a different format (`CalpicoMessage~Sentinel_…` and `msg_…` instead of the target `amsg_`/`call_`/`fc_` IDs).

## 2. Who checked what

**Codex produced these, and I relied on them without re-running anything:** all 12 files in `checks/*.json`, the hashes and source lines for the Jarvis captures, and the byte-for-byte copy claim for the four planning files. I did not query SQLite, open native rollout files (they are outside this directory) or recompute any SHA-256 hash.

**I checked these myself with Read and Grep:**
- I read every file you listed, plus the inputs, `CLAUDE_FINAL_AUDIT.md` and my previous `response.md`.
- I counted the `message_id` entries: 34 + 27 = 61. I confirmed the one duplicate ID and the one "Loading" row.
- I searched `recovered/` for all 44 target IDs by prefix, and for the two receiving-thread prefixes `01a1d245` and `01a1d2a9`. There were 0 matches.
- The arithmetic across the receipts is consistent:
  - 12 + 11 + 4 + 3 = 30 gaps.
  - 44 IDs = 12 + 11 + 21 (seven pin exchanges × three IDs each).
  - 17 found + 27 not found = 44.
  - The 20 matched export files reduce to 17 unique hashes. 18 are identical to packaged files and 2 are the original pin-audit exports.
  - 46 + 7 + 5 + 4 = 62 communication-metadata records, each holding only `trigger_turn`.
- I converted the planning task's epoch timestamps to dates.

**The hash correction** is internally consistent. The first check compared hashes that include line endings with old hashes that exclude them, and wrongly stopped. Once both conventions were applied to the same original bytes, all 14 endpoints matched both ways, and no file was changed. This was a mismatch in how the hashes were computed, not evidence that a file was altered. I did not recompute the hashes myself.

## 3. Limitations

- **Jarvis:** these are two selected excerpts read from the rendered page, not a full export. Times are on-screen labels with no dates. In the follow-up excerpt they are out of order and span several days.
- **Planning task:** reasoning, transfer credentials and most tool records were left out. **Claude's actual three-agent planning output** (`CSAW_AHA_Qualifier_Plan.md` and the agent transcripts) **is not in this directory.** Any claim that "Claude switched from Fable 5.1 to Opus 4.8" or "ran 3 agents" is Codex reporting what it saw on screen, not a captured Claude record.
- **Of the two browser-entered prompts, only one was verified as sent:**
  - `call_53f1…` has status **failed**, and the turn's summary says "No Send action was taken."
  - `call_06e4…` completed and was reported "sent once."
- **OUT-R03:** the missing row is a recorded absence only. Why it is missing is not proven. My previous response called it "expected"; that wording should be dropped.
- **Pin counting:** my previous rule that one endpoint alone doesn't recover a pair was too strict. An authentic, stable body from either end would count if its identity is established. In practice no such body exists at either end.
- `checks/COMMAND_EVENT_RECOVERY.json` is cited by the baseline file but is not in this directory, so I still can't confirm the earlier command-output recovery.

## 4. Factual corrections for a public-facing short report

No public-facing report is in this directory, so I can't check its exact wording. Any version should say the following:

1. **"0 of 30 indexed gaps recovered."** Don't call the Jarvis or planning material "partial recovery" or say a gap is closed because the topic matches.
2. Describe the Jarvis material as **selected excerpts** (61 rows, 60 unique, 1 placeholder), not a full log. It includes many refusals: from 8:58 AM in the follow-up excerpt onward, Jarvis declined further Trojan-building or coordination help. Don't suggest Jarvis directed later implementation.
3. **Published-solution caveat:**
   - Jarvis's early plan said to "document what comes from the published solution."
   - The prompt sent to Claude did not exclude the solution.
   - Codex then told Claude to keep "using those versus independent recovery as conditional paths."
   - The later user instruction ("don't look at solutions") and both later agent briefs exclude it, along with "prior solution-based planning."
   - This shows neither that the final hardware used a solution nor that all early planning avoided one. Claude's early plan itself isn't available to check.
4. **UNTAM'D** was a proposed fictional framing. The handshake sequence, encoding and payload were explicitly left undecided. These records don't show it was implemented.
5. **Agent runs:** as of these records, Claude Code was signed out and "no new agents ran" for the two-agent setup. The three-agent run happened in the Claude web app, and its output isn't captured here.
6. **Completeness of AI logs:** the qualifier requires complete AI interaction logs. The Jarvis conversation shaped design choices (the backdoor option and the UNTAM'D letters) but is only partly captured. The follow-up excerpt also records the user asking that this conversation not be added to the logs. The report should not call the AI logs complete for all interactions unless that claim is limited in scope.
7. All current technical claims still have to rest on the existing submission evidence, not on these planning records.

## 5. Remaining unchecked source in this directory

Nothing left in this directory could plausibly hold a target body. The only material gaps are:
- `checks/COMMAND_EVENT_RECOVERY.json`, which is referenced but missing;
- the public-facing report itself, which wasn't supplied.

I don't recommend more searching here.
