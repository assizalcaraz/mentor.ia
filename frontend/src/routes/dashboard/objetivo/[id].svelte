<script>
  import { onMount } from 'svelte';
  import { params } from 'svelte-spa-router';

  let objetivo = {};
  let tareas = [];
  let id = '';
  let error = '';
  let cargandoTareas = true;

  onMount(async () => {
    id = params.id;

    if (!id) {
      error = '⚠️ No se pudo determinar el ID del objetivo.';
      cargandoTareas = false;
      return;
    }

    console.log("🌟 ID detectado:", id);

    try {
      const res = await fetch(`/api/arquitecto/obtener_objetivo/${id}/`);
      if (!res.ok) throw new Error('No se pudo obtener el objetivo');
      objetivo = await res.json();
      console.log("📥 Objetivo cargado:", objetivo);

      if (objetivo.roadmap_id) {
        const tareasRes = await fetch(`/api/roadmaps/${objetivo.roadmap_id}/tareas/`);
        if (tareasRes.ok) {
          tareas = await tareasRes.json();
          console.log("📋 Tareas cargadas:", tareas);
        } else {
          console.warn('⚠️ No se pudieron cargar las tareas.');
          tareas = [];
        }
      } else {
        console.warn('⚠️ El objetivo no tiene roadmap asociado.');
      }
    } catch (err) {
      console.error('❌ Error cargando datos:', err);
      error = err.message || 'Error inesperado';
    } finally {
      cargandoTareas = false;
    }
  });
</script>

<div class="p-6">
  {#if error}
    <p class="text-red-500 font-semibold">⚠️ {error}</p>
  {:else}
    <h1 class="text-3xl font-bold mb-4">{objetivo.titulo || 'Objetivo no disponible'}</h1>
    <p class="text-gray-400 mb-6">{objetivo.descripcion || 'Sin descripción disponible.'}</p>

    <div class="mt-8">
      <h2 class="text-2xl font-semibold mb-4">🧩 Lista de Tareas del Roadmap</h2>

      {#if cargandoTareas}
        <p class="text-gray-400 italic animate-pulse">⌛ Cargando tareas...</p>
      {:else if tareas && tareas.length > 0}
        <ul class="list-disc pl-6 space-y-2">
          {#each tareas.filter(t => t && t.id) as tarea (tarea.id)}
            <li>
              <strong>{tarea.tarea}</strong> — {tarea.tipo}, prioridad {tarea.prioridad}
              {#if tarea.depende_de && tarea.depende_de.length > 0}
                <div class="text-xs text-gray-400">
                  ↳ Depende de: {tarea.depende_de.join(', ')}
                </div>
              {/if}
            </li>
          {/each}
        </ul>
      {:else}
        <p class="text-gray-400 italic">🚧 No hay tareas asignadas todavía.</p>
      {/if}
    </div>
  {/if}
</div>
