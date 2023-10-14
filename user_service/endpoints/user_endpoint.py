"""Handles endpoints for user service"""
from starlette.requests import Request
from starlette.responses import JSONResponse
from sqlalchemy.exc import IntegrityError
from user_service.services.user_service import UserService
from user_service.models import ASYNC_DB_ENGINE
from user_service.exceptions import UserExistError, UserDoesNotExistError


class UserEndpoint:
    """endpoint class to handle user services"""

    svc: UserService = UserService(ASYNC_DB_ENGINE)
    CREATED: int = 201
    SUCCESS: int = 200
    CONFLICT: int = 409
    NOT_FOUND: int = 404

    @classmethod
    async def create_user(cls, request: Request) -> JSONResponse:
        """Handles create user service"""

        try:
            payload: dict[str, str] = await request.json()
            user: dict[str, str] = await cls.svc.create_user_service(payload)
            return JSONResponse(user, status_code=cls.CREATED)
        except IntegrityError:
            return JSONResponse(UserExistError.error(), status_code=cls.CONFLICT)

    @classmethod
    async def update_user(cls, request: Request) -> JSONResponse:
        """Handles update user service"""

        try:
            payload: dict[str, str] = await request.json()
            payload["id"] = request.path_params["id"]
            user: dict[str, str] = await cls.svc.update_user_service(payload)
            return JSONResponse(user, status_code=cls.SUCCESS)
        except AttributeError:
            return JSONResponse(
                UserDoesNotExistError.error(), status_code=cls.NOT_FOUND
            )

    @classmethod
    async def delete_user(cls, request: Request) -> JSONResponse:
        """Handles delete user service"""

        try:
            user_id: str = request.path_params["id"]
            await cls.svc.delete_user_service(user_id)
            return JSONResponse(None, status_code=cls.SUCCESS)
        except AttributeError:
            return JSONResponse(
                UserDoesNotExistError.error(), status_code=cls.NOT_FOUND
            )

    @classmethod
    async def fetch_user(cls, request: Request) -> JSONResponse:
        """Handles fetch user service"""

        try:
            user_id: str = request.path_params["id"]
            user: dict[str, str] = await cls.svc.read_user_service(user_id)
            return JSONResponse(user, status_code=cls.SUCCESS)
        except AttributeError:
            return JSONResponse(
                UserDoesNotExistError.error(), status_code=cls.NOT_FOUND
            )
