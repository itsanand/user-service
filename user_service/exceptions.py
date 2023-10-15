"""Handles user service related exception"""
from typing import Union


class UserExistError:  # pylint: disable=too-few-public-methods
    """class for user already exists error"""

    @staticmethod
    def error() -> dict[str, Union[str, int]]:
        """user already exists payload"""

        return {"code": 409, "error": "User already exist with the same email or phone"}


class UserDoesNotExistError:  # pylint: disable=too-few-public-methods
    """class for user does not exist error"""

    @staticmethod
    def error() -> dict[str, Union[str, int]]:
        """user does not exist payload"""

        return {"code": 404, "error": "User not Found"}
