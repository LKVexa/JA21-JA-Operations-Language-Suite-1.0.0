# JA21 JA Operations Language Textbook
## Reproducible Builds, Governed Deployment, Reliable Recovery, and Evidence

**Edition:** 1.0.0  
**Suite:** JA21 JA Operations Language Suite  
**Extension:** `.jaops`  
**Evidence status:** corpus-modeled unless a separate native execution report is supplied.

## Preface

This textbook turns the uploaded JA Operations Language corpus into a coherent course of study. It treats builds, services, deployment, upgrades, rollback, packaging, offline operation, and air-gapped release as typed language concerns. The 10,000-record corpus is the technical reference; the 1,000-program pack is the laboratory library; this book provides the conceptual sequence and review discipline.

The five analytical roles are used throughout. **SOPHIA** examines semantic and systemic coherence. **CHARLOTTE** examines operational information architecture and human-readable control surfaces. **LANDON** examines compiler, executor, scheduler, platform, and recovery feasibility. **Professor** examines pedagogy, counterexamples, and proof obligations. **Podium** examines publication, release, integrity, and certification readiness.

## How to use the book

Read each chapter with the representative `.jaops` program open. Follow the source hash through the script catalog into the normalized corpus record. Compare source, semantic judgment, typed AST, R12 record, modeled runtime plan, and MCRT identity. Never present modeled outcomes as native execution evidence; implement and record native tests separately.

## Contents

1. The JA Operations Language as a Full Suite
2. Program Anatomy, Workspaces, and Policy
3. Targets, Compiler Profiles, and Environments
4. Dependencies, Lockfiles, and Reproducibility
5. Resource and GPU Requirements
6. Services, Workers, and LANDON Workers
7. Scaling Rules and Capacity Envelopes
8. Health Checks, Metrics, Logging, and Traces
9. Network and Storage Bindings
10. Secret References and Capability Boundaries
11. Deployment Timelines and Release Channels
12. Upgrade Strategies and Rollback Rules
13. Deployment Probes and Readiness Certification
14. Offline and Air-Gapped Deployment
15. Project, Workspace, and Clean-Room Builds
16. Artifact Repositories and MSSLB Packaging
17. Desktop Installers and Target Deployment
18. Compiler Frontend, Typed AST, and Diagnostics
19. Runtime Executor, Scheduler, and Replay
20. Optimization and Caching Without Semantic Drift
21. R12, MCRT, Certification, and Smithson 8S
22. Standalone JA Operations Toolchain Capstone

# Chapter 1: The JA Operations Language as a Full Suite

## Learning objectives

- Explain operations programs as evidence-bearing deployment specifications using JA Operations source, semantic, AST, R12, runtime, and MCRT layers.
- State and test the invariant that source, policy, plan, artifact, and receipt remain connected.
- Construct a positive case and a minimal case involving treating deployment files as untyped shell fragments.
- Separate modeled corpus evidence from native compiler or executor evidence.

## Technical foundation

This chapter treats **operations programs as evidence-bearing deployment specifications** as a language concern rather than an informal runbook convention. In JA Operations, declarations are compiled into a typed operational graph whose nodes carry identity, effects, capabilities, policy decisions, and recovery obligations. That graph is valuable because it makes infrastructure intent reviewable before any external process is started. The author can reason about a workspace as a bounded state machine, while the compiler can reject undeclared authority and the runtime can emit evidence tied to the same source hash.

The governing invariant is that **source, policy, plan, artifact, and receipt remain connected**. This requires more than syntactic validity. A conforming implementation must preserve the link between module identity, AST node identity, semantic judgment, R12 lowering, execution plan, and MCRT receipt. The corpus uses operator `build` for the representative record and models effects `secret.read` under capabilities `ledger.append`. Those values are not decorative metadata: they define what can be optimized, what must be sandboxed, and what a certifier must be able to replay.

A common failure mode is **treating deployment files as untyped shell fragments**. The language should surface that condition at the earliest reliable stage: parsing for malformed declarations, semantic analysis for incompatible types or topology, policy analysis for unauthorized effects, plan construction for unsatisfied dependencies, and runtime validation for environmental divergence. The technical corpus includes positive, negative, boundary, integration, security, performance, determinism, interoperability, recovery, and certification classes so that a future implementation learns both acceptance and refusal behavior.

Implementation should proceed through small explicit passes. Parse the source into stable nodes; resolve workspace and target names; infer the operational artifact type; compute effects and required capabilities; evaluate network, secret, build, deployment, package, and ledger policy; lower accepted nodes to R12; build a deterministic execution plan; and reserve MCRT emission for a modeled or native outcome with an unambiguous evidence label. Optimization may fold declarations or reuse artifacts only when the dependency, compiler, target, environment, policy, lock, and source identities match the declared equivalence profile.

## Representative corpus program

**Record:** `JAOPS-00032`  
**Feature:** `workspace_build`  
**Level:** `beginner`  
**Validation class:** `positive`  
**Source SHA-256:** `1be02938a8886c508037d28f4c38382e521dccd293e3d3eceaa3b0d11051e2e3`

```jaops
ja source 0.3
module corpus.ja_operations.example_00032
use Operations
policy explicit_network

workspace SuiteJAOPS_00032 {
    target windows-x64
    compiler profile release
    dependencies locked
    environment offline
    resource cpu 2 memory 4GB
    network disabled
    secret signing_key reference "vault://release/signing"
    service worker_34 replicas 1
    health_check worker_34 every 7s
    upgrade rolling
    rollback on health_failure
    package msslb
}
assert deployment.reproducible == true
emit package "SuiteJAOPS_00032.msslb"
```

## Evidence trace

- Semantic identity: `sem-053242a01290b6a99e7e`
- Judgment: `Environment; Policy; {ledger.append} ⊢ node-d6a1d74fd33db4e12f49 : DeploymentArtifact ! {secret.read} ⇒ validated`
- AST node: `node-d6a1d74fd33db4e12f49` (`DeploymentDecl`)
- Declared/inferred type: `DeploymentArtifact` / `DeploymentArtifact`
- Effects: `secret.read`
- Capabilities: `ledger.append`
- Semantic operator: `build`
- Policy decision: `allow`
- R12 record: `r12-ffb7c4aba016646946b0`
- MCRT record: `mcrt-a2e4b7e04bfca48fb50b`
- Expected validation: `pass`
- Diagnostic: `none`
- Evidence scope: modeled, not native execution

## Five-lens review

SOPHIA examines whether the declaration, effect set, capability path, recovery behavior, and evidence identities form one coherent system. CHARLOTTE examines whether the operational information architecture is legible: authors should see prerequisites, gates, risks, transitions, and remedies without reading raw runtime logs. LANDON examines parser support, scheduler feasibility, sandbox boundaries, file and process behavior, target constraints, and observability. Professor requires a stated invariant, a positive case, a minimal counterexample, and a test oracle. Podium requires release-ready navigation, provenance, checksums, evidence boundaries, and a clear certification decision.

## Engineering checklist

- Confirm stable source, AST, R12, and MCRT identities.
- Verify all effects have explicit capabilities and policy decisions.
- Verify secrets remain references and are redacted from every evidence surface.
- Verify network, storage, build, package, deployment, and ledger boundaries.
- Verify failure, retry, rollback, and terminal states are explicit.
- Verify deterministic replay inputs and cache keys are complete.
- Record unsupported behavior as a diagnostic rather than a silent approximation.

## Laboratory

**Task:** Assemble a minimal standalone operations suite and evidence map.

1. Copy the representative program into a separate laboratory module.
2. Write down the invariant before modifying the source.
3. Produce one accepted variant and one minimal rejected variant.
4. Predict the semantic judgment, policy decision, R12 identity change, and MCRT outcome.
5. Run the structural validator; where no native compiler exists, label all remaining results as modeled.
6. Submit source, expected diagnostics, evidence map, replay inputs, and a concise certification decision.

## Review questions

1. Which declaration carries the most important operational authority in this chapter?
2. Which hash or identity must change when the program is modified, and which identities may remain stable?
3. At what stage should the primary failure be detected?
4. Which optimization is safe, and which optimization would erase a policy or recovery obligation?
5. What native test would be required to promote the modeled outcome into execution evidence?

# Chapter 2: Program Anatomy, Workspaces, and Policy

## Learning objectives

- Explain workspace boundaries, module identity, and explicit policy declarations using JA Operations source, semantic, AST, R12, runtime, and MCRT layers.
- State and test the invariant that every executable operation belongs to a named workspace and policy context.
- Construct a positive case and a minimal case involving allowing declarations to inherit undeclared authority.
- Separate modeled corpus evidence from native compiler or executor evidence.

## Technical foundation

This chapter treats **workspace boundaries, module identity, and explicit policy declarations** as a language concern rather than an informal runbook convention. In JA Operations, declarations are compiled into a typed operational graph whose nodes carry identity, effects, capabilities, policy decisions, and recovery obligations. That graph is valuable because it makes infrastructure intent reviewable before any external process is started. The author can reason about a workspace as a bounded state machine, while the compiler can reject undeclared authority and the runtime can emit evidence tied to the same source hash.

The governing invariant is that **every executable operation belongs to a named workspace and policy context**. This requires more than syntactic validity. A conforming implementation must preserve the link between module identity, AST node identity, semantic judgment, R12 lowering, execution plan, and MCRT receipt. The corpus uses operator `build` for the representative record and models effects `secret.read` under capabilities `ledger.append`. Those values are not decorative metadata: they define what can be optimized, what must be sandboxed, and what a certifier must be able to replay.

A common failure mode is **allowing declarations to inherit undeclared authority**. The language should surface that condition at the earliest reliable stage: parsing for malformed declarations, semantic analysis for incompatible types or topology, policy analysis for unauthorized effects, plan construction for unsatisfied dependencies, and runtime validation for environmental divergence. The technical corpus includes positive, negative, boundary, integration, security, performance, determinism, interoperability, recovery, and certification classes so that a future implementation learns both acceptance and refusal behavior.

Implementation should proceed through small explicit passes. Parse the source into stable nodes; resolve workspace and target names; infer the operational artifact type; compute effects and required capabilities; evaluate network, secret, build, deployment, package, and ledger policy; lower accepted nodes to R12; build a deterministic execution plan; and reserve MCRT emission for a modeled or native outcome with an unambiguous evidence label. Optimization may fold declarations or reuse artifacts only when the dependency, compiler, target, environment, policy, lock, and source identities match the declared equivalence profile.

## Representative corpus program

**Record:** `JAOPS-00032`  
**Feature:** `workspace_build`  
**Level:** `beginner`  
**Validation class:** `positive`  
**Source SHA-256:** `1be02938a8886c508037d28f4c38382e521dccd293e3d3eceaa3b0d11051e2e3`

```jaops
ja source 0.3
module corpus.ja_operations.example_00032
use Operations
policy explicit_network

workspace SuiteJAOPS_00032 {
    target windows-x64
    compiler profile release
    dependencies locked
    environment offline
    resource cpu 2 memory 4GB
    network disabled
    secret signing_key reference "vault://release/signing"
    service worker_34 replicas 1
    health_check worker_34 every 7s
    upgrade rolling
    rollback on health_failure
    package msslb
}
assert deployment.reproducible == true
emit package "SuiteJAOPS_00032.msslb"
```

## Evidence trace

- Semantic identity: `sem-053242a01290b6a99e7e`
- Judgment: `Environment; Policy; {ledger.append} ⊢ node-d6a1d74fd33db4e12f49 : DeploymentArtifact ! {secret.read} ⇒ validated`
- AST node: `node-d6a1d74fd33db4e12f49` (`DeploymentDecl`)
- Declared/inferred type: `DeploymentArtifact` / `DeploymentArtifact`
- Effects: `secret.read`
- Capabilities: `ledger.append`
- Semantic operator: `build`
- Policy decision: `allow`
- R12 record: `r12-ffb7c4aba016646946b0`
- MCRT record: `mcrt-a2e4b7e04bfca48fb50b`
- Expected validation: `pass`
- Diagnostic: `none`
- Evidence scope: modeled, not native execution

## Five-lens review

SOPHIA examines whether the declaration, effect set, capability path, recovery behavior, and evidence identities form one coherent system. CHARLOTTE examines whether the operational information architecture is legible: authors should see prerequisites, gates, risks, transitions, and remedies without reading raw runtime logs. LANDON examines parser support, scheduler feasibility, sandbox boundaries, file and process behavior, target constraints, and observability. Professor requires a stated invariant, a positive case, a minimal counterexample, and a test oracle. Podium requires release-ready navigation, provenance, checksums, evidence boundaries, and a clear certification decision.

## Engineering checklist

- Confirm stable source, AST, R12, and MCRT identities.
- Verify all effects have explicit capabilities and policy decisions.
- Verify secrets remain references and are redacted from every evidence surface.
- Verify network, storage, build, package, deployment, and ledger boundaries.
- Verify failure, retry, rollback, and terminal states are explicit.
- Verify deterministic replay inputs and cache keys are complete.
- Record unsupported behavior as a diagnostic rather than a silent approximation.

## Laboratory

**Task:** Compare a positive workspace with a minimal policy violation.

1. Copy the representative program into a separate laboratory module.
2. Write down the invariant before modifying the source.
3. Produce one accepted variant and one minimal rejected variant.
4. Predict the semantic judgment, policy decision, R12 identity change, and MCRT outcome.
5. Run the structural validator; where no native compiler exists, label all remaining results as modeled.
6. Submit source, expected diagnostics, evidence map, replay inputs, and a concise certification decision.

## Review questions

1. Which declaration carries the most important operational authority in this chapter?
2. Which hash or identity must change when the program is modified, and which identities may remain stable?
3. At what stage should the primary failure be detected?
4. Which optimization is safe, and which optimization would erase a policy or recovery obligation?
5. What native test would be required to promote the modeled outcome into execution evidence?

# Chapter 3: Targets, Compiler Profiles, and Environments

## Learning objectives

- Explain target and compiler profiles as reproducibility inputs using JA Operations source, semantic, AST, R12, runtime, and MCRT layers.
- State and test the invariant that target, compiler, environment, and policy hashes define a stable build identity.
- Construct a positive case and a minimal case involving reusing artifacts across incompatible profiles.
- Separate modeled corpus evidence from native compiler or executor evidence.

## Technical foundation

This chapter treats **target and compiler profiles as reproducibility inputs** as a language concern rather than an informal runbook convention. In JA Operations, declarations are compiled into a typed operational graph whose nodes carry identity, effects, capabilities, policy decisions, and recovery obligations. That graph is valuable because it makes infrastructure intent reviewable before any external process is started. The author can reason about a workspace as a bounded state machine, while the compiler can reject undeclared authority and the runtime can emit evidence tied to the same source hash.

The governing invariant is that **target, compiler, environment, and policy hashes define a stable build identity**. This requires more than syntactic validity. A conforming implementation must preserve the link between module identity, AST node identity, semantic judgment, R12 lowering, execution plan, and MCRT receipt. The corpus uses operator `deploy` for the representative record and models effects `ledger.append` under capabilities `network.connect:declared`. Those values are not decorative metadata: they define what can be optimized, what must be sandboxed, and what a certifier must be able to replay.

A common failure mode is **reusing artifacts across incompatible profiles**. The language should surface that condition at the earliest reliable stage: parsing for malformed declarations, semantic analysis for incompatible types or topology, policy analysis for unauthorized effects, plan construction for unsatisfied dependencies, and runtime validation for environmental divergence. The technical corpus includes positive, negative, boundary, integration, security, performance, determinism, interoperability, recovery, and certification classes so that a future implementation learns both acceptance and refusal behavior.

Implementation should proceed through small explicit passes. Parse the source into stable nodes; resolve workspace and target names; infer the operational artifact type; compute effects and required capabilities; evaluate network, secret, build, deployment, package, and ledger policy; lower accepted nodes to R12; build a deterministic execution plan; and reserve MCRT emission for a modeled or native outcome with an unambiguous evidence label. Optimization may fold declarations or reuse artifacts only when the dependency, compiler, target, environment, policy, lock, and source identities match the declared equivalence profile.

## Representative corpus program

