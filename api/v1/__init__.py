from dotenv import load_dotenv

load_dotenv()

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .database import init_database
from .router import *

app = FastAPI()

async def startup():
    await init_database()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(
    router=auth_router,
    prefix="/token",
    tags=["Auth"],
)

app.include_router(
    router=user_router,
    prefix="/user",
    tags=["User"],
)
