import Index from './routes/index.svelte';
import Planificador from './routes/planificador.svelte';
import Dashboard from './routes/dashboard/dashboard.svelte';  // Nuevo
import Objetivo from './routes/dashboard/objetivo/[id].svelte'; // Opcional si usás vista de detalle

export default {
  '/': Index,
  '/dashboard': Dashboard,                       // Nuevo: vista híbrida tipo tablero
  '/dashboard/planificar': Planificador,
  '/dashboard/objetivo/:id': Objetivo            // Para vista expandida del objetivo (opcional)
};
