from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException

from sqlalchemy.ext.asyncio import AsyncSession

from api.schemas import CreateUser, ShowUser, DeleteUserResponse, UpdateUserRequest, UpdateUserResponse
from api.actions.user import _create_new_user, _get_user_by_id, _get_users_by_group_name, _delete_user, _update_user

from db.session import get_db

user_router = APIRouter()


@user_router.post('/', response_model=ShowUser)
async def create_user(body: CreateUser, db: AsyncSession = Depends(get_db)) -> ShowUser:
    return await _create_new_user(body, db)


@user_router.get('/', response_model=ShowUser)
async def get_user_by_id(user_id: UUID, db: AsyncSession = Depends(get_db)) -> ShowUser:
    return await _get_user_by_id(user_id, db)


@user_router.delete('/', response_model=DeleteUserResponse)
async def delete_user(user_id: UUID, db: AsyncSession = Depends(get_db)) -> DeleteUserResponse:
    deleted_user_id = await _delete_user(user_id, db)
    if deleted_user_id is None:
        raise HTTPException(
            status_code=404,
            detail='User not found',
        )
    return DeleteUserResponse(id=deleted_user_id)


@user_router.patch('/', response_model=UpdateUserResponse)
async def update_user(
    params_to_update: UpdateUserRequest, 
    user_id: UUID, 
    db: AsyncSession = Depends(get_db)
) -> UpdateUserResponse:
    params_to_update = params_to_update.model_dump(exclude_none=True)
    updated_user_id = await _update_user(
        updation_user_params=params_to_update,
        user_id=user_id,
        session=db,
    )
    if updated_user_id is None:
        raise HTTPException(
            status_code=404,
            detail='User not found',
        )
    return UpdateUserResponse(id=updated_user_id)


@user_router.get('/get_by_group/{group_name}/', response_model=list[ShowUser])
async def get_user_list_by_group_name(group_name):
    return await _get_users_by_group_name(group_name)