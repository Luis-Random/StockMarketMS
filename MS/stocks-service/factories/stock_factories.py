from Controllers.StockController import *
from Models.Stock import Stock
class StockFactories:
    @staticmethod
    def create_stock_service():
        return StockFacade()
class StockFacade:
    @staticmethod
    async def list_stocks():
        return stock.all()
    @staticmethod
    async def create_stock(request:Request):
        return create_stock(request)
    @staticmethod
    async def stock_edit(request:Request, stock_id:str):
        return stock_edit(request,stock_id)
    @staticmethod
    async def update_stock(request:Request, stock_id:str):
        return update_stock(request,stock_id)
    @staticmethod
    async def delete_stock(stock_id:str):
        return delete_stock(stock_id)
