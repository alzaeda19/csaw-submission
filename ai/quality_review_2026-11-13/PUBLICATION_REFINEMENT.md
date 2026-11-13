# Packaging verification refinement

The first post-push check of commit 762d255 found four historical Python bytecode files present in Git but excluded from the regenerated manifest and ZIP by an overbroad cache filter. They belong to the preserved cipher-reconstruction addendum and were included in the original copy provenance. No such historical file was deleted or executed.

The packaging filter was corrected to retain every original provenance-listed file, including these four sealed historical cache files, while excluding newly generated caches. The ZIP was rebuilt and all original-copy hashes were checked inside the ZIP as well as on disk. This packaging error did not change hardware or the simulation/verifier test outcomes. The initial failed integrity check and correction are recorded here rather than presented as a clean first attempt.
