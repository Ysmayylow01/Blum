import pyrogram
from loguru import logger
from data import config


async def create_sessions():
    while True:
        session_name = input('\nInput the name of the session (press Enter to exit): ')
        if not session_name: return

        session = pyrogram.Client(
            api_id=config.API_ID,
            api_hash=config.API_HASH,
            name=session_name,
            workdir=config.WORKDIR,
        )

        async with session:
            user_data = await session.get_me()

        logger.success(f'Added a session {user_data.username} | {user_data.phone_number}')
