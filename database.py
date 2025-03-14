from sqlalchemy import create_engine, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Configuración completa de la base de datos a utilizar
DATABASE_URL = "postgresql://postgres:admin@localhost:5432/examengsi2025"
SCHEMA_NAME = "examengsi2025_schema"

# Crear el motor de conexión
engine = create_engine(DATABASE_URL)
# Crear una sesión para manejar las consultas y demás
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
# Base para los modelos
Base = declarative_base()

# Crear el esquema si no existe
def create_schema():
    with engine.connect() as connection:
        connection.execute(text(f"CREATE SCHEMA IF NOT EXISTS {SCHEMA_NAME}"))
        connection.commit()

# Obtener la sesión 
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()