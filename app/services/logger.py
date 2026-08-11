from aiogram import Bot

from app.config import settings


async def log_event(bot: Bot, text: str):
    """Send logs to the logger group if configured."""
    if settings.LOGGER_GROUP_ID == 0:
        return

    try:
        await bot.send_message(settings.LOGGER_GROUP_ID, text)
    except Exception:
        # Ignore logger failures for now
        pass
