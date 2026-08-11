import asyncio

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.types import Message

from app.config import settings

bot = Bot(
    token=settings.BOT_TOKEN,
    default=DefaultBotProperties(parse_mode=ParseMode.HTML),
)

dp = Dispatcher()


@dp.message(CommandStart())
async def start(message: Message):
    await message.answer(
        "Hello! I am <b>ArchonChatBot</b>.\\n\\n"
        "This is Phase 1 of your AI companion bot."
    )


@dp.message()
async def echo(message: Message):
    if message.text:
        await message.answer(f"You said: {message.text}")
    else:
        await message.answer("I received your message.")


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
