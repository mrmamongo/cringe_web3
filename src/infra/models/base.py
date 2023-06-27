from dataclasses import dataclass, field

import orjson

from src.infra.adaptix.retort import retort


@dataclass
class BaseJsonApiModel:
    id: int = field(default=1)
    jsonrpc: str = field(default="2.0")

    def json(self):
        return orjson.dumps(retort.dump(self))
