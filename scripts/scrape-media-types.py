import enum
import json
import typing
from pprint import pprint as pp

import addict
import parse
import pydantic
import requests
import xmltodict


def fetch():
    resp = requests.get("https://www.iana.org/assignments/media-types/media-types.xml")

    data = addict.Dict(xmltodict.parse(resp.text, xml_attribs=False))

    parsed = {}

    for registry in data.registry.registry:
        media_type = registry.title.lower()

        parsed[media_type] = {}

        for record in registry.record:
            if not record.file:
                continue

            media_subtype = parse.parse(
                f"{media_type}/{{name}}", record.file.lower()
            ).named["name"]
            media_suffix = None

            if result := parse.parse("{prefix}+{suffix}", media_subtype):
                media_subtype = result.named["prefix"]
                media_suffix = result.named["suffix"]

            parsed[media_type].setdefault(media_subtype, set())

            if media_suffix:
                parsed[media_type][media_subtype].add(media_suffix)

    return parsed


d = fetch()

# with open('data.json', 'w') as file:
#     json.dump(d, file)

media_types = set()
media_subtypes = set()
media_suffixes = set()

for media_type in d:
    media_types.add(media_type)

    for media_subtype in d[media_type]:
        media_subtypes.add(media_subtype)

        for media_suffix in d[media_type][media_subtype]:
            media_suffixes.add(media_suffix)

"""
MediaType = enum.Enum \
(
    'MediaType',
    {
        media_type.upper(): media_type.lower()
        for media_type in media_types
    }
)

MediaSubtype = enum.Enum \
(
    'MediaSubtype',
    {
        media_subtype.replace('.', '').replace('-', '').upper(): media_subtype.lower()
        for media_subtype in media_subtypes
    }
)

MediaSuffix = enum.Enum \
(
    'MediaSuffix',
    {
        media_suffix.replace('-', '_').upper(): media_suffix.lower()
        for media_suffix in media_suffixes
    }
)

class MimeType(pydantic.BaseModel):
    type:       MediaType
    subtype:    MediaSubtype
    suffix:     typing.Optional[MediaSuffix]
    parameters: typing.Optional[typing.Dict[str, str]]

json = MimeType \
(
    type    = MediaType.APPLICATION,
    subtype = MediaSubtype.JSON,
)
"""
