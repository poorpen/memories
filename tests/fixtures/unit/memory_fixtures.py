import pytest
import faker

from src.memories.domain.memory.value_objects import text_block, media
from src.memories.domain.memory import models


@pytest.fixture
def fake_memory() -> models.Memory:
    fake = faker.Faker()
    return models.Memory(
        title=text_block.Title(fake.word()),
        text=text_block.Text(
            "".join(fake.random_elements(elements=("a", "b", "c", " "), length=500))
        ),
        photo=media.Photo(fake.url()),
        owner_id=1
    )
