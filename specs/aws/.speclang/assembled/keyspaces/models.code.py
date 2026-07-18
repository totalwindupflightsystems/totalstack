"""Keyspaces Store — Cassandra CQL 3.11 compatible.

Entities: Keyspace, Table, Type.
Store methods accept CamelCase kwargs matching AWS API.
"""

import time as _time


class KeyspacesException(Exception):
    """Base."""


class ConflictException(KeyspacesException):
    """Resource already exists."""


class ResourceNotFoundException(KeyspacesException):
    """Resource not found."""


class ServiceQuotaExceededException(KeyspacesException):
    """Quota exceeded."""


class ValidationException(KeyspacesException):
    """Validation error."""


class InternalServerException(KeyspacesException):
    """Internal error."""


class AccessDeniedException(KeyspacesException):
    """Access denied."""


class KeyspaceRecord:
    def __init__(self, keyspaceName, tags=None, replicationSpecification=None, **kw):
        self.keyspaceName = keyspaceName
        self.resourceArn = f"arn:aws:cassandra:us-east-1:000000000000:/keyspace/{keyspaceName}"
        self.replicationSpecification = replicationSpecification or {
            "replicationStrategy": "SINGLE_REGION"}

    def to_dict(self):
        rs = self.replicationSpecification or {}
        return {
            "keyspaceName": self.keyspaceName,
            "resourceArn": self.resourceArn,
            "replicationStrategy": rs.get("replicationStrategy", "SINGLE_REGION"),
            "replicationRegions": rs.get("replicationRegions", []),
        }


class TableRecord:
    def __init__(self, keyspaceName, tableName, schemaDefinition,
                 comment=None, clientSideTimestamps=None,
                 defaultTimeToLive=None, encryptionSpecification=None,
                 pointInTimeRecovery=None, ttl=None,
                 capacitySpecification=None, tags=None, **kw):
        self.tableName = tableName
        self.keyspaceName = keyspaceName
        self.schemaDefinition = schemaDefinition
        self.comment = comment or {}
        self.defaultTimeToLive = defaultTimeToLive
        self.clientSideTimestamps = clientSideTimestamps
        self.encryptionSpecification = encryptionSpecification
        self.pointInTimeRecovery = pointInTimeRecovery
        self.ttl = ttl
        self.capacitySpecification = capacitySpecification
        self.status = "ACTIVE"
        self.resourceArn = f"arn:aws:cassandra:us-east-1:000000000000:/keyspace/{keyspaceName}/table/{tableName}"

    def to_dict(self):
        return {
            "tableName": self.tableName,
            "keyspaceName": self.keyspaceName,
            "resourceArn": self.resourceArn,
            "schemaDefinition": self.schemaDefinition,
            "status": self.status,
            "comment": self.comment,
            "defaultTimeToLive": self.defaultTimeToLive,
            "creationTimestamp": _time.time(),
            "capacitySpecification": self.capacitySpecification,
            "encryptionSpecification": self.encryptionSpecification,
            "pointInTimeRecovery": self.pointInTimeRecovery,
            "ttl": self.ttl,
            "clientSideTimestamps": self.clientSideTimestamps,
        }


class TypeRecord:
    def __init__(self, keyspaceName, typeName, fieldDefinitions, **kw):
        self.typeName = typeName
        self.keyspaceName = keyspaceName
        self.fieldDefinitions = fieldDefinitions
        self.status = "ACTIVE"
        self.keyspaceArn = f"arn:aws:cassandra:us-east-1:000000000000:/keyspace/{keyspaceName}"
        self.lastModifiedTimestamp = _time.time()
        self.directReferringTables = []
        self.directParentTypes = []
        self.maxNestingDepth = 1

    def to_dict(self):
        return {
            "typeName": self.typeName,
            "keyspaceName": self.keyspaceName,
            "keyspaceArn": self.keyspaceArn,
            "fieldDefinitions": self.fieldDefinitions,
            "status": self.status,
            "lastModifiedTimestamp": self.lastModifiedTimestamp,
            "directReferringTables": self.directReferringTables,
            "directParentTypes": self.directParentTypes,
            "maxNestingDepth": self.maxNestingDepth,
        }


