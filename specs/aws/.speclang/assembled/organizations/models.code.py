"""AWS Organizations — store, exception classes, and data records.

Entities:
- Organization: top-level container for all accounts (max 1 per management account)
- Account: member account within the organization
- OrganizationalUnit (OU): nested container for accounts and child OUs
- Policy: service control policies (SCP), tag policies, backup policies, AI policies
"""

import time
import uuid
from collections import defaultdict

# ── Exception Classes ──────────────────────────────────────────────

class AWSOrganizationsNotInUseException(Exception):
    """The organization is not in use (no organization exists)."""
    pass


class AlreadyInOrganizationException(Exception):
    """The account is already in an organization."""
    pass


class AccountNotFoundException(Exception):
    """The specified account was not found."""
    pass


class AccountAlreadyClosedException(Exception):
    """The specified account is already closed."""
    pass


class OrganizationNotEmptyException(Exception):
    """The organization is not empty (still has member accounts)."""
    pass


class InvalidInputException(Exception):
    """The input does not satisfy the constraints specified by the AWS service."""
    pass


class ConstraintViolationException(Exception):
    """The request would violate a service constraint."""
    pass


class AccessDeniedException(Exception):
    """The caller does not have permission to perform the action."""
    pass


class ConcurrentModificationException(Exception):
    """The target of the operation is currently being modified."""
    pass


class PolicyNotFoundException(Exception):
    """The specified policy was not found."""
    pass


class PolicyTypeNotEnabledException(Exception):
    """The specified policy type isn't currently enabled in this root."""
    pass


class PolicyInUseException(Exception):
    """The policy is attached to one or more entities (must detach first)."""
    pass


class OrganizationalUnitNotFoundException(Exception):
    """The specified organizational unit (OU) was not found."""
    pass


class DuplicateOrganizationalUnitException(Exception):
    """An OU with the same name already exists under the specified parent."""
    pass


class ParentNotFoundException(Exception):
    """The specified parent root or OU was not found."""
    pass


class DuplicatePolicyAttachmentException(Exception):
    """The specified policy is already attached to the entity."""
    pass


class PolicyTypeNotAvailableForOrganizationException(Exception):
    """The policy type is not available for this organization."""
    pass


class RootNotFoundException(Exception):
    """The specified root was not found."""
    pass


class ChildNotFoundException(Exception):
    """The specified child entity was not found."""
    pass


class SourceParentNotFoundException(Exception):
    """The specified source parent was not found."""
    pass


class DestinationParentNotFoundException(Exception):
    """The specified destination parent was not found."""
    pass


class DuplicateAccountException(Exception):
    """An account with the same name already exists."""
    pass


class FinalizingOrganizationException(Exception):
    """The organization is in the process of being deleted."""
    pass


class HandshakeNotFoundException(Exception):
    """The specified handshake was not found."""
    pass


class HandshakeConstraintViolationException(Exception):
    """The handshake request violates a constraint."""
    pass


class AccountOwnerNotVerifiedException(Exception):
    """The account owner's email has not been verified."""
    pass


class CreateAccountStatusNotFoundException(Exception):
    """The specified create account request id was not found."""
    pass


class ServiceException(Exception):
    """A general service exception occurred."""
    pass


class TooManyRequestsException(Exception):
    """Too many requests were sent in a given amount of time."""
    pass


class UnsupportedAPIEndpointException(Exception):
    """The action is not supported by the endpoint."""
    pass


class MalformedPolicyDocumentException(Exception):
    """The policy document is not valid JSON or does not match the schema."""
    pass


class ResponsibilityTransferNotFoundException(Exception):
    """The specified responsibility transfer was not found."""
    pass


# ── Record Classes ─────────────────────────────────────────────────

class OrganizationRecord:
    """Represents an AWS Organization."""
    def __init__(self, id: str, arn: str, feature_set: str = "ALL",
                 master_account_id: str = "", master_account_email: str = "",
                 master_account_arn: str = "", available_policy_types: list = None):
        self.id = id
        self.arn = arn
        self.feature_set = feature_set  # ALL or CONSOLIDATED_BILLING
        self.master_account_id = master_account_id
        self.master_account_email = master_account_email
        self.master_account_arn = master_account_arn
        self.available_policy_types = available_policy_types or []

    def to_dict(self) -> dict:
        return {
            "Id": self.id,
            "Arn": self.arn,
            "FeatureSet": self.feature_set,
            "MasterAccountId": self.master_account_id,
            "MasterAccountEmail": self.master_account_email,
            "MasterAccountArn": self.master_account_arn,
            "AvailablePolicyTypes": self.available_policy_types,
        }


