"""Integration test for AWS Organizations — real store."""
import importlib.util
import os
import types

import pytest

ASSEMBLED_DIR = os.path.dirname(__file__)
SERVICE_DIR = os.path.join(ASSEMBLED_DIR, '..', 'organizations')

# ── Load models module ────────────────────────────────────────────
models_spec = importlib.util.spec_from_file_location(
    'models', os.path.join(SERVICE_DIR, 'models.code.py'))
models_mod = importlib.util.module_from_spec(models_spec)
models_spec.loader.exec_module(models_mod)

OrganizationsStore = models_mod.OrganizationsStore
OrganizationRecord = models_mod.OrganizationRecord
AccountRecord = models_mod.AccountRecord
OrganizationalUnitRecord = models_mod.OrganizationalUnitRecord
PolicyRecord = models_mod.PolicyRecord

# Exception classes
AWSOrganizationsNotInUseException = models_mod.AWSOrganizationsNotInUseException
AlreadyInOrganizationException = models_mod.AlreadyInOrganizationException
AccountNotFoundException = models_mod.AccountNotFoundException
AccountAlreadyClosedException = models_mod.AccountAlreadyClosedException
OrganizationNotEmptyException = models_mod.OrganizationNotEmptyException
InvalidInputException = models_mod.InvalidInputException
ConstraintViolationException = models_mod.ConstraintViolationException
AccessDeniedException = models_mod.AccessDeniedException
ConcurrentModificationException = models_mod.ConcurrentModificationException
PolicyNotFoundException = models_mod.PolicyNotFoundException
PolicyTypeNotEnabledException = models_mod.PolicyTypeNotEnabledException
PolicyInUseException = models_mod.PolicyInUseException
OrganizationalUnitNotFoundException = models_mod.OrganizationalUnitNotFoundException
DuplicateOrganizationalUnitException = models_mod.DuplicateOrganizationalUnitException
ParentNotFoundException = models_mod.ParentNotFoundException
DuplicatePolicyAttachmentException = models_mod.DuplicatePolicyAttachmentException
PolicyTypeNotAvailableForOrganizationException = models_mod.PolicyTypeNotAvailableForOrganizationException
RootNotFoundException = models_mod.RootNotFoundException
SourceParentNotFoundException = models_mod.SourceParentNotFoundException
DestinationParentNotFoundException = models_mod.DestinationParentNotFoundException
DuplicateAccountException = models_mod.DuplicateAccountException
MalformedPolicyDocumentException = models_mod.MalformedPolicyDocumentException
FinalizingOrganizationException = models_mod.FinalizingOrganizationException

# ── Module loaders ────────────────────────────────────────────────
import time as _time
import uuid as _uuid

skip_names = {'dataclass', 'time', 'uuid', '<lambda>'}

