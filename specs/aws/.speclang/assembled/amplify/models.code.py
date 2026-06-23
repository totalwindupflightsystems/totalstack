"""Amplify store — 5 entities: App, Branch, BackendEnvironment, DomainAssociation, Webhook.

Hierarchy: App (root) → Branch, BackendEnvironment, DomainAssociation (peers).
Branch → Webhook (child — stored globally by webhookId).
"""
import time as _time
import uuid as _uuid


def _gen_id(prefix):
    return prefix + str(_uuid.uuid4())[:8]


def _now():
    return _time.time()


def _normalize_tags(tags):
    if not tags:
        return {}
    if isinstance(tags, dict):
        return dict(tags)
    if isinstance(tags, list):
        result = {}
        for t in tags:
            k = t.get("key", t.get("Key", ""))
            v = t.get("value", t.get("Value", ""))
            result[k] = v
        return result
    return {}


# ── Exception classes ──────────────────────────────────────────────────

class NotFoundException(Exception):
    def __init__(self, message="Resource not found"):
        self.message = message
        super().__init__(self.message)


class ResourceNotFoundException(Exception):
    def __init__(self, message="Resource not found"):
        self.message = message
        super().__init__(self.message)


class BadRequestException(Exception):
    def __init__(self, message="Bad request"):
        self.message = message
        super().__init__(self.message)


class LimitExceededException(Exception):
    def __init__(self, message="Limit exceeded"):
        self.message = message
        super().__init__(self.message)


class UnauthorizedException(Exception):
    def __init__(self, message="Unauthorized"):
        self.message = message
        super().__init__(self.message)


class InternalFailureException(Exception):
    def __init__(self, message="Internal failure"):
        self.message = message
        super().__init__(self.message)


class DependentServiceFailureException(Exception):
    def __init__(self, message="Dependent service failure"):
        self.message = message
        super().__init__(self.message)


# ── Record classes ─────────────────────────────────────────────────────

class AppRecord:
    def __init__(self, name, appId=None, **kwargs):
        self.appId = appId or _gen_id("d")
        self.name = name
        self.description = kwargs.get("description", "")
        self.tags = _normalize_tags(kwargs.get("tags"))
        self.createTime = _now()
        self.updateTime = _now()
        for k, v in kwargs.items():
            if k not in ("description", "tags") and not k.startswith("_"):
                setattr(self, k, v)

    def to_dict(self):
        result = {"appId": self.appId, "name": self.name,
                  "createTime": self.createTime, "updateTime": self.updateTime}
        for attr in ["description", "repository", "platform", "defaultDomain",
                     "enableBranchAutoBuild", "enableBasicAuth", "customRules",
                     "environmentVariables", "buildSpec", "customHeaders"]:
            if hasattr(self, attr):
                result[attr] = getattr(self, attr)
        return result


class BranchRecord:
    def __init__(self, appId, branchName, **kwargs):
        self.appId = appId
        self.branchName = branchName
        self.branchArn = f"arn:aws:amplify:us-east-1:000000000000:apps/{appId}/branches/{branchName}"
        self.description = kwargs.get("description", "")
        self.stage = kwargs.get("stage", "NONE")
        self.tags = _normalize_tags(kwargs.get("tags"))
        self.createTime = _now()
        self.updateTime = _now()
        for k, v in kwargs.items():
            if k not in ("description", "stage", "tags") and not k.startswith("_"):
                setattr(self, k, v)

    def to_dict(self):
        result = {"appId": self.appId, "branchName": self.branchName,
                  "branchArn": self.branchArn, "stage": self.stage,
                  "createTime": self.createTime, "updateTime": self.updateTime}
        for attr in ["description", "framework", "enableAutoBuild",
                     "environmentVariables", "buildSpec", "ttl", "displayName"]:
            if hasattr(self, attr):
                result[attr] = getattr(self, attr)
        return result


class BackendEnvironmentRecord:
    def __init__(self, appId, environmentName, **kwargs):
        self.appId = appId
        self.environmentName = environmentName
        self.environmentArn = f"arn:aws:amplify:us-east-1:000000000000:apps/{appId}/backendenvironments/{environmentName}"
        self.stackName = kwargs.get("stackName", "")
        self.deploymentArtifacts = kwargs.get("deploymentArtifacts", "")
        self.createTime = _now()
        self.updateTime = _now()

    def to_dict(self):
        return {
            "appId": self.appId,
            "environmentName": self.environmentName,
            "environmentArn": self.environmentArn,
            "stackName": self.stackName,
            "deploymentArtifacts": self.deploymentArtifacts,
            "createTime": self.createTime,
            "updateTime": self.updateTime,
        }


