import pytest


@pytest.mark.parametrize(
    "data_for_update",
    [
        {"title": "some title", "text": "some text"},
        {"title": None, "text": "some text"},
        {"title": "some title", "text": None},
    ],
)
def test_valid_update_text_block(fake_memory, data_for_update):
    old_values = {"title": fake_memory.title, "text": fake_memory.text}
    fake_memory.update_text_block(**data_for_update)
    expected_values = dict()
    for k, v in data_for_update.items():
        if not v:
            value = old_values[k]
        else:
            value = v
        expected_values[k] = value
    assert fake_memory.title == expected_values["title"]
    assert fake_memory.text == expected_values["text"]
    assert fake_memory.create_at < fake_memory.update_at


def test_invalid_update_text_block(fake_memory):
    fake_memory.update_text_block()
    assert fake_memory.create_at == fake_memory.update_at