def _load_handler(op_name, globals_inject=None):
    path = os.path.join(SERVICE_DIR, op_name + '.code.py')
    spec = importlib.util.spec_from_file_location(op_name, path)
    mod = importlib.util.module_from_spec(spec)
    # Inject exception classes
    mod.InvalidInputException = InvalidInputException
    mod.AWSOrganizationsNotInUseException = AWSOrganizationsNotInUseException
    mod.AlreadyInOrganizationException = AlreadyInOrganizationException
    mod.AccountNotFoundException = AccountNotFoundException
    mod.AccountAlreadyClosedException = AccountAlreadyClosedException
    mod.OrganizationNotEmptyException = OrganizationNotEmptyException
    mod.ConstraintViolationException = ConstraintViolationException
    mod.AccessDeniedException = AccessDeniedException
    mod.ConcurrentModificationException = ConcurrentModificationException
    mod.PolicyNotFoundException = PolicyNotFoundException
    mod.PolicyTypeNotEnabledException = PolicyTypeNotEnabledException
    mod.PolicyInUseException = PolicyInUseException
    mod.OrganizationalUnitNotFoundException = OrganizationalUnitNotFoundException
    mod.DuplicateOrganizationalUnitException = DuplicateOrganizationalUnitException
    mod.ParentNotFoundException = ParentNotFoundException
    mod.DuplicatePolicyAttachmentException = DuplicatePolicyAttachmentException
    mod.PolicyTypeNotAvailableForOrganizationException = PolicyTypeNotAvailableForOrganizationException
    mod.RootNotFoundException = RootNotFoundException
    mod.SourceParentNotFoundException = SourceParentNotFoundException
    mod.DestinationParentNotFoundException = DestinationParentNotFoundException
    mod.DuplicateAccountException = DuplicateAccountException
    mod.MalformedPolicyDocumentException = MalformedPolicyDocumentException
    mod.FinalizingOrganizationException = FinalizingOrganizationException
    # Record classes
    mod.OrganizationRecord = OrganizationRecord
    mod.AccountRecord = AccountRecord
    mod.OrganizationalUnitRecord = OrganizationalUnitRecord
    mod.PolicyRecord = PolicyRecord
    # Stdlib injections
    mod.time = _time
    mod.uuid = _uuid
    mod.dataclass = lambda f: f
    if globals_inject:
        for name, value in globals_inject.items():
            setattr(mod, name, value)
    spec.loader.exec_module(mod)
    handler = None
    for v in mod.__dict__.values():
        if (isinstance(v, types.FunctionType)
                and not v.__name__.startswith('_')
                and v.__name__ not in skip_names):
            handler = v
            break
    return handler


# ── Organization Tests ────────────────────────────────────────────

class TestOrganization:
    @pytest.fixture
    def store(self):
        return OrganizationsStore()

    def test_create_organization(self, store):
        handler = _load_handler('CreateOrganization')
        response = handler(store, {"FeatureSet": "ALL"})
        assert response["Organization"]["FeatureSet"] == "ALL"
        assert response["Organization"]["Id"].startswith("o-")
        assert len(store.roots) == 1

    def test_create_consolidated_billing(self, store):
        handler = _load_handler('CreateOrganization')
        response = handler(store, {"FeatureSet": "CONSOLIDATED_BILLING"})
        assert response["Organization"]["FeatureSet"] == "CONSOLIDATED_BILLING"

    def test_create_duplicate_fails(self, store):
        handler = _load_handler('CreateOrganization')
        handler(store, {"FeatureSet": "ALL"})
        with pytest.raises(AlreadyInOrganizationException):
            handler(store, {"FeatureSet": "ALL"})

    def test_describe_organization(self, store):
        create = _load_handler('CreateOrganization')
        create(store, {"FeatureSet": "ALL"})

        handler = _load_handler('DescribeOrganization')
        response = handler(store, {})
        assert response["Organization"]["FeatureSet"] == "ALL"

    def test_describe_no_org(self, store):
        handler = _load_handler('DescribeOrganization')
        with pytest.raises(AWSOrganizationsNotInUseException):
            handler(store, {})

    def test_delete_organization(self, store):
        create = _load_handler('CreateOrganization')
        create(store, {"FeatureSet": "ALL"})

        handler = _load_handler('DeleteOrganization')
        handler(store, {})
        assert store.organization is None

    def test_delete_org_with_members_fails(self, store):
        create = _load_handler('CreateOrganization')
        create(store, {"FeatureSet": "ALL"})

        # Add a member account
        create_acct = _load_handler('CreateAccount')
        create_acct(store, {"Email": "member@test.com", "AccountName": "TestMember"})

        handler = _load_handler('DeleteOrganization')
        with pytest.raises(OrganizationNotEmptyException):
            handler(store, {})

    def test_enable_all_features(self, store):
        create = _load_handler('CreateOrganization')
        create(store, {"FeatureSet": "CONSOLIDATED_BILLING"})

        handler = _load_handler('EnableAllFeatures')
        handler(store, {})
        assert store.organization.feature_set == "ALL"


# ── Account Tests ─────────────────────────────────────────────────

