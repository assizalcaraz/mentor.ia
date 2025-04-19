<script>
  import { onMount } from 'svelte';
  import { writable } from 'svelte/store';
  import hljs from 'highlight.js';
  import 'highlight.js/styles/atom-one-dark.css';

  const prompt = writable("Escribí una función en Python que ordene una lista usando merge sort");
  const temperature = writable(0.2);
  const respuesta = writable("");
  const loading = writable(false);

  const API_URL = import.meta.env.VITE_API_URL;

  // Bloque reactivo: ejecuta esto cada vez que cambia $respuesta
  $: if ($respuesta) {
    setTimeout(() => {
      hljs.highlightAll();
    }, 0);
  }

  async function enviarConsulta() {
    loading.set(true);
    respuesta.set("");

    try {
      const url = new URL("/agentes/generar/", API_URL);
      url.searchParams.append("prompt", $prompt);

      const res = await fetch(url);
      const data = await res.json();
      respuesta.set(data.respuesta);
    } catch (error) {
      respuesta.set("Error al consultar el modelo: " + error);
    } finally {
      loading.set(false);
    }
  }
</script>


<main class="p-4 max-w-3xl mx-auto">
  <h1 class="text-2xl font-bold mb-4">Generador con LLM (Ollama)</h1>

  <div class="mb-4">
    <label class="block font-semibold mb-1">Prompt</label>
    <textarea bind:value={$prompt} class="w-full border p-2 rounded h-28" placeholder="Escribí tu consulta..."></textarea>
  </div>

  <div class="mb-4">
    <label class="block font-semibold mb-1">Temperatura</label>
    <input type="range" min="0" max="1" step="0.05" bind:value={$temperature} class="w-full" />
    <p class="text-sm">{$temperature}</p>
  </div>

  <button on:click={enviarConsulta} class="bg-blue-600 text-white px-4 py-2 rounded hover:bg-blue-700">
    Generar Respuesta
  </button>

  {#if $loading}
    <p class="mt-4 text-yellow-600">Consultando el modelo...</p>
  {/if}

  {#if $respuesta}
  <div class="mt-6 p-6 rounded-xl bg-gray-800 text-white shadow-xl">
    <h2 class="text-xl font-bold mb-4">🧠 Respuesta generada</h2>
    <pre class="bg-gray-950 text-green-300 p-4 rounded-md overflow-x-auto whitespace-pre-wrap">
      <code class="language-python">{$respuesta}</code>
    </pre>
  </div>


<style>
  main {
    font-family: system-ui, sans-serif;
  }
</style>
