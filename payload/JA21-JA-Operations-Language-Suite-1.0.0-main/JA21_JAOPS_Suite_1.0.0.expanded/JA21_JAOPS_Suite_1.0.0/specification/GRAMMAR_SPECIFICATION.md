# Grammar Specification

The provisional grammar captures the common corpus surface: source identity, module, Operations import, policy, workspace, target, compiler profile, dependencies, environment, resources, bindings, services, probes, upgrade, rollback, package, assertions, and emission. A production grammar must additionally specify comments, escaping, numeric ranges, units, qualified names, annotations, recovery, and source-span behavior.

Expected-failure records must remain parseable when the intended failure is semantic or policy-related. Parser recovery must not invent authority or silently repair a dangerous network, secret, rollback, or dependency declaration.