class TestAccount:
    @pytest.fixture
    def org_store(self):
        """Store with an organization already created."""
        store = OrganizationsStore()
        store.create_organization(feature_set="ALL")
        return store

    def test_create_account(self, org_store):
        handler = _load_handler('CreateAccount')
        response = handler(org_store, {"Email": "test@example.com", "AccountName": "TestAccount"})
        assert response["CreateAccountStatus"]["AccountId"] is not None
        assert response["CreateAccountStatus"]["State"] == "SUCCEEDED"

    def test_create_account_missing_email(self, org_store):
        handler = _load_handler('CreateAccount')
        with pytest.raises(InvalidInputException):
            handler(org_store, {"AccountName": "TestAccount"})

    def test_create_account_invalid_email(self, org_store):
        handler = _load_handler('CreateAccount')
        with pytest.raises(InvalidInputException):
            handler(org_store, {"Email": "not-an-email", "AccountName": "TestAccount"})

    def test_create_duplicate_name_fails(self, org_store):
        handler = _load_handler('CreateAccount')
        handler(org_store, {"Email": "test1@example.com", "AccountName": "TestAccount"})
        with pytest.raises(DuplicateAccountException):
            handler(org_store, {"Email": "test2@example.com", "AccountName": "TestAccount"})

    def test_describe_account(self, org_store):
        create = _load_handler('CreateAccount')
        result = create(org_store, {"Email": "test@example.com", "AccountName": "TestAccount"})
        aid = result["CreateAccountStatus"]["AccountId"]

        handler = _load_handler('DescribeAccount')
        response = handler(org_store, {"AccountId": aid})
        assert response["Account"]["Id"] == aid
        assert response["Account"]["Email"] == "test@example.com"

    def test_describe_nonexistent_account(self, org_store):
        handler = _load_handler('DescribeAccount')
        with pytest.raises(AccountNotFoundException):
            handler(org_store, {"AccountId": "999999999999"})

    def test_list_accounts(self, org_store):
        create = _load_handler('CreateAccount')
        create(org_store, {"Email": "a@test.com", "AccountName": "AccountA"})
        create(org_store, {"Email": "b@test.com", "AccountName": "AccountB"})

        handler = _load_handler('ListAccounts')
        response = handler(org_store, {})
        # At least 3 accounts: management + 2 created
        assert len(response["Accounts"]) >= 3

    def test_list_accounts_for_parent(self, org_store):
        root_id = org_store.roots[0]
        handler = _load_handler('ListAccountsForParent')
        response = handler(org_store, {"ParentId": root_id})
        # Management account should be in root
        assert len(response["Accounts"]) >= 1

    def test_move_account(self, org_store):
        create = _load_handler('CreateAccount')
        result = create(org_store, {"Email": "move@test.com", "AccountName": "MoveAccount"})
        aid = result["CreateAccountStatus"]["AccountId"]

        root_id = org_store.roots[0]
        # Create target OU
        create_ou = _load_handler('CreateOrganizationalUnit')
        ou_result = create_ou(org_store, {"ParentId": root_id, "Name": "TargetOU"})
        ou_id = ou_result["OrganizationalUnit"]["Id"]

        handler = _load_handler('MoveAccount')
        handler(org_store, {
            "AccountId": aid,
            "SourceParentId": root_id,
            "DestinationParentId": ou_id,
        })
        assert org_store.parent_map[aid] == ou_id

    def test_close_account(self, org_store):
        create = _load_handler('CreateAccount')
        result = create(org_store, {"Email": "close@test.com", "AccountName": "CloseAccount"})
        aid = result["CreateAccountStatus"]["AccountId"]

        handler = _load_handler('CloseAccount')
        handler(org_store, {"AccountId": aid})
        assert org_store.accounts[aid].status == "PENDING_CLOSURE"

    def test_close_already_closed_fails(self, org_store):
        create = _load_handler('CreateAccount')
        result = create(org_store, {"Email": "close@test.com", "AccountName": "CloseAccount"})
        aid = result["CreateAccountStatus"]["AccountId"]

        handler = _load_handler('CloseAccount')
        handler(org_store, {"AccountId": aid})
        with pytest.raises(AccountAlreadyClosedException):
            handler(org_store, {"AccountId": aid})

    def test_remove_account(self, org_store):
        create = _load_handler('CreateAccount')
        result = create(org_store, {"Email": "remove@test.com", "AccountName": "RemoveAccount"})
        aid = result["CreateAccountStatus"]["AccountId"]

        handler = _load_handler('RemoveAccountFromOrganization')
        handler(org_store, {"AccountId": aid})
        assert aid not in org_store.accounts

    def test_cannot_remove_management_account(self, org_store):
        handler = _load_handler('RemoveAccountFromOrganization')
        with pytest.raises(ConstraintViolationException):
            handler(org_store, {"AccountId": org_store.organization.master_account_id})


