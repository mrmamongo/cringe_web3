from enum import Enum


class METHOD(str, Enum):
    UNSET = "UNSET"
    block_number = "eth_blockNumber"
    get_balance = "eth_getBalance"
