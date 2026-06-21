"""WAFv2 service store — WebACL, IPSet, RegexPatternSet, RuleGroup, Logging, Policy."""

# ── Exception classes (matching AWS error codes) ────────────────────────

class WAFInternalErrorException(Exception):
    """Your request is valid, but WAF couldn't perform the operation because of a system problem."""

class WAFInvalidParameterException(Exception):
    """The operation failed because WAF didn't recognize a parameter in the request."""

class WAFNonexistentItemException(Exception):
    """WAF couldn't perform the operation because your resource doesn't exist."""

class WAFUnavailableEntityException(Exception):
    """WAF couldn't retrieve a resource that you specified for this operation."""

class WAFInvalidOperationException(Exception):
    """The operation isn't valid."""

class WAFLimitsExceededException(Exception):
    """WAF couldn't perform the operation because you exceeded your resource limit."""

class WAFInvalidResourceException(Exception):
    """WAF couldn't perform the operation because the resource isn't valid."""

class WAFSubscriptionNotFoundException(Exception):
    """You tried to use a managed rule group that's available by subscription, but you aren't subscribed."""

class WAFExpiredManagedRuleGroupVersionException(Exception):
    """The specified version for the managed rule group has expired."""

class WAFInvalidPermissionPolicyException(Exception):
    """The operation failed because the specified policy isn't valid."""

class WAFTagOperationException(Exception):
    """An error occurred during the tagging operation."""

class WAFTagOperationInternalErrorException(Exception):
    """WAF couldn't perform your tagging operation because of an internal error."""

class WAFOptimisticLockException(Exception):
    """WAF couldn't save your changes because you're trying to update a resource that has changed."""

class WAFDuplicateItemException(Exception):
    """WAF couldn't perform the operation because the resource already exists."""

class WAFFeatureNotIncludedInPricingPlanException(Exception):
    """The operation failed because the specified WAF feature isn't supported."""

class WAFAssociatedItemException(Exception):
    """WAF couldn't perform the operation because the resource is associated with another resource."""

class WAFLogDestinationPermissionIssueException(Exception):
    """The operation failed because you don't have permission to access the log destination."""

class WAFConfigurationWarningException(Exception):
    """The operation failed because of a configuration warning."""


# ── Data records ────────────────────────────────────────────────────────

class WebACLRecord:
    def __init__(self, id, name, scope, default_action, visibility_config, arn,
                 rules=None, capacity=None, description="",
                 custom_response_bodies=None, captcha_config=None,
                 challenge_config=None, token_domains=None,
                 association_config=None, tags=None,
                 managed_by_firewall_manager=False,
                 label_namespace=None, post_attack_data_inspection_config=None,
                 lock_token=None):
        self.id = id
        self.name = name
        self.scope = scope
        self.default_action = default_action
        self.visibility_config = visibility_config
        self.arn = arn
        self.rules = rules or []
        self.capacity = capacity
        self.description = description
        self.custom_response_bodies = custom_response_bodies or {}
        self.captcha_config = captcha_config or {}
        self.challenge_config = challenge_config or {}
        self.token_domains = token_domains or []
        self.association_config = association_config or {}
        self.tags = tags or []
        self.managed_by_firewall_manager = managed_by_firewall_manager
        self.label_namespace = label_namespace
        self.post_attack_data_inspection_config = post_attack_data_inspection_config or {}
        self.lock_token = lock_token

    def to_dict(self):
        result = {
            'Id': self.id, 'Name': self.name, 'ARN': self.arn,
            'DefaultAction': self.default_action,
            'VisibilityConfig': self.visibility_config,
            'Rules': self.rules,
            'Description': self.description,
            'Capacity': self.capacity,
        }
        if self.tags:
            result['Tags'] = self.tags
        return result


class IPSetRecord:
    def __init__(self, id, name, scope, ip_address_version, addresses, arn,
                 description="", lock_token=None, tags=None):
        self.id = id
        self.name = name
        self.scope = scope
        self.ip_address_version = ip_address_version
        self.addresses = addresses
        self.arn = arn
        self.description = description
        self.lock_token = lock_token
        self.tags = tags or []

    def to_summary(self):
        return {
            'Id': self.id, 'Name': self.name, 'ARN': self.arn,
            'IPAddressVersion': self.ip_address_version,
            'Description': self.description,
            'LockToken': self.lock_token,
        }


