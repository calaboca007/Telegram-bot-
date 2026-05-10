from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, CallbackQueryHandler
import requests

TOKEN = "8417128215:AAGVR60Fq9y9nM5IcG6J9RyWIgt_bkprsoA"


# START COMMAND
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🎵 Welcome to Calaboca Music Bot\n\n"
        "Commands:\n"
        "/music song name\n"
        "/lyrics artist - song"
    )


# MUSIC SEARCH (WITH COVER ART)

async def music(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = " ".join(context.args)

    if not query:
        await update.message.reply_text("❌ Type a song name.")
        return

    url = f"https://api.deezer.com/search?q={query}"
    res = requests.get(url).json()

    if not res["data"]:
        await update.message.reply_text("❌ No songs found.")
        return

    message = "🎵 Top Results:\n\n"

    for i, song in enumerate(res["data"][:5]):
        title = song["title"]
        artist = song["artist"]["name"]
        message += f"{i+1}. {title} - {artist}\n"

    await update.message.reply_text(message)
# LYRICS COMMAND
async def lyrics(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = " ".join(context.args)

    if "-" not in text:
        await update.message.reply_text("❌ Use: /lyrics artist - song")
        return

    artist, song = text.split("-", 1)

    url = f"https://api.lyrics.ovh/v1/{artist.strip()}/{song.strip()}"
    res = requests.get(url).json()

    lyrics_text = res.get("lyrics")

    if not lyrics_text:
        await update.message.reply_text("❌ Lyrics not found.")
        return

    if len(lyrics_text) > 3500:
        lyrics_text = lyrics_text[:3500]

    await update.message.reply_text(
        f"📝 Lyrics for {song.strip()}:\n\n{lyrics_text}"
    )


# BOT SETUP
app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("music", music))
app.add_handler(CommandHandler("lyrics", lyrics))

print("Bot is running...")
app.run_polling()
async def download(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = " ".join(context.args)

    if not query:
        await update.message.reply_text("❌ Type a song name.")
        return

    url = f"https://api.deezer.com/search?q={query}"
    res = requests.get(url).json()

    if not res["data"]:
        await update.message.reply_text("❌ No song found.")
        return

    song = res["data"][0]
    preview = song["preview"]

    await update.message.reply_audio(
        audio=preview,
        title=song["title"],
        performer=song["artist"]["name"]
    )
