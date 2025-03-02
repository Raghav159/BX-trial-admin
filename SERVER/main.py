from fastapi import FastAPI
from prisma import Prisma, register
from api.auth.login import router as login_router

app = FastAPI()

from api.auth.register import router as register_router

db = Prisma()
register(db)

@app.on_event("startup")
async def startup():
    await db.connect()

@app.on_event("shutdown")
async def shutdown():
    await db.disconnect()

app.include_router(register_router)
app.include_router(login_router)