class AccountRecord:
    """Represents an AWS account within an organization."""
    def __init__(self, id: str, arn: str, email: str, name: str,
                 status: str = "ACTIVE", joined_method: str = "CREATED",
                 joined_timestamp: float = None):
        self.id = id
        self.arn = arn
        self.email = email
        self.name = name
        self.status = status  # ACTIVE, SUSPENDED, PENDING_CLOSURE
        self.joined_method = joined_method  # INVITED or CREATED
        self.joined_timestamp = joined_timestamp or time.time()

    def to_dict(self) -> dict:
        return {
            "Id": self.id,
            "Arn": self.arn,
            "Email": self.email,
            "Name": self.name,
            "Status": self.status,
            "JoinedMethod": self.joined_method,
            "JoinedTimestamp": self.joined_timestamp,
        }


class OrganizationalUnitRecord:
    """Represents an Organizational Unit (OU)."""
    def __init__(self, id: str, arn: str, name: str):
        self.id = id
        self.arn = arn
        self.name = name

    def to_dict(self) -> dict:
        return {"Id": self.id, "Arn": self.arn, "Name": self.name}


class PolicyRecord:
    """Represents a policy (SCP, tag policy, backup policy, AI policy)."""
    def __init__(self, id: str, arn: str, name: str, description: str,
                 type: str, content: str, aws_managed: bool = False):
        self.id = id
        self.arn = arn
        self.name = name
        self.description = description
        self.type = type  # SERVICE_CONTROL_POLICY, TAG_POLICY, BACKUP_POLICY, AIsERVICES_OPT_OUT_POLICY
        self.content = content
        self.aws_managed = aws_managed

    def to_dict(self) -> dict:
        return {
            "Id": self.id,
            "Arn": self.arn,
            "Name": self.name,
            "Description": self.description,
            "Type": self.type,
            "AwsManaged": self.aws_managed,
        }

    def to_summary_dict(self) -> dict:
        return {
            "Id": self.id,
            "Arn": self.arn,
            "Name": self.name,
            "Description": self.description,
            "Type": self.type,
            "AwsManaged": self.aws_managed,
        }


# ── Store ──────────────────────────────────────────────────────────

