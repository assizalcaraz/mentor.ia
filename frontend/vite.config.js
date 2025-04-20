import { defineConfig } from 'vite';
import { svelte } from '@sveltejs/vite-plugin-svelte';

export default defineConfig({
  base: '/',
  plugins: [svelte()],
  server: {
    host: true,
    port: 5173,
    proxy: {
      '/agentes': {
        target: 'http://django:8000',
        changeOrigin: true,
        secure: false,
      },
    },
  },
});
