from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

ADMIN_ID = None  # غادي نحددوها من بعد

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    global ADMIN_ID
    if ADMIN_ID is None:
        ADMIN_ID = update.effective_user.id
        await update.message.reply_text("✅ ولات أنا الأدمن ديال هاد البوت.")
    else:
        await update.message.reply_text("🤖 مرحبا بك فبوت reset.")

async def reset(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.effective_user.id != ADMIN_ID:
        await update.message.reply_text("❌ ما عندكش الصلاحية.")
        return

    if len(context.args) == 0:
        await update.message.reply_text("⚠️ استعمل: /reset KEY")
        return

    key = context.args[0]
    await update.message.reply_text(f"♻️ تم طلب reset لهاد key:\n{key}")

app = ApplicationBuilder().token(8388173133:AAFvEtiPsNFLcemllb4hld3C6fPA7m58PN4).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("reset", reset))

app.run_polling()
