#!/usr/bin/env python3
"""
TotalStack catalog patcher — adds community entries for all TotalStack-native services
so the runtime coverage gate doesn't reject them with 501.

Run: python3 scripts/patch-catalog.py [--dry-run]
"""

import json
import re
import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
CATALOG_PATH = PROJECT_ROOT / "localstack-core/.filesystem/var/lib/localstack/cache/aws_catalog.json"
PROVIDERS_PATH = PROJECT_ROOT / "totalstack/providers.py"

DRY_RUN = "--dry-run" in sys.argv


def get_registered_services():
    """Parse @aws_provider(api="...") declarations from providers.py"""
    content = PROVIDERS_PATH.read_text()
    return sorted(set(re.findall(r'@aws_provider\(api="([^"]+)"', content)))


def get_service_operations(svc: str) -> list:
    """Extract implemented operations from the assembled .code.py handler files.

    This is the ground truth for what the auto-wired TotalStack provider for
    ``svc`` actually serves (the spec files may list ops that have no handler,
    and ops like TagResource/UntagResource can be missing from them).
    """
    assembled_dir = PROJECT_ROOT / "specs/aws/.speclang/assembled" / svc
    ops = set()
    if assembled_dir.is_dir():
        for f in sorted(assembled_dir.glob("*.code.py")):
            stem = f.name[: -len(".code.py")]
            if stem == "models":
                continue
            ops.add("".join(w[:1].upper() + w[1:] for w in stem.split("-")))
    return sorted(ops)


def get_s3tables_operations():
    """Extract operations from s3tables spec (fallback for services without an assembled dir)"""
    spec_files = list((PROJECT_ROOT / "specs/aws/s3tables").glob("*.spec.py.md"))
    ops = set()
    for sf in spec_files:
        text = sf.read_text()
        # Match operation names from handler definitions
        ops.update(re.findall(r"def\s+(\w+)\s*\(", text))
    return sorted(ops)


def get_all_operations():
    """Deprecated placeholder — per-service op lists now come from the assembled handlers."""
    return get_s3tables_operations()


def main():
    if not CATALOG_PATH.exists():
        print(f"ERROR: Catalog not found at {CATALOG_PATH}")
        print("Make sure the LocalStack container has been started at least once.")
        sys.exit(1)

    registered = get_registered_services()
    with open(CATALOG_PATH) as f:
        catalog = json.load(f)

    services = catalog["services"]
    added = 0
    skipped = 0

    for svc in registered:
        # per-service op list derived from the assembled handlers — the ground
        # truth for what the auto-wired provider actually serves
        operations = get_service_operations(svc) or get_all_operations()
        if svc not in services:
            # Not in catalog at all — add full entry
            services[svc] = {
                "community": {
                    "provider": f"{svc}:totalstack",
                    "operations": operations,
                    "plans": ["base", "freemium"],
                }
            }
            added += 1
        elif "community" not in services[svc]:
            # In catalog but pro-only — add community entry
            pro_ops = services[svc].get("pro", {}).get("operations", operations)
            services[svc]["community"] = {
                "provider": f"{svc}:totalstack",
                "operations": pro_ops,
                "plans": ["base", "freemium"],
            }
            added += 1
        else:
            # Existing community entry — refresh the op list if it is a
            # TotalStack provider and the derived list differs (keeps the
            # catalog in sync with the implemented handlers)
            community = services[svc].get("community", {})
            if community.get("provider") == f"{svc}:totalstack" and set(
                community.get("operations", [])
            ) != set(operations):
                services[svc]["community"]["operations"] = operations
                added += 1
            else:
                skipped += 1

    if DRY_RUN:
        print(f"DRY RUN: Would add community entries for {added} services, skip {skipped} already present")
        return

    with open(CATALOG_PATH, "w") as f:
        json.dump(catalog, f, indent=2)

    # Verify
    with open(CATALOG_PATH) as f:
        verify = json.load(f)

    verify_added = 0
    for svc in registered:
        etypes = list(verify["services"][svc].keys())
        if "community" in etypes:
            verify_added += 1

    print(f"✓ Patched catalog: {verify_added}/{len(registered)} TotalStack services now community")
    print(f"  s3tables: {list(verify['services']['s3tables'].keys())}")
    print(f"  s3tables provider: {verify['services']['s3tables']['community']['provider']}")
    print(f"  File: {CATALOG_PATH}")


if __name__ == "__main__":
    main()
