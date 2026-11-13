# Corrigendum to Independent Review — CSAW Evaluation (2026-11-13)

The original review remains preserved. The following corrections are accepted on the basis of the frozen source packet as cited. No reinterpretation of "not established" as proof of the opposite is made.

## Accepted Corrections

1. **Trojan trigger location.** `modified_wrapper.sv` increments `read_count` via nonblocking assignment from 0→1 on the first extraction edge, sampled 1 ns later. With `transfer()` calling `pulse(expected_flip)` at `k==bits_n-1` on the first read bit, the `read_count==1` XOR flips the **first sampled MSB**, not the second extraction bit. My original description of the affected bit is corrected accordingly.

2. **Detector label matrix.** Correct labels (clean/modified order) are:
   - HT1: CLEAN / CLEAN
   - HT2: CLEAN / TROJAN
   - HT3: CLEAN / CLEAN
   - HT4: TROJAN / TROJAN
   
   Exactly **two** detectors (HT1, HT3) miss the modified member; HT4 falsely flags the clean member. My statement that "three of four models miss the real Trojan at least once" is **withdrawn as incorrect**.

3. **Overhead status.** `overhead.json` reports `negligible_overhead_established=false`. This means negligible overhead is **not established**. It does **not** establish that overhead is non-negligible against any threshold; no accepted numerical threshold is present. Per-resource increases are measured only. Any wording in my review implying proven non-negligible overhead is corrected.

4. **Scope of phase.** The phase is **simulation-only**; hardware execution is not required. The future-board pin audit and reproduction sequence are forward-looking; absence of physical testing is a **stated limitation**, not a missing mandatory deliverable. Numeric key recovery is optional bonus. Full automation and negligible overhead are scoring targets; stealth remains part of the objective.

5. **Artifact completeness.** All artifact categories are present. Historical log completeness and stealth remain **unestablished** (not disproven). Normal-operation evidence is protocol-scoped. Staff access remains to be arranged per user preference; no model judgment can guarantee staff acceptance.

## Corrected Conclusion

The Trojan is confined to a single-bit flip on the first sampled MSB (correction 1). Detector performance shows two misses on the modified member and one false positive on the clean member (correction 2), not the broader miss rate previously stated. Overhead is characterized by measured per-resource increases with negligibility **not established** — neither confirmed nor refuted (correction 3). The evaluation is correctly framed as simulation-only, with physical testing a declared limitation rather than an outstanding mandatory item (correction 4). All artifact categories exist; stealth and historical-log completeness remain open, and staff access is pending arrangement (correction 5). These corrections narrow and sharpen the findings without altering the core outcome that a functional Trojan is present and is inconsistently detected.
