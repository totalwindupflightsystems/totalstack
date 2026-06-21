"""Integration tests for CodeArtifact — real CodeArtifactStore."""
import pytest
import os, sys, importlib.util, types

ASSEMBLED_DIR = os.path.dirname(__file__)
SERVICE_DIR = os.path.join(ASSEMBLED_DIR, '..', 'codeartifact')

# Load models module
models_spec = importlib.util.spec_from_file_location('models', os.path.join(SERVICE_DIR, 'models.code.py'))
models_mod = importlib.util.module_from_spec(models_spec)
models_spec.loader.exec_module(models_mod)

CodeArtifactStore = models_mod.CodeArtifactStore
DomainRecord = models_mod.DomainRecord
RepositoryRecord = models_mod.RepositoryRecord
PackageVersionRecord = models_mod.PackageVersionRecord
ResourceNotFoundException = models_mod.ResourceNotFoundException
ValidationException = models_mod.ValidationException
ConflictException = models_mod.ConflictException
_validate_domain_name = models_mod._validate_domain_name
_validate_repo_name = models_mod._validate_repo_name

# Load handler helpers
import time as _time
import uuid as _uuid

def _load_handler(op_name, globals_inject=None):
    """Load a single-handler .code.py file — returns the handler function."""
    path = os.path.join(SERVICE_DIR, op_name + '.code.py')
    spec = importlib.util.spec_from_file_location(op_name, path)
    mod = importlib.util.module_from_spec(spec)
    mod.ResourceNotFoundException = ResourceNotFoundException
    mod.ValidationException = ValidationException
    mod.ConflictException = ConflictException
    mod.time = _time
    mod.uuid = _uuid
    mod.DomainRecord = DomainRecord
    mod.RepositoryRecord = RepositoryRecord
    mod.PackageVersionRecord = PackageVersionRecord
    mod._validate_domain_name = _validate_domain_name
    mod._validate_repo_name = _validate_repo_name
    mod.dataclass = lambda f: f
    if globals_inject:
        for name, value in globals_inject.items():
            setattr(mod, name, value)
    spec.loader.exec_module(mod)
    skip_names = {'dataclass', 'time', 'uuid', '<lambda>', 'DomainRecord', 'RepositoryRecord',
                  'PackageVersionRecord', '_validate_domain_name', '_validate_repo_name'}
    handler = None
    for v in mod.__dict__.values():
        if (isinstance(v, types.FunctionType)
            and not v.__name__.startswith('_')
            and v.__name__ not in skip_names):
            handler = v
            break
    return handler

def _load_module(op_name, globals_inject=None):
    """Load a multi-handler .code.py file — returns the full module."""
    path = os.path.join(SERVICE_DIR, op_name + '.code.py')
    spec = importlib.util.spec_from_file_location(op_name, path)
    mod = importlib.util.module_from_spec(spec)
    mod.ResourceNotFoundException = ResourceNotFoundException
    mod.ValidationException = ValidationException
    mod.ConflictException = ConflictException
    mod.time = _time
    mod.uuid = _uuid
    mod.dataclass = lambda f: f
    if globals_inject:
        for name, value in globals_inject.items():
            setattr(mod, name, value)
    spec.loader.exec_module(mod)
    return mod


