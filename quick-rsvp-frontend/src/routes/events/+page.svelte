<script>
    import { onMount } from "svelte";
    import { getUpcomingEvents } from "$lib/api.js";

    let upcomingEvents = [];

    onMount(async () => {
        upcomingEvents = await getUpcomingEvents();
    });
</script>
<div class="fixed inset-0 flex flex-col justify-center items-center bg-cover bg-center"
    style="background-image: url('https://images.unsplash.com/photo-1591951425328-48c1fe7179cd'); background-size: cover; background-position: center;">
    
    <!-- Warm parchment-like gradient overlay -->
    <div class="absolute inset-0 bg-gradient-to-b from-transparent via-[#f5e1c0]/50 to-[#d2b48c]/70"></div>

    <!-- Centered Content Wrapper -->
    <div class="relative z-10 w-full max-w-6xl px-8 py-12 text-center">
        <h1 class="text-5xl font-serif text-gray-900">📅 Upcoming Events</h1>
        <p class="text-lg text-gray-700 mt-4">
            Discover and RSVP for our next book discussions!
        </p>

        <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8 mt-10 w-full">
            {#each upcomingEvents as event}
                <div class="bg-[#f5e1c0] bg-opacity-90 shadow-lg rounded-lg p-6 border border-gray-300 hover:shadow-xl transition">
                    <h3 class="text-2xl font-serif text-gray-900">{event.name}</h3>
                    <p class="text-gray-700 mt-2">{event.description}</p>
<p class="text-gray-800"><strong>Date & Time:</strong> {event.date}</p>
                    <p class="text-gray-800"><strong>Location:</strong> {event.location}</p>
                    <a href="/rsvp?eventId={event.id}" class="mt-4 inline-block bg-blue-600 text-white px-4 py-2 rounded-md hover:bg-blue-700 transition">
                        ✍️ RSVP Now
                    </a>
                </div>
            {/each}
        </div>
    </div>
</div>
