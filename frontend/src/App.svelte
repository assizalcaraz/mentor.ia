<script>
  import Router from 'svelte-spa-router'; // ✅ sin llaves
  import routes from './routes.js';
    
  let mensaje = 'Hola mundo desde Svelte 🎉';
</script>

<main class="p-8 text-center text-white bg-gray-900 min-h-screen">
  <h1 class="text-3xl font-bold">{mensaje}</h1>
  <Router {routes} />  <!-- ✅ movido dentro del <main> para que herede estilo si querés -->
</main>

<style>
  main {
    font-family: sans-serif;
  }
</style>
