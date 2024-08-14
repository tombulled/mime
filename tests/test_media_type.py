import pytest

import mediatype


@pytest.fixture
def media_type() -> mediatype.MediaType:
    return mediatype.MediaType(
        type="type",
        subtype="subtype",
        suffix="suffix",
        parameters={"key1": "val1", "key2": "val2"},
    )


@pytest.fixture
def string() -> str:
    return 'type/subtype+suffix; key1="val1"; key2="val2"'


def test_str(media_type: mediatype.MediaType, string: str) -> None:
    assert str(media_type) == string


def test_parser(media_type: mediatype.MediaType, string: str) -> None:
    assert mediatype.parse(string) == media_type
