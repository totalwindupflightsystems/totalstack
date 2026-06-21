# ElastiCache Store Model
# Generated for TotalStack ElastiCache emulator v1
# spec:trace: aws/elasticache/elasticache.spec.plan.md#store-design
# spec:id: @specs/aws/elasticache/models
# spec:generated: DO NOT EDIT — edit the spec instead

import uuid
import time
from collections import defaultdict

# --- Exception Classes ---

class ElastiCacheException(Exception):
    """Base exception for all ElastiCache errors."""
    def __init__(self, error_code, message, status_code=400):
        self.error_code = error_code
        self.message = message
        self.status_code = status_code
        super().__init__(f"{error_code}: {message}")

# Cache Cluster exceptions
class CacheClusterNotFoundFault(ElastiCacheException):
    def __init__(self, message="Cache cluster not found"):
        super().__init__("CacheClusterNotFoundFault", message, 404)

class CacheClusterAlreadyExistsFault(ElastiCacheException):
    def __init__(self, message="Cache cluster already exists"):
        super().__init__("CacheClusterAlreadyExistsFault", message, 409)

class InvalidCacheClusterStateFault(ElastiCacheException):
    def __init__(self, message="Invalid cache cluster state"):
        super().__init__("InvalidCacheClusterStateFault", message, 409)

class InsufficientCacheClusterCapacityFault(ElastiCacheException):
    def __init__(self, message="Insufficient cache cluster capacity"):
        super().__init__("InsufficientCacheClusterCapacityFault", message, 503)

class NodeQuotaForClusterExceeded(ElastiCacheException):
    def __init__(self, message="Node quota exceeded for cluster"):
        super().__init__("NodeQuotaForClusterExceeded", message, 400)

# Replication Group exceptions
class ReplicationGroupNotFoundFault(ElastiCacheException):
    def __init__(self, message="Replication group not found"):
        super().__init__("ReplicationGroupNotFoundFault", message, 404)

class ReplicationGroupAlreadyExistsFault(ElastiCacheException):
    def __init__(self, message="Replication group already exists"):
        super().__init__("ReplicationGroupAlreadyExistsFault", message, 409)

class InvalidReplicationGroupStateFault(ElastiCacheException):
    def __init__(self, message="Invalid replication group state"):
        super().__init__("InvalidReplicationGroupStateFault", message, 409)

# Parameter Group exceptions
class CacheParameterGroupNotFoundFault(ElastiCacheException):
    def __init__(self, message="Cache parameter group not found"):
        super().__init__("CacheParameterGroupNotFoundFault", message, 404)

class CacheParameterGroupAlreadyExistsFault(ElastiCacheException):
    def __init__(self, message="Cache parameter group already exists"):
        super().__init__("CacheParameterGroupAlreadyExistsFault", message, 409)

class InvalidCacheParameterGroupStateFault(ElastiCacheException):
    def __init__(self, message="Invalid cache parameter group state"):
        super().__init__("InvalidCacheParameterGroupStateFault", message, 409)

class CacheParameterGroupQuotaExceededFault(ElastiCacheException):
    def __init__(self, message="Cache parameter group quota exceeded"):
        super().__init__("CacheParameterGroupQuotaExceededFault", message, 400)

# Subnet Group exceptions
class CacheSubnetGroupNotFoundFault(ElastiCacheException):
    def __init__(self, message="Cache subnet group not found"):
        super().__init__("CacheSubnetGroupNotFoundFault", message, 404)

class CacheSubnetGroupAlreadyExistsFault(ElastiCacheException):
    def __init__(self, message="Cache subnet group already exists"):
        super().__init__("CacheSubnetGroupAlreadyExistsFault", message, 409)

class CacheSubnetGroupQuotaExceededFault(ElastiCacheException):
    def __init__(self, message="Cache subnet group quota exceeded"):
        super().__init__("CacheSubnetGroupQuotaExceededFault", message, 400)

class CacheSubnetQuotaExceededFault(ElastiCacheException):
    def __init__(self, message="Cache subnet quota exceeded"):
        super().__init__("CacheSubnetQuotaExceededFault", message, 400)

class CacheSubnetGroupInUse(ElastiCacheException):
    def __init__(self, message="Cache subnet group in use"):
        super().__init__("CacheSubnetGroupInUse", message, 409)

# Snapshot exceptions
class SnapshotNotFoundFault(ElastiCacheException):
    def __init__(self, message="Snapshot not found"):
        super().__init__("SnapshotNotFoundFault", message, 404)

class SnapshotAlreadyExistsFault(ElastiCacheException):
    def __init__(self, message="Snapshot already exists"):
        super().__init__("SnapshotAlreadyExistsFault", message, 409)

class InvalidSnapshotStateFault(ElastiCacheException):
    def __init__(self, message="Invalid snapshot state"):
        super().__init__("InvalidSnapshotStateFault", message, 409)

# User exceptions
class UserNotFoundFault(ElastiCacheException):
    def __init__(self, message="User not found"):
        super().__init__("UserNotFoundFault", message, 404)

class UserAlreadyExistsFault(ElastiCacheException):
    def __init__(self, message="User already exists"):
        super().__init__("UserAlreadyExistsFault", message, 409)

class InvalidUserStateFault(ElastiCacheException):
    def __init__(self, message="Invalid user state"):
        super().__init__("InvalidUserStateFault", message, 409)

