import App from './App.svelte';
import { wrap } from 'svelte-spa-router/wrap';
import Router from 'svelte-spa-router';
import routes from './routes.js';

const app = new App({
  target: document.getElementById('app'),
  props: {
    name: 'mundo'
  }
});

export default app;
