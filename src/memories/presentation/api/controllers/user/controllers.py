from flask import Blueprint, Response, g

from memories.applications.user.models import command
from memories.presentation.api.controllers.common import data_to_models
from memories.presentation.api.controllers.user import requests
from memories.presentation.api.controllers.user.router import users_router


@users_router.route("/", methods=["POST"])
@data_to_models.body_to_model(requests.RegisterUser)
def register_user(user: requests.RegisterUser):
    g.director.execute(command.RegisterUser(user.email_address, user.password))
    return Response(status=201)
