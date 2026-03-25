from contextlib import asynccontextmanager
from fastapi import FastAPI, Request
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

app.mount("/static", StaticFiles(directory="static"), name="static")
template =Jinja2Templates(directory="Templates") 

@app.get("/", response_class=HTMLResponse)
async def root(request : Request):
    return template.TemplateResponse("home.html", 
                                     {"request": request, "message": "Hello!"})

@app.get("/login", response_class=HTMLResponse)
async def login_home(request : Request):
    return template.TemplateResponse("login.html", {"request": request, "message": "Sign in"})