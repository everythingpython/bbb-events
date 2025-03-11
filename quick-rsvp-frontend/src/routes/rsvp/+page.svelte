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

<div class="min-h-screen flex items-center justify-center bg-parchment">
    <div class="bg-white shadow-lg rounded-lg p-8 max-w-lg w-full">
        <h1 class="text-4xl font-serif text-center text-bookBrown">✍️ RSVP for an Event</h1>
        <p class="text-center text-gray-600 mt-2">Secure your spot for an upcoming discussion.</p>

        <form class="space-y-4 mt-4" on:submit|preventDefault={handleSubmit}>
            <div>
                <label class="block text-gray-700 font-medium">Name:</label>
                <input type="text" bind:value={name} required
                    class="w-full border border-gray-300 rounded-lg px-3 py-2 focus:outline-none focus:ring-2 focus:ring-blue-500"/>
            </div>

            <div>
                <label class="block text-gray-700 font-medium">Email:</label>
                <input type="email" bind:value={email} required
                    class="w-full border border-gray-300 rounded-lg px-3 py-2 focus:outline-none focus:ring-2 focus:ring-blue-500"/>
            </div>

            <button type="submit"
                class="w-full bg-blue-500 text-white py-2 rounded-lg hover:bg-blue-600 transition">
                📩 Submit RSVP
            </button>
        </form>
    </div>
</div>
