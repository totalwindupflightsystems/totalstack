"""Network Firewall store — real in-memory implementation."""
import uuid


# ── Exception Classes ──────────────────────────────────────────────

class InvalidRequestException(Exception):
    pass

class InternalServerError(Exception):
    pass

class ResourceNotFoundException(Exception):
    pass

class ThrottlingException(Exception):
    pass

class LimitExceededException(Exception):
    pass

class InvalidResourcePolicyException(Exception):
    pass

class ResourceOwnerCheckException(Exception):
    pass


# ── Record Classes ─────────────────────────────────────────────────

class FirewallStatus:
    def __init__(self, Status="ACTIVE", ConfigurationSyncStateSummary="IN_SYNC",
                 SyncStates=None):
        self.Status = Status
        self.ConfigurationSyncStateSummary = ConfigurationSyncStateSummary
        self.SyncStates = SyncStates or {}

    def to_dict(self):
        return {
            "Status": self.Status,
            "ConfigurationSyncStateSummary": self.ConfigurationSyncStateSummary,
            "SyncStates": self.SyncStates,
        }


class EncryptionConfiguration:
    def __init__(self, KeyId=None, Type="CUSTOMER_KMS"):
        self.KeyId = KeyId
        self.Type = Type

    def to_dict(self):
        return {"KeyId": self.KeyId, "Type": self.Type}


class SubnetMapping:
    def __init__(self, SubnetId=None, IPAddressType=None):
        self.SubnetId = SubnetId
        self.IPAddressType = IPAddressType

    def to_dict(self):
        d = {"SubnetId": self.SubnetId}
        if self.IPAddressType:
            d["IPAddressType"] = self.IPAddressType
        return d


class FirewallRecord:
    def __init__(self, FirewallName, FirewallPolicyArn, VpcId=None,
                 SubnetMappings=None, DeleteProtection=False,
                 SubnetChangeProtection=False,
                 FirewallPolicyChangeProtection=False,
                 Description="", Tags=None,
                 EncryptionConfiguration=None,
                 AvailabilityZoneChangeProtection=False):
        self.FirewallName = FirewallName
        self.FirewallPolicyArn = FirewallPolicyArn
        self.VpcId = VpcId or "vpc-00000000"
        if isinstance(SubnetMappings, list):
            self.SubnetMappings = [
                SubnetMapping(**sm) if isinstance(sm, dict) else sm
                for sm in SubnetMappings
            ]
        else:
            self.SubnetMappings = []
        self.DeleteProtection = DeleteProtection
        self.SubnetChangeProtection = SubnetChangeProtection
        self.FirewallPolicyChangeProtection = FirewallPolicyChangeProtection
        self.AvailabilityZoneChangeProtection = AvailabilityZoneChangeProtection
        self.Description = Description or ""
        if isinstance(EncryptionConfiguration, dict):
            self.EncryptionConfiguration = EncryptionConfiguration(**EncryptionConfiguration)
        elif isinstance(EncryptionConfiguration, _EncryptionConfiguration):
            self.EncryptionConfiguration = EncryptionConfiguration
        else:
            self.EncryptionConfiguration = None
        self.Tags = Tags or []
        self.FirewallArn = f"arn:aws:network-firewall:us-east-1:000000000000:firewall/{uuid.uuid4().hex[:8]}"
        self.FirewallId = uuid.uuid4().hex[:8]
        self.Status = FirewallStatus()

    def to_dict(self):
        d = {
            "FirewallName": self.FirewallName,
            "FirewallArn": self.FirewallArn,
            "FirewallId": self.FirewallId,
            "FirewallPolicyArn": self.FirewallPolicyArn,
            "VpcId": self.VpcId,
            "SubnetMappings": [s.to_dict() if hasattr(s, 'to_dict') else s for s in self.SubnetMappings],
            "DeleteProtection": self.DeleteProtection,
            "SubnetChangeProtection": self.SubnetChangeProtection,
            "FirewallPolicyChangeProtection": self.FirewallPolicyChangeProtection,
            "Description": self.Description,
        }
        if self.EncryptionConfiguration:
            d["EncryptionConfiguration"] = self.EncryptionConfiguration.to_dict()
        return d