# ── OU Tests ──────────────────────────────────────────────────────

class TestOrganizationalUnit:
    @pytest.fixture
    def org_store(self):
        store = OrganizationsStore()
        store.create_organization(feature_set="ALL")
        return store

    def test_create_ou(self, org_store):
        root_id = org_store.roots[0]
        handler = _load_handler('CreateOrganizationalUnit')
        response = handler(org_store, {"ParentId": root_id, "Name": "Engineering"})
        assert response["OrganizationalUnit"]["Name"] == "Engineering"
        assert response["OrganizationalUnit"]["Id"].startswith("ou-")

    def test_create_ou_missing_name(self, org_store):
        handler = _load_handler('CreateOrganizationalUnit')
        with pytest.raises(InvalidInputException):
            handler(org_store, {"ParentId": org_store.roots[0]})

    def test_create_duplicate_name_fails(self, org_store):
        root_id = org_store.roots[0]
        handler = _load_handler('CreateOrganizationalUnit')
        handler(org_store, {"ParentId": root_id, "Name": "Engineering"})
        with pytest.raises(DuplicateOrganizationalUnitException):
            handler(org_store, {"ParentId": root_id, "Name": "Engineering"})

    def test_describe_ou(self, org_store):
        root_id = org_store.roots[0]
        create = _load_handler('CreateOrganizationalUnit')
        result = create(org_store, {"ParentId": root_id, "Name": "Engineering"})
        ou_id = result["OrganizationalUnit"]["Id"]

        handler = _load_handler('DescribeOrganizationalUnit')
        response = handler(org_store, {"OrganizationalUnitId": ou_id})
        assert response["OrganizationalUnit"]["Id"] == ou_id

    def test_describe_nonexistent_ou(self, org_store):
        handler = _load_handler('DescribeOrganizationalUnit')
        with pytest.raises(OrganizationalUnitNotFoundException):
            handler(org_store, {"OrganizationalUnitId": "ou-nonexistent"})

    def test_update_ou(self, org_store):
        root_id = org_store.roots[0]
        create = _load_handler('CreateOrganizationalUnit')
        result = create(org_store, {"ParentId": root_id, "Name": "Engineering"})
        ou_id = result["OrganizationalUnit"]["Id"]

        handler = _load_handler('UpdateOrganizationalUnit')
        response = handler(org_store, {"OrganizationalUnitId": ou_id, "Name": "Platform"})
        assert response["OrganizationalUnit"]["Name"] == "Platform"

    def test_delete_empty_ou(self, org_store):
        root_id = org_store.roots[0]
        create = _load_handler('CreateOrganizationalUnit')
        result = create(org_store, {"ParentId": root_id, "Name": "Empty"})
        ou_id = result["OrganizationalUnit"]["Id"]

        handler = _load_handler('DeleteOrganizationalUnit')
        handler(org_store, {"OrganizationalUnitId": ou_id})
        assert ou_id not in org_store.organizational_units

    def test_delete_ou_with_children_fails(self, org_store):
        root_id = org_store.roots[0]
        create = _load_handler('CreateOrganizationalUnit')
        result = create(org_store, {"ParentId": root_id, "Name": "Parent"})
        ou_id = result["OrganizationalUnit"]["Id"]

        # Add child account
        create_acct = _load_handler('CreateAccount')
        acct_result = create_acct(org_store, {"Email": "child@test.com", "AccountName": "ChildAcct"})
        aid = acct_result["CreateAccountStatus"]["AccountId"]
        # Move account into OU
        move = _load_handler('MoveAccount')
        move(org_store, {"AccountId": aid, "SourceParentId": root_id, "DestinationParentId": ou_id})

        handler = _load_handler('DeleteOrganizationalUnit')
        with pytest.raises(ConstraintViolationException):
            handler(org_store, {"OrganizationalUnitId": ou_id})

    def test_list_ous_for_parent(self, org_store):
        root_id = org_store.roots[0]
        create = _load_handler('CreateOrganizationalUnit')
        create(org_store, {"ParentId": root_id, "Name": "Dev"})
        create(org_store, {"ParentId": root_id, "Name": "Ops"})

        handler = _load_handler('ListOrganizationalUnitsForParent')
        response = handler(org_store, {"ParentId": root_id})
        assert len(response["OrganizationalUnits"]) == 2

    def test_list_roots(self, org_store):
        handler = _load_handler('ListRoots')
        response = handler(org_store, {})
        assert len(response["Roots"]) == 1
        assert "PolicyTypes" in response["Roots"][0]


