"""Handles endpoints for user service"""
from starlette.requests import Request


class UserEndpoint:
    """endpoint class to handle user services"""

    def __init__(self) -> None:
        pass

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
