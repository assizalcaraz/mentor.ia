import Planificador from './routes/planificador.svelte';
import ObjetivoDetalle from './routes/dashboard/objetivo/[id].svelte';

export default {
  '/dashboard/planificar': Planificador,
  '/dashboard/objetivo/:id': ObjetivoDetalle,
  // Podés agregar más rutas después si querés (por ejemplo `/dashboard/roadmaps`)
};


