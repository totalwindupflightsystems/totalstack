"""Grafana store — Workspaces, API keys, Service Accounts, Tokens, Tags."""
import uuid
import time as _time


# === Exception classes ===
class ValidationException(Exception):
    pass

class ResourceNotFoundException(Exception):
    pass

class ConflictException(Exception):
    pass

class InternalServerException(Exception):
    pass

class AccessDeniedException(Exception):
    pass

class ThrottlingException(Exception):
    pass

class ServiceQuotaExceededException(Exception):
    pass


def _convert_tags(tags):
    if not tags:
        return {}
    if isinstance(tags, dict):
        return dict(tags)
    result = {}
    for t in tags:
        k = t.get("key", t.get("Key", ""))
        v = t.get("value", t.get("Value", ""))
        result[k] = v
    return result


class WorkspaceRecord:
    def __init__(self, accountAccessType, permissionType, authenticationProviders,
                 workspaceName=None, workspaceDescription=None, workspaceRoleArn=None,
                 organizationRoleName=None, workspaceDataSources=None,
                 grafanaVersion=None, tags=None, clientToken=None):
        self.id = f"g-{uuid.uuid4().hex[:8]}"
        self.arn = f"arn:aws:grafana:us-east-1:123456789012:workspace/{self.id}"
        self.accountAccessType = accountAccessType
        self.permissionType = permissionType
        self.authenticationProviders = authenticationProviders or []
        self.workspaceName = workspaceName or ""
        self.workspaceDescription = workspaceDescription or ""
        self.workspaceRoleArn = workspaceRoleArn or ""
        self.organizationRoleName = organizationRoleName or ""
        self.workspaceDataSources = workspaceDataSources or []
        self.grafanaVersion = grafanaVersion or "9.4"
        self.tags = _convert_tags(tags)
        self.status = "ACTIVE"
        self.endpoint = f"https://{self.id}.grafana-workspace.us-east-1.amazonaws.com"
        self.created_time = _time.time()

    def to_dict(self):
        return {
            "id": self.id,
            "arn": self.arn,
            "accountAccessType": self.accountAccessType,
            "permissionType": self.permissionType,
            "name": self.workspaceName,
            "description": self.workspaceDescription,
            "workspaceRoleArn": self.workspaceRoleArn,
            "organizationRoleName": self.organizationRoleName,
            "dataSources": self.workspaceDataSources,
            "grafanaVersion": self.grafanaVersion,
            "authentication": {"providers": self.authenticationProviders},
            "status": self.status,
            "endpoint": self.endpoint,
            "created": self.created_time,
            "modified": self.created_time,
        }


class ApiKeyRecord:
    def __init__(self, keyName, keyRole, workspaceId):
        self.keyName = keyName
        self.keyRole = keyRole
        self.workspaceId = workspaceId
        self.key = f"grafana-api-key-{uuid.uuid4().hex[:16]}"
        self.created_time = _time.time()

    def to_dict(self):
        return {
            "keyName": self.keyName,
            "keyRole": self.keyRole,
            "workspaceId": self.workspaceId,
            "key": self.key,
        }


class ServiceAccountRecord:
    def __init__(self, name, grafanaRole, workspaceId):
        self.id = f"sa-{uuid.uuid4().hex[:8]}"
        self.name = name
        self.grafanaRole = grafanaRole
        self.workspaceId = workspaceId
        self.created_time = _time.time()

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "grafanaRole": self.grafanaRole,
            "workspaceId": self.workspaceId,
        }


class ServiceAccountTokenRecord:
    def __init__(self, name, serviceAccountId, workspaceId):
        self.id = f"sat-{uuid.uuid4().hex[:8]}"
        self.name = name
        self.serviceAccountId = serviceAccountId
        self.workspaceId = workspaceId
        self.token = f"glsa-token-{uuid.uuid4().hex[:20]}"
        self.created_time = _time.time()

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "serviceAccountId": self.serviceAccountId,
            "workspaceId": self.workspaceId,
            "token": self.token,
        }


