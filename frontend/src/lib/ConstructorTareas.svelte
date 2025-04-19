<script>
  let objetivo = "Explorar el uso de IA en la educación";
  let contexto = "";
  let tareas = [];

  async function consultarConstructor() {
    const params = new URLSearchParams({ objetivo, contexto });
    const res = await fetch(`http://localhost:8000/agentes/constructor/?${params.toString()}`);
    const data = await res.json();
    tareas = data.tareas || [];
  }
</script>

<h2>Desglosador de Objetivos (Constructor)</h2>

<input bind:value={objetivo} placeholder="Objetivo" />
<input bind:value={contexto} placeholder="Contexto (opcional)" />
<button on:click={consultarConstructor}>Consultar</button>

{#if tareas.length > 0}
  <ul>
    {#each tareas as tarea, i}
      <li><strong>{i + 1}.</strong> {tarea.descripcion}</li>
    {/each}
  </ul>
{/if}
