import psycopg2

# Conectar a PostgreSQL sin especificar una base de datos
conn = psycopg2.connect(
    dbname="postgres",  # La base de datos por defecto
    user="postgres",
    password="admin",
    host="localhost",  # Cambia si usas un servidor remoto
    port="5432"  # Puerto por defecto de PostgreSQL
)

conn.autocommit = True  # Necesario para ejecutar CREATE DATABASE

cursor = conn.cursor()

# Crear la base de datos
db_name = "examengsi2025"
#db_user = "examengsiuser"
db_schema = "examengsi2025_schema"

#cursor.execute(f"CREATE USER {db_user};")
cursor.execute(f"CREATE DATABASE {db_name};")
#cursor.execute(f"GRANT ALL PRIVILEGES ON DATABASE {db_name} TO {db_user};")

cursor.execute(f"CREATE SCHEMA {db_schema};")
cursor.execute(f"GRANT ALL PRIVILEGES ON SCHEMA {db_schema} TO postgres;")
#cursor.execute(f"GRANT USAGE, CREATE ON SCHEMA {db_name} TO {db_user};")

print(f"Base de datos '{db_name}' creada exitosamente.")

# Cerrar conexión
cursor.close()
conn.close()