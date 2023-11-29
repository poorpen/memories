from typing import Callable, Type
from pydantic import BaseModel
from flask import request


def body_to_model(model: Type[BaseModel]):
    def func_wrapper(func: Callable):
        def serializer(*args, **kwargs):
            view_model = model.model_validate(request.json)
            return func(view_model, *args, **kwargs)

        return serializer

    return func_wrapper


def query_to_model(model: Type[BaseModel]):
    def func_wrapper(func: Callable):
        def serializer(*args, **kwargs):
            param = model.model_validate(request.args.to_dict())
            return func(param, *args, **kwargs)

        return serializer

    return func_wrapper
