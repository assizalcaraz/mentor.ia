<script>
  import Router from 'svelte-spa-router';
  import routes from './routes.js';
</script>

<div class="min-h-screen bg-gray-950 text-white font-sans flex flex-col">
  <!-- Header -->
  <header class="bg-gray-900 shadow border-b border-gray-800 px-6 py-4 flex items-center justify-between">
    <h1 class="text-xl font-bold text-green-400">🚀 Mentor.IA</h1>
    <span class="text-sm text-gray-400 hidden sm:inline">Agentes inteligentes conectados</span>
  </header>

  <!-- Contenido principal -->
  <main class="flex-1 p-6 overflow-y-auto">
    <Router {routes} />
  </main>

  <!-- Footer opcional -->
  <footer class="text-xs text-gray-500 text-center py-4 border-t border-gray-800">
    © 2025 Mentor.IA — Versión experimental
  </footer>
</div>

<style>
  main {
    font-family: 'Inter', sans-serif;
  }
</style>
