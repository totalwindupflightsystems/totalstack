"""Integration test for Signer — real store."""
import pytest
import os
import types
import importlib.util
import time as _time
import uuid as _uuid

ASSEMBLED_DIR = os.path.dirname(__file__)
SERVICE_DIR = os.path.join(ASSEMBLED_DIR, '..', 'signer')

# Load models.code.py dynamically
models_spec = importlib.util.spec_from_file_location('models', os.path.join(SERVICE_DIR, 'models.code.py'))
models_mod = importlib.util.module_from_spec(models_spec)
models_spec.loader.exec_module(models_mod)

# Pull out needed names
SignerStore = models_mod.SignerStore
ProfileRecord = models_mod.ProfileRecord
JobRecord = models_mod.JobRecord
PlatformRecord = models_mod.PlatformRecord
Permission = models_mod.Permission
SignatureValidityPeriod = models_mod.SignatureValidityPeriod
SigningMaterial = models_mod.SigningMaterial
SigningPlatformOverrides = models_mod.SigningPlatformOverrides
Source = models_mod.Source
Destination = models_mod.Destination
SignedObject = models_mod.SignedObject
ConflictException = models_mod.ConflictException
ResourceNotFoundException = models_mod.ResourceNotFoundException
ValidationException = models_mod.ValidationException
AccessDeniedException = models_mod.AccessDeniedException
BadRequestException = models_mod.BadRequestException
NotFoundException = models_mod.NotFoundException
NotFoundError = getattr(models_mod, 'NotFoundException', ResourceNotFoundException)

skip_names = {'dataclass', 'time', 'uuid', '<lambda>'}


def _load_handler(op_name, globals_inject=None):
    """Load a generated .code.py module — returns the handler function."""
    path = os.path.join(SERVICE_DIR, op_name + '.code.py')
    spec = importlib.util.spec_from_file_location(op_name, path)
    mod = importlib.util.module_from_spec(spec)
    mod.SignerStore = SignerStore
    mod.ConflictException = ConflictException
    mod.ResourceNotFoundException = ResourceNotFoundException
    mod.ValidationException = ValidationException
    mod.AccessDeniedException = AccessDeniedException
    mod.BadRequestException = BadRequestException
    mod.NotFoundException = NotFoundException
    mod.NotFoundError = NotFoundError
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


class TestSigningPlatform:
    """Signing platforms are read-only, pre-defined."""

    _store = None

    @property
    def store(self):
        if self._store is None:
            self._store = SignerStore()
        return self._store

    def test_get_signing_platform_happy(self):
        handler = _load_handler('GetSigningPlatform')
        resp = handler(self.store, {"platformId": "AWSLambda-SHA384-ECDSA"})
        assert resp["platformId"] == "AWSLambda-SHA384-ECDSA"
        assert resp["category"] == "AWS Lambda"

    def test_get_signing_platform_not_found(self):
        handler = _load_handler('GetSigningPlatform')
        with pytest.raises(ResourceNotFoundException):
            handler(self.store, {"platformId": "nonexistent"})

    def test_list_signing_platforms(self):
        handler = _load_handler('ListSigningPlatforms')
        resp = handler(self.store, {})
        assert len(resp["platforms"]) >= 4
        assert any(p["platformId"] == "AWSLambda-SHA384-ECDSA" for p in resp["platforms"])


