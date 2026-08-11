import asyncio

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode

from app.bot.handlers import router
from app.bot.middlewares.maintenance import MaintenanceMiddleware
from app.config import settings
from app.db.session import init_db

bot = Bot(
    token=settings.BOT_TOKEN,
    default=DefaultBotProperties(parse_mode=ParseMode.HTML),
)

dp = Dispatcher()

# Maintenance middleware
dp.message.middleware(MaintenanceMiddleware())

# Register all handlers
dp.include_router(router)


async def main():
    # Database initialize
    await init_db()

    # Start Telegram bot
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
