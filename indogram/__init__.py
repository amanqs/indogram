#  Indogram - Telegram MTProto API Client Library for Python
#  Copyright (C) 2026-present Indogram Developers
#
#  This file is part of Indogram.
#
#  Indogram is free software: you can redistribute it and/or modify
#  it under the terms of the GNU Lesser General Public License as published
#  by the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  Indogram is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU Lesser General Public License for more details.
#
#  You should have received a copy of the GNU Lesser General Public License
#  along with Indogram.  If not, see <http://www.gnu.org/licenses/>.

from __future__ import annotations

import importlib
import importlib.abc
import importlib.util
import sys

# Ensure pyrogram is loaded as core engine
import pyrogram
from pyrogram import (
    Client,
    ContinuePropagation,
    StopPropagation,
    StopTransmission,
    compose,
    enums,
    filters,
    handlers,
    idle,
    raw,
    types,
)

__version__ = pyrogram.__version__
__license__ = "GNU Lesser General Public License v3.0 (LGPL-3.0)"
__copyright__ = "Copyright (C) 2026-present Indogram Developers"


class _IndogramAliasFinder(importlib.abc.MetaPathFinder):
    """Dynamic meta path finder to transparently map any indogram.* submodules

    to pyrogram.* submodules with shared module identity.
    """

    def find_spec(self, fullname: str, path=None, target=None):
        if fullname.startswith("indogram."):
            pyrogram_name = "pyrogram." + fullname[len("indogram.") :]
            try:
                mod = importlib.import_module(pyrogram_name)
            except ImportError:
                return None

            class _AliasLoader(importlib.abc.Loader):
                def create_module(self, spec):
                    return mod

                def exec_module(self, module):
                    pass

            spec = importlib.util.spec_from_loader(fullname, _AliasLoader())
            if hasattr(mod, "__path__"):
                spec.submodule_search_locations = list(mod.__path__)
            return spec
        return None


# Register finder if not present
if not any(isinstance(finder, _IndogramAliasFinder) for finder in sys.meta_path):
    sys.meta_path.insert(0, _IndogramAliasFinder())

# Sync existing pyrogram entries in sys.modules to indogram
for mod_name, mod in list(sys.modules.items()):
    if mod_name == "pyrogram" or mod_name.startswith("pyrogram."):
        indo_name = "indogram" + mod_name[len("pyrogram") :]
        if indo_name not in sys.modules:
            sys.modules[indo_name] = mod

__all__ = [
    "Client",
    "ContinuePropagation",
    "StopPropagation",
    "StopTransmission",
    "compose",
    "enums",
    "filters",
    "handlers",
    "idle",
    "raw",
    "types",
    "__version__",
]