class KeyspacesStore:
    def __init__(self):
        self._keyspaces: dict[str, KeyspaceRecord] = {}
        self._tables: dict[str, TableRecord] = {}
        self._types: dict[str, TypeRecord] = {}
        self._tags: dict[str, dict] = {}

    def _table_key(self, ks, tn):
        return f"{ks}/{tn}"

    # ── Keyspaces ─────────────────────────────────────────────

    def create_keyspace(self, keyspaceName, **kwargs):
        if keyspaceName in self._keyspaces:
            raise ConflictException(f"Keyspace '{keyspaceName}' already exists")
        rec = KeyspaceRecord(keyspaceName=keyspaceName, **kwargs)
        self._keyspaces[keyspaceName] = rec
        return rec.to_dict()

    def get_keyspace(self, keyspaceName, **kwargs):
        if keyspaceName not in self._keyspaces:
            raise ResourceNotFoundException(f"Keyspace '{keyspaceName}' not found")
        return self._keyspaces[keyspaceName].to_dict()

    def list_keyspaces(self, **kwargs):
        return {"keyspaces": [k.to_dict() for k in self._keyspaces.values()]}

    def delete_keyspace(self, keyspaceName, **kwargs):
        if keyspaceName not in self._keyspaces:
            raise ResourceNotFoundException(f"Keyspace '{keyspaceName}' not found")
        del self._keyspaces[keyspaceName]
        return {}

    def update_keyspace(self, keyspaceName, **kwargs):
        if keyspaceName not in self._keyspaces:
            raise ResourceNotFoundException(f"Keyspace '{keyspaceName}' not found")
        return self._keyspaces[keyspaceName].to_dict()

    # ── Tables ────────────────────────────────────────────────

    def create_table(self, keyspaceName, tableName, schemaDefinition, **kwargs):
        key = self._table_key(keyspaceName, tableName)
        if key in self._tables:
            raise ConflictException(f"Table '{tableName}' already exists in '{keyspaceName}'")
        if keyspaceName not in self._keyspaces:
            raise ResourceNotFoundException(f"Keyspace '{keyspaceName}' not found")
        rec = TableRecord(keyspaceName=keyspaceName, tableName=tableName,
                          schemaDefinition=schemaDefinition, **kwargs)
        self._tables[key] = rec
        return rec.to_dict()

    def get_table(self, keyspaceName, tableName, **kwargs):
        key = self._table_key(keyspaceName, tableName)
        if key not in self._tables:
            raise ResourceNotFoundException(f"Table '{tableName}' not found in '{keyspaceName}'")
        return self._tables[key].to_dict()

    def list_tables(self, keyspaceName, **kwargs):
        prefix = f"{keyspaceName}/"
        tables = [t.to_dict() for k, t in self._tables.items()
                  if k.startswith(prefix)]
        return {"tables": tables}

    def delete_table(self, keyspaceName, tableName, **kwargs):
        key = self._table_key(keyspaceName, tableName)
        if key not in self._tables:
            raise ResourceNotFoundException(f"Table '{tableName}' not found in '{keyspaceName}'")
        del self._tables[key]
        return {}

    def update_table(self, keyspaceName, tableName, **kwargs):
        key = self._table_key(keyspaceName, tableName)
        if key not in self._tables:
            raise ResourceNotFoundException(f"Table '{tableName}' not found in '{keyspaceName}'")
        return self._tables[key].to_dict()

    # ── Types ─────────────────────────────────────────────────

    def create_type(self, keyspaceName, typeName, fieldDefinitions, **kwargs):
        key = f"{keyspaceName}/{typeName}"
        if key in self._types:
            raise ConflictException(f"Type '{typeName}' already exists in '{keyspaceName}'")
        rec = TypeRecord(keyspaceName=keyspaceName, typeName=typeName,
                         fieldDefinitions=fieldDefinitions, **kwargs)
        self._types[key] = rec
        return rec.to_dict()

    def get_type(self, keyspaceName, typeName, **kwargs):
        key = f"{keyspaceName}/{typeName}"
        if key not in self._types:
            raise ResourceNotFoundException(f"Type '{typeName}' not found in '{keyspaceName}'")
        return self._types[key].to_dict()

    def list_types(self, keyspaceName, **kwargs):
        prefix = f"{keyspaceName}/"
        types = [t.to_dict() for k, t in self._types.items()
                 if k.startswith(prefix)]
        return {"types": types}

    def delete_type(self, keyspaceName, typeName, **kwargs):
        key = f"{keyspaceName}/{typeName}"
        if key not in self._types:
            raise ResourceNotFoundException(f"Type '{typeName}' not found in '{keyspaceName}'")
        rec = self._types.pop(key)
        return {"keyspaceArn": rec.keyspaceArn, "typeName": rec.typeName}

    # ── Tags ──────────────────────────────────────────────────

    def tag_resource(self, resourceArn, tags, **kwargs):
        if resourceArn not in self._tags:
            self._tags[resourceArn] = {}
        for t in tags:
            self._tags[resourceArn][t["key"]] = t["value"]
        return {}

    def untag_resource(self, resourceArn, tags, **kwargs):
        if resourceArn in self._tags:
            for t in tags:
                self._tags[resourceArn].pop(t["tagKey"], None)
        return {}

    def list_tags_for_resource(self, resourceArn, **kwargs):
        result = []
        for k, v in self._tags.get(resourceArn, {}).items():
            result.append({"key": k, "value": v})
        return {"tags": result}

    # ── Auto Scaling ─────────────────────────────────────────

    def get_table_auto_scaling_settings(self, keyspaceName, tableName, **kwargs):
        key = self._table_key(keyspaceName, tableName)
        if key not in self._tables:
            raise ResourceNotFoundException(f"Table '{tableName}' not found in '{keyspaceName}'")
        table = self._tables[key]
        return {
            "keyspaceName": table.keyspaceName,
            "tableName": table.tableName,
            "resourceArn": table.resourceArn,
            "autoScalingSpecification": {},
        }
