# 🧠 Mentor.ia

Mentor.ia es un entorno de desarrollo modular basado en agentes LLM, diseñado para funcionar tanto online como offline. Esta versión integra un **frontend en Svelte** y un **backend en Django**, todo orquestado mediante Docker.

---

## 🔧 Estado actual

- ✅ Frontend con Svelte y `svelte-spa-router`
- ✅ Navegación funcional (`/#/dashboard/planificar`)
- ✅ Dropdown para seleccionar agentes (`evaluacion`, `arquitecto`, `asistente`)
- ✅ Inputs dinámicos: `prompt`, `temperatura`
- ✅ Botón de ejecución (`Generar`)
- ✅ Servido con `nginx` desde contenedor Docker
- ✅ Backend Django parcialmente configurado

---

## 📁 Estructura del proyecto

```
mentoria/
├── backend/            # Backend Django
│   └── agentes/        # App principal con vistas por agente
├── frontend/           # Frontend Svelte + SPA
│   └── src/routes/     # dashboard, planificador, sandbox
├── nginx/              # nginx.conf personalizado
├── docker-compose.yml
└── .env                # Variables de entorno
```

---

## 🚀 Comandos útiles

```bash
# Build & deploy
make force

# Solo frontend
make front-redeploy

# Ver frontend en navegador
http://localhost/#/dashboard/planificar
```

---

## 🐳 Requisitos

- Docker y Docker Compose
- Node.js (si vas a desarrollar el frontend fuera del contenedor)
- `.env` en la raíz con:
  ```
  SECRET_KEY=changeme
  DEBUG=True
  ```

---

## ✨ En desarrollo

- Integración con API de agentes (arquitecto, evaluación, asistente)
- Visualización de respuestas generadas
- Persistencia en base de datos / logs
- Panel administrativo (Django Admin)
- Dashboard de métricas

---

## 🧠 Filosofía

Mentor.ia busca ser un entorno de exploración, construcción y reflexión utilizando agentes LLM conectados entre sí. Su arquitectura modular permite escalar, modificar e integrar nuevos flujos fácilmente.

---

## 🤝 Licencia

MIT – Libre para usar, modificar y compartir.