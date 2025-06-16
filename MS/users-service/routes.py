from fastapi import APIRouter, Request  
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates  
#from Controllers.UserController import *
from factories.user_factories import UserFactories

router = APIRouter()
templates = Jinja2Templates(directory="views")
userFactory = UserFactories.create_user_service()

router.add_api_route("/create-user", userFactory.create_user, methods=["POST"])
router.add_api_route("/get-user/{user_id}", userFactory.get_user, methods=["GET"])
@router.post("/api/transfer")
async def api_transfer_balance(request: Request):
    return await userFactory.transfer_balance(request)

@router.get("/users-page", response_class=HTMLResponse)
async def users_page(request: Request):
    users = await userFactory.list_users()
    return templates.TemplateResponse("user_index.html", {"request": request, "users": users})

@router.get("/create", response_class=HTMLResponse)
async def users_create_page(request: Request):
    return templates.TemplateResponse("user_create.html", {"request": request})



@router.get("/edit/{user_id}", response_class=HTMLResponse)
async def edit_user_view(request: Request, user_id: str):
    return await userFactory.user_edit(request, user_id)

@router.post("/update-user/{user_id}")
async def update_user_route(request: Request, user_id: str):
    return await userFactory.update_user(request, user_id)

@router.post("/delete-user/{user_id}")
async def delete_user_route(user_id: str):
    return await userFactory.delete_user(user_id)


@router.get("/api/users")
async def api_users():
    users = await userFactory.list_users()
    return [user.__dict__ for user in users]
