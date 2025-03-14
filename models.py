from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, MetaData
from sqlalchemy.orm import relationship
#from datetime import datetime
from database import Base, SCHEMA_NAME


class TableroMD(Base):
    __tablename__ = "tableros"
    __table_args__ = {"schema": SCHEMA_NAME}

    id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    nombre = Column(String, unique=True, nullable=False, index=True)
    descripcion = Column(String, nullable=True)

    listas = relationship("ListaMD", back_populates="tablero", cascade="all, delete")

class ListaMD(Base):
    __tablename__ = "listas"
    __table_args__ = {"schema": SCHEMA_NAME}

    id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    id_tablero = Column(Integer, ForeignKey(f"{SCHEMA_NAME}.tableros.id"), nullable=False)
    nombre = Column(String, nullable=False)

    tablero = relationship("TableroMD", back_populates="listas")
    tareas = relationship("TareaMD", back_populates="lista", cascade="all, delete")

class TareaMD(Base):
    __tablename__ = "tareas"
    __table_args__ = {"schema": SCHEMA_NAME}

    id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    id_lista = Column(Integer, ForeignKey(f"{SCHEMA_NAME}.listas.id"), nullable=False)
    titulo = Column(String, nullable=False)
    descripcion = Column(String, nullable=True)
    #estatus = Column(String, default="Por Hacer")  
    #fecha = Column(DateTime, default=datetime.utcnow)

    lista = relationship("ListaMD", back_populates="tareas")