class TestSigningProfile:
    _store = None

    @property
    def store(self):
        if self._store is None:
            self._store = SignerStore()
        return self._store

    def test_create_profile_happy(self):
        handler = _load_handler('PutSigningProfile')
        resp = handler(self.store, {
            "profileName": "test-profile",
            "platformId": "AWSLambda-SHA384-ECDSA",
            "signingMaterial": {"certificateArn": "arn:aws:acm:us-east-1:123456789012:certificate/abc"},
        })
        assert "arn" in resp
        assert resp["arn"].endswith("test-profile")
        assert "profileVersion" in resp

    def test_create_profile_with_tags(self):
        handler = _load_handler('PutSigningProfile')
        resp = handler(self.store, {
            "profileName": "tagged-profile",
            "platformId": "AWSLambda-SHA384-ECDSA",
            "tags": [{"key": "env", "value": "test"}, {"key": "team", "value": "dev"}],
        })
        assert resp["arn"].endswith("tagged-profile")

    def test_create_profile_update_existing(self):
        handler = _load_handler('PutSigningProfile')
        resp1 = handler(self.store, {
            "profileName": "update-profile",
            "platformId": "AWSLambda-SHA384-ECDSA",
        })
        v1 = resp1["profileVersion"]
        resp2 = handler(self.store, {
            "profileName": "update-profile",
            "platformId": "AWSLambda-SHA384-ECDSA",
        })
        v2 = resp2["profileVersion"]
        assert v2 != v1  # version changes on update

    def test_get_profile_happy(self):
        handler = _load_handler('PutSigningProfile')
        handler(self.store, {
            "profileName": "get-profile",
            "platformId": "AWSLambda-SHA384-ECDSA",
        })
        get_handler = _load_handler('GetSigningProfile')
        resp = get_handler(self.store, {"profileName": "get-profile"})
        assert resp["profileName"] == "get-profile"
        assert resp["status"] == "Active"

    def test_get_profile_not_found(self):
        get_handler = _load_handler('GetSigningProfile')
        with pytest.raises(ResourceNotFoundException):
            get_handler(self.store, {"profileName": "nonexistent"})

    def test_list_profiles(self):
        handler = _load_handler('PutSigningProfile')
        handler(self.store, {"profileName": "list-prof-1", "platformId": "AWSLambda-SHA384-ECDSA"})
        handler(self.store, {"profileName": "list-prof-2", "platformId": "AWSLambda-SHA384-ECDSA"})

        list_handler = _load_handler('ListSigningProfiles')
        resp = list_handler(self.store, {})
        names = [p["profileName"] for p in resp["profiles"]]
        assert "list-prof-1" in names
        assert "list-prof-2" in names

    def test_cancel_profile(self):
        handler = _load_handler('PutSigningProfile')
        handler(self.store, {"profileName": "cancel-prof", "platformId": "AWSLambda-SHA384-ECDSA"})

        cancel_handler = _load_handler('CancelSigningProfile')
        cancel_handler(self.store, {"profileName": "cancel-prof"})

        get_handler = _load_handler('GetSigningProfile')
        resp = get_handler(self.store, {"profileName": "cancel-prof"})
        assert resp["status"] == "Canceled"

    def test_cancel_profile_not_found(self):
        cancel_handler = _load_handler('CancelSigningProfile')
        with pytest.raises(ResourceNotFoundException):
            cancel_handler(self.store, {"profileName": "nonexistent"})

    def test_revoke_profile(self):
        handler = _load_handler('PutSigningProfile')
        resp = handler(self.store, {"profileName": "revoke-prof", "platformId": "AWSLambda-SHA384-ECDSA"})

        revoke_handler = _load_handler('RevokeSigningProfile')
        revoke_handler(self.store, {
            "profileName": "revoke-prof",
            "profileVersion": resp["profileVersion"],
            "reason": "No longer needed",
            "effectiveTime": _time.time(),
        })

        get_handler = _load_handler('GetSigningProfile')
        resp2 = get_handler(self.store, {"profileName": "revoke-prof"})
        assert resp2["status"] == "Revoked"
        assert resp2["revocationRecord"] is not None

    def test_revoke_profile_not_found(self):
        revoke_handler = _load_handler('RevokeSigningProfile')
        with pytest.raises(ResourceNotFoundException):
            revoke_handler(self.store, {
                "profileName": "nonexistent",
                "profileVersion": "1",
                "reason": "test",
                "effectiveTime": _time.time(),
            })


