import asyncio
from FragmentAPI import AsyncFragmentAPI

async def main():
    api = AsyncFragmentAPI(
        cookies="stel_ssid=73fe99ee138ed81a27_36735179866457374; stel_token=7a6e0889befdc57613c4f245127815287a6e08937a6e0061de7d3a52a28883e689a88",
        hash_value="c3d0ea624e192dd63c",
        wallet_mnemonic="differ color hold primary ensure illegal clap orange borrow lock essence verify pipe exchange auto venue flock jaguar black submit garbage injury city jealous",
        wallet_api_key="462217391156217a1be5819e36e69d389016b87c97242cd481ebe73e39731434"
    )

    user = await api.get_recipient_stars('username')
    print(f"Name: {user.name}")

    result = await api.buy_stars('username', 100)
    if result.success:
        print(f"✓ TX: {result.transaction_hash}")

    result = await api.buy_stars('primehimel', 100, show_sender=True)

    transfer = await api.transfer_ton("recipient.t.me", 0.5, "Payment")
    if transfer.success:
        print(f"✓ Transfer: {transfer.transaction_hash}")

    await api.close()

asyncio.run(main())
