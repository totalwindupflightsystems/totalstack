---
id: "@specs/aws/servicecatalog/plan"
version: 1.0.0
target_lang: plan
owned-by: specwriter
status: active
depends_on:
  - "@specs/aws/servicecatalog"
---

# AWS Service Catalog — Plan (HOW)

## Operations (26 core, 90 total)

### Portfolio (5 ops)
| Operation | Type | Purpose |
|-----------|------|---------|
| CreatePortfolio | Create | Portfolio with DisplayName, ProviderName, Description |
| DescribePortfolio | Read | Get by Id |
| ListPortfolios | List | All portfolios |
| UpdatePortfolio | Update | Modify DisplayName, ProviderName, Description |
| DeletePortfolio | Delete | Remove by Id |

### Product (6 ops)
| Operation | Type | Purpose |
|-----------|------|---------|
| CreateProduct | Create | Product with Name, Owner, ProductType, Description |
| DescribeProduct | Read | Get by Id |
| SearchProducts | List | All products |
| SearchProductsAsAdmin | List | All products (admin view) |
| UpdateProduct | Update | Modify Name, Owner, Description |
| DeleteProduct | Delete | Remove by Id |

### ProvisioningArtifact (4 ops)
| Operation | Type | Purpose |
|-----------|------|---------|
| CreateProvisioningArtifact | Create | New version of a product |
| DescribeProvisioningArtifact | Read | Get by ProductId + ProvisioningArtifactId |
| ListProvisioningArtifacts | List | All artifacts for a product |
| DeleteProvisioningArtifact | Delete | Remove a version |

### Constraint (3 ops)
| Operation | Type | Purpose |
|-----------|------|---------|
| CreateConstraint | Create | Governance rule (Type: LAUNCH/NOTIFICATION/TEMPLATE/STACKSET) |
| DescribeConstraint | Read | Get by Id |
| DeleteConstraint | Delete | Remove by Id |

### Portfolio-Product Association (2 ops)
| Operation | Type | Purpose |
|-----------|------|---------|
| AssociateProductWithPortfolio | Associate | Link product to portfolio |
| DisassociateProductFromPortfolio | Disassociate | Unlink |

### ProvisionedProduct (4 ops)
| Operation | Type | Purpose |
|-----------|------|---------|
| ProvisionProduct | Create | Provision a product instance |
| DescribeProvisionedProduct | Read | Get by Id |
| UpdateProvisionedProduct | Update | Modify provisioning |
| TerminateProvisionedProduct | Delete | Deprovision |

### TagOption (2 ops)
| Operation | Type | Purpose |
|-----------|------|---------|
| CreateTagOption | Create | Admin-managed tag |
| ListTagOptions | List | All tag options |

## Error Model
- `InvalidParametersException` — validation failure (400)
- `ResourceNotFoundException` — entity not found (404)
- `ResourceInUseException` — cannot delete in-use resource (409)
- `LimitExceededException` — quota exceeded (429)
- `DuplicateResourceException` — already exists (409)
- `TagOptionNotMigratedException` — migration required

## Store Design
Single `ServiceCatalogStore` with:
- 6 entity dicts (portfolio, product, provisioning_artifact, constraint, provisioned_product, tag_option)
- 2 association dicts (portfolio_products, product_portfolios) using `defaultdict(list)`
- Auto-increment ID generation (`port-000001`, `prod-000001`, etc.)
- Per-entity serializer methods

## Test Coverage
- 30 integration tests across 7 test classes (6 entities + associations)
- 4 E2E tests (skip-until-provider-wired)
- Happy path + error path for every CRUD operation

## Deferred Operations (64 remaining)
AcceptPortfolioShare, AssociateBudgetWithResource, AssociatePrincipalWithPortfolio, 
AssociateServiceActionWithProvisioningArtifact, AssociateTagOptionWithResource,
BatchAssociateServiceActionWithProvisioningArtifact, BatchDisassociateServiceActionFromProvisioningArtifact,
CopyProduct, CreatePortfolioShare, CreateProvisionedProductPlan, CreateServiceAction,
DeletePortfolioShare, DeleteProvisionedProductPlan, DeleteServiceAction,
DescribeCopyProductStatus, DescribePortfolioShares, DescribePortfolioShareStatus,
DescribeProductAsAdmin, DescribeProvisionedProductPlan, DescribeServiceAction,
DescribeServiceActionExecutionParameters, DescribeTagOption,
DisableAWSOrganizationsAccess, DisassociateBudgetFromResource,
DisassociatePrincipalFromPortfolio, DisassociateServiceActionFromProvisioningArtifact,
DisassociateTagOptionFromResource, EnableAWSOrganizationsAccess,
ExecuteProvisionedProductPlan, ExecuteProvisionedProductServiceAction,
GetAWSOrganizationsAccessStatus, GetProvisionedProductOutputs,
ImportAsProvisionedProduct, ListAcceptedPortfolioShares,
ListBudgetsForResource, ListConstraintsForPortfolio, ListLaunchPaths,
ListOrganizationPortfolioAccess, ListPortfolioAccess,
ListPortfoliosForProduct, ListPrincipalsForPortfolio,
ListProvisionedProductPlans, ListRecordHistory,
ListResourcesForTagOption, ListServiceActions,
ListServiceActionsForProvisioningArtifact, ListStackInstancesForProvisionedProduct,
NotifyProvisionProductEngineWorkflowResult, NotifyTerminateProvisionedProductEngineWorkflowResult,
NotifyUpdateProvisionedProductEngineWorkflowResult,
RejectPortfolioShare, ScanProvisionedProducts,
SearchProvisionedProducts, SyncResource,
TerminateProvisionedProduct (already done), UpdateConstraint,
UpdateProvisionedProduct (already done), UpdateProvisioningArtifact,
UpdateProvisionedProductProperties, UpdateServiceAction,
UpdateTagOption
