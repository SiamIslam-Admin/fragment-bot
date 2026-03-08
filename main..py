import os
import asyncio
from FragmentAPI import AsyncFragmentAPI

async def main():
    api = AsyncFragmentAPI(
        cookies=os.getenv("FRAGMENT_COOKIES"),
        hash_value=os.getenv("FRAGMENT_HASH"),
        wallet_mnemonic=os.getenv("WALLET_MNEMONIC"),
        wallet_api_key=os.getenv("WALLET_API_KEY")
    )

    user = await api.get_recipient_stars("username")
    print(f"Name: {user.name}")

    result = await api.buy_stars("username", 100)
    if result.success:
        print(f"TX: {result.transaction_hash}")

    result = await api.buy_stars("primehimel", 100, show_sender=True)

    transfer = await api.transfer_ton("recipient.t.me", 0.5, "Payment")
    if transfer.success:
        print(f"Transfer: {transfer.transaction_hash}")

    await api.close()

asyncio.run(main())
