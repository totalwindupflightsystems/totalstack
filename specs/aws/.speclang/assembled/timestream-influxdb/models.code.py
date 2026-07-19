"""Timestream for InfluxDB store — DbCluster, DbInstance, DbParameterGroup, tags."""
import uuid
import time as _time


# === Exception classes ===

class ValidationException(Exception):
    """Invalid request parameter."""

class ResourceNotFoundException(Exception):
    """Resource not found."""

class ConflictException(Exception):
    """Resource already exists."""

class InternalServerException(Exception):
    """Internal error."""

class AccessDeniedException(Exception):
    """Access denied."""

class ThrottlingException(Exception):
    """Too many requests."""

class ServiceQuotaExceededException(Exception):
    """Quota exceeded."""


# === Data classes ===

class LogDeliveryConfiguration:
    def __init__(self, s3Configuration=None):
        if isinstance(s3Configuration, dict):
            self.s3Configuration = S3Configuration(**s3Configuration)
        elif s3Configuration is not None:
            self.s3Configuration = s3Configuration
        else:
            self.s3Configuration = None

    def to_dict(self):
        result = {}
        if self.s3Configuration:
            result["s3Configuration"] = self.s3Configuration.to_dict() if hasattr(self.s3Configuration, 'to_dict') else self.s3Configuration
        return result


class S3Configuration:
    def __init__(self, bucketName=None, bucketPrefix=None):
        self.bucketName = bucketName or ""
        self.bucketPrefix = bucketPrefix or ""

    def to_dict(self):
        return {
            "bucketName": self.bucketName,
            "bucketPrefix": self.bucketPrefix,
        }


# === Record classes ===

class DbClusterRecord:
    def __init__(self, name, dbInstanceType, vpcSubnetIds, vpcSecurityGroupIds,
                 username=None, password=None, organization=None, bucket=None,
                 port=None, dbParameterGroupIdentifier=None, dbStorageType=None,
                 allocatedStorage=None, networkType=None, publiclyAccessible=None,
                 deploymentType=None, failoverMode=None, logDeliveryConfiguration=None,
                 tags=None):
        self.id = f"dbcluster-{uuid.uuid4().hex[:12]}"
        self.arn = f"arn:aws:timestream-influxdb:us-east-1:123456789012:dbcluster/{self.id}"
        self.name = name
        self.dbInstanceType = dbInstanceType
        self.vpcSubnetIds = vpcSubnetIds or []
        self.vpcSecurityGroupIds = vpcSecurityGroupIds or []
        self.username = username or "admin"
        self.password = password or ""
        self.organization = organization or ""
        self.bucket = bucket or ""
        self.port = port or 8086
        self.dbParameterGroupIdentifier = dbParameterGroupIdentifier or ""
        self.dbStorageType = dbStorageType or "InfluxIOIncludedT1"
        self.allocatedStorage = allocatedStorage or 400
        self.networkType = networkType or "IPV4"
        self.publiclyAccessible = publiclyAccessible or False
        self.deploymentType = deploymentType or "MULTI_NODE_READ_REPLICAS"
        self.failoverMode = failoverMode or "AUTOMATIC"
        if isinstance(logDeliveryConfiguration, dict):
            self.logDeliveryConfiguration = LogDeliveryConfiguration(**logDeliveryConfiguration)
        elif logDeliveryConfiguration is not None:
            self.logDeliveryConfiguration = logDeliveryConfiguration
        else:
            self.logDeliveryConfiguration = None
        self.tags = _convert_tags(tags)
        self.status = "CREATING"
        self.endpoint = ""
        self.created_time = _time.time()

    def to_dict(self):
        result = {
            "id": self.id,
            "arn": self.arn,
            "name": self.name,
            "dbInstanceType": self.dbInstanceType,
            "vpcSubnetIds": self.vpcSubnetIds,
            "vpcSecurityGroupIds": self.vpcSecurityGroupIds,
            "username": self.username,
            "organization": self.organization,
            "bucket": self.bucket,
            "port": self.port,
            "dbParameterGroupIdentifier": self.dbParameterGroupIdentifier,
            "dbStorageType": self.dbStorageType,
            "allocatedStorage": self.allocatedStorage,
            "networkType": self.networkType,
            "publiclyAccessible": self.publiclyAccessible,
            "deploymentType": self.deploymentType,
            "failoverMode": self.failoverMode,
            "status": self.status,
            "endpoint": self.endpoint,
        }
        if self.logDeliveryConfiguration:
            result["logDeliveryConfiguration"] = self.logDeliveryConfiguration.to_dict() if hasattr(self.logDeliveryConfiguration, 'to_dict') else self.logDeliveryConfiguration
        return result


