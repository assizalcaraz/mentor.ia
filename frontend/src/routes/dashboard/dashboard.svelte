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

<div class="flex h-screen bg-gray-950 text-white">
  <!-- Sidebar -->
  <aside class="w-64 bg-gray-900 p-5 border-r border-gray-800 shadow-md">
    <h2 class="text-xl font-bold mb-6">📂 Objetivos</h2>
    <div class="space-y-3">
      {#each objetivos as obj}
        <button
          class="w-full text-left bg-gray-800 hover:bg-gray-700 px-4 py-2 rounded-lg shadow-sm transition"
          on:click={() => verObjetivo(obj)}>
          <div class="font-semibold">{obj.titulo}</div>
          <div class="text-xs text-gray-400">{obj.fecha_creacion.slice(0, 10)}</div>
        </button>
      {/each}
    </div>
  </aside>

  <!-- Main Panel -->
  <main class="flex-1 px-10 py-8 overflow-y-auto">
    {#if seleccionado}
      <div class="bg-gray-900 p-6 rounded-lg shadow-lg border border-gray-800">
        <h2 class="text-3xl font-bold mb-2 text-green-400">{seleccionado.titulo}</h2>
        <p class="text-gray-400 mb-6 italic">{seleccionado.descripcion}</p>

        <h3 class="text-xl font-semibold mb-4 text-blue-400">Tareas del roadmap más reciente</h3>
        <ul class="space-y-3 text-sm">
          {#each seleccionado.tareas as tarea}
            <li class="bg-gray-800 p-3 rounded-lg border border-gray-700">
              <div class="font-semibold text-white">{tarea.tarea}</div>
              <div class="text-gray-400">
                {tarea.tipo} • prioridad {tarea.prioridad}
              </div>
              {#if tarea.depende_de.length > 0}
                <div class="text-xs text-gray-500 mt-1">↳ depende de: {tarea.depende_de.join(', ')}</div>
              {/if}
            </li>
          {/each}
        </ul>
      </div>
    {:else}
      <p class="text-gray-500 text-lg">Selecciona un objetivo del panel lateral para ver los detalles.</p>
    {/if}
  </main>
</div>
