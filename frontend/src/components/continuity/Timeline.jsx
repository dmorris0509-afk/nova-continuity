import { useEffect, useState } from "react";

export default function Timeline() {
  const [events, setEvents] = useState([]);

  useEffect(() => {
    fetch("http://127.0.0.1:8000/events")
      .then((res) => res.json())
      .then((data) => setEvents(data))
      .catch((err) => console.error(err));
  }, []);

  return (
    <div>
      <h2>Timeline</h2>

      {events.map((event) => (
        <div key={event.id}>
          <strong>{event.name}</strong>
          <br />
          <small>{event.id}</small>
        </div>
      ))}
    </div>
  );
}
