const BASE_URL = "http://127.0.0.1:8000";  // Make sure FastAPI is running


export async function getUpcomingEvents() {
    const res = await fetch(`${BASE_URL}/events/upcoming`);
    return res.json();
}

export async function getPastEvents() {
    const res = await fetch(`${BASE_URL}/events/past`);
    return res.json();
}

export async function getEvents() {
    const res = await fetch("http://127.0.0.1:8000/events/");
    const events = await res.json();

    return events.map(event => ({
        ...event,
        date: formatToIST(event.date)  // Convert date to UTC+05:30
    }));
}

function formatToIST(utcDate) {
    const date = new Date(utcDate);
    return date.toLocaleString("en-IN", { timeZone: "Asia/Kolkata", hour12: false });
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
