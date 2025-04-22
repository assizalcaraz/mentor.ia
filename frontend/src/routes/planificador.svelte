<script>
  import { onMount } from 'svelte';
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
        resultado = { ...data.plan, objetivo_id: data.objetivo_id };

      }
    } catch (err) {
      error = 'Error al conectar con el backend';
      console.error(err);
    } finally {
      loading = false;
    }
  }

  async function validarPlan() {
    try {
      const res = await fetch('/agentes/simular/', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          agente: 'asistente',
          tipo: 'asistente',
          prompt: `Ejecutar plan generado para: ${resultado.objetivo}`,
          objetivo_id: resultado.objetivo_id,
          fase: 'ejecucion'
        })
      });

      const data = await res.json();
      alert("✅ Asistente activado. Tarea simulada: " + data.respuesta);
    } catch (err) {
      alert("❌ Error al validar el plan");
      console.error(err);
    }
  }

</script>

<main class="p-6 max-w-3xl mx-auto text-white">
  <h1 class="text-2xl font-bold mb-4">Planificador de Objetivos 🧠</h1>

  <label class="block mb-2">Objetivo</label>
  <textarea bind:value={objetivo} class="w-full p-2 text-black mb-4" rows="3" placeholder="Ej: Construir un asistente de IA para clases virtuales"></textarea>

  <label class="block mb-2">Contexto adicional (opcional)</label>
  <textarea bind:value={contexto} class="w-full p-2 text-black mb-4" rows="2" placeholder="Ej: Proyecto educativo para secundaria técnica"></textarea>

  <button on:click={planificar} class="bg-green-600 hover:bg-green-700 px-4 py-2 rounded text-white" disabled={loading}>
    {loading ? 'Generando plan...' : 'Generar plan'}
  </button>

  {#if error}
    <p class="mt-4 text-red-400">⚠️ {error}</p>
  {/if}

  {#if resultado}
    <div class="mt-6 bg-gray-800 p-4 rounded shadow">
      <h2 class="text-xl font-semibold mb-2">Plan generado por el Arquitecto 🏗️</h2>
      <p class="text-sm text-gray-300 mb-4 italic">Objetivo: {resultado.objetivo}</p>

      <ul class="list-disc pl-6 space-y-2">
        {#each resultado.tareas as tarea}
          <li>
            <div class="font-medium">{tarea.tarea}</div>
            <div class="text-sm text-gray-400">
              Tipo: {tarea.tipo} | Prioridad: {tarea.prioridad}
              {#if tarea.depende_de.length > 0}
                <br />Depende de: {tarea.depende_de.join(', ')}
              {/if}
            </div>
          </li>
        {/each}
      </ul>

      <button on:click={validarPlan} class="mt-4 bg-blue-600 hover:bg-blue-700 px-4 py-2 rounded text-white">
        Validar plan y continuar ➡️
      </button>      
    </div>
  {/if}
</main>