**Record:** `JAOPS-00261`  
**Feature:** `compiler_profile`  
**Level:** `beginner`  
**Validation class:** `positive`  
**Source SHA-256:** `387650ddb8ff0314d0856b293b59eeaae621cda827f4205b8ea0494bac25db6e`

```jaops
ja source 0.3
module corpus.ja_operations.example_00261
use Operations
policy explicit_network

workspace SuiteJAOPS_00261 {
    target windows-x64
    compiler profile release
    dependencies locked
    environment offline
    resource cpu 7 memory 9GB
    network disabled
    secret signing_key reference "vault://release/signing"
    service worker_69 replicas 2
    health_check worker_69 every 19s
    upgrade rolling
    rollback on health_failure
    package msslb
}
assert deployment.reproducible == true
emit package "SuiteJAOPS_00261.msslb"
```

## Evidence trace

- Semantic identity: `sem-4b1af21751f87674d494`
- Judgment: `Environment; Policy; {network.connect:declared} ⊢ node-8fca17528bf69fe64f39 : DeploymentArtifact ! {ledger.append} ⇒ validated`
- AST node: `node-8fca17528bf69fe64f39` (`DeploymentDecl`)
- Declared/inferred type: `DeploymentArtifact` / `DeploymentArtifact`
- Effects: `ledger.append`
- Capabilities: `network.connect:declared`
- Semantic operator: `deploy`
- Policy decision: `allow`
- R12 record: `r12-cd228bc09e16282c6c5f`
- MCRT record: `mcrt-40b82c389b6c08b82459`
- Expected validation: `pass`
- Diagnostic: `none`
- Evidence scope: modeled, not native execution

## Five-lens review

SOPHIA examines whether the declaration, effect set, capability path, recovery behavior, and evidence identities form one coherent system. CHARLOTTE examines whether the operational information architecture is legible: authors should see prerequisites, gates, risks, transitions, and remedies without reading raw runtime logs. LANDON examines parser support, scheduler feasibility, sandbox boundaries, file and process behavior, target constraints, and observability. Professor requires a stated invariant, a positive case, a minimal counterexample, and a test oracle. Podium requires release-ready navigation, provenance, checksums, evidence boundaries, and a clear certification decision.

## Engineering checklist

- Confirm stable source, AST, R12, and MCRT identities.
- Verify all effects have explicit capabilities and policy decisions.
- Verify secrets remain references and are redacted from every evidence surface.
- Verify network, storage, build, package, deployment, and ledger boundaries.
- Verify failure, retry, rollback, and terminal states are explicit.
- Verify deterministic replay inputs and cache keys are complete.
- Record unsupported behavior as a diagnostic rather than a silent approximation.

## Laboratory

**Task:** Construct a matrix of target/profile/environment identities.

1. Copy the representative program into a separate laboratory module.
2. Write down the invariant before modifying the source.
3. Produce one accepted variant and one minimal rejected variant.
4. Predict the semantic judgment, policy decision, R12 identity change, and MCRT outcome.
5. Run the structural validator; where no native compiler exists, label all remaining results as modeled.
6. Submit source, expected diagnostics, evidence map, replay inputs, and a concise certification decision.

## Review questions

1. Which declaration carries the most important operational authority in this chapter?
2. Which hash or identity must change when the program is modified, and which identities may remain stable?
3. At what stage should the primary failure be detected?
4. Which optimization is safe, and which optimization would erase a policy or recovery obligation?
5. What native test would be required to promote the modeled outcome into execution evidence?

# Chapter 4: Dependencies, Lockfiles, and Reproducibility

## Learning objectives

- Explain dependency resolution and immutable lock evidence using JA Operations source, semantic, AST, R12, runtime, and MCRT layers.
- State and test the invariant that the lock graph and artifact repository identities are closed and replayable.
- Construct a positive case and a minimal case involving floating dependencies and hidden transitive downloads.
- Separate modeled corpus evidence from native compiler or executor evidence.

## Technical foundation

This chapter treats **dependency resolution and immutable lock evidence** as a language concern rather than an informal runbook convention. In JA Operations, declarations are compiled into a typed operational graph whose nodes carry identity, effects, capabilities, policy decisions, and recovery obligations. That graph is valuable because it makes infrastructure intent reviewable before any external process is started. The author can reason about a workspace as a bounded state machine, while the compiler can reject undeclared authority and the runtime can emit evidence tied to the same source hash.

The governing invariant is that **the lock graph and artifact repository identities are closed and replayable**. This requires more than syntactic validity. A conforming implementation must preserve the link between module identity, AST node identity, semantic judgment, R12 lowering, execution plan, and MCRT receipt. The corpus uses operator `package` for the representative record and models effects `file.read` under capabilities `secret.read:reference_only`. Those values are not decorative metadata: they define what can be optimized, what must be sandboxed, and what a certifier must be able to replay.

A common failure mode is **floating dependencies and hidden transitive downloads**. The language should surface that condition at the earliest reliable stage: parsing for malformed declarations, semantic analysis for incompatible types or topology, policy analysis for unauthorized effects, plan construction for unsatisfied dependencies, and runtime validation for environmental divergence. The technical corpus includes positive, negative, boundary, integration, security, performance, determinism, interoperability, recovery, and certification classes so that a future implementation learns both acceptance and refusal behavior.

Implementation should proceed through small explicit passes. Parse the source into stable nodes; resolve workspace and target names; infer the operational artifact type; compute effects and required capabilities; evaluate network, secret, build, deployment, package, and ledger policy; lower accepted nodes to R12; build a deterministic execution plan; and reserve MCRT emission for a modeled or native outcome with an unambiguous evidence label. Optimization may fold declarations or reuse artifacts only when the dependency, compiler, target, environment, policy, lock, and source identities match the declared equivalence profile.

## Representative corpus program

**Record:** `JAOPS-00028`  
**Feature:** `dependency`  
**Level:** `beginner`  
**Validation class:** `positive`  
**Source SHA-256:** `2665fbe0175688ed9180a96c8384d7b0c0565668b0d7bfb9213424f95ad060f5`

```jaops
ja source 0.3
module corpus.ja_operations.example_00028
use Operations
policy explicit_network

workspace SuiteJAOPS_00028 {
    target windows-x64
    compiler profile release
    dependencies locked
    environment offline
    resource cpu 6 memory 16GB
    network disabled
    secret signing_key reference "vault://release/signing"
    service worker_30 replicas 1
    health_check worker_30 every 34s
    upgrade rolling
    rollback on health_failure
    package msslb
}
assert deployment.reproducible == true
emit package "SuiteJAOPS_00028.msslb"
```

## Evidence trace

- Semantic identity: `sem-e590f0bba6df5d1dbf81`
- Judgment: `Environment; Policy; {secret.read:reference_only} ⊢ node-c877cd55cba09dc2bcc0 : DeploymentArtifact ! {file.read} ⇒ validated`
- AST node: `node-c877cd55cba09dc2bcc0` (`DeploymentDecl`)
- Declared/inferred type: `DeploymentArtifact` / `DeploymentArtifact`
- Effects: `file.read`
- Capabilities: `secret.read:reference_only`
- Semantic operator: `package`
- Policy decision: `allow`
- R12 record: `r12-d263a53dd4d5675a1a32`
- MCRT record: `mcrt-448240236e1cfd22f001`
- Expected validation: `pass`
- Diagnostic: `none`
- Evidence scope: modeled, not native execution

## Five-lens review

SOPHIA examines whether the declaration, effect set, capability path, recovery behavior, and evidence identities form one coherent system. CHARLOTTE examines whether the operational information architecture is legible: authors should see prerequisites, gates, risks, transitions, and remedies without reading raw runtime logs. LANDON examines parser support, scheduler feasibility, sandbox boundaries, file and process behavior, target constraints, and observability. Professor requires a stated invariant, a positive case, a minimal counterexample, and a test oracle. Podium requires release-ready navigation, provenance, checksums, evidence boundaries, and a clear certification decision.

## Engineering checklist

- Confirm stable source, AST, R12, and MCRT identities.
- Verify all effects have explicit capabilities and policy decisions.
- Verify secrets remain references and are redacted from every evidence surface.
- Verify network, storage, build, package, deployment, and ledger boundaries.
- Verify failure, retry, rollback, and terminal states are explicit.
- Verify deterministic replay inputs and cache keys are complete.
- Record unsupported behavior as a diagnostic rather than a silent approximation.

## Laboratory

**Task:** Produce and audit a deterministic dependency lock.

1. Copy the representative program into a separate laboratory module.
2. Write down the invariant before modifying the source.
3. Produce one accepted variant and one minimal rejected variant.
4. Predict the semantic judgment, policy decision, R12 identity change, and MCRT outcome.
5. Run the structural validator; where no native compiler exists, label all remaining results as modeled.
6. Submit source, expected diagnostics, evidence map, replay inputs, and a concise certification decision.

## Review questions

1. Which declaration carries the most important operational authority in this chapter?
2. Which hash or identity must change when the program is modified, and which identities may remain stable?
3. At what stage should the primary failure be detected?
4. Which optimization is safe, and which optimization would erase a policy or recovery obligation?
5. What native test would be required to promote the modeled outcome into execution evidence?

# Chapter 5: Resource and GPU Requirements

## Learning objectives

- Explain typed capacity declarations and admission control using JA Operations source, semantic, AST, R12, runtime, and MCRT layers.
- State and test the invariant that resource requests are validated before scheduling and remain visible in receipts.
- Construct a positive case and a minimal case involving best-effort overcommit that invalidates performance evidence.
- Separate modeled corpus evidence from native compiler or executor evidence.

## Technical foundation

This chapter treats **typed capacity declarations and admission control** as a language concern rather than an informal runbook convention. In JA Operations, declarations are compiled into a typed operational graph whose nodes carry identity, effects, capabilities, policy decisions, and recovery obligations. That graph is valuable because it makes infrastructure intent reviewable before any external process is started. The author can reason about a workspace as a bounded state machine, while the compiler can reject undeclared authority and the runtime can emit evidence tied to the same source hash.

The governing invariant is that **resource requests are validated before scheduling and remain visible in receipts**. This requires more than syntactic validity. A conforming implementation must preserve the link between module identity, AST node identity, semantic judgment, R12 lowering, execution plan, and MCRT receipt. The corpus uses operator `deploy` for the representative record and models effects `file.read` under capabilities `deployment.modify:approved`. Those values are not decorative metadata: they define what can be optimized, what must be sandboxed, and what a certifier must be able to replay.

A common failure mode is **best-effort overcommit that invalidates performance evidence**. The language should surface that condition at the earliest reliable stage: parsing for malformed declarations, semantic analysis for incompatible types or topology, policy analysis for unauthorized effects, plan construction for unsatisfied dependencies, and runtime validation for environmental divergence. The technical corpus includes positive, negative, boundary, integration, security, performance, determinism, interoperability, recovery, and certification classes so that a future implementation learns both acceptance and refusal behavior.

Implementation should proceed through small explicit passes. Parse the source into stable nodes; resolve workspace and target names; infer the operational artifact type; compute effects and required capabilities; evaluate network, secret, build, deployment, package, and ledger policy; lower accepted nodes to R12; build a deterministic execution plan; and reserve MCRT emission for a modeled or native outcome with an unambiguous evidence label. Optimization may fold declarations or reuse artifacts only when the dependency, compiler, target, environment, policy, lock, and source identities match the declared equivalence profile.

## Representative corpus program

**Record:** `JAOPS-00161`  
**Feature:** `resource_requirement`  
**Level:** `beginner`  
**Validation class:** `positive`  
**Source SHA-256:** `325b8636658aa24a2409340dafdc023e2495dd2e07de297dbe418f0bdd794fc0`

```jaops
ja source 0.3
module corpus.ja_operations.example_00161
use Operations
policy explicit_network

workspace SuiteJAOPS_00161 {
    target windows-x64
    compiler profile release
    dependencies locked
    environment offline
    resource cpu 3 memory 5GB
    network disabled
    secret signing_key reference "vault://release/signing"
    service worker_66 replicas 2
    health_check worker_66 every 12s
    upgrade rolling
    rollback on health_failure
    package msslb
}
assert deployment.reproducible == true
emit package "SuiteJAOPS_00161.msslb"
```

## Evidence trace

- Semantic identity: `sem-8392bbfb3030a9dae844`
- Judgment: `Environment; Policy; {deployment.modify:approved} ⊢ node-69a548a02af059a804c5 : DeploymentArtifact ! {file.read} ⇒ validated`
- AST node: `node-69a548a02af059a804c5` (`DeploymentDecl`)
- Declared/inferred type: `DeploymentArtifact` / `DeploymentArtifact`
- Effects: `file.read`
- Capabilities: `deployment.modify:approved`
- Semantic operator: `deploy`
- Policy decision: `allow`
- R12 record: `r12-f5a688cb530e1167fd18`
- MCRT record: `mcrt-3d326f8bec1b0770de86`
- Expected validation: `pass`
- Diagnostic: `none`
- Evidence scope: modeled, not native execution

## Five-lens review

SOPHIA examines whether the declaration, effect set, capability path, recovery behavior, and evidence identities form one coherent system. CHARLOTTE examines whether the operational information architecture is legible: authors should see prerequisites, gates, risks, transitions, and remedies without reading raw runtime logs. LANDON examines parser support, scheduler feasibility, sandbox boundaries, file and process behavior, target constraints, and observability. Professor requires a stated invariant, a positive case, a minimal counterexample, and a test oracle. Podium requires release-ready navigation, provenance, checksums, evidence boundaries, and a clear certification decision.

## Engineering checklist

- Confirm stable source, AST, R12, and MCRT identities.
- Verify all effects have explicit capabilities and policy decisions.
- Verify secrets remain references and are redacted from every evidence surface.
- Verify network, storage, build, package, deployment, and ledger boundaries.
- Verify failure, retry, rollback, and terminal states are explicit.
- Verify deterministic replay inputs and cache keys are complete.
- Record unsupported behavior as a diagnostic rather than a silent approximation.

## Laboratory

**Task:** Design admission tests for cpu, memory, storage, and gpu limits.

1. Copy the representative program into a separate laboratory module.
2. Write down the invariant before modifying the source.
3. Produce one accepted variant and one minimal rejected variant.
4. Predict the semantic judgment, policy decision, R12 identity change, and MCRT outcome.
5. Run the structural validator; where no native compiler exists, label all remaining results as modeled.
6. Submit source, expected diagnostics, evidence map, replay inputs, and a concise certification decision.

## Review questions

1. Which declaration carries the most important operational authority in this chapter?
2. Which hash or identity must change when the program is modified, and which identities may remain stable?
3. At what stage should the primary failure be detected?
4. Which optimization is safe, and which optimization would erase a policy or recovery obligation?
5. What native test would be required to promote the modeled outcome into execution evidence?

# Chapter 6: Services, Workers, and LANDON Workers

## Learning objectives

- Explain service topology, worker identity, and governed execution roles using JA Operations source, semantic, AST, R12, runtime, and MCRT layers.
- State and test the invariant that replica identities and capabilities are explicit and restart-safe.
- Construct a positive case and a minimal case involving anonymous workers with mutable authority.
- Separate modeled corpus evidence from native compiler or executor evidence.

## Technical foundation

This chapter treats **service topology, worker identity, and governed execution roles** as a language concern rather than an informal runbook convention. In JA Operations, declarations are compiled into a typed operational graph whose nodes carry identity, effects, capabilities, policy decisions, and recovery obligations. That graph is valuable because it makes infrastructure intent reviewable before any external process is started. The author can reason about a workspace as a bounded state machine, while the compiler can reject undeclared authority and the runtime can emit evidence tied to the same source hash.

The governing invariant is that **replica identities and capabilities are explicit and restart-safe**. This requires more than syntactic validity. A conforming implementation must preserve the link between module identity, AST node identity, semantic judgment, R12 lowering, execution plan, and MCRT receipt. The corpus uses operator `deploy` for the representative record and models effects `file.read` under capabilities `build.execute`. Those values are not decorative metadata: they define what can be optimized, what must be sandboxed, and what a certifier must be able to replay.