class DbInstanceRecord:
    def __init__(self, name, password, dbInstanceType, vpcSubnetIds, vpcSecurityGroupIds,
                 allocatedStorage, username=None, organization=None, bucket=None,
                 publiclyAccessible=None, dbStorageType=None, dbParameterGroupIdentifier=None,
                 deploymentType=None, logDeliveryConfiguration=None, tags=None,
                 port=None, networkType=None, dbClusterId=""):
        self.id = f"dbinstance-{uuid.uuid4().hex[:12]}"
        self.arn = f"arn:aws:timestream-influxdb:us-east-1:123456789012:dbinstance/{self.id}"
        self.name = name
        self.password = password
        self.dbInstanceType = dbInstanceType
        self.vpcSubnetIds = vpcSubnetIds or []
        self.vpcSecurityGroupIds = vpcSecurityGroupIds or []
        self.allocatedStorage = allocatedStorage
        self.username = username or "admin"
        self.organization = organization or ""
        self.bucket = bucket or ""
        self.publiclyAccessible = publiclyAccessible or False
        self.dbStorageType = dbStorageType or "InfluxIOIncludedT1"
        self.dbParameterGroupIdentifier = dbParameterGroupIdentifier or ""
        self.deploymentType = deploymentType or "SINGLE_AZ"
        if isinstance(logDeliveryConfiguration, dict):
            self.logDeliveryConfiguration = LogDeliveryConfiguration(**logDeliveryConfiguration)
        elif logDeliveryConfiguration is not None:
            self.logDeliveryConfiguration = logDeliveryConfiguration
        else:
            self.logDeliveryConfiguration = None
        self.tags = _convert_tags(tags)
        self.port = port or 8086
        self.networkType = networkType or "IPV4"
        self.dbClusterId = dbClusterId
        self.status = "CREATING"
        self.endpoint = ""
        self.created_time = _time.time()

    def to_dict(self):
        result = {
            "id": self.id,
            "arn": self.arn,
            "name": self.name,
            "dbInstanceType": self.dbInstanceType,
            "vpcSubnetIds": self.vpcSubnetIds,
            "vpcSecurityGroupIds": self.vpcSecurityGroupIds,
            "allocatedStorage": self.allocatedStorage,
            "username": self.username,
            "organization": self.organization,
            "bucket": self.bucket,
            "publiclyAccessible": self.publiclyAccessible,
            "dbStorageType": self.dbStorageType,
            "dbParameterGroupIdentifier": self.dbParameterGroupIdentifier,
            "deploymentType": self.deploymentType,
            "port": self.port,
            "networkType": self.networkType,
            "dbClusterId": self.dbClusterId,
            "status": self.status,
            "endpoint": self.endpoint,
        }
        if self.logDeliveryConfiguration:
            result["logDeliveryConfiguration"] = self.logDeliveryConfiguration.to_dict() if hasattr(self.logDeliveryConfiguration, 'to_dict') else self.logDeliveryConfiguration
        return result


class DbParameterGroupRecord:
    def __init__(self, name, description=None, parameters=None, tags=None):
        self.id = f"dbparametergroup-{uuid.uuid4().hex[:12]}"
        self.arn = f"arn:aws:timestream-influxdb:us-east-1:123456789012:dbparametergroup/{self.id}"
        self.name = name
        self.description = description or ""
        self.parameters = parameters or {}
        self.tags = _convert_tags(tags)
        self.created_time = _time.time()

    def to_dict(self):
        return {
            "id": self.id,
            "arn": self.arn,
            "name": self.name,
            "description": self.description,
            "parameters": self.parameters,
        }


# === Helpers ===

def _convert_tags(tags):
    """Convert AWS tag list [{key, value}] to flat dict {key: value}."""
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


def _build_tag_list(tag_dict):
    """Convert flat dict back to AWS tag list."""
    if not tag_dict:
        return {}
    return dict(tag_dict)


# === TimestreamForInfluxDB Store ===

