from __future__ import annotations

import argparse
import sys

from pianzi_kexing.dataset import load_manifest
from pianzi_kexing.policy import evaluate_entry, opsec_checklist


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="pianzi-kexing")
    subparsers = parser.add_subparsers(dest="command", required=True)

    validate_parser = subparsers.add_parser("validate-manifest", help="校验风险清单")
    validate_parser.add_argument("path", help="manifest JSON 文件路径")

    subparsers.add_parser("print-opsec-checklist", help="输出维护者去风险清单")
    return parser


def handle_validate_manifest(path: str) -> int:
    entries = load_manifest(path)
    failed = 0
    for entry in entries:
        decision = evaluate_entry(entry)
        status = "ALLOW" if decision.allowed else "BLOCK"
        print(f"[{status}] {entry.subject_id}")
        for issue in decision.issues:
            print(f"  - {issue}")
        if not decision.allowed:
            failed += 1
    print(f"summary: total={len(entries)} blocked={failed}")
    return 0 if failed == 0 else 1


def handle_print_opsec_checklist() -> int:
    for item in opsec_checklist():
        print(f"- {item}")
    return 0


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)

    if args.command == "validate-manifest":
        return handle_validate_manifest(args.path)
    if args.command == "print-opsec-checklist":
        return handle_print_opsec_checklist()

    parser.print_help()
    return 1


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
