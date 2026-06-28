"""Integration test for RAM — real RamStore."""
import pytest
import os
import importlib.util
import types

ASSEMBLED_DIR = os.path.dirname(__file__)
SERVICE_DIR = os.path.join(ASSEMBLED_DIR, '..', 'ram')

# Load models module dynamically
models_spec = importlib.util.spec_from_file_location(
    'models', os.path.join(SERVICE_DIR, 'models.code.py'))
models_mod = importlib.util.module_from_spec(models_spec)
models_spec.loader.exec_module(models_mod)

# Pull out needed names
RamStore = models_mod.RamStore
InvalidParameterException = models_mod.InvalidParameterException
ResourceNotFoundException = models_mod.ResourceNotFoundException
UnknownResourceException = models_mod.UnknownResourceException
OperationNotPermittedException = models_mod.OperationNotPermittedException
PermissionAlreadyExistsException = models_mod.PermissionAlreadyExistsException
ResourceShareInvitationArnNotFoundException = models_mod.ResourceShareInvitationArnNotFoundException
ResourceShareInvitationAlreadyAcceptedException = models_mod.ResourceShareInvitationAlreadyAcceptedException
ResourceShareInvitationAlreadyRejectedException = models_mod.ResourceShareInvitationAlreadyRejectedException
ResourceShareInvitationExpiredException = models_mod.ResourceShareInvitationExpiredException


def _load_handler(op_name, globals_inject=None):
    """Load a single-handler .code.py file — returns the handler function."""
    path = os.path.join(SERVICE_DIR, op_name + '.code.py')
    spec = importlib.util.spec_from_file_location(op_name, path)
    mod = importlib.util.module_from_spec(spec)
    # Inject exception classes (generated code references these without imports)
    mod.InvalidParameterException = InvalidParameterException
    mod.ResourceNotFoundException = ResourceNotFoundException
    mod.UnknownResourceException = UnknownResourceException
    mod.OperationNotPermittedException = OperationNotPermittedException
    mod.PermissionAlreadyExistsException = PermissionAlreadyExistsException
    mod.ResourceShareInvitationArnNotFoundException = ResourceShareInvitationArnNotFoundException
    mod.ResourceShareInvitationAlreadyAcceptedException = ResourceShareInvitationAlreadyAcceptedException
    mod.ResourceShareInvitationAlreadyRejectedException = ResourceShareInvitationAlreadyRejectedException
    mod.ResourceShareInvitationExpiredException = ResourceShareInvitationExpiredException
    if globals_inject:
        for name, value in globals_inject.items():
            setattr(mod, name, value)
    spec.loader.exec_module(mod)
    # Find the handler function (skip imports like uuid, time, Exception classes)
    skip_names = {'uuid', 'time', 'datetime', 'dataclass', '<lambda>'}
    handler = None
    for v in mod.__dict__.values():
        if (isinstance(v, types.FunctionType)
                and not v.__name__.startswith('_')
                and v.__name__ not in skip_names):
            handler = v
            break
    return handler