class TestDomainCRUD:
    """Integration tests for Domain operations."""

    @pytest.fixture
    def store(self):
        return CodeArtifactStore()

    def test_create_domain_happy_path(self, store):
        handler = _load_handler('CreateDomain')
        response = handler(store, {"domain": "test-domain"})
        assert response is not None
        assert "domain" in response
        assert response["domain"]["name"] == "test-domain"
        assert response["domain"]["status"] == "Active"
        assert "test-domain" in store.domains

    def test_create_domain_missing_name(self, store):
        handler = _load_handler('CreateDomain')
        with pytest.raises(ValidationException):
            handler(store, {})

    def test_create_domain_duplicate(self, store):
        handler = _load_handler('CreateDomain')
        handler(store, {"domain": "test-domain"})
        with pytest.raises(ConflictException):
            handler(store, {"domain": "test-domain"})

    def test_describe_domain(self, store):
        create = _load_handler('CreateDomain')
        describe = _load_handler('DescribeDomain')
        create(store, {"domain": "test-domain"})
        response = describe(store, {"domain": "test-domain"})
        assert response["domain"]["name"] == "test-domain"
        assert response["domain"]["arn"] is not None

    def test_describe_domain_nonexistent(self, store):
        handler = _load_handler('DescribeDomain')
        with pytest.raises(ResourceNotFoundException):
            handler(store, {"domain": "nonexistent"})

    def test_list_domains(self, store):
        create = _load_handler('CreateDomain')
        list_domains = _load_handler('ListDomains')
        create(store, {"domain": "domain-a"})
        create(store, {"domain": "domain-b"})
        response = list_domains(store, {})
        assert len(response["domains"]) == 2

    def test_delete_domain(self, store):
        create = _load_handler('CreateDomain')
        delete = _load_handler('DeleteDomain')
        create(store, {"domain": "test-domain"})
        response = delete(store, {"domain": "test-domain"})
        assert response["domain"]["status"] == "Deleted"
        assert "test-domain" not in store.domains

    def test_delete_domain_nonexistent(self, store):
        handler = _load_handler('DeleteDomain')
        with pytest.raises(ResourceNotFoundException):
            handler(store, {"domain": "nonexistent"})

    def test_domain_policy_roundtrip(self, store):
        create = _load_handler('CreateDomain')
        get_policy = _load_handler('GetDomainPermissionsPolicy')
        put_policy = _load_handler('PutDomainPermissionsPolicy')
        delete_policy = _load_handler('DeleteDomainPermissionsPolicy')
        create(store, {"domain": "test-domain"})
        # Put
        put_policy(store, {"domain": "test-domain", "policyDocument": '{"Version":"2012-10-17"}'})
        # Get
        resp = get_policy(store, {"domain": "test-domain"})
        assert '{"Version":"2012-10-17"}' in resp["policy"]["document"]
        # Delete
        resp = delete_policy(store, {"domain": "test-domain"})
        assert resp["policy"]["document"] == ""


class TestRepositoryCRUD:
    """Integration tests for Repository operations."""

    @pytest.fixture
    def store(self):
        s = CodeArtifactStore()
        create_domain = _load_handler('CreateDomain')
        create_domain(s, {"domain": "test-domain"})
        return s

    def test_create_repository(self, store):
        handler = _load_handler('CreateRepository')
        response = handler(store, {"domain": "test-domain", "repository": "test-repo"})
        assert response["repository"]["name"] == "test-repo"
        assert response["repository"]["domainName"] == "test-domain"
        assert ("test-domain", "test-repo") in store.repositories

    def test_create_repo_missing_domain(self, store):
        handler = _load_handler('CreateRepository')
        with pytest.raises(ValidationException):
            handler(store, {"repository": "test-repo"})

    def test_create_repo_missing_repo_name(self, store):
        handler = _load_handler('CreateRepository')
        with pytest.raises(ValidationException):
            handler(store, {"domain": "test-domain"})

    def test_create_repo_duplicate(self, store):
        handler = _load_handler('CreateRepository')
        handler(store, {"domain": "test-domain", "repository": "test-repo"})
        with pytest.raises(ConflictException):
            handler(store, {"domain": "test-domain", "repository": "test-repo"})

    def test_describe_repository(self, store):
        create = _load_handler('CreateRepository')
        describe = _load_handler('DescribeRepository')
        create(store, {"domain": "test-domain", "repository": "test-repo"})
        response = describe(store, {"domain": "test-domain", "repository": "test-repo"})
        assert response["repository"]["name"] == "test-repo"
        assert response["repository"]["arn"] is not None

    def test_describe_repo_nonexistent(self, store):
        handler = _load_handler('DescribeRepository')
        with pytest.raises(ResourceNotFoundException):
            handler(store, {"domain": "test-domain", "repository": "nonexistent"})

    def test_update_repository_description(self, store):
        create = _load_handler('CreateRepository')
        update = _load_handler('UpdateRepository')
        describe = _load_handler('DescribeRepository')
        create(store, {"domain": "test-domain", "repository": "test-repo"})
        update(store, {"domain": "test-domain", "repository": "test-repo", "description": "New desc"})
        resp = describe(store, {"domain": "test-domain", "repository": "test-repo"})
        assert resp["repository"]["description"] == "New desc"

    def test_list_repositories(self, store):
        create = _load_handler('CreateRepository')
        list_repos = _load_handler('ListRepositories')
        create(store, {"domain": "test-domain", "repository": "repo-a"})
        create(store, {"domain": "test-domain", "repository": "repo-b"})
        response = list_repos(store, {})
        assert len(response["repositories"]) == 2

    def test_list_repos_in_domain(self, store):
        create = _load_handler('CreateRepository')
        list_repos = _load_handler('ListRepositoriesInDomain')
        create(store, {"domain": "test-domain", "repository": "repo-x"})
        response = list_repos(store, {"domain": "test-domain"})
        assert len(response["repositories"]) == 1

    def test_get_repo_endpoint(self, store):
        create = _load_handler('CreateRepository')
        handler = _load_handler('GetRepositoryEndpoint')
        create(store, {"domain": "test-domain", "repository": "test-repo"})
        response = handler(store, {"domain": "test-domain", "repository": "test-repo", "format": "npm"})
        assert "repositoryEndpoint" in response
        assert "npm" in response["repositoryEndpoint"]

    def test_repo_policy_roundtrip(self, store):
        create = _load_handler('CreateRepository')
        create(store, {"domain": "test-domain", "repository": "test-repo"})
        repo_policy_mod = _load_module('RepositoryPermissionsPolicy')
        # Put
        repo_policy_mod.execute_put_repository_permissions_policy(
            store, {"domain": "test-domain", "repository": "test-repo", "policyDocument": '{"v":"1"}'})
        # Get
        resp = repo_policy_mod.execute_get_repository_permissions_policy(
            store, {"domain": "test-domain", "repository": "test-repo"})
        assert '{"v":"1"}' in resp["policy"]["document"]
        # Delete
        resp = repo_policy_mod.execute_delete_repository_permissions_policy(
            store, {"domain": "test-domain", "repository": "test-repo"})
        assert resp["policy"]["document"] == ""


