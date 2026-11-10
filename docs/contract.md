# Contract rules

The contract describes read-only endpoints exposed by the devops data plane:

| Endpoint | Purpose |
| --- | --- |
| `/health` | Liveness and schema version |
| `/repos` | Repository inventory and archive state |
| `/progress` | Progress metrics and per-repository rows |

The spec is the source of truth. Generated clients and documentation must be
built from `openapi.yaml`, not from hand-written copies.
