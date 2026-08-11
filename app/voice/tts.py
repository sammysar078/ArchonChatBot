from pathlib import Path

from openai import AsyncOpenAI

from app.config import settings

client = AsyncOpenAI(api_key=settings.OPENAI_API_KEY)


async def generate_voice(text: str, output_path: str):
    """
    Text-to-speech (female voice foundation).
    """

    if not settings.OPENAI_API_KEY:
        return False

    try:
        response = await client.audio.speech.create(
            model="gpt-4o-mini-tts",
            voice="alloy",
            input=text,
        )

        path = Path(output_path)
        path.write_bytes(response.content)

        return True

    except Exception:
        return False
