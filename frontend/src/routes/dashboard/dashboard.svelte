<script>
  import { onMount } from 'svelte';

  let objetivos = [];
  let seleccionado = null;

  onMount(async () => {
    const res = await fetch('/agentes/historial/', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({})
    });

    const data = await res.json();
    if (data.objetivos) {
      objetivos = data.objetivos;
    }
  });

  function verObjetivo(obj) {
    seleccionado = obj;
  }
</script>

<div class="flex h-screen bg-gray-900 text-white">
  <!-- Panel lateral -->
  <aside class="w-64 p-4 bg-gray-800 border-r border-gray-700 overflow-y-auto">
    <h2 class="text-lg font-bold mb-4">📁 Objetivos</h2>
    {#each objetivos as obj}
      <button class="block w-full text-left p-2 mb-2 rounded hover:bg-gray-700"
              on:click={() => verObjetivo(obj)}>
        {obj.titulo}
        <div class="text-xs text-gray-400">{obj.fecha_creacion.slice(0, 10)}</div>
      </button>
    {/each}
  </aside>

  <!-- Panel principal -->
  <main class="flex-1 p-6 overflow-y-auto">
    {#if seleccionado}
      <h2 class="text-2xl font-bold mb-2">{seleccionado.titulo}</h2>
      <p class="text-gray-400 italic mb-4">{seleccionado.descripcion}</p>

      <h3 class="font-semibold mb-2">Tareas del roadmap más reciente:</h3>
      <ul class="list-disc pl-6 space-y-2 text-sm">
        {#each seleccionado.tareas as tarea}
          <li>
            <strong>{tarea.tarea}</strong> – {tarea.tipo}, prioridad {tarea.prioridad}
            {#if tarea.depende_de.length > 0}
              <div class="text-xs text-gray-400">↳ depende de: {tarea.depende_de.join(', ')}</div>
            {/if}
          </li>
        {/each}
      </ul>
    {:else}
      <p class="text-gray-400">Selecciona un objetivo para ver los detalles.</p>
    {/if}
  </main>
</div>
