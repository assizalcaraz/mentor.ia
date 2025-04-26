<script>
  let objetivo = '';
  let contexto = '';
  let resultado = null;
  let loading = false;
  let error = '';

  async function planificar() {
    loading = true;
    error = '';
    resultado = null;

    try {
      const res = await fetch('/agentes/arquitecto/planificar/', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ objetivo, contexto })
      });

      const data = await res.json();
      if (!res.ok) {
        error = data.error || 'Error desconocido';
      } else {
        resultado = data.plan;
      }
    } catch (err) {
      error = 'Error al conectar con el backend';
      console.error(err);
    } finally {
      loading = false;
    }
  }

  function validarPlan() {
    // Pronto para activar siguiente fase
    alert('🚧 Acción de validación aún no implementada.');
  }
</script>

<main class="max-w-3xl mx-auto py-10 text-white font-sans">
  <h1 class="text-3xl font-bold text-primary mb-6">🧠 Planificador de Objetivos</h1>

  <label class="block mb-1 text-sm font-medium text-accent">Objetivo</label>
  <textarea bind:value={objetivo} class="w-full p-3 rounded bg-dark-light text-white mb-4" rows="3" placeholder="Ej: Crear un sistema de asistencia facial..."></textarea>

  <label class="block mb-1 text-sm font-medium text-accent">Contexto adicional (opcional)</label>
  <textarea bind:value={contexto} class="w-full p-3 rounded bg-dark-light text-white mb-4" rows="2" placeholder="Proyecto para FADU, con sistema de validación distribuido..."></textarea>

  <button on:click={planificar} class="bg-primary hover:bg-emerald-700 px-6 py-2 rounded text-white font-semibold" disabled={loading}>
    {loading ? 'Generando...' : 'Generar plan'}
  </button>

  {#if error}
    <p class="mt-4 text-red-400">⚠️ {error}</p>
  {/if}

  {#if resultado}
    <div class="mt-6 bg-dark-light p-6 rounded shadow">
      <h2 class="text-xl font-semibold mb-2 text-accent">📋 Plan generado</h2>
      <p class="text-sm text-gray-300 italic mb-4">Objetivo: {resultado.objetivo}</p>

      <ul class="list-disc pl-6 space-y-3">
        {#each resultado.tareas as tarea}
          <li>
            <strong>{tarea.tarea}</strong> — {tarea.tipo}, prioridad {tarea.prioridad}
            {#if tarea.depende_de.length > 0}
              <div class="text-xs text-gray-400">↳ depende de: {tarea.depende_de.join(', ')}</div>
            {/if}
          </li>
        {/each}
      </ul>

      <button class="mt-6 bg-accent hover:bg-blue-500 px-4 py-2 rounded text-white" on:click={validarPlan}>
        ✅ Validar plan y continuar
      </button>
    </div>
  {/if}
</main>