class DomainAssociationRecord:
    def __init__(self, appId, domainName, subDomainSettings, **kwargs):
        self.appId = appId
        self.domainName = domainName
        self.subDomainSettings = subDomainSettings
        self.domainAssociationArn = f"arn:aws:amplify:us-east-1:000000000000:apps/{appId}/domains/{domainName}"
        self.enableAutoSubDomain = kwargs.get("enableAutoSubDomain", False)
        self.domainStatus = "AVAILABLE"
        self.createTime = _now()
        self.updateTime = _now()

    def to_dict(self):
        return {
            "appId": self.appId,
            "domainName": self.domainName,
            "subDomainSettings": self.subDomainSettings,
            "enableAutoSubDomain": self.enableAutoSubDomain,
            "domainStatus": self.domainStatus,
            "domainAssociationArn": self.domainAssociationArn,
            "createTime": self.createTime,
            "updateTime": self.updateTime,
        }


class WebhookRecord:
    def __init__(self, appId, branchName, webhookId=None, **kwargs):
        self.webhookId = webhookId or _gen_id("w")
        self.appId = appId
        self.branchName = branchName
        self.description = kwargs.get("description", "")
        self.webhookArn = f"arn:aws:amplify:us-east-1:000000000000:apps/{appId}/webhooks/{self.webhookId}"
        self.createTime = _now()
        self.updateTime = _now()

    def to_dict(self):
        return {
            "webhookId": self.webhookId,
            "appId": self.appId,
            "branchName": self.branchName,
            "description": self.description,
            "webhookArn": self.webhookArn,
            "createTime": self.createTime,
            "updateTime": self.updateTime,
        }


# ── Store class ────────────────────────────────────────────────────────

