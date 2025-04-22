# 🧠 Colección Postman — Mentor.IA

Esta colección contiene endpoints clave para interactuar con el backend de Mentor.IA.

## 🌐 Configuración
Reemplazá `{{base_url}}` por la URL de tu backend:

Ejemplo:
- Local: `http://localhost`
- Producción: `https://tu-dominio.com`

## 📬 Endpoints disponibles

### 🔧 /agentes/arquitecto/planificar/
- **Método**: `POST`
- **Body** (JSON):
  ```json
  {
    "objetivo": "Tu objetivo principal",
    "contexto": "Contexto opcional",
    "objetivo_id": "id_personalizado_opcional"
  }
  ```
- **Respuesta**: Lista de tareas planificadas por el agente arquitecto.

### 🧠 /agentes/memoria/
- **Método**: `POST`
- **Body** (JSON):
  ```json
  {
    "prompt": "Consulta sobre el contexto",
    "objetivo_id": "id relacionado"
  }
  ```
- **Respuesta**: Lista de documentos relevantes desde ChromaDB.

### 📚 /agentes/historial/
- **Método**: `POST`
- **Body** (JSON):
  ```json
  {
    "objetivo_id": "id relacionado"
  }
  ```
- **Respuesta**: Texto plano con todo el contexto recuperado.

## ✅ Recomendaciones
1. Comenzá con `/planificar/` para registrar un objetivo.
2. Luego consultá `/memoria/` o `/historial/` para ver lo registrado.
3. Ideal para debug y exploración directa desde Postman.