class TestResourceShare:
    _store = None

    @property
    def store(self):
        if self._store is None:
            self._store = RamStore()
        return self._store

    def test_create_happy_path(self):
        handler = _load_handler('create-resource-share')
        req = {"name": "test-share", "principals": ["arn:aws:iam::111111111111:root"]}
        resp = handler(self.store, req)
        assert resp["resourceShareArn"].startswith("arn:aws:ram:")
        assert resp["name"] == "test-share"
        assert resp["status"] == "ACTIVE"

    def test_create_with_tags_and_resources(self):
        handler = _load_handler('create-resource-share')
        req = {
            "name": "tagged-share",
            "resourceArns": ["arn:aws:ec2:us-east-1:000000000000:instance/i-abc123"],
            "tags": [{"key": "env", "value": "test"}, {"key": "team", "value": "devops"}],
        }
        resp = handler(self.store, req)
        assert resp["resourceShareArn"].startswith("arn:aws:ram:")
        assert len(resp["tags"]) == 2
        assert resp["tags"][0]["key"] == "env"

    def test_create_missing_name(self):
        handler = _load_handler('create-resource-share')
        with pytest.raises(KeyError):
            handler(self.store, {})

    def test_get_single(self):
        handler = _load_handler('create-resource-share')
        resp = handler(self.store, {"name": "get-test"})
        arn = resp["resourceShareArn"]

        get_handler = _load_handler('get-resource-shares')
        result = get_handler(self.store, {"resourceShareArns": [arn], "resourceOwner": "SELF"})
        assert len(result["resourceShares"]) == 1
        assert result["resourceShares"][0]["name"] == "get-test"

    def test_get_all(self):
        # Create 2 shares explicitly to verify list works
        create_h = _load_handler('create-resource-share')
        create_h(self.store, {"name": "list-test-1"})
        create_h(self.store, {"name": "list-test-2"})
        get_handler = _load_handler('get-resource-shares')
        result = get_handler(self.store, {"resourceOwner": "SELF"})
        assert len(result["resourceShares"]) >= 2

    def test_get_nonexistent_arn(self):
        get_handler = _load_handler('get-resource-shares')
        result = get_handler(self.store, {"resourceShareArns": ["arn:aws:ram:us-east-1:000000000000:resource-share/nonexistent"], "resourceOwner": "SELF"})
        assert len(result["resourceShares"]) == 0

    def test_update_name(self):
        create_h = _load_handler('create-resource-share')
        resp = create_h(self.store, {"name": "update-test"})
        arn = resp["resourceShareArn"]

        update_h = _load_handler('update-resource-share')
        result = update_h(self.store, {"resourceShareArn": arn, "name": "updated-name"})
        assert result["name"] == "updated-name"

    def test_update_nonexistent(self):
        update_h = _load_handler('update-resource-share')
        with pytest.raises(UnknownResourceException):
            update_h(self.store, {"resourceShareArn": "arn:aws:ram:us-east-1:000000000000:resource-share/nonexistent", "name": "x"})

    def test_delete_happy(self):
        create_h = _load_handler('create-resource-share')
        resp = create_h(self.store, {"name": "delete-test"})
        arn = resp["resourceShareArn"]

        delete_h = _load_handler('delete-resource-share')
        result = delete_h(self.store, {"resourceShareArn": arn})
        assert result["resourceShareArn"] == arn

        # Verify deleted
        get_h = _load_handler('get-resource-shares')
        result = get_h(self.store, {"resourceShareArns": [arn], "resourceOwner": "SELF"})
        assert len(result["resourceShares"]) == 0

    def test_delete_nonexistent(self):
        delete_h = _load_handler('delete-resource-share')
        with pytest.raises(UnknownResourceException):
            delete_h(self.store, {"resourceShareArn": "arn:aws:ram:us-east-1:000000000000:resource-share/nonexistent"})