class AmplifyStore:
    def __init__(self):
        self._apps = {}
        self._branches = {}
        self._backend_environments = {}
        self._domain_associations = {}
        self._webhooks = {}
        self._tags = {}

    # ── App ────────────────────────────────────────────────────────

    def apps(self, appId=None):
        if appId is not None:
            return self._apps.get(appId)
        return list(self._apps.values())

    def create_app(self, name, **kwargs):
        record = AppRecord(name, **kwargs)
        self._apps[record.appId] = record
        if record.tags:
            self._tags[record.appId] = record.tags
        return record

    def get_app(self, appId):
        record = self._apps.get(appId)
        if not record:
            raise NotFoundException(f"App {appId} not found")
        return record

    def list_apps(self, nextToken=None, maxResults=None):
        result = [a.to_dict() for a in self._apps.values()]
        return {"apps": result, "nextToken": None}

    def delete_app(self, appId):
        if appId not in self._apps:
            raise NotFoundException(f"App {appId} not found")
        record = self._apps.pop(appId)
        return record

    def update_app(self, appId, **kwargs):
        record = self._apps.get(appId)
        if not record:
            raise NotFoundException(f"App {appId} not found")
        for k, v in kwargs.items():
            if v is not None:
                setattr(record, k, v)
        record.updateTime = _now()
        return record

    # ── Branch ─────────────────────────────────────────────────────

    def branches(self, appId=None, branchName=None):
        if branchName is not None and appId is not None:
            return self._branches.get((appId, branchName))
        if appId is not None:
            return [v for k, v in self._branches.items() if k[0] == appId]
        return list(self._branches.values())

    def create_branch(self, appId, branchName, **kwargs):
        if appId not in self._apps:
            raise NotFoundException(f"App {appId} not found")
        key = (appId, branchName)
        if key in self._branches:
            raise BadRequestException(f"Branch {branchName} already exists")
        record = BranchRecord(appId, branchName, **kwargs)
        self._branches[key] = record
        if record.tags:
            self._tags[record.branchArn] = record.tags
        return record

    def get_branch(self, appId, branchName):
        record = self._branches.get((appId, branchName))
        if not record:
            raise NotFoundException(f"Branch {branchName} not found")
        return record

    def list_branches(self, appId, nextToken=None, maxResults=None):
        result = [v.to_dict() for k, v in self._branches.items() if k[0] == appId]
        return {"branches": result, "nextToken": None}

    def delete_branch(self, appId, branchName):
        key = (appId, branchName)
        if key not in self._branches:
            raise NotFoundException(f"Branch {branchName} not found")
        record = self._branches.pop(key)
        return record

    def update_branch(self, appId, branchName, **kwargs):
        key = (appId, branchName)
        record = self._branches.get(key)
        if not record:
            raise NotFoundException(f"Branch {branchName} not found")
        for k, v in kwargs.items():
            if v is not None:
                setattr(record, k, v)
        record.updateTime = _now()
        return record

    # ── BackendEnvironment ─────────────────────────────────────────

    def backend_environments(self, appId=None, environmentName=None):
        if environmentName is not None and appId is not None:
            return self._backend_environments.get((appId, environmentName))
        if appId is not None:
            return [v for k, v in self._backend_environments.items() if k[0] == appId]
        return list(self._backend_environments.values())

    def create_backend_environment(self, appId, environmentName, **kwargs):
        if appId not in self._apps:
            raise NotFoundException(f"App {appId} not found")
        key = (appId, environmentName)
        if key in self._backend_environments:
            raise BadRequestException(f"BackendEnvironment {environmentName} already exists")
        record = BackendEnvironmentRecord(appId, environmentName, **kwargs)
        self._backend_environments[key] = record
        return record

    def get_backend_environment(self, appId, environmentName):
        record = self._backend_environments.get((appId, environmentName))
        if not record:
            raise NotFoundException(f"BackendEnvironment {environmentName} not found")
        return record

    def list_backend_environments(self, appId, nextToken=None, maxResults=None, environmentName=None):
        result = [v.to_dict() for k, v in self._backend_environments.items() if k[0] == appId]
        return {"backendEnvironments": result, "nextToken": None}

    def delete_backend_environment(self, appId, environmentName):
        key = (appId, environmentName)
        if key not in self._backend_environments:
            raise NotFoundException(f"BackendEnvironment {environmentName} not found")
        record = self._backend_environments.pop(key)
        return record

    # ── DomainAssociation ──────────────────────────────────────────

    def domain_associations(self, appId=None, domainName=None):
        if domainName is not None and appId is not None:
            return self._domain_associations.get((appId, domainName))
        if appId is not None:
            return [v for k, v in self._domain_associations.items() if k[0] == appId]
        return list(self._domain_associations.values())

    def create_domain_association(self, appId, domainName, subDomainSettings, **kwargs):
        if appId not in self._apps:
            raise NotFoundException(f"App {appId} not found")
        key = (appId, domainName)
        if key in self._domain_associations:
            raise BadRequestException(f"DomainAssociation {domainName} already exists")
        record = DomainAssociationRecord(appId, domainName, subDomainSettings, **kwargs)
        self._domain_associations[key] = record
        return record

    def get_domain_association(self, appId, domainName):
        record = self._domain_associations.get((appId, domainName))
        if not record:
            raise NotFoundException(f"DomainAssociation {domainName} not found")
        return record

    def list_domain_associations(self, appId, nextToken=None, maxResults=None):
        result = [v.to_dict() for k, v in self._domain_associations.items() if k[0] == appId]
        return {"domainAssociations": result, "nextToken": None}

    def delete_domain_association(self, appId, domainName):
        key = (appId, domainName)
        if key not in self._domain_associations:
            raise NotFoundException(f"DomainAssociation {domainName} not found")
        record = self._domain_associations.pop(key)
        return record

    def update_domain_association(self, appId, domainName, **kwargs):
        key = (appId, domainName)
        record = self._domain_associations.get(key)
        if not record:
            raise NotFoundException(f"DomainAssociation {domainName} not found")
        for k, v in kwargs.items():
            if v is not None:
                setattr(record, k, v)
        record.updateTime = _now()
        return record

    # ── Webhook ────────────────────────────────────────────────────

    def webhooks(self, webhookId=None):
        if webhookId is not None:
            return self._webhooks.get(webhookId)
        return list(self._webhooks.values())

    def create_webhook(self, appId, branchName, **kwargs):
        if appId not in self._apps:
            raise NotFoundException(f"App {appId} not found")
        record = WebhookRecord(appId, branchName, **kwargs)
        self._webhooks[record.webhookId] = record
        return record

    def get_webhook(self, webhookId):
        record = self._webhooks.get(webhookId)
        if not record:
            raise NotFoundException(f"Webhook {webhookId} not found")
        return record

    def list_webhooks(self, appId, nextToken=None, maxResults=None):
        result = [v.to_dict() for v in self._webhooks.values() if v.appId == appId]
        return {"webhooks": result, "nextToken": None}

    def delete_webhook(self, webhookId):
        if webhookId not in self._webhooks:
            raise NotFoundException(f"Webhook {webhookId} not found")
        record = self._webhooks.pop(webhookId)
        return record

    def update_webhook(self, webhookId, **kwargs):
        record = self._webhooks.get(webhookId)
        if not record:
            raise NotFoundException(f"Webhook {webhookId} not found")
        for k, v in kwargs.items():
            if v is not None:
                setattr(record, k, v)
        record.updateTime = _now()
        return record

    # ── Tags ───────────────────────────────────────────────────────

    def tag_resource(self, resourceArn, tags):
        normalized = _normalize_tags(tags)
        if not normalized:
            return
        existing = self._tags.get(resourceArn, {})
        existing.update(normalized)
        self._tags[resourceArn] = existing

    def untag_resource(self, resourceArn, tagKeys):
        existing = self._tags.get(resourceArn, {})
        for key in tagKeys:
            existing.pop(key, None)
        self._tags[resourceArn] = existing

    def list_tags_for_resource(self, resourceArn):
        tags = self._tags.get(resourceArn, {})
        return {"tags": [{"key": k, "value": v} for k, v in tags.items()]}
