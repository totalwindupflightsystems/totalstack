---
id: "@specs/aws/codeartifact/meta"
target_lang: meta
version: 1.0.0
owned-by: specwriter
status: active
---

# CodeArtifact Service — Meta Specification

## Why

AWS CodeArtifact is a fully managed artifact repository service that makes it easy for organizations to securely store, publish, and share software packages used in their development process. It supports popular package formats including npm, PyPI, Maven, NuGet, Swift, and generic packages.

## Problem Space

CodeArtifact provides a hierarchical namespace for package management:
- **Domain**: Top-level organizational boundary for repositories
- **Repository**: Stores packages and defines upstream sources
- **Package**: Named artifact (e.g., `lodash` for npm)
- **PackageVersion**: Specific version of a package

Each domain can contain multiple repositories. Repositories can have upstream connections to other repositories or external public registries. Permissions can be set at the domain and repository level.

## Architecture

The emulator implements:
- In-memory store (`CodeArtifactStore`) with dict-backed domain/repo/package storage
- Standard AWS exception classes (ResourceNotFoundException, ConflictException, etc.)
- 21 core CRUD operations across domains, repositories, packages, and tags
- Permission policy storage (domain and repository level)
- Authorization token generation (simulated)
- Tagging support (TagResource, UntagResource, ListTagsForResource)

## Design Philosophy

- **Greenfield**: CodeArtifact does not exist in LocalStack v4.14.0 — all store/exception classes are new
- **Flat store**: Dict-based storage per entity type, keyed by compound keys where needed
- **Validation-first**: Every handler validates inputs before touching the store
- **Idempotent creates**: Creating an existing resource raises ConflictException
- **Consistent error model**: Validates with standard AWS error shapes

## Success Metrics

- All 21 core operations implemented with handlers
- Integration tests cover 3+ operations with real store
- E2E tests exercise full create→describe→delete workflow
- All tests pass before marking "done"
