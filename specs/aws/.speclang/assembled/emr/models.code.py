"""EMR emulator store — clusters, instance fleets, groups, steps, security configs, studios."""
import uuid
import time as _time

# ─── Exceptions ───────────────────────────────────────────────────────────────
class ClusterNotFoundFault(Exception):
    pass

class InvalidRequestException(Exception):
    pass

class ValidationException(Exception):
    pass

class AlreadyExistsException(Exception):
    pass


# ─── Record Classes ───────────────────────────────────────────────────────────

class ClusterRecord:
    def __init__(self, Name, Id=None, ReleaseLabel=None, ServiceRole=None,
                 JobFlowRole=None, LogUri=None, Applications=None,
                 Steps=None, BootstrapActions=None, Configurations=None,
                 Tags=None, VisibleToAllUsers=None, AutoTerminate=True,
                 ScaleDownBehavior=None, SecurityConfiguration=None,
                 InstanceCollectionType=None, **kwargs):
        self.Id = Id or 'j-' + str(uuid.uuid4())[:12]
        self.Name = Name
        self.ReleaseLabel = ReleaseLabel
        self.ServiceRole = ServiceRole or "EMR_DefaultRole"
        self.JobFlowRole = JobFlowRole
        self.LogUri = LogUri
        self.Applications = Applications or []
        self.BootstrapActions = BootstrapActions or []
        self.Configurations = Configurations or []
        self.Tags = Tags or []
        self.VisibleToAllUsers = VisibleToAllUsers
        self.AutoTerminate = AutoTerminate
        self.ScaleDownBehavior = ScaleDownBehavior
        self.SecurityConfiguration = SecurityConfiguration
        self.Status = {"State": "WAITING", "StateChangeReason": {}}
        self.Steps = Steps or []
        self.Fleets = {}
        self.Groups = {}
        self.InstanceCollectionType = InstanceCollectionType

    def to_dict(self):
        return {
            "Id": self.Id,
            "Name": self.Name,
            "Status": self.Status,
            "ReleaseLabel": self.ReleaseLabel,
            "ServiceRole": self.ServiceRole,
            "VisibleToAllUsers": self.VisibleToAllUsers if self.VisibleToAllUsers is not None else True,
            "AutoTerminate": self.AutoTerminate,
            "Tags": self.Tags,
            "SecurityConfiguration": self.SecurityConfiguration,
            "Applications": self.Applications,
            "LogUri": self.LogUri,
        }


class InstanceFleetRecord:
    def __init__(self, Id=None, Name=None, InstanceFleetType=None,
                 TargetOnDemandCapacity=None, TargetSpotCapacity=None,
                 InstanceTypeConfigs=None, **kwargs):
        self.Id = Id or 'if-' + str(uuid.uuid4())[:8]
        self.Name = Name
        self.InstanceFleetType = InstanceFleetType or "MASTER"
        self.TargetOnDemandCapacity = TargetOnDemandCapacity or 1
        self.TargetSpotCapacity = TargetSpotCapacity or 0
        self.InstanceTypeConfigs = InstanceTypeConfigs or []
        self.Status = {"State": "RUNNING"}

    def to_dict(self):
        return {
            "Id": self.Id,
            "Name": self.Name,
            "InstanceFleetType": self.InstanceFleetType,
            "Status": self.Status,
            "TargetOnDemandCapacity": self.TargetOnDemandCapacity,
            "TargetSpotCapacity": self.TargetSpotCapacity,
        }


class InstanceGroupRecord:
    def __init__(self, Id=None, Name=None, InstanceRole=None,
                 InstanceType=None, InstanceCount=None,
                 Market=None, **kwargs):
        self.Id = Id or 'ig-' + str(uuid.uuid4())[:8]
        self.Name = Name
        self.InstanceRole = InstanceRole or "MASTER"
        self.InstanceType = InstanceType
        self.InstanceCount = InstanceCount or 1
        self.Market = Market or "ON_DEMAND"
        self.Status = {"State": "RUNNING"}

    def to_dict(self):
        return {
            "Id": self.Id,
            "Name": self.Name,
            "InstanceRole": self.InstanceRole,
            "InstanceType": self.InstanceType,
            "InstanceCount": self.InstanceCount,
            "Market": self.Market,
            "Status": self.Status,
        }


class StepRecord:
    def __init__(self, Id=None, Name=None, ActionOnFailure="CONTINUE",
                 HadoopJarStep=None, **kwargs):
        self.Id = Id or 's-' + str(uuid.uuid4())[:12]
        self.Name = Name or "Unnamed Step"
        self.ActionOnFailure = ActionOnFailure
        self.Status = {"State": "PENDING"}
        if HadoopJarStep and isinstance(HadoopJarStep, dict):
            self.HadoopJarStep = HadoopJarStep

    def to_dict(self):
        d = {
            "Id": self.Id,
            "Name": self.Name,
            "Status": self.Status,
            "ActionOnFailure": self.ActionOnFailure,
        }
        if hasattr(self, 'HadoopJarStep'):
            d["Config"] = {"Jar": self.HadoopJarStep.get("Jar", ""), "Args": self.HadoopJarStep.get("Args", [])}
        return d


