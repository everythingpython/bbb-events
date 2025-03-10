<script>
    import { page } from "$app/stores";
    import { submitRSVP } from "$lib/api.js";

    let name = "";
    let email = "";
    let eventId = "";

    $: eventId = new URLSearchParams($page.url.search).get("eventId") || "";

    async function handleSubmit() {
        if (!name || !email || !eventId) return alert("All fields are required");
        const response = await submitRSVP(name, email, eventId);
        alert("RSVP successful!");
    }
</script>

<h1>RSVP for Event</h1>
<form on:submit|preventDefault={handleSubmit}>
    <label>
        Name:
        <input type="text" bind:value={name} required />
    </label>
    <label>
        Email:
        <input type="email" bind:value={email} required />
    </label>
    <button type="submit">Submit</button>
</form>