class DuplicateUserNameFault(ElastiCacheException):
    def __init__(self, message="Duplicate user name"):
        super().__init__("DuplicateUserNameFault", message, 409)

class UserQuotaExceededFault(ElastiCacheException):
    def __init__(self, message="User quota exceeded"):
        super().__init__("UserQuotaExceededFault", message, 400)

# User Group exceptions
class UserGroupNotFoundFault(ElastiCacheException):
    def __init__(self, message="User group not found"):
        super().__init__("UserGroupNotFoundFault", message, 404)

class UserGroupAlreadyExistsFault(ElastiCacheException):
    def __init__(self, message="User group already exists"):
        super().__init__("UserGroupAlreadyExistsFault", message, 409)

class InvalidUserGroupStateFault(ElastiCacheException):
    def __init__(self, message="Invalid user group state"):
        super().__init__("InvalidUserGroupStateFault", message, 409)

class DefaultUserRequired(ElastiCacheException):
    def __init__(self, message="Default user is required"):
        super().__init__("DefaultUserRequired", message, 400)

# General exceptions
class InvalidParameterValueException(ElastiCacheException):
    def __init__(self, message="Invalid parameter value"):
        super().__init__("InvalidParameterValueException", message, 400)

class InvalidParameterCombinationException(ElastiCacheException):
    def __init__(self, message="Invalid parameter combination"):
        super().__init__("InvalidParameterCombinationException", message, 400)

class TagQuotaPerResourceExceeded(ElastiCacheException):
    def __init__(self, message="Tag quota per resource exceeded"):
        super().__init__("TagQuotaPerResourceExceeded", message, 400)

class ServiceLinkedRoleNotFoundFault(ElastiCacheException):
    def __init__(self, message="Service linked role not found"):
        super().__init__("ServiceLinkedRoleNotFoundFault", message, 400)

class InvalidARNFault(ElastiCacheException):
    def __init__(self, message="Invalid ARN"):
        super().__init__("InvalidARNFault", message, 400)

class SnapshotFeatureNotSupportedFault(ElastiCacheException):
    def __init__(self, message="Snapshot feature not supported"):
        super().__init__("SnapshotFeatureNotSupportedFault", message, 400)

class SnapshotQuotaExceededFault(ElastiCacheException):
    def __init__(self, message="Snapshot quota exceeded"):
        super().__init__("SnapshotQuotaExceededFault", message, 400)

# Cache Security Group exceptions (for tag operations that reference them)
class CacheSecurityGroupNotFoundFault(ElastiCacheException):
    def __init__(self, message="Cache security group not found"):
        super().__init__("CacheSecurityGroupNotFoundFault", message, 404)

class ReservedCacheNodeNotFoundFault(ElastiCacheException):
    def __init__(self, message="Reserved cache node not found"):
        super().__init__("ReservedCacheNodeNotFoundFault", message, 404)

class ServerlessCacheNotFoundFault(ElastiCacheException):
    def __init__(self, message="Serverless cache not found"):
        super().__init__("ServerlessCacheNotFoundFault", message, 404)

class ServerlessCacheSnapshotNotFoundFault(ElastiCacheException):
    def __init__(self, message="Serverless cache snapshot not found"):
        super().__init__("ServerlessCacheSnapshotNotFoundFault", message, 404)

class InvalidServerlessCacheStateFault(ElastiCacheException):
    def __init__(self, message="Invalid serverless cache state"):
        super().__init__("InvalidServerlessCacheStateFault", message, 409)

class InvalidServerlessCacheSnapshotStateFault(ElastiCacheException):
    def __init__(self, message="Invalid serverless cache snapshot state"):
        super().__init__("InvalidServerlessCacheSnapshotStateFault", message, 409)

class InvalidSubnet(ElastiCacheException):
    def __init__(self, message="Invalid subnet"):
        super().__init__("InvalidSubnet", message, 400)

class SubnetInUse(ElastiCacheException):
    def __init__(self, message="Subnet in use"):
        super().__init__("SubnetInUse", message, 409)

class SubnetNotAllowedFault(ElastiCacheException):
    def __init__(self, message="Subnet not allowed"):
        super().__init__("SubnetNotAllowedFault", message, 400)

class InvalidGlobalReplicationGroupStateFault(ElastiCacheException):
    def __init__(self, message="Invalid global replication group state"):
        super().__init__("InvalidGlobalReplicationGroupStateFault", message, 409)

class DefaultUserAssociatedToUserGroupFault(ElastiCacheException):
    def __init__(self, message="Default user associated to user group"):
        super().__init__("DefaultUserAssociatedToUserGroupFault", message, 409)

# --- Store Class ---

class ElastiCacheStore:
    """In-memory store for ElastiCache resources."""
    
    def __init__(self):
        self.cache_clusters = {}
        self.replication_groups = {}
        self.parameter_groups = {}
        self.subnet_groups = {}
        self.snapshots = {}
        self.users = {}
        self.user_groups = {}
        self.events = []
        self.tags = defaultdict(list)
    
    def reset(self):
        """Reset all stores (useful for test isolation)."""
        self.cache_clusters.clear()
        self.replication_groups.clear()
        self.parameter_groups.clear()
        self.subnet_groups.clear()
        self.snapshots.clear()
        self.users.clear()
        self.user_groups.clear()
        self.events.clear()
        self.tags.clear()
