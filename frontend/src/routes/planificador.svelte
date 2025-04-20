<script>
  import { writable } from 'svelte/store';
  import hljs from 'highlight.js';
  import 'highlight.js/styles/atom-one-dark.css';

  const prompt = writable("Escribí una función en Python que ordene una lista usando merge sort");
  const temperatura = writable(0.2);
  const respuesta = writable("");
  const loading = writable(false);
  const tipo = writable("codigo");
  const modelo = writable("codellama:7b-instruct");
  const criterio = writable("calidad técnica");
  const objetivo = writable("Crear una app de asistencia con reconocimiento facial");
  const contexto = writable("");

  const tipos = ["codigo", "consulta", "arquitecto", "evaluacion"];
  const modelos = ["codellama:7b-instruct", "phind-codellama"];

  $: if ($respuesta) {
    setTimeout(() => hljs.highlightAll(), 0);
  }

  async function enviarConsulta() {
    loading.set(true);
    respuesta.set("");

    let payload = {
      tipo: $tipo,
      temperatura: $temperatura,
      modelo: $modelo,
    };

    if ($tipo === "evaluacion") {
      payload = { ...payload, prompt: $prompt, criterio: $criterio };
    } else if ($tipo === "arquitecto") {
      payload = { ...payload, objetivo: $objetivo, contexto: $contexto };
    } else {
      payload = { ...payload, prompt: $prompt };
    }

    try {
      const res = await fetch("http://localhost:8000/agentes/procesar/", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(payload)
      });

      const data = await res.json();

      const clean = (data.respuesta || JSON.stringify(data))
        .replace(/^```[a-z]*\n?/i, "")
        .replace(/```$/, "");

      respuesta.set(clean);
    } catch (error) {
      respuesta.set("Error: " + error);
    } finally {
      loading.set(false);
    }
  }

  const historialCompilado = writable("");
  const respuestaSimulada = writable("");
  const resultadosMemoria = writable([]);

  async function obtenerHistorial() {
    const res = await fetch("http://localhost:8000/agentes/historial/", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ objetivo_id: "demo_001" })
    });
    const data = await res.json();
    historialCompilado.set(data.contexto || "No hay historial.");
  }

  async function simularInteraccion() {
    const res = await fetch("http://localhost:8000/agentes/simular/", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({
        agente: "arquitecto",
        tipo: "codigo",
        prompt: "Cómo crear un panel lateral",
        objetivo_id: "demo_001",
        fase: "inicio"
      })
    });

    const data = await res.json();
    respuestaSimulada.set(data.respuesta || "Error");
  }

  async function consultarMemoria() {
    const res = await fetch("http://localhost:8000/agentes/memoria/", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({
        prompt: "panel lateral",
        objetivo_id: "demo_001"
      })
    });

    const data = await res.json();
    resultadosMemoria.set(data.resultados || []);
  }
</script>

<main class="p-6 max-w-3xl mx-auto space-y-6">
  <h1 class="text-2xl font-bold">🧪 Generador LLM interactivo</h1>

  <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
    <div>
      <label class="block font-semibold mb-1">Tipo de consulta</label>
      <select bind:value={$tipo} class="w-full border p-2 rounded">
        {#each tipos as t}
          <option>{t}</option>
        {/each}
      </select>
    </div>
    <div>
      <label class="block font-semibold mb-1">Modelo</label>
      <select bind:value={$modelo} class="w-full border p-2 rounded">
        {#each modelos as m}
          <option>{m}</option>
        {/each}
      </select>
    </div>
  </div>

  {#if $tipo === 'evaluacion'}
    <div>
      <label class="block font-semibold mb-1">Criterio de evaluación</label>
      <input bind:value={$criterio} class="w-full border p-2 rounded" />
    </div>
  {/if}

  {#if $tipo === 'arquitecto'}
    <div>
      <label class="block font-semibold mb-1">Objetivo</label>
      <input bind:value={$objetivo} class="w-full border p-2 rounded" />
    </div>
    <div>
      <label class="block font-semibold mb-1">Contexto</label>
      <textarea bind:value={$contexto} class="w-full border p-2 rounded h-20"></textarea>
    </div>
  {/if}

  {#if $tipo !== 'arquitecto' && $tipo !== 'evaluacion'}
    <div>
      <label class="block font-semibold mb-1">Prompt</label>
      <textarea bind:value={$prompt} class="w-full border p-2 rounded h-28"></textarea>
    </div>
  {/if}

  <div>
    <label class="block font-semibold mb-1">Temperatura</label>
    <input type="range" min="0" max="1" step="0.05" bind:value={$temperatura} class="w-full" />
    <p class="text-sm">{$temperatura}</p>
  </div>

  <button on:click={enviarConsulta} class="bg-blue-600 text-white px-4 py-2 rounded hover:bg-blue-700">
    Generar
  </button>

  {#if $loading}
    <p class="text-yellow-600">Cargando respuesta...</p>
  {/if}

  {#if $respuesta}
    <div class="mt-6 p-6 rounded-xl bg-gray-800 text-white shadow-xl">
      <h2 class="text-xl font-bold mb-4">🔎 Respuesta</h2>
      <pre class="bg-gray-950 text-green-300 p-4 rounded-md overflow-x-auto whitespace-pre-wrap">
        <code class="language-json">{$respuesta}</code>
      </pre>
    </div>
  {/if}

  <button on:click={obtenerHistorial} class="bg-indigo-600 text-white px-4 py-2 rounded hover:bg-indigo-700">
    🧠 Ver historial compilado
  </button>

  {#if $historialCompilado}
    <div class="bg-gray-900 text-green-300 p-4 mt-4 rounded-md whitespace-pre-wrap">
      <h3 class="text-white font-bold mb-2">🧩 Historial de Interacciones:</h3>
      <pre>{$historialCompilado}</pre>
    </div>
  {/if}

  <section class="mt-12 border-t pt-6 space-y-4">
    <h2 class="text-xl font-bold">🧪 Pruebas con memoria simulada</h2>

    <button on:click={simularInteraccion} class="bg-green-700 text-white px-4 py-2 rounded hover:bg-green-800">
      Simular interacción y guardar
    </button>

    <button on:click={consultarMemoria} class="ml-4 bg-purple-700 text-white px-4 py-2 rounded hover:bg-purple-800">
      Consultar memoria
    </button>

    <div class="bg-gray-800 p-4 rounded mt-4 text-white">
      <h3 class="font-semibold">Última respuesta simulada:</h3>
      <pre class="whitespace-pre-wrap">{$respuestaSimulada}</pre>
    </div>

    <div class="bg-gray-900 p-4 rounded mt-4 text-white">
      <h3 class="font-semibold">Resultados en memoria:</h3>
      <ul class="list-disc ml-4">
        {#each $resultadosMemoria as item}
          <li>{item}</li>
        {/each}
      </ul>
    </div>
  </section>
</main>

<style>
  main {
    font-family: system-ui, sans-serif;
  }
</style>