A common failure mode is **anonymous workers with mutable authority**. The language should surface that condition at the earliest reliable stage: parsing for malformed declarations, semantic analysis for incompatible types or topology, policy analysis for unauthorized effects, plan construction for unsatisfied dependencies, and runtime validation for environmental divergence. The technical corpus includes positive, negative, boundary, integration, security, performance, determinism, interoperability, recovery, and certification classes so that a future implementation learns both acceptance and refusal behavior.

Implementation should proceed through small explicit passes. Parse the source into stable nodes; resolve workspace and target names; infer the operational artifact type; compute effects and required capabilities; evaluate network, secret, build, deployment, package, and ledger policy; lower accepted nodes to R12; build a deterministic execution plan; and reserve MCRT emission for a modeled or native outcome with an unambiguous evidence label. Optimization may fold declarations or reuse artifacts only when the dependency, compiler, target, environment, policy, lock, and source identities match the declared equivalence profile.

## Representative corpus program

**Record:** `JAOPS-00301`  
**Feature:** `landon_worker`  
**Level:** `beginner`  
**Validation class:** `positive`  
**Source SHA-256:** `c3f63debea63a2a6489dba22e7c78d8e9258967025995d0688838cb765d67b93`

```jaops
ja source 0.3
module corpus.ja_operations.example_00301
use Operations
policy explicit_network

workspace SuiteJAOPS_00301 {
    target windows-x64
    compiler profile release
    dependencies locked
    environment offline
    resource cpu 7 memory 17GB
    network disabled
    secret signing_key reference "vault://release/signing"
    service worker_12 replicas 2
    health_check worker_12 every 28s
    upgrade rolling
    rollback on health_failure
    package msslb
}
assert deployment.reproducible == true
emit package "SuiteJAOPS_00301.msslb"
```

## Evidence trace

- Semantic identity: `sem-6eaa3e5a491595f897f4`
- Judgment: `Environment; Policy; {build.execute} ⊢ node-88e256cdfd463f67b4e2 : DeploymentArtifact ! {file.read} ⇒ validated`
- AST node: `node-88e256cdfd463f67b4e2` (`DeploymentDecl`)
- Declared/inferred type: `DeploymentArtifact` / `DeploymentArtifact`
- Effects: `file.read`
- Capabilities: `build.execute`
- Semantic operator: `deploy`
- Policy decision: `allow`
- R12 record: `r12-46f5723b623bc4f49b10`
- MCRT record: `mcrt-50ad0d691f8c1fb75d14`
- Expected validation: `pass`
- Diagnostic: `none`
- Evidence scope: modeled, not native execution

## Five-lens review

SOPHIA examines whether the declaration, effect set, capability path, recovery behavior, and evidence identities form one coherent system. CHARLOTTE examines whether the operational information architecture is legible: authors should see prerequisites, gates, risks, transitions, and remedies without reading raw runtime logs. LANDON examines parser support, scheduler feasibility, sandbox boundaries, file and process behavior, target constraints, and observability. Professor requires a stated invariant, a positive case, a minimal counterexample, and a test oracle. Podium requires release-ready navigation, provenance, checksums, evidence boundaries, and a clear certification decision.

## Engineering checklist

- Confirm stable source, AST, R12, and MCRT identities.
- Verify all effects have explicit capabilities and policy decisions.
- Verify secrets remain references and are redacted from every evidence surface.
- Verify network, storage, build, package, deployment, and ledger boundaries.
- Verify failure, retry, rollback, and terminal states are explicit.
- Verify deterministic replay inputs and cache keys are complete.
- Record unsupported behavior as a diagnostic rather than a silent approximation.

## Laboratory

**Task:** Model a service with ordinary and landon-governed workers.

1. Copy the representative program into a separate laboratory module.
2. Write down the invariant before modifying the source.
3. Produce one accepted variant and one minimal rejected variant.
4. Predict the semantic judgment, policy decision, R12 identity change, and MCRT outcome.
5. Run the structural validator; where no native compiler exists, label all remaining results as modeled.
6. Submit source, expected diagnostics, evidence map, replay inputs, and a concise certification decision.

## Review questions

1. Which declaration carries the most important operational authority in this chapter?
2. Which hash or identity must change when the program is modified, and which identities may remain stable?
3. At what stage should the primary failure be detected?
4. Which optimization is safe, and which optimization would erase a policy or recovery obligation?
5. What native test would be required to promote the modeled outcome into execution evidence?

# Chapter 7: Scaling Rules and Capacity Envelopes

## Learning objectives

- Explain deterministic scaling decisions based on declared metrics and bounds using JA Operations source, semantic, AST, R12, runtime, and MCRT layers.
- State and test the invariant that scale transitions respect minimums, maximums, cooldowns, and evidence windows.
- Construct a positive case and a minimal case involving reactive oscillation and unbounded replica growth.
- Separate modeled corpus evidence from native compiler or executor evidence.

## Technical foundation

This chapter treats **deterministic scaling decisions based on declared metrics and bounds** as a language concern rather than an informal runbook convention. In JA Operations, declarations are compiled into a typed operational graph whose nodes carry identity, effects, capabilities, policy decisions, and recovery obligations. That graph is valuable because it makes infrastructure intent reviewable before any external process is started. The author can reason about a workspace as a bounded state machine, while the compiler can reject undeclared authority and the runtime can emit evidence tied to the same source hash.

The governing invariant is that **scale transitions respect minimums, maximums, cooldowns, and evidence windows**. This requires more than syntactic validity. A conforming implementation must preserve the link between module identity, AST node identity, semantic judgment, R12 lowering, execution plan, and MCRT receipt. The corpus uses operator `build` for the representative record and models effects `ledger.append` under capabilities `ledger.append`. Those values are not decorative metadata: they define what can be optimized, what must be sandboxed, and what a certifier must be able to replay.

A common failure mode is **reactive oscillation and unbounded replica growth**. The language should surface that condition at the earliest reliable stage: parsing for malformed declarations, semantic analysis for incompatible types or topology, policy analysis for unauthorized effects, plan construction for unsatisfied dependencies, and runtime validation for environmental divergence. The technical corpus includes positive, negative, boundary, integration, security, performance, determinism, interoperability, recovery, and certification classes so that a future implementation learns both acceptance and refusal behavior.

Implementation should proceed through small explicit passes. Parse the source into stable nodes; resolve workspace and target names; infer the operational artifact type; compute effects and required capabilities; evaluate network, secret, build, deployment, package, and ledger policy; lower accepted nodes to R12; build a deterministic execution plan; and reserve MCRT emission for a modeled or native outcome with an unambiguous evidence label. Optimization may fold declarations or reuse artifacts only when the dependency, compiler, target, environment, policy, lock, and source identities match the declared equivalence profile.

## Representative corpus program

**Record:** `JAOPS-00002`  
**Feature:** `scaling_rule`  
**Level:** `beginner`  
**Validation class:** `positive`  
**Source SHA-256:** `18673537d0372534de9d9ea965d3eebfa14eb44055e23400253fb34f256de169`

```jaops
ja source 0.3
module corpus.ja_operations.example_00002
use Operations
policy explicit_network

workspace SuiteJAOPS_00002 {
    target windows-x64
    compiler profile release
    dependencies locked
    environment offline
    resource cpu 4 memory 6GB
    network disabled
    secret signing_key reference "vault://release/signing"
    service worker_4 replicas 3
    health_check worker_4 every 8s
    upgrade rolling
    rollback on health_failure
    package msslb
}
assert deployment.reproducible == true
emit package "SuiteJAOPS_00002.msslb"
```

## Evidence trace

- Semantic identity: `sem-b98538b9a0ec92a95b51`
- Judgment: `Environment; Policy; {ledger.append} ⊢ node-e6b1aa70a3c2a46ecc3c : DeploymentArtifact ! {ledger.append} ⇒ validated`
- AST node: `node-e6b1aa70a3c2a46ecc3c` (`DeploymentDecl`)
- Declared/inferred type: `DeploymentArtifact` / `DeploymentArtifact`
- Effects: `ledger.append`
- Capabilities: `ledger.append`
- Semantic operator: `build`
- Policy decision: `allow`
- R12 record: `r12-f240f0609447340d1ecb`
- MCRT record: `mcrt-100872021a42329bdf78`
- Expected validation: `pass`
- Diagnostic: `none`
- Evidence scope: modeled, not native execution

## Five-lens review

SOPHIA examines whether the declaration, effect set, capability path, recovery behavior, and evidence identities form one coherent system. CHARLOTTE examines whether the operational information architecture is legible: authors should see prerequisites, gates, risks, transitions, and remedies without reading raw runtime logs. LANDON examines parser support, scheduler feasibility, sandbox boundaries, file and process behavior, target constraints, and observability. Professor requires a stated invariant, a positive case, a minimal counterexample, and a test oracle. Podium requires release-ready navigation, provenance, checksums, evidence boundaries, and a clear certification decision.

## Engineering checklist

- Confirm stable source, AST, R12, and MCRT identities.
- Verify all effects have explicit capabilities and policy decisions.
- Verify secrets remain references and are redacted from every evidence surface.
- Verify network, storage, build, package, deployment, and ledger boundaries.
- Verify failure, retry, rollback, and terminal states are explicit.
- Verify deterministic replay inputs and cache keys are complete.
- Record unsupported behavior as a diagnostic rather than a silent approximation.

## Laboratory

**Task:** Write and test a bounded scaling envelope.

1. Copy the representative program into a separate laboratory module.
2. Write down the invariant before modifying the source.
3. Produce one accepted variant and one minimal rejected variant.
4. Predict the semantic judgment, policy decision, R12 identity change, and MCRT outcome.
5. Run the structural validator; where no native compiler exists, label all remaining results as modeled.
6. Submit source, expected diagnostics, evidence map, replay inputs, and a concise certification decision.

## Review questions

1. Which declaration carries the most important operational authority in this chapter?
2. Which hash or identity must change when the program is modified, and which identities may remain stable?
3. At what stage should the primary failure be detected?
4. Which optimization is safe, and which optimization would erase a policy or recovery obligation?
5. What native test would be required to promote the modeled outcome into execution evidence?

# Chapter 8: Health Checks, Metrics, Logging, and Traces

## Learning objectives

- Explain observability as typed operational evidence using JA Operations source, semantic, AST, R12, runtime, and MCRT layers.
- State and test the invariant that probes are side-effect bounded and logs redact secrets while retaining trace identity.
- Construct a positive case and a minimal case involving health endpoints that mutate state or leak credentials.
- Separate modeled corpus evidence from native compiler or executor evidence.

## Technical foundation

This chapter treats **observability as typed operational evidence** as a language concern rather than an informal runbook convention. In JA Operations, declarations are compiled into a typed operational graph whose nodes carry identity, effects, capabilities, policy decisions, and recovery obligations. That graph is valuable because it makes infrastructure intent reviewable before any external process is started. The author can reason about a workspace as a bounded state machine, while the compiler can reject undeclared authority and the runtime can emit evidence tied to the same source hash.

The governing invariant is that **probes are side-effect bounded and logs redact secrets while retaining trace identity**. This requires more than syntactic validity. A conforming implementation must preserve the link between module identity, AST node identity, semantic judgment, R12 lowering, execution plan, and MCRT receipt. The corpus uses operator `deploy` for the representative record and models effects `network.connect` under capabilities `network.connect:declared`. Those values are not decorative metadata: they define what can be optimized, what must be sandboxed, and what a certifier must be able to replay.

A common failure mode is **health endpoints that mutate state or leak credentials**. The language should surface that condition at the earliest reliable stage: parsing for malformed declarations, semantic analysis for incompatible types or topology, policy analysis for unauthorized effects, plan construction for unsatisfied dependencies, and runtime validation for environmental divergence. The technical corpus includes positive, negative, boundary, integration, security, performance, determinism, interoperability, recovery, and certification classes so that a future implementation learns both acceptance and refusal behavior.

Implementation should proceed through small explicit passes. Parse the source into stable nodes; resolve workspace and target names; infer the operational artifact type; compute effects and required capabilities; evaluate network, secret, build, deployment, package, and ledger policy; lower accepted nodes to R12; build a deterministic execution plan; and reserve MCRT emission for a modeled or native outcome with an unambiguous evidence label. Optimization may fold declarations or reuse artifacts only when the dependency, compiler, target, environment, policy, lock, and source identities match the declared equivalence profile.

## Representative corpus program

**Record:** `JAOPS-00171`  
**Feature:** `health_check`  
**Level:** `beginner`  
**Validation class:** `positive`  
**Source SHA-256:** `9457284a74a851862dc9d5a6048f5f928531f5efe8bf6f4d68e510b522e4ecd6`

```jaops
ja source 0.3
module corpus.ja_operations.example_00171
use Operations
policy explicit_network

workspace SuiteJAOPS_00171 {
    target windows-x64
    compiler profile release
    dependencies locked
    environment offline
    resource cpu 5 memory 15GB
    network disabled
    secret signing_key reference "vault://release/signing"
    service worker_76 replicas 4
    health_check worker_76 every 22s
    upgrade rolling
    rollback on health_failure
    package msslb
}
assert deployment.reproducible == true
emit package "SuiteJAOPS_00171.msslb"
```

## Evidence trace

- Semantic identity: `sem-10f65874dd2594fc7022`
- Judgment: `Environment; Policy; {network.connect:declared} ⊢ node-ef128fe7109ac5e03be5 : DeploymentArtifact ! {network.connect} ⇒ validated`
- AST node: `node-ef128fe7109ac5e03be5` (`DeploymentDecl`)
- Declared/inferred type: `DeploymentArtifact` / `DeploymentArtifact`
- Effects: `network.connect`
- Capabilities: `network.connect:declared`
- Semantic operator: `deploy`
- Policy decision: `allow`
- R12 record: `r12-c22024b202fcae28b5bb`
- MCRT record: `mcrt-470e211bf449d4259d07`
- Expected validation: `pass`
- Diagnostic: `none`
- Evidence scope: modeled, not native execution

## Five-lens review

SOPHIA examines whether the declaration, effect set, capability path, recovery behavior, and evidence identities form one coherent system. CHARLOTTE examines whether the operational information architecture is legible: authors should see prerequisites, gates, risks, transitions, and remedies without reading raw runtime logs. LANDON examines parser support, scheduler feasibility, sandbox boundaries, file and process behavior, target constraints, and observability. Professor requires a stated invariant, a positive case, a minimal counterexample, and a test oracle. Podium requires release-ready navigation, provenance, checksums, evidence boundaries, and a clear certification decision.

## Engineering checklist

- Confirm stable source, AST, R12, and MCRT identities.
- Verify all effects have explicit capabilities and policy decisions.
- Verify secrets remain references and are redacted from every evidence surface.
- Verify network, storage, build, package, deployment, and ledger boundaries.
- Verify failure, retry, rollback, and terminal states are explicit.
- Verify deterministic replay inputs and cache keys are complete.
- Record unsupported behavior as a diagnostic rather than a silent approximation.

## Laboratory

**Task:** Construct a probe/metric/log/trace evidence chain.

1. Copy the representative program into a separate laboratory module.
2. Write down the invariant before modifying the source.
3. Produce one accepted variant and one minimal rejected variant.
4. Predict the semantic judgment, policy decision, R12 identity change, and MCRT outcome.
5. Run the structural validator; where no native compiler exists, label all remaining results as modeled.
6. Submit source, expected diagnostics, evidence map, replay inputs, and a concise certification decision.

## Review questions

1. Which declaration carries the most important operational authority in this chapter?
2. Which hash or identity must change when the program is modified, and which identities may remain stable?
3. At what stage should the primary failure be detected?
4. Which optimization is safe, and which optimization would erase a policy or recovery obligation?
5. What native test would be required to promote the modeled outcome into execution evidence?

# Chapter 9: Network and Storage Bindings

## Learning objectives

- Explain explicit bindings, locality, and capability-controlled connectivity using JA Operations source, semantic, AST, R12, runtime, and MCRT layers.
- State and test the invariant that every endpoint and volume has a declared authority, protocol, and lifecycle.
- Construct a positive case and a minimal case involving implicit egress, mutable mount semantics, and untracked external state.
- Separate modeled corpus evidence from native compiler or executor evidence.

