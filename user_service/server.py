"""Handles User App Server"""
from starlette.applications import Starlette
from starlette.routing import Route
from starlette.middleware import Middleware
from starlette.middleware.cors import CORSMiddleware
from user_service.endpoints.user_endpoint import UserEndpoint
from user_service.endpoints.swagger_doc import SwaggerDoc

user_endpoint: UserEndpoint = UserEndpoint()
swagger_doc: SwaggerDoc = SwaggerDoc()

routes: list[Route] = [
    Route("/user", user_endpoint.create_user, methods=["POST"]),
    Route("/user/{id}", user_endpoint.update_user, methods=["PATCH"]),
    Route("/user/{id}", user_endpoint.delete_user, methods=["DELETE"]),
    Route("/user/{id}", user_endpoint.fetch_user, methods=["GET"]),
    Route("/docs", swagger_doc.swagger_ui, methods=["GET"]),
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

app: Starlette = Starlette(routes=routes, middleware=middleware)
