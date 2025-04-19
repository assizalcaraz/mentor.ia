import { defineConfig } from 'vite'
import { svelte } from '@sveltejs/vite-plugin-svelte'

export default defineConfig({
  plugins: [svelte()],
  server: {
    host: true,     // necesario para acceso desde fuera del contenedor
    port: 5173,     // puerto del frontend en desarrollo
    proxy: {
      '/agentes': {
        target: 'http://django:8000',
        changeOrigin: true,
        secure: false,
      },
    },
  },
})
