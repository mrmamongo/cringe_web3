import asyncio

from src.presentation.client import Client


async def main():
    client = Client("e8e6eab701504a82a8b88841b2dc3e68")
    balance = await client.get_balance()

    print(balance)

if __name__ == '__main__':
    asyncio.run(main())