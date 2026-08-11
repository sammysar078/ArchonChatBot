from aiogram import Bot
from sqlalchemy import select

from app.db.session import AsyncSessionLocal
from app.db.models import UserMemory


async def get_all_user_ids():
    """
    Temporary user source.
    Later we will use a dedicated users table.
    """
    async with AsyncSessionLocal() as session:
        result = await session.execute(select(UserMemory.user_id).distinct())
        return list(result.scalars().all())


async def broadcast_message(bot: Bot, text: str):
    users = await get_all_user_ids()

    success = 0
    failed = 0

    for user_id in users:
        try:
            await bot.send_message(user_id, text)
            success += 1
        except Exception:
            failed += 1

    return success, failed
