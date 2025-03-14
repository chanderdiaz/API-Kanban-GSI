import psycopg2

try:
    conn = psycopg2.connect(
        dbname="postgres",
        user="postgres",
        password="admin",
        host="localhost",
        port="5432"
    )
    print("Conexión exitosa a PostgreSQL")
    conn.close()
except Exception as e:
    print("Error de conexión:", e)