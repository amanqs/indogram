from __future__ import annotations

from datetime import datetime, timedelta, timezone

# Zona waktu standar Indonesia
WIB = timezone(timedelta(hours=7), name="WIB")
WITA = timezone(timedelta(hours=8), name="WITA")
WIT = timezone(timedelta(hours=9), name="WIT")


def now_wib() -> datetime:
    """Mengembalikan waktu saat ini dalam zona WIB (UTC+7)."""
    return datetime.now(WIB)


def format_rupiah(amount: int | float, prefix: str = "Rp ") -> str:
    """Format angka menjadi format mata uang Rupiah.

    Contoh: format_rupiah(50000) -> 'Rp 50.000'
    """
    try:
        val = int(amount)
        formatted = f"{val:,}".replace(",", ".")
        return f"{prefix}{formatted}"
    except (ValueError, TypeError):
        return f"{prefix}{amount}"


def format_bytes(size: int | float) -> str:
    """Format ukuran byte menjadi string yang mudah dibaca (KB, MB, GB).

    Contoh: format_bytes(1048576) -> '1.00 MB'
    """
    for unit in ["B", "KB", "MB", "GB", "TB"]:
        if abs(size) < 1024.0:
            return f"{size:3.2f} {unit}".strip()
        size /= 1024.0
    return f"{size:.2f} PB"


def format_date_id(dt: datetime | None = None, include_time: bool = True) -> str:
    """Format tanggal ke dalam bahasa Indonesia.

    Contoh: 'Senin, 24 September 2026, 23:50 WIB'
    """
    if dt is None:
        dt = now_wib()
    elif dt.tzinfo is None:
        dt = dt.replace(tzinfo=WIB)

    days = ["Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu", "Minggu"]
    months = [
        "",
        "Januari",
        "Februari",
        "Maret",
        "April",
        "Mei",
        "Juni",
        "Juli",
        "Agustus",
        "September",
        "Oktober",
        "November",
        "Desember",
    ]

    day_name = days[dt.weekday()]
    month_name = months[dt.month]

    base = f"{day_name}, {dt.day} {month_name} {dt.year}"
    if include_time:
        tz_name = dt.tzname() or "WIB"
        base += f", {dt.strftime('%H:%M')} {tz_name}"
    return base


__all__ = [
    "WIB",
    "WITA",
    "WIT",
    "format_bytes",
    "format_date_id",
    "format_rupiah",
    "now_wib",
]
