import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

TOKEN = os.getenv(8508758212:AAH57JNhrIMScMfb0KM7gFeZf2wfzjievQE)

user_scores = {}

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    user_scores[user_id] = 0
    await update.message.reply_text(
        "🐶 Welcome to Piru Tap Game!\n\nTap with /tap command!"
    )

async def tap(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    if user_id not in user_scores:
        user_scores[user_id] = 0
    user_scores[user_id] += 1
    await update.message.reply_text(f"🔥 Points: {user_scores[user_id]}")

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("tap", tap))

app.run_polling()
