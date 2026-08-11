from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

from app.services.broadcast import broadcast_message
from app.services.logger import log_event
from app.services.permissions import (
    has_permission,
    is_owner,
)

router = Router()


@router.message(Command("broadcast"))
async def broadcast(message: Message):
    user_id = message.from_user.id

    if not (
        await is_owner(user_id)
        or await has_permission(user_id, "broadcast")
    ):
        await message.answer("Permission denied.")
        return

    parts = (message.text or "").split(maxsplit=1)
    if len(parts) != 2:
        await message.answer("Usage: /broadcast <message>")
        return

    text = parts[1]

    await message.answer("Broadcast started...")

    success, failed = await broadcast_message(message.bot, text)

    result = (
        "Broadcast completed.\\n\\n"
        f"Success: {success}\\n"
        f"Failed: {failed}"
    )

    await log_event(message.bot, "📢 " + result)
    await message.answer(result)
