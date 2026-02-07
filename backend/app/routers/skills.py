from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from sqlalchemy import text

from ..database import get_db

router = APIRouter(prefix="/skills", tags=["Skills"])


@router.get("/top")
def get_top_skills(db: Session = Depends(get_db)):
    skills = db.execute(
        text("""
        SELECT s.name, COUNT(ps.skill_id) AS count
        FROM skills s
        LEFT JOIN project_skills ps ON ps.skill_id = s.id
        GROUP BY s.id
        ORDER BY count DESC
        """)
    ).mappings().all()

    return skills
