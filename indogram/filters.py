from __future__ import annotations

import pyrogram.filters
from pyrogram.filters import *

__all__ = pyrogram.filters.__all__ if hasattr(pyrogram.filters, "__all__") else dir(pyrogram.filters)
