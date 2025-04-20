import Planificador from './routes/planificador.svelte';
import Index from './routes/index.svelte';

export default {
  '/': Index,
  '/dashboard/planificar': Planificador,
};
