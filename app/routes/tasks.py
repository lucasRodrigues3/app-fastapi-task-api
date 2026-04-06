from fastapi import APIRouter
from app.schemas.tasks import TaskCreate
from app.db.database import SessionLocal
from app.db.models import Task

router = APIRouter()


@router.post("/tasks")
def create_task(task: TaskCreate):
    db = SessionLocal()

    db_task = Task(title=task.title, done=task.done)
    db.add(db_task)
    db.commit()
    db.refresh(db_task)

    db.close()

    return db_task


@router.get("/tasks")
def get_tasks():
    db = SessionLocal()

    tasks = db.query(Task).all()

    db.close()

    return tasks