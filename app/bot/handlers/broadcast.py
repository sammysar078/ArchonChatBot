from telegram import Update
from telegram.ext import ContextTypes

from app.config import OWNER_ID


async def broadcast_command(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
):
    if update.effective_user.id != OWNER_ID:
        return

    if not context.args:
        await update.message.reply_text(
            "❌ Broadcast message missing.\n\n"
            "Example:\n"
            "/broadcast Hello everyone!"
        )
        return

    message = " ".join(context.args)

    # Temporary response.
    # User database se recipients next step mein connect karenge.
    await update.message.reply_text(
        "📢 Broadcast system received your message.\n\n"
        f"Message:\n{message}\n\n"
        "⏳ Recipients database integration next step mein add karenge."
    )
