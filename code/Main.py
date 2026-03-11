from contextlib import asynccontextmanager
from fastapi import FastAPI
from routes.Inventory import inv_app
from routes.UserRoute import user_app
from DataBase import InitializeDB

@asynccontextmanager
async def lifespan(app: FastAPI):
    print("Starting inventory system...")
    await InitializeDB()
    yield
    print("System shutting down...")

app = FastAPI(lifespan=lifespan)
app.include_router(inv_app)
app.include_router(user_app)