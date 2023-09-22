from typing import Union
from datetime import datetime
from uuid import UUID
from sqlalchemy import select, update, and_

from sqlalchemy.ext.asyncio import AsyncSession

from db.models import Role, User


class UserDAL:
    
    
    def __init__(self, db_session: AsyncSession):
        self.db_session = db_session
    
    
    async def create_user(
        self,
        first_name: str,
        second_name: str,
        email: str,
        password_hash: str,
        birth_date: datetime,
        roles: list[Role]
    ) -> User:
        new_user = User(
            first_name=first_name,
            second_name=second_name,
            email=email,
            password_hash=password_hash,
            birth_date=birth_date,
            roles=roles,
        )
        self.db_session.add(new_user)
        await self.db_session.flush()
        return new_user
    
    
    async def get_user_by_id(self, user_id: UUID) -> Union[User, None]:
        query = select(User).where(User.id == user_id)
        res = await self.db_session.execute(query)
        user_row = res.fetchone()
        if user_row is not None:
            return user_row[0]
    
    
    async def get_user_by_email(self, email: str) -> Union[User, None]:
        query = select(User).where(User.email == email)
        res = await self.db_session.execute(query)
        user_row = res.fetch_one()
        if user_row is not None:
            return user_row[0]
        
    
    async def delete_user(self, user_id: UUID) -> Union[UUID, None]:
        query = (
            update(User)
            .where(and_(User.id == user_id, User.is_disabled == False))
            .values(is_disabled = True)
            .returning(User.id)
        )
        res = await self.db_session.execute(query)
        deleted_user_id_row = res.fetchone()
        if deleted_user_id_row is not None:
            return deleted_user_id_row[0]
    
    
    async def update_user(self, user_id: UUID, **kwargs) -> Union[UUID, None]:
        query = (
            update(User)
            .where(and_(User.id == user_id, User.is_disabled == False))
            .values(kwargs)
            .returning(User.id)
        )
        res = await self.db_session.execute(query)
        updated_user_id_row = res.fetchone()
        if updated_user_id_row is not None:
            return updated_user_id_row[0]
        
    
    async def get_user_list_by_group_name(self, group_name):
        pass