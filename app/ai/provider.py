from openai import AsyncOpenAI

from app.ai.prompts import SYSTEM_PROMPT
from app.config import settings

client = AsyncOpenAI(api_key=settings.OPENAI_API_KEY)


async def generate_reply(user_message: str) -> str:
    if not settings.OPENAI_API_KEY:
        return (
            "OpenAI API key configured nahi hai.\\n"
            "Abhi placeholder mode mein chal raha hoon."
        )

    try:
        response = await client.chat.completions.create(
            model="gpt-4.1-mini",
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": user_message},
            ],
            temperature=0.8,
        )

        return response.choices[0].message.content.strip()

    except Exception:
        return (
            "AI service se connect nahi ho pa raha. "
            "Baad mein dobara try karo."
        )
