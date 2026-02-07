from pydantic import BaseModel, EmailStr
from typing import List, Optional


class ProjectBase(BaseModel):
    title: str
    description: Optional[str] = None
    link: Optional[str] = None


class SkillBase(BaseModel):
    name: str


class ProfileBase(BaseModel):
    name: str
    email: EmailStr
    education: Optional[str] = None
    github: Optional[str] = None
    linkedin: Optional[str] = None
    portfolio: Optional[str] = None


class ProfileUpdate(BaseModel):
    name: Optional[str] = None
    education: Optional[str] = None
    github: Optional[str] = None
    linkedin: Optional[str] = None
    portfolio: Optional[str] = None


class ProfileResponse(ProfileBase):
    id: int

    model_config = {
        "from_attributes": True
    }