class TestPermission:
    _store = None

    @property
    def store(self):
        if self._store is None:
            self._store = RamStore()
        return self._store

    def test_create_permission_happy(self):
        handler = _load_handler('create-permission')
        req = {
            "name": "test-permission",
            "resourceType": "ec2:Instance",
            "policyTemplate": '{"Effect":"Allow"}',
        }
        resp = handler(self.store, req)
        assert resp["permissionArn"].startswith("arn:aws:ram:")
        assert resp["name"] == "test-permission"
        assert resp["defaultVersion"] == 1

    def test_create_permission_duplicate(self):
        handler = _load_handler('create-permission')
        req = {
            "name": "perm-dup-test",
            "resourceType": "ec2:Instance",
            "policyTemplate": '{"Effect":"Allow"}',
        }
        handler(self.store, req)
        with pytest.raises(PermissionAlreadyExistsException):
            handler(self.store, req)

    def test_create_missing_required(self):
        handler = _load_handler('create-permission')
        with pytest.raises(KeyError):
            handler(self.store, {})

    def test_get_permission(self):
        create_h = _load_handler('create-permission')
        resp = create_h(self.store, {
            "name": "get-perm-test",
            "resourceType": "ec2:Instance",
            "policyTemplate": '{"Effect":"Allow"}',
        })
        arn = resp["permissionArn"]

        get_h = _load_handler('get-permission')
        result = get_h(self.store, {"permissionArn": arn})
        assert result["permissionArn"] == arn
        assert result["policyTemplate"] == '{"Effect":"Allow"}'

    def test_get_nonexistent(self):
        get_h = _load_handler('get-permission')
        with pytest.raises(ResourceNotFoundException):
            get_h(self.store, {"permissionArn": "arn:aws:ram:us-east-1:000000000000:permission/nonexistent"})

    def test_list_permissions(self):
        create_h = _load_handler('create-permission')
        create_h(self.store, {
            "name": "list-perm-a",
            "resourceType": "ec2:Instance",
            "policyTemplate": '{}',
        })
        create_h(self.store, {
            "name": "list-perm-b",
            "resourceType": "ec2:Subnet",
            "policyTemplate": '{}',
        })

        list_h = _load_handler('list-permissions')
        result = list_h(self.store, {})
        assert len(result["permissions"]) >= 2

        # Filter by resource type
        result = list_h(self.store, {"resourceType": "ec2:Subnet"})
        assert len(result["permissions"]) >= 1

    def test_create_permission_version(self):
        create_h = _load_handler('create-permission')
        resp = create_h(self.store, {
            "name": "version-perm-test",
            "resourceType": "ec2:Instance",
            "policyTemplate": '{"v":1}',
        })
        arn = resp["permissionArn"]

        cv_h = _load_handler('create-permission-version')
        result = cv_h(self.store, {"permissionArn": arn, "policyTemplate": '{"v":2}'})
        assert result["permissionArn"] == arn
        assert result["version"] == 2

    def test_create_version_nonexistent(self):
        cv_h = _load_handler('create-permission-version')
        with pytest.raises(ResourceNotFoundException):
            cv_h(self.store, {"permissionArn": "arn:nonexistent", "policyTemplate": "{}"})

    def test_list_permission_versions(self):
        create_h = _load_handler('create-permission')
        resp = create_h(self.store, {
            "name": "versions-test",
            "resourceType": "ec2:Instance",
            "policyTemplate": '{"v":1}',
        })
        arn = resp["permissionArn"]

        cv_h = _load_handler('create-permission-version')
        cv_h(self.store, {"permissionArn": arn, "policyTemplate": '{"v":2}'})

        lv_h = _load_handler('list-permission-versions')
        result = lv_h(self.store, {"permissionArn": arn})
        assert len(result["versions"]) == 2

    def test_set_default_version(self):
        create_h = _load_handler('create-permission')
        resp = create_h(self.store, {
            "name": "default-ver-test",
            "resourceType": "ec2:Instance",
            "policyTemplate": '{"v":1}',
        })
        arn = resp["permissionArn"]
        cv_h = _load_handler('create-permission-version')
        cv_h(self.store, {"permissionArn": arn, "policyTemplate": '{"v":2}'})

        sdv_h = _load_handler('set-default-permission-version')
        result = sdv_h(self.store, {"permissionArn": arn, "permissionVersion": 2})
        assert result["returnValue"] is True

        # Verify
        get_h = _load_handler('get-permission')
        result = get_h(self.store, {"permissionArn": arn})
        assert result["policyTemplate"] == '{"v":2}'

    def test_set_default_nonexistent_version(self):
        create_h = _load_handler('create-permission')
        resp = create_h(self.store, {
            "name": "bad-default-test",
            "resourceType": "ec2:Instance",
            "policyTemplate": '{"v":1}',
        })
        arn = resp["permissionArn"]
        sdv_h = _load_handler('set-default-permission-version')
        with pytest.raises(InvalidParameterException):
            sdv_h(self.store, {"permissionArn": arn, "permissionVersion": 99})

    def test_delete_permission_version(self):
        create_h = _load_handler('create-permission')
        resp = create_h(self.store, {
            "name": "del-ver-test",
            "resourceType": "ec2:Instance",
            "policyTemplate": '{"v":1}',
        })
        arn = resp["permissionArn"]
        cv_h = _load_handler('create-permission-version')
        cv_h(self.store, {"permissionArn": arn, "policyTemplate": '{"v":2}'})
        cv_h(self.store, {"permissionArn": arn, "policyTemplate": '{"v":3}'})

        dv_h = _load_handler('delete-permission-version')
        result = dv_h(self.store, {"permissionArn": arn, "permissionVersion": 2})
        assert result["returnValue"] is True

        # Verify version 2 gone
        lv_h = _load_handler('list-permission-versions')
        result = lv_h(self.store, {"permissionArn": arn})
        assert len(result["versions"]) == 2  # 1 and 3 remain
        for v in result["versions"]:
            assert v["version"] != 2

    def test_delete_default_version_blocked(self):
        create_h = _load_handler('create-permission')
        resp = create_h(self.store, {
            "name": "cant-del-default",
            "resourceType": "ec2:Instance",
            "policyTemplate": '{"v":1}',
        })
        arn = resp["permissionArn"]
        dv_h = _load_handler('delete-permission-version')
        with pytest.raises(OperationNotPermittedException):
            dv_h(self.store, {"permissionArn": arn, "permissionVersion": 1})

    def test_delete_permission(self):
        create_h = _load_handler('create-permission')
        resp = create_h(self.store, {
            "name": "del-perm-test",
            "resourceType": "ec2:Instance",
            "policyTemplate": '{}',
        })
        arn = resp["permissionArn"]

        del_h = _load_handler('delete-permission')
        result = del_h(self.store, {"permissionArn": arn})
        assert result["returnValue"] is True

        # Verify gone
        get_h = _load_handler('get-permission')
        with pytest.raises(ResourceNotFoundException):
            get_h(self.store, {"permissionArn": arn})

    def test_delete_nonexistent_permission(self):
        del_h = _load_handler('delete-permission')
        with pytest.raises(ResourceNotFoundException):
            del_h(self.store, {"permissionArn": "arn:nonexistent"})