class FirewallPolicyData:
    """The actual policy rules inside a FirewallPolicy."""
    def __init__(self, StatelessDefaultActions=None,
                 StatelessFragmentDefaultActions=None,
                 StatelessRuleGroupReferences=None,
                 StatefulRuleGroupReferences=None,
                 StatefulDefaultActions=None,
                 StatefulEngineOptions=None,
                 TLSInspectionConfigurationArn=None):
        self.StatelessDefaultActions = StatelessDefaultActions or ["aws:forward_to_sfe"]
        self.StatelessFragmentDefaultActions = StatelessFragmentDefaultActions or ["aws:forward_to_sfe"]
        self.StatelessRuleGroupReferences = StatelessRuleGroupReferences or []
        self.StatefulRuleGroupReferences = StatefulRuleGroupReferences or []
        self.StatefulDefaultActions = StatefulDefaultActions or []
        self.StatefulEngineOptions = StatefulEngineOptions or {}
        self.TLSInspectionConfigurationArn = TLSInspectionConfigurationArn

    def to_dict(self):
        d = {
            "StatelessDefaultActions": self.StatelessDefaultActions,
            "StatelessFragmentDefaultActions": self.StatelessFragmentDefaultActions,
        }
        if self.StatelessRuleGroupReferences:
            d["StatelessRuleGroupReferences"] = self.StatelessRuleGroupReferences
        if self.StatefulRuleGroupReferences:
            d["StatefulRuleGroupReferences"] = self.StatefulRuleGroupReferences
        if self.StatefulDefaultActions:
            d["StatefulDefaultActions"] = self.StatefulDefaultActions
        if self.StatefulEngineOptions:
            d["StatefulEngineOptions"] = self.StatefulEngineOptions
        if self.TLSInspectionConfigurationArn:
            d["TLSInspectionConfigurationArn"] = self.TLSInspectionConfigurationArn
        return d


class FirewallPolicyRecord:
    def __init__(self, FirewallPolicyName, FirewallPolicy,
                 Description="", Tags=None,
                 EncryptionConfiguration=None):
        self.FirewallPolicyName = FirewallPolicyName
        if isinstance(FirewallPolicy, dict):
            self.FirewallPolicy = FirewallPolicyData(**FirewallPolicy)
        elif isinstance(FirewallPolicy, FirewallPolicyData):
            self.FirewallPolicy = FirewallPolicy
        else:
            self.FirewallPolicy = FirewallPolicyData()
        self.Description = Description or ""
        self.Tags = Tags or []
        if isinstance(EncryptionConfiguration, dict):
            self.EncryptionConfiguration = EncryptionConfiguration(**EncryptionConfiguration)
        elif isinstance(EncryptionConfiguration, _EncryptionConfiguration):
            self.EncryptionConfiguration = EncryptionConfiguration
        else:
            self.EncryptionConfiguration = None
        self.FirewallPolicyArn = f"arn:aws:network-firewall:us-east-1:000000000000:firewall-policy/{uuid.uuid4().hex[:8]}"
        self.FirewallPolicyId = uuid.uuid4().hex[:8]
        self.ConsumedStatelessRuleCapacity = 0
        self.ConsumedStatefulRuleCapacity = 0
        self.NumberOfAssociations = 0

    def to_dict(self):
        d = {
            "FirewallPolicyName": self.FirewallPolicyName,
            "FirewallPolicyArn": self.FirewallPolicyArn,
            "FirewallPolicyId": self.FirewallPolicyId,
            "FirewallPolicy": self.FirewallPolicy.to_dict(),
            "Description": self.Description,
            "ConsumedStatelessRuleCapacity": self.ConsumedStatelessRuleCapacity,
            "ConsumedStatefulRuleCapacity": self.ConsumedStatefulRuleCapacity,
            "NumberOfAssociations": self.NumberOfAssociations,
        }
        if self.EncryptionConfiguration:
            d["EncryptionConfiguration"] = self.EncryptionConfiguration.to_dict()
        return d


# Parameter-class aliases (avoid shadowing in __init__)
_EncryptionConfiguration = EncryptionConfiguration
_FirewallPolicyData = None  # not needed — FirewallPolicy param name differs from class


class RuleGroupData:
    def __init__(self, RulesSource=None, RuleVariables=None,
                 StatefulRuleOptions=None, ReferenceSets=None):
        self.RulesSource = RulesSource or {}
        self.RuleVariables = RuleVariables
        self.StatefulRuleOptions = StatefulRuleOptions
        self.ReferenceSets = ReferenceSets

    def to_dict(self):
        d = {"RulesSource": self.RulesSource}
        if self.RuleVariables:
            d["RuleVariables"] = self.RuleVariables
        if self.StatefulRuleOptions:
            d["StatefulRuleOptions"] = self.StatefulRuleOptions
        if self.ReferenceSets:
            d["ReferenceSets"] = self.ReferenceSets
        return d


