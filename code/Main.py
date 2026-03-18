from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from routes.Inventory import inv_app
from routes.UserRoute import user_app
from DataBase.DataBase import InitializeDB

@asynccontextmanager
async def lifespan(app: FastAPI):
    print("Starting inventory system...")
    await InitializeDB()
    yield
    print("System shutting down...")

app = FastAPI(lifespan=lifespan)
app.include_router(inv_app)
app.include_router(user_app)

@app.get("/", tags=["Main"])
async def root():
    return {"message" : "welcome"}