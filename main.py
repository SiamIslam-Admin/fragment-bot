import asyncio
import logging
import json
from FragmentAPI import AsyncFragmentAPI
from FragmentAPI.exceptions import UserNotFoundError

# 1. Setup logging to stdout for Railway
logging.basicConfig(
    level=logging.INFO,
    format='%(levelname)s: %(message)s'
)
logger = logging.getLogger(__name__)

async def main():
    api = AsyncFragmentAPI(
        cookies="stel_ssid=73fe99ee138ed81a27_36735179866457374; stel_token=7a6e0889befdc57613c4f245127815287a6e08937a6e0061de7d3a52a28883e689a88",
        hash_value="c3d0ea624e192dd63c",
        wallet_mnemonic="differ color hold primary ensure illegal clap orange borrow lock essence verify pipe exchange auto venue flock jaguar black submit garbage injury city jealous",
        wallet_api_key="462217391156217a1be5819e36e69d389016b87c97242cd481ebe73e39731434",
        wallet_version="W5"   # try V4R2 first
        # wallet_version="W5"    # if your wallet is V5, test this instead
    )

    try:
        target = "primehimel"
        
        # Log the start of the process
        logger.info(f"Starting request for target: {target}")

        # Get recipient info
        user = await api.get_recipient_stars(target)
        # Log the full user object/response
        logger.info(f"Recipient Found - Name: {user.name}, Full Info: {user.__dict__}")

        # Buy stars
        amount = 50
        result = await api.buy_stars(target, amount)
        
        # Log the full purchase result
        if result.success:
            logger.info(f"SUCCESS: Bought {amount} stars for {target}. TX: {result.transaction_hash}")
            logger.info(f"Full Response Data: {result.__dict__}")
        else:
            logger.error(f"FAILURE: Buy stars failed for {target}. Response: {result.__dict__}")

    except UserNotFoundError as e:
        logger.error(f"User Not Found Error: {e}")

    except Exception as e:
        # This will log the full traceback for unexpected errors
        logger.exception(f"Unexpected error occurred during execution: {e}")

    finally:
        await api.close()
        logger.info("API connection closed.")

if __name__ == "__main__":
    asyncio.run(main())