class RuleGroupRecord:
    def __init__(self, RuleGroupName, Type, Capacity, RuleGroup=None,
                 Description="", Tags=None, Rules=None,
                 EncryptionConfiguration=None):
        self.RuleGroupName = RuleGroupName
        self.Type = Type or "STATELESS"
        self.Capacity = Capacity or 100
        if isinstance(RuleGroup, dict):
            self.RuleGroup = RuleGroupData(**RuleGroup)
        elif isinstance(RuleGroup, RuleGroupData):
            self.RuleGroup = RuleGroup
        else:
            self.RuleGroup = RuleGroupData()
        self.Description = Description or ""
        self.Rules = Rules or ""
        self.Tags = Tags or []
        if isinstance(EncryptionConfiguration, dict):
            self.EncryptionConfiguration = EncryptionConfiguration(**EncryptionConfiguration)
        elif isinstance(EncryptionConfiguration, _EncryptionConfiguration):
            self.EncryptionConfiguration = EncryptionConfiguration
        else:
            self.EncryptionConfiguration = None
        self.RuleGroupArn = f"arn:aws:network-firewall:us-east-1:000000000000:rule-group/{uuid.uuid4().hex[:8]}"
        self.RuleGroupId = uuid.uuid4().hex[:8]
        self.ConsumedCapacity = 0
        self.NumberOfAssociations = 0

    def to_dict(self):
        d = {
            "RuleGroupName": self.RuleGroupName,
            "RuleGroupArn": self.RuleGroupArn,
            "RuleGroupId": self.RuleGroupId,
            "Type": self.Type,
            "Capacity": self.Capacity,
            "RuleGroup": self.RuleGroup.to_dict(),
            "Description": self.Description,
            "ConsumedCapacity": self.ConsumedCapacity,
            "NumberOfAssociations": self.NumberOfAssociations,
        }
        if self.Rules:
            d["Rules"] = self.Rules
        if self.EncryptionConfiguration:
            d["EncryptionConfiguration"] = self.EncryptionConfiguration.to_dict()
        return d


# ── Store Class ────────────────────────────────────────────────────

