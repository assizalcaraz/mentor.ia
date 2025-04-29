# 🧠 Bitácora de Desarrollo — Proyecto Mentor.IA

## 📅 Fecha: 2025-04-29  
### Versión: v0.5 — Vista de Objetivo dinámica y descarga segura de modelos

---

### ✅ Funcionalidades implementadas

- Implementado endpoint `GET /api/arquitecto/obtener_objetivo/<id>/` para devolver metadata completa de un objetivo.
- Vista dinámica `/dashboard/objetivo/:id` ahora renderiza correctamente:
  - Título, descripción, prioridad, fecha, y check-in del objetivo.
  - Tareas asociadas al roadmap si existen.
- Captura segura de parámetros `params.id` desde `svelte-spa-router` usando `export let params`.
- Corrección de redirección post-objetivo creado: navegación correcta hacia `/dashboard/objetivo/:id`.
- Validación de errores y estados cargando/error en el frontend (`⌛`, `❌`, `🚧`).

---

### ⚙️ Infraestructura

- Instalación y testeo del modelo ONNX `all-MiniLM-L6-v2` con persistencia local.
- Se creó script `preload_models.py` para forzar descarga segura dentro del contenedor Django.
- Montaje persistente de `/root/.cache/chroma/onnx_models` vía volumen Docker (`backup_chroma_onnx_models/`).
- Limpieza del repositorio: exclusión vía `.gitignore` de `chroma_db` y backups de modelos ONNX.
- Confirmación de correcto acceso desde Nginx hacia rutas `/api/arquitecto/obtener_objetivo/:id`.

---

### 🧪 Verificaciones

- Verificación manual desde el navegador de flujo completo:
  - Creación de objetivo.
  - Redirección automática a `/dashboard/objetivo/:id`.
  - Carga asincrónica de datos del objetivo y su roadmap.
- Confirmación de respuesta en formato JSON válido desde el backend.
- Verificación de `params.id` recibido correctamente como prop.
- Test de navegación desde distintos navegadores (incl. iPhone/Safari y MacOS/Chrome).
- Confirmación de persistencia de modelos en volumen montado y ejecución limpia del preload.

---

### 🔧 Pendientes

- Crear endpoint `/api/roadmaps/<id>/tareas/` para completar carga de tareas del roadmap.
- Mostrar tareas pendientes directamente en la vista de objetivo (ya está esbozado el bucle `#each`).
- Marcar tareas como completadas desde frontend.
- Incorporar fallback para vista vacía sin roadmap o sin tareas.
- Unificar estilos visuales entre Planificador y Detalle de Objetivo.
- Preparar vista `/dashboard/` general con cards para todos los objetivos existentes.

---

### 🧭 Siguientes pasos sugeridos

1. Implementar y testear `/api/roadmaps/<id>/tareas/`.
2. Crear `dashboard/index.svelte` para listar objetivos como tarjetas clickeables.
3. Establecer acciones básicas de tareas: completar, editar, eliminar.
4. Agregar paginación o scroll virtual si se acumulan muchos objetivos.
5. Implementar backup automático de `chroma_db/` antes de `docker-compose down`.
6. Iniciar sistema de versiones e historial para cada objetivo.


## 📅 Fecha: 2025-04-22  
### Versión: v0.4 — Objetivos persistentes y Roadmap conectado

---

### ✅ Funcionalidades implementadas

- Modelo `Objetivo`, `Roadmap` y `Tarea` en Django con migraciones aplicadas.
- Endpoint `/agentes/arquitecto/planificar/` modificado para crear:
  - Objetivo si no existe.
  - Roadmap asociado.
  - Tareas persistentes en base de datos.
- Se mantiene compatibilidad con ChromaDB para trazabilidad semántica.
- Vista `dashboard.svelte` adaptada para mostrar objetivos con roadmap más reciente.
- Planificador Svelte estilizado con Tailwind extendido.

---

### ⚙️ Infraestructura

- Validación de persistencia real en ChromaDB (`chroma/`).
- Confirmación de uso de mocks mediante `.env` (`USAR_MOCKS=true`).
- Estilizado base unificado desde `App.svelte` como plantilla principal.
- Configuración extendida de `tailwind.config.js`.

---

### 🧪 Verificaciones

- Planificación desde el frontend genera correctamente datos en DB y Chroma.
- Dashboard lista y muestra detalles sin errores.
- Mock activo y funcional para pruebas offline.
- Validación visual de persistencia en contenedor `postgres` y carpeta `chroma`.

---

### 🔧 Pendientes

- Implementar acción real para botón "Validar plan".
- Dashboard debe permitir edición o marcación de tareas completadas.
- Falta vista timeline para múltiples roadmaps por objetivo.
- Historial semántico aún no cruzado con modelos Django.

---

### 🧭 Siguientes pasos sugeridos

