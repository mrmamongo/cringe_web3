def to_hex(value: int):
    return hex(value)


def from_hex(value: str):
    assert value.startswith("0x")
    return int(value, 16)