## Technical foundation

This chapter treats **explicit bindings, locality, and capability-controlled connectivity** as a language concern rather than an informal runbook convention. In JA Operations, declarations are compiled into a typed operational graph whose nodes carry identity, effects, capabilities, policy decisions, and recovery obligations. That graph is valuable because it makes infrastructure intent reviewable before any external process is started. The author can reason about a workspace as a bounded state machine, while the compiler can reject undeclared authority and the runtime can emit evidence tied to the same source hash.

The governing invariant is that **every endpoint and volume has a declared authority, protocol, and lifecycle**. This requires more than syntactic validity. A conforming implementation must preserve the link between module identity, AST node identity, semantic judgment, R12 lowering, execution plan, and MCRT receipt. The corpus uses operator `deploy` for the representative record and models effects `secret.read` under capabilities `deployment.modify:approved`. Those values are not decorative metadata: they define what can be optimized, what must be sandboxed, and what a certifier must be able to replay.

A common failure mode is **implicit egress, mutable mount semantics, and untracked external state**. The language should surface that condition at the earliest reliable stage: parsing for malformed declarations, semantic analysis for incompatible types or topology, policy analysis for unauthorized effects, plan construction for unsatisfied dependencies, and runtime validation for environmental divergence. The technical corpus includes positive, negative, boundary, integration, security, performance, determinism, interoperability, recovery, and certification classes so that a future implementation learns both acceptance and refusal behavior.

Implementation should proceed through small explicit passes. Parse the source into stable nodes; resolve workspace and target names; infer the operational artifact type; compute effects and required capabilities; evaluate network, secret, build, deployment, package, and ledger policy; lower accepted nodes to R12; build a deterministic execution plan; and reserve MCRT emission for a modeled or native outcome with an unambiguous evidence label. Optimization may fold declarations or reuse artifacts only when the dependency, compiler, target, environment, policy, lock, and source identities match the declared equivalence profile.

## Representative corpus program

**Record:** `JAOPS-00221`  
**Feature:** `network_binding`  
**Level:** `beginner`  
**Validation class:** `positive`  
**Source SHA-256:** `90a674dcedef41e16612d0ab64cd9484083b1a995bd81e4a7a1e3da442c51768`

```jaops
ja source 0.3
module corpus.ja_operations.example_00221
use Operations
policy explicit_network

workspace SuiteJAOPS_00221 {
    target windows-x64
    compiler profile release
    dependencies locked
    environment offline
    resource cpu 7 memory 17GB
    network disabled
    secret signing_key reference "vault://release/signing"
    service worker_29 replicas 2
    health_check worker_29 every 10s
    upgrade rolling
    rollback on health_failure
    package msslb
}
assert deployment.reproducible == true
emit package "SuiteJAOPS_00221.msslb"
```

## Evidence trace

- Semantic identity: `sem-95fb0f7e6192454880b3`
- Judgment: `Environment; Policy; {deployment.modify:approved} ⊢ node-0512d4ab5acb35789e41 : DeploymentArtifact ! {secret.read} ⇒ validated`
- AST node: `node-0512d4ab5acb35789e41` (`DeploymentDecl`)
- Declared/inferred type: `DeploymentArtifact` / `DeploymentArtifact`
- Effects: `secret.read`
- Capabilities: `deployment.modify:approved`
- Semantic operator: `deploy`
- Policy decision: `allow`
- R12 record: `r12-2de6d73994ee14743ddc`
- MCRT record: `mcrt-23a0ad8e0d04503380e6`
- Expected validation: `pass`
- Diagnostic: `none`
- Evidence scope: modeled, not native execution

## Five-lens review

SOPHIA examines whether the declaration, effect set, capability path, recovery behavior, and evidence identities form one coherent system. CHARLOTTE examines whether the operational information architecture is legible: authors should see prerequisites, gates, risks, transitions, and remedies without reading raw runtime logs. LANDON examines parser support, scheduler feasibility, sandbox boundaries, file and process behavior, target constraints, and observability. Professor requires a stated invariant, a positive case, a minimal counterexample, and a test oracle. Podium requires release-ready navigation, provenance, checksums, evidence boundaries, and a clear certification decision.

## Engineering checklist

- Confirm stable source, AST, R12, and MCRT identities.
- Verify all effects have explicit capabilities and policy decisions.
- Verify secrets remain references and are redacted from every evidence surface.
- Verify network, storage, build, package, deployment, and ledger boundaries.
- Verify failure, retry, rollback, and terminal states are explicit.
- Verify deterministic replay inputs and cache keys are complete.
- Record unsupported behavior as a diagnostic rather than a silent approximation.

## Laboratory

**Task:** Audit a workspace for undeclared network and storage effects.

1. Copy the representative program into a separate laboratory module.
2. Write down the invariant before modifying the source.
3. Produce one accepted variant and one minimal rejected variant.
4. Predict the semantic judgment, policy decision, R12 identity change, and MCRT outcome.
5. Run the structural validator; where no native compiler exists, label all remaining results as modeled.
6. Submit source, expected diagnostics, evidence map, replay inputs, and a concise certification decision.

## Review questions

1. Which declaration carries the most important operational authority in this chapter?
2. Which hash or identity must change when the program is modified, and which identities may remain stable?
3. At what stage should the primary failure be detected?
4. Which optimization is safe, and which optimization would erase a policy or recovery obligation?
5. What native test would be required to promote the modeled outcome into execution evidence?

# Chapter 10: Secret References and Capability Boundaries

## Learning objectives

- Explain reference-only secret access and least authority using JA Operations source, semantic, AST, R12, runtime, and MCRT layers.
- State and test the invariant that secret material never appears in source, logs, package metadata, or MCRT payloads.
- Construct a positive case and a minimal case involving embedding credentials or broadening capabilities during retry.
- Separate modeled corpus evidence from native compiler or executor evidence.

## Technical foundation

This chapter treats **reference-only secret access and least authority** as a language concern rather than an informal runbook convention. In JA Operations, declarations are compiled into a typed operational graph whose nodes carry identity, effects, capabilities, policy decisions, and recovery obligations. That graph is valuable because it makes infrastructure intent reviewable before any external process is started. The author can reason about a workspace as a bounded state machine, while the compiler can reject undeclared authority and the runtime can emit evidence tied to the same source hash.

The governing invariant is that **secret material never appears in source, logs, package metadata, or MCRT payloads**. This requires more than syntactic validity. A conforming implementation must preserve the link between module identity, AST node identity, semantic judgment, R12 lowering, execution plan, and MCRT receipt. The corpus uses operator `upgrade` for the representative record and models effects `deployment.modify` under capabilities `ledger.append`. Those values are not decorative metadata: they define what can be optimized, what must be sandboxed, and what a certifier must be able to replay.

A common failure mode is **embedding credentials or broadening capabilities during retry**. The language should surface that condition at the earliest reliable stage: parsing for malformed declarations, semantic analysis for incompatible types or topology, policy analysis for unauthorized effects, plan construction for unsatisfied dependencies, and runtime validation for environmental divergence. The technical corpus includes positive, negative, boundary, integration, security, performance, determinism, interoperability, recovery, and certification classes so that a future implementation learns both acceptance and refusal behavior.

Implementation should proceed through small explicit passes. Parse the source into stable nodes; resolve workspace and target names; infer the operational artifact type; compute effects and required capabilities; evaluate network, secret, build, deployment, package, and ledger policy; lower accepted nodes to R12; build a deterministic execution plan; and reserve MCRT emission for a modeled or native outcome with an unambiguous evidence label. Optimization may fold declarations or reuse artifacts only when the dependency, compiler, target, environment, policy, lock, and source identities match the declared equivalence profile.

## Representative corpus program

**Record:** `JAOPS-00020`  
**Feature:** `secret_reference`  
**Level:** `beginner`  
**Validation class:** `positive`  
**Source SHA-256:** `125ace017881f2835223557f4039584d4fdbd7d706542ddbb23e827a5643ad33`

```jaops
ja source 0.3
module corpus.ja_operations.example_00020
use Operations
policy explicit_network

workspace SuiteJAOPS_00020 {
    target windows-x64
    compiler profile release
    dependencies locked
    environment offline
    resource cpu 6 memory 8GB
    network disabled
    secret signing_key reference "vault://release/signing"
    service worker_22 replicas 1
    health_check worker_22 every 26s
    upgrade rolling
    rollback on health_failure
    package msslb
}
assert deployment.reproducible == true
emit package "SuiteJAOPS_00020.msslb"
```

## Evidence trace

- Semantic identity: `sem-e09f0ddbd56410006c1b`
- Judgment: `Environment; Policy; {ledger.append} ⊢ node-30a2e9c324b37d5a0c8c : DeploymentArtifact ! {deployment.modify} ⇒ validated`
- AST node: `node-30a2e9c324b37d5a0c8c` (`DeploymentDecl`)
- Declared/inferred type: `DeploymentArtifact` / `DeploymentArtifact`
- Effects: `deployment.modify`
- Capabilities: `ledger.append`
- Semantic operator: `upgrade`
- Policy decision: `allow`
- R12 record: `r12-e8509ad04259ef42b1a5`
- MCRT record: `mcrt-1133d1dc9e67d4e77e05`
- Expected validation: `pass`
- Diagnostic: `none`
- Evidence scope: modeled, not native execution

## Five-lens review

SOPHIA examines whether the declaration, effect set, capability path, recovery behavior, and evidence identities form one coherent system. CHARLOTTE examines whether the operational information architecture is legible: authors should see prerequisites, gates, risks, transitions, and remedies without reading raw runtime logs. LANDON examines parser support, scheduler feasibility, sandbox boundaries, file and process behavior, target constraints, and observability. Professor requires a stated invariant, a positive case, a minimal counterexample, and a test oracle. Podium requires release-ready navigation, provenance, checksums, evidence boundaries, and a clear certification decision.

## Engineering checklist

- Confirm stable source, AST, R12, and MCRT identities.
- Verify all effects have explicit capabilities and policy decisions.
- Verify secrets remain references and are redacted from every evidence surface.
- Verify network, storage, build, package, deployment, and ledger boundaries.
- Verify failure, retry, rollback, and terminal states are explicit.
- Verify deterministic replay inputs and cache keys are complete.
- Record unsupported behavior as a diagnostic rather than a silent approximation.

## Laboratory

**Task:** Design a secret-reference flow with redaction tests.

1. Copy the representative program into a separate laboratory module.
2. Write down the invariant before modifying the source.
3. Produce one accepted variant and one minimal rejected variant.
4. Predict the semantic judgment, policy decision, R12 identity change, and MCRT outcome.
5. Run the structural validator; where no native compiler exists, label all remaining results as modeled.
6. Submit source, expected diagnostics, evidence map, replay inputs, and a concise certification decision.

## Review questions

1. Which declaration carries the most important operational authority in this chapter?
2. Which hash or identity must change when the program is modified, and which identities may remain stable?
3. At what stage should the primary failure be detected?
4. Which optimization is safe, and which optimization would erase a policy or recovery obligation?
5. What native test would be required to promote the modeled outcome into execution evidence?

# Chapter 11: Deployment Timelines and Release Channels

## Learning objectives

- Explain ordered release stages, promotion gates, and channel identity using JA Operations source, semantic, AST, R12, runtime, and MCRT layers.
- State and test the invariant that promotion requires evidence from the same artifact identity and declared channel.
- Construct a positive case and a minimal case involving rebuilding between stages or promoting by mutable tag.
- Separate modeled corpus evidence from native compiler or executor evidence.

## Technical foundation

This chapter treats **ordered release stages, promotion gates, and channel identity** as a language concern rather than an informal runbook convention. In JA Operations, declarations are compiled into a typed operational graph whose nodes carry identity, effects, capabilities, policy decisions, and recovery obligations. That graph is valuable because it makes infrastructure intent reviewable before any external process is started. The author can reason about a workspace as a bounded state machine, while the compiler can reject undeclared authority and the runtime can emit evidence tied to the same source hash.

The governing invariant is that **promotion requires evidence from the same artifact identity and declared channel**. This requires more than syntactic validity. A conforming implementation must preserve the link between module identity, AST node identity, semantic judgment, R12 lowering, execution plan, and MCRT receipt. The corpus uses operator `scale` for the representative record and models effects `secret.read` under capabilities `secret.read:reference_only`. Those values are not decorative metadata: they define what can be optimized, what must be sandboxed, and what a certifier must be able to replay.

A common failure mode is **rebuilding between stages or promoting by mutable tag**. The language should surface that condition at the earliest reliable stage: parsing for malformed declarations, semantic analysis for incompatible types or topology, policy analysis for unauthorized effects, plan construction for unsatisfied dependencies, and runtime validation for environmental divergence. The technical corpus includes positive, negative, boundary, integration, security, performance, determinism, interoperability, recovery, and certification classes so that a future implementation learns both acceptance and refusal behavior.

Implementation should proceed through small explicit passes. Parse the source into stable nodes; resolve workspace and target names; infer the operational artifact type; compute effects and required capabilities; evaluate network, secret, build, deployment, package, and ledger policy; lower accepted nodes to R12; build a deterministic execution plan; and reserve MCRT emission for a modeled or native outcome with an unambiguous evidence label. Optimization may fold declarations or reuse artifacts only when the dependency, compiler, target, environment, policy, lock, and source identities match the declared equivalence profile.

## Representative corpus program

**Record:** `JAOPS-00004`  
**Feature:** `deployment_timeline`  
**Level:** `beginner`  
**Validation class:** `positive`  
**Source SHA-256:** `7f24b7ef0ae4392659e8b25d8e2cb17e7be7c2227014900a946c5f73b0b593c6`

```jaops
ja source 0.3
module corpus.ja_operations.example_00004
use Operations
policy explicit_network

workspace SuiteJAOPS_00004 {
    target windows-x64
    compiler profile release
    dependencies locked
    environment offline
    resource cpu 6 memory 8GB
    network disabled
    secret signing_key reference "vault://release/signing"
    service worker_6 replicas 1
    health_check worker_6 every 10s
    upgrade rolling
    rollback on health_failure
    package msslb
}
assert deployment.reproducible == true
emit package "SuiteJAOPS_00004.msslb"
```

## Evidence trace

- Semantic identity: `sem-e90494e6e315fb278129`
- Judgment: `Environment; Policy; {secret.read:reference_only} ⊢ node-52e3feeb532274d49870 : DeploymentArtifact ! {secret.read} ⇒ validated`
- AST node: `node-52e3feeb532274d49870` (`DeploymentDecl`)
- Declared/inferred type: `DeploymentArtifact` / `DeploymentArtifact`
- Effects: `secret.read`
- Capabilities: `secret.read:reference_only`
- Semantic operator: `scale`
- Policy decision: `allow`
- R12 record: `r12-db353b4bd2080039c479`
- MCRT record: `mcrt-c49f6d08cb654c1c9448`
- Expected validation: `pass`
- Diagnostic: `none`
- Evidence scope: modeled, not native execution

## Five-lens review

SOPHIA examines whether the declaration, effect set, capability path, recovery behavior, and evidence identities form one coherent system. CHARLOTTE examines whether the operational information architecture is legible: authors should see prerequisites, gates, risks, transitions, and remedies without reading raw runtime logs. LANDON examines parser support, scheduler feasibility, sandbox boundaries, file and process behavior, target constraints, and observability. Professor requires a stated invariant, a positive case, a minimal counterexample, and a test oracle. Podium requires release-ready navigation, provenance, checksums, evidence boundaries, and a clear certification decision.

## Engineering checklist

- Confirm stable source, AST, R12, and MCRT identities.
- Verify all effects have explicit capabilities and policy decisions.
- Verify secrets remain references and are redacted from every evidence surface.
- Verify network, storage, build, package, deployment, and ledger boundaries.
- Verify failure, retry, rollback, and terminal states are explicit.
- Verify deterministic replay inputs and cache keys are complete.
- Record unsupported behavior as a diagnostic rather than a silent approximation.

## Laboratory

**Task:** Model a staged deployment timeline with immutable promotion.

