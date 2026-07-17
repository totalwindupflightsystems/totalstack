"""OpenSearchServerless store — collections + policies + tags."""
import json
import uuid
import time


# --- Exception classes ---

class ValidationException(Exception):
    """Invalid input parameter."""
    pass


class ResourceNotFoundException(Exception):
    """Resource not found."""
    pass


class ConflictException(Exception):
    """Resource already exists."""
    pass


class InternalServerException(Exception):
    """Internal server error."""
    pass


class ServiceQuotaExceededException(Exception):
    """Service quota exceeded."""
    pass


class OcuLimitExceededException(Exception):
    """OCU limit exceeded."""
    pass


# --- Record classes ---

class CollectionRecord:
    def __init__(self, name, id=None, type=None, description=None,
                 status=None, arn=None, standbyReplicas=None,
                 vectorOptions=None, collectionGroupName=None,
                 tags=None, createdDate=None, **kwargs):
        self.id = id or str(uuid.uuid4())
        self.name = name
        self.type = type or "SEARCH"
        self.description = description or ""
        self.status = status or "ACTIVE"
        self.arn = arn or "arn:aws:aoss:us-east-1:000000000000:collection/" + self.id
        self.standbyReplicas = standbyReplicas or "DISABLED"
        self.vectorOptions = vectorOptions
        self.collectionName = collectionGroupName
        self.tags = tags or []
        self.createdDate = createdDate or int(time.time())
        self.policyVersion = "1"

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "type": self.type,
            "description": self.description,
            "status": self.status,
            "arn": self.arn,
            "standbyReplicas": self.standbyReplicas,
            "vectorOptions": self.vectorOptions,
            "collectionGroupName": self.collectionName,
            "createdDate": self.createdDate,
        }


class PolicyRecord:
    def __init__(self, type, name, policy=None, description=None,
                 policyVersion=None, **kwargs):
        self.type = type
        self.name = name
        if policy is None:
            self.policy = {}
        elif isinstance(policy, str):
            self.policy = json.loads(policy)
        else:
            self.policy = policy
        self.description = description or ""
        self.policyVersion = policyVersion or "1"
        self.createdDate = int(time.time())
        self.lastModifiedDate = self.createdDate

    def to_dict(self):
        return {
            "type": self.type,
            "name": self.name,
            "policyVersion": self.policyVersion,
            "description": self.description,
            "policy": self.policy,
            "createdDate": self.createdDate,
            "lastModifiedDate": self.lastModifiedDate,
        }


class LifecyclePolicyRecord:
    def __init__(self, type, name, policy=None, description=None,
                 policyVersion=None, **kwargs):
        self.type = type
        self.name = name
        if policy is None:
            self.policy = {}
        elif isinstance(policy, str):
            self.policy = json.loads(policy)
        else:
            self.policy = policy
        self.description = description or ""
        self.policyVersion = policyVersion or "1"
        self.createdDate = int(time.time())
        self.lastModifiedDate = self.createdDate

    def to_dict(self):
        return {
            "type": self.type,
            "name": self.name,
            "policyVersion": self.policyVersion,
            "description": self.description,
            "policy": self.policy,
            "createdDate": self.createdDate,
            "lastModifiedDate": self.lastModifiedDate,
        }


# --- Store ---

