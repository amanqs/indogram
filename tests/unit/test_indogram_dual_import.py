from __future__ import annotations

try:
    import pytest
except ImportError:
    pytest = None


def test_indogram_top_level_import():
    import indogram
    import pyrogram

    assert indogram.__version__ == pyrogram.__version__
    assert indogram.Client is pyrogram.Client
    assert indogram.filters.text is pyrogram.filters.text
    assert indogram.types.Message is pyrogram.types.Message
    assert indogram.enums.ChatType is pyrogram.enums.ChatType
    assert indogram.StopPropagation is pyrogram.StopPropagation


def test_indogram_deep_submodule_import():
    from indogram.errors import RPCError, FloodWait
    from pyrogram.errors import RPCError as PyRPCError, FloodWait as PyFloodWait
    from indogram.raw.types import InputPeerChat
    from pyrogram.raw.types import InputPeerChat as PyInputPeerChat

    assert RPCError is PyRPCError
    assert FloodWait is PyFloodWait
    assert InputPeerChat is PyInputPeerChat


def test_indonesian_utilities():
    from indogram.utils import WIB, format_bytes, format_date_id, format_rupiah, now_wib

    assert WIB.utcoffset(None).total_seconds() == 7 * 3600
    assert format_rupiah(50000) == "Rp 50.000"
    assert format_rupiah(1250000) == "Rp 1.250.000"
    assert format_bytes(1048576) == "1.00 MB"

    dt = now_wib()
    assert dt.tzinfo == WIB
    formatted_date = format_date_id(dt)
    assert "WIB" in formatted_date
