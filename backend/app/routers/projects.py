from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session
from sqlalchemy import text

from ..database import get_db

router = APIRouter(prefix="/projects", tags=["Projects"])


@router.get("")
def get_projects_by_skill(
    skill: str = Query(..., description="Filter projects by skill"),
    db: Session = Depends(get_db)
):
    query = """
SELECT p.id, p.title, p.description, p.link
FROM projects p
JOIN project_skills ps ON p.id = ps.project_id
JOIN skills s ON s.id = ps.skill_id
WHERE LOWER(s.name) LIKE LOWER(:skill)
"""


    projects = db.execute(
        text(query),
        {"skill": f"%{skill}%"}
    ).mappings().all()

    return projects
