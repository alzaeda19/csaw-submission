# Exact remaining AI-record gaps

**The previously missing 6,178-character output section is recovered. No known command-output character gap remains in the two audited outputs.** The ordinary message-body/argument gaps below remain unavailable.

This is the inventory of known gaps in the audited review records, not a claim that every historical conversation is complete. These omissions existed in the earlier sealed records; the 11 outgoing argument fields were omitted from earlier short summaries, not newly lost.

The [machine-readable ledger](ai/log_recovery_2026-11-13/MISSING_RECORDS.json) includes source paths, exact line numbers, timestamps, message/call IDs and provenance. The [recovery report](docs/AI_LOG_RECOVERY.md) documents the searches and authentic output recovery.

## Twelve incoming reviewer instructions

| Record | Reviewer | Native line | Kind | Message ID |
|---|---|---:|---|---|
| IN-P01 | protocol_review | 13 | NEW_TASK | `amsg_01a1d245-2b62-7b60-8bd1-86e43547510a` |
| IN-P02 | protocol_review | 36 | NEW_TASK | `amsg_01a1d248-c109-7071-9393-f1c41406bfff` |
| IN-P03 | protocol_review | 57 | NEW_TASK | `amsg_01a1d24d-7e64-7f53-814d-c0b885be00fa` |
| IN-P04 | protocol_review | 80 | NEW_TASK | `amsg_01a1d25a-fb63-7ce2-aeab-71b76337140c` |
| IN-P05 | protocol_review | 108 | NEW_TASK | `amsg_01a1d25d-98e6-73c0-9d3c-8179979a699f` |
| IN-P06 | protocol_review | 162 | MESSAGE | `amsg_01a1d260-21e4-7b93-a9f5-b356d72df6ab` |
| IN-P07 | protocol_review | 178 | MESSAGE | `amsg_01a1d260-8118-7c73-9fc6-3da934009774` |
| IN-R01 | report_review | 13 | NEW_TASK | `amsg_01a1d245-3bf3-7282-89a5-e7ab67a1fb08` |
| IN-R02 | report_review | 34 | NEW_TASK | `amsg_01a1d247-4cff-7e33-abbd-3769096958e2` |
| IN-R03 | report_review | 55 | NEW_TASK | `amsg_01a1d25b-1302-7551-a4c7-e1d7db7afdb4` |
| IN-R04 | report_review | 68 | MESSAGE | `amsg_01a1d25b-7350-76e3-a76c-5414aed97470` |
| IN-R05 | report_review | 96 | NEW_TASK | `amsg_01a1d25f-d122-7db0-8c5d-d97ce2949ac0` |

These are nine task requests and three steering messages. Routing wrappers are retained; their ordinary bodies are opaque and do not appear in the normal API projections.

## Eleven outgoing reviewer-call argument fields

| Record | Reviewer | Native line | Call ID | Dispatch evidence |
|---|---|---:|---|---|
| OUT-P01 | protocol_review | 21 | `call_19d3992a8fbf4734bc74853e44db8222` | Completed call; empty output receipt |
| OUT-P02 | protocol_review | 44 | `call_339e27886fbd4cc2916066a2277aa61d` | Completed call; empty output receipt |
| OUT-P03 | protocol_review | 65 | `call_a1b80aa89ab84051ab4fd45f0278ea29` | Completed call; empty output receipt |
| OUT-P04 | protocol_review | 88 | `call_d915ad0a8d4d428cba2d1299e8a5356f` | Completed call; empty output receipt |
| OUT-P05 | protocol_review | 95 | `call_9b3eefdb992f438db087cc98a4e31f1f` | Completed call; empty output receipt |
| OUT-P06 | protocol_review | 132 | `call_e81664e6ad8b44c0ae8c04b31ec6776a` | Completed call; empty output receipt |
| OUT-P07 | protocol_review | 179 | `call_8957e443f9f2463688009dcd07f88fba` | Completed call; empty output receipt |
| OUT-R01 | report_review | 19 | `call_9900f5093bb74bcd98a4ccfe7a2a39ce` | Completed call; empty output receipt |
| OUT-R02 | report_review | 42 | `call_305463d629114b7792565742cccbbbd6` | Completed call; empty output receipt |
| OUT-R03 | report_review | 63 | `call_5ef0f9495e984fbbb802bc57cf7bd6b1` | Aborted before dispatch |
| OUT-R04 | report_review | 83 | `call_8bb06266c1d74b9eac7fcbc2d757fec2` | Completed call; empty output receipt |

These are separate from the incoming instructions. One call was explicitly aborted before dispatch. Empty receipts for the other ten do not independently prove delivery. Separate final answers are preserved but cannot substitute for these missing arguments without exact identity-matched text.

## Seven pin-audit message exchanges

| Record | Type | Parent line | Peer line | Message or call ID |
|---|---|---:|---:|---|
| PIN-I1 | initial delegation | 1522 | 13 | `amsg_01a1d2a9-6048-7001-a132-d24debfaa320` |
| PIN-I2 | metadata-only clarification | 1556 | 60 | `amsg_01a1d2a9-f6e9-7320-a28e-57c12247912c` |
| PIN-I3 | final visual-review request | 1674 | 76 | `amsg_01a1d2ac-64f8-7702-b394-8276a197abd7` |
| PIN-I4 | exact-path clarification | 1688 | 99 | `amsg_01a1d2ac-bb5d-7ef0-8d82-52ebe659800e` |
| PIN-P1 | peer progress message | 1538 | 31 | `call_b8d9ba29ee544e048b28780a44e8eff8` |
| PIN-P2 | peer progress message | 1553 | 47 | `call_13146faa462946c98dba080b9c1fbcc5` |
| PIN-P3 | peer progress message | 1685 | 86 | `call_b87eacd723b742dbb74a7ab0c11978ca` |

Four instructions and three progress messages are counted once per exchange, even though both endpoints have records. The two peer final responses are available. Hidden reasoning, internal metadata and deliberately excluded unrelated material are not counted as missing ordinary messages.

## Counts and status

- 12 unavailable incoming reviewer instruction bodies.
- 11 unavailable outgoing reviewer argument fields, including one aborted call.
- 4 unavailable pin-review instructions and 3 unavailable pin-review progress messages.
- 0 remaining character gaps in the two audited command outputs.

**30 indexed unavailable records remain.** This number describes categories of records, including an aborted call; it is not a count of 30 confirmed delivered messages. No absent content was invented. The exact generation-log requirement and staff acceptance remain unestablished.
