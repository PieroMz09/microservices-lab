FROM python:3.11-slim

# Configuración base del entorno
ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PIP_NO_CACHE_DIR=off \
    PIP_DEFAULT_TIMEOUT=100

WORKDIR /app

# Instalar dependencias del sistema necesarias
RUN apt-get update && apt-get install -y \
    gcc \
    postgresql-client \
    && rm -rf /var/lib/apt/lists/*

# Copiar e instalar dependencias Python
COPY requirements.txt .
RUN pip install --upgrade pip wheel setuptools && \
    pip install --default-timeout=100 --no-cache-dir -r requirements.txt

# Copiar el código del proyecto
COPY . .

# Dar permisos de ejecución al entrypoint (si existe)
RUN chmod +x /app/entrypoint.sh || true

# Comando de inicio con Gunicorn
CMD ["gunicorn", "auth_service.wsgi:application", "--bind", "0.0.0.0:8000", "--workers", "3"]