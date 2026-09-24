"""Contoh 1: Bot Sederhana (Echo Bot) dengan Indogram."""
from indogram import Client, filters
from indogram.types import Message
from indogram.utils import format_date_id, now_wib

API_ID = 1234567
API_HASH = "your_api_hash"
BOT_TOKEN = "your_bot_token"

app = Client("echo_bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)


@app.on_message(filters.command("start"))
async def start(client: Client, message: Message):
    waktu = format_date_id(now_wib())
    await message.reply_text(
        f"👋 Halo **{message.from_user.first_name}**!\n\n"
        f"Bot ini berjalan dengan **Indogram**.\n"
        f"⏰ Waktu server: `{waktu}`"
    )


@app.on_message(filters.text & filters.private)
async def echo(client: Client, message: Message):
    await message.reply_text(f"Anda mengirim: {message.text}")


if __name__ == "__main__":
    app.run()