class NetworkFirewallStore:
    def __init__(self):
        self._firewalls: dict[str, FirewallRecord] = {}
        self._policies: dict[str, FirewallPolicyRecord] = {}
        self._rule_groups: dict[str, RuleGroupRecord] = {}
        self._tags: dict[str, dict] = {}

    # ── Method accessors ────────────────────────────────────────────

    def firewalls(self, arn: str = None):
        if arn is not None:
            return self._firewalls.get(arn)
        return list(self._firewalls.values())

    def policies(self, arn: str = None):
        if arn is not None:
            return self._policies.get(arn)
        return list(self._policies.values())

    def rule_groups(self, arn: str = None):
        if arn is not None:
            return self._rule_groups.get(arn)
        return list(self._rule_groups.values())

    # ── Firewall CRUD ───────────────────────────────────────────────

    def create_firewall(self, FirewallName, FirewallPolicyArn,
                        VpcId=None, SubnetMappings=None,
                        DeleteProtection=False,
                        SubnetChangeProtection=False,
                        FirewallPolicyChangeProtection=False,
                        Description="", Tags=None,
                        EncryptionConfiguration=None,
                        AvailabilityZoneChangeProtection=False):
        # Check duplicate
        for f in self._firewalls.values():
            if f.FirewallName == FirewallName:
                raise InvalidRequestException(
                    f"Firewall with name '{FirewallName}' already exists")
        rec = FirewallRecord(
            FirewallName=FirewallName,
            FirewallPolicyArn=FirewallPolicyArn,
            VpcId=VpcId,
            SubnetMappings=SubnetMappings,
            DeleteProtection=DeleteProtection,
            SubnetChangeProtection=SubnetChangeProtection,
            FirewallPolicyChangeProtection=FirewallPolicyChangeProtection,
            Description=Description,
            Tags=Tags,
            EncryptionConfiguration=EncryptionConfiguration,
            AvailabilityZoneChangeProtection=AvailabilityZoneChangeProtection)
        self._firewalls[rec.FirewallArn] = rec
        if Tags:
            self._tags[rec.FirewallArn] = {t.get("Key", t.get("key","")): t.get("Value", t.get("value","")) for t in Tags}
        return {"Firewall": rec.to_dict(),
                "FirewallStatus": rec.Status.to_dict()}

    def describe_firewall(self, FirewallArn=None, FirewallName=None):
        rec = None
        if FirewallArn:
            rec = self._firewalls.get(FirewallArn)
        elif FirewallName:
            for f in self._firewalls.values():
                if f.FirewallName == FirewallName:
                    rec = f
                    break
        if not rec:
            raise ResourceNotFoundException("Firewall not found")
        return {"Firewall": rec.to_dict(),
                "FirewallStatus": rec.Status.to_dict(),
                "UpdateToken": uuid.uuid4().hex}

    def describe_firewall_metadata(self, FirewallArn=None, FirewallName=None):
        rec = None
        if FirewallArn:
            rec = self._firewalls.get(FirewallArn)
        elif FirewallName:
            for f in self._firewalls.values():
                if f.FirewallName == FirewallName:
                    rec = f
                    break
        if not rec:
            raise ResourceNotFoundException("Firewall not found")
        return {"FirewallArn": rec.FirewallArn,
                "FirewallName": rec.FirewallName,
                "Description": rec.Description}

    def delete_firewall(self, FirewallArn=None, FirewallName=None):
        rec = None
        if FirewallArn:
            rec = self._firewalls.pop(FirewallArn, None)
        elif FirewallName:
            for arn, f in list(self._firewalls.items()):
                if f.FirewallName == FirewallName:
                    rec = f
                    del self._firewalls[arn]
                    break
        if not rec:
            raise ResourceNotFoundException("Firewall not found")
        self._tags.pop(rec.FirewallArn, None)
        return {"Firewall": rec.to_dict(),
                "FirewallStatus": rec.Status.to_dict()}

    def list_firewalls(self, MaxResults=None, NextToken=None, VpcIds=None):
        fws = list(self._firewalls.values())
        if VpcIds:
            fws = [f for f in fws if f.VpcId in VpcIds]
        token = None
        if MaxResults and len(fws) > MaxResults:
            token = fws[MaxResults].FirewallArn
            fws = fws[:MaxResults]
        return {"Firewalls": [f.to_dict() for f in fws],
                "NextToken": token}

    # ── Firewall update-protection methods ──────────────────────────

    def update_firewall_delete_protection(self, FirewallArn=None,
                                          FirewallName=None,
                                          DeleteProtection=False):
        rec = self._resolve_firewall(FirewallArn, FirewallName)
        rec.DeleteProtection = DeleteProtection
        return {"FirewallArn": rec.FirewallArn,
                "FirewallName": rec.FirewallName,
                "DeleteProtection": rec.DeleteProtection,
                "UpdateToken": uuid.uuid4().hex}

    def update_firewall_description(self, FirewallArn=None,
                                    FirewallName=None,
                                    Description=""):
        rec = self._resolve_firewall(FirewallArn, FirewallName)
        rec.Description = Description
        return {"FirewallArn": rec.FirewallArn,
                "FirewallName": rec.FirewallName,
                "Description": rec.Description,
                "UpdateToken": uuid.uuid4().hex}

    def update_firewall_policy_change_protection(self, FirewallArn=None,
                                                  FirewallName=None,
                                                  FirewallPolicyChangeProtection=False):
        rec = self._resolve_firewall(FirewallArn, FirewallName)
        rec.FirewallPolicyChangeProtection = FirewallPolicyChangeProtection
        return {"FirewallArn": rec.FirewallArn,
                "FirewallName": rec.FirewallName,
                "FirewallPolicyChangeProtection": rec.FirewallPolicyChangeProtection,
                "UpdateToken": uuid.uuid4().hex}

    def update_subnet_change_protection(self, FirewallArn=None,
                                        FirewallName=None,
                                        SubnetChangeProtection=False):
        rec = self._resolve_firewall(FirewallArn, FirewallName)
        rec.SubnetChangeProtection = SubnetChangeProtection
        return {"FirewallArn": rec.FirewallArn,
                "FirewallName": rec.FirewallName,
                "SubnetChangeProtection": rec.SubnetChangeProtection,
                "UpdateToken": uuid.uuid4().hex}

    def _resolve_firewall(self, arn, name):
        if arn:
            rec = self._firewalls.get(arn)
            if rec:
                return rec
        if name:
            for f in self._firewalls.values():
                if f.FirewallName == name:
                    return f
        raise ResourceNotFoundException("Firewall not found")

    # ── FirewallPolicy CRUD ─────────────────────────────────────────

    def create_firewall_policy(self, FirewallPolicyName, FirewallPolicy,
                               Description="", Tags=None,
                               EncryptionConfiguration=None):
        for p in self._policies.values():
            if p.FirewallPolicyName == FirewallPolicyName:
                raise InvalidRequestException(
                    f"Firewall policy '{FirewallPolicyName}' already exists")
        rec = FirewallPolicyRecord(
            FirewallPolicyName=FirewallPolicyName,
            FirewallPolicy=FirewallPolicy,
            Description=Description,
            Tags=Tags,
            EncryptionConfiguration=EncryptionConfiguration)
        self._policies[rec.FirewallPolicyArn] = rec
        if Tags:
            self._tags[rec.FirewallPolicyArn] = {t.get("Key", t.get("key","")): t.get("Value", t.get("value","")) for t in Tags}
        return {"FirewallPolicyResponse": rec.to_dict(),
                "UpdateToken": uuid.uuid4().hex}

    def describe_firewall_policy(self, FirewallPolicyArn=None,
                                  FirewallPolicyName=None):
        rec = self._resolve_policy(FirewallPolicyArn, FirewallPolicyName)
        return {"FirewallPolicyResponse": rec.to_dict(),
                "FirewallPolicy": rec.FirewallPolicy.to_dict(),
                "UpdateToken": uuid.uuid4().hex}

    def update_firewall_policy(self, UpdateToken, FirewallPolicy,
                               FirewallPolicyArn=None,
                               FirewallPolicyName=None,
                               Description=None,
                               EncryptionConfiguration=None):
        rec = self._resolve_policy(FirewallPolicyArn, FirewallPolicyName)
        if isinstance(FirewallPolicy, dict):
            rec.FirewallPolicy = FirewallPolicyData(**FirewallPolicy)
        if Description is not None:
            rec.Description = Description
        if EncryptionConfiguration is not None:
            if isinstance(EncryptionConfiguration, dict):
                rec.EncryptionConfiguration = EncryptionConfiguration(**EncryptionConfiguration)
            else:
                rec.EncryptionConfiguration = EncryptionConfiguration
        return {"FirewallPolicyResponse": rec.to_dict(),
                "UpdateToken": uuid.uuid4().hex}

    def delete_firewall_policy(self, FirewallPolicyArn=None,
                                FirewallPolicyName=None):
        rec = self._resolve_policy(FirewallPolicyArn, FirewallPolicyName)
        # Check no firewalls use this policy
        for f in self._firewalls.values():
            if f.FirewallPolicyArn == rec.FirewallPolicyArn:
                raise InvalidRequestException(
                    "Can't delete policy — it's associated with a firewall")
        if FirewallPolicyArn:
            del self._policies[FirewallPolicyArn]
        else:
            for k, v in list(self._policies.items()):
                if v == rec:
                    del self._policies[k]
                    break
        self._tags.pop(rec.FirewallPolicyArn, None)
        return {"FirewallPolicyResponse": rec.to_dict()}

    def list_firewall_policies(self, MaxResults=None, NextToken=None):
        pols = list(self._policies.values())
        token = None
        if MaxResults and len(pols) > MaxResults:
            token = pols[MaxResults].FirewallPolicyArn
            pols = pols[:MaxResults]
        return {"FirewallPolicies": [p.to_dict() for p in pols],
                "NextToken": token}

    def _resolve_policy(self, arn, name):
        if arn:
            rec = self._policies.get(arn)
            if rec:
                return rec
        if name:
            for p in self._policies.values():
                if p.FirewallPolicyName == name:
                    return p
        raise ResourceNotFoundException("Firewall policy not found")

    # ── RuleGroup CRUD ──────────────────────────────────────────────

    def create_rule_group(self, RuleGroupName, Type, Capacity,
                          RuleGroup=None, Description="", Tags=None,
                          Rules=None, EncryptionConfiguration=None):
        for rg in self._rule_groups.values():
            if rg.RuleGroupName == RuleGroupName and rg.Type == Type:
                raise InvalidRequestException(
                    f"Rule group '{RuleGroupName}' ({Type}) already exists")
        rec = RuleGroupRecord(
            RuleGroupName=RuleGroupName, Type=Type, Capacity=Capacity,
            RuleGroup=RuleGroup, Description=Description, Tags=Tags,
            Rules=Rules, EncryptionConfiguration=EncryptionConfiguration)
        self._rule_groups[rec.RuleGroupArn] = rec
        if Tags:
            self._tags[rec.RuleGroupArn] = {t.get("Key", t.get("key","")): t.get("Value", t.get("value","")) for t in Tags}
        return {"RuleGroupResponse": rec.to_dict(),
                "UpdateToken": uuid.uuid4().hex}

    def describe_rule_group(self, RuleGroupArn=None, RuleGroupName=None,
                            Type=None):
        if RuleGroupArn:
            rec = self._rule_groups.get(RuleGroupArn)
            if not rec:
                raise ResourceNotFoundException("Rule group not found")
        elif RuleGroupName:
            rec = None
            for rg in self._rule_groups.values():
                if rg.RuleGroupName == RuleGroupName:
                    if Type and rg.Type != Type:
                        continue
                    rec = rg
                    break
            if not rec:
                raise ResourceNotFoundException("Rule group not found")
        else:
            raise InvalidRequestException("Must provide RuleGroupArn or RuleGroupName")
        return {"RuleGroupResponse": rec.to_dict(),
                "RuleGroup": rec.RuleGroup.to_dict(),
                "UpdateToken": uuid.uuid4().hex}

    def update_rule_group(self, UpdateToken,
                          RuleGroupArn=None, RuleGroupName=None,
                          Type=None, RuleGroup=None, Description=None,
                          Rules=None, EncryptionConfiguration=None):
        if RuleGroupArn:
            rec = self._rule_groups.get(RuleGroupArn)
        elif RuleGroupName:
            rec = None
            for rg in self._rule_groups.values():
                if rg.RuleGroupName == RuleGroupName:
                    if Type and rg.Type != Type:
                        continue
                    rec = rg
                    break
        if not rec:
            raise ResourceNotFoundException("Rule group not found")
        if RuleGroup is not None:
            if isinstance(RuleGroup, dict):
                rec.RuleGroup = RuleGroupData(**RuleGroup)
        if Description is not None:
            rec.Description = Description
        if Rules is not None:
            rec.Rules = Rules
        if EncryptionConfiguration is not None:
            if isinstance(EncryptionConfiguration, dict):
                rec.EncryptionConfiguration = EncryptionConfiguration(**EncryptionConfiguration)
            else:
                rec.EncryptionConfiguration = EncryptionConfiguration
        return {"RuleGroupResponse": rec.to_dict(),
                "UpdateToken": uuid.uuid4().hex}

    def delete_rule_group(self, RuleGroupArn=None, RuleGroupName=None,
                          Type=None):
        rec = self._resolve_rule_group(RuleGroupArn, RuleGroupName, Type)
        if RuleGroupArn:
            del self._rule_groups[RuleGroupArn]
        else:
            for k, v in list(self._rule_groups.items()):
                if v == rec:
                    del self._rule_groups[k]
                    break
        self._tags.pop(rec.RuleGroupArn, None)
        return {"RuleGroupResponse": rec.to_dict()}

    def list_rule_groups(self, MaxResults=None, NextToken=None, Scope=None,
                         ManagedType=None, Type=None):
        rgs = list(self._rule_groups.values())
        if Type:
            rgs = [rg for rg in rgs if rg.Type == Type]
        token = None
        if MaxResults and len(rgs) > MaxResults:
            token = rgs[MaxResults].RuleGroupArn
            rgs = rgs[:MaxResults]
        return {"RuleGroups": [rg.to_dict() for rg in rgs],
                "NextToken": token}

    def _resolve_rule_group(self, arn, name, type_):
        if arn:
            rec = self._rule_groups.get(arn)
            if rec:
                return rec
        if name:
            for rg in self._rule_groups.values():
                if rg.RuleGroupName == name:
                    if type_ and rg.Type != type_:
                        continue
                    return rg
        raise ResourceNotFoundException("Rule group not found")

    # ── Tags ────────────────────────────────────────────────────────

    def tag_resource(self, ResourceArn, Tags):
        tag_dict = self._tags.get(ResourceArn, {})
        for t in Tags:
            tag_dict[t.get("Key", t.get("key",""))] = t.get("Value", t.get("value",""))
        self._tags[ResourceArn] = tag_dict
        return {}

    def untag_resource(self, ResourceArn, TagKeys):
        if ResourceArn in self._tags:
            for k in TagKeys:
                self._tags[ResourceArn].pop(k, None)
        return {}

    def list_tags_for_resource(self, ResourceArn, MaxResults=None, NextToken=None):
        tags = self._tags.get(ResourceArn, {})
        result = [{"Key": k, "Value": v} for k, v in tags.items()]
        return {"Tags": result}
