from urllib.request import Request

from Controllers.UserController import *
from Models.User import User
class UserFactories:
    @staticmethod
    def create_user_service():
        return UserFacade()
class UserFacade:
    @staticmethod
    async def create_user():
        return await create_users()
    @staticmethod
    async def list_users():
        return await list_users()
    @staticmethod
    async def get_user(user_id:str):
        return await get_user(user_id)
    @staticmethod
    async def user_edit(user_id:str):
        return await user_edit(user_id)
    @staticmethod
    async def update_user(request:Request,user_id:str):
        return await update_user(request,user_id)
    @staticmethod
    async def delete_user(user_id:str):
        return await delete_user(user_id)
    @staticmethod
    async def transfer_balance(request:Request):
        return await transfer_balance(request)
