from types import TracebackType
from typing import Type, TypeVar

from aiohttp import ClientSession

from src.controller.adapter.base import BaseAdapter
from src.infra.adaptix.retort import retort
from src.infra.models.request import RequestModel
from src.infra.models.response import ResponseModel

RequestT = TypeVar("RequestT", bound=RequestModel)
ResponseT = TypeVar("ResponseT", bound=ResponseModel)


class HttpAdapter(BaseAdapter):
    __api_key: str
    __session: ClientSession

    def __init__(self, base_url: str = "https://mainfest.infura.io", api_key: str = ""):
        self.__api_key = api_key
        self.__session = ClientSession(base_url=base_url)

    async def __aenter__(self) -> "HttpAdapter":
        await self.__session.__aenter__()
        return self

    async def __aexit__(self,
                        exc_type: Type[BaseException] | None,
                        exc_val: BaseException | None,
                        exc_tb: TracebackType | None) -> None:
        await self.__session.__aexit__(exc_type, exc_val, exc_tb)

    async def send_request(self, data: RequestT, response_type: Type[ResponseT]) -> ResponseT:
        async with self.__session.post(url=f"/v3/{self.__api_key}", json=data.json()) as res:
            if res.status != 200:
                return retort.load(await res.text(), response_type)
