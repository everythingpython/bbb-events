const BASE_URL = "http://127.0.0.1:8000";  // Make sure FastAPI is running

export async function getPastEvents() {
    const res = await fetch(`${BASE_URL}/events/past`);
    return res.json();
}

export async function getEvents() {
    const res = await fetch(`${BASE_URL}/events/`);
    if (!res.ok) {
        console.error("Error fetching events:", res.status);
        return [];
    }
    return res.json();
}

export async function submitRSVP(name, email, eventId) {
    const res = await fetch(`${BASE_URL}/rsvp/`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ name, email, event_id: eventId }),
    });

    if (!res.ok) {
        console.error("RSVP failed:", res.status);
        return null;
    }
    return res.json();
}
