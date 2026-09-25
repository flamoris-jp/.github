#!/usr/bin/env python3
from __future__ import annotations

import json
import os
import sys
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path
from typing import Any

API_ROOT = "https://api.github.com"
API_VERSION = "2026-03-10"
START_MARKER = "<!-- development-status:start -->"
END_MARKER = "<!-- development-status:end -->"
STATUS_ORDER = ("stable", "development", "planned", "meta", "unspecified")


def github_get(path: str, token: str) -> Any:
    request = urllib.request.Request(
        f"{API_ROOT}{path}",
        headers={
            "Accept": "application/vnd.github+json",
            "Authorization": f"Bearer {token}",
            "User-Agent": "flamoris-development-status-sync",
            "X-GitHub-Api-Version": API_VERSION,
        },
    )
    try:
        with urllib.request.urlopen(request, timeout=30) as response:
            return json.load(response)
    except urllib.error.HTTPError as exc:
        body = exc.read().decode("utf-8", errors="replace")
        raise RuntimeError(
            f"GitHub API request failed ({exc.code}) for {path}: {body}"
        ) from exc


def get_paginated(path: str, token: str) -> list[dict[str, Any]]:
    results: list[dict[str, Any]] = []
    page = 1
    while True:
        separator = "&" if "?" in path else "?"
        page_path = f"{path}{separator}per_page=100&page={page}"
        batch = github_get(page_path, token)
        if not isinstance(batch, list):
            raise RuntimeError(f"Expected a list from {page_path}")
        results.extend(batch)
        if len(batch) < 100:
            return results
        page += 1


def validate_property_schema(org: str, property_name: str, token: str) -> None:
    org_path = urllib.parse.quote(org, safe="")
    property_path = urllib.parse.quote(property_name, safe="")
    schema = github_get(
        f"/orgs/{org_path}/properties/schema/{property_path}",
        token,
    )
    if schema.get("value_type") != "single_select":
        raise RuntimeError(
            f"{property_name!r} must be an organization single_select custom property"
        )

    allowed = schema.get("allowed_values")
    allowed_values = set(allowed) if isinstance(allowed, list) else set()
    required_values = set(STATUS_ORDER[:-1])
    missing = sorted(required_values - allowed_values)
    if missing:
        raise RuntimeError(
            f"{property_name!r} is missing required allowed values: "
            + ", ".join(missing)
        )


def public_repository_names(org: str, token: str) -> set[str]:
    org_path = urllib.parse.quote(org, safe="")
    repositories = get_paginated(
        f"/orgs/{org_path}/repos?type=public&sort=full_name",
        token,
    )
    names: set[str] = set()
    for repository in repositories:
        name = repository.get("name")
        if isinstance(name, str) and name:
            names.add(name)
    return names


def development_statuses(
    org: str,
    property_name: str,
    token: str,
    public_names: set[str],
) -> dict[str, str]:
    org_path = urllib.parse.quote(org, safe="")
    repositories = get_paginated(f"/orgs/{org_path}/properties/values", token)

    statuses: dict[str, str] = {}
    for repository in repositories:
        name = repository.get("repository_name")
        if not isinstance(name, str) or name not in public_names:
            continue

        raw_value: Any = None
        for prop in repository.get("properties", []):
            if prop.get("property_name") == property_name:
                raw_value = prop.get("value")
                break

        if isinstance(raw_value, str):
            normalized = raw_value.strip().lower()
        else:
            normalized = ""

        if normalized not in STATUS_ORDER[:-1]:
            normalized = "unspecified"
        statuses[name] = normalized

    for name in public_names:
        statuses.setdefault(name, "unspecified")

    return statuses


def render_status_block(org: str, property_name: str, statuses: dict[str, str]) -> str:
    groups = {status: [] for status in STATUS_ORDER}
    for repository, status in statuses.items():
        groups[status].append(repository)

    lines = [
        f"_Status is synchronized automatically from the `{property_name}` "
        "organization custom property. Public repositories only._",
        "",
        "| Status | Repositories |",
        "|---|---|",
    ]

    any_rows = False
    for status in STATUS_ORDER:
        repositories = sorted(groups[status], key=str.casefold)
        if not repositories:
            continue
        any_rows = True
        links = ", ".join(
            f"[{name}](https://github.com/{org}/{name})" for name in repositories
        )
        lines.append(f"| `{status}` | {links} |")

    if not any_rows:
        lines.append("| `unspecified` | No public repositories found. |")

    return "\n".join(lines)


def replace_generated_section(path: Path, rendered: str) -> bool:
    original = path.read_text(encoding="utf-8")
    if original.count(START_MARKER) != 1 or original.count(END_MARKER) != 1:
        raise RuntimeError(
            f"{path} must contain exactly one {START_MARKER} and one {END_MARKER}"
        )

    start = original.index(START_MARKER) + len(START_MARKER)
    end = original.index(END_MARKER, start)
    updated = original[:start] + "\n" + rendered + "\n" + original[end:]

    if updated == original:
        return False

    path.write_text(updated, encoding="utf-8")
    return True


def main() -> int:
    token = os.environ.get("FLAMORIS_CUSTOM_PROPERTIES_TOKEN", "").strip()
    if not token:
        raise RuntimeError(
            "FLAMORIS_CUSTOM_PROPERTIES_TOKEN is required. "
            "Use a fine-grained token with organization Custom properties: Read."
        )

    org = os.environ.get("FLAMORIS_ORG", "flamoris-jp").strip()
    property_name = os.environ.get(
        "FLAMORIS_DEVELOPMENT_STATUS_PROPERTY", "development_status"
    ).strip()
    profile_path = Path(
        os.environ.get("FLAMORIS_PROFILE_README", "profile/README.md")
    )

    validate_property_schema(org, property_name, token)
    public_names = public_repository_names(org, token)
    statuses = development_statuses(org, property_name, token, public_names)
    rendered = render_status_block(org, property_name, statuses)
    changed = replace_generated_section(profile_path, rendered)

    print(
        f"development status sync: {len(public_names)} public repositories, "
        f"profile {'updated' if changed else 'unchanged'}"
    )
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except Exception as exc:
        print(f"error: {exc}", file=sys.stderr)
        raise SystemExit(1)
