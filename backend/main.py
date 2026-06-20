import uuid
import time
import sqlite3

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Database

conn = sqlite3.connect("events.db", check_same_thread=False)
cur = conn.cursor()

# Events Table

cur.execute("""
CREATE TABLE IF NOT EXISTS events (
    id TEXT PRIMARY KEY,
    timestamp INTEGER NOT NULL,
    name TEXT NOT NULL,
    parentId TEXT
)
""")

# Receipts Table

cur.execute("""
CREATE TABLE IF NOT EXISTS receipts (
    id TEXT PRIMARY KEY,
    eventId TEXT NOT NULL,
    status TEXT NOT NULL,
    details TEXT NOT NULL
)
""")
# File Events Table

cur.execute("""
CREATE TABLE IF NOT EXISTS file_events (
    id TEXT PRIMARY KEY,
    eventId TEXT NOT NULL,
    path TEXT NOT NULL,
    timestamp INTEGER NOT NULL
)
""")
conn.commit()


# Create Event

@app.post("/events")
def create_event(name: str, parentId: str | None = None):
    event_id = str(uuid.uuid4())
    timestamp = int(time.time())

    cur.execute(
        """
        INSERT INTO events (id, timestamp, name, parentId)
        VALUES (?, ?, ?, ?)
        """,
        (event_id, timestamp, name, parentId)
    )

    conn.commit()

    return {
        "id": event_id,
        "timestamp": timestamp,
        "name": name,
        "parentId": parentId,
    }


# Timeline

@app.get("/events")
def list_events():
    rows = cur.execute(
        """
        SELECT id, timestamp, name, parentId
        FROM events
        ORDER BY timestamp ASC
        """
    ).fetchall()

    return [
        {
            "id": row[0],
            "timestamp": row[1],
            "name": row[2],
            "parentId": row[3],
        }
        for row in rows
    ]


# Lineage

@app.get("/lineage/{event_id}")
def get_lineage(event_id: str):
    query = """
    WITH RECURSIVE lineage(id, timestamp, name, parentId) AS (
        SELECT id, timestamp, name, parentId
        FROM events
        WHERE id = ?

        UNION ALL

        SELECT e.id, e.timestamp, e.name, e.parentId
        FROM events e
        JOIN lineage l
            ON e.id = l.parentId
    )
    SELECT * FROM lineage;
    """

    rows = cur.execute(query, (event_id,)).fetchall()

    return [
        {
            "id": row[0],
            "timestamp": row[1],
            "name": row[2],
            "parentId": row[3],
        }
        for row in rows
    ]


# Issue Receipt

@app.post("/events/{event_id}/receipt")
def issue_receipt(
    event_id: str,
    status: str = "PASS",
    details: str = "Receipt issued",
):
    receipt_id = str(uuid.uuid4())

    cur.execute(
        """
        INSERT INTO receipts (id, eventId, status, details)
        VALUES (?, ?, ?, ?)
        """,
        (receipt_id, event_id, status, details),
    )

    conn.commit()

    return {
        "id": receipt_id,
        "eventId": event_id,
        "status": status,
        "details": details,
    }


# View Receipts

@app.get("/receipts")
def list_receipts():
    rows = cur.execute(
        """
        SELECT id, eventId, status, details
        FROM receipts
        """
    ).fetchall()

    return [
        {
            "id": row[0],
            "eventId": row[1],
            "status": row[2],
            "details": row[3],
        }
        for row in rows
    ]
# File Open

@app.post("/file/open")
def open_file(path: str):
    timestamp = int(time.time())

    event_id = str(uuid.uuid4())

    cur.execute(
        """
        INSERT INTO events (id, timestamp, name, parentId)
        VALUES (?, ?, ?, ?)
        """,
        (event_id, timestamp, "File.Opened", None)
    )

    file_event_id = str(uuid.uuid4())

    cur.execute(
        """
        INSERT INTO file_events (id, eventId, path, timestamp)
        VALUES (?, ?, ?, ?)
        """,
        (file_event_id, event_id, path, timestamp)
    )

    conn.commit()

    try:
        with open(path, "r") as f:
            content = f.read()
    except FileNotFoundError:
        content = ""

    return {
        "eventId": event_id,
        "path": path,
        "content": content
    }
# File Save

# File Save

@app.post("/file/save")
def save_file(path: str, content: str):
    timestamp = int(time.time())

    with open(path, "w") as f:
        f.write(content)

    row = cur.execute(
        """
        SELECT eventId
        FROM file_events
        WHERE path = ?
        ORDER BY timestamp DESC
        LIMIT 1
        """,
        (path,)
    ).fetchone()

    parent_id = None

    if row:
        parent_id = row[0]

    event_id = str(uuid.uuid4())

    cur.execute(
        """
        INSERT INTO events (id, timestamp, name, parentId)
        VALUES (?, ?, ?, ?)
        """,
        (event_id, timestamp, "File.Saved", parent_id)
    )

    file_event_id = str(uuid.uuid4())

    cur.execute(
        """
        INSERT INTO file_events (id, eventId, path, timestamp)
        VALUES (?, ?, ?, ?)
        """,
        (file_event_id, event_id, path, timestamp)
    )

    conn.commit()

    return {
        "eventId": event_id,
        "path": path,
        "status": "saved",
        "parentId": parent_id
    }
