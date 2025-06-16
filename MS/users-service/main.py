from fastapi import FastAPI  
from fastapi.staticfiles import StaticFiles 
from fastapi.templating import Jinja2Templates  
from routes import router as user_router

app = FastAPI()
app.include_router(user_router)

templates = Jinja2Templates(directory="views")
