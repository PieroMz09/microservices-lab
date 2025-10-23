# Imagen base de Python
FROM python:3.11-slim

# Establecer directorio de trabajo
WORKDIR /app

# Copiar todo el contenido del servicio
COPY . .

# Instalar dependencias (psycopg2 y redis para la prueba)
RUN pip install psycopg2-binary redis

# Mantener el contenedor vivo (solo para desarrollo)
CMD ["tail", "-f", "/dev/null"]