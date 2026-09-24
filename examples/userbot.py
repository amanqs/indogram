"""Contoh 3: Userbot / Akun Pribadi Telegram dengan Indogram."""
import asyncio
from indogram import Client, filters
from indogram.types import Message
from indogram.utils import format_date_id, now_wib

API_ID = 1234567
API_HASH = "your_api_hash"

# Inisialisasi client akun Telegram (Userbot)
app = Client("my_account", api_id=API_ID, api_hash=API_HASH)


@app.on_message(filters.me & filters.command("ping", prefixes="."))
async def ping(client: Client, message: Message):
    await message.edit_text(f"🏓 **Pong!**\n`{format_date_id(now_wib())}`")


async def main():
    async with app:
        me = await app.get_me()
        print(f"Berhasil login sebagai: {me.first_name} (@{me.username})")
        # Menjaga userbot tetap berjalan
        await asyncio.Event().wait()


if __name__ == "__main__":
    asyncio.run(main())
