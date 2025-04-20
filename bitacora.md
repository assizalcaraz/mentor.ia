# 🧠 Bitácora de Desarrollo — Proyecto Mentor.IA

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