class TestSigningJob:
    _store = None

    @property
    def store(self):
        if self._store is None:
            self._store = SignerStore()
        return self._store

    def _create_profile(self):
        """Helper to create a profile for job testing."""
        handler = _load_handler('PutSigningProfile')
        handler(self.store, {"profileName": "job-prof", "platformId": "AWSLambda-SHA384-ECDSA"})

    def test_start_job_happy(self):
        self._create_profile()
        handler = _load_handler('StartSigningJob')
        resp = handler(self.store, {
            "source": {"s3": {"bucketName": "my-bucket", "key": "code.zip", "version": "1"}},
            "destination": {"s3": {"bucketName": "my-bucket", "prefix": "signed/"}},
            "profileName": "job-prof",
            "clientRequestToken": "token-123",
        })
        assert "jobId" in resp
        assert "jobOwner" in resp

    def test_start_job_profile_not_found(self):
        handler = _load_handler('StartSigningJob')
        with pytest.raises(ResourceNotFoundException):
            handler(self.store, {
                "source": {"s3": {"bucketName": "b", "key": "k"}},
                "destination": {"s3": {"bucketName": "b", "prefix": "p/"}},
                "profileName": "nonexistent",
                "clientRequestToken": "token",
            })

    def test_describe_job_happy(self):
        self._create_profile()
        start_handler = _load_handler('StartSigningJob')
        resp = start_handler(self.store, {
            "source": {"s3": {"bucketName": "b", "key": "k"}},
            "destination": {"s3": {"bucketName": "b", "prefix": "p/"}},
            "profileName": "job-prof",
            "clientRequestToken": "token-2",
        })

        describe_handler = _load_handler('DescribeSigningJob')
        resp2 = describe_handler(self.store, {"jobId": resp["jobId"]})
        assert resp2["jobId"] == resp["jobId"]
        assert resp2["profileName"] == "job-prof"
        assert resp2["status"] in ("InProgress", "Succeeded")

    def test_describe_job_not_found(self):
        describe_handler = _load_handler('DescribeSigningJob')
        with pytest.raises(ResourceNotFoundException):
            describe_handler(self.store, {"jobId": "nonexistent"})

    def test_list_jobs(self):
        self._create_profile()
        start_handler = _load_handler('StartSigningJob')
        start_handler(self.store, {
            "source": {"s3": {"bucketName": "b", "key": "k1"}},
            "destination": {"s3": {"bucketName": "b", "prefix": "p1/"}},
            "profileName": "job-prof",
            "clientRequestToken": "token-3",
        })
        start_handler(self.store, {
            "source": {"s3": {"bucketName": "b", "key": "k2"}},
            "destination": {"s3": {"bucketName": "b", "prefix": "p2/"}},
            "profileName": "job-prof",
            "clientRequestToken": "token-4",
        })

        list_handler = _load_handler('ListSigningJobs')
        resp = list_handler(self.store, {})
        assert len(resp["jobs"]) >= 2

    def test_revoke_signature(self):
        self._create_profile()
        start_handler = _load_handler('StartSigningJob')
        resp = start_handler(self.store, {
            "source": {"s3": {"bucketName": "b", "key": "k"}},
            "destination": {"s3": {"bucketName": "b", "prefix": "p/"}},
            "profileName": "job-prof",
            "clientRequestToken": "token-5",
        })

        revoke_handler = _load_handler('RevokeSignature')
        revoke_handler(self.store, {"jobId": resp["jobId"], "reason": "Compromised key"})
        revoke_handler(self.store, {"jobId": resp["jobId"], "reason": "Compromised key"})
        # Revoking again is ok

    def test_revoke_signature_not_found(self):
        revoke_handler = _load_handler('RevokeSignature')
        with pytest.raises(ResourceNotFoundException):
            revoke_handler(self.store, {"jobId": "nonexistent", "reason": "test"})


class TestProfilePermissions:
    _store = None

    @property
    def store(self):
        if self._store is None:
            self._store = SignerStore()
        return self._store

    def _create_profile(self):
        handler = _load_handler('PutSigningProfile')
        handler(self.store, {"profileName": "perm-prof", "platformId": "AWSLambda-SHA384-ECDSA"})

    def test_add_permission_happy(self):
        self._create_profile()
        handler = _load_handler('AddProfilePermission')
        resp = handler(self.store, {
            "profileName": "perm-prof",
            "action": "signer:StartSigningJob",
            "principal": "123456789012",
            "statementId": "stmt-1",
        })
        assert "revisionId" in resp

    def test_add_permission_profile_not_found(self):
        handler = _load_handler('AddProfilePermission')
        with pytest.raises(ResourceNotFoundException):
            handler(self.store, {
                "profileName": "nonexistent",
                "action": "signer:StartSigningJob",
                "principal": "123456789012",
                "statementId": "stmt-1",
            })

    def test_list_permissions(self):
        self._create_profile()
        add_handler = _load_handler('AddProfilePermission')
        add_handler(self.store, {
            "profileName": "perm-prof",
            "action": "signer:StartSigningJob",
            "principal": "123456789012",
            "statementId": "stmt-1",
        })

        list_handler = _load_handler('ListProfilePermissions')
        resp = list_handler(self.store, {"profileName": "perm-prof"})
        assert "permissions" in resp
        assert len(resp["permissions"]) >= 1
        assert resp["permissions"][0]["statementId"] == "stmt-1"

    def test_remove_permission(self):
        self._create_profile()
        add_handler = _load_handler('AddProfilePermission')
        add_handler(self.store, {
            "profileName": "perm-prof",
            "action": "signer:StartSigningJob",
            "principal": "123456789012",
            "statementId": "stmt-del",
        })

        remove_handler = _load_handler('RemoveProfilePermission')
        resp = remove_handler(self.store, {
            "profileName": "perm-prof",
            "revisionId": "abc",
            "statementId": "stmt-del",
        })
        assert "revisionId" in resp

    def test_remove_permission_not_found(self):
        self._create_profile()
        remove_handler = _load_handler('RemoveProfilePermission')
        with pytest.raises(ResourceNotFoundException):
            remove_handler(self.store, {
                "profileName": "perm-prof",
                "revisionId": "abc",
                "statementId": "nonexistent",
            })