class RegexPatternSetRecord:
    def __init__(self, id, name, scope, regular_expression_list, arn,
                 description="", lock_token=None, tags=None):
        self.id = id
        self.name = name
        self.scope = scope
        self.regular_expression_list = regular_expression_list
        self.arn = arn
        self.description = description
        self.lock_token = lock_token
        self.tags = tags or []

    def to_summary(self):
        return {
            'Id': self.id, 'Name': self.name, 'ARN': self.arn,
            'Description': self.description,
            'LockToken': self.lock_token,
        }


class RuleGroupRecord:
    def __init__(self, id, name, scope, capacity, visibility_config, arn,
                 rules=None, description="", lock_token=None, tags=None,
                 custom_response_bodies=None,
                 available_labels=None, consumed_labels=None,
                 label_namespace=None):
        self.id = id
        self.name = name
        self.scope = scope
        self.capacity = capacity
        self.visibility_config = visibility_config
        self.arn = arn
        self.rules = rules or []
        self.description = description
        self.lock_token = lock_token
        self.tags = tags or []
        self.custom_response_bodies = custom_response_bodies or {}
        self.available_labels = available_labels or []
        self.consumed_labels = consumed_labels or []
        self.label_namespace = label_namespace

    def to_summary(self):
        return {
            'Id': self.id, 'Name': self.name, 'ARN': self.arn,
            'Description': self.description,
            'LockToken': self.lock_token,
        }


class LoggingConfigurationRecord:
    def __init__(self, resource_arn, log_destination_configs,
                 redacted_fields=None, managed_by_firewall_manager=False,
                 logging_filter=None):
        self.resource_arn = resource_arn
        self.log_destination_configs = log_destination_configs
        self.redacted_fields = redacted_fields or []
        self.managed_by_firewall_manager = managed_by_firewall_manager
        self.logging_filter = logging_filter or {}


class PermissionPolicyRecord:
    def __init__(self, resource_arn, policy):
        self.resource_arn = resource_arn
        self.policy = policy


# ── Store ───────────────────────────────────────────────────────────────

