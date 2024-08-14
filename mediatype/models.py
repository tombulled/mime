from dataclasses import dataclass, field
from typing import ClassVar, Mapping, MutableMapping, Optional

"""
from neoclient import MediaType

MediaType.APPLICATION_JSON

from neoclient.mediatype import MediaType, APPLICATION_JSON
"""

__all__ = ("MediaType",)


@dataclass
class MediaType:
    type: str
    subtype: str # NOTE: Can contain a prefix (aka "tree") and a suffix
    # suffix: Optional[str] = None # TODO: Keep me?
    parameters: Mapping[str, str] = field(default_factory=dict)

    def __repr__(self) -> str:
        return f"{type(self).__name__}({self.string()!r})"

    def __str__(self) -> str:
        return self.string()

    def string(self, suffix: bool = True, parameters: bool = True) -> str:
        return "".join(
            (
                f"{self.type}/",
                f"{self.subtype}",
                # f"+{self.suffix}" if suffix and self.suffix else "",
                "; " if parameters and self.parameters else "",
                "; ".join(f'{key}="{value}"' for key, value in self.parameters.items())
                if parameters and self.parameters
                else "",
            ),
        )
    
    def sort(self):
        raise NotImplementedError # TODO
