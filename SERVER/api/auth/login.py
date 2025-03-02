from fastapi import APIRouter
from pydantic import BaseModel
from prisma.models import User as PrismaUser

class User(BaseModel):
    email:str
    password:str
    role:str

router = APIRouter()

@router.post("/user/login")
async def login(user:User):
    prisma_user=await PrismaUser.prisma().findUnique(where={"email":user.email})
    if prisma_user is None:
        return {"error":"User not found"}
    else:
        if prisma_user.password==user.password :
            return {"fullName":prisma_user.fullName,"email":prisma_user.email,"role":prisma_user.role}
        else:
            return {"error":"Incorrect password"}