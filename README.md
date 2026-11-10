# contract-openapi

OpenAPI 3.1 contracts for the public devops data plane.

## Layout

| Path | Holds |
| --- | --- |
| `openapi.yaml` | REST specification |
| `schemas/` | Reusable JSON schemas |
| `examples/` | Request and response examples |
| `docs/` | Contract rules and usage |
| `docs/issues/` | Local task queue |

## Validation

```bash
bash infra/scripts/ci.sh
npx --yes @redocly/cli@latest lint openapi.yaml
```

## Rules

- Public contracts only.
- Every operation has an `operationId` and a `200` response.
- Breaking changes require a version bump.
