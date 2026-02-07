from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy import text

from ..database import get_db
from ..schemas import ProfileBase, ProfileUpdate

router = APIRouter(prefix="/profile", tags=["Profile"])


@router.get("/")
def get_profile(db: Session = Depends(get_db)):
    profile = db.execute(
        text("SELECT * FROM profile LIMIT 1")
    ).mappings().first()

    if not profile:
        raise HTTPException(status_code=404, detail="Profile not found")

    return profile



@router.post("/")
def create_profile(profile: ProfileBase, db: Session = Depends(get_db)):
    db.execute(
        text("""
        INSERT INTO profile (name, email, education, github, linkedin, portfolio)
        VALUES (:name, :email, :education, :github, :linkedin, :portfolio)
        """),
        profile.dict()
    )
    db.commit()
    return {"message": "Profile created"}



@router.put("/")
def update_profile(profile: ProfileUpdate, db: Session = Depends(get_db)):
    fields = {k: v for k, v in profile.dict().items() if v is not None}

    if not fields:
        raise HTTPException(status_code=400, detail="No fields to update")

    set_clause = ", ".join([f"{k} = :{k}" for k in fields])

    db.execute(
        text(f"UPDATE profile SET {set_clause}"),
        fields
    )
    db.commit()

    return {"message": "Profile updated"}
