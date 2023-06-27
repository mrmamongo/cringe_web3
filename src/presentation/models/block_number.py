from dataclasses import dataclass, field

from src.infra import utils
from src.infra.models.request import RequestModel
from src.infra.models.response import ResponseModel


@dataclass
class BlockNumberRequest(RequestModel):
    params = []


@dataclass
class BlockNumberResponse(ResponseModel):
    def __post_init__(self):
        self.result = str(utils.from_hex(self.result))
