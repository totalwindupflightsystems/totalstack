---
id: "@specs/aws/organizations/plan"
version: 1.0.0
target_lang: plan
owned-by: codegen
status: active
depends_on:
  - "@specs/aws/organizations"
---

# AWS Organizations — Plan Spec (HOW)

## Operations Implemented (25 core)

### Organization (4 ops)
| Operation | Description |
|-----------|-------------|
| CreateOrganization | Create a new organization |
| DescribeOrganization | Get current organization details |
| DeleteOrganization | Delete the organization (must be empty) |
| EnableAllFeatures | Upgrade to full AWS Organizations |

### Account (7 ops)
| Operation | Description |
|-----------|-------------|
| CreateAccount | Create a new member account |
| DescribeAccount | Get account details |
| CloseAccount | Close (suspend) an account |
| RemoveAccountFromOrganization | Remove account from organization |
| MoveAccount | Move account between OUs |
| ListAccounts | List all accounts |
| ListAccountsForParent | List accounts under a parent OU |

### Organizational Unit (6 ops)
| Operation | Description |
|-----------|-------------|
| CreateOrganizationalUnit | Create a new OU |
| DescribeOrganizationalUnit | Get OU details |
| UpdateOrganizationalUnit | Rename an OU |
| DeleteOrganizationalUnit | Delete empty OU |
| ListOrganizationalUnitsForParent | List OUs under a parent |
| ListRoots | List root OUs |

### Policy (8 ops)
| Operation | Description |
|-----------|-------------|
| CreatePolicy | Create a new policy |
| DescribePolicy | Get policy details + content |
| UpdatePolicy | Update policy content/description/name |
| DeletePolicy | Delete unattached policy |
| AttachPolicy | Attach policy to target |
| DetachPolicy | Detach policy from target |
| ListPolicies | List policies by type filter |
| ListPoliciesForTarget | List policies attached to target |

## Error Model

| Exception | HTTP | When |
|-----------|------|------|
| AWSOrganizationsNotInUseException | 400 | No organization exists |
| AlreadyInOrganizationException | 400 | Account already in org |
| AccountNotFoundException | 400 | Account not found |
| OrganizationalUnitNotFoundException | 400 | OU not found |
| PolicyNotFoundException | 400 | Policy not found |
| InvalidInputException | 400 | Missing/invalid required fields |
| ConstraintViolationException | 400 | Operation violates constraint |
| DuplicateOrganizationalUnitException | 400 | Duplicate OU name under parent |
| DuplicatePolicyAttachmentException | 400 | Policy already attached |
| PolicyInUseException | 400 | Policy attached to targets |
| MalformedPolicyDocumentException | 400 | Invalid JSON policy content |
| OrganizationNotEmptyException | 400 | Org still has members |

## Deferred Operations (35+ for future passes)
- Handshake operations (Accept/Cancel/Decline/Invite)
- CreateAccountStatus (async polling)
- Tag/Untag operations
- Delegated administrator management
- Service access management
- Effective policy operations
- Responsibility transfers
- GovCloud account creation
- Resource policy operations
- Child navigation (ListChildren, ListParents)
