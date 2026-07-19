"""Verified Permissions store — PolicyStore, Policy, PolicyTemplate, IdentitySource, Tags, Schema."""
import uuid


class InvalidRequestException(Exception):
    pass


class ResourceNotFoundException(InvalidRequestException):
    pass


class ConflictException(InvalidRequestException):
    pass


class ValidationException(InvalidRequestException):
    pass


def _convert_tags(tags):
    if not tags:
        return {}
    if isinstance(tags, dict):
        return tags
    if isinstance(tags, list):
        return {t.get("Key", t.get("key", "")): t.get("Value", t.get("value", "")) for t in tags}
    return {}


class PolicyStoreRecord:
    def __init__(self, ValidationSettings, Description=None, Tags=None):
        self.PolicyStoreId = f"PStore-{uuid.uuid4().hex[:8]}"
        self.Arn = f"arn:aws:verifiedpermissions::000000000000:policy-store/{self.PolicyStoreId}"
        self.ValidationSettings = ValidationSettings or {}
        self.Description = Description or ""
        self.Tags = _convert_tags(Tags)
        self.Schema = None

    def to_dict(self):
        return {
            "policyStoreId": self.PolicyStoreId,
            "arn": self.Arn,
            "description": self.Description,
            "createdDate": "2024-01-01T00:00:00Z",
            "lastUpdatedDate": "2024-01-01T00:00:00Z",
            "validationSettings": self.ValidationSettings,
        }


class PolicyRecord:
    def __init__(self, PolicyStoreId, Definition, Tags=None):
        self.PolicyId = f"Policy-{uuid.uuid4().hex[:8]}"
        self.PolicyStoreId = PolicyStoreId
        self.Definition = Definition or {}
        self.Tags = _convert_tags(Tags)
        self.PolicyType = Definition.get("Static", {}).get("Statement") and "STATIC" or "TEMPLATE_LINKED"

    def to_dict(self):
        return {
            "policyId": self.PolicyId,
            "policyStoreId": self.PolicyStoreId,
            "policyType": self.PolicyType,
            "definition": self.Definition,
            "createdDate": "2024-01-01T00:00:00Z",
            "lastUpdatedDate": "2024-01-01T00:00:00Z",
        }


class IdentitySourceRecord:
    def __init__(self, PolicyStoreId, Configuration, PrincipalEntityType=None, Tags=None):
        self.IdentitySourceId = f"IS-{uuid.uuid4().hex[:8]}"
        self.PolicyStoreId = PolicyStoreId
        self.Configuration = Configuration or {}
        self.PrincipalEntityType = PrincipalEntityType or ""
        self.Tags = _convert_tags(Tags)

    def to_dict(self):
        return {
            "identitySourceId": self.IdentitySourceId,
            "policyStoreId": self.PolicyStoreId,
            "principalEntityType": self.PrincipalEntityType,
            "configuration": self.Configuration,
            "createdDate": "2024-01-01T00:00:00Z",
            "lastUpdatedDate": "2024-01-01T00:00:00Z",
        }


