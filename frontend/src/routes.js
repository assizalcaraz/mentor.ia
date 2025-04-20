import Index from './routes/index.svelte';
import Planificador from './routes/planificador.svelte';

export default {
  '/': Index,
  '/dashboard/planificar': Planificador
};
