"""Handles endpoints for user service"""
from starlette.requests import Request
from sqlalchemy import Engine
from sqlalchemy.orm import sessionmaker


class UserEndpoint:
    """endpoint class to handle user services"""

    def __init__(self, db_engine: Engine) -> None:
        self.session = sessionmaker(db_engine)

    def create_user(self, _: Request) -> None:
        """Handles create user service"""
        raise NotImplementedError()

    def update_user(self, _: Request) -> None:
        """Handles update user service"""
        raise NotImplementedError()

    def delete_user(self, _: Request) -> None:
        """Handles delete user service"""
        raise NotImplementedError()

    def fetch_user(self, _: Request) -> None:
        """Handles fetch user service"""
        raise NotImplementedError()
