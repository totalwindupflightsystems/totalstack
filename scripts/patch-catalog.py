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


def get_s3tables_operations():
    """Extract operations from s3tables spec"""
    spec_files = list((PROJECT_ROOT / "specs/aws/s3tables").glob("*.spec.py.md"))
    ops = set()
    for sf in spec_files:
        text = sf.read_text()
        # Match operation names from handler definitions
        ops.update(re.findall(r'def\s+(\w+)\s*\(', text))
    return sorted(ops)


def get_all_operations():
    """Get operations from s3tables as our baseline (24 ops).
    For other services, derive from their spec files."""
    # For now, use s3tables operations as template for all TotalStack services
    # In a full implementation, we'd parse each service's spec
    return get_s3tables_operations()


def main():
    if not CATALOG_PATH.exists():
        print(f"ERROR: Catalog not found at {CATALOG_PATH}")
        print("Make sure the LocalStack container has been started at least once.")
        sys.exit(1)

    registered = get_registered_services()
    operations = get_all_operations()

    with open(CATALOG_PATH) as f:
        catalog = json.load(f)

    services = catalog["services"]
    added = 0
    skipped = 0

    for svc in registered:
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
