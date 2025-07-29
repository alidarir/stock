from fastapi import APIRouter
from ali_backend.celery import hello_world


router = APIRouter()

@router.get("/ping")
def ping():
    return {"message": "pong"}
