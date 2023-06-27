import functools
from typing import Type

from src.controller.adapter.base import BaseAdapter
from src.controller.adapter.http import HttpAdapter
from src.presentation.models.block_number import BlockNumberResponse, BlockNumberRequest


class Client:
    __adapter_class: BaseAdapter

    def __init__(self, api_key: str, adapter_class: Type[BaseAdapter] = HttpAdapter):
        self.__adapter_class = adapter_class

    async def get_balance(self) -> BlockNumberResponse:
        async with self.__adapter_class() as adapter:
            return await adapter.send_request(BlockNumberRequest(), response_type=BlockNumberResponse)
