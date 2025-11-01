from fastapi import APIRouter, Depends
from sqlalchemy import text
from sqlalchemy.orm import Session
from app.database.session import get_db

router = APIRouter()


@router.get("/health")
def health_check():
    return {"status": "healthy", "service": "StudyMind AI API"}


@router.get("/health/db")
def health_check_db(db: Session = Depends(get_db)):
    try:
        db.execute(text("SELECT 1"))
        return {"status": "healthy", "database": "connected"}
    except Exception as e:
        return {"status": "unhealthy", "database": "disconnected", "error": str(e)}