class TestPackages:
    """Integration tests for Package operations."""

    @pytest.fixture
    def store(self):
        s = CodeArtifactStore()
        create_domain = _load_handler('CreateDomain')
        create_domain(s, {"domain": "test-domain"})
        create_repo = _load_handler('CreateRepository')
        create_repo(s, {"domain": "test-domain", "repository": "test-repo"})
        return s

    def test_list_packages_empty(self, store):
        handler = _load_handler('ListPackages')
        response = handler(store, {"domain": "test-domain", "repository": "test-repo"})
        assert response["packages"] == []

    def test_list_package_versions_empty(self, store):
        handler = _load_handler('ListPackageVersions')
        response = handler(store, {"domain": "test-domain", "repository": "test-repo", "format": "npm", "package": "lodash"})
        assert response["versions"] == []


class TestAuthAndTags:
    """Integration tests for auth token and tagging."""

    @pytest.fixture
    def store(self):
        s = CodeArtifactStore()
        create_domain = _load_handler('CreateDomain')
        create_domain(s, {"domain": "test-domain"})
        return s

    def test_get_auth_token(self, store):
        mod = _load_module('AuthorizationAndTags')
        response = mod.execute_get_authorization_token(store, {"domain": "test-domain"})
        assert "authorizationToken" in response
        assert response["authorizationToken"].startswith("codeartifact-token-")

    def test_tag_and_untag_resource(self, store):
        mod = _load_module('AuthorizationAndTags')
        domain = store.domains["test-domain"]
        arn = domain.arn
        # Tag
        mod.execute_tag_resource(store, {"resourceArn": arn, "tags": [{"key": "env", "value": "test"}]})
        # List
        resp = mod.execute_list_tags_for_resource(store, {"resourceArn": arn})
        assert len(resp["tags"]) == 1
        assert resp["tags"][0]["key"] == "env"
        # Untag
        mod.execute_untag_resource(store, {"resourceArn": arn, "tagKeys": ["env"]})
        resp = mod.execute_list_tags_for_resource(store, {"resourceArn": arn})
        assert len(resp["tags"]) == 0