1. Activar validación de plan como transición de fase.
2. Mostrar fecha, estado y cantidad de tareas por objetivo.
3. Permitir filtrar objetivos por agente (asistente, usuario).
4. Crear endpoint `/objetivos/` para consumir desde frontend todos los modelos.
5. Preparar backup completo de modelos y embeddings para compartir datasets.

3

## 📅 Fecha: 2025-04-20  
### Versión: v0.3 — Agente Arquitecto y Roadmap LLM

---

### ✅ Funcionalidades implementadas

- Creación del endpoint `/agentes/arquitecto/planificar/`.
- Generación real de tareas con LLM (`codellama:7b-instruct`) vía contenedor `ollama`.
- Refactor de `ollama_client.py` para incluir uso de mocks configurables por `.env`.
- Incorporación de prompt específico para arquitecto en `prompts.py`.
- Estructura JSON validada y parseada automáticamente desde respuesta cruda del modelo.
- Registro en ChromaDB de cada tarea con `objetivo_id`, `fase` y `agente`.

---

### ⚙️ Infraestructura

- Revisión de redes Docker (`llm_network`) y conexión cruzada entre servicios.
- Aumento de timeout de lectura en Nginx y backend para respuestas largas del modelo.
- Corrección del `nginx.conf` para proxy y soporte SPA (`try_files $uri /index.html`).
- Debug detallado de errores 504 y resolución de conflictos de redirección interna.
- Confirmación de inicio correcto del modelo tras calentamiento de `ollama`.

---

### 🧪 Verificaciones

- Curl directo desde Django a `ollama:11434` exitoso.
- Pruebas con distintos objetivos (e.g., “aprender colores en inglés”) devolvieron JSON válido.
- Persistencia de tareas confirmada en base vectorial (`chroma/`).
- Logs de ejecución detallados en consola con trazas completas.
- Mocks desactivables para testing offline de la arquitectura.

---

### 🔧 Pendientes

- Mostrar tareas planificadas en el frontend (etapa `planificar`).
- Implementar botón de validación que inicie fase de ejecución con el asistente.
- Rediseñar visualización general de objetivos y tareas en el dashboard.
- Aplicar migraciones de apps Django base (`auth`, `sessions`, etc).
- Verificar almacenamiento persistente y backup de ChromaDB.

---

### 🧭 Siguientes pasos sugeridos

1. Visualizar la respuesta del agente arquitecto en frontend.
2. Agregar botón para validar plan y lanzar ciclo de ejecución.
3. Integrar almacenamiento de fases del ciclo: planificación → ejecución → validación.
4. Optimizar carga inicial del modelo Ollama y reducir latencias.
5. Consolidar bitácora y generar documentación inicial del proyecto en el `README.md`.


## 📅 Fecha: 2025-04-19
### Versión: v0.2 — Interacción y Memoria Básica

---

### ✅ Funcionalidades implementadas

- Implementación de endpoint `/agentes/simular/` en Django.
- Generación de respuestas simuladas (`mock_llm.py`).
- Persistencia en ChromaDB de cada interacción con metadatos (`agente`, `fase`, `objetivo_id`).
- Recuperación del historial completo por objetivo (`/agentes/historial/`).
- Visualización de memoria vectorial desde la interfaz Svelte.
- Build estable de contenedor `django` con `chromadb` y `sentence-transformers`.
- Debug directo desde consola con trazas explícitas (`print()` y `traceback`).

---

### ⚙️ Infraestructura

- Revisión del `Dockerfile` para asegurar correcta instalación de dependencias.
- Corrección de contexto de copia para `requirements.txt`.
- Debug de errores 500 silenciosos por variables de entorno no montadas.
- Limpieza de caché y reconstrucción sin capas (`--no-cache`).

---

### 🧪 Verificaciones

- Confirmación de escritura/lectura en ChromaDB.
- Prueba de funcionamiento de todos los botones del frontend.
- Confirmación de logs funcionales y traza de flujo de datos.
- Comprobación de respuesta a solicitudes desde navegador y consola.

---

### 🔧 Pendientes

- Endpoint de consulta semántica (`/agentes/memoria/`) aún no testeado en flujo real.
- No se ha implementado el ciclo completo con múltiples agentes (solo constructor).
- Falta visualización tipo “chat” o timeline entre agentes.
- Validar persistencia real de los documentos (`persist_directory`) al reiniciar.
- Evaluar compresión y resumen de interacciones largas.
- Migraciones pendientes (`auth`, `admin`, `sessions`...).

---

### 🧭 Siguientes pasos sugeridos

1. Probar `/agentes/memoria/` con resultados desde `chromadb.query()`.
2. Diseñar visual “estilo conversación” para el historial entre agentes.
3. Implementar revisor que lea de memoria y genere validaciones.
4. Comenzar con embedding real (no solo `mock_llm`) usando modelo liviano.
5. Preparar `README.md` con capturas y descripción general del proyecto.
