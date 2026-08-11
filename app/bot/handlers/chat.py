from aiogram import Router
from aiogram.types import Message

from app.ai.provider import generate_reply

router = Router()


@router.message()
async def chat(message: Message):
    if not message.text:
        await message.answer("I can understand text messages for now.")
        return

    reply = await generate_reply(message.text)
    await message.answer(reply)
