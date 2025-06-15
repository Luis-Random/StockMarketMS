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
        return create_users()
    @staticmethod
    async def list_users():
        return list_users()
    @staticmethod
    async def get_user(user_id:str):
        return get_user(user_id)
    @staticmethod
    async def user_edit(user_id:str):
        return user_edit(user_id)
    @staticmethod
    async def update_user(request:Request,user_id:str):
        return update_user(request,user_id)
    @staticmethod
    async def delete_user(user_id:str):
        return delete_user(user_id)
    @staticmethod
    async def transfer_balance(request:Request):
        return transfer_balance(request)
