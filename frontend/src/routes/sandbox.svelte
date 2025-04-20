<script>
  import { writable } from 'svelte/store';

  const tipo = writable("codigo");
  const prompt = writable("Escribí una función que devuelva la sucesión de Fibonacci");
  const modelo = writable("codellama:7b-instruct");
  const temperatura = writable(0.2);
  const respuesta = writable("");
  const cargando = writable(false);

  const tipos = ["codigo", "evaluacion", "arquitecto"];
  const modelos = ["codellama:7b-instruct", "phind-codellama"];

  async function enviar() {
    cargando.set(true);
    respuesta.set("");

    const payload = {
      tipo: $tipo,
      prompt: $prompt,
      modelo: $modelo,
      temperatura: $temperatura,
      ...( $tipo === "evaluacion" ? { criterio: "claridad" } : {} ),
      ...( $tipo === "arquitecto" ? { contexto: "Prueba rápida de sandbox" } : {} )
    };

    try {
      const res = await fetch("http://localhost:8000/agentes/sandbox/procesar/", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(payload)
      });

      const data = await res.json();
      respuesta.set(data.respuesta || "Sin respuesta.");
    } catch (e) {
      respuesta.set("❌ Error al comunicar con el backend.");
    } finally {
      cargando.set(false);
    }
  }
</script>

<main class="max-w-3xl mx-auto p-6 space-y-6">
  <h1 class="text-2xl font-bold text-white">🧪 Sandbox LLM</h1>

  <div class="space-y-4">
    <div>
      <label class="text-white font-semibold">Tipo</label>
      <select bind:value={$tipo} class="w-full p-2 rounded border">
        {#each tipos as t}
          <option>{t}</option>
        {/each}
      </select>
    </div>

    <div>
      <label class="text-white font-semibold">Modelo</label>
      <select bind:value={$modelo} class="w-full p-2 rounded border">
        {#each modelos as m}
          <option>{m}</option>
        {/each}
      </select>
    </div>

    <div>
      <label class="text-white font-semibold">Prompt</label>
      <textarea bind:value={$prompt} class="w-full p-2 rounded border h-32"></textarea>
    </div>

    <div>
      <label class="text-white font-semibold">Temperatura</label>
      <input type="range" min="0" max="1" step="0.05" bind:value={$temperatura} class="w-full" />
      <p class="text-sm text-white">{$temperatura}</p>
    </div>

    <button on:click={enviar} class="bg-blue-600 text-white px-4 py-2 rounded hover:bg-blue-700">
      Enviar consulta
    </button>
  </div>

  {#if $cargando}
    <p class="text-yellow-400">⏳ Generando respuesta...</p>
  {/if}

  {#if $respuesta}
    <div class="bg-gray-800 text-green-300 mt-4 p-4 rounded-md whitespace-pre-wrap">
      <h2 class="text-white font-bold mb-2">🔎 Respuesta:</h2>
      <pre>{$respuesta}</pre>
    </div>
  {/if}
</main>

<style>
  main {
    font-family: system-ui, sans-serif;
  }
</style>
