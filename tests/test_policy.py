from pathlib import Path

from pianzi_kexing.dataset import load_manifest
from pianzi_kexing.policy import evaluate_entry, opsec_checklist


def test_load_manifest_and_validate_entries() -> None:
    manifest_path = Path(__file__).resolve().parents[1] / "examples" / "watchlist_manifest.json"
    entries = load_manifest(manifest_path)

    assert len(entries) == 2

    first = evaluate_entry(entries[0])
    second = evaluate_entry(entries[1])

    assert first.allowed is True
    assert second.allowed is False
    assert any("群众曝光式指认数据" in issue for issue in second.issues)


def test_opsec_checklist_contains_org_account_recommendation() -> None:
    items = opsec_checklist()
    assert any("GitHub Organization" in item for item in items)
