from types import TracebackType
from typing import Protocol, Type, TypeVar

from src.infra.models.request import RequestModel
from src.infra.models.response import ResponseModel

RequestT = TypeVar("RequestT", bound=RequestModel)
ResponseT = TypeVar("ResponseT", bound=ResponseModel)


class BaseAdapter(Protocol):
    async def __aenter__(self) -> "BaseAdapter":
        pass

    async def __aexit__(self,
                        exc_type: Type[BaseException] | None,
                        exc_val: BaseException | None,
                        exc_tb: TracebackType | None) -> None:
        pass

    async def send_request(self, data: RequestT, response_type: Type[ResponseT]) -> ResponseT:
        pass
