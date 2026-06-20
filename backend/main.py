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

cur.execute("""
CREATE TABLE IF NOT EXISTS events (
    id TEXT PRIMARY KEY,
    timestamp INTEGER NOT NULL,
    name TEXT NOT NULL,
    parentId TEXT
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
        "parentId": parentId
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
            "parentId": row[3]
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
            "parentId": row[3]
        }
        for row in rows
    ]
