from fastapi import FastAPI
from app.routes.tasks import router as tasks_router
from app.db.database import engine
from app.db import models

models.Base.metadata.create_all(bind=engine)
app = FastAPI()


@app.get("/")
def read_root():
    return {"message": "API do Lucas rodando"}


@app.get("/health")
def health_check():
    return {"status": "ok"}


@app.get("/hello/{name}")
def say_hello(name: str):
    return {"message": f"Olá, {name}"}


app.include_router(tasks_router)