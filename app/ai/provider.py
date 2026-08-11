from app.ai.prompts import SYSTEM_PROMPT


async def generate_reply(user_message: str) -> str:
    """
    Temporary AI placeholder.

    In the next step we will connect this to OpenAI/GPT.
    """

    if not user_message:
        return "I received your message."

    return (
        "[AI Placeholder]\\n\\n"
        f"System: {SYSTEM_PROMPT[:40]}...\\n"
        f"User: {user_message}"
    )
