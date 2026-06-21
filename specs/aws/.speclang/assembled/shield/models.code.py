"""Shield service store — Protection, ProtectionGroup, Subscription, DRT configuration."""
from dataclasses import dataclass, field

# ── Exception classes (matching AWS error codes) ──────────────────────

class InternalErrorException(Exception):
    """Problem with the service infrastructure. Retry the request."""

class InvalidOperationException(Exception):
    """Operation would not cause any change to occur."""

class InvalidParameterException(Exception):
    """Parameters passed to the API are invalid."""

class InvalidPaginationTokenException(Exception):
    """Pagination token is invalid."""

class InvalidResourceException(Exception):
    """Resource is not valid for this operation."""

class LimitsExceededException(Exception):
    """Operation would exceed a limit."""

class NoAssociatedRoleException(Exception):
    """ARN of the role does not exist."""

class AccessDeniedForDependencyException(Exception):
    """User did not have iam:PassRole permission."""

class OptimisticLockException(Exception):
    """Resource state has been modified by another client."""

class ResourceNotFoundException(Exception):
    """Specified resource does not exist."""

class AccessDeniedException(Exception):
    """User does not have sufficient access."""

class LockedSubscriptionException(Exception):
    """Subscription is locked and cannot be modified."""

class ResourceAlreadyExistsException(Exception):
    """Resource with the same name/ID already exists."""


# ── Data records ──────────────────────────────────────────────────────

@dataclass
class ProtectionRecord:
    id: str
    name: str
    resource_arn: str
    health_check_ids: list = field(default_factory=list)
    tags: list = field(default_factory=list)

@dataclass
class ProtectionGroupRecord:
    protection_group_id: str
    aggregation: str  # SUM, MEAN, MAX
    pattern: str  # ARBITRARY, BY_RESOURCE_TYPE
    resource_type: str | None = None  # Required if pattern=BY_RESOURCE_TYPE
    members: list = field(default_factory=list)
    tags: list = field(default_factory=list)

@dataclass
class SubscriptionRecord:
    auto_renew: str = 'DISABLED'  # ENABLED, DISABLED
    proactive_engagement_status: str = 'DISABLED'  # ENABLED, DISABLED, PENDING
    subscription_limits: dict = field(default_factory=lambda: {
        'ProtectionLimits': {'Max': 1000},
        'ProtectionGroupLimits': {'Max': 20}
    })
    start_time: str | None = None
    end_time: str | None = None
    time_commitment_in_seconds: int | None = None

@dataclass
class DRTConfigRecord:
    role_arn: str | None = None
    log_bucket_list: list = field(default_factory=list)
    emergency_contact_list: list = field(default_factory=list)

@dataclass
class ApplicationLayerResponseRecord:
    resource_arn: str
    action: str  # COUNT, BLOCK


# ── Store ─────────────────────────────────────────────────────────────

