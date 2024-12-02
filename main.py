import asyncio
import traceback

import loguru

from services.data_processing import user_data_processing
from services.mbti_analysis import mbti_genai_analysis
from services.twitter_services import get_user_twitter_id_by_apidance, get_user_twitter_data_by_apidance


async def mbti_analysis(username: str):
    try:
        try:
            user_info = await get_user_twitter_id_by_apidance(username)
        except Exception as e:
            loguru.logger.error(e)
            loguru.logger.error(traceback.format_exc())
            return False

        user_id = user_info["user_id"]
        user_name = user_info["user_name"]
        print(f"username: {user_name}, user_id: {user_id}")

        try:
            user_data = await get_user_twitter_data_by_apidance(str(user_id))
        except Exception as e:
            loguru.logger.error(e)
            loguru.logger.error(traceback.format_exc())
            return False
        try:
            result = await user_data_processing(user_data)
        except Exception as e:
            loguru.logger.error(e)
            loguru.logger.error(traceback.format_exc())
            return False
        try:
            data = await mbti_genai_analysis(result, user_name)
        except Exception as e:
            loguru.logger.error(e)
            loguru.logger.error(traceback.format_exc())
        print(data)
    except Exception as e:
        loguru.logger.error(e)
        loguru.logger.error(traceback.format_exc())


async def main():
    name = input("Please enter a username: ")
    result = await mbti_analysis(username=name)
    print(result)

if __name__ == '__main__':
    asyncio.run(main())
