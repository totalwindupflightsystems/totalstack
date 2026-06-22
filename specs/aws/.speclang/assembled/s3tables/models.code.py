"""S3 Tables store, records, and exception classes.

Core entities:
  - TableBucket: top-level container
  - Namespace: logical grouping within a table bucket
  - Table: Iceberg table within a namespace

Operations covered (20 of 49):
  Create/Get/Delete/ListTableBucket
  Create/Get/Delete/ListNamespace
  Create/Get/Delete/ListTables/RenameTable
  GetTableEncryption, GetTableBucketEncryption
  GetTableMaintenanceConfiguration, GetTableBucketMaintenanceConfiguration
  TagResource, UntagResource, ListTagsForResource
"""
import uuid
import time as _time
from collections import defaultdict


# ---------------------------------------------------------------------------
# Exception classes (matching botocore error shapes)
# ---------------------------------------------------------------------------

class InternalServerErrorException(Exception):
    """500-level server error."""
    pass


class ForbiddenException(Exception):
    """403 — insufficient permissions."""
    pass


class NotFoundException(Exception):
    """Resource not found."""
    pass


class AccessDeniedException(Exception):
    """Access denied."""
    pass


class TooManyRequestsException(Exception):
    """429 — rate limit."""
    pass


class ConflictException(Exception):
    """Resource already exists / conflict."""
    pass


class BadRequestException(Exception):
    """Invalid request."""
    pass


# ---------------------------------------------------------------------------
# Record classes
# ---------------------------------------------------------------------------

class TableBucketRecord:
    """Record for a table bucket."""

    def __init__(self, name, encryption_configuration=None,
                 storage_class_configuration=None, tags=None):
        self.arn = f"arn:aws:s3tables:::bucket/{name}"
        self.name = name
        self.table_bucket_id = str(uuid.uuid4())
        self.owner_account_id = "000000000000"
        self.created_at = _time.time()
        self.encryption_configuration = encryption_configuration or {}
        self.storage_class_configuration = storage_class_configuration or {}
        self.tags = tags or {}


class NamespaceRecord:
    """Record for a namespace within a table bucket."""

    def __init__(self, table_bucket_arn, namespace):
        self.table_bucket_arn = table_bucket_arn
        self.namespace_name = namespace
        self.namespace_id = str(uuid.uuid4())
        self.owner_account_id = "000000000000"
        self.created_by = "000000000000"
        self.created_at = _time.time()


class TableRecord:
    """Record for an Iceberg table within a namespace."""

    def __init__(self, table_bucket_arn, namespace, name, format="ICEBERG",
                 encryption_configuration=None, table_type="customer"):
        self.table_bucket_arn = table_bucket_arn
        self.namespace = namespace
        self.name = name
        self.table_id = str(uuid.uuid4())
        self.format = format
        self.table_type = table_type
        self.encryption_configuration = encryption_configuration or {}
        self.created_at = _time.time()
        self.metadata_location = None


# ---------------------------------------------------------------------------
# Store
# ---------------------------------------------------------------------------