1. Copy the representative program into a separate laboratory module.
2. Write down the invariant before modifying the source.
3. Produce one accepted variant and one minimal rejected variant.
4. Predict the semantic judgment, policy decision, R12 identity change, and MCRT outcome.
5. Run the structural validator; where no native compiler exists, label all remaining results as modeled.
6. Submit source, expected diagnostics, evidence map, replay inputs, and a concise certification decision.

## Review questions

1. Which declaration carries the most important operational authority in this chapter?
2. Which hash or identity must change when the program is modified, and which identities may remain stable?
3. At what stage should the primary failure be detected?
4. Which optimization is safe, and which optimization would erase a policy or recovery obligation?
5. What native test would be required to promote the modeled outcome into execution evidence?

# Chapter 12: Upgrade Strategies and Rollback Rules

## Learning objectives

- Explain journaled transitions, health gates, and reversible state using JA Operations source, semantic, AST, R12, runtime, and MCRT layers.
- State and test the invariant that every upgrade edge has a tested rollback edge and durable checkpoint.
- Construct a positive case and a minimal case involving partial upgrades without a consistent rollback boundary.
- Separate modeled corpus evidence from native compiler or executor evidence.

## Technical foundation

This chapter treats **journaled transitions, health gates, and reversible state** as a language concern rather than an informal runbook convention. In JA Operations, declarations are compiled into a typed operational graph whose nodes carry identity, effects, capabilities, policy decisions, and recovery obligations. That graph is valuable because it makes infrastructure intent reviewable before any external process is started. The author can reason about a workspace as a bounded state machine, while the compiler can reject undeclared authority and the runtime can emit evidence tied to the same source hash.

The governing invariant is that **every upgrade edge has a tested rollback edge and durable checkpoint**. This requires more than syntactic validity. A conforming implementation must preserve the link between module identity, AST node identity, semantic judgment, R12 lowering, execution plan, and MCRT receipt. The corpus uses operator `build` for the representative record and models effects `file.write` under capabilities `package.write`. Those values are not decorative metadata: they define what can be optimized, what must be sandboxed, and what a certifier must be able to replay.

A common failure mode is **partial upgrades without a consistent rollback boundary**. The language should surface that condition at the earliest reliable stage: parsing for malformed declarations, semantic analysis for incompatible types or topology, policy analysis for unauthorized effects, plan construction for unsatisfied dependencies, and runtime validation for environmental divergence. The technical corpus includes positive, negative, boundary, integration, security, performance, determinism, interoperability, recovery, and certification classes so that a future implementation learns both acceptance and refusal behavior.

Implementation should proceed through small explicit passes. Parse the source into stable nodes; resolve workspace and target names; infer the operational artifact type; compute effects and required capabilities; evaluate network, secret, build, deployment, package, and ledger policy; lower accepted nodes to R12; build a deterministic execution plan; and reserve MCRT emission for a modeled or native outcome with an unambiguous evidence label. Optimization may fold declarations or reuse artifacts only when the dependency, compiler, target, environment, policy, lock, and source identities match the declared equivalence profile.

## Representative corpus program

**Record:** `JAOPS-00012`  
**Feature:** `upgrade_strategy`  
**Level:** `beginner`  
**Validation class:** `positive`  
**Source SHA-256:** `08d9ffb8ca60ca8f57c34e3906e453a84900a3dd35b5c98aa5b01aa1dc70f7ed`

```jaops
ja source 0.3
module corpus.ja_operations.example_00012
use Operations
policy explicit_network

workspace SuiteJAOPS_00012 {
    target windows-x64
    compiler profile release
    dependencies locked
    environment offline
    resource cpu 6 memory 16GB
    network disabled
    secret signing_key reference "vault://release/signing"
    service worker_14 replicas 1
    health_check worker_14 every 18s
    upgrade rolling
    rollback on health_failure
    package msslb
}
assert deployment.reproducible == true
emit package "SuiteJAOPS_00012.msslb"
```

## Evidence trace

- Semantic identity: `sem-0b4cf89cd8ad977aeadd`
- Judgment: `Environment; Policy; {package.write} ⊢ node-2f8617894d3d704d17ae : DeploymentArtifact ! {file.write} ⇒ validated`
- AST node: `node-2f8617894d3d704d17ae` (`DeploymentDecl`)
- Declared/inferred type: `DeploymentArtifact` / `DeploymentArtifact`
- Effects: `file.write`
- Capabilities: `package.write`
- Semantic operator: `build`
- Policy decision: `allow`
- R12 record: `r12-8ecfc11d260f453d39bd`
- MCRT record: `mcrt-572940d9e2253c1e9b1e`
- Expected validation: `pass`
- Diagnostic: `none`
- Evidence scope: modeled, not native execution

## Five-lens review

SOPHIA examines whether the declaration, effect set, capability path, recovery behavior, and evidence identities form one coherent system. CHARLOTTE examines whether the operational information architecture is legible: authors should see prerequisites, gates, risks, transitions, and remedies without reading raw runtime logs. LANDON examines parser support, scheduler feasibility, sandbox boundaries, file and process behavior, target constraints, and observability. Professor requires a stated invariant, a positive case, a minimal counterexample, and a test oracle. Podium requires release-ready navigation, provenance, checksums, evidence boundaries, and a clear certification decision.

## Engineering checklist

- Confirm stable source, AST, R12, and MCRT identities.
- Verify all effects have explicit capabilities and policy decisions.
- Verify secrets remain references and are redacted from every evidence surface.
- Verify network, storage, build, package, deployment, and ledger boundaries.
- Verify failure, retry, rollback, and terminal states are explicit.
- Verify deterministic replay inputs and cache keys are complete.
- Record unsupported behavior as a diagnostic rather than a silent approximation.

## Laboratory

**Task:** Simulate rolling, blue-green, and canary recovery paths.

1. Copy the representative program into a separate laboratory module.
2. Write down the invariant before modifying the source.
3. Produce one accepted variant and one minimal rejected variant.
4. Predict the semantic judgment, policy decision, R12 identity change, and MCRT outcome.
5. Run the structural validator; where no native compiler exists, label all remaining results as modeled.
6. Submit source, expected diagnostics, evidence map, replay inputs, and a concise certification decision.

## Review questions

1. Which declaration carries the most important operational authority in this chapter?
2. Which hash or identity must change when the program is modified, and which identities may remain stable?
3. At what stage should the primary failure be detected?
4. Which optimization is safe, and which optimization would erase a policy or recovery obligation?
5. What native test would be required to promote the modeled outcome into execution evidence?

# Chapter 13: Deployment Probes and Readiness Certification

## Learning objectives

- Explain readiness, liveness, and certification probes using JA Operations source, semantic, AST, R12, runtime, and MCRT layers.
- State and test the invariant that probe evidence is bounded, repeatable, and tied to the deployed artifact.
- Construct a positive case and a minimal case involving using a single superficial probe as certification.
- Separate modeled corpus evidence from native compiler or executor evidence.

## Technical foundation

This chapter treats **readiness, liveness, and certification probes** as a language concern rather than an informal runbook convention. In JA Operations, declarations are compiled into a typed operational graph whose nodes carry identity, effects, capabilities, policy decisions, and recovery obligations. That graph is valuable because it makes infrastructure intent reviewable before any external process is started. The author can reason about a workspace as a bounded state machine, while the compiler can reject undeclared authority and the runtime can emit evidence tied to the same source hash.

The governing invariant is that **probe evidence is bounded, repeatable, and tied to the deployed artifact**. This requires more than syntactic validity. A conforming implementation must preserve the link between module identity, AST node identity, semantic judgment, R12 lowering, execution plan, and MCRT receipt. The corpus uses operator `package` for the representative record and models effects `secret.read` under capabilities `package.write`. Those values are not decorative metadata: they define what can be optimized, what must be sandboxed, and what a certifier must be able to replay.

A common failure mode is **using a single superficial probe as certification**. The language should surface that condition at the earliest reliable stage: parsing for malformed declarations, semantic analysis for incompatible types or topology, policy analysis for unauthorized effects, plan construction for unsatisfied dependencies, and runtime validation for environmental divergence. The technical corpus includes positive, negative, boundary, integration, security, performance, determinism, interoperability, recovery, and certification classes so that a future implementation learns both acceptance and refusal behavior.

Implementation should proceed through small explicit passes. Parse the source into stable nodes; resolve workspace and target names; infer the operational artifact type; compute effects and required capabilities; evaluate network, secret, build, deployment, package, and ledger policy; lower accepted nodes to R12; build a deterministic execution plan; and reserve MCRT emission for a modeled or native outcome with an unambiguous evidence label. Optimization may fold declarations or reuse artifacts only when the dependency, compiler, target, environment, policy, lock, and source identities match the declared equivalence profile.

## Representative corpus program

**Record:** `JAOPS-00018`  
**Feature:** `deployment_probe`  
**Level:** `beginner`  
**Validation class:** `positive`  
**Source SHA-256:** `0e048abdd60f72046b62e039e8e616801cb539534021a9e23e5d654f84a3ee2b`

```jaops
ja source 0.3
module corpus.ja_operations.example_00018
use Operations
policy explicit_network

workspace SuiteJAOPS_00018 {
    target windows-x64
    compiler profile release
    dependencies locked
    environment offline
    resource cpu 4 memory 6GB
    network disabled
    secret signing_key reference "vault://release/signing"
    service worker_20 replicas 3
    health_check worker_20 every 24s
    upgrade rolling
    rollback on health_failure
    package msslb
}
assert deployment.reproducible == true
emit package "SuiteJAOPS_00018.msslb"
```

## Evidence trace

- Semantic identity: `sem-d8307322c5403e0aefe3`
- Judgment: `Environment; Policy; {package.write} ⊢ node-a2e698903bdbc4779d3b : DeploymentArtifact ! {secret.read} ⇒ validated`
- AST node: `node-a2e698903bdbc4779d3b` (`DeploymentDecl`)
- Declared/inferred type: `DeploymentArtifact` / `DeploymentArtifact`
- Effects: `secret.read`
- Capabilities: `package.write`
- Semantic operator: `package`
- Policy decision: `allow`
- R12 record: `r12-47a38950d2d633132e6e`
- MCRT record: `mcrt-44fff7721b531102f0ba`
- Expected validation: `pass`
- Diagnostic: `none`
- Evidence scope: modeled, not native execution

## Five-lens review

SOPHIA examines whether the declaration, effect set, capability path, recovery behavior, and evidence identities form one coherent system. CHARLOTTE examines whether the operational information architecture is legible: authors should see prerequisites, gates, risks, transitions, and remedies without reading raw runtime logs. LANDON examines parser support, scheduler feasibility, sandbox boundaries, file and process behavior, target constraints, and observability. Professor requires a stated invariant, a positive case, a minimal counterexample, and a test oracle. Podium requires release-ready navigation, provenance, checksums, evidence boundaries, and a clear certification decision.

## Engineering checklist

- Confirm stable source, AST, R12, and MCRT identities.
- Verify all effects have explicit capabilities and policy decisions.
- Verify secrets remain references and are redacted from every evidence surface.
- Verify network, storage, build, package, deployment, and ledger boundaries.
- Verify failure, retry, rollback, and terminal states are explicit.
- Verify deterministic replay inputs and cache keys are complete.
- Record unsupported behavior as a diagnostic rather than a silent approximation.

## Laboratory

**Task:** Build a multi-probe readiness gate and failure witness.

1. Copy the representative program into a separate laboratory module.
2. Write down the invariant before modifying the source.
3. Produce one accepted variant and one minimal rejected variant.
4. Predict the semantic judgment, policy decision, R12 identity change, and MCRT outcome.
5. Run the structural validator; where no native compiler exists, label all remaining results as modeled.
6. Submit source, expected diagnostics, evidence map, replay inputs, and a concise certification decision.

## Review questions

1. Which declaration carries the most important operational authority in this chapter?
2. Which hash or identity must change when the program is modified, and which identities may remain stable?
3. At what stage should the primary failure be detected?
4. Which optimization is safe, and which optimization would erase a policy or recovery obligation?
5. What native test would be required to promote the modeled outcome into execution evidence?

# Chapter 14: Offline and Air-Gapped Deployment

## Learning objectives

- Explain closed dependency graphs and fail-closed execution using JA Operations source, semantic, AST, R12, runtime, and MCRT layers.
- State and test the invariant that all required artifacts, schemas, keys, and policies are locally attestable.
- Construct a positive case and a minimal case involving quiet network fallback or missing offline provenance.
- Separate modeled corpus evidence from native compiler or executor evidence.

## Technical foundation

This chapter treats **closed dependency graphs and fail-closed execution** as a language concern rather than an informal runbook convention. In JA Operations, declarations are compiled into a typed operational graph whose nodes carry identity, effects, capabilities, policy decisions, and recovery obligations. That graph is valuable because it makes infrastructure intent reviewable before any external process is started. The author can reason about a workspace as a bounded state machine, while the compiler can reject undeclared authority and the runtime can emit evidence tied to the same source hash.

The governing invariant is that **all required artifacts, schemas, keys, and policies are locally attestable**. This requires more than syntactic validity. A conforming implementation must preserve the link between module identity, AST node identity, semantic judgment, R12 lowering, execution plan, and MCRT receipt. The corpus uses operator `deploy` for the representative record and models effects `network.connect` under capabilities `build.execute`. Those values are not decorative metadata: they define what can be optimized, what must be sandboxed, and what a certifier must be able to replay.

A common failure mode is **quiet network fallback or missing offline provenance**. The language should surface that condition at the earliest reliable stage: parsing for malformed declarations, semantic analysis for incompatible types or topology, policy analysis for unauthorized effects, plan construction for unsatisfied dependencies, and runtime validation for environmental divergence. The technical corpus includes positive, negative, boundary, integration, security, performance, determinism, interoperability, recovery, and certification classes so that a future implementation learns both acceptance and refusal behavior.

Implementation should proceed through small explicit passes. Parse the source into stable nodes; resolve workspace and target names; infer the operational artifact type; compute effects and required capabilities; evaluate network, secret, build, deployment, package, and ledger policy; lower accepted nodes to R12; build a deterministic execution plan; and reserve MCRT emission for a modeled or native outcome with an unambiguous evidence label. Optimization may fold declarations or reuse artifacts only when the dependency, compiler, target, environment, policy, lock, and source identities match the declared equivalence profile.

## Representative corpus program

**Record:** `JAOPS-00241`  
**Feature:** `air_gapped_deployment`  
**Level:** `beginner`  
**Validation class:** `positive`  
**Source SHA-256:** `24a50856e8648b44347cf722721dd5d8946f7b453c3500020c30a350a8f76cee`

```jaops
ja source 0.3
module corpus.ja_operations.example_00241
use Operations
policy explicit_network

workspace SuiteJAOPS_00241 {
    target windows-x64
    compiler profile release
    dependencies locked
    environment offline
    resource cpu 3 memory 5GB
    network disabled
    secret signing_key reference "vault://release/signing"
    service worker_49 replicas 2
    health_check worker_49 every 30s
    upgrade rolling
    rollback on health_failure
    package msslb
}
assert deployment.reproducible == true
emit package "SuiteJAOPS_00241.msslb"
```

## Evidence trace

- Semantic identity: `sem-cea28fb4311bc0f51960`
- Judgment: `Environment; Policy; {build.execute} ⊢ node-71334b8f91b471ce5883 : DeploymentArtifact ! {network.connect} ⇒ validated`
- AST node: `node-71334b8f91b471ce5883` (`DeploymentDecl`)
- Declared/inferred type: `DeploymentArtifact` / `DeploymentArtifact`
- Effects: `network.connect`
- Capabilities: `build.execute`
- Semantic operator: `deploy`
- Policy decision: `allow`
- R12 record: `r12-d335f1384b78af35ce1c`
- MCRT record: `mcrt-a03849627f4bbe5e36b2`
- Expected validation: `pass`
- Diagnostic: `none`
- Evidence scope: modeled, not native execution

## Five-lens review

