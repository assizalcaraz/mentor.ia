# 🧠 Bitácora de Desarrollo — Proyecto Mentor.IA

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
