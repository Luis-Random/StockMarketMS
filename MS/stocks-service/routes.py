# routes.py
from fastapi import APIRouter, Request  # type: ignore
from fastapi.responses import HTMLResponse  # type: ignore
from fastapi.templating import Jinja2Templates  # type: ignore
from Controllers.StockController import *
from Models.Stock import Stock # type: ignore
from factories.stock_factories import StockFactories

router = APIRouter()
templates = Jinja2Templates(directory="views")
stock = StockFactories.create_stock_service()

@router.get("/stocks-page", response_class=HTMLResponse)
async def stocks_page(request: Request):
    stocks = await stock.list_stocks()
    return templates.TemplateResponse("stock_index.html", {"request": request, "stocks": stocks})


@router.get("/create", response_class=HTMLResponse)
async def stocks_create_page(request: Request):
    return templates.TemplateResponse("stock_create.html", {"request": request})

@router.post("/stocks")
async def stocks_create(request: Request):
    return await stock.create_stock(request)

@router.get("/edit/{stock_id}", response_class=HTMLResponse)
async def stocks_edit_page(request: Request, stock_id: str):
    return await stock.stock_edit(request, stock_id)

@router.post("/update/{stock_id}")
async def stocks_update(request: Request, stock_id: str):
    return await stock.update_stock(request, stock_id)

@router.post("/delete/{stock_id}")
async def stocks_delete(stock_id: str):
    return await stock.delete_stock(stock_id)


@router.get("/api/stocks")
async def api_stocks():
    stocks = await stock.list_stocks()
    return [stock.__dict__ for stock in stocks]

@router.post("/api/update-price")
async def api_update_price(request: Request):
    data = await request.json()
    stock_id = data["stock_id"]
    new_price = float(data["price"])
    Stock.update_stock_price(stock_id, new_price)
    return {"status": "Preço atualizado"}

