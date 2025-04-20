# backend/Dockerfile

FROM python:3.10-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

# Instalar dependencias del sistema
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    curl \
    git \
    && rm -rf /var/lib/apt/lists/*

# ✅ Cambiar directorio de trabajo
WORKDIR /app

# ✅ Copiar requirements
COPY requirements.txt /app/requirements.txt

# Instalar dependencias Python
RUN pip install --upgrade pip && pip install -r /app/requirements.txt

# ✅ Copiar todo lo demás al contenedor
COPY . /app/

# Exponer puerto
EXPOSE 8000

# Comando de ejecución
CMD ["gunicorn", "mentoria.wsgi:application", "--bind", "0.0.0.0:8000"]