class SecurityConfigurationRecord:
    def __init__(self, Name, SecurityConfiguration, **kwargs):
        self.Name = Name
        self.SecurityConfiguration = SecurityConfiguration
        self.CreationDateTime = None

    def to_dict(self):
        return {
            "Name": self.Name,
            "SecurityConfiguration": self.SecurityConfiguration,
            "CreationDateTime": self.CreationDateTime,
        }


class StudioRecord:
    def __init__(self, Name, StudioId=None, Description=None, AuthMode=None,
                 VpcId=None, SubnetIds=None, ServiceRole=None,
                 UserRole=None, WorkspaceSecurityGroupId=None,
                 EngineSecurityGroupId=None, DefaultS3Location=None,
                 Tags=None, **kwargs):
        self.StudioId = StudioId or 'es-' + str(uuid.uuid4())[:8]
        self.Name = Name
        self.Description = Description
        self.AuthMode = AuthMode or "SSO"
        self.VpcId = VpcId
        self.SubnetIds = SubnetIds or []
        self.ServiceRole = ServiceRole
        self.UserRole = UserRole
        self.WorkspaceSecurityGroupId = WorkspaceSecurityGroupId
        self.EngineSecurityGroupId = EngineSecurityGroupId
        self.DefaultS3Location = DefaultS3Location
        self.Tags = Tags or []
        self.Status = "READY"
        self.Url = f"https://{self.StudioId}.emrstudio.aws"

    def to_dict(self):
        return {
            "StudioId": self.StudioId,
            "Name": self.Name,
            "Description": self.Description,
            "AuthMode": self.AuthMode,
            "VpcId": self.VpcId,
            "SubnetIds": self.SubnetIds,
            "ServiceRole": self.ServiceRole,
            "UserRole": self.UserRole,
            "Url": self.Url,
            "Tags": self.Tags,
        }


# ─── EMRStore ─────────────────────────────────────────────────────────────────

