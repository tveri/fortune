from typing import Union

from sqlalchemy.ext.asyncio import AsyncSession
from uuid import UUID

from db.models import Role, User
from db.dals import UserDAL
from api.schemas import ShowUser, CreateUser

from hashing import Hasher


async def _create_new_user(body: CreateUser, session: AsyncSession) -> ShowUser:
    async with session.begin():
        user_dal = UserDAL(session)
        user = await user_dal.create_user(
            first_name=body.first_name,
            second_name=body.second_name,
            email=body.email,
            password_hash=Hasher.get_password_hash(body.password),
            birth_date=body.birth_date,
            roles=[
                Role.USER_ROLE,
            ],
        )
        return ShowUser(
            id=user.id,
            first_name=user.first_name,
            second_name=user.second_name,
            email=user.email,
            birth_date=user.birth_date,
            is_disabled=user.is_disabled,
        )


async def _update_user(
    updation_user_params: dict,
    user_id: UUID,
    session: AsyncSession,
) -> Union[UUID, None]:
    async with session.begin():
        user_dal = UserDAL(session)
        updated_user_id = await user_dal.update_user(
            user_id=user_id, 
            **updation_user_params
        )
        return updated_user_id
        

async def _delete_user(user_id: UUID, session: AsyncSession) -> Union[UUID, None]:
    async with session.begin():
        user_dal = UserDAL(session)
        deleted_user_id = await user_dal.delete_user(user_id)
        return deleted_user_id


async def _get_user_by_id(user_id: UUID, session: AsyncSession) -> Union[User, None]:
    async with session.begin():
        user_dal = UserDAL(session)
        user = await user_dal.get_user_by_id(user_id)
        return user
        

async def _get_users_by_group_name(group_name):
    user_dal = UserDAL()
    return await user_dal.get_user_list_by_group_name(group_name)
