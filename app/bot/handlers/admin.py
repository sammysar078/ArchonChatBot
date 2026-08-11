from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

from app.services.permissions import is_owner

router = Router()


@router.message(Command("whoami"))
async def whoami(message: Message):
    if await is_owner(message.from_user.id):
        await message.answer("You are the <b>Owner</b> of ArchonChatBot.")
    else:
        await message.answer("You are a normal user.")
