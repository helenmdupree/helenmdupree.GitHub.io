#!/usr/bin/env python3
from __future__ import annotations

import re
import sys
import xml.etree.ElementTree as ET
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
errors: list[str] = []
warnings: list[str] = []


def fail(message: str) -> None:
    errors.append(message)


def warn(message: str) -> None:
    warnings.append(message)


# 1. Guard the custom-domain contract.
cname = ROOT / "CNAME"
if not cname.exists():
    fail("CNAME is missing.")
elif cname.read_text(encoding="utf-8").strip() != "soubel.com":
    fail("CNAME must contain exactly: soubel.com")

# 2. Guard public search-engine crawl configuration.
robots = ROOT / "robots.txt"
if not robots.exists():
    fail("robots.txt is missing.")
else:
    robots_text = robots.read_text(encoding="utf-8")
    for required in (
        "User-agent: *",
        "Allow: /",
        "Sitemap: https://soubel.com/sitemap.xml",
    ):
        if required not in robots_text:
            fail(f"robots.txt is missing required directive: {required}")

# 3. Validate sitemap syntax and SOUBEL-only URLs.
sitemap = ROOT / "sitemap.xml"
if not sitemap.exists():
    fail("sitemap.xml is missing.")
else:
    try:
        tree = ET.parse(sitemap)
        root = tree.getroot()
        ns = {"sm": "http://www.sitemaps.org/schemas/sitemap/0.9"}
        locs = [
            (node.text or "").strip()
            for node in root.findall("sm:url/sm:loc", ns)
        ]
        if not locs:
            fail("sitemap.xml contains no URL entries.")
        if len(locs) != len(set(locs)):
            fail("sitemap.xml contains duplicate URLs.")
        for loc in locs:
            if not (loc == "https://soubel.com/" or loc.startswith("https://soubel.com/")):
                fail(f"sitemap.xml contains a non-SOUBEL URL: {loc}")
    except ET.ParseError as exc:
        fail(f"sitemap.xml is not valid XML: {exc}")

# 4. Fail closed on files that should never live in the public repository.
forbidden_names = {
    ".env",
    "id_rsa",
    "id_ed25519",
}
forbidden_suffixes = {".pem", ".key", ".p12", ".pfx"}
forbidden_roots = {"whoqual", "security", "private", "internal"}

for path in ROOT.rglob("*"):
    if not path.is_file():
        continue
    rel = path.relative_to(ROOT)
    parts_lower = [part.lower() for part in rel.parts]
    name_lower = path.name.lower()

    if name_lower in forbidden_names or name_lower.startswith(".env."):
        fail(f"Forbidden sensitive file in public repository: {rel}")
    if path.suffix.lower() in forbidden_suffixes:
        fail(f"Forbidden key/certificate file in public repository: {rel}")
    if parts_lower and parts_lower[0] in forbidden_roots:
        fail(f"Private/internal root directory is not allowed in public repository: {rel}")

# 5. Scan readable source files for common credential patterns.
text_suffixes = {
    ".html", ".htm", ".js", ".css", ".md", ".txt", ".json",
    ".yaml", ".yml", ".xml", ".py", ".toml", ".ini", ".cfg",
}
secret_patterns = {
    "private key block": re.compile(r"-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----"),
    "GitHub token": re.compile(r"\bgh[pousr]_[A-Za-z0-9_]{20,}\b"),
    "AWS access key": re.compile(r"\bAKIA[0-9A-Z]{16}\b"),
    "OpenAI-style secret key": re.compile(r"\bsk-[A-Za-z0-9_-]{20,}\b"),
    "client secret assignment": re.compile(r"(?i)\bclient[_-]?secret\s*[:=]\s*['\"][^'\"]{8,}['\"]"),
    "API key assignment": re.compile(r"(?i)\bapi[_-]?key\s*[:=]\s*['\"][^'\"]{12,}['\"]"),
}

for path in ROOT.rglob("*"):
    if not path.is_file() or path.suffix.lower() not in text_suffixes:
        continue
    rel = path.relative_to(ROOT)
    # The checker itself contains regex examples by design.
    if rel.as_posix() == ".github/scripts/prepublish_check.py":
        continue
    try:
        text = path.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        continue
    for label, pattern in secret_patterns.items():
        if pattern.search(text):
            fail(f"Possible {label} found in public file: {rel}")

# 6. Keep redirect-only legacy routes out of the public client-side search corpus.
search_index = ROOT / "assets" / "library-search-index.js"
if not search_index.exists():
    fail("assets/library-search-index.js is missing.")
else:
    search_index_text = search_index.read_text(encoding="utf-8")
    forbidden_search_records = (
        '"url":"/expertise/pipeline-asset-integrity/"',
    )
    for forbidden_record in forbidden_search_records:
        if forbidden_record in search_index_text:
            fail(
                "Redirect-only legacy route found in public search index: "
                + forbidden_record
            )

# 7. Existing deployment fragments are not a publish blocker yet, but stay visible.
if (ROOT / ".deploy").exists():
    warn(".deploy/ exists in the public repository. It is a documented cleanup candidate and should contain no private material.")

for message in warnings:
    print(f"WARNING: {message}")

if errors:
    print("\nPRE-PUBLISH GATE: FAIL")
    for message in errors:
        print(f"ERROR: {message}")
    sys.exit(1)

print("\nPRE-PUBLISH GATE: PASS")
print("CNAME, crawl directives, sitemap, public/private path boundaries, search-index exclusions, and common secret patterns passed.")
