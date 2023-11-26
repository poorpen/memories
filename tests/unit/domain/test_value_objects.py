import os

import pytest
import faker
from typing import Type, Tuple, Any

from memories.domain.memory.value_objects import text_block, media


@pytest.mark.parametrize(
    "value_object_class, value_object_args",
    [
        (text_block.Title, ("some title",)),
        (text_block.Text, ("some text",)),
        (media.Photo, ("http://www.example.com/photo.jpg",)),
    ],
)
def test_valid_value_object(value_object_class: Type, value_object_args: Tuple[Any]):
    value_object = value_object_class(*value_object_args)
    assert value_object.raw_value == value_object_args[0]


@pytest.mark.parametrize(
    "value_object_class, exception, value_object_args",
    [
        (text_block.Title, text_block.StringIsEmpty, ("",)),
        (text_block.Title, text_block.StringIsEmpty, ("     ",)),
        (
            text_block.Title,
            text_block.CharacterLimitExceeded,
            (
                "".join(
                    (faker.Faker()).random_elements(
                        elements=("a", "b", "c", " "), length=80
                    )
                ),
            ),
        ),
        (media.Photo, media.InvalidPhotoURL, (" ",)),
        (media.Photo, media.InvalidPhotoURL, ("http://example",)),
        (media.Photo, media.InvalidPhotoURL, ("http://example.com:80:80",)),
        (
            media.Photo,
            media.InvalidPhotoURL,
            {"photo_url": "http://example.com/path with spaces"},
        ),
    ],
)
def test_invalid_value_object(
    value_object_class: Type,
    exception: Type[Exception],
    value_object_args: Tuple[Any],
):
    with pytest.raises(exception):
        value_object_class(*value_object_args)
