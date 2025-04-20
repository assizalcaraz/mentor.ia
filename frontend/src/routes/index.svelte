<script>
    import { onMount } from 'svelte';
  
    onMount(() => {
      console.log('🌱 Bienvenido a Mentor.IA');
    });
  </script>
  
  <section class="text-center py-12">
    <h1 class="text-4xl font-bold text-white mb-4">🚀 Mentor.IA</h1>
    <p class="text-gray-300 mb-6">Tu plataforma para crear y planificar agentes inteligentes de forma interactiva.</p>
    <a href="/#/dashboard/planificar" class="bg-blue-600 px-6 py-3 rounded text-white hover:bg-blue-700 transition">
      Empezar a planificar
    </a>
  </section>
  
  <style>
    section {
      font-family: system-ui, sans-serif;
    }
  </style>
  