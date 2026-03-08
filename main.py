import asyncio
import logging
import os
import json
from dotenv import load_dotenv
from FragmentAPI import AsyncFragmentAPI
from FragmentAPI.exceptions import UserNotFoundError

# Load secrets from .env file
load_dotenv()

# Setup logging to show full details
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
        wallet_version="V4R2"  # Use "V4R2" if Tonkeeper says V4R2
    )

    try:
        target = "primehimel"
        amount = 50
        
        logger.info(f"--- FETCHING RECIPIENT DATA ---")
        user = await api.get_recipient_stars(target)
        
        # LOGGING FULL API RESULT FOR USER LOOKUP
        # Use json.dumps to make it pretty and readable
        logger.info(f"RAW USER RESULT: {json.dumps(user.__dict__, indent=4)}")

        if not user.found:
            logger.error(f"User {target} not found.")
            return

        logger.info(f"--- ATTEMPTING PURCHASE ---")
        result = await api.buy_stars(target, amount)
        
        # LOGGING FULL API RESULT FOR PURCHASE
        # This will show the exact 'error' and 'success' fields from the server
        logger.info(f"RAW PURCHASE RESULT: {json.dumps(result.__dict__, indent=4)}")
        
        if result.success:
            logger.info("SUCCESS: Purchase confirmed.")
        else:
            logger.error(f"FAILED: Server returned error -> {result.error}")

    except UserNotFoundError:
        logger.error("User not found error triggered.")
    except Exception as e:
        logger.exception(f"Unexpected error: {e}")
    finally:
        await api.close()
        logger.info("Connection closed.")

if __name__ == "__main__":
    asyncio.run(main())
