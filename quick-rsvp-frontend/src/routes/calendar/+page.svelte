<script>
    import { onMount } from "svelte";
    import { getPastEvents } from "$lib/api.js";

    let pastEvents = [];

    onMount(async () => {
        pastEvents = await getPastEvents();
    });
</script>

<h1 class="text-3xl font-bold text-center text-gray-800 mt-6">Past Events</h1>

<div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6 p-6">
    {#each pastEvents as event}
        <div class="bg-white shadow-md rounded-lg p-5 border border-gray-200">
            <h3 class="text-xl font-semibold text-gray-800">{event.name}</h3>
            <p class="text-gray-600">{event.description}</p>
            <p class="text-gray-700 mt-2"><strong>Date:</strong> {event.date}</p>
            <p class="text-gray-700"><strong>Location:</strong> {event.location}</p>
        </div>
    {/each}
</div>
