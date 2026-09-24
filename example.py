"""Contoh penggunaan Indogram (Telegram MTProto Client Library)

Dapat menggunakan import indogram ataupun import pyrogram!
"""
from indogram import Client, filters
from indogram.types import Message

# Ganti dengan api_id dan api_hash Anda dari https://my.telegram.org
API_ID = 1234567
API_HASH = "your_api_hash_here"
BOT_TOKEN = "your_bot_token_here"

# Inisialisasi client Indogram
app = Client(
    name="indogram_bot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN,
)


@app.on_message(filters.command("start"))
async def start_handler(client: Client, message: Message):
    """Menangani perintah /start"""
    await message.reply_text(
        "👋 Halo! Bot ini berjalan menggunakan library **Indogram**!\n\n"
        "Library Telegram MTProto asinkron berkecepatan tinggi dengan dual-import compatibility."
    )


@app.on_message(filters.text & filters.private)
async def echo_handler(client: Client, message: Message):
    """Echo pesan teks pribadi"""
    await message.reply_text(f"Pesan diterima: {message.text}")


if __name__ == "__main__":
    print("Menjalankan Indogram Bot...")
    app.run()
