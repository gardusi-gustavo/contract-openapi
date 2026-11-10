#!/usr/bin/env bash
set -euo pipefail
ROOT="${CI_PROJECT_DIR:-$(git rev-parse --show-toplevel)}"
cd "$ROOT"
"$ROOT/infra/scripts/ci/validate-repo.sh" --root "$ROOT"
"$ROOT/infra/scripts/ci/check-size.sh" --root "$ROOT"
"$ROOT/infra/scripts/ci/validate-local-issues.sh" --root "$ROOT"
python3 infra/scripts/validate_openapi.py
echo "contract-openapi checks ok"