class OpenSearchServerlessStore:
    def __init__(self):
        self._collections = {}
        self._access_policies = {}
        self._security_policies = {}
        self._lifecycle_policies = {}
        self._tags = {}

    # --- Collections ---

    def create_collection(self, name, **kwargs):
        existing = [c for c in self._collections.values() if c.name == name]
        if existing:
            raise ConflictException("Collection already exists: " + name)
        record = CollectionRecord(name=name, **kwargs)
        self._collections[record.id] = record
        return record.to_dict()

    def batch_get_collection(self, ids=None, names=None):
        result = []
        if ids:
            for cid in ids:
                if cid in self._collections:
                    result.append(self._collections[cid].to_dict())
        if names:
            for c in self._collections.values():
                if c.name in names:
                    result.append(c.to_dict())
        return {"collectionDetails": result}

    def list_collections(self, collectionFilters=None, **kwargs):
        items = [c.to_dict() for c in self._collections.values()]
        return {"collectionSummaries": items}

    def update_collection(self, id, description=None, clientToken=None, **kwargs):
        if id not in self._collections:
            raise ResourceNotFoundException("Collection not found: " + id)
        record = self._collections[id]
        if description is not None:
            record.description = description
        return record.to_dict()

    def delete_collection(self, id, clientToken=None, **kwargs):
        if id not in self._collections:
            raise ResourceNotFoundException("Collection not found: " + id)
        del self._collections[id]
        return {}

    # --- Access Policies ---

    def _policy_key(self, type, name):
        return type + ":" + name

    def create_access_policy(self, type, name, policy, description=None,
                              clientToken=None, **kwargs):
        key = self._policy_key(type, name)
        if key in self._access_policies:
            raise ConflictException("Access policy already exists: " + key)
        record = PolicyRecord(type=type, name=name, policy=policy,
                              description=description)
        self._access_policies[key] = record
        return {"accessPolicyDetail": record.to_dict()}

    def get_access_policy(self, type, name, **kwargs):
        key = self._policy_key(type, name)
        if key not in self._access_policies:
            raise ResourceNotFoundException("Access policy not found: " + key)
        return {"accessPolicyDetail": self._access_policies[key].to_dict()}

    def list_access_policies(self, type, resource=None, **kwargs):
        items = [p.to_dict() for p in self._access_policies.values()
                 if p.type == type]
        return {"accessPolicySummaries": items}

    def update_access_policy(self, type, name, policyVersion,
                              description=None, policy=None,
                              clientToken=None, **kwargs):
        key = self._policy_key(type, name)
        if key not in self._access_policies:
            raise ResourceNotFoundException("Access policy not found: " + key)
        record = self._access_policies[key]
        record.policyVersion = policyVersion
        if description is not None:
            record.description = description
        if policy is not None:
            record.policy = json.loads(policy) if isinstance(policy, str) else policy
        record.lastModifiedDate = int(time.time())
        return {"accessPolicyDetail": record.to_dict()}

    def delete_access_policy(self, type, name, clientToken=None, **kwargs):
        key = self._policy_key(type, name)
        if key not in self._access_policies:
            raise ResourceNotFoundException("Access policy not found: " + key)
        del self._access_policies[key]
        return {}

    # --- Security Policies ---

    def create_security_policy(self, type, name, policy, description=None,
                                clientToken=None, **kwargs):
        key = self._policy_key(type, name)
        if key in self._security_policies:
            raise ConflictException("Security policy already exists: " + key)
        record = PolicyRecord(type=type, name=name, policy=policy,
                              description=description)
        self._security_policies[key] = record
        return {"securityPolicyDetail": record.to_dict()}

    def get_security_policy(self, type, name, **kwargs):
        key = self._policy_key(type, name)
        if key not in self._security_policies:
            raise ResourceNotFoundException("Security policy not found: " + key)
        return {"securityPolicyDetail": self._security_policies[key].to_dict()}

    def list_security_policies(self, type, resource=None, **kwargs):
        items = [p.to_dict() for p in self._security_policies.values()
                 if p.type == type]
        return {"securityPolicySummaries": items}

    def update_security_policy(self, type, name, policyVersion,
                                description=None, policy=None,
                                clientToken=None, **kwargs):
        key = self._policy_key(type, name)
        if key not in self._security_policies:
            raise ResourceNotFoundException("Security policy not found: " + key)
        record = self._security_policies[key]
        record.policyVersion = policyVersion
        if description is not None:
            record.description = description
        if policy is not None:
            record.policy = json.loads(policy) if isinstance(policy, str) else policy
        record.lastModifiedDate = int(time.time())
        return {"securityPolicyDetail": record.to_dict()}

    def delete_security_policy(self, type, name, clientToken=None, **kwargs):
        key = self._policy_key(type, name)
        if key not in self._security_policies:
            raise ResourceNotFoundException("Security policy not found: " + key)
        del self._security_policies[key]
        return {}

    # --- Lifecycle Policies ---

    def create_lifecycle_policy(self, type, name, policy, description=None,
                                 clientToken=None, **kwargs):
        key = self._policy_key(type, name)
        if key in self._lifecycle_policies:
            raise ConflictException("Lifecycle policy already exists: " + key)
        record = LifecyclePolicyRecord(type=type, name=name, policy=policy,
                                       description=description)
        self._lifecycle_policies[key] = record
        return {"lifecyclePolicyDetail": record.to_dict()}

    def batch_get_lifecycle_policy(self, identifiers, **kwargs):
        result = []
        for ident in identifiers:
            t = ident.get("type", "")
            n = ident.get("name", "")
            key = self._policy_key(t, n)
            if key in self._lifecycle_policies:
                result.append(self._lifecycle_policies[key].to_dict())
        return {"lifecyclePolicyDetails": result}

    def list_lifecycle_policies(self, type, resources=None, **kwargs):
        items = [p.to_dict() for p in self._lifecycle_policies.values()
                 if p.type == type]
        return {"lifecyclePolicySummaries": items}

    def update_lifecycle_policy(self, type, name, policyVersion,
                                 description=None, policy=None,
                                 clientToken=None, **kwargs):
        key = self._policy_key(type, name)
        if key not in self._lifecycle_policies:
            raise ResourceNotFoundException("Lifecycle policy not found: " + key)
        record = self._lifecycle_policies[key]
        record.policyVersion = policyVersion
        if description is not None:
            record.description = description
        if policy is not None:
            record.policy = json.loads(policy) if isinstance(policy, str) else policy
        record.lastModifiedDate = int(time.time())
        return {"lifecyclePolicyDetail": record.to_dict()}

    def delete_lifecycle_policy(self, type, name, clientToken=None, **kwargs):
        key = self._policy_key(type, name)
        if key not in self._lifecycle_policies:
            raise ResourceNotFoundException("Lifecycle policy not found: " + key)
        del self._lifecycle_policies[key]
        return {}

    # --- Tags ---

    def tag_resource(self, resourceArn, tags, **kwargs):
        if isinstance(tags, list):
            flat = {}
            for t in tags:
                flat[t.get("key", t.get("Key", ""))] = t.get("value", t.get("Value", ""))
            self._tags[resourceArn] = flat
        else:
            self._tags[resourceArn] = dict(tags)
        return {}

    def untag_resource(self, resourceArn, tagKeys, **kwargs):
        if resourceArn in self._tags:
            for k in tagKeys:
                self._tags[resourceArn].pop(k, None)
        return {}

    def list_tags_for_resource(self, resourceArn, **kwargs):
        flat = self._tags.get(resourceArn, {})
        tags_list = [{"key": k, "value": v} for k, v in flat.items()]
        return {"tags": tags_list}
