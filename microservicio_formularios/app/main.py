from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from .database import engine, SessionLocal
from .models import Base
from . import crud, schemas
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
       CORSMiddleware,
       allow_origins=["*"],  # O ["*"] solo para pruebas
       allow_credentials=True,
       allow_methods=["*"],
       allow_headers=["*"],
   )

@app.on_event("startup")
def startup():
    Base.metadata.create_all(bind=engine)

# Dependencia para obtener la sesión de base de datos
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/", tags=["root"])
def read_root():
    return {"msg": "Microservicio de Formularios funcionando"}

# CRUD Formularios
@app.post("/formularios/", response_model=schemas.Formulario, tags=["formularios"])
def create_formulario(formulario: schemas.FormularioCreate, db: Session = Depends(get_db)):
    return crud.create_formulario(db, formulario)

@app.get("/formularios/", response_model=list[schemas.Formulario], tags=["formularios"])
def read_formularios(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_formularios(db, skip=skip, limit=limit)

@app.get("/formularios/{formulario_id}", response_model=schemas.Formulario, tags=["formularios"])
def read_formulario(formulario_id: int, db: Session = Depends(get_db)):
    db_formulario = crud.get_formulario(db, formulario_id=formulario_id)
    if db_formulario is None:
        raise HTTPException(status_code=404, detail="Formulario no encontrado")
    return db_formulario

@app.put("/formularios/{formulario_id}", response_model=schemas.Formulario, tags=["formularios"])
def update_formulario(formulario_id: int, formulario: schemas.FormularioCreate, db: Session = Depends(get_db)):
    db_formulario = crud.update_formulario(db, formulario_id, formulario)
    if db_formulario is None:
        raise HTTPException(status_code=404, detail="Formulario no encontrado")
    return db_formulario

@app.delete("/formularios/{formulario_id}", response_model=schemas.Formulario, tags=["formularios"])
def delete_formulario(formulario_id: int, db: Session = Depends(get_db)):
    db_formulario = crud.delete_formulario(db, formulario_id)
    if db_formulario is None:
        raise HTTPException(status_code=404, detail="Formulario no encontrado")
    return db_formulario

# CRUD Objetivos
@app.post("/objetivos/", response_model=schemas.ObjetivoFormulario, tags=["objetivos"])
def create_objetivo(objetivo: schemas.ObjetivoFormularioCreate, db: Session = Depends(get_db)):
    return crud.create_objetivo(db, objetivo)

@app.get("/objetivos/", response_model=list[schemas.ObjetivoFormulario], tags=["objetivos"])
def read_objetivos(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_objetivos(db, skip=skip, limit=limit)

@app.get("/objetivos/{objetivo_id}", response_model=schemas.ObjetivoFormulario, tags=["objetivos"])
def read_objetivo(objetivo_id: int, db: Session = Depends(get_db)):
    db_objetivo = crud.get_objetivo(db, objetivo_id=objetivo_id)
    if db_objetivo is None:
        raise HTTPException(status_code=404, detail="Objetivo no encontrado")
    return db_objetivo

@app.put("/objetivos/{objetivo_id}", response_model=schemas.ObjetivoFormulario, tags=["objetivos"])
def update_objetivo(objetivo_id: int, objetivo: schemas.ObjetivoFormularioCreate, db: Session = Depends(get_db)):
    db_objetivo = crud.update_objetivo(db, objetivo_id, objetivo)
    if db_objetivo is None:
        raise HTTPException(status_code=404, detail="Objetivo no encontrado")
    return db_objetivo

@app.delete("/objetivos/{objetivo_id}", response_model=schemas.ObjetivoFormulario, tags=["objetivos"])
def delete_objetivo(objetivo_id: int, db: Session = Depends(get_db)):
    db_objetivo = crud.delete_objetivo(db, objetivo_id)
    if db_objetivo is None:
        raise HTTPException(status_code=404, detail="Objetivo no encontrado")
    return db_objetivo

# CRUD Participantes
@app.post("/participantes/", response_model=schemas.ParticipanteFormulario, tags=["participantes"])
def create_participante(participante: schemas.ParticipanteFormularioCreate, db: Session = Depends(get_db)):
    return crud.create_participante(db, participante)

@app.get("/participantes/", response_model=list[schemas.ParticipanteFormulario], tags=["participantes"])
def read_participantes(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_participantes(db, skip=skip, limit=limit)

@app.get("/participantes/{participante_id}", response_model=schemas.ParticipanteFormulario, tags=["participantes"])
def read_participante(participante_id: int, db: Session = Depends(get_db)):
    db_participante = crud.get_participante(db, participante_id=participante_id)
    if db_participante is None:
        raise HTTPException(status_code=404, detail="Participante no encontrado")
    return db_participante

@app.put("/participantes/{participante_id}", response_model=schemas.ParticipanteFormulario, tags=["participantes"])
def update_participante(participante_id: int, participante: schemas.ParticipanteFormularioCreate, db: Session = Depends(get_db)):
    db_participante = crud.update_participante(db, participante_id, participante)
    if db_participante is None:
        raise HTTPException(status_code=404, detail="Participante no encontrado")
    return db_participante

@app.delete("/participantes/{participante_id}", response_model=schemas.ParticipanteFormulario, tags=["participantes"])
def delete_participante(participante_id: int, db: Session = Depends(get_db)):
    db_participante = crud.delete_participante(db, participante_id)
    if db_participante is None:
        raise HTTPException(status_code=404, detail="Participante no encontrado")
    return db_participante