class TestAssociation:
    _store = None

    @property
    def store(self):
        if self._store is None:
            self._store = RamStore()
        return self._store

    def _create_share(self, name="assoc-test"):
        handler = _load_handler('create-resource-share')
        return handler(self.store, {"name": name})["resourceShareArn"]

    def test_associate_resource(self):
        arn = self._create_share("assoc-resource-test")
        handler = _load_handler('associate-resource-share')
        resp = handler(self.store, {
            "resourceShareArn": arn,
            "resourceArns": ["arn:aws:ec2:us-east-1:000000000000:instance/i-123"],
        })
        assert len(resp["resourceShareAssociations"]) == 1
        assert resp["resourceShareAssociations"][0]["associationType"] == "RESOURCE"
        assert resp["resourceShareAssociations"][0]["status"] == "ASSOCIATED"

    def test_associate_principal(self):
        arn = self._create_share("assoc-principal-test")
        handler = _load_handler('associate-resource-share')
        resp = handler(self.store, {
            "resourceShareArn": arn,
            "principals": ["arn:aws:iam::111111111111:role/test"],
        })
        assert len(resp["resourceShareAssociations"]) == 1
        assert resp["resourceShareAssociations"][0]["associationType"] == "PRINCIPAL"

    def test_associate_nonexistent_share(self):
        handler = _load_handler('associate-resource-share')
        with pytest.raises(UnknownResourceException):
            handler(self.store, {
                "resourceShareArn": "arn:nonexistent",
                "resourceArns": ["arn:aws:ec2:us-east-1:000000000000:instance/i-123"],
            })

    def test_disassociate_resource(self):
        arn = self._create_share("disassoc-test")
        assoc_h = _load_handler('associate-resource-share')
        assoc_h(self.store, {
            "resourceShareArn": arn,
            "resourceArns": ["arn:aws:ec2:us-east-1:000000000000:instance/i-123"],
        })

        disassoc_h = _load_handler('disassociate-resource-share')
        resp = disassoc_h(self.store, {
            "resourceShareArn": arn,
            "resourceArns": ["arn:aws:ec2:us-east-1:000000000000:instance/i-123"],
        })
        assert len(resp["resourceShareAssociations"]) == 1

    def test_get_associations(self):
        arn = self._create_share("get-assoc-test")
        assoc_h = _load_handler('associate-resource-share')
        assoc_h(self.store, {
            "resourceShareArn": arn,
            "resourceArns": ["arn:aws:ec2:us-east-1:000000000000:instance/i-456"],
        })
        assoc_h(self.store, {
            "resourceShareArn": arn,
            "principals": ["arn:aws:iam::111111111111:user/test"],
        })

        get_h = _load_handler('get-resource-share-associations')
        # Get resource associations
        resp = get_h(self.store, {
            "associationType": "RESOURCE",
            "resourceShareArns": [arn],
        })
        assert len(resp["resourceShareAssociations"]) == 1

        # Get principal associations
        resp = get_h(self.store, {
            "associationType": "PRINCIPAL",
            "resourceShareArns": [arn],
        })
        assert len(resp["resourceShareAssociations"]) == 1

    def test_associate_permission(self):
        arn = self._create_share("perm-assoc-test")
        # Create a permission first
        perm_h = _load_handler('create-permission')
        perm_resp = perm_h(self.store, {
            "name": "assoc-perm",
            "resourceType": "ec2:Instance",
            "policyTemplate": '{}',
        })
        perm_arn = perm_resp["permissionArn"]

        handler = _load_handler('associate-resource-share-permission')
        resp = handler(self.store, {
            "resourceShareArn": arn,
            "permissionArn": perm_arn,
        })
        assert resp["returnValue"] is True

    def test_disassociate_permission(self):
        arn = self._create_share("dis-perm-test")
        perm_h = _load_handler('create-permission')
        perm_resp = perm_h(self.store, {
            "name": "dis-perm",
            "resourceType": "ec2:Instance",
            "policyTemplate": '{}',
        })
        perm_arn = perm_resp["permissionArn"]

        assoc_h = _load_handler('associate-resource-share-permission')
        assoc_h(self.store, {"resourceShareArn": arn, "permissionArn": perm_arn})

        dis_h = _load_handler('disassociate-resource-share-permission')
        resp = dis_h(self.store, {"resourceShareArn": arn, "permissionArn": perm_arn})
        assert resp["returnValue"] is True

    def test_list_resource_share_permissions(self):
        arn = self._create_share("list-perms-test")
        perm_h = _load_handler('create-permission')
        perm_resp = perm_h(self.store, {
            "name": "list-perms-perm",
            "resourceType": "ec2:Instance",
            "policyTemplate": '{}',
        })
        perm_arn = perm_resp["permissionArn"]

        assoc_h = _load_handler('associate-resource-share-permission')
        assoc_h(self.store, {"resourceShareArn": arn, "permissionArn": perm_arn})

        list_h = _load_handler('list-resource-share-permissions')
        resp = list_h(self.store, {"resourceShareArn": arn})
        assert len(resp["permissions"]) == 1

    def test_list_principals(self):
        arn = self._create_share("list-princ-test")
        assoc_h = _load_handler('associate-resource-share')
        assoc_h(self.store, {
            "resourceShareArn": arn,
            "principals": ["arn:aws:iam::111111111111:root"],
        })

        list_h = _load_handler('list-principals')
        resp = list_h(self.store, {"resourceOwner": "SELF"})
        assert len(resp["principals"]) >= 1

    def test_list_resources(self):
        arn = self._create_share("list-res-test")
        assoc_h = _load_handler('associate-resource-share')
        assoc_h(self.store, {
            "resourceShareArn": arn,
            "resourceArns": ["arn:aws:ec2:us-east-1:000000000000:instance/i-999"],
        })

        list_h = _load_handler('list-resources')
        resp = list_h(self.store, {"resourceOwner": "SELF"})
        assert len(resp["resources"]) >= 1


