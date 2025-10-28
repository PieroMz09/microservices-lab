import os
import psycopg2
import redis

def test_postgres():
    try:
        conn = psycopg2.connect(
            host=os.getenv('DB_HOST', 'localhost'),
            database=os.getenv('POSTGRES_DB', 'main_db'),
            user=os.getenv('POSTGRES_USER', 'devuser'),
            password=os.getenv('POSTGRES_PASSWORD', 'devpass'),
            port=5432
        )
        print("✅ PostgreSQL: Conexión exitosa")
        conn.close()
        return True
    except Exception as e:
        print(f"❌ PostgreSQL: Error - {e}")
        return False

def test_redis():
    try:
        r = redis.Redis(
            host=os.getenv('REDIS_HOST', 'localhost'),
            port=int(os.getenv('REDIS_PORT', 6379)),
            decode_responses=True
        )
        r.ping()
        print("✅ Redis: Conexión exitosa")
        return True
    except Exception as e:
        print(f"❌ Redis: Error - {e}")
        return False

if __name__ == "__main__":
    print("🔍 Probando conexiones...\n")
    postgres_ok = test_postgres()
    redis_ok = test_redis()
    
    if postgres_ok and redis_ok:
        print("\n🎉 Todas las conexiones funcionan correctamente")
    else:
        print("\n⚠️ Algunas conexiones fallaron")