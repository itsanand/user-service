"""Handles User App Server"""
from starlette.applications import Starlette
from starlette.routing import Route
from user_service.endpoints.user_endpoint import UserEndpoint
from user_service.models import DB_ENGINE

user_endpoint: UserEndpoint = UserEndpoint(DB_ENGINE)

routes: list[Route] = [
    Route("/user", user_endpoint.create_user, methods=["POST"]),
    Route("/user/{id}", user_endpoint.update_user, methods=["PATCH"]),
    Route("/user/{id}", user_endpoint.delete_user, methods=["DELETE"]),
    Route("/user/{id}", user_endpoint.fetch_user, methods=["GET"]),
]

app: Starlette = Starlette(routes=routes)
