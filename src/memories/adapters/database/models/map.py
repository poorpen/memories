from memories.adapters.database.models.user import map_user
from memories.adapters.database.models.memory import map_memory


def register_all_maps():
    map_user()
    map_memory()
