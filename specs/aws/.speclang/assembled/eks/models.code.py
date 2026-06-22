"""EKS Store — Cluster lifecycle, node groups, Fargate profiles, addons, access management.

Supports 28 core operations across 5 entities:
- Cluster (Create/Delete/Describe/List/UpdateConfig/UpdateVersion)
- Nodegroup (Create/Delete/Describe/List/UpdateConfig/UpdateVersion)
- FargateProfile (Create/Delete/Describe/List)
- Addon (Create/Delete/Describe/List/Update)
- AccessEntry (Create/Delete/Describe/List/Update)
- TagOperations (TagResource/UntagResource/ListTagsForResource)
"""

import uuid
import time
from collections import defaultdict


def _uid():
    return uuid.uuid4().hex[:8]


def _now():
    return int(time.time())


# ── Exception Classes ────────────────────────────────────────────

class InvalidParameterException(Exception):
    """Invalid parameter in request."""
    def __init__(self, message="Invalid parameter"):
        self.message = message
        super().__init__(message)


class InvalidRequestException(Exception):
    """Invalid request."""
    def __init__(self, message="Invalid request"):
        self.message = message
        super().__init__(message)


class ResourceNotFoundException(Exception):
    """Resource not found."""
    def __init__(self, message="Resource not found"):
        self.message = message
        super().__init__(message)


class ResourceInUseException(Exception):
    """Resource is in use and cannot be deleted."""
    def __init__(self, message="Resource in use"):
        self.message = message
        super().__init__(message)


class ResourceLimitExceededException(Exception):
    """Resource limit exceeded."""
    def __init__(self, message="Resource limit exceeded"):
        self.message = message
        super().__init__(message)


class ServerException(Exception):
    """Internal server error."""
    def __init__(self, message="Internal server error"):
        self.message = message
        super().__init__(message)


class UnsupportedAvailabilityZoneException(Exception):
    """Unsupported AZ."""
    def __init__(self, message="Unsupported AZ"):
        self.message = message
        super().__init__(message)


# ── Record Classes ────────────────────────────────────────────────

class VpcConfigResponse:
    def __init__(self, subnetIds=None, securityGroupIds=None, clusterSecurityGroupId=None,
                 vpcId=None, endpointPublicAccess=None, endpointPrivateAccess=None,
                 publicAccessCidrs=None):
        self.subnetIds = subnetIds or []
        self.securityGroupIds = securityGroupIds or []
        self.clusterSecurityGroupId = clusterSecurityGroupId or ""
        self.vpcId = vpcId or ""
        self.endpointPublicAccess = endpointPublicAccess if endpointPublicAccess is not None else True
        self.endpointPrivateAccess = endpointPrivateAccess if endpointPrivateAccess is not None else False
        self.publicAccessCidrs = publicAccessCidrs or []


class KubernetesNetworkConfigResponse:
    def __init__(self, serviceIpv4Cidr=None, serviceIpv6Cidr=None, ipFamily=None,
                 elasticLoadBalancing=None):
        self.serviceIpv4Cidr = serviceIpv4Cidr or ""
        self.serviceIpv6Cidr = serviceIpv6Cidr or ""
        self.ipFamily = ipFamily or "ipv4"
        self.elasticLoadBalancing = elasticLoadBalancing or {}


class Logging:
    def __init__(self, clusterLogging=None):
        self.clusterLogging = clusterLogging or []


