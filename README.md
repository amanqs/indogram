<p align="center">
    <br />
    <h1 align="center">⚡ Indogram</h1>
    <p align="center"><b>Elegant, modern, and asynchronous Telegram MTProto API Framework in Python</b></p>
    <p align="center">
        <i>Dual-import support: works with both <code>import indogram</code> and <code>import pyrogram</code></i>
    </p>
</p>

<p align="center">
    <img src="https://img.shields.io/badge/Python-3.10%2B-blue.svg?logo=python&logoColor=white" alt="Python 3.10+" />
    <img src="https://img.shields.io/badge/License-LGPLv3-green.svg" alt="License" />
    <img src="https://img.shields.io/badge/AsyncIO-Ready-orange.svg" alt="AsyncIO Ready" />
    <img src="https://img.shields.io/badge/Compatibility-Pyrogram%20Drop--in-brightgreen.svg" alt="Pyrogram Compatible" />
</p>

---

## 📖 Overview

**Indogram** is an actively maintained MTProto API framework for Python. It empowers developers to interact effortlessly with the Telegram MTProto API via both user accounts (custom clients/userbots) and bot identities (Bot API alternative).

Indogram is built with **Dual-Import Architecture**:
- 🚀 **New Projects**: Use `from indogram import Client, filters, types`
- 🔄 **Existing Projects**: Drop-in compatible with `from pyrogram import Client, filters, types` (no code changes needed for existing bots and plugins!)

---

## ✨ Features

- **Dual-Import Compatibility**: Import as `indogram` or `pyrogram` interchangeably with 100% shared module and class identities.
- **Modern Telegram Features**: Support for Stories, Topics, Forum Channels, Business Accounts, Star Gifts, Reactions, and more.
- **Async & Fast**: Built for `asyncio`, with optional C-accelerated speedups via [TgCrypto](https://github.com/pyrogram/tgcrypto) and `uvloop`.
- **Fully Typed**: Rich type annotations with PEP 561 compliance (`py.typed`) for autocomplete in VS Code, PyCharm, and language servers.
- **Easy & Intuitive**: Clean decorator-based event handlers (`@app.on_message()`, `@app.on_callback_query()`, etc.).

---

## 📦 Installation

### Stable / Local Package
```bash
pip install indogram
```

### High-Performance (TgCrypto & uvloop)
```bash
pip install "indogram[fast]"
```

### QR Code Login Support
```bash
pip install "indogram[qrcode]"
```

### Development / Direct from Source
```bash
git clone https://github.com/amanqs/indogram.git
cd indogram
pip install .
```

---

## 🚀 Quick Start

### 1. Simple Echo Bot (using `indogram`)

```python
from indogram import Client, filters
from indogram.types import Message

# Initialize client (Get api_id and api_hash from https://my.telegram.org)
app = Client(
    "my_bot",
    api_id=1234567,
    api_hash="your_api_hash_here",
    bot_token="your_bot_token_here",
)


@app.on_message(filters.command("start"))
async def start_command(client: Client, message: Message):
    await message.reply_text("👋 Halo! Selamat datang di bot yang ditenagai oleh **Indogram**!")


@app.on_message(filters.text & filters.private)
async def echo(client: Client, message: Message):
    await message.reply_text(f"Anda berkata: {message.text}")


if __name__ == "__main__":
    app.run()
```

### 2. Userbot / MTProto Client

```python
import asyncio
from indogram import Client

app = Client(
    "my_account",
    api_id=1234567,
    api_hash="your_api_hash_here",
)


async def main():
    async with app:
        me = await app.get_me()
        print(f"Logged in as: {me.first_name} (@{me.username})")
        await app.send_message("me", "✨ Pesan tes dari Indogram!")


if __name__ == "__main__":
    asyncio.run(main())
```

### 3. Existing Pyrogram Code (Zero Changes Required)

Existing code written for Pyrogram continues to work out-of-the-box:

```python
from pyrogram import Client, filters

app = Client("legacy_bot", bot_token="TOKEN")


@app.on_message(filters.text)
async def handler(client, message):
    await message.reply("Still works seamlessly with Indogram!")


app.run()
```

---

## 🛠️ Building & Recompiling MTProto Schemas

If you modify API TL schemas or need to build distribution wheels:

```bash
# Compile MTProto API & error definitions
python -c "from compiler.api.compiler import start; start(False); from compiler.errors.compiler import start as start_err; start_err()"

# Build wheel & sdist distributions
python -m build
```

---

## 📄 License & Attribution

Indogram is licensed under the [GNU Lesser General Public License v3.0 (LGPL-3.0)](COPYING.lesser).

- Based on and derived from [Kurigram](https://github.com/kurigram-org/kurigram) and [Pyrogram](https://github.com/pyrogram/pyrogram) (Copyright © Dan <dan@pyrogram.org>).
- Maintained and customized for **Indogram**.
