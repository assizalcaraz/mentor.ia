<script context="module">
  export async function load({ params }) {
    const res = await fetch("http://localhost:8000/agentes/memoria/", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ objetivo_id: params.id })
    });
    const data = await res.json();
    return { props: { objetivoId: params.id, resultados: data.resultados || [] } };
  }
</script>

<script>
  export let objetivoId;
  export let resultados;

  async function desarrollarTarea(tarea) {
    const res = await fetch("http://localhost:8000/agentes/simular/", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({
        agente: tarea.agente,
        tipo: "codigo",
        prompt: tarea.tarea || tarea.texto || "Desarrollar paso",
        objetivo_id: objetivoId,
        fase: "desarrollo"
      })
    });

    const data = await res.json();
    alert("Respuesta almacenada: " + (data.respuesta || data.error));
    location.reload();
  }
</script>

<main class="max-w-4xl mx-auto p-6 space-y-6">
  <h1 class="text-3xl font-bold text-white">📌 Objetivo: {objetivoId}</h1>

  {#if resultados.length === 0}
    <p class="text-yellow-300">No se encontraron tareas relacionadas a este objetivo.</p>
  {:else}
    <div class="space-y-4">
      {#each resultados as r}
        <div class="bg-gray-800 text-white p-4 rounded-xl shadow space-y-1">
          <p><strong>Fase:</strong> {r.metadatos.fase}</p>
          <p><strong>Agente:</strong> {r.metadatos.agente}</p>
          <p><strong>Contenido:</strong> {r.contenido.tarea || r.contenido.texto || "[Sin contenido]"}</p>

          {#if r.metadatos.fase === 'planificacion'}
            <button class="mt-2 bg-blue-500 text-white px-3 py-1 rounded hover:bg-blue-600" on:click={() => desarrollarTarea(r.contenido)}>
              🚀 Desarrollar tarea
            </button>
          {/if}
        </div>
      {/each}
    </div>
  {/if}

  {#if r.metadatos.fase === 'desarrollo'}
  <div class="mt-2 p-3 bg-gray-700 rounded">
    <p class="text-green-300"><strong>Respuesta generada:</strong></p>
    <pre class="text-white">{JSON.stringify(r.contenido, null, 2)}</pre>
  </div>
{/if}

</main>

<style>
  main {
    font-family: system-ui, sans-serif;
  }
</style>