class S3TablesStore:
    """In-memory store for S3 Tables."""

    def __init__(self):
        self._buckets: dict[str, TableBucketRecord] = {}
        self._namespaces: dict[str, dict[str, NamespaceRecord]] = defaultdict(dict)
        self._tables: dict[str, dict[str, TableRecord]] = defaultdict(dict)
        self._tags: dict[str, dict[str, str]] = defaultdict(dict)
        self._encryption: dict[str, dict] = {}
        self._maintenance: dict[str, dict] = {}

    # -- Table Bucket operations --

    def create_table_bucket(self, name, encryptionConfiguration=None,
                            storageClassConfiguration=None, tags=None):
        if name in self._buckets:
            raise ConflictException(f"Table bucket '{name}' already exists")
        record = TableBucketRecord(
            name=name,
            encryption_configuration=encryptionConfiguration,
            storage_class_configuration=storageClassConfiguration,
            tags=tags,
        )
        self._buckets[name] = record
        if tags:
            # Convert list of {key, value} dicts to flat dict
            if isinstance(tags, list):
                tag_dict = {}
                for t in tags:
                    tag_dict[t.get("key", t.get("Key", ""))] = t.get("value", t.get("Value", ""))
                self._tags[record.arn] = tag_dict
            else:
                self._tags[record.arn] = dict(tags)
        if encryptionConfiguration:
            self._encryption[record.arn] = encryptionConfiguration
        return {"arn": record.arn}

    def get_table_bucket(self, tableBucketARN):
        for rec in self._buckets.values():
            if rec.arn == tableBucketARN:
                return {
                    "arn": rec.arn,
                    "name": rec.name,
                    "ownerAccountId": rec.owner_account_id,
                    "createdAt": rec.created_at,
                    "tableBucketId": rec.table_bucket_id,
                    "type": "customer",
                }
        raise NotFoundException(f"Table bucket not found: {tableBucketARN}")

    def delete_table_bucket(self, tableBucketARN):
        for key, rec in list(self._buckets.items()):
            if rec.arn == tableBucketARN:
                del self._buckets[key]
                self._tags.pop(rec.arn, None)
                self._encryption.pop(rec.arn, None)
                self._namespaces.pop(rec.arn, None)
                self._tables.pop(rec.arn, None)
                return {}
        raise NotFoundException(f"Table bucket not found: {tableBucketARN}")

    def list_table_buckets(self, prefix=None, continuationToken=None,
                           maxBuckets=None, type=None):
        buckets = list(self._buckets.values())
        if prefix:
            buckets = [b for b in buckets if b.name.startswith(prefix)]
        if maxBuckets:
            buckets = buckets[:maxBuckets]
        summaries = []
        for b in buckets:
            summaries.append({
                "arn": b.arn,
                "name": b.name,
                "createdAt": b.created_at,
            })
        return {"tableBuckets": summaries}

    # -- Namespace operations --

    def create_namespace(self, tableBucketARN, namespace):
        self._get_bucket_by_arn(tableBucketARN)
        if isinstance(namespace, list):
            namespaces = namespace
        else:
            namespaces = [namespace]
        created = []
        for ns in namespaces:
            if ns in self._namespaces.get(tableBucketARN, {}):
                raise ConflictException(
                    f"Namespace '{ns}' already exists in {tableBucketARN}")
            rec = NamespaceRecord(tableBucketARN, ns)
            self._namespaces[tableBucketARN][ns] = rec
            created.append(ns)
        return {
            "tableBucketARN": tableBucketARN,
            "namespace": created,
        }

    def get_namespace(self, tableBucketARN, namespace):
        ns_map = self._namespaces.get(tableBucketARN, {})
        if namespace not in ns_map:
            raise NotFoundException(
                f"Namespace '{namespace}' not found in {tableBucketARN}")
        rec = ns_map[namespace]
        return {
            "namespace": [rec.namespace_name],
            "createdAt": rec.created_at,
            "createdBy": rec.created_by,
            "ownerAccountId": rec.owner_account_id,
            "namespaceId": rec.namespace_id,
            "tableBucketId": "bucket-id",
        }

    def delete_namespace(self, tableBucketARN, namespace):
        ns_map = self._namespaces.get(tableBucketARN, {})
        if namespace not in ns_map:
            raise NotFoundException(
                f"Namespace '{namespace}' not found in {tableBucketARN}")
        del ns_map[namespace]
        return {}

    def list_namespaces(self, tableBucketARN, prefix=None,
                        continuationToken=None, maxNamespaces=None):
        self._get_bucket_by_arn(tableBucketARN)
        ns_map = self._namespaces.get(tableBucketARN, {})
        namespaces = list(ns_map.values())
        if prefix:
            namespaces = [n for n in namespaces if n.namespace_name.startswith(prefix)]
        if maxNamespaces:
            namespaces = namespaces[:maxNamespaces]
        summaries = []
        for n in namespaces:
            summaries.append({
                "namespace": [n.namespace_name],
                "createdAt": n.created_at,
            })
        return {"namespaces": summaries}

    # -- Table operations --

    def create_table(self, tableBucketARN, namespace, name, format="ICEBERG",
                     encryptionConfiguration=None, tableType="customer"):
        self._get_bucket_by_arn(tableBucketARN)
        ns_map = self._namespaces.get(tableBucketARN, {})
        if namespace not in ns_map:
            raise NotFoundException(
                f"Namespace '{namespace}' not found in {tableBucketARN}")
        table_key = f"{namespace}/{name}"
        table_map = self._tables.get(tableBucketARN, {})
        if table_key in table_map:
            raise ConflictException(
                f"Table '{name}' already exists in namespace '{namespace}'")
        rec = TableRecord(
            table_bucket_arn=tableBucketARN,
            namespace=namespace,
            name=name,
            format=format,
            encryption_configuration=encryptionConfiguration,
            table_type=tableType,
        )
        if tableBucketARN not in self._tables:
            self._tables[tableBucketARN] = {}
        self._tables[tableBucketARN][table_key] = rec
        return {
            "name": name,
            "tableType": rec.table_type,
            "format": rec.format,
            "tableARN": f"{tableBucketARN}/table/{namespace}/{name}",
        }

    def get_table(self, tableBucketARN, namespace, name):
        table_map = self._tables.get(tableBucketARN, {})
        table_key = f"{namespace}/{name}"
        if table_key not in table_map:
            raise NotFoundException(
                f"Table '{name}' not found in namespace '{namespace}'")
        rec = table_map[table_key]
        return {
            "name": rec.name,
            "format": rec.format,
            "tableType": rec.table_type,
            "namespace": [rec.namespace],
            "tableARN": f"{tableBucketARN}/table/{namespace}/{name}",
            "createdAt": rec.created_at,
        }

    def delete_table(self, tableBucketARN, namespace, name):
        table_map = self._tables.get(tableBucketARN, {})
        table_key = f"{namespace}/{name}"
        if table_key not in table_map:
            raise NotFoundException(
                f"Table '{name}' not found in namespace '{namespace}'")
        del table_map[table_key]
        return {}

    def list_tables(self, tableBucketARN, namespace, prefix=None,
                    continuationToken=None, maxTables=None):
        self._get_bucket_by_arn(tableBucketARN)
        table_map = self._tables.get(tableBucketARN, {})
        tables = [t for t in table_map.values() if t.namespace == namespace]
        if prefix:
            tables = [t for t in tables if t.name.startswith(prefix)]
        if maxTables:
            tables = tables[:maxTables]
        summaries = []
        for t in tables:
            summaries.append({
                "name": t.name,
                "namespace": [t.namespace],
                "format": t.format,
                "tableType": t.table_type,
            })
        return {"tables": summaries}

    def rename_table(self, tableBucketARN, namespace, name, newName):
        table_map = self._tables.get(tableBucketARN, {})
        table_key = f"{namespace}/{name}"
        if table_key not in table_map:
            raise NotFoundException(
                f"Table '{name}' not found in namespace '{namespace}'")
        new_key = f"{namespace}/{newName}"
        if new_key in table_map:
            raise ConflictException(
                f"Table '{newName}' already exists in namespace '{namespace}'")
        rec = table_map.pop(table_key)
        rec.name = newName
        table_map[new_key] = rec
        return {"name": newName}

    # -- Encryption operations --

    def get_table_encryption(self, tableBucketARN, namespace, name):
        self.get_table(tableBucketARN, namespace, name)
        arn = f"{tableBucketARN}/table/{namespace}/{name}"
        return self._encryption.get(arn, {})

    def get_table_bucket_encryption(self, tableBucketARN):
        self._get_bucket_by_arn(tableBucketARN)
        return self._encryption.get(tableBucketARN, {})

    # -- Maintenance configuration operations --

    def get_table_maintenance_configuration(self, tableBucketARN, namespace, name):
        self.get_table(tableBucketARN, namespace, name)
        arn = f"{tableBucketARN}/table/{namespace}/{name}"
        return self._maintenance.get(arn, {})

    def get_table_bucket_maintenance_configuration(self, tableBucketARN):
        self._get_bucket_by_arn(tableBucketARN)
        return self._maintenance.get(tableBucketARN, {})

    # -- Tag operations --

    def tag_resource(self, resourceArn, tags):
        if isinstance(tags, list):
            tag_dict = {}
            for t in tags:
                tag_dict[t.get("key", t.get("Key", ""))] = t.get("value", t.get("Value", ""))
            tags = tag_dict
        self._tags.setdefault(resourceArn, {}).update(tags)
        return {}

    def untag_resource(self, resourceArn, tagKeys):
        tag_map = self._tags.get(resourceArn, {})
        for key in tagKeys:
            tag_map.pop(key, None)
        return {}

    def list_tags_for_resource(self, resourceArn):
        tag_map = self._tags.get(resourceArn, {})
        tags_list = [{"key": k, "value": v} for k, v in tag_map.items()]
        return {"tags": tags_list}

    # -- Helpers --

    def _get_bucket_by_arn(self, arn):
        for rec in self._buckets.values():
            if rec.arn == arn:
                return rec
        raise NotFoundException(f"Table bucket not found: {arn}")
