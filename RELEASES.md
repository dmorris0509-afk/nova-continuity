# RELEASES.md

# Nova Release History

---

## v0.0 — Continuity Events

Status:
Released

Description:

Initial continuity substrate.

Capabilities:

* Event creation
* Event storage
* Timeline retrieval
* Event lineage reconstruction

Major Components:

* events table
* /events API
* /lineage API

Commit Era:

June 2026

---

## v0.1 — Receipts

Status:
Released

Description:

Validation layer added to continuity substrate.

Capabilities:

* Receipt issuance
* Receipt storage
* Receipt retrieval

Major Components:

* receipts table
* /receipts API

Commit Era:

June 2026

---

## v0.2 — File Continuity

Status:
Released

Description:

File operations become continuity-aware.

Capabilities:

* File.Opened events
* File.Saved events
* File history lineage
* File event tracking

Major Components:

* file_events table
* /file/open API
* /file/save API

Commit Era:

June 2026

Tag:

v0.2

---

## v0.3 — Decision Continuity

Status:
Planned

Description:

Decision Registry and architectural reasoning preservation.

Capabilities:

* Decision tracking
* Decision rationale
* Decision outcomes
* Decision lineage

Major Components:

* DECISION_REGISTRY.md

Branch:

feat/v0.3-decision-continuity

Commit Era:

June 2026

---

## Future Releases

v0.4 Replay

v0.5 Governance

v0.6 Federation

---

Core Principle:

Nova should be able to reconstruct not only what happened, but why it happened.

