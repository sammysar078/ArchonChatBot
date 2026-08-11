from aiogram import Router
from aiogram.filters import Command, CommandStart
from aiogram.types import Message

router = Router()


@router.message(CommandStart())
async def start(message: Message):
    await message.answer(
        "Hello! I am <b>ArchonChatBot</b>.\\n\\n"
        "AI Companion is being built step by step."
    )


@router.message(Command("help"))
async def help_command(message: Message):
    await message.answer(
        "/start - Start the bot\\n"
        "/help - Show help\\n"
        "/ping - Check if bot is online"
    )


@router.message(Command("ping"))
async def ping(message: Message):
    await message.answer("Pong! ArchonChatBot is online.")
