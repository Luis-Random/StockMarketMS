from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from routes import router as stocks_router

app = FastAPI()
app.include_router(stocks_router)

templates = Jinja2Templates(directory="views")