class GrafanaStore:
    def __init__(self):
        self._workspaces: dict[str, WorkspaceRecord] = {}
        self._api_keys: dict[str, dict[str, ApiKeyRecord]] = {}
        self._service_accounts: dict[str, dict[str, ServiceAccountRecord]] = {}
        self._service_account_tokens: dict[str, dict[str, ServiceAccountTokenRecord]] = {}
        self._tags: dict[str, dict] = {}

    # --- Workspace ---

    def workspaces(self, ws_id: str = None):
        if ws_id is not None:
            return self._workspaces.get(ws_id)
        return list(self._workspaces.values())

    def create_workspace(self, accountAccessType, permissionType, authenticationProviders,
                         workspaceName=None, workspaceDescription=None, workspaceRoleArn=None,
                         organizationRoleName=None, workspaceDataSources=None,
                         grafanaVersion=None, tags=None, clientToken=None):
        for ws in self._workspaces.values():
            if ws.workspaceName == workspaceName:
                raise ConflictException(f"Workspace with name '{workspaceName}' already exists")
        record = WorkspaceRecord(
            accountAccessType=accountAccessType, permissionType=permissionType,
            authenticationProviders=authenticationProviders,
            workspaceName=workspaceName, workspaceDescription=workspaceDescription,
            workspaceRoleArn=workspaceRoleArn, organizationRoleName=organizationRoleName,
            workspaceDataSources=workspaceDataSources, grafanaVersion=grafanaVersion,
            tags=tags, clientToken=clientToken)
        self._workspaces[record.id] = record
        if record.tags:
            self._tags[record.arn] = dict(record.tags)
        return {"workspace": record.to_dict()}

    def describe_workspace(self, workspaceId):
        record = self._workspaces.get(workspaceId)
        if not record:
            raise ResourceNotFoundException(f"Workspace '{workspaceId}' not found")
        return {"workspace": record.to_dict()}

    def list_workspaces(self, nextToken=None, maxResults=None):
        return {"workspaces": [w.to_dict() for w in self._workspaces.values()]}

    def update_workspace(self, workspaceId, accountAccessType=None, permissionType=None,
                         workspaceName=None, workspaceDescription=None,
                         workspaceRoleArn=None, organizationRoleName=None,
                         workspaceDataSources=None, workspaceNotificationDestinations=None,
                         workspaceOrganizationalUnits=None, stackSetName=None,
                         vpcConfiguration=None, removeVpcConfiguration=None,
                         networkAccessControl=None, removeNetworkAccessControl=None):
        record = self._workspaces.get(workspaceId)
        if not record:
            raise ResourceNotFoundException(f"Workspace '{workspaceId}' not found")
        if accountAccessType:
            record.accountAccessType = accountAccessType
        if permissionType:
            record.permissionType = permissionType
        if workspaceName:
            record.workspaceName = workspaceName
        if workspaceDescription:
            record.workspaceDescription = workspaceDescription
        if workspaceRoleArn:
            record.workspaceRoleArn = workspaceRoleArn
        if organizationRoleName:
            record.organizationRoleName = organizationRoleName
        if workspaceDataSources:
            record.workspaceDataSources = workspaceDataSources
        return {"workspace": record.to_dict()}

    def delete_workspace(self, workspaceId):
        record = self._workspaces.pop(workspaceId, None)
        if not record:
            raise ResourceNotFoundException(f"Workspace '{workspaceId}' not found")
        self._api_keys.pop(workspaceId, None)
        self._service_accounts.pop(workspaceId, None)
        self._service_account_tokens.pop(workspaceId, None)
        self._tags.pop(record.arn, None)
        return {"workspace": record.to_dict()}

    # --- API Keys (scoped to workspace) ---

    def create_workspace_api_key(self, workspaceId, keyName, keyRole, secondsToLive):
        if workspaceId not in self._workspaces:
            raise ResourceNotFoundException(f"Workspace '{workspaceId}' not found")
        if workspaceId not in self._api_keys:
            self._api_keys[workspaceId] = {}
        if keyName in self._api_keys[workspaceId]:
            raise ConflictException(f"API key '{keyName}' already exists")
        record = ApiKeyRecord(keyName=keyName, keyRole=keyRole, workspaceId=workspaceId)
        self._api_keys[workspaceId][keyName] = record
        return record.to_dict()

    def delete_workspace_api_key(self, workspaceId, keyName):
        if workspaceId not in self._api_keys:
            raise ResourceNotFoundException(f"Workspace '{workspaceId}' not found")
        record = self._api_keys[workspaceId].pop(keyName, None)
        if not record:
            raise ResourceNotFoundException(f"API key '{keyName}' not found")
        return record.to_dict()

    # --- Service Accounts ---

    def create_workspace_service_account(self, workspaceId, name, grafanaRole):
        if workspaceId not in self._workspaces:
            raise ResourceNotFoundException(f"Workspace '{workspaceId}' not found")
        if workspaceId not in self._service_accounts:
            self._service_accounts[workspaceId] = {}
        for sa in self._service_accounts[workspaceId].values():
            if sa.name == name:
                raise ConflictException(f"Service account '{name}' already exists")
        record = ServiceAccountRecord(name=name, grafanaRole=grafanaRole, workspaceId=workspaceId)
        self._service_accounts[workspaceId][record.id] = record
        return record.to_dict()

    def delete_workspace_service_account(self, workspaceId, serviceAccountId):
        if workspaceId not in self._service_accounts:
            raise ResourceNotFoundException(f"Workspace '{workspaceId}' not found")
        record = self._service_accounts[workspaceId].pop(serviceAccountId, None)
        if not record:
            raise ResourceNotFoundException(f"Service account '{serviceAccountId}' not found")
        return {"serviceAccountId": record.id, "workspaceId": record.workspaceId}

    # --- Service Account Tokens ---

    def create_workspace_service_account_token(self, workspaceId, serviceAccountId, name, secondsToLive):
        if workspaceId not in self._workspaces:
            raise ResourceNotFoundException(f"Workspace '{workspaceId}' not found")
        if workspaceId not in self._service_accounts:
            raise ResourceNotFoundException(f"Workspace '{workspaceId}' not found")
        if serviceAccountId not in self._service_accounts[workspaceId]:
            raise ResourceNotFoundException(f"Service account '{serviceAccountId}' not found")
        if workspaceId not in self._service_account_tokens:
            self._service_account_tokens[workspaceId] = {}
        record = ServiceAccountTokenRecord(name=name, serviceAccountId=serviceAccountId, workspaceId=workspaceId)
        self._service_account_tokens[workspaceId][record.id] = record
        return {"serviceAccountToken": {"id": record.id, "name": record.name, "token": record.token}, "workspaceId": record.workspaceId, "serviceAccountId": record.serviceAccountId}

    def delete_workspace_service_account_token(self, workspaceId, serviceAccountId, tokenId):
        if workspaceId not in self._service_account_tokens:
            raise ResourceNotFoundException(f"Workspace '{workspaceId}' not found")
        record = self._service_account_tokens[workspaceId].pop(tokenId, None)
        if not record:
            raise ResourceNotFoundException(f"Token '{tokenId}' not found")
        return {"tokenId": record.id}

    # --- Tags ---

    def tag_resource(self, resourceArn, tags):
        tag_dict = _convert_tags(tags)
        if resourceArn in self._tags:
            self._tags[resourceArn].update(tag_dict)
        else:
            self._tags[resourceArn] = tag_dict
        return {}

    def untag_resource(self, resourceArn, tagKeys):
        if resourceArn in self._tags:
            for k in tagKeys:
                self._tags[resourceArn].pop(k, None)
            if not self._tags[resourceArn]:
                del self._tags[resourceArn]
        return {}

    def list_tags_for_resource(self, resourceArn):
        return {"tags": dict(self._tags.get(resourceArn, {}))}

    # --- Authentication ---

    def describe_workspace_authentication(self, workspaceId):
        ws = self._workspaces.get(workspaceId)
        if not ws:
            raise ResourceNotFoundException(f"Workspace '{workspaceId}' not found")
        return {"authentication": {"providers": ws.authenticationProviders}}

    def update_workspace_authentication(self, workspaceId, authenticationProviders):
        ws = self._workspaces.get(workspaceId)
        if not ws:
            raise ResourceNotFoundException(f"Workspace '{workspaceId}' not found")
        ws.authenticationProviders = authenticationProviders
        return {"authentication": {"providers": ws.authenticationProviders}}
