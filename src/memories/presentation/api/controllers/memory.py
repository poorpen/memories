from flask import Blueprint

from memories.presentation.api.controllers.utils import data_to_models
from memories.presentation.api.controllers import requests, responses


memories_router = Blueprint("memories", __name__, url_prefix="/memories")