class ShieldStore:
    """In-memory store for Shield Advanced resources."""

    def __init__(self):
        self.protections: dict = {}
        self.protection_groups: dict = {}
        self.subscription: SubscriptionRecord | None = None
        self.drt_config: DRTConfigRecord = DRTConfigRecord()
        self.health_checks: dict = {}  # protection_id -> [health_check_arn, ...]
        self.app_layer_responses: dict = {}  # resource_arn -> ApplicationLayerResponseRecord
        self.tags: dict = {}  # resource_arn -> [{"Key":..., "Value":...}, ...]

    # ── Protection ─────────────────────────────────────────────────

    def create_protection(self, name, resource_arn, tags=None):
        # Check for duplicate
        for p in self.protections.values():
            if p.name == name and p.resource_arn == resource_arn:
                raise ResourceAlreadyExistsException(
                    f"Protection with name={name} and resource_arn={resource_arn} already exists"
                )
        protection_id = f"p-{len(self.protections) + 1:08d}"
        record = ProtectionRecord(
            id=protection_id,
            name=name,
            resource_arn=resource_arn,
            tags=tags or []
        )
        self.protections[protection_id] = record
        if tags:
            self.tags[resource_arn] = tags
        return {"ProtectionId": protection_id}

    def describe_protection(self, protection_id=None, resource_arn=None):
        if protection_id:
            record = self.protections.get(protection_id)
            if not record:
                raise ResourceNotFoundException(f"Protection {protection_id} not found")
            return self._protection_to_dict(record)
        if resource_arn:
            for p in self.protections.values():
                if p.resource_arn == resource_arn:
                    return self._protection_to_dict(p)
            raise ResourceNotFoundException(f"Protection for {resource_arn} not found")
        raise InvalidParameterException("Must specify ProtectionId or ResourceArn")

    def delete_protection(self, protection_id):
        if protection_id not in self.protections:
            raise ResourceNotFoundException(f"Protection {protection_id} not found")
        record = self.protections.pop(protection_id)
        # Clean up tags
        self.tags.pop(record.resource_arn, None)
        return {}

    def list_protections(self, next_token=None, max_results=None, inclusion_filters=None):
        items = list(self.protections.values())
        result = [self._protection_to_dict(p) for p in items]
        return {"Protections": result, "NextToken": None}

    def _protection_to_dict(self, p):
        return {
            "Id": p.id,
            "Name": p.name,
            "ResourceArn": p.resource_arn,
            "HealthCheckIds": p.health_check_ids,
            "ProtectionArn": f"arn:aws:shield::000000000000:protection/{p.id}",
        }

    # ── ProtectionGroup ────────────────────────────────────────────

    def create_protection_group(self, protection_group_id, aggregation, pattern,
                                 resource_type=None, members=None, tags=None):
        if protection_group_id in self.protection_groups:
            raise ResourceAlreadyExistsException(
                f"ProtectionGroup {protection_group_id} already exists"
            )
        if not aggregation:
            raise InvalidParameterException("Aggregation is required")
        if pattern not in ('ARBITRARY', 'BY_RESOURCE_TYPE'):
            raise InvalidParameterException(
                f"Pattern must be ARBITRARY or BY_RESOURCE_TYPE, got {pattern}"
            )
        if pattern == 'BY_RESOURCE_TYPE' and not resource_type:
            raise InvalidParameterException(
                "ResourceType is required when Pattern is BY_RESOURCE_TYPE"
            )
        record = ProtectionGroupRecord(
            protection_group_id=protection_group_id,
            aggregation=aggregation,
            pattern=pattern,
            resource_type=resource_type,
            members=members or [],
            tags=tags or []
        )
        self.protection_groups[protection_group_id] = record
        if tags:
            pg_arn = f"arn:aws:shield::000000000000:protection-group/{protection_group_id}"
            self.tags[pg_arn] = tags
        return {"ProtectionGroupId": protection_group_id}

    def describe_protection_group(self, protection_group_id):
        if protection_group_id not in self.protection_groups:
            raise ResourceNotFoundException(
                f"ProtectionGroup {protection_group_id} not found"
            )
        return self._pg_to_dict(self.protection_groups[protection_group_id])

    def update_protection_group(self, protection_group_id, aggregation, pattern,
                                 resource_type=None, members=None):
        if protection_group_id not in self.protection_groups:
            raise ResourceNotFoundException(
                f"ProtectionGroup {protection_group_id} not found"
            )
        record = self.protection_groups[protection_group_id]
        record.aggregation = aggregation
        record.pattern = pattern
        record.resource_type = resource_type
        if members is not None:
            record.members = members
        return {}

    def delete_protection_group(self, protection_group_id):
        if protection_group_id not in self.protection_groups:
            raise ResourceNotFoundException(
                f"ProtectionGroup {protection_group_id} not found"
            )
        self.protection_groups.pop(protection_group_id)
        return {}

    def list_protection_groups(self, next_token=None, max_results=None, inclusion_filters=None):
        items = list(self.protection_groups.values())
        result = [self._pg_to_dict(pg) for pg in items]
        return {"ProtectionGroups": result, "NextToken": None}

    def list_resources_in_protection_group(self, protection_group_id, next_token=None, max_results=None):
        if protection_group_id not in self.protection_groups:
            raise ResourceNotFoundException(
                f"ProtectionGroup {protection_group_id} not found"
            )
        pg = self.protection_groups[protection_group_id]
        return {"ResourceArns": list(pg.members), "NextToken": None}

    def _pg_to_dict(self, pg):
        d = {
            "ProtectionGroupId": pg.protection_group_id,
            "Aggregation": pg.aggregation,
            "Pattern": pg.pattern,
            "Members": pg.members,
            "ProtectionGroupArn": f"arn:aws:shield::000000000000:protection-group/{pg.protection_group_id}",
        }
        if pg.resource_type:
            d["ResourceType"] = pg.resource_type
        return d

    # ── Subscription ───────────────────────────────────────────────

    def create_subscription(self):
        if self.subscription is not None:
            raise ResourceAlreadyExistsException("Subscription already exists")
        self.subscription = SubscriptionRecord()
        return {}

    def delete_subscription(self):
        if self.subscription is None:
            raise ResourceNotFoundException("No subscription found")
        self.subscription = None
        return {}

    def describe_subscription(self):
        if self.subscription is None:
            raise ResourceNotFoundException("No subscription found")
        return self._sub_to_dict(self.subscription)

    def update_subscription(self, auto_renew=None):
        if self.subscription is None:
            raise ResourceNotFoundException("No subscription found")
        if auto_renew is not None:
            self.subscription.auto_renew = auto_renew
        return {}

    def get_subscription_state(self):
        state = "ACTIVE" if self.subscription is not None else "INACTIVE"
        return {"SubscriptionState": state}

    def _sub_to_dict(self, sub):
        return {
            "AutoRenew": sub.auto_renew,
            "ProactiveEngagementStatus": sub.proactive_engagement_status,
            "SubscriptionLimits": sub.subscription_limits,
            "TimeCommitmentInSeconds": sub.time_commitment_in_seconds or 0,
        }

    # ── DRT Configuration ──────────────────────────────────────────

    def associate_drt_log_bucket(self, log_bucket):
        # Check role exists first
        if not self.drt_config.role_arn:
            raise NoAssociatedRoleException("No DRT role associated")
        if len(self.drt_config.log_bucket_list) >= 10:
            raise LimitsExceededException("Maximum 10 log buckets allowed")
        if log_bucket in self.drt_config.log_bucket_list:
            raise InvalidOperationException("Log bucket already associated")
        if not (3 <= len(log_bucket) <= 63):
            raise InvalidParameterException("LogBucket must be 3-63 characters")
        self.drt_config.log_bucket_list.append(log_bucket)
        return {}

    def disassociate_drt_log_bucket(self, log_bucket):
        if log_bucket not in self.drt_config.log_bucket_list:
            raise ResourceNotFoundException(f"LogBucket {log_bucket} not associated")
        self.drt_config.log_bucket_list.remove(log_bucket)
        return {}

    def associate_drt_role(self, role_arn):
        self.drt_config.role_arn = role_arn
        return {}

    def disassociate_drt_role(self):
        self.drt_config.role_arn = None
        return {}

    def describe_drt_access(self):
        return {
            "RoleArn": self.drt_config.role_arn or "",
            "LogBucketList": list(self.drt_config.log_bucket_list),
        }

    # ── Health Check ───────────────────────────────────────────────

    def associate_health_check(self, protection_id, health_check_arn):
        if protection_id not in self.protections:
            raise ResourceNotFoundException(f"Protection {protection_id} not found")
        if protection_id not in self.health_checks:
            self.health_checks[protection_id] = []
        if health_check_arn in self.health_checks[protection_id]:
            raise InvalidOperationException("HealthCheck already associated")
        self.health_checks[protection_id].append(health_check_arn)
        self.protections[protection_id].health_check_ids.append(health_check_arn)
        return {}

    def disassociate_health_check(self, protection_id, health_check_arn):
        if protection_id not in self.protections:
            raise ResourceNotFoundException(f"Protection {protection_id} not found")
        if protection_id not in self.health_checks or health_check_arn not in self.health_checks[protection_id]:
            raise ResourceNotFoundException(f"HealthCheck {health_check_arn} not associated")
        self.health_checks[protection_id].remove(health_check_arn)
        self.protections[protection_id].health_check_ids.remove(health_check_arn)
        return {}

    # ── Proactive Engagement ───────────────────────────────────────

    def associate_proactive_engagement_details(self, emergency_contact_list):
        self.drt_config.emergency_contact_list = emergency_contact_list
        return {}

    def enable_proactive_engagement(self):
        if self.subscription is None:
            raise ResourceNotFoundException("No subscription found")
        self.subscription.proactive_engagement_status = 'ENABLED'
        return {}

    def disable_proactive_engagement(self):
        if self.subscription is None:
            raise ResourceNotFoundException("No subscription found")
        self.subscription.proactive_engagement_status = 'DISABLED'
        return {}

    # ── Emergency Contact ──────────────────────────────────────────

    def describe_emergency_contact_settings(self):
        return {"EmergencyContactList": list(self.drt_config.emergency_contact_list)}

    def update_emergency_contact_settings(self, emergency_contact_list=None):
        if emergency_contact_list is not None:
            self.drt_config.emergency_contact_list = emergency_contact_list
        return {}

    # ── Application Layer Auto Response ────────────────────────────

    def enable_application_layer_automatic_response(self, resource_arn, action):
        if resource_arn in self.app_layer_responses:
            raise InvalidOperationException("Already enabled for this resource")
        if action not in ('COUNT', 'BLOCK'):
            raise InvalidParameterException(f"Action must be COUNT or BLOCK, got {action}")
        self.app_layer_responses[resource_arn] = ApplicationLayerResponseRecord(
            resource_arn=resource_arn, action=action
        )
        return {}

    def disable_application_layer_automatic_response(self, resource_arn):
        if resource_arn not in self.app_layer_responses:
            raise ResourceNotFoundException(f"No automatic response for {resource_arn}")
        self.app_layer_responses.pop(resource_arn)
        return {}

    def update_application_layer_automatic_response(self, resource_arn, action):
        if resource_arn not in self.app_layer_responses:
            raise ResourceNotFoundException(f"No automatic response for {resource_arn}")
        if action not in ('COUNT', 'BLOCK'):
            raise InvalidParameterException(f"Action must be COUNT or BLOCK, got {action}")
        self.app_layer_responses[resource_arn].action = action
        return {}

    # ── Tags ───────────────────────────────────────────────────────

    def tag_resource(self, resource_arn, tags):
        self.tags[resource_arn] = tags
        return {}

    def untag_resource(self, resource_arn, tag_keys):
        if resource_arn not in self.tags:
            raise ResourceNotFoundException(f"No tags for {resource_arn}")
        current = self.tags[resource_arn]
        self.tags[resource_arn] = [t for t in current if t.get('Key') not in tag_keys]
        return {}

    def list_tags_for_resource(self, resource_arn):
        return {"Tags": self.tags.get(resource_arn, [])}
