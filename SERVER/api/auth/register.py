from fastapi import APIRouter, FastAPI
from pydantic import BaseModel
from prisma.models import User as PrismaUser

class User(BaseModel):
    fullName: str
    email: str
    password: str
    role: str

router = APIRouter()

@router.post("/user/register")
async def register(user: User):
    prisma_user = await PrismaUser.prisma().create(data={
        "fullName": user.fullName,
        "email": user.email,
        "password": user.password,
        "role": user.role
    })
    return {"fullName": prisma_user.fullName, "email": prisma_user.email, "password": prisma_user.password, "role": prisma_user.role}