from __future__ import annotations

import json
from pathlib import Path

from pianzi_kexing.models import WatchlistEntry


def load_manifest(path: str | Path) -> list[WatchlistEntry]:
    manifest_path = Path(path)
    payload = json.loads(manifest_path.read_text(encoding="utf-8"))
    if not isinstance(payload, list):
        raise ValueError("manifest 必须是 JSON 数组")

    entries: list[WatchlistEntry] = []
    for item in payload:
        entries.append(WatchlistEntry(**item))
    return entries
