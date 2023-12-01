from typing import Callable, Type
from pydantic import BaseModel
from flask import request


def body_to_model(model: Type[BaseModel]):
    def func_wrapper(func: Callable):
        def serializesr(*args, **kwargs):
            view_model = model.model_validate(request.json)
            return func(*args, view_model, **kwargs)

        return serializesr

    return func_wrapper


def query_to_model(model: Type[BaseModel]):
    def func_wrapper(func: Callable):
        def serializer(*args, **kwargs):
            param = model.model_validate(request.args.to_dict())
            return func(*args, param, **kwargs)

        return serializer

    return func_wrapper
