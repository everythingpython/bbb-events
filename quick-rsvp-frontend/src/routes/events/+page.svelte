<script>
    import { onMount } from "svelte";
    import { getEvents } from "$lib/api.js";

    let events = [];

    onMount(async () => {
        events = await getEvents();
        console.log("Fetched events:", events);  // Debugging
    });
</script>

<h1 class="text-3xl font-bold text-blue-600">Upcoming Events</h1>

{#if events.length > 0}
    <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6 p-6">
        {#each events as event}
            <div class="bg-white shadow-md rounded-lg p-5 border border-gray-200 hover:shadow-xl transition">
                <h3 class="text-xl font-semibold text-blue-600">{event.name}</h3>
                <p class="text-gray-600">{event.description}</p>
                <p class="text-gray-700 mt-2"><strong>Date:</strong> {event.date}</p>
                <p class="text-gray-700"><strong>Location:</strong> {event.location}</p>
            </div>
        {/each}
    </div>
{:else}
    <p class="text-gray-600 text-center mt-10">No events available.</p>
{/if}