class TimestreamForInfluxDBStore:
    def __init__(self):
        self._clusters: dict[str, DbClusterRecord] = {}
        self._instances: dict[str, DbInstanceRecord] = {}
        self._param_groups: dict[str, DbParameterGroupRecord] = {}
        self._tags: dict[str, dict] = {}  # arn → {key: value}

    # --- DbCluster accessors ---

    def db_clusters(self, cluster_id: str = None):
        """Return a single cluster or list all."""
        if cluster_id is not None:
            return self._clusters.get(cluster_id)
        return list(self._clusters.values())

    def create_db_cluster(self, name, dbInstanceType, vpcSubnetIds, vpcSecurityGroupIds,
                          username=None, password=None, organization=None, bucket=None,
                          port=None, dbParameterGroupIdentifier=None, dbStorageType=None,
                          allocatedStorage=None, networkType=None, publiclyAccessible=None,
                          deploymentType=None, failoverMode=None, logDeliveryConfiguration=None,
                          tags=None):
        # Check for duplicate name
        for c in self._clusters.values():
            if c.name == name:
                raise ConflictException(f"DbCluster with name '{name}' already exists")

        record = DbClusterRecord(
            name=name, dbInstanceType=dbInstanceType,
            vpcSubnetIds=vpcSubnetIds, vpcSecurityGroupIds=vpcSecurityGroupIds,
            username=username, password=password, organization=organization,
            bucket=bucket, port=port,
            dbParameterGroupIdentifier=dbParameterGroupIdentifier,
            dbStorageType=dbStorageType, allocatedStorage=allocatedStorage,
            networkType=networkType, publiclyAccessible=publiclyAccessible,
            deploymentType=deploymentType, failoverMode=failoverMode,
            logDeliveryConfiguration=logDeliveryConfiguration, tags=tags)
        self._clusters[record.id] = record
        if record.tags:
            self._tags[record.arn] = dict(record.tags)
        return record.to_dict()

    def get_db_cluster(self, dbClusterId):
        record = self._clusters.get(dbClusterId)
        if not record:
            raise ResourceNotFoundException(f"DbCluster '{dbClusterId}' not found")
        return record.to_dict()

    def list_db_clusters(self, nextToken=None, maxResults=None):
        clusters = list(self._clusters.values())
        result = [c.to_dict() for c in clusters]
        return {"items": result}

    def update_db_cluster(self, dbClusterId, logDeliveryConfiguration=None,
                          dbParameterGroupIdentifier=None, port=None,
                          dbInstanceType=None, failoverMode=None):
        record = self._clusters.get(dbClusterId)
        if not record:
            raise ResourceNotFoundException(f"DbCluster '{dbClusterId}' not found")
        if logDeliveryConfiguration:
            if isinstance(logDeliveryConfiguration, dict):
                record.logDeliveryConfiguration = LogDeliveryConfiguration(**logDeliveryConfiguration)
            else:
                record.logDeliveryConfiguration = logDeliveryConfiguration
        if dbParameterGroupIdentifier:
            record.dbParameterGroupIdentifier = dbParameterGroupIdentifier
        if port:
            record.port = port
        if dbInstanceType:
            record.dbInstanceType = dbInstanceType
        if failoverMode:
            record.failoverMode = failoverMode
        return record.to_dict()

    def delete_db_cluster(self, dbClusterId):
        record = self._clusters.pop(dbClusterId, None)
        if not record:
            raise ResourceNotFoundException(f"DbCluster '{dbClusterId}' not found")
        self._tags.pop(record.arn, None)
        return record.to_dict()

    def reboot_db_cluster(self, dbClusterId, instanceIds=None):
        record = self._clusters.get(dbClusterId)
        if not record:
            raise ResourceNotFoundException(f"DbCluster '{dbClusterId}' not found")
        return record.to_dict()

    # --- DbInstance accessors ---

    def db_instances(self, instance_id: str = None):
        """Return a single instance or list all."""
        if instance_id is not None:
            return self._instances.get(instance_id)
        return list(self._instances.values())

    def create_db_instance(self, name, password, dbInstanceType, vpcSubnetIds,
                           vpcSecurityGroupIds, allocatedStorage, username=None,
                           organization=None, bucket=None, publiclyAccessible=None,
                           dbStorageType=None, dbParameterGroupIdentifier=None,
                           deploymentType=None, logDeliveryConfiguration=None, tags=None,
                           port=None, networkType=None, dbClusterId=""):
        # Check for duplicate name
        for inst in self._instances.values():
            if inst.name == name:
                raise ConflictException(f"DbInstance with name '{name}' already exists")

        record = DbInstanceRecord(
            name=name, password=password, dbInstanceType=dbInstanceType,
            vpcSubnetIds=vpcSubnetIds, vpcSecurityGroupIds=vpcSecurityGroupIds,
            allocatedStorage=allocatedStorage, username=username,
            organization=organization, bucket=bucket,
            publiclyAccessible=publiclyAccessible, dbStorageType=dbStorageType,
            dbParameterGroupIdentifier=dbParameterGroupIdentifier,
            deploymentType=deploymentType,
            logDeliveryConfiguration=logDeliveryConfiguration, tags=tags,
            port=port, networkType=networkType, dbClusterId=dbClusterId)
        self._instances[record.id] = record
        if record.tags:
            self._tags[record.arn] = dict(record.tags)
        return record.to_dict()

    def get_db_instance(self, identifier):
        record = self._instances.get(identifier)
        if not record:
            raise ResourceNotFoundException(f"DbInstance '{identifier}' not found")
        return record.to_dict()

    def list_db_instances(self, nextToken=None, maxResults=None):
        instances = list(self._instances.values())
        return {"items": [i.to_dict() for i in instances]}

    def list_db_instances_for_cluster(self, dbClusterId, nextToken=None, maxResults=None):
        instances = [i for i in self._instances.values() if i.dbClusterId == dbClusterId]
        return {"items": [i.to_dict() for i in instances]}

    def update_db_instance(self, identifier, logDeliveryConfiguration=None,
                           dbParameterGroupIdentifier=None, port=None,
                           dbInstanceType=None, deploymentType=None,
                           dbStorageType=None, allocatedStorage=None):
        record = self._instances.get(identifier)
        if not record:
            raise ResourceNotFoundException(f"DbInstance '{identifier}' not found")
        if logDeliveryConfiguration:
            if isinstance(logDeliveryConfiguration, dict):
                record.logDeliveryConfiguration = LogDeliveryConfiguration(**logDeliveryConfiguration)
            else:
                record.logDeliveryConfiguration = logDeliveryConfiguration
        if dbParameterGroupIdentifier:
            record.dbParameterGroupIdentifier = dbParameterGroupIdentifier
        if port:
            record.port = port
        if dbInstanceType:
            record.dbInstanceType = dbInstanceType
        if deploymentType:
            record.deploymentType = deploymentType
        if dbStorageType:
            record.dbStorageType = dbStorageType
        if allocatedStorage:
            record.allocatedStorage = allocatedStorage
        return record.to_dict()

    def delete_db_instance(self, identifier):
        record = self._instances.pop(identifier, None)
        if not record:
            raise ResourceNotFoundException(f"DbInstance '{identifier}' not found")
        self._tags.pop(record.arn, None)
        return record.to_dict()

    def reboot_db_instance(self, identifier):
        record = self._instances.get(identifier)
        if not record:
            raise ResourceNotFoundException(f"DbInstance '{identifier}' not found")
        return record.to_dict()

    # --- DbParameterGroup accessors ---

    def db_parameter_groups(self, group_id: str = None):
        """Return a single param group or list all."""
        if group_id is not None:
            return self._param_groups.get(group_id)
        return list(self._param_groups.values())

    def create_db_parameter_group(self, name, description=None, parameters=None, tags=None):
        for pg in self._param_groups.values():
            if pg.name == name:
                raise ConflictException(f"DbParameterGroup with name '{name}' already exists")

        record = DbParameterGroupRecord(
            name=name, description=description, parameters=parameters, tags=tags)
        self._param_groups[record.id] = record
        if record.tags:
            self._tags[record.arn] = dict(record.tags)
        return record.to_dict()

    def get_db_parameter_group(self, identifier):
        record = self._param_groups.get(identifier)
        if not record:
            raise ResourceNotFoundException(f"DbParameterGroup '{identifier}' not found")
        return record.to_dict()

    def list_db_parameter_groups(self, nextToken=None, maxResults=None):
        groups = list(self._param_groups.values())
        return {"items": [g.to_dict() for g in groups]}

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
        tag_dict = self._tags.get(resourceArn, {})
        return {"tags": dict(tag_dict)}
