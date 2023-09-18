from fastapi import APIRouter

from api.schemas import ShowUser
from api.actions.user import _get_users_by_group_name

user_router = APIRouter()


@user_router.get('/get_by_group/{group_name}/', response_model=list[ShowUser])
async def get_user_list_by_group_name(group_name):
    return await _get_users_by_group_name(group_name)