class WAFv2Store:
    """In-memory store for WAFv2 resources."""

    def __init__(self):
        self.web_acls = {}        # id -> WebACLRecord
        self.ip_sets = {}         # id -> IPSetRecord
        self.regex_pattern_sets = {}  # id -> RegexPatternSetRecord
        self.rule_groups = {}     # id -> RuleGroupRecord
        self.logging_configs = {} # resource_arn -> LoggingConfigurationRecord
        self.permission_policies = {} # resource_arn -> PermissionPolicyRecord
        self.webacl_associations = {}  # resource_arn -> web_acl_arn

    # ── ID generation ───────────────────────────────────────────────────

    def _generate_id(self, name, scope):
        import uuid
        return str(uuid.uuid4())

    def _generate_lock_token(self):
        import uuid
        return str(uuid.uuid4())

    def _generate_arn(self, resource_type, id, scope, region='us-east-1', account_id='123456789012'):
        if scope == 'CLOUDFRONT':
            return f'arn:aws:wafv2:us-east-1:{account_id}:{scope}/{resource_type}/{id}'
        return f'arn:aws:wafv2:{region}:{account_id}:{scope}/{resource_type}/{id}'

    # ── WebACL CRUD ─────────────────────────────────────────────────────

    def create_web_acl(self, name, scope, default_action, visibility_config, description="",
                       rules=None, capacity=None, custom_response_bodies=None,
                       captcha_config=None, challenge_config=None, token_domains=None,
                       association_config=None, tags=None):
        if name in [a.name for a in self.web_acls.values()]:
            raise WAFDuplicateItemException(
                f"A web ACL with name '{name}' already exists")
        id = self._generate_id(name, scope)
        arn = self._generate_arn('webacl', id, scope)
        record = WebACLRecord(
            id=id, name=name, scope=scope,
            default_action=default_action,
            visibility_config=visibility_config,
            arn=arn, rules=rules, capacity=capacity,
            description=description,
            custom_response_bodies=custom_response_bodies,
            captcha_config=captcha_config,
            challenge_config=challenge_config,
            token_domains=token_domains,
            association_config=association_config,
            tags=tags,
            lock_token=self._generate_lock_token())
        self.web_acls[id] = record
        return record.to_dict()

    def get_web_acl(self, id, name, scope):
        if id:
            record = self.web_acls.get(id)
        elif name:
            for r in self.web_acls.values():
                if r.name == name and r.scope == scope:
                    record = r
                    break
            else:
                record = None
        else:
            raise WAFInvalidParameterException("Either Id or Name is required")
        if record is None:
            raise WAFNonexistentItemException(
                f"Web ACL '{id or name}' does not exist")
        return record

    def update_web_acl(self, id, name, scope, lock_token, default_action,
                       visibility_config, description="", rules=None):
        record = self.get_web_acl(id, name, scope)
        if lock_token and record.lock_token and record.lock_token != lock_token:
            raise WAFOptimisticLockException(
                "The resource has been modified since you last retrieved it")
        record.default_action = default_action
        record.visibility_config = visibility_config
        record.description = description
        if rules is not None:
            record.rules = rules
        record.lock_token = self._generate_lock_token()
        return {'NextLockToken': record.lock_token}

    def delete_web_acl(self, id, name, scope, lock_token):
        record = self.get_web_acl(id, name, scope)
        if lock_token and record.lock_token and record.lock_token != lock_token:
            raise WAFOptimisticLockException(
                "The resource has been modified since you last retrieved it")
        # Check associations
        associated = [arn for arn, acl_arn in self.webacl_associations.items()
                      if acl_arn == record.arn]
        if associated:
            raise WAFAssociatedItemException(
                f"Web ACL is associated with resources: {associated}")
        del self.web_acls[record.id]

    def list_web_acls(self, scope, next_marker=None, limit=None):
        items = [r for r in self.web_acls.values() if r.scope == scope]
        result = [{'Id': r.id, 'Name': r.name, 'ARN': r.arn,
                    'Description': r.description} for r in items]
        return {'WebACLs': result, 'NextMarker': next_marker}

    # ── IPSet CRUD ──────────────────────────────────────────────────────

    def create_ip_set(self, name, scope, ip_address_version, addresses,
                      description="", tags=None):
        if name in [s.name for s in self.ip_sets.values() if s.scope == scope]:
            raise WAFDuplicateItemException(
                f"An IP set with name '{name}' already exists in scope {scope}")
        id = self._generate_id(name, scope)
        arn = self._generate_arn('ipset', id, scope)
        record = IPSetRecord(
            id=id, name=name, scope=scope,
            ip_address_version=ip_address_version,
            addresses=addresses, arn=arn,
            description=description,
            lock_token=self._generate_lock_token(),
            tags=tags)
        self.ip_sets[id] = record
        return record.to_summary()

    def get_ip_set(self, id, name, scope):
        if id:
            record = self.ip_sets.get(id)
        elif name:
            for r in self.ip_sets.values():
                if r.name == name and r.scope == scope:
                    record = r
                    break
            else:
                record = None
        else:
            raise WAFInvalidParameterException("Either Id or Name is required")
        if record is None:
            raise WAFNonexistentItemException(
                f"IP set '{id or name}' does not exist")
        return record

    def update_ip_set(self, id, name, scope, lock_token, addresses,
                      description=""):
        record = self.get_ip_set(id, name, scope)
        if lock_token and record.lock_token and record.lock_token != lock_token:
            raise WAFOptimisticLockException(
                "The resource has been modified since you last retrieved it")
        record.addresses = addresses
        if description:
            record.description = description
        record.lock_token = self._generate_lock_token()
        return {'NextLockToken': record.lock_token}

    def delete_ip_set(self, id, name, scope, lock_token):
        record = self.get_ip_set(id, name, scope)
        if lock_token and record.lock_token and record.lock_token != lock_token:
            raise WAFOptimisticLockException(
                "The resource has been modified since you last retrieved it")
        del self.ip_sets[record.id]

    def list_ip_sets(self, scope, next_marker=None, limit=None):
        items = [r for r in self.ip_sets.values() if r.scope == scope]
        result = [r.to_summary() for r in items]
        return {'IPSets': result, 'NextMarker': next_marker}

    # ── RegexPatternSet CRUD ────────────────────────────────────────────

    def create_regex_pattern_set(self, name, scope, regular_expression_list,
                                 description="", tags=None):
        if name in [s.name for s in self.regex_pattern_sets.values() if s.scope == scope]:
            raise WAFDuplicateItemException(
                f"A regex pattern set with name '{name}' already exists in scope {scope}")
        id = self._generate_id(name, scope)
        arn = self._generate_arn('regexpatternset', id, scope)
        record = RegexPatternSetRecord(
            id=id, name=name, scope=scope,
            regular_expression_list=regular_expression_list,
            arn=arn, description=description,
            lock_token=self._generate_lock_token(),
            tags=tags)
        self.regex_pattern_sets[id] = record
        return record.to_summary()

    def get_regex_pattern_set(self, id, name, scope):
        if id:
            record = self.regex_pattern_sets.get(id)
        elif name:
            for r in self.regex_pattern_sets.values():
                if r.name == name and r.scope == scope:
                    record = r
                    break
            else:
                record = None
        else:
            raise WAFInvalidParameterException("Either Id or Name is required")
        if record is None:
            raise WAFNonexistentItemException(
                f"Regex pattern set '{id or name}' does not exist")
        return record

    def update_regex_pattern_set(self, id, name, scope, lock_token,
                                 regular_expression_list, description=""):
        record = self.get_regex_pattern_set(id, name, scope)
        if lock_token and record.lock_token and record.lock_token != lock_token:
            raise WAFOptimisticLockException(
                "The resource has been modified since you last retrieved it")
        record.regular_expression_list = regular_expression_list
        if description:
            record.description = description
        record.lock_token = self._generate_lock_token()
        return {'NextLockToken': record.lock_token}

    def delete_regex_pattern_set(self, id, name, scope, lock_token):
        record = self.get_regex_pattern_set(id, name, scope)
        if lock_token and record.lock_token and record.lock_token != lock_token:
            raise WAFOptimisticLockException(
                "The resource has been modified since you last retrieved it")
        del self.regex_pattern_sets[record.id]

    def list_regex_pattern_sets(self, scope, next_marker=None, limit=None):
        items = [r for r in self.regex_pattern_sets.values() if r.scope == scope]
        result = [r.to_summary() for r in items]
        return {'RegexPatternSets': result, 'NextMarker': next_marker}

    # ── RuleGroup CRUD ──────────────────────────────────────────────────

    def create_rule_group(self, name, scope, capacity, visibility_config,
                          description="", rules=None, tags=None,
                          custom_response_bodies=None):
        if name in [g.name for g in self.rule_groups.values() if g.scope == scope]:
            raise WAFDuplicateItemException(
                f"A rule group with name '{name}' already exists in scope {scope}")
        id = self._generate_id(name, scope)
        arn = self._generate_arn('rulegroup', id, scope)
        record = RuleGroupRecord(
            id=id, name=name, scope=scope,
            capacity=capacity,
            visibility_config=visibility_config,
            arn=arn, rules=rules,
            description=description,
            lock_token=self._generate_lock_token(),
            tags=tags,
            custom_response_bodies=custom_response_bodies)
        self.rule_groups[id] = record
        return record.to_summary()

    def get_rule_group(self, id, name, scope):
        if id:
            record = self.rule_groups.get(id)
        elif name:
            for r in self.rule_groups.values():
                if r.name == name and r.scope == scope:
                    record = r
                    break
            else:
                record = None
        else:
            raise WAFInvalidParameterException("Either Id or Name is required")
        if record is None:
            raise WAFNonexistentItemException(
                f"Rule group '{id or name}' does not exist")
        return record

    def update_rule_group(self, id, name, scope, lock_token, visibility_config,
                          description="", rules=None):
        record = self.get_rule_group(id, name, scope)
        if lock_token and record.lock_token and record.lock_token != lock_token:
            raise WAFOptimisticLockException(
                "The resource has been modified since you last retrieved it")
        record.visibility_config = visibility_config
        if description:
            record.description = description
        if rules is not None:
            record.rules = rules
        record.lock_token = self._generate_lock_token()
        return {'NextLockToken': record.lock_token}

    def delete_rule_group(self, id, name, scope, lock_token):
        record = self.get_rule_group(id, name, scope)
        if lock_token and record.lock_token and record.lock_token != lock_token:
            raise WAFOptimisticLockException(
                "The resource has been modified since you last retrieved it")
        del self.rule_groups[record.id]

    def list_rule_groups(self, scope, next_marker=None, limit=None):
        items = [r for r in self.rule_groups.values() if r.scope == scope]
        result = [r.to_summary() for r in items]
        return {'RuleGroups': result, 'NextMarker': next_marker}

    # ── Logging Configuration CRUD ──────────────────────────────────────

    def put_logging_configuration(self, logging_configuration):
        resource_arn = logging_configuration.get('ResourceArn')
        if not resource_arn:
            raise WAFInvalidParameterException("ResourceArn is required")
        record = LoggingConfigurationRecord(
            resource_arn=resource_arn,
            log_destination_configs=logging_configuration.get('LogDestinationConfigs', []),
            redacted_fields=logging_configuration.get('RedactedFields'),
            managed_by_firewall_manager=logging_configuration.get('ManagedByFirewallManager', False),
            logging_filter=logging_configuration.get('LoggingFilter'))
        self.logging_configs[resource_arn] = record
        return {'LoggingConfiguration': {
            'ResourceArn': resource_arn,
            'LogDestinationConfigs': record.log_destination_configs,
        }}

    def get_logging_configuration(self, resource_arn):
        record = self.logging_configs.get(resource_arn)
        if record is None:
            raise WAFNonexistentItemException(
                f"No logging configuration for {resource_arn}")
        return {'LoggingConfiguration': {
            'ResourceArn': record.resource_arn,
            'LogDestinationConfigs': record.log_destination_configs,
        }}

    def delete_logging_configuration(self, resource_arn):
        if resource_arn not in self.logging_configs:
            raise WAFNonexistentItemException(
                f"No logging configuration for {resource_arn}")
        del self.logging_configs[resource_arn]

    def list_logging_configurations(self, scope, next_marker=None, limit=None):
        items = list(self.logging_configs.values())
        result = [{'ResourceArn': r.resource_arn,
                    'LogDestinationConfigs': r.log_destination_configs}
                  for r in items]
        return {'LoggingConfigurations': result, 'NextMarker': next_marker}

    # ── Permission Policy CRUD ──────────────────────────────────────────

    def put_permission_policy(self, resource_arn, policy):
        self.permission_policies[resource_arn] = PermissionPolicyRecord(
            resource_arn=resource_arn, policy=policy)

    def get_permission_policy(self, resource_arn):
        record = self.permission_policies.get(resource_arn)
        if record is None:
            raise WAFNonexistentItemException(
                f"No permission policy for {resource_arn}")
        return {'Policy': record.policy}

    def delete_permission_policy(self, resource_arn):
        if resource_arn not in self.permission_policies:
            raise WAFNonexistentItemException(
                f"No permission policy for {resource_arn}")
        del self.permission_policies[resource_arn]

    # ── WebACL Associations ─────────────────────────────────────────────

    def associate_web_acl(self, web_acl_arn, resource_arn):
        # Verify web ACL exists
        web_acl_id = web_acl_arn.split('/')[-1]
        if web_acl_id not in self.web_acls:
            raise WAFNonexistentItemException(
                f"Web ACL '{web_acl_arn}' does not exist")
        self.webacl_associations[resource_arn] = web_acl_arn

    def disassociate_web_acl(self, resource_arn):
        if resource_arn not in self.webacl_associations:
            raise WAFNonexistentItemException(
                f"No web ACL associated with {resource_arn}")
        del self.webacl_associations[resource_arn]

    def get_web_acl_for_resource(self, resource_arn):
        web_acl_arn = self.webacl_associations.get(resource_arn)
        if web_acl_arn is None:
            raise WAFNonexistentItemException(
                f"No web ACL associated with {resource_arn}")
        web_acl_id = web_acl_arn.split('/')[-1]
        record = self.web_acls.get(web_acl_id)
        if record is None:
            raise WAFNonexistentItemException(
                "Web ACL not found")
        return {'WebACL': record.to_dict()}

    def list_resources_for_web_acl(self, web_acl_arn):
        resources = [arn for arn, acl_arn in self.webacl_associations.items()
                     if acl_arn == web_acl_arn]
        return {'ResourceArns': resources}

    # ── Tags ────────────────────────────────────────────────────────────

    def tag_resource(self, resource_arn, tags):
        # Find the resource by ARN
        for collection in [self.web_acls, self.ip_sets,
                           self.regex_pattern_sets, self.rule_groups]:
            for record in collection.values():
                if record.arn == resource_arn:
                    record.tags = record.tags or []
                    for tag in tags:
                        record.tags.append(tag)
                    return
        raise WAFNonexistentItemException(
            f"Resource '{resource_arn}' does not exist")

    def untag_resource(self, resource_arn, tag_keys):
        for collection in [self.web_acls, self.ip_sets,
                           self.regex_pattern_sets, self.rule_groups]:
            for record in collection.values():
                if record.arn == resource_arn:
                    record.tags = [t for t in record.tags
                                   if t.get('Key') not in tag_keys]
                    return
        raise WAFNonexistentItemException(
            f"Resource '{resource_arn}' does not exist")

    def list_tags_for_resource(self, resource_arn):
        for collection in [self.web_acls, self.ip_sets,
                           self.regex_pattern_sets, self.rule_groups]:
            for record in collection.values():
                if record.arn == resource_arn:
                    return {'TagInfoForResource': {
                        'ResourceARN': resource_arn,
                        'TagList': record.tags or [],
                    }}
        raise WAFNonexistentItemException(
            f"Resource '{resource_arn}' does not exist")
