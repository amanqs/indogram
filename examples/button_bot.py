"""Contoh 2: Bot dengan Tombol Inline (Inline Keyboard) & Callback."""
from indogram import Client, filters
from indogram.types import (
    CallbackQuery,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    Message,
)
from indogram.utils import format_rupiah

API_ID = 1234567
API_HASH = "your_api_hash"
BOT_TOKEN = "your_bot_token"

app = Client("button_bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)


@app.on_message(filters.command("menu"))
async def menu_command(client: Client, message: Message):
    keyboard = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton("🛒 Cek Harga", callback_data="check_price"),
                InlineKeyboardButton("ℹ️ Info Indogram", callback_data="info"),
            ],
            [
                InlineKeyboardButton("🌐 Repository GitHub", url="https://github.com/amanqs/indogram")
            ],
        ]
    )
    await message.reply_text("Silakan pilih menu di bawah:", reply_markup=keyboard)


@app.on_callback_query()
async def callback_handler(client: Client, callback: CallbackQuery):
    if callback.data == "check_price":
        harga = format_rupiah(50000)
        await callback.answer(f"Harga paket: {harga}", show_alert=True)
    elif callback.data == "info":
        await callback.answer()
        await callback.message.edit_text("Indogram adalah framework Telegram MTProto asinkron untuk Python.")


if __name__ == "__main__":
    app.run()
