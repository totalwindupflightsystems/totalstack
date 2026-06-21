"""CodeArtifact store and models for TotalStack greenfield emulator.

CodeArtifact is a fully managed artifact repository service. The entity hierarchy:
  Domain → Repository → Package → PackageVersion

Each layer has CRUD operations with permission policies at domain/repo level.
"""

from collections import defaultdict
import time as _time
import uuid as _uuid


# ── Exception Classes ──────────────────────────────────────────────────────

class AccessDeniedException(Exception):
    """The operation was denied due to insufficient permissions."""
    pass

class ConflictException(Exception):
    """The operation cannot be completed because a resource is in a conflicting state."""
    pass

class InternalServerException(Exception):
    """An internal server error occurred."""
    pass

class ResourceNotFoundException(Exception):
    """The specified resource does not exist."""
    pass

class ServiceQuotaExceededException(Exception):
    """The operation would exceed a service quota."""
    pass

class ThrottlingException(Exception):
    """The request was throttled."""
    pass

class ValidationException(Exception):
    """The input parameters are invalid."""
    pass


# ── Data Records ───────────────────────────────────────────────────────────

class DomainRecord:
    """Represents a CodeArtifact domain."""
    def __init__(self, name, owner, encryption_key=None):
        self.name = name
        self.owner = owner
        self.arn = f"arn:aws:codeartifact:us-east-1:{owner}:domain/{name}"
        self.created_time = _time.time()
        self.encryption_key = encryption_key or "AWS_OWNED_KEY"
        self.s3_bucket_arn = f"arn:aws:s3:::codeartifact-{name}"
        self.repository_count = 0
        self.asset_size_bytes = 0
        self.status = "Active"

class RepositoryRecord:
    """Represents a CodeArtifact repository within a domain."""
    def __init__(self, name, domain_name, domain_owner, description=None):
        self.name = name
        self.domain_name = domain_name
        self.domain_owner = domain_owner
        self.arn = f"arn:aws:codeartifact:us-east-1:{domain_owner}:repository/{domain_name}/{name}"
        self.description = description or ""
        self.created_time = _time.time()
        self.administrator_account = domain_owner
        self.external_connections = []
        self.upstreams = []

class PackageVersionRecord:
    """Represents a single package version within a repository."""
    def __init__(self, version, package_name, package_format, package_namespace=None):
        self.version = version
        self.package_name = package_name
        self.format = package_format
        self.namespace = package_namespace
        self.status = "Published"
        self.revision = _uuid.uuid4().hex[:8]
        self.published_time = _time.time()


# ── CodeArtifactStore ──────────────────────────────────────────────────────

class CodeArtifactStore:
    """In-memory store for CodeArtifact resources."""

    def __init__(self):
        # Domain operations
        self.domains = {}          # name → DomainRecord
        self.domain_policies = {}  # domain_name → policy_document (string)

        # Repository operations
        self.repositories = {}     # (domain_name, repo_name) → RepositoryRecord
        self.repo_policies = {}    # (domain_name, repo_name) → policy_document
        self.repo_endpoints = {}   # (domain_name, repo_name) → {format: url}

        # Package operations
        self.packages = defaultdict(dict)  # (domain, repo) → {pkg_name: pkg_info}
        self.package_versions = defaultdict(dict)  # (domain, repo, pkg_name, format) → {version: PackageVersionRecord}
        self.package_groups = {}  # group_name → PackageGroupRecord
        self.package_group_origins = {}  # group_name → origin_config

        # Tagging
        self.tags = defaultdict(dict)  # arn → {key: value}

    # ── Domain Helpers ─────────────────────────────────────────────────

    def _get_domain(self, domain_name):
        if domain_name not in self.domains:
            raise ResourceNotFoundException(f"Domain {domain_name} not found")
        return self.domains[domain_name]

    def _get_repo(self, domain_name, repo_name):
        key = (domain_name, repo_name)
        if key not in self.repositories:
            raise ResourceNotFoundException(f"Repository {repo_name} not found in domain {domain_name}")
        return self.repositories[key]

    # ── Tag Helpers ────────────────────────────────────────────────────

    def _get_arn(self, resource_type, domain_name, repo_name=None, package_name=None):
        owner = self.domains.get(domain_name, DomainRecord(domain_name, "123456789012")).owner
        if resource_type == "domain":
            return f"arn:aws:codeartifact:us-east-1:{owner}:domain/{domain_name}"
        elif resource_type == "repository":
            return f"arn:aws:codeartifact:us-east-1:{owner}:repository/{domain_name}/{repo_name}"
        elif resource_type == "package":
            return f"arn:aws:codeartifact:us-east-1:{owner}:package/{domain_name}/{repo_name}/{package_name}"
        return f"arn:aws:codeartifact:us-east-1:{owner}:{resource_type}/{domain_name}"


# ── Helper Functions ───────────────────────────────────────────────────────

def _validate_domain_name(name):
    """Validate domain name: 2-50 chars, must start with letter, alphanumeric+hyphen."""
    if not name or len(name) < 2 or len(name) > 50:
        raise ValidationException("Domain name must be between 2 and 50 characters")
    if not name[0].isalpha():
        raise ValidationException("Domain name must start with a letter")
    import re
    if not re.match(r'^[a-z][a-z0-9\-]{0,48}[a-z0-9]$', name):
        raise ValidationException("Domain name contains invalid characters")

def _validate_repo_name(name):
    """Validate repository name: 2-100 chars, alphanumeric+special."""
    if not name or len(name) < 2 or len(name) > 100:
        raise ValidationException("Repository name must be between 2 and 100 characters")
    import re
    if not re.match(r'^[A-Za-z0-9][A-Za-z0-9._\-]{1,99}$', name):
        raise ValidationException("Repository name contains invalid characters")
