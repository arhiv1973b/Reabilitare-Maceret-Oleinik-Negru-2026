# CASE-MACHERET-1997-2026 Consolidated Legal Dossier

**Status:** Architectural phase complete
**Generated:** 2026-09-20
**Protocol:** TI-ULA / Jus Cogens / Erga Omnes

## Artifacts (local workspace)

| File | SHA-256 | Size |
|------|---------|------|
| CASE_MACHERET_1997_2026_DOSSIER.md | `bcd4927701824031535df4983ffb8c4891d817794a58b39366f27df157fd303a` | 11 298 B |
| CASE_MACHERET_1997_2026_DOSSIER.pdf | `b7830de88715a3a88be3ceab918bd2f16d0058d9f883a64972489305c035d9dd` | 38 327 B |
| CASE_MACHERET_1997_2026_DOSSIER.html | `82eb47f7f2e64c48ae35e119bfef08d05761c0770219e728496f5e496483432e` | 35 939 B |

## Contents
- NODE_LEGAL_BASIS_JUS_COGENS (Root of Trust)
- NODE_TORTURE_AND_COVERUP_1997_1998
- NODE_CONTINUING_CONSEQUENCES_1997_2026
- SUBNODE_PROPERTY_RESTITUTION_1977_2026
- NODE_ENTITY_ACCOUNTABILITY_NETWORK
- NODE_FINANCIAL_MODEL_1997_2026 (provisional 1 098 500 EUR)
- LINK_NON_REHABILITATION_JUS_COGENS
- LINK_ACCOUNTABILITY_TO_CONSEQUENCES

## Release instruction
Because the GitHub connector does not expose a create-release endpoint in this session, create the release manually:

```bash
gh release create v2.0.0-dossier \
  --title "CASE-MACHERET-1997-2026: Consolidated Legal Dossier" \
  --notes "Immutable evidence graph dossier generated via TI-ULA. Includes Jus Cogens framework, verified entities, and provisional financial model (1,098,500 EUR)." \
  CASE_MACHERET_1997_2026_DOSSIER.md \
  CASE_MACHERET_1997_2026_DOSSIER.pdf \
  CASE_MACHERET_1997_2026_DOSSIER.html
```

Or via GitHub web UI: Releases → Draft a new release → tag `v2.0.0-dossier`.