class VerifiedPermissionsStore:
    def __init__(self):
        self._policystores = {}
        self._policies = {}
        self._identitysources = {}

    # === PolicyStore ===
    def create_policy_store(self, ValidationSettings, Description=None, Tags=None):
        rec = PolicyStoreRecord(ValidationSettings=ValidationSettings,
                                Description=Description, Tags=Tags)
        self._policystores[rec.PolicyStoreId] = rec
        return {"policyStoreId": rec.PolicyStoreId, "arn": rec.Arn,
                "createdDate": "2024-01-01T00:00:00Z",
                "lastUpdatedDate": "2024-01-01T00:00:00Z"}

    def get_policy_store(self, PolicyStoreId):
        rec = self._policystores.get(PolicyStoreId)
        if not rec:
            raise ResourceNotFoundException(f"PolicyStore {PolicyStoreId} not found")
        return rec.to_dict()

    def list_policy_stores(self, MaxResults=None, NextToken=None):
        ids = list(self._policystores.keys())
        return {"policyStores": [{"policyStoreId": i, "arn": self._policystores[i].Arn} for i in ids]}

    def delete_policy_store(self, PolicyStoreId):
        if PolicyStoreId not in self._policystores:
            raise ResourceNotFoundException(f"PolicyStore {PolicyStoreId} not found")
        del self._policystores[PolicyStoreId]
        return {}

    def put_schema(self, PolicyStoreId, Definition):
        rec = self._policystores.get(PolicyStoreId)
        if not rec:
            raise ResourceNotFoundException(f"PolicyStore {PolicyStoreId} not found")
        rec.Schema = Definition
        return {"policyStoreId": PolicyStoreId,
                "namespaces": [],
                "createdDate": "2024-01-01T00:00:00Z",
                "lastUpdatedDate": "2024-01-01T00:00:00Z"}

    def get_schema(self, PolicyStoreId):
        rec = self._policystores.get(PolicyStoreId)
        if not rec:
            raise ResourceNotFoundException(f"PolicyStore {PolicyStoreId} not found")
        import json as _json
        schema_raw = rec.Schema or {}
        schema_str = _json.dumps(schema_raw) if isinstance(schema_raw, dict) else str(schema_raw)
        return {"policyStoreId": PolicyStoreId, "schema": schema_str,
                "createdDate": "2024-01-01T00:00:00Z", "lastUpdatedDate": "2024-01-01T00:00:00Z"}

    # === Policy ===
    def create_policy(self, PolicyStoreId, Definition, Tags=None):
        if PolicyStoreId not in self._policystores:
            raise ResourceNotFoundException(f"PolicyStore {PolicyStoreId} not found")
        rec = PolicyRecord(PolicyStoreId=PolicyStoreId, Definition=Definition, Tags=Tags)
        self._policies[rec.PolicyId] = rec
        return {"policyId": rec.PolicyId, "policyStoreId": PolicyStoreId,
                "policyType": rec.PolicyType,
                "createdDate": "2024-01-01T00:00:00Z",
                "lastUpdatedDate": "2024-01-01T00:00:00Z"}

    def get_policy(self, PolicyStoreId, PolicyId):
        rec = self._policies.get(PolicyId)
        if not rec or rec.PolicyStoreId != PolicyStoreId:
            raise ResourceNotFoundException(f"Policy {PolicyId} not found")
        return rec.to_dict()

    def list_policies(self, PolicyStoreId, MaxResults=None, NextToken=None):
        pols = [p for p in self._policies.values() if p.PolicyStoreId == PolicyStoreId]
        return {"policies": [{"policyId": p.PolicyId, "policyType": p.PolicyType} for p in pols]}

    def delete_policy(self, PolicyStoreId, PolicyId):
        rec = self._policies.get(PolicyId)
        if not rec or rec.PolicyStoreId != PolicyStoreId:
            raise ResourceNotFoundException(f"Policy {PolicyId} not found")
        del self._policies[PolicyId]
        return {}

    # === IdentitySource ===
    def create_identity_source(self, PolicyStoreId, Configuration,
                               PrincipalEntityType=None, Tags=None):
        if PolicyStoreId not in self._policystores:
            raise ResourceNotFoundException(f"PolicyStore {PolicyStoreId} not found")
        rec = IdentitySourceRecord(PolicyStoreId=PolicyStoreId,
                                   Configuration=Configuration,
                                   PrincipalEntityType=PrincipalEntityType,
                                   Tags=Tags)
        self._identitysources[rec.IdentitySourceId] = rec
        return {"identitySourceId": rec.IdentitySourceId, "policyStoreId": PolicyStoreId,
                "createdDate": "2024-01-01T00:00:00Z",
                "lastUpdatedDate": "2024-01-01T00:00:00Z"}

    def get_identity_source(self, PolicyStoreId, IdentitySourceId):
        rec = self._identitysources.get(IdentitySourceId)
        if not rec or rec.PolicyStoreId != PolicyStoreId:
            raise ResourceNotFoundException(f"IdentitySource {IdentitySourceId} not found")
        return rec.to_dict()

    def list_identity_sources(self, PolicyStoreId, MaxResults=None, NextToken=None):
        sources = [s for s in self._identitysources.values()
                   if s.PolicyStoreId == PolicyStoreId]
        return {"identitySources": [
            {"identitySourceId": s.IdentitySourceId} for s in sources
        ]}

    def delete_identity_source(self, PolicyStoreId, IdentitySourceId):
        rec = self._identitysources.get(IdentitySourceId)
        if not rec or rec.PolicyStoreId != PolicyStoreId:
            raise ResourceNotFoundException(f"IdentitySource {IdentitySourceId} not found")
        del self._identitysources[IdentitySourceId]
        return {}

    # === IsAuthorized ===
    def is_authorized(self, PolicyStoreId, Principal, Action, Resource, Context=None):
        if PolicyStoreId not in self._policystores:
            raise ResourceNotFoundException(f"PolicyStore {PolicyStoreId} not found")
        return {"decision": "ALLOW", "determiningPolicies": [], "errors": []}

    # === Tags ===
    def tag_resource(self, ResourceArn, Tags):
        tag_dict = _convert_tags(Tags)
        for col in [self._policystores, self._policies, self._identitysources]:
            for rid, rec in col.items():
                if getattr(rec, "Arn", "") == ResourceArn:
                    existing = getattr(rec, "Tags", {})
                    existing.update(tag_dict)
                    return {}
        raise ResourceNotFoundException(f"Resource {ResourceArn} not found")

    def list_tags_for_resource(self, ResourceArn):
        for col in [self._policystores, self._policies, self._identitysources]:
            for rid, rec in col.items():
                if getattr(rec, "Arn", "") == ResourceArn:
                    tags = getattr(rec, "Tags", {})
                    tag_list = [{"Key": k, "Value": v} for k, v in tags.items()]
                    return {"tags": tag_list}
        raise ResourceNotFoundException(f"Resource {ResourceArn} not found")
