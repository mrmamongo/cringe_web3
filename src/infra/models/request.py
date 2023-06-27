from dataclasses import dataclass, field

from src.infra.models.base import BaseJsonApiModel
from src.infra.models.method import METHOD


@dataclass
class RequestModel(BaseJsonApiModel):
    method: METHOD = field(default=METHOD.UNSET)
    params: list = field(default_factory=list)