class ClusterRecord:
    def __init__(self, name, version=None, roleArn=None, resourcesVpcConfig=None,
                 kubernetesNetworkConfig=None, logging=None, tags=None, **kwargs):
        self.name = name
        self.arn = f"arn:aws:eks:us-east-1:123456789012:cluster/{name}"
        self.version = version or "1.32"
        self.roleArn = roleArn or ""
        # Convert dict to VpcConfigResponse if needed
        if isinstance(resourcesVpcConfig, dict):
            self.resourcesVpcConfig = VpcConfigResponse(**resourcesVpcConfig)
        else:
            self.resourcesVpcConfig = resourcesVpcConfig or VpcConfigResponse()
        if isinstance(kubernetesNetworkConfig, dict):
            self.kubernetesNetworkConfig = KubernetesNetworkConfigResponse(**kubernetesNetworkConfig)
        else:
            self.kubernetesNetworkConfig = kubernetesNetworkConfig or KubernetesNetworkConfigResponse()
        if isinstance(logging, dict):
            self.logging = Logging(**logging)
        else:
            self.logging = logging or Logging()
        self.tags = tags or {}
        self.status = "ACTIVE"
        self.endpoint = f"https://{_uid()}.gr7.us-east-1.eks.amazonaws.com"
        self.certificateAuthority = {"data": "LS0tLS1CRUdJTi...BASE64..."}
        self.identity = {"oidc": {"issuer": f"https://oidc.eks.us-east-1.amazonaws.com/id/{_uid()}"}}
        self.createdAt = _now()
        self.platformVersion = "eks.5"
        self.accessConfig = {"authenticationMode": "API_AND_CONFIG_MAP"}
        self.upgradePolicy = {"supportType": "STANDARD"}
        self.zonalShiftConfig = {"enabled": False}


class NodegroupScalingConfig:
    def __init__(self, minSize=None, maxSize=None, desiredSize=None):
        self.minSize = minSize or 1
        self.maxSize = maxSize or 3
        self.desiredSize = desiredSize or 1


class NodegroupRecord:
    def __init__(self, nodegroupName, clusterName, scalingConfig=None,
                 subnets=None, instanceTypes=None, amiType=None, tags=None, **kwargs):
        self.nodegroupName = nodegroupName
        self.nodegroupArn = f"arn:aws:eks:us-east-1:123456789012:nodegroup/{clusterName}/{nodegroupName}/{_uid()}"
        self.clusterName = clusterName
        self.scalingConfig = scalingConfig or NodegroupScalingConfig()
        self.subnets = subnets or []
        self.instanceTypes = instanceTypes or ["t3.medium"]
        self.amiType = amiType or "AL2_x86_64"
        self.tags = tags or {}
        self.status = "ACTIVE"
        self.version = "1.32"
        self.releaseVersion = "1.32.0-20250101"
        self.createdAt = _now()
        self.modifiedAt = _now()
        self.nodeRole = ""
        self.labels = {}
        self.taints = []
        self.resources = {"autoScalingGroups": [{"name": f"{clusterName}-{_uid()}"}],
                          "remoteAccessSecurityGroup": ""}
        self.diskSize = 20
        self.health = {"issues": []}
        self.launchTemplate = None
        self.capacityType = "ON_DEMAND"
        self.updateConfig = {"maxUnavailable": 1}
        self.nodeRepairConfig = {"enabled": True}


class FargateProfileSelector:
    def __init__(self, namespace=None, labels=None):
        self.namespace = namespace or "default"
        self.labels = labels or {}


class FargateProfileRecord:
    def __init__(self, fargateProfileName, clusterName, podExecutionRoleArn=None,
                 subnets=None, selectors=None, tags=None, **kwargs):
        self.fargateProfileName = fargateProfileName
        self.fargateProfileArn = f"arn:aws:eks:us-east-1:123456789012:fargateprofile/{clusterName}/{fargateProfileName}/{_uid()}"
        self.clusterName = clusterName
        self.podExecutionRoleArn = podExecutionRoleArn or ""
        self.subnets = subnets or []
        self.selectors = selectors or [FargateProfileSelector()]
        self.tags = tags or {}
        self.status = "ACTIVE"
        self.createdAt = _now()


class AddonRecord:
    def __init__(self, addonName, clusterName, addonVersion=None,
                 serviceAccountRoleArn=None, tags=None, **kwargs):
        self.addonName = addonName
        self.clusterName = clusterName
        self.addonVersion = addonVersion or "v1.0.0-eksbuild.1"
        self.serviceAccountRoleArn = serviceAccountRoleArn or ""
        self.tags = tags or {}
        self.status = "ACTIVE"
        self.addonArn = f"arn:aws:eks:us-east-1:123456789012:addon/{clusterName}/{addonName}/{_uid()}"
        self.createdAt = _now()
        self.modifiedAt = _now()
        self.health = {"issues": []}
        self.configurationValues = ""
        self.marketplaceInformation = None
        self.podIdentityAssociations = []


