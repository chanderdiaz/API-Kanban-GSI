from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from database import create_schema, engine, Base, get_db
from models import TableroMD, ListaMD, TareaMD
from schemas import TableroModel, ListaModel, TareaModel


# Crear esquema, BD y tablas
create_schema()
Base.metadata.create_all(bind=engine)


app = FastAPI(
    title="API Kanban GSI",
    summary="Desarrollado por Alexander Díaz para examen en GSI.",
    version="1.0.0",
    contact={
        "name": "Alexander Díaz",
        "email": "diaz.chander.7@gmail.com",
    },
)

# Endpoints para los tableros
@app.post("/tableros/")
def crear_tablero(tablero: TableroModel, db: Session = Depends(get_db)):
    db_tablero = TableroMD(**tablero.dict())
    db.add(db_tablero)
    db.commit()
    db.refresh(db_tablero)
    return db_tablero

@app.get("/tableros/")
def get_tableros(db: Session = Depends(get_db)):
    return db.query(TableroMD).all()

# Endpoints para las listas
@app.post("/listas/")
def crear_lista(lista: ListaModel, db: Session = Depends(get_db)):
    db_lista = ListaMD(**lista.dict())
    db.add(db_lista)
    db.commit()
    db.refresh(db_lista)
    return db_lista

@app.get("/listas/{tablero_id}")
def get_listas(tablero_id: str, db: Session = Depends(get_db)):
    return db.query(ListaMD).filter(ListaMD.tablero_id == tablero_id).all()

# Endpoints para tareas
@app.post("/tareas/")
def crear_tarea(tarea: TareaModel, db: Session = Depends(get_db)):
    db_tarea = TareaMD(**tarea.dict())
    db.add(db_tarea)
    db.commit()
    db.refresh(db_tarea)
    return db_tarea

@app.get("/tareas/{lista_id}")
def get_tareas(lista_id: str, db: Session = Depends(get_db)):
    return db.query(TareaMD).filter(TareaMD.lista_id == lista_id).all()