# ── Policy Tests ──────────────────────────────────────────────────

SCP_CONTENT = '{"Version":"2012-10-17","Statement":[{"Effect":"Deny","Action":"*","Resource":"*"}]}'

class TestPolicy:
    @pytest.fixture
    def org_store(self):
        store = OrganizationsStore()
        store.create_organization(feature_set="ALL")
        return store

    def test_create_policy(self, org_store):
        handler = _load_handler('CreatePolicy')
        response = handler(org_store, {
            "Content": SCP_CONTENT,
            "Description": "Deny all policy",
            "Name": "DenyAll",
            "Type": "SERVICE_CONTROL_POLICY",
        })
        assert response["Policy"]["Name"] == "DenyAll"
        assert response["Policy"]["Id"].startswith("p-")

    def test_create_policy_invalid_json(self, org_store):
        handler = _load_handler('CreatePolicy')
        with pytest.raises(MalformedPolicyDocumentException):
            handler(org_store, {
                "Content": "not json",
                "Description": "Bad policy",
                "Name": "BadPolicy",
                "Type": "SERVICE_CONTROL_POLICY",
            })

    def test_describe_policy(self, org_store):
        create = _load_handler('CreatePolicy')
        result = create(org_store, {
            "Content": SCP_CONTENT,
            "Description": "Test policy",
            "Name": "TestPolicy",
            "Type": "SERVICE_CONTROL_POLICY",
        })
        pid = result["Policy"]["Id"]

        handler = _load_handler('DescribePolicy')
        response = handler(org_store, {"PolicyId": pid})
        assert response["Policy"]["Id"] == pid
        assert "Content" in response["Policy"]

    def test_describe_nonexistent_policy(self, org_store):
        handler = _load_handler('DescribePolicy')
        with pytest.raises(PolicyNotFoundException):
            handler(org_store, {"PolicyId": "p-nonexistent"})

    def test_update_policy(self, org_store):
        create = _load_handler('CreatePolicy')
        result = create(org_store, {
            "Content": SCP_CONTENT,
            "Description": "Original description",
            "Name": "UpdateMe",
            "Type": "SERVICE_CONTROL_POLICY",
        })
        pid = result["Policy"]["Id"]

        handler = _load_handler('UpdatePolicy')
        handler(org_store, {
            "PolicyId": pid,
            "Description": "Updated description",
        })
        assert org_store.policies[pid].description == "Updated description"

    def test_delete_unattached_policy(self, org_store):
        create = _load_handler('CreatePolicy')
        result = create(org_store, {
            "Content": SCP_CONTENT,
            "Description": "DeleteMe",
            "Name": "DeleteMe",
            "Type": "SERVICE_CONTROL_POLICY",
        })
        pid = result["Policy"]["Id"]

        handler = _load_handler('DeletePolicy')
        handler(org_store, {"PolicyId": pid})
        assert pid not in org_store.policies

    def test_delete_attached_policy_fails(self, org_store):
        create = _load_handler('CreatePolicy')
        result = create(org_store, {
            "Content": SCP_CONTENT,
            "Description": "Attached policy",
            "Name": "AttachedPolicy",
            "Type": "SERVICE_CONTROL_POLICY",
        })
        pid = result["Policy"]["Id"]

        # Attach to root
        attach = _load_handler('AttachPolicy')
        attach(org_store, {"PolicyId": pid, "TargetId": org_store.roots[0]})

        handler = _load_handler('DeletePolicy')
        with pytest.raises(PolicyInUseException):
            handler(org_store, {"PolicyId": pid})

    def test_attach_policy(self, org_store):
        create = _load_handler('CreatePolicy')
        result = create(org_store, {
            "Content": SCP_CONTENT,
            "Description": "Test attach",
            "Name": "TestAttach",
            "Type": "SERVICE_CONTROL_POLICY",
        })
        pid = result["Policy"]["Id"]
        root_id = org_store.roots[0]

        handler = _load_handler('AttachPolicy')
        handler(org_store, {"PolicyId": pid, "TargetId": root_id})
        assert root_id in org_store.policy_targets[pid]

    def test_attach_duplicate_fails(self, org_store):
        create = _load_handler('CreatePolicy')
        result = create(org_store, {
            "Content": SCP_CONTENT,
            "Description": "Test attach",
            "Name": "TestAttach2",
            "Type": "SERVICE_CONTROL_POLICY",
        })
        pid = result["Policy"]["Id"]
        root_id = org_store.roots[0]

        handler = _load_handler('AttachPolicy')
        handler(org_store, {"PolicyId": pid, "TargetId": root_id})
        with pytest.raises(DuplicatePolicyAttachmentException):
            handler(org_store, {"PolicyId": pid, "TargetId": root_id})

    def test_detach_policy(self, org_store):
        create = _load_handler('CreatePolicy')
        result = create(org_store, {
            "Content": SCP_CONTENT,
            "Description": "Test detach",
            "Name": "TestDetach",
            "Type": "SERVICE_CONTROL_POLICY",
        })
        pid = result["Policy"]["Id"]
        root_id = org_store.roots[0]

        attach = _load_handler('AttachPolicy')
        attach(org_store, {"PolicyId": pid, "TargetId": root_id})

        handler = _load_handler('DetachPolicy')
        handler(org_store, {"PolicyId": pid, "TargetId": root_id})
        assert root_id not in org_store.policy_targets.get(pid, [])

    def test_list_policies(self, org_store):
        create = _load_handler('CreatePolicy')
        create(org_store, {
            "Content": SCP_CONTENT, "Description": "P1",
            "Name": "Policy1", "Type": "SERVICE_CONTROL_POLICY",
        })
        create(org_store, {
            "Content": SCP_CONTENT, "Description": "P2",
            "Name": "Policy2", "Type": "SERVICE_CONTROL_POLICY",
        })

        handler = _load_handler('ListPolicies')
        response = handler(org_store, {"Filter": "SERVICE_CONTROL_POLICY"})
        assert len(response["Policies"]) == 2

    def test_list_policies_for_target(self, org_store):
        create = _load_handler('CreatePolicy')
        result = create(org_store, {
            "Content": SCP_CONTENT, "Description": "Target policy",
            "Name": "TargetPolicy", "Type": "SERVICE_CONTROL_POLICY",
        })
        pid = result["Policy"]["Id"]

        attach = _load_handler('AttachPolicy')
        attach(org_store, {"PolicyId": pid, "TargetId": org_store.roots[0]})

        handler = _load_handler('ListPoliciesForTarget')
        response = handler(org_store, {
            "TargetId": org_store.roots[0],
            "Filter": "SERVICE_CONTROL_POLICY",
        })
        assert len(response["Policies"]) == 1
