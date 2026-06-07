#!/usr/bin/env python3
"""
stripe_setup.py -- one-command go-live for the MetaBrainAGI storefront.

Reads assets/stripe-catalog.json, then (using a RESTRICTED Stripe key from the
env var STRIPE_API_KEY) creates, per product:
  * a Stripe Product,
  * a recurring monthly Price (pro_monthly, in cents),
  * a one-time Price (license_one_time, in cents) when > 0,
  * a Payment Link for the monthly price,
and writes the resulting ids + payment_link_pro/license back into the catalog.
The storefront reads the catalog at load, so the Buy buttons go live the moment
you commit the updated JSON. No live keys are stored in the repo.

USAGE:
  export STRIPE_API_KEY=rk_live_...      # a RESTRICTED key: Products+Prices+PaymentLinks = write
  python scripts/stripe_setup.py          # add --dry-run to preview without creating
  git add assets/stripe-catalog.json && git commit -m "stripe: wire payment links" && git push

Stdlib + requests only. Idempotent-ish: skips products that already have a payment_link_pro.
"""
from __future__ import annotations
import json, os, sys
from pathlib import Path

try:
    import requests
except Exception:
    print("ERROR: pip install requests"); sys.exit(1)

CATALOG = Path(__file__).resolve().parents[1] / "assets" / "stripe-catalog.json"
API = "https://api.stripe.com/v1"
KEY = os.environ.get("STRIPE_API_KEY", "").strip()
DRY = "--dry-run" in sys.argv


def _post(path: str, data: dict) -> dict:
    r = requests.post(f"{API}/{path}", data=data, auth=(KEY, ""), timeout=30)
    if r.status_code >= 300:
        raise RuntimeError(f"{path} -> {r.status_code}: {r.text[:300]}")
    return r.json()


def main() -> int:
    if not KEY and not DRY:
        print("ERROR: set STRIPE_API_KEY (a RESTRICTED key). Or run with --dry-run.")
        return 2
    cat = json.loads(CATALOG.read_text(encoding="utf-8"))
    free = set(cat.get("free", []))
    changed = 0
    for p in cat.get("products", []):
        key, name = p.get("key"), p.get("name")
        if key in free:
            continue
        if p.get("payment_link_pro"):
            print(f"  [skip] {name} (already has a payment link)"); continue
        monthly = int(p.get("pro_monthly") or 0)
        if monthly <= 0:
            print(f"  [skip] {name} (no monthly price)"); continue
        if DRY:
            print(f"  [dry] would create: {name} @ ${monthly/100:.2f}/mo (+ link)"); continue
        try:
            prod = _post("products", {"name": f"{name} (Pro)"})
            price = _post("prices", {
                "product": prod["id"], "currency": cat.get("currency", "usd"),
                "unit_amount": monthly, "recurring[interval]": "month",
            })
            link = _post("payment_links", {
                "line_items[0][price]": price["id"], "line_items[0][quantity]": 1,
            })
            p["stripe_product_id"] = prod["id"]
            p["price_id_pro"] = price["id"]
            p["payment_link_pro"] = link["url"]
            lic = int(p.get("license_one_time") or 0)
            if lic > 0:
                lprice = _post("prices", {
                    "product": prod["id"], "currency": cat.get("currency", "usd"),
                    "unit_amount": lic,
                })
                llink = _post("payment_links", {
                    "line_items[0][price]": lprice["id"], "line_items[0][quantity]": 1,
                })
                p["price_id_license"] = lprice["id"]
                p["payment_link_license"] = llink["url"]
            changed += 1
            print(f"  [ok] {name} -> {link['url']}")
        except Exception as e:
            print(f"  [FAIL] {name}: {e}")
    if changed and not DRY:
        cat["mode"] = "live"
        CATALOG.write_text(json.dumps(cat, indent=2) + "\n", encoding="utf-8")
        print(f"\nwrote {changed} payment links -> {CATALOG.name}. Commit + push to go live.")
    else:
        print("\n(no changes written)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