class AccessEntryRecord:
    def __init__(self, clusterName, principalArn, kubernetesGroups=None,
                 tags=None, username=None, **kwargs):
        self.clusterName = clusterName
        self.principalArn = principalArn
        self.kubernetesGroups = kubernetesGroups or []
        self.tags = tags or {}
        self.username = username or ""
        self.accessEntryArn = f"arn:aws:eks:us-east-1:123456789012:access-entry/{clusterName}/{_uid()}"
        self.createdAt = _now()
        self.modifiedAt = _now()
        self.type = "STANDARD"


class AssociatedAccessPolicy:
    def __init__(self, policyArn, accessScope=None):
        self.policyArn = policyArn
        self.accessScope = accessScope or {"type": "cluster"}
        self.associatedAt = _now()
        self.modifiedAt = _now()


class UpdateRecord:
    def __init__(self, updateId, updateType, params=None, status="Successful"):
        self.id = updateId
        self.type = updateType
        self.params = params or []
        self.status = status
        self.createdAt = _now()
        self.errors = []


# ── EKS Store ──────────────────────────────────────────────────

class EKSStore:
    """In-memory store for EKS resources."""

    def __init__(self):
        self._clusters: dict[str, ClusterRecord] = {}
        self._nodegroups: dict[str, dict[str, NodegroupRecord]] = defaultdict(dict)
        self._fargate_profiles: dict[str, dict[str, FargateProfileRecord]] = defaultdict(dict)
        self._addons: dict[str, dict[str, AddonRecord]] = defaultdict(dict)
        self._access_entries: dict[str, dict[str, AccessEntryRecord]] = defaultdict(dict)
        self._access_policies: dict[str, dict[str, list[AssociatedAccessPolicy]]] = defaultdict(lambda: defaultdict(list))
        self._updates: dict[str, list[UpdateRecord]] = defaultdict(list)

    # ── Clusters ───────────────────────────────────────────────

    def create_cluster(self, name, **kwargs):
        if name in self._clusters:
            raise ResourceInUseException(f"Cluster {name} already exists")
        record = ClusterRecord(name=name, **kwargs)
        self._clusters[name] = record
        self._updates[name] = []
        return {"cluster": self._to_cluster_dict(record)}

    def describe_cluster(self, name):
        record = self._clusters.get(name)
        if not record:
            raise ResourceNotFoundException(f"Cluster {name} not found")
        return {"cluster": self._to_cluster_dict(record)}

    def list_clusters(self):
        return {"clusters": sorted(self._clusters.keys())}

    def delete_cluster(self, name):
        if name not in self._clusters:
            raise ResourceNotFoundException(f"Cluster {name} not found")
        # Check for dependent resources
        if self._nodegroups.get(name):
            raise ResourceInUseException(f"Cluster {name} has node groups")
        if self._fargate_profiles.get(name):
            raise ResourceInUseException(f"Cluster {name} has Fargate profiles")
        del self._clusters[name]
        return {"cluster": {"name": name, "status": "DELETING"}}

    def update_cluster_config(self, name, **kwargs):
        record = self._clusters.get(name)
        if not record:
            raise ResourceNotFoundException(f"Cluster {name} not found")
        if "resourcesVpcConfig" in kwargs:
            vpc = kwargs["resourcesVpcConfig"]
            if isinstance(vpc, dict):
                record.resourcesVpcConfig = VpcConfigResponse(**vpc)
            else:
                record.resourcesVpcConfig = vpc
        if "logging" in kwargs:
            lg = kwargs["logging"]
            if isinstance(lg, dict):
                record.logging = Logging(**lg)
            else:
                record.logging = lg
        if "accessConfig" in kwargs:
            record.accessConfig = kwargs["accessConfig"]
        if "upgradePolicy" in kwargs:
            record.upgradePolicy = kwargs["upgradePolicy"]
        update_id = _uid()
        self._updates[name].append(UpdateRecord(update_id, "ConfigUpdate"))
        return {"update": {"id": update_id, "status": "Successful"}}

    def update_cluster_version(self, name, version, **kwargs):
        record = self._clusters.get(name)
        if not record:
            raise ResourceNotFoundException(f"Cluster {name} not found")
        record.version = version
        update_id = _uid()
        self._updates[name].append(UpdateRecord(update_id, "VersionUpdate", [{"type": "Version", "value": version}]))
        return {"update": {"id": update_id, "status": "Successful"}}

    # ── Nodegroups ─────────────────────────────────────────────

    def create_nodegroup(self, clusterName, nodegroupName, **kwargs):
        if clusterName not in self._clusters:
            raise ResourceNotFoundException(f"Cluster {clusterName} not found")
        if nodegroupName in self._nodegroups[clusterName]:
            raise ResourceInUseException(f"Nodegroup {nodegroupName} already exists")
        record = NodegroupRecord(clusterName=clusterName, nodegroupName=nodegroupName, **kwargs)
        self._nodegroups[clusterName][nodegroupName] = record
        return {"nodegroup": self._to_nodegroup_dict(record)}

    def describe_nodegroup(self, clusterName, nodegroupName):
        record = self._nodegroups.get(clusterName, {}).get(nodegroupName)
        if not record:
            raise ResourceNotFoundException(f"Nodegroup {nodegroupName} not found in cluster {clusterName}")
        return {"nodegroup": self._to_nodegroup_dict(record)}

    def list_nodegroups(self, clusterName):
        if clusterName not in self._clusters:
            raise ResourceNotFoundException(f"Cluster {clusterName} not found")
        return {"nodegroups": sorted(self._nodegroups[clusterName].keys())}

    def delete_nodegroup(self, clusterName, nodegroupName):
        record = self._nodegroups.get(clusterName, {}).get(nodegroupName)
        if not record:
            raise ResourceNotFoundException(f"Nodegroup {nodegroupName} not found")
        del self._nodegroups[clusterName][nodegroupName]
        return {"nodegroup": {"nodegroupName": nodegroupName, "status": "DELETING"}}

    def update_nodegroup_config(self, clusterName, nodegroupName, **kwargs):
        record = self._nodegroups.get(clusterName, {}).get(nodegroupName)
        if not record:
            raise ResourceNotFoundException(f"Nodegroup {nodegroupName} not found")
        if "scalingConfig" in kwargs:
            record.scalingConfig = NodegroupScalingConfig(**kwargs["scalingConfig"])
        if "labels" in kwargs:
            record.labels = kwargs["labels"]
        if "taints" in kwargs:
            record.taints = kwargs.get("taints", {}).get("addOrUpdateTaints", [])
        update_id = _uid()
        return {"update": {"id": update_id, "status": "Successful"}}

    def update_nodegroup_version(self, clusterName, nodegroupName, version=None, **kwargs):
        record = self._nodegroups.get(clusterName, {}).get(nodegroupName)
        if not record:
            raise ResourceNotFoundException(f"Nodegroup {nodegroupName} not found")
        if version:
            record.version = version
        update_id = _uid()
        return {"update": {"id": update_id, "status": "Successful"}}

    # ── Fargate Profiles ───────────────────────────────────────

    def create_fargate_profile(self, clusterName, fargateProfileName, **kwargs):
        if clusterName not in self._clusters:
            raise ResourceNotFoundException(f"Cluster {clusterName} not found")
        if fargateProfileName in self._fargate_profiles[clusterName]:
            raise ResourceInUseException(f"Fargate profile {fargateProfileName} already exists")
        record = FargateProfileRecord(clusterName=clusterName, fargateProfileName=fargateProfileName, **kwargs)
        self._fargate_profiles[clusterName][fargateProfileName] = record
        return {"fargateProfile": self._to_fargate_dict(record)}

    def describe_fargate_profile(self, clusterName, fargateProfileName):
        record = self._fargate_profiles.get(clusterName, {}).get(fargateProfileName)
        if not record:
            raise ResourceNotFoundException(f"Fargate profile {fargateProfileName} not found")
        return {"fargateProfile": self._to_fargate_dict(record)}

    def list_fargate_profiles(self, clusterName):
        if clusterName not in self._clusters:
            raise ResourceNotFoundException(f"Cluster {clusterName} not found")
        return {"fargateProfileNames": sorted(self._fargate_profiles[clusterName].keys())}

    def delete_fargate_profile(self, clusterName, fargateProfileName):
        record = self._fargate_profiles.get(clusterName, {}).get(fargateProfileName)
        if not record:
            raise ResourceNotFoundException(f"Fargate profile {fargateProfileName} not found")
        del self._fargate_profiles[clusterName][fargateProfileName]
        return {"fargateProfile": {"fargateProfileName": fargateProfileName, "status": "DELETING"}}

    # ── Addons ─────────────────────────────────────────────────

    def create_addon(self, clusterName, addonName, **kwargs):
        if clusterName not in self._clusters:
            raise ResourceNotFoundException(f"Cluster {clusterName} not found")
        if addonName in self._addons[clusterName]:
            raise ResourceInUseException(f"Addon {addonName} already exists")
        record = AddonRecord(clusterName=clusterName, addonName=addonName, **kwargs)
        self._addons[clusterName][addonName] = record
        return {"addon": self._to_addon_dict(record)}

    def describe_addon(self, clusterName, addonName):
        record = self._addons.get(clusterName, {}).get(addonName)
        if not record:
            raise ResourceNotFoundException(f"Addon {addonName} not found in cluster {clusterName}")
        return {"addon": self._to_addon_dict(record)}

    def list_addons(self, clusterName):
        if clusterName not in self._clusters:
            raise ResourceNotFoundException(f"Cluster {clusterName} not found")
        return {"addons": sorted(self._addons[clusterName].keys())}

    def delete_addon(self, clusterName, addonName):
        record = self._addons.get(clusterName, {}).get(addonName)
        if not record:
            raise ResourceNotFoundException(f"Addon {addonName} not found")
        del self._addons[clusterName][addonName]
        return {"addon": {"addonName": addonName, "status": "DELETING"}}

    def update_addon(self, clusterName, addonName, **kwargs):
        record = self._addons.get(clusterName, {}).get(addonName)
        if not record:
            raise ResourceNotFoundException(f"Addon {addonName} not found")
        if "addonVersion" in kwargs:
            record.addonVersion = kwargs["addonVersion"]
        if "serviceAccountRoleArn" in kwargs:
            record.serviceAccountRoleArn = kwargs["serviceAccountRoleArn"]
        return {"update": {"id": _uid(), "status": "Successful"}}

    # ── Access Entries ─────────────────────────────────────────

    def create_access_entry(self, clusterName, principalArn, **kwargs):
        if clusterName not in self._clusters:
            raise ResourceNotFoundException(f"Cluster {clusterName} not found")
        if principalArn in self._access_entries[clusterName]:
            raise ResourceInUseException(f"Access entry for {principalArn} already exists")
        record = AccessEntryRecord(clusterName=clusterName, principalArn=principalArn, **kwargs)
        self._access_entries[clusterName][principalArn] = record
        return {"accessEntry": self._to_access_entry_dict(record)}

    def describe_access_entry(self, clusterName, principalArn):
        record = self._access_entries.get(clusterName, {}).get(principalArn)
        if not record:
            raise ResourceNotFoundException(f"Access entry for {principalArn} not found")
        return {"accessEntry": self._to_access_entry_dict(record)}

    def list_access_entries(self, clusterName):
        if clusterName not in self._clusters:
            raise ResourceNotFoundException(f"Cluster {clusterName} not found")
        return {"accessEntries": sorted(self._access_entries[clusterName].keys())}

    def delete_access_entry(self, clusterName, principalArn):
        record = self._access_entries.get(clusterName, {}).get(principalArn)
        if not record:
            raise ResourceNotFoundException(f"Access entry for {principalArn} not found")
        del self._access_entries[clusterName][principalArn]
        return {}

    def update_access_entry(self, clusterName, principalArn, **kwargs):
        record = self._access_entries.get(clusterName, {}).get(principalArn)
        if not record:
            raise ResourceNotFoundException(f"Access entry for {principalArn} not found")
        if "kubernetesGroups" in kwargs:
            record.kubernetesGroups = kwargs["kubernetesGroups"]
        if "username" in kwargs:
            record.username = kwargs["username"]
        return {"accessEntry": self._to_access_entry_dict(record)}

    # ── Access Policies (associated with access entries) ───────

    def associate_access_policy(self, clusterName, principalArn, policyArn, accessScope=None):
        record = self._access_entries.get(clusterName, {}).get(principalArn)
        if not record:
            raise ResourceNotFoundException(f"Access entry for {principalArn} not found")
        ap = AssociatedAccessPolicy(policyArn, accessScope)
        self._access_policies[clusterName][principalArn].append(ap)
        return {"clusterName": clusterName, "principalArn": principalArn,
                "associatedAccessPolicy": {"policyArn": policyArn, "accessScope": ap.accessScope,
                                           "associatedAt": ap.associatedAt}}

    def disassociate_access_policy(self, clusterName, principalArn, policyArn):
        policies = self._access_policies.get(clusterName, {}).get(principalArn, [])
        self._access_policies[clusterName][principalArn] = [p for p in policies if p.policyArn != policyArn]
        return {}

    def list_associated_access_policies(self, clusterName, principalArn):
        policies = self._access_policies.get(clusterName, {}).get(principalArn, [])
        return {"clusterName": clusterName, "principalArn": principalArn,
                "associatedAccessPolicies": [{"policyArn": p.policyArn, "accessScope": p.accessScope,
                                              "associatedAt": p.associatedAt} for p in policies]}

    # ── Tags ───────────────────────────────────────────────────

    def tag_resource(self, resourceArn, tags):
        """Apply tags to any EKS resource by ARN lookup."""
        for coll_name, coll in [("_clusters", self._clusters), ("_nodegroups", self._nodegroups)]:
            if isinstance(coll, dict):
                if coll_name == "_clusters":
                    for name, rec in coll.items():
                        if rec.arn == resourceArn:
                            rec.tags.update(tags)
                            return {}
                elif coll_name == "_nodegroups":
                    for cn, ng_map in coll.items():
                        for nn, rec in ng_map.items():
                            if rec.nodegroupArn == resourceArn:
                                rec.tags.update(tags)
                                return {}
        raise ResourceNotFoundException(f"Resource {resourceArn} not found")

    def untag_resource(self, resourceArn, tagKeys):
        for coll_name, coll in [("_clusters", self._clusters), ("_nodegroups", self._nodegroups)]:
            if coll_name == "_clusters":
                for name, rec in coll.items():
                    if rec.arn == resourceArn:
                        for k in tagKeys:
                            rec.tags.pop(k, None)
                        return {}
            elif coll_name == "_nodegroups":
                for cn, ng_map in coll.items():
                    for nn, rec in ng_map.items():
                        if rec.nodegroupArn == resourceArn:
                            for k in tagKeys:
                                rec.tags.pop(k, None)
                            return {}
        raise ResourceNotFoundException(f"Resource {resourceArn} not found")

    def list_tags_for_resource(self, resourceArn):
        for coll_name, coll in [("_clusters", self._clusters), ("_nodegroups", self._nodegroups)]:
            if coll_name == "_clusters":
                for name, rec in coll.items():
                    if rec.arn == resourceArn:
                        return {"tags": dict(rec.tags)}
            elif coll_name == "_nodegroups":
                for cn, ng_map in coll.items():
                    for nn, rec in ng_map.items():
                        if rec.nodegroupArn == resourceArn:
                            return {"tags": dict(rec.tags)}
        raise ResourceNotFoundException(f"Resource {resourceArn} not found")

    def describe_update(self, name, updateId, **kwargs):
        updates = self._updates.get(name, [])
        for u in updates:
            if u.id == updateId:
                return {"update": {"id": u.id, "type": u.type, "status": u.status,
                                   "params": u.params, "createdAt": u.createdAt, "errors": u.errors}}
        raise ResourceNotFoundException(f"Update {updateId} not found")

    def list_updates(self, name, **kwargs):
        updates = self._updates.get(name, [])
        return {"updateIds": [u.id for u in updates]}

    # ── Serialization helpers ──────────────────────────────────

    def _to_cluster_dict(self, r):
        return {
            "name": r.name, "arn": r.arn, "version": r.version, "roleArn": r.roleArn,
            "resourcesVpcConfig": {"subnetIds": r.resourcesVpcConfig.subnetIds,
                                    "securityGroupIds": r.resourcesVpcConfig.securityGroupIds,
                                    "vpcId": r.resourcesVpcConfig.vpcId,
                                    "endpointPublicAccess": r.resourcesVpcConfig.endpointPublicAccess,
                                    "endpointPrivateAccess": r.resourcesVpcConfig.endpointPrivateAccess},
            "kubernetesNetworkConfig": {"serviceIpv4Cidr": r.kubernetesNetworkConfig.serviceIpv4Cidr,
                                         "ipFamily": r.kubernetesNetworkConfig.ipFamily},
            "logging": r.logging.__dict__ if hasattr(r.logging, '__dict__') else {},
            "status": r.status, "endpoint": r.endpoint, "certificateAuthority": r.certificateAuthority,
            "identity": r.identity, "createdAt": r.createdAt, "platformVersion": r.platformVersion,
            "tags": r.tags, "accessConfig": r.accessConfig,
        }

    def _to_nodegroup_dict(self, r):
        return {
            "nodegroupName": r.nodegroupName, "nodegroupArn": r.nodegroupArn,
            "clusterName": r.clusterName, "version": r.version, "releaseVersion": r.releaseVersion,
            "status": r.status, "scalingConfig": {"minSize": r.scalingConfig.minSize,
                                                   "maxSize": r.scalingConfig.maxSize,
                                                   "desiredSize": r.scalingConfig.desiredSize},
            "subnets": r.subnets, "instanceTypes": r.instanceTypes, "amiType": r.amiType,
            "tags": r.tags, "createdAt": r.createdAt, "diskSize": r.diskSize,
            "health": r.health, "capacityType": r.capacityType, "resources": r.resources,
        }

    def _to_fargate_dict(self, r):
        return {
            "fargateProfileName": r.fargateProfileName, "fargateProfileArn": r.fargateProfileArn,
            "clusterName": r.clusterName, "podExecutionRoleArn": r.podExecutionRoleArn,
            "subnets": r.subnets, "status": r.status, "createdAt": r.createdAt, "tags": r.tags,
            "selectors": [{"namespace": s.namespace, "labels": s.labels} for s in r.selectors],
        }

    def _to_addon_dict(self, r):
        return {
            "addonName": r.addonName, "clusterName": r.clusterName, "addonVersion": r.addonVersion,
            "status": r.status, "addonArn": r.addonArn, "createdAt": r.createdAt,
            "modifiedAt": r.modifiedAt, "serviceAccountRoleArn": r.serviceAccountRoleArn,
            "tags": r.tags, "health": r.health,
        }

    def _to_access_entry_dict(self, r):
        return {
            "clusterName": r.clusterName, "principalArn": r.principalArn,
            "kubernetesGroups": r.kubernetesGroups, "accessEntryArn": r.accessEntryArn,
            "createdAt": r.createdAt, "modifiedAt": r.modifiedAt, "tags": r.tags,
            "username": r.username, "type": r.type,
        }