SOPHIA examines whether the declaration, effect set, capability path, recovery behavior, and evidence identities form one coherent system. CHARLOTTE examines whether the operational information architecture is legible: authors should see prerequisites, gates, risks, transitions, and remedies without reading raw runtime logs. LANDON examines parser support, scheduler feasibility, sandbox boundaries, file and process behavior, target constraints, and observability. Professor requires a stated invariant, a positive case, a minimal counterexample, and a test oracle. Podium requires release-ready navigation, provenance, checksums, evidence boundaries, and a clear certification decision.

## Engineering checklist

- Confirm stable source, AST, R12, and MCRT identities.
- Verify all effects have explicit capabilities and policy decisions.
- Verify secrets remain references and are redacted from every evidence surface.
- Verify network, storage, build, package, deployment, and ledger boundaries.
- Verify failure, retry, rollback, and terminal states are explicit.
- Verify deterministic replay inputs and cache keys are complete.
- Record unsupported behavior as a diagnostic rather than a silent approximation.

## Laboratory

**Task:** Prepare and inspect an air-gap deployment bundle.

1. Copy the representative program into a separate laboratory module.
2. Write down the invariant before modifying the source.
3. Produce one accepted variant and one minimal rejected variant.
4. Predict the semantic judgment, policy decision, R12 identity change, and MCRT outcome.
5. Run the structural validator; where no native compiler exists, label all remaining results as modeled.
6. Submit source, expected diagnostics, evidence map, replay inputs, and a concise certification decision.

## Review questions

1. Which declaration carries the most important operational authority in this chapter?
2. Which hash or identity must change when the program is modified, and which identities may remain stable?
3. At what stage should the primary failure be detected?
4. Which optimization is safe, and which optimization would erase a policy or recovery obligation?
5. What native test would be required to promote the modeled outcome into execution evidence?

# Chapter 15: Project, Workspace, and Clean-Room Builds

## Learning objectives

- Explain hermetic construction from declared inputs using JA Operations source, semantic, AST, R12, runtime, and MCRT layers.
- State and test the invariant that a clean-room rebuild yields equivalent semantic and artifact identities within declared tolerances.
- Construct a positive case and a minimal case involving stateful build hosts and environment-dependent outputs.
- Separate modeled corpus evidence from native compiler or executor evidence.

## Technical foundation

This chapter treats **hermetic construction from declared inputs** as a language concern rather than an informal runbook convention. In JA Operations, declarations are compiled into a typed operational graph whose nodes carry identity, effects, capabilities, policy decisions, and recovery obligations. That graph is valuable because it makes infrastructure intent reviewable before any external process is started. The author can reason about a workspace as a bounded state machine, while the compiler can reject undeclared authority and the runtime can emit evidence tied to the same source hash.

The governing invariant is that **a clean-room rebuild yields equivalent semantic and artifact identities within declared tolerances**. This requires more than syntactic validity. A conforming implementation must preserve the link between module identity, AST node identity, semantic judgment, R12 lowering, execution plan, and MCRT receipt. The corpus uses operator `deploy` for the representative record and models effects `file.write` under capabilities `network.connect:declared`. Those values are not decorative metadata: they define what can be optimized, what must be sandboxed, and what a certifier must be able to replay.

A common failure mode is **stateful build hosts and environment-dependent outputs**. The language should surface that condition at the earliest reliable stage: parsing for malformed declarations, semantic analysis for incompatible types or topology, policy analysis for unauthorized effects, plan construction for unsatisfied dependencies, and runtime validation for environmental divergence. The technical corpus includes positive, negative, boundary, integration, security, performance, determinism, interoperability, recovery, and certification classes so that a future implementation learns both acceptance and refusal behavior.

Implementation should proceed through small explicit passes. Parse the source into stable nodes; resolve workspace and target names; infer the operational artifact type; compute effects and required capabilities; evaluate network, secret, build, deployment, package, and ledger policy; lower accepted nodes to R12; build a deterministic execution plan; and reserve MCRT emission for a modeled or native outcome with an unambiguous evidence label. Optimization may fold declarations or reuse artifacts only when the dependency, compiler, target, environment, policy, lock, and source identities match the declared equivalence profile.

## Representative corpus program

**Record:** `JAOPS-00201`  
**Feature:** `clean_room_build`  
**Level:** `beginner`  
**Validation class:** `positive`  
**Source SHA-256:** `5ee822933f968e8cbbbcf7f3657378e7f525e62857b703ac412404223129c5f9`

```jaops
ja source 0.3
module corpus.ja_operations.example_00201
use Operations
policy explicit_network

workspace SuiteJAOPS_00201 {
    target windows-x64
    compiler profile release
    dependencies locked
    environment offline
    resource cpu 3 memory 13GB
    network disabled
    secret signing_key reference "vault://release/signing"
    service worker_9 replicas 2
    health_check worker_9 every 21s
    upgrade rolling
    rollback on health_failure
    package msslb
}
assert deployment.reproducible == true
emit package "SuiteJAOPS_00201.msslb"
```

## Evidence trace

- Semantic identity: `sem-9e2067161937c5427364`
- Judgment: `Environment; Policy; {network.connect:declared} ⊢ node-1d5158b85f5b84e4f4f6 : DeploymentArtifact ! {file.write} ⇒ validated`
- AST node: `node-1d5158b85f5b84e4f4f6` (`DeploymentDecl`)
- Declared/inferred type: `DeploymentArtifact` / `DeploymentArtifact`
- Effects: `file.write`
- Capabilities: `network.connect:declared`
- Semantic operator: `deploy`
- Policy decision: `allow`
- R12 record: `r12-9373cb9c1beac4b35300`
- MCRT record: `mcrt-ef2fb7136d2ab03081d5`
- Expected validation: `pass`
- Diagnostic: `none`
- Evidence scope: modeled, not native execution

## Five-lens review

SOPHIA examines whether the declaration, effect set, capability path, recovery behavior, and evidence identities form one coherent system. CHARLOTTE examines whether the operational information architecture is legible: authors should see prerequisites, gates, risks, transitions, and remedies without reading raw runtime logs. LANDON examines parser support, scheduler feasibility, sandbox boundaries, file and process behavior, target constraints, and observability. Professor requires a stated invariant, a positive case, a minimal counterexample, and a test oracle. Podium requires release-ready navigation, provenance, checksums, evidence boundaries, and a clear certification decision.

## Engineering checklist

- Confirm stable source, AST, R12, and MCRT identities.
- Verify all effects have explicit capabilities and policy decisions.
- Verify secrets remain references and are redacted from every evidence surface.
- Verify network, storage, build, package, deployment, and ledger boundaries.
- Verify failure, retry, rollback, and terminal states are explicit.
- Verify deterministic replay inputs and cache keys are complete.
- Record unsupported behavior as a diagnostic rather than a silent approximation.

## Laboratory

**Task:** Compare ordinary and clean-room build receipts.

1. Copy the representative program into a separate laboratory module.
2. Write down the invariant before modifying the source.
3. Produce one accepted variant and one minimal rejected variant.
4. Predict the semantic judgment, policy decision, R12 identity change, and MCRT outcome.
5. Run the structural validator; where no native compiler exists, label all remaining results as modeled.
6. Submit source, expected diagnostics, evidence map, replay inputs, and a concise certification decision.

## Review questions

1. Which declaration carries the most important operational authority in this chapter?
2. Which hash or identity must change when the program is modified, and which identities may remain stable?
3. At what stage should the primary failure be detected?
4. Which optimization is safe, and which optimization would erase a policy or recovery obligation?
5. What native test would be required to promote the modeled outcome into execution evidence?

# Chapter 16: Artifact Repositories and MSSLB Packaging

## Learning objectives

- Explain content-addressed artifacts and governed package assembly using JA Operations source, semantic, AST, R12, runtime, and MCRT layers.
- State and test the invariant that package contents, hashes, policies, and provenance are complete before signing.
- Construct a positive case and a minimal case involving mutable repositories and unsigned provenance gaps.
- Separate modeled corpus evidence from native compiler or executor evidence.

## Technical foundation

This chapter treats **content-addressed artifacts and governed package assembly** as a language concern rather than an informal runbook convention. In JA Operations, declarations are compiled into a typed operational graph whose nodes carry identity, effects, capabilities, policy decisions, and recovery obligations. That graph is valuable because it makes infrastructure intent reviewable before any external process is started. The author can reason about a workspace as a bounded state machine, while the compiler can reject undeclared authority and the runtime can emit evidence tied to the same source hash.

The governing invariant is that **package contents, hashes, policies, and provenance are complete before signing**. This requires more than syntactic validity. A conforming implementation must preserve the link between module identity, AST node identity, semantic judgment, R12 lowering, execution plan, and MCRT receipt. The corpus uses operator `build` for the representative record and models effects `process.spawn` under capabilities `secret.read:reference_only`. Those values are not decorative metadata: they define what can be optimized, what must be sandboxed, and what a certifier must be able to replay.

A common failure mode is **mutable repositories and unsigned provenance gaps**. The language should surface that condition at the earliest reliable stage: parsing for malformed declarations, semantic analysis for incompatible types or topology, policy analysis for unauthorized effects, plan construction for unsatisfied dependencies, and runtime validation for environmental divergence. The technical corpus includes positive, negative, boundary, integration, security, performance, determinism, interoperability, recovery, and certification classes so that a future implementation learns both acceptance and refusal behavior.

Implementation should proceed through small explicit passes. Parse the source into stable nodes; resolve workspace and target names; infer the operational artifact type; compute effects and required capabilities; evaluate network, secret, build, deployment, package, and ledger policy; lower accepted nodes to R12; build a deterministic execution plan; and reserve MCRT emission for a modeled or native outcome with an unambiguous evidence label. Optimization may fold declarations or reuse artifacts only when the dependency, compiler, target, environment, policy, lock, and source identities match the declared equivalence profile.

## Representative corpus program

**Record:** `JAOPS-00022`  
**Feature:** `msslb_packaging`  
**Level:** `beginner`  
**Validation class:** `positive`  
**Source SHA-256:** `11311a1a691b4414703e74a7a2d7138ec6b92bf57b148b1eb56efdd069e819bd`

```jaops
ja source 0.3
module corpus.ja_operations.example_00022
use Operations
policy explicit_network

workspace SuiteJAOPS_00022 {
    target windows-x64
    compiler profile release
    dependencies locked
    environment offline
    resource cpu 8 memory 10GB
    network disabled
    secret signing_key reference "vault://release/signing"
    service worker_24 replicas 3
    health_check worker_24 every 28s
    upgrade rolling
    rollback on health_failure
    package msslb
}
assert deployment.reproducible == true
emit package "SuiteJAOPS_00022.msslb"
```

## Evidence trace

- Semantic identity: `sem-2c288b6be70b7617add3`
- Judgment: `Environment; Policy; {secret.read:reference_only} ⊢ node-2953ae1247eaa98b565f : DeploymentArtifact ! {process.spawn} ⇒ validated`
- AST node: `node-2953ae1247eaa98b565f` (`DeploymentDecl`)
- Declared/inferred type: `DeploymentArtifact` / `DeploymentArtifact`
- Effects: `process.spawn`
- Capabilities: `secret.read:reference_only`
- Semantic operator: `build`
- Policy decision: `allow`
- R12 record: `r12-09a0f372b040043e0f28`
- MCRT record: `mcrt-f72f28eb464e1d34808c`
- Expected validation: `pass`
- Diagnostic: `none`
- Evidence scope: modeled, not native execution

## Five-lens review

SOPHIA examines whether the declaration, effect set, capability path, recovery behavior, and evidence identities form one coherent system. CHARLOTTE examines whether the operational information architecture is legible: authors should see prerequisites, gates, risks, transitions, and remedies without reading raw runtime logs. LANDON examines parser support, scheduler feasibility, sandbox boundaries, file and process behavior, target constraints, and observability. Professor requires a stated invariant, a positive case, a minimal counterexample, and a test oracle. Podium requires release-ready navigation, provenance, checksums, evidence boundaries, and a clear certification decision.

## Engineering checklist

- Confirm stable source, AST, R12, and MCRT identities.
- Verify all effects have explicit capabilities and policy decisions.
- Verify secrets remain references and are redacted from every evidence surface.
- Verify network, storage, build, package, deployment, and ledger boundaries.
- Verify failure, retry, rollback, and terminal states are explicit.
- Verify deterministic replay inputs and cache keys are complete.
- Record unsupported behavior as a diagnostic rather than a silent approximation.

## Laboratory

**Task:** Assemble an msslb package and verify its manifest.

1. Copy the representative program into a separate laboratory module.
2. Write down the invariant before modifying the source.
3. Produce one accepted variant and one minimal rejected variant.
4. Predict the semantic judgment, policy decision, R12 identity change, and MCRT outcome.
5. Run the structural validator; where no native compiler exists, label all remaining results as modeled.
6. Submit source, expected diagnostics, evidence map, replay inputs, and a concise certification decision.

## Review questions

1. Which declaration carries the most important operational authority in this chapter?
2. Which hash or identity must change when the program is modified, and which identities may remain stable?
3. At what stage should the primary failure be detected?
4. Which optimization is safe, and which optimization would erase a policy or recovery obligation?
5. What native test would be required to promote the modeled outcome into execution evidence?

# Chapter 17: Desktop Installers and Target Deployment

## Learning objectives

- Explain installer transactions, platform checks, and uninstall/rollback behavior using JA Operations source, semantic, AST, R12, runtime, and MCRT layers.
- State and test the invariant that install, upgrade, repair, and uninstall are explicit recoverable transactions.
- Construct a positive case and a minimal case involving one-way installation and hidden prerequisite acquisition.
- Separate modeled corpus evidence from native compiler or executor evidence.

## Technical foundation

This chapter treats **installer transactions, platform checks, and uninstall/rollback behavior** as a language concern rather than an informal runbook convention. In JA Operations, declarations are compiled into a typed operational graph whose nodes carry identity, effects, capabilities, policy decisions, and recovery obligations. That graph is valuable because it makes infrastructure intent reviewable before any external process is started. The author can reason about a workspace as a bounded state machine, while the compiler can reject undeclared authority and the runtime can emit evidence tied to the same source hash.

The governing invariant is that **install, upgrade, repair, and uninstall are explicit recoverable transactions**. This requires more than syntactic validity. A conforming implementation must preserve the link between module identity, AST node identity, semantic judgment, R12 lowering, execution plan, and MCRT receipt. The corpus uses operator `package` for the representative record and models effects `process.spawn` under capabilities `ledger.append`. Those values are not decorative metadata: they define what can be optimized, what must be sandboxed, and what a certifier must be able to replay.

A common failure mode is **one-way installation and hidden prerequisite acquisition**. The language should surface that condition at the earliest reliable stage: parsing for malformed declarations, semantic analysis for incompatible types or topology, policy analysis for unauthorized effects, plan construction for unsatisfied dependencies, and runtime validation for environmental divergence. The technical corpus includes positive, negative, boundary, integration, security, performance, determinism, interoperability, recovery, and certification classes so that a future implementation learns both acceptance and refusal behavior.

Implementation should proceed through small explicit passes. Parse the source into stable nodes; resolve workspace and target names; infer the operational artifact type; compute effects and required capabilities; evaluate network, secret, build, deployment, package, and ledger policy; lower accepted nodes to R12; build a deterministic execution plan; and reserve MCRT emission for a modeled or native outcome with an unambiguous evidence label. Optimization may fold declarations or reuse artifacts only when the dependency, compiler, target, environment, policy, lock, and source identities match the declared equivalence profile.

## Representative corpus program

**Record:** `JAOPS-00008`  
**Feature:** `desktop_installer`  
**Level:** `beginner`  
**Validation class:** `positive`  
**Source SHA-256:** `f8a1b5f4f899a434ede15ccac919462d31a897b2801a101622cf5c38affa670b`

```jaops
ja source 0.3
module corpus.ja_operations.example_00008
use Operations
policy explicit_network

workspace SuiteJAOPS_00008 {
    target windows-x64
    compiler profile release
    dependencies locked
    environment offline
    resource cpu 2 memory 12GB
    network disabled
    secret signing_key reference "vault://release/signing"
    service worker_10 replicas 1
    health_check worker_10 every 14s
    upgrade rolling
    rollback on health_failure
    package msslb
}
assert deployment.reproducible == true
emit package "SuiteJAOPS_00008.msslb"
```

