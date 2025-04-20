<script>
  import { writable } from 'svelte/store';

  // Stores reactivas
  const tipo = writable('');
  const modelo = writable('');
  const criterio = writable('');
  const objetivo = writable('');
  const contexto = writable('');
  const prompt = writable('');
  const temperatura = writable(0.7);

  // Opciones de ejemplo
  const tipos = ['evaluacion', 'arquitecto', 'asistente'];
  const modelos = ['gpt-4', 'llama3', 'mistral'];

  let resultado = '';
</script>

<main class="p-6 text-white bg-gray-900 min-h-screen space-y-6">
  <h1 class="text-2xl font-bold mb-4">Planificador de Agentes</h1>

  <div class="grid md:grid-cols-2 gap-4">
    <div>
      <label class="block font-semibold mb-1" for="tipo">Tipo de consulta</label>
      <select id="tipo" bind:value={$tipo} class="w-full border p-2 rounded bg-gray-800 text-white">
        <option value="" disabled>Seleccionar</option>
        {#each tipos as t}
          <option value={t}>{t}</option>
        {/each}
      </select>
    </div>

    <div>
      <label class="block font-semibold mb-1" for="modelo">Modelo</label>
      <select id="modelo" bind:value={$modelo} class="w-full border p-2 rounded bg-gray-800 text-white">
        <option value="" disabled>Seleccionar</option>
        {#each modelos as m}
          <option value={m}>{m}</option>
        {/each}
      </select>
    </div>
  </div>

  {#if $tipo === 'evaluacion'}
    <div>
      <label class="block font-semibold mb-1">Criterio de evaluación</label>
      <input bind:value={$criterio} class="w-full border p-2 rounded bg-gray-800 text-white" />
    </div>
  {/if}

  {#if $tipo === 'arquitecto'}
    <div>
      <label class="block font-semibold mb-1">Objetivo</label>
      <input bind:value={$objetivo} class="w-full border p-2 rounded bg-gray-800 text-white" />
    </div>
    <div>
      <label class="block font-semibold mb-1">Contexto</label>
      <textarea bind:value={$contexto} class="w-full border p-2 rounded h-20 bg-gray-800 text-white"></textarea>
    </div>
  {/if}

  {#if $tipo !== 'arquitecto' && $tipo !== 'evaluacion'}
    <div>
      <label class="block font-semibold mb-1">Prompt</label>
      <textarea bind:value={$prompt} class="w-full border p-2 rounded h-28 bg-gray-800 text-white"></textarea>
    </div>
  {/if}

  <div>
    <label class="block font-semibold mb-1">Temperatura</label>
    <input type="range" min="0" max="1" step="0.05" bind:value={$temperatura} class="w-full" />
    <p class="text-sm">{$temperatura}</p>
  </div>

  <div class="mt-4">
    <button
      class="bg-blue-600 hover:bg-blue-700 text-white px-4 py-2 rounded"
      on:click={() => resultado = 'Simulación de envío 🎯'}
    >
      Generar
    </button>
  </div>

  {#if resultado}
    <div class="mt-6 bg-gray-800 p-4 rounded">
      <p>{resultado}</p>
    </div>
  {/if}
</main>