class TestTags:
    _store = None

    @property
    def store(self):
        if self._store is None:
            self._store = SignerStore()
        return self._store

    def _create_profile(self):
        handler = _load_handler('PutSigningProfile')
        return handler(self.store, {"profileName": "tag-prof", "platformId": "AWSLambda-SHA384-ECDSA"})

    def test_tag_resource(self):
        resp = self._create_profile()
        arn = resp["arn"]

        tag_handler = _load_handler('TagResource')
        tag_handler(self.store, {
            "resourceArn": arn,
            "tags": [{"key": "env", "value": "prod"}, {"key": "owner", "value": "team-a"}],
        })

        list_handler = _load_handler('ListTagsForResource')
        resp2 = list_handler(self.store, {"resourceArn": arn})
        assert resp2["tags"]["env"] == "prod"
        assert resp2["tags"]["owner"] == "team-a"

    def test_untag_resource(self):
        resp = self._create_profile()
        arn = resp["arn"]

        tag_handler = _load_handler('TagResource')
        tag_handler(self.store, {"resourceArn": arn, "tags": [{"key": "env", "value": "test"}]})

        untag_handler = _load_handler('UntagResource')
        untag_handler(self.store, {"resourceArn": arn, "tagKeys": ["env"]})

        list_handler = _load_handler('ListTagsForResource')
        resp2 = list_handler(self.store, {"resourceArn": arn})
        assert "env" not in resp2["tags"]

    def test_list_tags_empty(self):
        resp = self._create_profile()
        arn = resp["arn"]
        list_handler = _load_handler('ListTagsForResource')
        resp2 = list_handler(self.store, {"resourceArn": arn})
        assert resp2["tags"] == {}


class TestSignPayload:
    _store = None

    @property
    def store(self):
        if self._store is None:
            self._store = SignerStore()
        return self._store

    def _create_profile(self):
        handler = _load_handler('PutSigningProfile')
        handler(self.store, {"profileName": "sign-prof", "platformId": "AWSLambda-SHA384-ECDSA"})

    def test_sign_payload_happy(self):
        self._create_profile()
        handler = _load_handler('SignPayload')
        resp = handler(self.store, {
            "profileName": "sign-prof",
            "payload": b"hello-world-data",
            "payloadFormat": "JSON",
        })
        assert "jobId" in resp
        assert "signature" in resp

    def test_sign_payload_profile_not_found(self):
        handler = _load_handler('SignPayload')
        with pytest.raises(ResourceNotFoundException):
            handler(self.store, {
                "profileName": "nonexistent",
                "payload": b"data",
                "payloadFormat": "JSON",
            })


class TestRevocationStatus:
    _store = None

    @property
    def store(self):
        if self._store is None:
            self._store = SignerStore()
        return self._store

    def test_get_revocation_status_happy(self):
        handler = _load_handler('GetRevocationStatus')
        resp = handler(self.store, {
            "signatureTimestamp": _time.time(),
            "platformId": "AWSLambda-SHA384-ECDSA",
            "profileVersionArn": "arn:aws:signer:us-east-1:123456789012:/signing-profiles/test/1",
            "jobArn": "arn:aws:signer:us-east-1:123456789012:/signing-jobs/test-job",
            "certificateHashes": ["abc123"],
        })
        assert "revokedEntities" in resp
