<script>
    import { onMount } from "svelte";
    import { getPastEvents } from "$lib/api.js";

    let pastEvents = [];

    onMount(async () => {
        pastEvents = await getPastEvents();
    });
</script>

<div class="fixed inset-0 flex flex-col justify-center items-center bg-cover bg-center"
    style="background-image: url('https://images.unsplash.com/photo-1591951425328-48c1fe7179cd'); background-size: cover; background-position: center;">
    
    <!-- Warm parchment-like gradient overlay -->
    <div class="absolute inset-0 bg-gradient-to-b from-transparent via-[#f5e1c0]/50 to-[#d2b48c]/70"></div>

    <!-- Centered Content Wrapper -->
    <div class="relative z-10 w-full max-w-6xl px-8 py-12 text-center">
        <h1 class="text-5xl font-serif text-gray-900">📚 Past Events</h1>
        <p class="text-lg text-gray-700 mt-4">
            A look back at our most memorable book discussions.
        </p>

        <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8 mt-10 w-full">
            {#each pastEvents as event}
                <div class="bg-[#f5e1c0] bg-opacity-90 shadow-lg rounded-lg p-6 border border-gray-300 hover:shadow-xl transition">
                    <h3 class="text-2xl font-serif text-gray-900">{event.name}</h3>
                    <p class="text-gray-700 mt-2">{event.description}</p>
                    <p class="text-gray-800 mt-2"><strong>Date:</strong> {event.date}</p>
                    <p class="text-gray-800"><strong>Location:</strong> {event.location}</p>
                </div>
            {/each}
        </div>
    </div>
</div>