class OrganizationsStore:
    """In-memory store for AWS Organizations state."""

    VALID_POLICY_TYPES = {
        "SERVICE_CONTROL_POLICY",
        "TAG_POLICY",
        "BACKUP_POLICY",
        "AISERVICES_OPT_OUT_POLICY",
    }

    VALID_ACCOUNT_STATUSES = {"ACTIVE", "SUSPENDED", "PENDING_CLOSURE"}

    def __init__(self):
        # Single organization (only one allowed per management account)
        self.organization = None  # type: Optional[OrganizationRecord]

        # Account management
        self.accounts = {}  # id -> AccountRecord
        self.account_counter = 100000000000  # 12-digit account IDs

        # OU management
        self.organizational_units = {}  # id -> OrganizationalUnitRecord
        # Parent-child relationships: parent_id -> [child_ou_ids]
        self.ou_children = defaultdict(list)
        # Parent-child relationships: parent_id -> [account_ids]
        self.account_children = defaultdict(list)
        # Child -> parent mapping
        self.parent_map = {}  # child_id -> parent_id
        # Root IDs for the organization
        self.roots = []  # list of root OU IDs

        # Policy management
        self.policies = {}  # id -> PolicyRecord
        # Enabled policy types per root
        self.enabled_policy_types = defaultdict(set)  # root_id -> {policy_type, ...}
        # Policy attachments: policy_id -> [target_ids]
        self.policy_targets = defaultdict(list)  # policy_id -> [target_id, ...]
        # Reverse: target_id -> [policy_ids]
        self.target_policies = defaultdict(list)  # target_id -> [policy_id, ...]

    # ── Organization Operations ─────────────────────────────────

    def create_organization(self, feature_set: str = "ALL") -> OrganizationRecord:
        """Create a new organization. Only one allowed."""
        if self.organization is not None:
            return self.organization

        org_id = f"o-{uuid.uuid4().hex[:10]}"
        account_id = self._next_account_id()
        arn = f"arn:aws:organizations::{account_id}:organization/{org_id}"
        master_arn = f"arn:aws:organizations::{account_id}:account/{org_id}/{account_id}"

        org = OrganizationRecord(
            id=org_id,
            arn=arn,
            feature_set=feature_set,
            master_account_id=account_id,
            master_account_email="management@example.com",
            master_account_arn=master_arn,
            available_policy_types=[
                {"Type": "SERVICE_CONTROL_POLICY", "Status": "ENABLED"}
            ] if feature_set == "ALL" else [],
        )
        self.organization = org

        # Create a root OU
        root_id = f"r-{uuid.uuid4().hex[:4]}"
        root_arn = f"arn:aws:organizations::{account_id}:root/{org_id}/{root_id}"
        root_ou = OrganizationalUnitRecord(id=root_id, arn=root_arn, name="Root")
        self.organizational_units[root_id] = root_ou
        self.roots.append(root_id)

        # Put management account in the root
        if account_id not in self.accounts:
            mgmt = AccountRecord(
                id=account_id, arn=master_arn,
                email="management@example.com", name="Management Account",
                status="ACTIVE", joined_method="CREATED"
            )
            self.accounts[account_id] = mgmt
        self.account_children[root_id].append(account_id)
        self.parent_map[account_id] = root_id

        # Enable SCP if ALL features
        if feature_set == "ALL":
            self.enabled_policy_types[root_id].add("SERVICE_CONTROL_POLICY")

        return org

    def describe_organization(self) -> OrganizationRecord:
        """Describe the current organization."""
        if self.organization is None:
            raise AWSOrganizationsNotInUseException("No organization exists")
        return self.organization

    def delete_organization(self):
        """Delete the organization. All member accounts must be removed first."""
        if self.organization is None:
            raise AWSOrganizationsNotInUseException("No organization exists")
        # Check no non-management accounts exist
        master_id = self.organization.master_account_id
        non_mgmt = [aid for aid in self.accounts if aid != master_id]
        if non_mgmt:
            raise OrganizationNotEmptyException("Organization still has member accounts")
        self.organization = None

    def enable_all_features(self):
        """Enable all features (Full AWS Organizations)."""
        if self.organization is None:
            raise AWSOrganizationsNotInUseException("No organization exists")
        if self.organization.feature_set == "ALL":
            return  # Already enabled
        self.organization.feature_set = "ALL"
        for root_id in self.roots:
            self.enabled_policy_types[root_id].add("SERVICE_CONTROL_POLICY")
            self.organization.available_policy_types.append(
                {"Type": "SERVICE_CONTROL_POLICY", "Status": "ENABLED"}
            )

    # ── Account Operations ─────────────────────────────────────

    def _next_account_id(self) -> str:
        self.account_counter += 1
        return str(self.account_counter)

    def create_account(self, email: str, name: str, role_name: str = None,
                       iam_user_access_to_billing: str = "ALLOW",
                       tags: list = None) -> dict:
        """Create a new member account (asynchronous in real AWS)."""
        if self.organization is None:
            raise AWSOrganizationsNotInUseException("No organization exists")

        # Validate email format (basic)
        if '@' not in email:
            raise InvalidInputException("Invalid email address")

        # Check duplicate name
        for acc in self.accounts.values():
            if acc.name == name:
                raise DuplicateAccountException(
                    f"An account with the name '{name}' already exists"
                )

        request_id = f"car-{uuid.uuid4().hex[:17]}"
        account_id = self._next_account_id()
        arn = f"arn:aws:organizations::{account_id}:account/{self.organization.id}/{account_id}"

        account = AccountRecord(
            id=account_id, arn=arn, email=email, name=name,
            status="ACTIVE", joined_method="CREATED"
        )
        self.accounts[account_id] = account

        # Place in root
        root_id = self.roots[0]
        self.account_children[root_id].append(account_id)
        self.parent_map[account_id] = root_id

        return {
            "CreateAccountStatus": {
                "Id": request_id,
                "AccountName": name,
                "State": "SUCCEEDED",
                "AccountId": account_id,
                "RequestedTimestamp": time.time(),
                "CompletedTimestamp": time.time(),
            }
        }

    def describe_account(self, account_id: str) -> AccountRecord:
        """Describe an account."""
        if self.organization is None:
            raise AWSOrganizationsNotInUseException("No organization exists")
        if account_id not in self.accounts:
            raise AccountNotFoundException(f"Account '{account_id}' not found")
        return self.accounts[account_id]

    def remove_account_from_organization(self, account_id: str):
        """Remove an account from the organization."""
        if self.organization is None:
            raise AWSOrganizationsNotInUseException("No organization exists")
        if account_id not in self.accounts:
            raise AccountNotFoundException(f"Account '{account_id}' not found")
        if account_id == self.organization.master_account_id:
            raise ConstraintViolationException(
                "Cannot remove the management account"
            )

        # Remove from parent
        parent_id = self.parent_map.pop(account_id, None)
        if parent_id and account_id in self.account_children[parent_id]:
            self.account_children[parent_id].remove(account_id)

        del self.accounts[account_id]

    def close_account(self, account_id: str):
        """Close (delete) an account."""
        if self.organization is None:
            raise AWSOrganizationsNotInUseException("No organization exists")
        if account_id not in self.accounts:
            raise AccountNotFoundException(f"Account '{account_id}' not found")
        acc = self.accounts[account_id]
        if acc.status == "PENDING_CLOSURE":
            raise AccountAlreadyClosedException("Account is already closed")
        if account_id == self.organization.master_account_id:
            raise ConstraintViolationException("Cannot close the management account")
        acc.status = "PENDING_CLOSURE"

    def move_account(self, account_id: str, source_parent_id: str,
                     destination_parent_id: str):
        """Move an account from one parent to another."""
        if self.organization is None:
            raise AWSOrganizationsNotInUseException("No organization exists")
        if account_id not in self.accounts:
            raise AccountNotFoundException(f"Account '{account_id}' not found")

        current_parent = self.parent_map.get(account_id)
        if current_parent is None:
            raise AccountNotFoundException(f"Account '{account_id}' not found in any OU")
        if current_parent != source_parent_id:
            raise SourceParentNotFoundException(
                f"Source parent '{source_parent_id}' is not the current parent"
            )
        if destination_parent_id not in self.organizational_units:
            raise DestinationParentNotFoundException(
                f"Destination parent '{destination_parent_id}' not found"
            )

        # Remove from source
        if account_id in self.account_children[source_parent_id]:
            self.account_children[source_parent_id].remove(account_id)

        # Add to destination
        self.account_children[destination_parent_id].append(account_id)
        self.parent_map[account_id] = destination_parent_id

    def list_accounts(self, next_token: str = None, max_results: int = 20) -> dict:
        """List all accounts in the organization."""
        if self.organization is None:
            raise AWSOrganizationsNotInUseException("No organization exists")
        all_accounts = list(self.accounts.values())
        return {
            "Accounts": [a.to_dict() for a in all_accounts],
            "NextToken": None,
        }

    def list_accounts_for_parent(self, parent_id: str, next_token: str = None,
                                  max_results: int = 20) -> dict:
        """List accounts under a specific parent."""
        if self.organization is None:
            raise AWSOrganizationsNotInUseException("No organization exists")
        if parent_id not in self.organizational_units:
            raise ParentNotFoundException(f"Parent '{parent_id}' not found")

        child_accounts = self.account_children.get(parent_id, [])
        accounts = [self.accounts[aid] for aid in child_accounts if aid in self.accounts]
        return {
            "Accounts": [a.to_dict() for a in accounts],
            "NextToken": None,
        }

    # ── Organizational Unit Operations ─────────────────────────

    def create_organizational_unit(self, parent_id: str, name: str) -> OrganizationalUnitRecord:
        """Create a new OU under the specified parent."""
        if self.organization is None:
            raise AWSOrganizationsNotInUseException("No organization exists")
        if parent_id not in self.organizational_units:
            raise ParentNotFoundException(f"Parent '{parent_id}' not found")

        # Check duplicate name under same parent
        for child_id in self.ou_children.get(parent_id, []):
            if self.organizational_units[child_id].name == name:
                raise DuplicateOrganizationalUnitException(
                    f"An OU named '{name}' already exists under this parent"
                )

        ou_id = f"ou-{uuid.uuid4().hex[:11]}"
        account_id = self.organization.master_account_id
        arn = f"arn:aws:organizations::{account_id}:ou/{self.organization.id}/{ou_id}"

        ou = OrganizationalUnitRecord(id=ou_id, arn=arn, name=name)
        self.organizational_units[ou_id] = ou
        self.ou_children[parent_id].append(ou_id)
        self.parent_map[ou_id] = parent_id
        return ou

    def describe_organizational_unit(self, ou_id: str) -> OrganizationalUnitRecord:
        """Describe an OU."""
        if self.organization is None:
            raise AWSOrganizationsNotInUseException("No organization exists")
        if ou_id not in self.organizational_units:
            raise OrganizationalUnitNotFoundException(f"OU '{ou_id}' not found")
        return self.organizational_units[ou_id]

    def update_organizational_unit(self, ou_id: str, name: str = None) -> dict:
        """Update an OU name."""
        if self.organization is None:
            raise AWSOrganizationsNotInUseException("No organization exists")
        if ou_id not in self.organizational_units:
            raise OrganizationalUnitNotFoundException(f"OU '{ou_id}' not found")

        ou = self.organizational_units[ou_id]
        if name:
            # Check duplicate name under same parent
            parent_id = self.parent_map.get(ou_id)
            if parent_id:
                for child_id in self.ou_children.get(parent_id, []):
                    if child_id != ou_id and self.organizational_units[child_id].name == name:
                        raise DuplicateOrganizationalUnitException(
                            f"An OU named '{name}' already exists under this parent"
                        )
            ou.name = name
        return {"OrganizationalUnit": ou.to_dict()}

    def delete_organizational_unit(self, ou_id: str):
        """Delete an OU. Must be empty of accounts and child OUs."""
        if self.organization is None:
            raise AWSOrganizationsNotInUseException("No organization exists")
        if ou_id not in self.organizational_units:
            raise OrganizationalUnitNotFoundException(f"OU '{ou_id}' not found")

        # Check if OU has child accounts
        if self.account_children.get(ou_id):
            raise ConstraintViolationException("OU has child accounts")
        # Check if OU has child OUs
        if self.ou_children.get(ou_id):
            raise ConstraintViolationException("OU has child OUs")

        parent_id = self.parent_map.pop(ou_id, None)
        if parent_id and ou_id in self.ou_children[parent_id]:
            self.ou_children[parent_id].remove(ou_id)

        del self.organizational_units[ou_id]

    def list_organizational_units_for_parent(self, parent_id: str,
                                              next_token: str = None,
                                              max_results: int = 20) -> dict:
        """List OUs under a specific parent."""
        if self.organization is None:
            raise AWSOrganizationsNotInUseException("No organization exists")
        if parent_id not in self.organizational_units:
            raise ParentNotFoundException(f"Parent '{parent_id}' not found")

        child_ou_ids = self.ou_children.get(parent_id, [])
        ous = [self.organizational_units[oid] for oid in child_ou_ids if oid in self.organizational_units]
        return {
            "OrganizationalUnits": [ou.to_dict() for ou in ous],
            "NextToken": None,
        }

    def list_roots(self, next_token: str = None, max_results: int = 20) -> dict:
        """List all roots in the organization."""
        if self.organization is None:
            raise AWSOrganizationsNotInUseException("No organization exists")
        roots = [self.organizational_units[rid] for rid in self.roots if rid in self.organizational_units]
        result = []
        for r in roots:
            d = r.to_dict()
            policy_types = []
            for pt in self.enabled_policy_types.get(r.id, set()):
                policy_types.append({"Type": pt, "Status": "ENABLED"})
            d["PolicyTypes"] = policy_types
            result.append(d)
        return {"Roots": result, "NextToken": None}

    # ── Policy Operations ───────────────────────────────────────

    def create_policy(self, content: str, description: str, name: str, type: str,
                      tags: list = None) -> PolicyRecord:
        """Create a new policy."""
        if self.organization is None:
            raise AWSOrganizationsNotInUseException("No organization exists")
        if type not in self.VALID_POLICY_TYPES:
            raise InvalidInputException(f"Invalid policy type: {type}")

        # Verify content is valid JSON
        import json
        try:
            json.loads(content)
        except json.JSONDecodeError:
            raise MalformedPolicyDocumentException("Policy content is not valid JSON")

        # Check policy type enabled at root
        enabled_anywhere = any(type in pts for pts in self.enabled_policy_types.values())
        if not enabled_anywhere and type != "TAG_POLICY":
            raise PolicyTypeNotEnabledException(
                f"Policy type '{type}' is not enabled in any root"
            )

        # Check duplicate name
        for p in self.policies.values():
            if p.name == name and p.type == type:
                raise InvalidInputException(
                    f"A policy named '{name}' of type '{type}' already exists"
                )

        policy_id = f"p-{uuid.uuid4().hex[:8]}"
        account_id = self.organization.master_account_id
        arn = f"arn:aws:organizations::{account_id}:policy/{self.organization.id}/{type}/{policy_id}"

        policy = PolicyRecord(
            id=policy_id, arn=arn, name=name, description=description,
            type=type, content=content
        )
        self.policies[policy_id] = policy
        return policy

    def describe_policy(self, policy_id: str) -> dict:
        """Describe a policy (returns full content)."""
        if self.organization is None:
            raise AWSOrganizationsNotInUseException("No organization exists")
        if policy_id not in self.policies:
            raise PolicyNotFoundException(f"Policy '{policy_id}' not found")
        p = self.policies[policy_id]
        return {"Policy": {"PolicySummary": p.to_summary_dict(), "Content": p.content}}

    def update_policy(self, policy_id: str, content: str = None,
                      description: str = None, name: str = None) -> dict:
        """Update a policy."""
        if self.organization is None:
            raise AWSOrganizationsNotInUseException("No organization exists")
        if policy_id not in self.policies:
            raise PolicyNotFoundException(f"Policy '{policy_id}' not found")

        p = self.policies[policy_id]
        if content is not None:
            import json
            try:
                json.loads(content)
            except json.JSONDecodeError:
                raise MalformedPolicyDocumentException("Policy content is not valid JSON")
            p.content = content
        if description is not None:
            p.description = description
        if name is not None:
            p.name = name
        return {"Policy": {"PolicySummary": p.to_summary_dict(), "Content": p.content}}

    def delete_policy(self, policy_id: str):
        """Delete a policy. Must be detached from all entities first."""
        if self.organization is None:
            raise AWSOrganizationsNotInUseException("No organization exists")
        if policy_id not in self.policies:
            raise PolicyNotFoundException(f"Policy '{policy_id}' not found")
        if self.policy_targets.get(policy_id):
            raise PolicyInUseException("Policy is attached to one or more entities")
        del self.policies[policy_id]

    def attach_policy(self, policy_id: str, target_id: str):
        """Attach a policy to a target (root, OU, or account)."""
        if self.organization is None:
            raise AWSOrganizationsNotInUseException("No organization exists")
        if policy_id not in self.policies:
            raise PolicyNotFoundException(f"Policy '{policy_id}' not found")

        # Validate target exists
        target_exists = (target_id in self.organizational_units or
                        target_id in self.accounts)
        if not target_exists:
            raise InvalidInputException(f"Target '{target_id}' not found")

        # Check not already attached
        if target_id in self.policy_targets.get(policy_id, []):
            raise DuplicatePolicyAttachmentException(
                f"Policy '{policy_id}' is already attached to target '{target_id}'"
            )

        self.policy_targets[policy_id].append(target_id)
        self.target_policies[target_id].append(policy_id)

    def detach_policy(self, policy_id: str, target_id: str):
        """Detach a policy from a target."""
        if self.organization is None:
            raise AWSOrganizationsNotInUseException("No organization exists")
        if policy_id not in self.policies:
            raise PolicyNotFoundException(f"Policy '{policy_id}' not found")

        if target_id in self.policy_targets.get(policy_id, []):
            self.policy_targets[policy_id].remove(target_id)
        if policy_id in self.target_policies.get(target_id, []):
            self.target_policies[target_id].remove(policy_id)

    def list_policies(self, filter: str, next_token: str = None,
                       max_results: int = 20) -> dict:
        """List policies, optionally filtered by type."""
        if self.organization is None:
            raise AWSOrganizationsNotInUseException("No organization exists")

        filtered = []
        for p in self.policies.values():
            if filter == "SERVICE_CONTROL_POLICY" and p.type != "SERVICE_CONTROL_POLICY":
                continue
            if filter == "TAG_POLICY" and p.type != "TAG_POLICY":
                continue
            if filter == "BACKUP_POLICY" and p.type != "BACKUP_POLICY":
                continue
            if filter == "AISERVICES_OPT_OUT_POLICY" and p.type != "AISERVICES_OPT_OUT_POLICY":
                continue
            filtered.append(p.to_summary_dict())

        return {"Policies": filtered, "NextToken": None}

    def list_policies_for_target(self, target_id: str, filter: str,
                                  next_token: str = None,
                                  max_results: int = 20) -> dict:
        """List policies attached to a target."""
        if self.organization is None:
            raise AWSOrganizationsNotInUseException("No organization exists")

        target_exists = (target_id in self.organizational_units or
                        target_id in self.accounts)
        if not target_exists:
            raise InvalidInputException(f"Target '{target_id}' not found")

        attached = self.target_policies.get(target_id, [])
        policies = []
        for pid in attached:
            if pid in self.policies:
                p = self.policies[pid]
                if filter == "SERVICE_CONTROL_POLICY" and p.type != "SERVICE_CONTROL_POLICY":
                    continue
                policies.append(p.to_summary_dict())

        return {"Policies": policies, "NextToken": None}
