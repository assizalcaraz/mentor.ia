<script>
  import { push } from 'svelte-spa-router';
  import { onMount } from 'svelte';

  let objetivo = '';
  let contexto = '';
  let loading = false;
  let error = '';

  async function crearObjetivo() {
    loading = true;
    error = '';

    try {
      const res = await fetch('/api/arquitecto/crear_objetivo/', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ objetivo, contexto })
      });

      const data = await res.json();
      console.log('📦 Respuesta crear_objetivo:', data);

      if (!res.ok) {
        throw new Error(data.error || 'Error desconocido');
      }

      const objetivoId = data.objetivo_id;
      console.log('🚀 Redirigiendo a /dashboard/objetivo/' + objetivoId);

      // Redirigir automáticamente
      push(`/dashboard/objetivo/${objetivoId}`);
    } catch (err) {
      console.error(err);
      error = err.message;
    } finally {
      loading = false;
    }
  }
</script>

<main class="max-w-3xl mx-auto py-10 text-white font-sans">
  <h1 class="text-3xl font-bold text-primary mb-6">🚀 Crear Nuevo Objetivo</h1>

  <label class="block mb-1 text-sm font-medium text-accent">Objetivo</label>
  <textarea bind:value={objetivo} class="w-full p-3 rounded bg-dark-light text-white mb-4" rows="3" placeholder="Ej: Crear un sistema de asistencia facial..."></textarea>

  <label class="block mb-1 text-sm font-medium text-accent">Contexto adicional (opcional)</label>
  <textarea bind:value={contexto} class="w-full p-3 rounded bg-dark-light text-white mb-4" rows="2" placeholder="Proyecto para FADU, con sistema de validación distribuido..."></textarea>

  <button on:click={crearObjetivo} class="bg-primary hover:bg-emerald-700 px-6 py-2 rounded text-white font-semibold" disabled={loading}>
    {loading ? 'Creando...' : 'Crear Objetivo'}
  </button>

  {#if error}
    <p class="mt-4 text-red-400">⚠️ {error}</p>
  {/if}
</main>
