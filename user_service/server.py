"""Handles User App Server"""
from sqlalchemy import inspect
from starlette.applications import Starlette
from starlette.routing import Route
from starlette.middleware import Middleware
from starlette.middleware.cors import CORSMiddleware
from user_service.endpoints.user_endpoint import UserEndpoint
from user_service.endpoints.swagger_doc import SwaggerDoc
from user_service.models import DB_ENGINE, BASE

user_endpoint: UserEndpoint = UserEndpoint()
swagger_doc: SwaggerDoc = SwaggerDoc()

routes: list[Route] = [
    Route("/user", user_endpoint.create_user, methods=["POST"]),
    Route("/user/{id}", user_endpoint.update_user, methods=["PATCH"]),
    Route("/user/{id}", user_endpoint.delete_user, methods=["DELETE"]),
    Route("/user/{id}", user_endpoint.fetch_user, methods=["GET"]),
    Route("/user-service/docs", swagger_doc.swagger_ui, methods=["GET"]),
    Route("/spec", swagger_doc.get_spec, methods=["GET"]),
]

middleware = [
    Middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    ),
]


def on_startup():
    """Check if table exist or not and create table"""
    inspector = inspect(DB_ENGINE)
    if not inspector.has_table("User"):
        BASE.metadata.create_all(DB_ENGINE)


app: Starlette = Starlette(routes=routes, middleware=middleware)

app.add_event_handler("startup", on_startup)
