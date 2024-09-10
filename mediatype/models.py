from dataclasses import dataclass, field
from typing import Mapping

__all__ = ("MediaType",)


@dataclass
class MediaType:
    type: str
    subtype: str
    parameters: Mapping[str, str] = field(default_factory=dict)

    def __repr__(self) -> str:
        return f"{type(self).__name__}({self.string()!r})"

    def __str__(self) -> str:
        return self.string()

    def string(self, *, parameters: bool = True) -> str:
        return "".join(
            (
                f"{self.type}/",
                f"{self.subtype}",
                "; " if parameters and self.parameters else "",
                "; ".join(f'{key}="{value}"' for key, value in self.parameters.items())
                if parameters and self.parameters
                else "",
            ),
        )
    
    def sort(self) -> "MediaType":
        return MediaType(
            type=self.type,
            subtype=self.subtype,
            parameters=dict(sorted(self.parameters.items())),
        )
