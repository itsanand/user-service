"""Handles user services"""
from uuid import uuid4
from sqlalchemy import update, delete
from sqlalchemy.ext.asyncio import AsyncEngine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.asyncio import AsyncSession
from user_service.models import User


class UserService:
    """user service class"""

    def __init__(self, db_engine: AsyncEngine) -> None:
        self.async_session = sessionmaker(
            db_engine, class_=AsyncSession
        )  # type: ignore

    async def create_user_service(self, payload: dict[str, str]) -> dict[str, str]:
        """Create user entity and a unique id for current user
        and create a record in User table.
        NOTE: emailID and phoneNumber are a unique key db will
        throw IntegrityError.
        """

        async with self.async_session() as db_session:  # type: ignore
            try:
                user: User = User(**payload)
                payload["id"] = str(uuid4())
                user.id = payload["id"]  # type: ignore
                db_session.add(user)
                await db_session.commit()
                return payload
            except IntegrityError as error:
                await db_session.rollback()
                raise error
            except Exception as error:
                await db_session.rollback()
                raise error

    async def update_user_service(self, payload: dict[str, str]) -> dict[str, str]:
        """user service to update user details"""

        async with self.async_session() as db_session:  # type: ignore
            try:
                query = update(User).where(User.id == payload["id"]).values(**payload)
                await db_session.execute(query)
                await db_session.commit()
                return await self.read_user_service(payload["id"])
            except IntegrityError as error:
                await db_session.rollback()
                raise error
            except Exception as error:
                await db_session.rollback()
                raise error

    async def read_user_service(self, user_id: str) -> dict[str, str]:
        """Read user based on the user id"""

        async with self.async_session() as db_session:  # type: ignore
            user: User = await db_session.get(User, user_id)
            return {
                "id": user.id,  # type: ignore
                "firstName": user.firstName,  # type: ignore
                "lastName": user.lastName,  # type: ignore
                "emailID": user.emailID,  # type: ignore
                "phoneNumber": user.phoneNumber,  # type: ignore
            }

    async def delete_user_service(self, user_id: str) -> None:
        """Delete user record based on user id"""

        try:
            async with self.async_session() as db_session:  # type: ignore
                _: dict[str, str] = await self.read_user_service(user_id)
                query = delete(User).where(User.id == user_id)
                await db_session.execute(query)
                await db_session.commit()
        except IntegrityError as error:
            await db_session.rollback()
            raise error
        except Exception as error:
            await db_session.rollback()
            raise error
