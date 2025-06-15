from Controllers.OrderController import *
from Models.Order import *
class OrdersFactories:
     @staticmethod
     def create_order_service():
          return OrderFacade()
class OrderFacade:
     @staticmethod
     async def fetch_users():
          return await fetch_users()
     @staticmethod
     async def fetch_stocks():
          return await fetch_stocks()
     @staticmethod
     async def transfer_balance(buyer_id:str, seller_id:str, amount:float):
          return await transfer_balance(buyer_id, seller_id, amount)
     @staticmethod
     async def list_orders():
          return await list_orders()
     @staticmethod
     async def process_order_matching(order: Order):
          return await process_order_matching(order)
     @staticmethod
     async def create_order(request:Request):
          return await create_order(request)
     @staticmethod
     async def order_edit(request:Request, order_id: str):
          return await order_edit(request, order_id)
     @staticmethod
     async def update_order(request:Request, order_id: str):
          return await update_order(request, order_id)
     @staticmethod
     async def delete_order(order_id: str):
          return await delete_order(order_id)

