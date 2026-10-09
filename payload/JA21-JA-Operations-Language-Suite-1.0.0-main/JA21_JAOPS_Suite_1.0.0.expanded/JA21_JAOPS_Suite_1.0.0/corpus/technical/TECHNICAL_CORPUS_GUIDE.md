# JA21 JA Operations Technical Corpus Guide

## Scope

This corpus contains **10,000 normalized JA Operations Language records**. Each record preserves the source program, semantic interpretation, typed AST, compiler representation, R12 lowering, modeled runtime representation, MCRT record, validation expectation, optimization notes, and Smithson 8S annotation supplied by the uploaded source.

## Evidence boundary

The records model expected compiler and runtime behavior. They do not constitute proof that a native JA Operations parser, compiler, deployment executor, installer, package host, or R12/MCRT runtime executed the program. Native results must be recorded separately and must never overwrite modeled evidence.

## Corpus organization

- `JA21_JAOPS_TECHNICAL_CORPUS_10000.jsonl.gz` — master normalized corpus
- `shards/` — twenty 500-record shards
- `CORPUS_INDEX.csv` — compact search and audit index
- `DOCUMENT_COUPLING_MECHANICS.json` — document-level 8S annotation
- `../schema/JA21_JAOPS_NORMALIZED_SCHEMA.json` — normalized record schema

## Record navigation

Start with `record_id`, `feature`, `level`, and `validation_class`. Follow `source_sha256` into the AST origin hash, then inspect the semantic judgment, policy decision, R12 record, runtime expectation, and MCRT identity. Use the script catalog to locate the selected teaching program when the record belongs to the 1,000-script pack.

## Publication principles

1. Preserve exact source text and source hashes.
2. Keep expected failures; they define the language boundary.
3. Separate modeled evidence from native execution evidence.
4. Preserve capability, secret, network, rollback, and reproducibility gates during optimization.
5. Treat offline and air-gapped operation as explicit profiles, not marketing labels.
6. Keep projected and latent 8S evidence separate and retain uncertainty.
