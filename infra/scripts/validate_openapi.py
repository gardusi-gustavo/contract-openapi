#!/usr/bin/env python3
from __future__ import annotations
import sys
from pathlib import Path
import yaml

spec = yaml.safe_load(Path("openapi.yaml").read_text())
errors = []
if not str(spec.get("openapi", "")).startswith("3.1"):
    errors.append("openapi must be 3.1.x")
if not spec.get("info", {}).get("version"):
    errors.append("info.version is required")
paths = spec.get("paths") or {}
for path in ("/health", "/repos", "/progress"):
    if path not in paths:
        errors.append(f"missing path: {path}")
    else:
        operation = paths[path].get("get") or {}
        if not operation.get("operationId"):
            errors.append(f"{path}: operationId is required")
        if "200" not in operation.get("responses", {}):
            errors.append(f"{path}: 200 response is required")
schemas = spec.get("components", {}).get("schemas") or {}
for name in ("Health", "Repository", "Progress"):
    if name not in schemas:
        errors.append(f"missing schema: {name}")
for error in errors:
    print(f"ERROR: {error}", file=sys.stderr)
if errors:
    raise SystemExit(1)
print(f"openapi ok: {len(paths)} paths, {len(schemas)} schemas")
