from fastapi import FastAPI # type: ignore
from fastapi.staticfiles import StaticFiles # type: ignore
from fastapi.templating import Jinja2Templates # type: ignore
from routes import router as stocks_router 

app = FastAPI()
app.include_router(stocks_router)

templates = Jinja2Templates(directory="views")