class TestTags:
    _store = None

    @property
    def store(self):
        if self._store is None:
            self._store = RamStore()
        return self._store

    def _create_share(self, name="tag-test"):
        handler = _load_handler('create-resource-share')
        return handler(self.store, {"name": name})["resourceShareArn"]

    def test_tag_resource(self):
        arn = self._create_share("tag-test")
        handler = _load_handler('tag-resource')
        handler(self.store, {
            "resourceShareArn": arn,
            "tags": [{"key": "env", "value": "prod"}, {"key": "region", "value": "us-west-2"}],
        })

        get_h = _load_handler('get-resource-shares')
        result = get_h(self.store, {"resourceShareArns": [arn], "resourceOwner": "SELF"})
        tags = result["resourceShares"][0]["tags"]
        assert len(tags) == 2

    def test_tag_resource_nonexistent(self):
        handler = _load_handler('tag-resource')
        with pytest.raises(UnknownResourceException):
            handler(self.store, {
                "resourceShareArn": "arn:nonexistent",
                "tags": [{"key": "x", "value": "y"}],
            })

    def test_untag_resource(self):
        arn = self._create_share("untag-test")
        tag_h = _load_handler('tag-resource')
        tag_h(self.store, {
            "resourceShareArn": arn,
            "tags": [{"key": "env", "value": "test"}, {"key": "region", "value": "east"}],
        })

        untag_h = _load_handler('untag-resource')
        untag_h(self.store, {"resourceShareArn": arn, "tagKeys": ["env"]})

        get_h = _load_handler('get-resource-shares')
        result = get_h(self.store, {"resourceShareArns": [arn], "resourceOwner": "SELF"})
        tags = result["resourceShares"][0]["tags"]
        assert len(tags) == 1
        assert tags[0]["key"] == "region"


