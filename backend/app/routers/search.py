from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session
from sqlalchemy import text

from ..database import get_db

router = APIRouter(
    prefix="/search",
    tags=["Search"]
)

@router.get("", summary="Search projects")
@router.get("/", summary="Search projects")
def search(
    q: str = Query(..., min_length=1, description="Search keyword"),
    db: Session = Depends(get_db)
):
    sql = text("""
        SELECT id, title, description, link
        FROM projects
        WHERE LOWER(title) LIKE LOWER(:q)
           OR LOWER(description) LIKE LOWER(:q)
        ORDER BY id DESC
    """)

    results = db.execute(sql, {"q": f"%{q}%"}).mappings().all()

    return results