## Evidence trace

- Semantic identity: `sem-0f02353804a97da48b46`
- Judgment: `Environment; Policy; {ledger.append} ⊢ node-a05ad618b4c6c189425d : DeploymentArtifact ! {process.spawn} ⇒ validated`
- AST node: `node-a05ad618b4c6c189425d` (`DeploymentDecl`)
- Declared/inferred type: `DeploymentArtifact` / `DeploymentArtifact`
- Effects: `process.spawn`
- Capabilities: `ledger.append`
- Semantic operator: `package`
- Policy decision: `allow`
- R12 record: `r12-c80c0a67bba0adad9037`
- MCRT record: `mcrt-446520add8f4ef4162c9`
- Expected validation: `pass`
- Diagnostic: `none`
- Evidence scope: modeled, not native execution

## Five-lens review

SOPHIA examines whether the declaration, effect set, capability path, recovery behavior, and evidence identities form one coherent system. CHARLOTTE examines whether the operational information architecture is legible: authors should see prerequisites, gates, risks, transitions, and remedies without reading raw runtime logs. LANDON examines parser support, scheduler feasibility, sandbox boundaries, file and process behavior, target constraints, and observability. Professor requires a stated invariant, a positive case, a minimal counterexample, and a test oracle. Podium requires release-ready navigation, provenance, checksums, evidence boundaries, and a clear certification decision.

## Engineering checklist

- Confirm stable source, AST, R12, and MCRT identities.
- Verify all effects have explicit capabilities and policy decisions.
- Verify secrets remain references and are redacted from every evidence surface.
- Verify network, storage, build, package, deployment, and ledger boundaries.
- Verify failure, retry, rollback, and terminal states are explicit.
- Verify deterministic replay inputs and cache keys are complete.
- Record unsupported behavior as a diagnostic rather than a silent approximation.

## Laboratory

**Task:** Design a windows-safe installer transaction plan.

1. Copy the representative program into a separate laboratory module.
2. Write down the invariant before modifying the source.
3. Produce one accepted variant and one minimal rejected variant.
4. Predict the semantic judgment, policy decision, R12 identity change, and MCRT outcome.
5. Run the structural validator; where no native compiler exists, label all remaining results as modeled.
6. Submit source, expected diagnostics, evidence map, replay inputs, and a concise certification decision.

## Review questions

1. Which declaration carries the most important operational authority in this chapter?
2. Which hash or identity must change when the program is modified, and which identities may remain stable?
3. At what stage should the primary failure be detected?
4. Which optimization is safe, and which optimization would erase a policy or recovery obligation?
5. What native test would be required to promote the modeled outcome into execution evidence?

# Chapter 18: Compiler Frontend, Typed AST, and Diagnostics

## Learning objectives

- Explain parsing operations declarations into stable typed nodes using JA Operations source, semantic, AST, R12, runtime, and MCRT layers.
- State and test the invariant that source spans, types, effects, capabilities, and policy decisions remain inspectable.
- Construct a positive case and a minimal case involving collapsing every failure into a generic deployment error.
- Separate modeled corpus evidence from native compiler or executor evidence.

## Technical foundation

This chapter treats **parsing operations declarations into stable typed nodes** as a language concern rather than an informal runbook convention. In JA Operations, declarations are compiled into a typed operational graph whose nodes carry identity, effects, capabilities, policy decisions, and recovery obligations. That graph is valuable because it makes infrastructure intent reviewable before any external process is started. The author can reason about a workspace as a bounded state machine, while the compiler can reject undeclared authority and the runtime can emit evidence tied to the same source hash.

The governing invariant is that **source spans, types, effects, capabilities, and policy decisions remain inspectable**. This requires more than syntactic validity. A conforming implementation must preserve the link between module identity, AST node identity, semantic judgment, R12 lowering, execution plan, and MCRT receipt. The corpus uses operator `deploy` for the representative record and models effects `ledger.append` under capabilities `network.connect:declared`. Those values are not decorative metadata: they define what can be optimized, what must be sandboxed, and what a certifier must be able to replay.

A common failure mode is **collapsing every failure into a generic deployment error**. The language should surface that condition at the earliest reliable stage: parsing for malformed declarations, semantic analysis for incompatible types or topology, policy analysis for unauthorized effects, plan construction for unsatisfied dependencies, and runtime validation for environmental divergence. The technical corpus includes positive, negative, boundary, integration, security, performance, determinism, interoperability, recovery, and certification classes so that a future implementation learns both acceptance and refusal behavior.

Implementation should proceed through small explicit passes. Parse the source into stable nodes; resolve workspace and target names; infer the operational artifact type; compute effects and required capabilities; evaluate network, secret, build, deployment, package, and ledger policy; lower accepted nodes to R12; build a deterministic execution plan; and reserve MCRT emission for a modeled or native outcome with an unambiguous evidence label. Optimization may fold declarations or reuse artifacts only when the dependency, compiler, target, environment, policy, lock, and source identities match the declared equivalence profile.

## Representative corpus program

**Record:** `JAOPS-00261`  
**Feature:** `compiler_profile`  
**Level:** `beginner`  
**Validation class:** `positive`  
**Source SHA-256:** `387650ddb8ff0314d0856b293b59eeaae621cda827f4205b8ea0494bac25db6e`

```jaops
ja source 0.3
module corpus.ja_operations.example_00261
use Operations
policy explicit_network

workspace SuiteJAOPS_00261 {
    target windows-x64
    compiler profile release
    dependencies locked
    environment offline
    resource cpu 7 memory 9GB
    network disabled
    secret signing_key reference "vault://release/signing"
    service worker_69 replicas 2
    health_check worker_69 every 19s
    upgrade rolling
    rollback on health_failure
    package msslb
}
assert deployment.reproducible == true
emit package "SuiteJAOPS_00261.msslb"
```

## Evidence trace

- Semantic identity: `sem-4b1af21751f87674d494`
- Judgment: `Environment; Policy; {network.connect:declared} ⊢ node-8fca17528bf69fe64f39 : DeploymentArtifact ! {ledger.append} ⇒ validated`
- AST node: `node-8fca17528bf69fe64f39` (`DeploymentDecl`)
- Declared/inferred type: `DeploymentArtifact` / `DeploymentArtifact`
- Effects: `ledger.append`
- Capabilities: `network.connect:declared`
- Semantic operator: `deploy`
- Policy decision: `allow`
- R12 record: `r12-cd228bc09e16282c6c5f`
- MCRT record: `mcrt-40b82c389b6c08b82459`
- Expected validation: `pass`
- Diagnostic: `none`
- Evidence scope: modeled, not native execution

## Five-lens review

SOPHIA examines whether the declaration, effect set, capability path, recovery behavior, and evidence identities form one coherent system. CHARLOTTE examines whether the operational information architecture is legible: authors should see prerequisites, gates, risks, transitions, and remedies without reading raw runtime logs. LANDON examines parser support, scheduler feasibility, sandbox boundaries, file and process behavior, target constraints, and observability. Professor requires a stated invariant, a positive case, a minimal counterexample, and a test oracle. Podium requires release-ready navigation, provenance, checksums, evidence boundaries, and a clear certification decision.

## Engineering checklist

- Confirm stable source, AST, R12, and MCRT identities.
- Verify all effects have explicit capabilities and policy decisions.
- Verify secrets remain references and are redacted from every evidence surface.
- Verify network, storage, build, package, deployment, and ledger boundaries.
- Verify failure, retry, rollback, and terminal states are explicit.
- Verify deterministic replay inputs and cache keys are complete.
- Record unsupported behavior as a diagnostic rather than a silent approximation.

## Laboratory

**Task:** Specify diagnostics for syntax, policy, capability, and topology failures.

1. Copy the representative program into a separate laboratory module.
2. Write down the invariant before modifying the source.
3. Produce one accepted variant and one minimal rejected variant.
4. Predict the semantic judgment, policy decision, R12 identity change, and MCRT outcome.
5. Run the structural validator; where no native compiler exists, label all remaining results as modeled.
6. Submit source, expected diagnostics, evidence map, replay inputs, and a concise certification decision.

## Review questions

1. Which declaration carries the most important operational authority in this chapter?
2. Which hash or identity must change when the program is modified, and which identities may remain stable?
3. At what stage should the primary failure be detected?
4. Which optimization is safe, and which optimization would erase a policy or recovery obligation?
5. What native test would be required to promote the modeled outcome into execution evidence?

# Chapter 19: Runtime Executor, Scheduler, and Replay

## Learning objectives

- Explain deterministic plan execution, sandboxing, and recovery journals using JA Operations source, semantic, AST, R12, runtime, and MCRT layers.
- State and test the invariant that the same plan and inputs reproduce the same state transitions and receipt identities.
- Construct a positive case and a minimal case involving nondeterministic scheduling without traceable ordering.
- Separate modeled corpus evidence from native compiler or executor evidence.

## Technical foundation

This chapter treats **deterministic plan execution, sandboxing, and recovery journals** as a language concern rather than an informal runbook convention. In JA Operations, declarations are compiled into a typed operational graph whose nodes carry identity, effects, capabilities, policy decisions, and recovery obligations. That graph is valuable because it makes infrastructure intent reviewable before any external process is started. The author can reason about a workspace as a bounded state machine, while the compiler can reject undeclared authority and the runtime can emit evidence tied to the same source hash.

The governing invariant is that **the same plan and inputs reproduce the same state transitions and receipt identities**. This requires more than syntactic validity. A conforming implementation must preserve the link between module identity, AST node identity, semantic judgment, R12 lowering, execution plan, and MCRT receipt. The corpus uses operator `deploy` for the representative record and models effects `file.write` under capabilities `build.execute`. Those values are not decorative metadata: they define what can be optimized, what must be sandboxed, and what a certifier must be able to replay.

A common failure mode is **nondeterministic scheduling without traceable ordering**. The language should surface that condition at the earliest reliable stage: parsing for malformed declarations, semantic analysis for incompatible types or topology, policy analysis for unauthorized effects, plan construction for unsatisfied dependencies, and runtime validation for environmental divergence. The technical corpus includes positive, negative, boundary, integration, security, performance, determinism, interoperability, recovery, and certification classes so that a future implementation learns both acceptance and refusal behavior.

Implementation should proceed through small explicit passes. Parse the source into stable nodes; resolve workspace and target names; infer the operational artifact type; compute effects and required capabilities; evaluate network, secret, build, deployment, package, and ledger policy; lower accepted nodes to R12; build a deterministic execution plan; and reserve MCRT emission for a modeled or native outcome with an unambiguous evidence label. Optimization may fold declarations or reuse artifacts only when the dependency, compiler, target, environment, policy, lock, and source identities match the declared equivalence profile.

## Representative corpus program

**Record:** `JAOPS-00271`  
**Feature:** `worker`  
**Level:** `beginner`  
**Validation class:** `positive`  
**Source SHA-256:** `ff2048e4443a21c4f9974bcb1469e4d87ad4e3c6ea9410855c3a00d34d5d0871`

```jaops
ja source 0.3
module corpus.ja_operations.example_00271
use Operations
policy explicit_network

workspace SuiteJAOPS_00271 {
    target windows-x64
    compiler profile release
    dependencies locked
    environment offline
    resource cpu 9 memory 19GB
    network disabled
    secret signing_key reference "vault://release/signing"
    service worker_79 replicas 4
    health_check worker_79 every 29s
    upgrade rolling
    rollback on health_failure
    package msslb
}
assert deployment.reproducible == true
emit package "SuiteJAOPS_00271.msslb"
```

## Evidence trace

- Semantic identity: `sem-79a2809d9ebc5690c8a7`
- Judgment: `Environment; Policy; {build.execute} ⊢ node-c8abd10695aa5f120592 : DeploymentArtifact ! {file.write} ⇒ validated`
- AST node: `node-c8abd10695aa5f120592` (`DeploymentDecl`)
- Declared/inferred type: `DeploymentArtifact` / `DeploymentArtifact`
- Effects: `file.write`
- Capabilities: `build.execute`
- Semantic operator: `deploy`
- Policy decision: `allow`
- R12 record: `r12-d52a2073ac7a420a933d`
- MCRT record: `mcrt-d4d5e9d8df7cdefb3afc`
- Expected validation: `pass`
- Diagnostic: `none`
- Evidence scope: modeled, not native execution

## Five-lens review

SOPHIA examines whether the declaration, effect set, capability path, recovery behavior, and evidence identities form one coherent system. CHARLOTTE examines whether the operational information architecture is legible: authors should see prerequisites, gates, risks, transitions, and remedies without reading raw runtime logs. LANDON examines parser support, scheduler feasibility, sandbox boundaries, file and process behavior, target constraints, and observability. Professor requires a stated invariant, a positive case, a minimal counterexample, and a test oracle. Podium requires release-ready navigation, provenance, checksums, evidence boundaries, and a clear certification decision.

## Engineering checklist

- Confirm stable source, AST, R12, and MCRT identities.
- Verify all effects have explicit capabilities and policy decisions.
- Verify secrets remain references and are redacted from every evidence surface.
- Verify network, storage, build, package, deployment, and ledger boundaries.
- Verify failure, retry, rollback, and terminal states are explicit.
- Verify deterministic replay inputs and cache keys are complete.
- Record unsupported behavior as a diagnostic rather than a silent approximation.

## Laboratory

**Task:** Define a replayable executor schedule and receipt.

1. Copy the representative program into a separate laboratory module.
2. Write down the invariant before modifying the source.
3. Produce one accepted variant and one minimal rejected variant.
4. Predict the semantic judgment, policy decision, R12 identity change, and MCRT outcome.
5. Run the structural validator; where no native compiler exists, label all remaining results as modeled.
6. Submit source, expected diagnostics, evidence map, replay inputs, and a concise certification decision.

## Review questions

1. Which declaration carries the most important operational authority in this chapter?
2. Which hash or identity must change when the program is modified, and which identities may remain stable?
3. At what stage should the primary failure be detected?
4. Which optimization is safe, and which optimization would erase a policy or recovery obligation?
5. What native test would be required to promote the modeled outcome into execution evidence?

# Chapter 20: Optimization and Caching Without Semantic Drift

## Learning objectives

- Explain safe caching, parallelism, and plan simplification using JA Operations source, semantic, AST, R12, runtime, and MCRT layers.
- State and test the invariant that optimization preserves policy gates, recovery edges, artifact identity, and observable results.
- Construct a positive case and a minimal case involving cache hits across changed locks, policies, or target profiles.
- Separate modeled corpus evidence from native compiler or executor evidence.

## Technical foundation

This chapter treats **safe caching, parallelism, and plan simplification** as a language concern rather than an informal runbook convention. In JA Operations, declarations are compiled into a typed operational graph whose nodes carry identity, effects, capabilities, policy decisions, and recovery obligations. That graph is valuable because it makes infrastructure intent reviewable before any external process is started. The author can reason about a workspace as a bounded state machine, while the compiler can reject undeclared authority and the runtime can emit evidence tied to the same source hash.

The governing invariant is that **optimization preserves policy gates, recovery edges, artifact identity, and observable results**. This requires more than syntactic validity. A conforming implementation must preserve the link between module identity, AST node identity, semantic judgment, R12 lowering, execution plan, and MCRT receipt. The corpus uses operator `deploy` for the representative record and models effects `ledger.append` under capabilities `deployment.modify:approved`. Those values are not decorative metadata: they define what can be optimized, what must be sandboxed, and what a certifier must be able to replay.

A common failure mode is **cache hits across changed locks, policies, or target profiles**. The language should surface that condition at the earliest reliable stage: parsing for malformed declarations, semantic analysis for incompatible types or topology, policy analysis for unauthorized effects, plan construction for unsatisfied dependencies, and runtime validation for environmental divergence. The technical corpus includes positive, negative, boundary, integration, security, performance, determinism, interoperability, recovery, and certification classes so that a future implementation learns both acceptance and refusal behavior.

