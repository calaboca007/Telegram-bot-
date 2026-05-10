from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

TOKEN = "8417128215:AAGVR60Fq9y9nM5IcG6J9RyWIgt_bkprsoA"

# Start command
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🎵 Welcome to Calaboca Music Bot!\n\n"
        "Commands:\n"
        "/music song name\n"
        "/lyrics song name\n"
        "/"
    )

# Help command
async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🎧 Available Commands:\n\n"
        "/music - Search music\n"
        "/lyrics - Get lyrics\n"
        "/help - Show help"
    )

# Music command
async def music(update: Update, context: ContextTypes.DEFAULT_TYPE):
    song = " ".join(context.args)

    if not song:
        await update.message.reply_text("❌ Please type a song name.")
        return

    await update.message.reply_text(
        f"🔍 Searching for: {song}\n\n"
        "🎵 Music feature coming soon."
    )

# Lyrics command
async def lyrics(update: Update, context: ContextTypes.DEFAULT_TYPE):
    song = " ".join(context.args)

    if not song:
        await update.message.reply_text("❌ Please type a song name.")
        return

    await update.message.reply_text(
        f"📝 Lyrics search for: {song}\n\n"
        "Lyrics feature coming soon."
    )

# Main bot setup
app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("help", help_command))
app.add_handler(CommandHandler("music", music))
app.add_handler(CommandHandler("lyrics", lyrics))

print("Bot is running...")
app.run_polling()
