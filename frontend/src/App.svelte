<script>
  import Router from 'svelte-spa-router';
  import routes from './routes.js';
  import Header from './components/Header.svelte';
</script>

<main class="min-h-screen bg-gray-950 text-white font-sans">
  <Header />
  <Router {routes} />
</main>

<style>
  main {
    padding: 2rem;
  }
</style>
