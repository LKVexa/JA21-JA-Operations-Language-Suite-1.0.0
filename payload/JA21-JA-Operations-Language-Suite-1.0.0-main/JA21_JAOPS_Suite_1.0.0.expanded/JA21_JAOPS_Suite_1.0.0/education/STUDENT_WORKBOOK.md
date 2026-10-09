# JA21 JA Operations Language Student Workbook

Use one section per textbook chapter. Preserve exact record IDs, source hashes, expected diagnostics, and evidence scope.

## Chapter 1: The JA Operations Language as a Full Suite

- State the invariant: source, policy, plan, artifact, and receipt remain connected.
- Describe the primary failure: treating deployment files as untyped shell fragments.
- Record the selected corpus record and source SHA-256.
- Draw source → AST → semantic judgment → R12 → execution plan → MCRT.
- Produce one accepted and one rejected variant.
- Identify required native tests and the certification boundary.

## Chapter 2: Program Anatomy, Workspaces, and Policy

- State the invariant: every executable operation belongs to a named workspace and policy context.
- Describe the primary failure: allowing declarations to inherit undeclared authority.
- Record the selected corpus record and source SHA-256.
- Draw source → AST → semantic judgment → R12 → execution plan → MCRT.
- Produce one accepted and one rejected variant.
- Identify required native tests and the certification boundary.

## Chapter 3: Targets, Compiler Profiles, and Environments

- State the invariant: target, compiler, environment, and policy hashes define a stable build identity.
- Describe the primary failure: reusing artifacts across incompatible profiles.
- Record the selected corpus record and source SHA-256.
- Draw source → AST → semantic judgment → R12 → execution plan → MCRT.
- Produce one accepted and one rejected variant.
- Identify required native tests and the certification boundary.

## Chapter 4: Dependencies, Lockfiles, and Reproducibility

- State the invariant: the lock graph and artifact repository identities are closed and replayable.
- Describe the primary failure: floating dependencies and hidden transitive downloads.
- Record the selected corpus record and source SHA-256.
- Draw source → AST → semantic judgment → R12 → execution plan → MCRT.
- Produce one accepted and one rejected variant.
- Identify required native tests and the certification boundary.

## Chapter 5: Resource and GPU Requirements

- State the invariant: resource requests are validated before scheduling and remain visible in receipts.
- Describe the primary failure: best-effort overcommit that invalidates performance evidence.
- Record the selected corpus record and source SHA-256.
- Draw source → AST → semantic judgment → R12 → execution plan → MCRT.
- Produce one accepted and one rejected variant.
- Identify required native tests and the certification boundary.

## Chapter 6: Services, Workers, and LANDON Workers

- State the invariant: replica identities and capabilities are explicit and restart-safe.
- Describe the primary failure: anonymous workers with mutable authority.
- Record the selected corpus record and source SHA-256.
- Draw source → AST → semantic judgment → R12 → execution plan → MCRT.
- Produce one accepted and one rejected variant.
- Identify required native tests and the certification boundary.

## Chapter 7: Scaling Rules and Capacity Envelopes

- State the invariant: scale transitions respect minimums, maximums, cooldowns, and evidence windows.
- Describe the primary failure: reactive oscillation and unbounded replica growth.
- Record the selected corpus record and source SHA-256.
- Draw source → AST → semantic judgment → R12 → execution plan → MCRT.
- Produce one accepted and one rejected variant.
- Identify required native tests and the certification boundary.

## Chapter 8: Health Checks, Metrics, Logging, and Traces

- State the invariant: probes are side-effect bounded and logs redact secrets while retaining trace identity.
- Describe the primary failure: health endpoints that mutate state or leak credentials.
- Record the selected corpus record and source SHA-256.
- Draw source → AST → semantic judgment → R12 → execution plan → MCRT.
- Produce one accepted and one rejected variant.
- Identify required native tests and the certification boundary.

## Chapter 9: Network and Storage Bindings

- State the invariant: every endpoint and volume has a declared authority, protocol, and lifecycle.
- Describe the primary failure: implicit egress, mutable mount semantics, and untracked external state.
- Record the selected corpus record and source SHA-256.
- Draw source → AST → semantic judgment → R12 → execution plan → MCRT.
- Produce one accepted and one rejected variant.
- Identify required native tests and the certification boundary.

## Chapter 10: Secret References and Capability Boundaries

- State the invariant: secret material never appears in source, logs, package metadata, or MCRT payloads.
- Describe the primary failure: embedding credentials or broadening capabilities during retry.
- Record the selected corpus record and source SHA-256.
- Draw source → AST → semantic judgment → R12 → execution plan → MCRT.
- Produce one accepted and one rejected variant.
- Identify required native tests and the certification boundary.

## Chapter 11: Deployment Timelines and Release Channels

- State the invariant: promotion requires evidence from the same artifact identity and declared channel.
- Describe the primary failure: rebuilding between stages or promoting by mutable tag.
- Record the selected corpus record and source SHA-256.
- Draw source → AST → semantic judgment → R12 → execution plan → MCRT.
- Produce one accepted and one rejected variant.
- Identify required native tests and the certification boundary.

