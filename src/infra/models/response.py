from dataclasses import dataclass

from src.infra.models.base import BaseJsonApiModel


@dataclass
class ResponseModel(BaseJsonApiModel):
    result: str = ""
