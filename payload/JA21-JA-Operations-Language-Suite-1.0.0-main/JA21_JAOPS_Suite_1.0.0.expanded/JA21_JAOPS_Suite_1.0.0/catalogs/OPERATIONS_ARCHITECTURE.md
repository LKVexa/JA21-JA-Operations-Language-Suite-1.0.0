# JA Operations Language Architecture

```text
JAOPS source (.jaops)
        │
        ▼
Parser and policy loader
        │  workspace, target, compiler profile, dependencies, environment
        ▼
Typed Operations AST
        │  resources, services, bindings, health, scaling, upgrade, rollback
        ▼
Semantic and capability judgment
        │  network, secret, build, deployment, package, ledger effects
        ▼
R12 operational record
        │  stable identity, inputs, policy decision, output hashes
        ▼
JA Operations Executor
        │  deterministic plan, sandbox, probes, rollback journal
        ▼
MSSLB / installer / deployment artifact
        │
        ▼
MCRT receipt and replay evidence
```

## Architectural invariants

- No implicit network authority.
- Secret values remain references and are redacted from logs and receipts.
- Dependency, compiler, policy, target, and lock hashes determine build-cache identity.
- Scaling, upgrade, and rollback transitions are explicit state-machine edges.
- Health probes cannot silently widen capabilities.
- Offline and air-gapped profiles fail closed when an undeclared dependency is required.
- Optimization must preserve policy decisions, R12 identities, MCRT provenance, and recovery behavior.
