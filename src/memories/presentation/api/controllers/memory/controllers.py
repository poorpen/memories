import json

from flask import Response, g


from memories.applications.memory.models import command, query
from memories.presentation.api.controllers.common import data_to_models
from memories.presentation.api.controllers.memory import requests, responses
from memories.presentation.api.controllers.memory.router import memories_router


@memories_router.route("/", methods=["POST"], endpoint="add_memory")
@data_to_models.body_to_model(requests.AddMemory)
def add_memory(memory: requests.AddMemory):
    memory_id = g.director.execute(
        command.CreateMemory(memory.title, memory.text, memory.photo)
    )
    return Response(responses.MemoryId(id=memory_id).model_dump_json(), status=201)


@memories_router.route("/my", methods=["GET"], endpoint="my_memories")
@data_to_models.query_to_model(requests.GetMemories)
def get_my_memories(query_param: requests.GetMemories):
    memories = g.director.execute(
        query.GetMyMemories(query_param.limit, query_param.offset)
    )
    return Response(
        [responses.Memory(**memory.__dict__).model_dump_json() for memory in memories]
    )


@memories_router.route("/feed", methods=["GET"], endpoint="feed_memories")
@data_to_models.query_to_model(requests.GetMemories)
def get_feed_memories(query_param: requests.GetMemories):
    memories = g.director.execute(
        query.GetOtherMemories(query_param.limit, query_param.offset)
    )
    print(memories)
    return Response(
        [responses.Memory(**memory.__dict__).model_dump_json() for memory in memories]
    )


@memories_router.route(
    "/<int:memory_id>/text/", methods=["PATCH"], endpoint="update_text"
)
@data_to_models.body_to_model(requests.UpdateText)
def update_text_in_memory(text_block: requests.UpdateText, memory_id: int):
    g.director.execute(command.UpdateText(memory_id, text_block.title, text_block.text))
    return Response(status=204)


@memories_router.route(
    "/<int:memory_id>/media/", methods=["PATCH"], endpoint="update_media"
)
@data_to_models.body_to_model(requests.UpdateMedia)
def update_media_in_memory(media: requests.UpdateMedia, memory_id: int):
    g.director.execute(command.UpdateMedia(memory_id, media.photo))
    return Response(status=204)


@memories_router.route("/<int:memory_id>/", methods=["DELETE"], endpoint="delete_media")
def delete_memory(memory_id: int):
    g.director.execute(command.DeleteMemory(memory_id))
    return Response(status=204)