class EMRStore:
    def __init__(self):
        self._clusters = {}
        self._security_configs = {}
        self._studios = {}

    # ── Clusters ──────────────────────────────────────────────────────────

    def clusters(self, cluster_id=None):
        if cluster_id is not None:
            return self._clusters.get(cluster_id)
        return list(self._clusters.values())

    def run_job_flow(self, Name, **kwargs):
        record = ClusterRecord(Name, **kwargs)
        self._clusters[record.Id] = record
        return record

    def describe_cluster(self, ClusterId):
        record = self._clusters.get(ClusterId)
        if not record:
            raise ClusterNotFoundFault(f"Cluster {ClusterId} not found")
        return record

    def list_clusters(self, ClusterStates=None, **_kw):
        results = list(self._clusters.values())
        if ClusterStates and isinstance(ClusterStates, list):
            results = [c for c in results if c.Status["State"] in ClusterStates]
        return results

    def terminate_job_flows(self, JobFlowIds):
        for jid in JobFlowIds:
            if jid in self._clusters:
                self._clusters[jid].Status = {"State": "TERMINATED"}

    # ── Instance Fleets ───────────────────────────────────────────────────

    def add_instance_fleet(self, ClusterId, InstanceFleet):
        cluster = self._clusters.get(ClusterId)
        if not cluster:
            raise ClusterNotFoundFault(f"Cluster {ClusterId} not found")
        if isinstance(InstanceFleet, dict):
            fleet = InstanceFleetRecord(**InstanceFleet)
        else:
            fleet = InstanceFleetRecord(**(InstanceFleet.__dict__ if hasattr(InstanceFleet, '__dict__') else {}))
        cluster.Fleets[fleet.Id] = fleet
        return fleet

    def modify_instance_fleet(self, ClusterId, InstanceFleet):
        cluster = self._clusters.get(ClusterId)
        if not cluster:
            raise ClusterNotFoundFault(f"Cluster {ClusterId} not found")
        if isinstance(InstanceFleet, dict) and "InstanceFleetId" in InstanceFleet:
            fid = InstanceFleet["InstanceFleetId"]
            if fid in cluster.Fleets:
                fleet = cluster.Fleets[fid]
                if "TargetOnDemandCapacity" in InstanceFleet:
                    fleet.TargetOnDemandCapacity = InstanceFleet["TargetOnDemandCapacity"]
                if "TargetSpotCapacity" in InstanceFleet:
                    fleet.TargetSpotCapacity = InstanceFleet["TargetSpotCapacity"]

    def list_instance_fleets(self, ClusterId, **_kw):
        cluster = self._clusters.get(ClusterId)
        if not cluster:
            raise ClusterNotFoundFault(f"Cluster {ClusterId} not found")
        return list(cluster.Fleets.values())

    # ── Instance Groups ───────────────────────────────────────────────────

    def add_instance_groups(self, JobFlowId, InstanceGroups):
        cluster = self._clusters.get(JobFlowId)
        if not cluster:
            raise ClusterNotFoundFault(f"Cluster {JobFlowId} not found")
        results = []
        if isinstance(InstanceGroups, list):
            for ig in InstanceGroups:
                if isinstance(ig, dict):
                    rec = InstanceGroupRecord(**ig)
                else:
                    rec = ig
                cluster.Groups[rec.Id] = rec
                results.append(rec)
        return results

    def modify_instance_groups(self, ClusterId=None, InstanceGroups=None):
        if ClusterId and ClusterId in self._clusters:
            cluster = self._clusters[ClusterId]
            if InstanceGroups and isinstance(InstanceGroups, list):
                for mod in InstanceGroups:
                    if isinstance(mod, dict) and "InstanceGroupId" in mod:
                        gid = mod["InstanceGroupId"]
                        if gid in cluster.Groups:
                            g = cluster.Groups[gid]
                            if "InstanceCount" in mod:
                                g.InstanceCount = mod["InstanceCount"]

    def list_instance_groups(self, ClusterId, **_kw):
        cluster = self._clusters.get(ClusterId)
        if not cluster:
            raise ClusterNotFoundFault(f"Cluster {ClusterId} not found")
        return list(cluster.Groups.values())

    # ── Steps ─────────────────────────────────────────────────────────────

    def add_job_flow_steps(self, JobFlowId, Steps, ExecutionRoleArn=None):
        cluster = self._clusters.get(JobFlowId)
        if not cluster:
            raise ClusterNotFoundFault(f"Cluster {JobFlowId} not found")
        results = []
        if isinstance(Steps, list):
            for s in Steps:
                if isinstance(s, dict):
                    rec = StepRecord(**s)
                    cluster.Steps.append(rec)
                    results.append(rec)
        return results

    def cancel_steps(self, ClusterId, StepIds):
        cluster = self._clusters.get(ClusterId)
        if not cluster:
            raise ClusterNotFoundFault(f"Cluster {ClusterId} not found")
        for s in cluster.Steps:
            if s.Id in StepIds:
                s.Status = {"State": "CANCELLED"}

    def describe_step(self, ClusterId, StepId):
        cluster = self._clusters.get(ClusterId)
        if not cluster:
            raise ClusterNotFoundFault(f"Cluster {ClusterId} not found")
        for s in cluster.Steps:
            if s.Id == StepId:
                return s
        raise InvalidRequestException(f"Step {StepId} not found on cluster {ClusterId}")

    def list_steps(self, ClusterId, StepIds=None, StepStates=None, **_kw):
        cluster = self._clusters.get(ClusterId)
        if not cluster:
            raise ClusterNotFoundFault(f"Cluster {ClusterId} not found")
        results = cluster.Steps
        if StepIds:
            results = [s for s in results if s.Id in StepIds]
        if StepStates and isinstance(StepStates, list):
            results = [s for s in results if s.Status["State"] in StepStates]
        return results

    # ── Security Configurations ───────────────────────────────────────────

    def create_security_configuration(self, Name, SecurityConfiguration):
        if Name in self._security_configs:
            raise AlreadyExistsException(f"Security configuration {Name} already exists")
        record = SecurityConfigurationRecord(Name, SecurityConfiguration)
        record.CreationDateTime = _time.time()
        self._security_configs[Name] = record
        return record

    def describe_security_configuration(self, Name):
        if Name not in self._security_configs:
            raise InvalidRequestException(f"Security configuration {Name} not found")
        return self._security_configs[Name]

    def list_security_configurations(self, **_kw):
        return list(self._security_configs.values())

    def delete_security_configuration(self, Name):
        if Name not in self._security_configs:
            raise InvalidRequestException(f"Security configuration {Name} not found")
        del self._security_configs[Name]

    # ── Studios ───────────────────────────────────────────────────────────

    def create_studio(self, Name, **kwargs):
        record = StudioRecord(Name, **kwargs)
        self._studios[record.StudioId] = record
        return record

    def describe_studio(self, StudioId):
        if StudioId not in self._studios:
            raise InvalidRequestException(f"Studio {StudioId} not found")
        return self._studios[StudioId]

    def list_studios(self, **_kw):
        return list(self._studios.values())

    def update_studio(self, StudioId, **kwargs):
        if StudioId not in self._studios:
            raise InvalidRequestException(f"Studio {StudioId} not found")
        record = self._studios[StudioId]
        for k, v in kwargs.items():
            if hasattr(record, k):
                setattr(record, k, v)
        return record

    def delete_studio(self, StudioId):
        if StudioId not in self._studios:
            raise InvalidRequestException(f"Studio {StudioId} not found")
        del self._studios[StudioId]
