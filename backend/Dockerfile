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

# Crear directorio de trabajo
WORKDIR /app/backend

# Copiar dependencias desde raíz del proyecto al contenedor
COPY requirements.txt /app/requirements.txt

# Instalar dependencias
RUN pip install --upgrade pip && pip install -r /app/requirements.txt

# Copiar el resto del proyecto (todo mentoria/)
COPY . /app/

# Exponer puerto Django
EXPOSE 8000

# Ejecutar gunicorn desde backend/
CMD ["gunicorn", "mentoria.wsgi:application", "--bind", "0.0.0.0:8000"]
