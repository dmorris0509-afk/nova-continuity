# Acceptance Tests

## v0.0 — Continuity Exists

### Test 1: Create Event
Steps:
1. POST /events?name=RootEvent

Expected:
- Event is created
- Event receives a unique ID
- Event is persisted

Status: PASSED ✅

---

### Test 2: Timeline Retrieval
Steps:
1. Create an event
2. GET /events

Expected:
- Event appears in timeline output

Status: PASSED ✅

---

### Test 3: Lineage Traversal
Steps:
1. Create RootEvent
2. Create ChildEvent with parentId=RootEvent.id
3. GET /lineage/{ChildEvent.id}

Expected:
- ChildEvent returned
- RootEvent returned
- Correct parent-child chain reconstructed

Status: PASSED ✅

---

## v0.1 — Receipts

Status: NOT IMPLEMENTED

---

## v0.2 — File Continuity

Status: NOT IMPLEMENTED

---

## Current Acceptance Summary

- [x] Create Event
- [x] View Timeline
- [x] Inspect Lineage
- [ ] Issue Receipt
- [ ] View Receipts
- [ ] Open File
- [ ] Save File
- [ ] File Save Creates Event
- [ ] File History Forms Lineage

Continuity Proof:

RootEvent
  ↑
ChildEvent

Event → Timeline → Lineage

Status: v0.0 PASSED
Date: 2026-06-20
