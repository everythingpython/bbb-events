<script>
    let backgroundImage = "https://images.unsplash.com/photo-1591951425328-48c1fe7179cd";
</script>

<div class="fixed inset-0 w-screen h-screen flex items-center justify-center"
    style="background-image: url('{backgroundImage}'); background-size: cover; background-position: center; background-repeat: no-repeat;">
    
    <!-- Warm parchment-like gradient overlay -->
    <div class="absolute inset-0 bg-gradient-to-b from-transparent via-[#f5e1c0]/50 to-[#d2b48c]/70"></div>

    <!-- Semi-transparent parchment-colored text box -->
    <div class="relative z-10 bg-[#f5e1c0] bg-opacity-80 p-8 rounded-lg text-center text-gray-800 max-w-3xl mx-auto shadow-md">
        <h1 class="text-2xl font-serif font-bold">📖 Broke Bibliophiles Bangalore Event Manager</h1>
        <p class="mt-4 text-lg font-body">Join us in discovering great books, insightful discussions, and engaging events.</p>

        <div class="mt-8 flex flex-col md:flex-row justify-center gap-4">
            <a href="/events" class="bg-yellow-600 text-gray-900 px-6 py-3 rounded-lg text-lg shadow-md hover:bg-yellow-700 transition duration-300">
                📅 View Upcoming Events
            </a>
            <a href="/calendar" class="bg-blue-500 text-white px-6 py-3 rounded-lg text-lg shadow-md hover:bg-blue-600 transition duration-300">
                📚 Past Events Archive
            </a>
            <a href="/rsvp" class="bg-green-500 text-white px-6 py-3 rounded-lg text-lg shadow-md hover:bg-green-600 transition duration-300">
                ✍️ RSVP for an Event
            </a>
        </div>
    </div>
</div>
