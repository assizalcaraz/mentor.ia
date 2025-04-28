<script>
  import Router from 'svelte-spa-router';
  import routes from './routes.js';
</script>

<div class="min-h-screen bg-gray-950 text-white font-sans flex flex-col">
  <header class="bg-gray-900 shadow border-b border-gray-800 px-6 py-4 flex items-center justify-between">
    <h1 class="text-xl font-bold text-green-400">🚀 Mentor.IA</h1>
  </header>

  <main class="flex-1 p-6 overflow-y-auto">
    <Router {routes} useHash={true} />
  </main>

  <footer class="text-xs text-gray-500 text-center py-4 border-t border-gray-800">
    © 2025 Mentor.IA — Versión experimental
  </footer>
</div>