## Chapter 12: Upgrade Strategies and Rollback Rules

- State the invariant: every upgrade edge has a tested rollback edge and durable checkpoint.
- Describe the primary failure: partial upgrades without a consistent rollback boundary.
- Record the selected corpus record and source SHA-256.
- Draw source → AST → semantic judgment → R12 → execution plan → MCRT.
- Produce one accepted and one rejected variant.
- Identify required native tests and the certification boundary.

## Chapter 13: Deployment Probes and Readiness Certification

- State the invariant: probe evidence is bounded, repeatable, and tied to the deployed artifact.
- Describe the primary failure: using a single superficial probe as certification.
- Record the selected corpus record and source SHA-256.
- Draw source → AST → semantic judgment → R12 → execution plan → MCRT.
- Produce one accepted and one rejected variant.
- Identify required native tests and the certification boundary.

## Chapter 14: Offline and Air-Gapped Deployment

- State the invariant: all required artifacts, schemas, keys, and policies are locally attestable.
- Describe the primary failure: quiet network fallback or missing offline provenance.
- Record the selected corpus record and source SHA-256.
- Draw source → AST → semantic judgment → R12 → execution plan → MCRT.
- Produce one accepted and one rejected variant.
- Identify required native tests and the certification boundary.

## Chapter 15: Project, Workspace, and Clean-Room Builds

- State the invariant: a clean-room rebuild yields equivalent semantic and artifact identities within declared tolerances.
- Describe the primary failure: stateful build hosts and environment-dependent outputs.
- Record the selected corpus record and source SHA-256.
- Draw source → AST → semantic judgment → R12 → execution plan → MCRT.
- Produce one accepted and one rejected variant.
- Identify required native tests and the certification boundary.

## Chapter 16: Artifact Repositories and MSSLB Packaging

- State the invariant: package contents, hashes, policies, and provenance are complete before signing.
- Describe the primary failure: mutable repositories and unsigned provenance gaps.
- Record the selected corpus record and source SHA-256.
- Draw source → AST → semantic judgment → R12 → execution plan → MCRT.
- Produce one accepted and one rejected variant.
- Identify required native tests and the certification boundary.

## Chapter 17: Desktop Installers and Target Deployment

- State the invariant: install, upgrade, repair, and uninstall are explicit recoverable transactions.
- Describe the primary failure: one-way installation and hidden prerequisite acquisition.
- Record the selected corpus record and source SHA-256.
- Draw source → AST → semantic judgment → R12 → execution plan → MCRT.
- Produce one accepted and one rejected variant.
- Identify required native tests and the certification boundary.

## Chapter 18: Compiler Frontend, Typed AST, and Diagnostics

- State the invariant: source spans, types, effects, capabilities, and policy decisions remain inspectable.
- Describe the primary failure: collapsing every failure into a generic deployment error.
- Record the selected corpus record and source SHA-256.
- Draw source → AST → semantic judgment → R12 → execution plan → MCRT.
- Produce one accepted and one rejected variant.
- Identify required native tests and the certification boundary.

## Chapter 19: Runtime Executor, Scheduler, and Replay

- State the invariant: the same plan and inputs reproduce the same state transitions and receipt identities.
- Describe the primary failure: nondeterministic scheduling without traceable ordering.
- Record the selected corpus record and source SHA-256.
- Draw source → AST → semantic judgment → R12 → execution plan → MCRT.
- Produce one accepted and one rejected variant.
- Identify required native tests and the certification boundary.

## Chapter 20: Optimization and Caching Without Semantic Drift

- State the invariant: optimization preserves policy gates, recovery edges, artifact identity, and observable results.
- Describe the primary failure: cache hits across changed locks, policies, or target profiles.
- Record the selected corpus record and source SHA-256.
- Draw source → AST → semantic judgment → R12 → execution plan → MCRT.
- Produce one accepted and one rejected variant.
- Identify required native tests and the certification boundary.

## Chapter 21: R12, MCRT, Certification, and Smithson 8S

- State the invariant: modeled evidence and native evidence remain distinct and every relation retains provenance.
- Describe the primary failure: promoting projected evidence into unsupported physical or execution claims.
- Record the selected corpus record and source SHA-256.
- Draw source → AST → semantic judgment → R12 → execution plan → MCRT.
- Produce one accepted and one rejected variant.
- Identify required native tests and the certification boundary.

## Chapter 22: Standalone JA Operations Toolchain Capstone

- State the invariant: the final release is navigable, reproducible, air-gap-safe, and independently auditable.
- Describe the primary failure: shipping source without validators, receipts, recovery tests, or evidence boundaries.
- Record the selected corpus record and source SHA-256.
- Draw source → AST → semantic judgment → R12 → execution plan → MCRT.
- Produce one accepted and one rejected variant.
- Identify required native tests and the certification boundary.
