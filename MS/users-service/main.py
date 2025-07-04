from fastapi import FastAPI  # type: ignore
from fastapi.staticfiles import StaticFiles # type: ignore
from fastapi.templating import Jinja2Templates  # type: ignore
from routes import router as user_router

app = FastAPI()
app.include_router(user_router)

templates = Jinja2Templates(directory="views")
