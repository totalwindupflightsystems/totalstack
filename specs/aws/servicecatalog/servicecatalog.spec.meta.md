---
id: "@specs/aws/servicecatalog"
version: 1.0.0
target_lang: meta
owned-by: specwriter
status: active
---

# AWS Service Catalog — Meta (WHY)

## Service Overview
AWS Service Catalog allows organizations to create and manage catalogs of IT services that are approved for use on AWS. These IT services can include virtual machine images, servers, software, and databases. It enables centralized governance and compliance through portfolios, products, constraints, and provisioning.

## Architecture
Service Catalog is a **6-entity CRUD service** with association management:

- **Portfolio** — collection of products with shared constraints and access controls
- **Product** — an IT service (CloudFormation template, Terraform config, etc.)
- **ProvisioningArtifact** — a specific version of a product
- **Constraint** — governance rule on product provisioning (LAUNCH, NOTIFICATION, TEMPLATE, STACKSET)
- **ProvisionedProduct** — a running instance of a product provisioned by an end user
- **TagOption** — key-value metadata tag managed by administrators

## Design Philosophy
- **Store-driven**: All state lives in `ServiceCatalogStore` — a dict-backed in-memory store with 6 entity collections
- **Handler-per-operation**: One `.code.py` file per operation, minimal logic in handlers (validation → store delegation → response wrapping)
- **Validation at handler level**: Required field checking with `InvalidParametersException`
- **Error model**: ResourceNotFoundException (404), InvalidParametersException (400), DuplicateResourceException (409), LimitExceededException (429)

## Entity Relationships
```
Portfolio ──(AssociateProductWithPortfolio)── Product
Portfolio ──(CreateConstraint)── Constraint (PortfolioId)
Product ──(CreateProvisioningArtifact)── ProvisioningArtifact
Product ──(ProvisionProduct)── ProvisionedProduct
```

## Success Metrics
- [x] 26 core CRUD operations implemented
- [x] 30/30 integration tests passing
- [x] 4 E2E tests written (awaiting provider wiring)
- [x] 7 exception classes
- [x] 6 entity data classes