Implementation should proceed through small explicit passes. Parse the source into stable nodes; resolve workspace and target names; infer the operational artifact type; compute effects and required capabilities; evaluate network, secret, build, deployment, package, and ledger policy; lower accepted nodes to R12; build a deterministic execution plan; and reserve MCRT emission for a modeled or native outcome with an unambiguous evidence label. Optimization may fold declarations or reuse artifacts only when the dependency, compiler, target, environment, policy, lock, and source identities match the declared equivalence profile.

## Representative corpus program

**Record:** `JAOPS-00191`  
**Feature:** `reproducibility_policy`  
**Level:** `beginner`  
**Validation class:** `positive`  
**Source SHA-256:** `cc1606e8948a9d35785cd6f0c420a479bc372c18fc365f81fbd219317701fe30`

```jaops
ja source 0.3
module corpus.ja_operations.example_00191
use Operations
policy explicit_network

workspace SuiteJAOPS_00191 {
    target windows-x64
    compiler profile release
    dependencies locked
    environment offline
    resource cpu 9 memory 19GB
    network disabled
    secret signing_key reference "vault://release/signing"
    service worker_96 replicas 4
    health_check worker_96 every 11s
    upgrade rolling
    rollback on health_failure
    package msslb
}
assert deployment.reproducible == true
emit package "SuiteJAOPS_00191.msslb"
```

## Evidence trace

- Semantic identity: `sem-fab455a3da0f156f3302`
- Judgment: `Environment; Policy; {deployment.modify:approved} ⊢ node-f357c6f99adc87635843 : DeploymentArtifact ! {ledger.append} ⇒ validated`
- AST node: `node-f357c6f99adc87635843` (`DeploymentDecl`)
- Declared/inferred type: `DeploymentArtifact` / `DeploymentArtifact`
- Effects: `ledger.append`
- Capabilities: `deployment.modify:approved`
- Semantic operator: `deploy`
- Policy decision: `allow`
- R12 record: `r12-98f53dcb8015eb9a373c`
- MCRT record: `mcrt-8d09215e13ce34b6b643`
- Expected validation: `pass`
- Diagnostic: `none`
- Evidence scope: modeled, not native execution

## Five-lens review

SOPHIA examines whether the declaration, effect set, capability path, recovery behavior, and evidence identities form one coherent system. CHARLOTTE examines whether the operational information architecture is legible: authors should see prerequisites, gates, risks, transitions, and remedies without reading raw runtime logs. LANDON examines parser support, scheduler feasibility, sandbox boundaries, file and process behavior, target constraints, and observability. Professor requires a stated invariant, a positive case, a minimal counterexample, and a test oracle. Podium requires release-ready navigation, provenance, checksums, evidence boundaries, and a clear certification decision.

## Engineering checklist

- Confirm stable source, AST, R12, and MCRT identities.
- Verify all effects have explicit capabilities and policy decisions.
- Verify secrets remain references and are redacted from every evidence surface.
- Verify network, storage, build, package, deployment, and ledger boundaries.
- Verify failure, retry, rollback, and terminal states are explicit.
- Verify deterministic replay inputs and cache keys are complete.
- Record unsupported behavior as a diagnostic rather than a silent approximation.

## Laboratory

**Task:** Build cache-key and invalidation tests.

1. Copy the representative program into a separate laboratory module.
2. Write down the invariant before modifying the source.
3. Produce one accepted variant and one minimal rejected variant.
4. Predict the semantic judgment, policy decision, R12 identity change, and MCRT outcome.
5. Run the structural validator; where no native compiler exists, label all remaining results as modeled.
6. Submit source, expected diagnostics, evidence map, replay inputs, and a concise certification decision.

## Review questions

1. Which declaration carries the most important operational authority in this chapter?
2. Which hash or identity must change when the program is modified, and which identities may remain stable?
3. At what stage should the primary failure be detected?
4. Which optimization is safe, and which optimization would erase a policy or recovery obligation?
5. What native test would be required to promote the modeled outcome into execution evidence?

# Chapter 21: R12, MCRT, Certification, and Smithson 8S

## Learning objectives

- Explain provenance records, replay invariants, uncertainty, and coupling classification using JA Operations source, semantic, AST, R12, runtime, and MCRT layers.
- State and test the invariant that modeled evidence and native evidence remain distinct and every relation retains provenance.
- Construct a positive case and a minimal case involving promoting projected evidence into unsupported physical or execution claims.
- Separate modeled corpus evidence from native compiler or executor evidence.

## Technical foundation

This chapter treats **provenance records, replay invariants, uncertainty, and coupling classification** as a language concern rather than an informal runbook convention. In JA Operations, declarations are compiled into a typed operational graph whose nodes carry identity, effects, capabilities, policy decisions, and recovery obligations. That graph is valuable because it makes infrastructure intent reviewable before any external process is started. The author can reason about a workspace as a bounded state machine, while the compiler can reject undeclared authority and the runtime can emit evidence tied to the same source hash.

The governing invariant is that **modeled evidence and native evidence remain distinct and every relation retains provenance**. This requires more than syntactic validity. A conforming implementation must preserve the link between module identity, AST node identity, semantic judgment, R12 lowering, execution plan, and MCRT receipt. The corpus uses operator `deploy` for the representative record and models effects `file.read` under capabilities `network.connect:declared`. Those values are not decorative metadata: they define what can be optimized, what must be sandboxed, and what a certifier must be able to replay.

A common failure mode is **promoting projected evidence into unsupported physical or execution claims**. The language should surface that condition at the earliest reliable stage: parsing for malformed declarations, semantic analysis for incompatible types or topology, policy analysis for unauthorized effects, plan construction for unsatisfied dependencies, and runtime validation for environmental divergence. The technical corpus includes positive, negative, boundary, integration, security, performance, determinism, interoperability, recovery, and certification classes so that a future implementation learns both acceptance and refusal behavior.

Implementation should proceed through small explicit passes. Parse the source into stable nodes; resolve workspace and target names; infer the operational artifact type; compute effects and required capabilities; evaluate network, secret, build, deployment, package, and ledger policy; lower accepted nodes to R12; build a deterministic execution plan; and reserve MCRT emission for a modeled or native outcome with an unambiguous evidence label. Optimization may fold declarations or reuse artifacts only when the dependency, compiler, target, environment, policy, lock, and source identities match the declared equivalence profile.

## Representative corpus program

**Record:** `JAOPS-00231`  
**Feature:** `trace`  
**Level:** `beginner`  
**Validation class:** `positive`  
**Source SHA-256:** `ac518b60e2485087a1f5cf1a4367a3283861eefa5d8080d5db0448678545a06a`

```jaops
ja source 0.3
module corpus.ja_operations.example_00231
use Operations
policy explicit_network

workspace SuiteJAOPS_00231 {
    target windows-x64
    compiler profile release
    dependencies locked
    environment offline
    resource cpu 9 memory 11GB
    network disabled
    secret signing_key reference "vault://release/signing"
    service worker_39 replicas 4
    health_check worker_39 every 20s
    upgrade rolling
    rollback on health_failure
    package msslb
}
assert deployment.reproducible == true
emit package "SuiteJAOPS_00231.msslb"
```

## Evidence trace

- Semantic identity: `sem-290c8a799e16810ebd47`
- Judgment: `Environment; Policy; {network.connect:declared} ⊢ node-52045f900fe5300e87a6 : DeploymentArtifact ! {file.read} ⇒ validated`
- AST node: `node-52045f900fe5300e87a6` (`DeploymentDecl`)
- Declared/inferred type: `DeploymentArtifact` / `DeploymentArtifact`
- Effects: `file.read`
- Capabilities: `network.connect:declared`
- Semantic operator: `deploy`
- Policy decision: `allow`
- R12 record: `r12-7812bd27121236c6d33c`
- MCRT record: `mcrt-d151971a48a5ace45744`
- Expected validation: `pass`
- Diagnostic: `none`
- Evidence scope: modeled, not native execution

## Five-lens review

SOPHIA examines whether the declaration, effect set, capability path, recovery behavior, and evidence identities form one coherent system. CHARLOTTE examines whether the operational information architecture is legible: authors should see prerequisites, gates, risks, transitions, and remedies without reading raw runtime logs. LANDON examines parser support, scheduler feasibility, sandbox boundaries, file and process behavior, target constraints, and observability. Professor requires a stated invariant, a positive case, a minimal counterexample, and a test oracle. Podium requires release-ready navigation, provenance, checksums, evidence boundaries, and a clear certification decision.

## Engineering checklist

- Confirm stable source, AST, R12, and MCRT identities.
- Verify all effects have explicit capabilities and policy decisions.
- Verify secrets remain references and are redacted from every evidence surface.
- Verify network, storage, build, package, deployment, and ledger boundaries.
- Verify failure, retry, rollback, and terminal states are explicit.
- Verify deterministic replay inputs and cache keys are complete.
- Record unsupported behavior as a diagnostic rather than a silent approximation.

## Laboratory

**Task:** Construct a certification packet with r12, mcrt, and 8s limitations.

1. Copy the representative program into a separate laboratory module.
2. Write down the invariant before modifying the source.
3. Produce one accepted variant and one minimal rejected variant.
4. Predict the semantic judgment, policy decision, R12 identity change, and MCRT outcome.
5. Run the structural validator; where no native compiler exists, label all remaining results as modeled.
6. Submit source, expected diagnostics, evidence map, replay inputs, and a concise certification decision.

## Review questions

1. Which declaration carries the most important operational authority in this chapter?
2. Which hash or identity must change when the program is modified, and which identities may remain stable?
3. At what stage should the primary failure be detected?
4. Which optimization is safe, and which optimization would erase a policy or recovery obligation?
5. What native test would be required to promote the modeled outcome into execution evidence?

# Chapter 22: Standalone JA Operations Toolchain Capstone

## Learning objectives

- Explain integrating authoring, compilation, execution, packaging, validation, and publication using JA Operations source, semantic, AST, R12, runtime, and MCRT layers.
- State and test the invariant that the final release is navigable, reproducible, air-gap-safe, and independently auditable.
- Construct a positive case and a minimal case involving shipping source without validators, receipts, recovery tests, or evidence boundaries.
- Separate modeled corpus evidence from native compiler or executor evidence.

## Technical foundation

This chapter treats **integrating authoring, compilation, execution, packaging, validation, and publication** as a language concern rather than an informal runbook convention. In JA Operations, declarations are compiled into a typed operational graph whose nodes carry identity, effects, capabilities, policy decisions, and recovery obligations. That graph is valuable because it makes infrastructure intent reviewable before any external process is started. The author can reason about a workspace as a bounded state machine, while the compiler can reject undeclared authority and the runtime can emit evidence tied to the same source hash.

The governing invariant is that **the final release is navigable, reproducible, air-gap-safe, and independently auditable**. This requires more than syntactic validity. A conforming implementation must preserve the link between module identity, AST node identity, semantic judgment, R12 lowering, execution plan, and MCRT receipt. The corpus uses operator `deploy` for the representative record and models effects `deployment.modify` under capabilities `build.execute`. Those values are not decorative metadata: they define what can be optimized, what must be sandboxed, and what a certifier must be able to replay.

A common failure mode is **shipping source without validators, receipts, recovery tests, or evidence boundaries**. The language should surface that condition at the earliest reliable stage: parsing for malformed declarations, semantic analysis for incompatible types or topology, policy analysis for unauthorized effects, plan construction for unsatisfied dependencies, and runtime validation for environmental divergence. The technical corpus includes positive, negative, boundary, integration, security, performance, determinism, interoperability, recovery, and certification classes so that a future implementation learns both acceptance and refusal behavior.

Implementation should proceed through small explicit passes. Parse the source into stable nodes; resolve workspace and target names; infer the operational artifact type; compute effects and required capabilities; evaluate network, secret, build, deployment, package, and ledger policy; lower accepted nodes to R12; build a deterministic execution plan; and reserve MCRT emission for a modeled or native outcome with an unambiguous evidence label. Optimization may fold declarations or reuse artifacts only when the dependency, compiler, target, environment, policy, lock, and source identities match the declared equivalence profile.

## Representative corpus program

**Record:** `JAOPS-00181`  
**Feature:** `release_channel`  
**Level:** `beginner`  
**Validation class:** `positive`  
**Source SHA-256:** `945a0fc24e053437da564c84ca97c5857d3c246abee2fdd82cd25116fb457da8`

```jaops
ja source 0.3
module corpus.ja_operations.example_00181
use Operations
policy explicit_network

workspace SuiteJAOPS_00181 {
    target windows-x64
    compiler profile release
    dependencies locked
    environment offline
    resource cpu 7 memory 9GB
    network disabled
    secret signing_key reference "vault://release/signing"
    service worker_86 replicas 2
    health_check worker_86 every 32s
    upgrade rolling
    rollback on health_failure
    package msslb
}
assert deployment.reproducible == true
emit package "SuiteJAOPS_00181.msslb"
```

## Evidence trace

- Semantic identity: `sem-500575818750e3032261`
- Judgment: `Environment; Policy; {build.execute} ⊢ node-b75378921a11a506f3f9 : DeploymentArtifact ! {deployment.modify} ⇒ validated`
- AST node: `node-b75378921a11a506f3f9` (`DeploymentDecl`)
- Declared/inferred type: `DeploymentArtifact` / `DeploymentArtifact`
- Effects: `deployment.modify`
- Capabilities: `build.execute`
- Semantic operator: `deploy`
- Policy decision: `allow`
- R12 record: `r12-a3afda73bb11e6cd2190`
- MCRT record: `mcrt-7b3e62e4c444eaae41b6`
- Expected validation: `pass`
- Diagnostic: `none`
- Evidence scope: modeled, not native execution

## Five-lens review

SOPHIA examines whether the declaration, effect set, capability path, recovery behavior, and evidence identities form one coherent system. CHARLOTTE examines whether the operational information architecture is legible: authors should see prerequisites, gates, risks, transitions, and remedies without reading raw runtime logs. LANDON examines parser support, scheduler feasibility, sandbox boundaries, file and process behavior, target constraints, and observability. Professor requires a stated invariant, a positive case, a minimal counterexample, and a test oracle. Podium requires release-ready navigation, provenance, checksums, evidence boundaries, and a clear certification decision.

## Engineering checklist

- Confirm stable source, AST, R12, and MCRT identities.
- Verify all effects have explicit capabilities and policy decisions.
- Verify secrets remain references and are redacted from every evidence surface.
- Verify network, storage, build, package, deployment, and ledger boundaries.
- Verify failure, retry, rollback, and terminal states are explicit.
- Verify deterministic replay inputs and cache keys are complete.
- Record unsupported behavior as a diagnostic rather than a silent approximation.

## Laboratory

**Task:** Build and certify a small offline operations toolchain.

1. Copy the representative program into a separate laboratory module.
2. Write down the invariant before modifying the source.
3. Produce one accepted variant and one minimal rejected variant.
4. Predict the semantic judgment, policy decision, R12 identity change, and MCRT outcome.
5. Run the structural validator; where no native compiler exists, label all remaining results as modeled.
6. Submit source, expected diagnostics, evidence map, replay inputs, and a concise certification decision.

## Review questions

1. Which declaration carries the most important operational authority in this chapter?
2. Which hash or identity must change when the program is modified, and which identities may remain stable?
3. At what stage should the primary failure be detected?
4. Which optimization is safe, and which optimization would erase a policy or recovery obligation?
5. What native test would be required to promote the modeled outcome into execution evidence?

# Appendix A: Evidence Vocabulary

- **Modeled evidence:** expected result generated by the corpus specification.
- **Structural validation:** package-level checks for counts, hashes, declarations, catalogs, and balance.
- **Native compiler evidence:** parser, semantic, lowering, and artifact results produced by an implementation.
- **Native runtime evidence:** observed executor behavior, state transitions, outputs, probes, rollback, and receipts.
- **Certification evidence:** signed decision that identifies the exact artifact, policies, toolchain, tests, limitations, and reviewer authority.

# Appendix B: Recommended Capstone Evidence Packet

1. Source and lock graph
2. Compiler and target profiles
3. Policy and capability report
4. Typed AST and semantic judgment
5. R12 records
6. Deterministic execution plan
7. Probe and observability definitions
8. Upgrade and rollback journal
9. Package/installer manifest
10. MCRT receipt
11. Structural and native test reports
12. Limitations and certification decision