class TestInvitation:
    _store = None

    @property
    def store(self):
        if self._store is None:
            self._store = RamStore()
        return self._store

    def _create_share_and_invite(self):
        create_h = _load_handler('create-resource-share')
        resp = create_h(self.store, {"name": "invite-test"})
        share_arn = resp["resourceShareArn"]
        invite = self.store.create_invitation(share_arn)
        return invite.resourceShareInvitationArn

    def test_accept_invitation(self):
        invite_arn = self._create_share_and_invite()
        handler = _load_handler('accept-resource-share-invitation')
        resp = handler(self.store, {"resourceShareInvitationArn": invite_arn})
        assert resp["status"] == "ACCEPTED"

    def test_accept_already_accepted(self):
        invite_arn = self._create_share_and_invite()
        handler = _load_handler('accept-resource-share-invitation')
        handler(self.store, {"resourceShareInvitationArn": invite_arn})
        with pytest.raises(ResourceShareInvitationAlreadyAcceptedException):
            handler(self.store, {"resourceShareInvitationArn": invite_arn})

    def test_accept_nonexistent(self):
        handler = _load_handler('accept-resource-share-invitation')
        with pytest.raises(ResourceShareInvitationArnNotFoundException):
            handler(self.store, {"resourceShareInvitationArn": "arn:nonexistent"})

    def test_reject_invitation(self):
        invite_arn = self._create_share_and_invite()
        handler = _load_handler('reject-resource-share-invitation')
        resp = handler(self.store, {"resourceShareInvitationArn": invite_arn})
        assert resp["status"] == "REJECTED"

    def test_reject_already_rejected(self):
        invite_arn = self._create_share_and_invite()
        handler = _load_handler('reject-resource-share-invitation')
        handler(self.store, {"resourceShareInvitationArn": invite_arn})
        with pytest.raises(ResourceShareInvitationAlreadyRejectedException):
            handler(self.store, {"resourceShareInvitationArn": invite_arn})

    def test_get_invitations(self):
        self._create_share_and_invite()
        handler = _load_handler('get-resource-share-invitations')
        resp = handler(self.store, {})
        assert len(resp["resourceShareInvitations"]) >= 1

    def test_get_invitations_by_arn(self):
        invite_arn = self._create_share_and_invite()
        handler = _load_handler('get-resource-share-invitations')
        resp = handler(self.store, {"resourceShareInvitationArns": [invite_arn]})
        assert len(resp["resourceShareInvitations"]) == 1
        assert resp["resourceShareInvitations"][0]["resourceShareInvitationArn"] == invite_arn

    def test_accept_expired(self):
        invite_arn = self._create_share_and_invite()
        invite = self.store.invitations(invite_arn)
        invite.status = "EXPIRED"
        handler = _load_handler('accept-resource-share-invitation')
        with pytest.raises(ResourceShareInvitationExpiredException):
            handler(self.store, {"resourceShareInvitationArn": invite_arn})


class TestMisc:
    _store = None

    @property
    def store(self):
        if self._store is None:
            self._store = RamStore()
        return self._store

    def test_enable_sharing(self):
        handler = _load_handler('enable-sharing-with-aws-organization')
        resp = handler(self.store, {})
        assert resp["returnValue"] is True

    def test_list_resource_types(self):
        handler = _load_handler('list-resource-types')
        resp = handler(self.store, {})
        assert len(resp["resourceTypes"]) >= 1
