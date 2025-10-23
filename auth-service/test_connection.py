import os
import psycopg2
import redis

# Variables de entorno
POSTGRES_USER = os.getenv("POSTGRES_USER", "devuser")
POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD", "devpass")
POSTGRES_DB = os.getenv("POSTGRES_DB", "main_db")
POSTGRES_HOST = os.getenv("POSTGRES_HOST", "postgres")

REDIS_HOST = os.getenv("REDIS_HOST", "redis")
REDIS_PORT = os.getenv("REDIS_PORT", 6379)

# Probar conexión con PostgreSQL
print("🟦 Probando conexión con PostgreSQL...")
try:
    conn = psycopg2.connect(
        dbname=POSTGRES_DB,
        user=POSTGRES_USER,
        password=POSTGRES_PASSWORD,
        host=POSTGRES_HOST
    )
    print("✅ Conexión a PostgreSQL exitosa.")
    conn.close()
except Exception as e:
    print("❌ Error al conectar con PostgreSQL:", e)

# Probar conexión con Redis
print("\n🟥 Probando conexión con Redis...")
try:
    r = redis.Redis(host=REDIS_HOST, port=int(REDIS_PORT))
    r.ping()
    print("✅ Conexión a Redis exitosa.")
except Exception as e:
    print("❌ Error al conectar con Redis:", e)