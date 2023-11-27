from sqlalchemy import MetaData
from sqlalchemy.orm import registry

metadata_obj = MetaData()
mapper_registry = registry()
