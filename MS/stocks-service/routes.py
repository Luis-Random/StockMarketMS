from fastapi import APIRouter, Request # type: ignore
from fastapi.responses import HTMLResponse # type: ignore
from fastapi.templating import Jinja2Templates # type: ignore
#from Controllers.StockController import *
from Models.Stock import Stock # type: ignore
from factories.stock_factories import StockFactories
from Database.database import get_stock_price_history

router = APIRouter()
templates = Jinja2Templates(directory="views")
stockFactory = StockFactories.create_stock_service()

@router.get("/stocks-page", response_class=HTMLResponse)
async def stocks_page(request: Request):
    stocks = await stockFactory.list_stocks()
    return templates.TemplateResponse("stock_index.html", {"request": request, "stocks": stocks})


@router.get("/create", response_class=HTMLResponse)
async def stocks_create_page(request: Request):
    return templates.TemplateResponse("stock_create.html", {"request": request})


@router.get("/edit/{stock_id}", response_class=HTMLResponse)
async def stocks_edit_page(request: Request, stock_id: str):
    return await stockFactory.stock_edit(request, stock_id)
# ---------------- ACTION ROUTES ------------------

@router.post("/stocks")
async def stocks_create(request: Request):
    return await stockFactory.create_stock(request)

@router.post("/update/{stock_id}")
async def stocks_update(request: Request, stock_id: str):
    return await stockFactory.update_stock(request, stock_id)

@router.post("/delete/{stock_id}")
async def stocks_delete(stock_id: str):
    return await stockFactory.delete_stock(stock_id)


@router.get("/api/stocks")
async def api_stocks():
    stocks = await stockFactory.list_stocks()
    return [stock.__dict__ for stock in stocks]

@router.post("/api/update-price")
async def api_update_price(request: Request):
    data = await request.json()
    stock_id = data["stock_id"]
    new_price = float(data["price"])
    Stock.update_stock_price(stock_id, new_price)
    return {"status": "Preço atualizado"}

@router.get("/api/stocks/history")
async def get_stock_history():
    try:
        return get_stock_price_history()
    except Exception as e:
        import traceback
        traceback.print_exc()
        return {"error": str(e)}
        '''
