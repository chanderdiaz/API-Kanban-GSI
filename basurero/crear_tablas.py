from database import engine, Base
import models  

print("Creando tablas en el esquema 'examengsi2025'...")
Base.metadata.create_all(bind=engine)
print("Tablas creadas exitosamente en el esquema 'examengsi2025'.")