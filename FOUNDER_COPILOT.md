# NOVA_FOUNDER_COPILOT_V1.md

## Mission

Nova Founder Copilot is a continuity-native assistant designed to preserve founder memory, architectural decisions, project lineage, and execution history.

Purpose:

Prevent loss of context.

Preserve decision history.

Provide recall, reconstruction, and guidance across the entire Nova ecosystem.

---

# Core Capability 1 — Founder Memory

Store:

* Founder discussions
* Major decisions
* Architecture decisions
* Strategic choices
* Milestone approvals

Example:

Question:

"What was our reasoning for Replay Layer?"

Response:

* Decision Summary
* Decision Date
* Participants
* Related Documents
* Related Commits

---

# Core Capability 2 — Architecture Recall

Question:

"Show continuity evolution."

Response:

v0.0 Events

v0.1 Receipts

v0.2 File Continuity

v0.3 Decision Continuity

v0.4 Replay

v0.5 Governance

---

# Core Capability 3 — Decision Registry

Decision Record

Decision {
id
timestamp
title
rationale
alternatives
participants
outcome
references
}

Example:

Decision:
Runtime Separation

Outcome:
Substrate, Runtime, Governance, Operator Surface

Status:
Accepted

---

# Core Capability 4 — Founder Meeting Recorder

Input:

Meeting Notes

Output:

Summary

Action Items

Open Questions

Risks

Decisions

Continuity Events

---

# Core Capability 5 — GitHub Awareness

Ingest:

Commits

Branches

Tags

Pull Requests

Output:

Weekly Project Summary

Example:

This Week:

* 4 commits
* 1 new branch
* v0.2 completed
* Cockpit UI added

---

# Core Capability 6 — Continuity Search

Questions:

"What changed after v0.1?"

"Why did we choose lineage?"

"What is unresolved?"

Returns:

* Documents
* Decisions
* Commits
* Events

---

# Initial Data Model

FounderEvent {
id
timestamp
type
title
content
author
}

FounderDecision {
id
title
rationale
outcome
participants
timestamp
}

FounderAction {
id
task
owner
status
dueDate
}

---

# MVP Screens

1. Founder Dashboard

* Recent Events
* Open Decisions
* Active Branches

2. Decision Registry

* Accepted
* Pending
* Rejected

3. Timeline

* Events
* Commits
* Decisions

4. Search

* Architecture Search
* Founder Search

---

# Future Evolution

v0.2
Decision Intelligence

v0.3
Replay Workspace

v0.4
Governance Runtime

v0.5
Federation

---

Core Principle:

Nova should be capable of remembering the creation of Nova itself.

