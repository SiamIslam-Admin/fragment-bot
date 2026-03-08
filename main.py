import asyncio
import logging
from FragmentAPI import AsyncFragmentAPI
from FragmentAPI.exceptions import UserNotFoundError

# 1. Setup logging
logging.basicConfig(
    level=logging.INFO,
    format='%(levelname)s: %(message)s'
)
logger = logging.getLogger(__name__)

async def main():
    # --- CONFIGURATION AREA ---
    # 1. Get FRESH cookies from Fragment.com (Network Tab)
    # 2. Verify your wallet version in Tonkeeper (V4R2 or W5)
    api = AsyncFragmentAPI(
        cookies="stel_ssid=73fe99ee138ed81a27_36735179866457374; stel_token=7a6e0889befdc57613c4f245127815287a6e08937a6e0061de7d3a52a28883e689a88",
        hash_value="c3d0ea624e192dd63c",
        wallet_mnemonic="differ color hold primary ensure illegal clap orange borrow lock essence verify pipe exchange auto venue flock jaguar black submit garbage injury city jealous",
        wallet_api_key="462217391156217a1be5819e36e69d389016b87c97242cd481ebe73e39731434",
        wallet_version="V4R2"  # Use "V4R2" if Tonkeeper says V4R2
    )

    try:
        # STEP 1: Verify Wallet Address
        # This confirms if the script is looking at the right wallet
        address = await api.get_wallet_address()
        logger.info(f"VERIFICATION: Script is using wallet address: {address}")
        logger.info("Compare this address with your Tonkeeper/Telegram wallet!")

        target = "primehimel"
        amount = 50
        
        logger.info(f"Checking recipient: {target}")
        user = await api.get_recipient_stars(target)
        
        if user.found:
            logger.info(f"Recipient Found: {user.name}")
            
            # STEP 2: Execute Purchase
            logger.info(f"Attempting to buy {amount} stars...")
            result = await api.buy_stars(target, amount)
            
            if result.success:
                logger.info(f"SUCCESS! TX Hash: {result.transaction_hash}")
            else:
                # If 'Access denied' happens here, your cookies or hash are invalid
                logger.error(f"FAILED: {result.error}")
                if "Access denied" in str(result.error):
                    logger.warning("PRO-TIP: Refresh your stel_ssid and stel_token cookies!")
        else:
            logger.error("Target user not found on Fragment.")

    except UserNotFoundError:
        logger.error(f"Error: The username '{target}' does not exist.")
    except Exception as e:
        logger.exception(f"An unexpected error occurred: {e}")
    finally:
        await api.close()
        logger.info("Connection closed.")

if __name__ == "__main__":
    asyncio.run(main())
