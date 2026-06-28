"""DataSync store — Agent, Location, Task, TaskExecution, Tags."""
import uuid


# === Exception Classes ===
class InvalidRequestException(Exception):
    """Invalid request."""
    pass


class InternalException(Exception):
    """Internal error."""
    pass


class ResourceNotFoundException(InvalidRequestException):
    """Resource not found."""
    pass


class ResourceInUseException(InvalidRequestException):
    """Resource already exists."""
    pass


# === Record Classes ===
class AgentRecord:
    def __init__(self, AgentName=None, ActivationKey=None, VpcEndpointId=None,
                 SubnetArns=None, SecurityGroupArns=None, Tags=None):
        self.AgentArn = f"arn:aws:datasync:us-east-1:000000000000:agent/agent-{uuid.uuid4().hex[:8]}"
        self.ActivationKey = ActivationKey or ""
        self.AgentName = AgentName or ""
        self.VpcEndpointId = VpcEndpointId or ""
        self.SubnetArns = SubnetArns or []
        self.SecurityGroupArns = SecurityGroupArns or []
        self.Status = "ONLINE"
        self.Tags = _convert_tags(Tags)

    def to_dict(self):
        return {
            "AgentArn": self.AgentArn,
            "ActivationKey": self.ActivationKey,
            "AgentName": self.AgentName,
            "VpcEndpointId": self.VpcEndpointId,
            "SubnetArns": self.SubnetArns,
            "SecurityGroupArns": self.SecurityGroupArns,
            "Status": self.Status,
        }


class LocationRecord:
    def __init__(self, LocationType="S3", **kwargs):
        self.LocationArn = f"arn:aws:datasync:us-east-1:000000000000:location/loc-{uuid.uuid4().hex[:8]}"
        self.LocationType = LocationType
        self.LocationUri = kwargs.get("LocationUri", "")
        self.Tags = _convert_tags(kwargs.get("Tags"))
        # Store all raw fields for describe
        self._fields = dict(kwargs)

    def to_dict(self):
        d = {
            "LocationArn": self.LocationArn,
            "LocationUri": self.LocationUri,
            "LocationType": self.LocationType,
        }
        # Merge stored fields
        for k, v in self._fields.items():
            if k not in ("Tags", "LocationUri", "LocationType"):
                d[k] = v
        return d


class TaskRecord:
    def __init__(self, SourceLocationArn=None, DestinationLocationArn=None,
                 Name=None, CloudWatchLogGroupArn=None, Options=None,
                 Excludes=None, Schedule=None, Tags=None, Includes=None,
                 ManifestConfig=None, TaskReportConfig=None, TaskMode=None):
        self.TaskArn = f"arn:aws:datasync:us-east-1:000000000000:task/task-{uuid.uuid4().hex[:8]}"
        self.SourceLocationArn = SourceLocationArn or ""
        self.DestinationLocationArn = DestinationLocationArn or ""
        self.Name = Name or ""
        self.CloudWatchLogGroupArn = CloudWatchLogGroupArn or ""
        self.Options = Options or {}
        self.Excludes = Excludes or []
        self.Schedule = Schedule or {}
        self.Tags = _convert_tags(Tags)
        self.Includes = Includes or []
        self.ManifestConfig = ManifestConfig or {}
        self.TaskReportConfig = TaskReportConfig or {}
        self.TaskMode = TaskMode or "BASIC"
        self.Status = "AVAILABLE"

    def to_dict(self):
        return {
            "TaskArn": self.TaskArn,
            "SourceLocationArn": self.SourceLocationArn,
            "DestinationLocationArn": self.DestinationLocationArn,
            "Name": self.Name,
            "CloudWatchLogGroupArn": self.CloudWatchLogGroupArn,
            "Options": self.Options,
            "Excludes": self.Excludes,
            "Schedule": self.Schedule,
            "Includes": self.Includes,
            "ManifestConfig": self.ManifestConfig,
            "TaskReportConfig": self.TaskReportConfig,
            "TaskMode": self.TaskMode,
            "Status": self.Status,
        }


class TaskExecutionRecord:
    def __init__(self, TaskArn=None, OverrideOptions=None, Includes=None,
                 Excludes=None, ManifestConfig=None, TaskReportConfig=None, Tags=None):
        self.TaskExecutionArn = f"arn:aws:datasync:us-east-1:000000000000:task/task-{uuid.uuid4().hex[:8]}/execution/exec-{uuid.uuid4().hex[:8]}"
        self.TaskArn = TaskArn or ""
        self.Status = "SUCCESS"
        self.OverrideOptions = OverrideOptions or {}
        self.Includes = Includes or []
        self.Excludes = Excludes or []
        self.ManifestConfig = ManifestConfig or {}
        self.TaskReportConfig = TaskReportConfig or {}
        self.Tags = _convert_tags(Tags)

    def to_dict(self):
        return {
            "TaskExecutionArn": self.TaskExecutionArn,
            "TaskArn": self.TaskArn,
            "Status": self.Status,
        }


# === Tag Helper ===
def _convert_tags(tags):
    """Convert AWS tag list to flat dict."""
    if not tags:
        return {}
    if isinstance(tags, dict):
        return tags
    if isinstance(tags, list):
        result = {}
        for t in tags:
            result[t.get("Key", t.get("key", ""))] = t.get("Value", t.get("value", ""))
        return result
    return {}


# === Store ===
class DataSyncStore:
    def __init__(self):
        self._agents = {}
        self._locations = {}
        self._tasks = {}
        self._executions = {}

    # ---- Agent ----
    def create_agent(self, ActivationKey, AgentName=None, Tags=None,
                     VpcEndpointId=None, SubnetArns=None, SecurityGroupArns=None):
        record = AgentRecord(
            ActivationKey=ActivationKey,
            AgentName=AgentName,
            VpcEndpointId=VpcEndpointId,
            SubnetArns=SubnetArns,
            SecurityGroupArns=SecurityGroupArns,
            Tags=Tags,
        )
        self._agents[record.AgentArn] = record
        return {"AgentArn": record.AgentArn}

    def describe_agent(self, AgentArn):
        rec = self._agents.get(AgentArn)
        if not rec:
            raise ResourceNotFoundException(f"Agent {AgentArn} not found")
        return rec.to_dict()

    def list_agents(self, MaxResults=None, NextToken=None):
        all_agents = list(self._agents.keys())
        return {"Agents": [{"AgentArn": a} for a in all_agents]}

    def delete_agent(self, AgentArn):
        if AgentArn not in self._agents:
            raise ResourceNotFoundException(f"Agent {AgentArn} not found")
        del self._agents[AgentArn]
        return {}

    def update_agent(self, AgentArn, Name=None):
        rec = self._agents.get(AgentArn)
        if not rec:
            raise ResourceNotFoundException(f"Agent {AgentArn} not found")
        if Name is not None:
            rec.AgentName = Name
        return {}

    # ---- Location ----
    def create_location_s3(self, S3BucketArn, S3Config, Subdirectory=None,
                           S3StorageClass=None, AgentArns=None, Tags=None):
        location_uri = f"s3://{S3BucketArn}"
        record = LocationRecord(
            LocationType="S3",
            LocationUri=location_uri,
            S3BucketArn=S3BucketArn,
            S3Config=S3Config,
            Subdirectory=Subdirectory,
            S3StorageClass=S3StorageClass,
            AgentArns=AgentArns,
            Tags=Tags,
        )
        self._locations[record.LocationArn] = record
        return {"LocationArn": record.LocationArn}

    def create_location_nfs(self, Subdirectory, ServerHostname, OnPremConfig,
                            MountOptions=None, Tags=None):
        location_uri = f"nfs://{ServerHostname}{Subdirectory}"
        record = LocationRecord(
            LocationType="NFS",
            LocationUri=location_uri,
            Subdirectory=Subdirectory,
            ServerHostname=ServerHostname,
            OnPremConfig=OnPremConfig,
            MountOptions=MountOptions,
            Tags=Tags,
        )
        self._locations[record.LocationArn] = record
        return {"LocationArn": record.LocationArn}

    def list_locations(self, MaxResults=None, NextToken=None, Filters=None):
        all_locs = list(self._locations.keys())
        return {"Locations": [{"LocationArn": a} for a in all_locs]}

    def delete_location(self, LocationArn):
        if LocationArn not in self._locations:
            raise ResourceNotFoundException(f"Location {LocationArn} not found")
        del self._locations[LocationArn]
        return {}

    def describe_location(self, LocationArn):
        rec = self._locations.get(LocationArn)
        if not rec:
            raise ResourceNotFoundException(f"Location {LocationArn} not found")
        return rec.to_dict()

    # ---- Task ----
    def create_task(self, SourceLocationArn, DestinationLocationArn, Name=None,
                    CloudWatchLogGroupArn=None, Options=None, Excludes=None,
                    Schedule=None, Tags=None, Includes=None, ManifestConfig=None,
                    TaskReportConfig=None, TaskMode=None):
        record = TaskRecord(
            SourceLocationArn=SourceLocationArn,
            DestinationLocationArn=DestinationLocationArn,
            Name=Name,
            CloudWatchLogGroupArn=CloudWatchLogGroupArn,
            Options=Options,
            Excludes=Excludes,
            Schedule=Schedule,
            Tags=Tags,
            Includes=Includes,
            ManifestConfig=ManifestConfig,
            TaskReportConfig=TaskReportConfig,
            TaskMode=TaskMode,
        )
        self._tasks[record.TaskArn] = record
        return {"TaskArn": record.TaskArn}

    def describe_task(self, TaskArn):
        rec = self._tasks.get(TaskArn)
        if not rec:
            raise ResourceNotFoundException(f"Task {TaskArn} not found")
        return rec.to_dict()

    def list_tasks(self, MaxResults=None, NextToken=None, Filters=None):
        all_tasks = list(self._tasks.keys())
        return {"Tasks": [{"TaskArn": t} for t in all_tasks]}

    def delete_task(self, TaskArn):
        if TaskArn not in self._tasks:
            raise ResourceNotFoundException(f"Task {TaskArn} not found")
        del self._tasks[TaskArn]
        return {}

    def update_task(self, TaskArn, Options=None, Excludes=None, Schedule=None,
                    Name=None, CloudWatchLogGroupArn=None, Includes=None,
                    ManifestConfig=None, TaskReportConfig=None):
        rec = self._tasks.get(TaskArn)
        if not rec:
            raise ResourceNotFoundException(f"Task {TaskArn} not found")
        if Options is not None:
            rec.Options = Options
        if Excludes is not None:
            rec.Excludes = Excludes
        if Schedule is not None:
            rec.Schedule = Schedule
        if Name is not None:
            rec.Name = Name
        if CloudWatchLogGroupArn is not None:
            rec.CloudWatchLogGroupArn = CloudWatchLogGroupArn
        if Includes is not None:
            rec.Includes = Includes
        if ManifestConfig is not None:
            rec.ManifestConfig = ManifestConfig
        if TaskReportConfig is not None:
            rec.TaskReportConfig = TaskReportConfig
        return {}

    # ---- TaskExecution ----
    def start_task_execution(self, TaskArn, OverrideOptions=None, Includes=None,
                             Excludes=None, ManifestConfig=None, TaskReportConfig=None,
                             Tags=None):
        rec = self._tasks.get(TaskArn)
        if not rec:
            raise ResourceNotFoundException(f"Task {TaskArn} not found")
        exec_rec = TaskExecutionRecord(
            TaskArn=TaskArn,
            OverrideOptions=OverrideOptions,
            Includes=Includes,
            Excludes=Excludes,
            ManifestConfig=ManifestConfig,
            TaskReportConfig=TaskReportConfig,
            Tags=Tags,
        )
        self._executions[exec_rec.TaskExecutionArn] = exec_rec
        return {"TaskExecutionArn": exec_rec.TaskExecutionArn}

    def describe_task_execution(self, TaskExecutionArn):
        rec = self._executions.get(TaskExecutionArn)
        if not rec:
            raise ResourceNotFoundException(f"TaskExecution {TaskExecutionArn} not found")
        return rec.to_dict()

    # ---- Tags ----
    def tag_resource(self, ResourceArn, Tags):
        tag_dict = _convert_tags(Tags)
        for collection in [self._agents, self._locations, self._tasks, self._executions]:
            if ResourceArn in collection:
                existing = getattr(collection[ResourceArn], "Tags", {})
                existing.update(tag_dict)
                return {}
        raise ResourceNotFoundException(f"Resource {ResourceArn} not found")

    def list_tags_for_resource(self, ResourceArn, MaxResults=None, NextToken=None):
        for collection_name in ["_agents", "_locations", "_tasks", "_executions"]:
            collection = getattr(self, collection_name)
            if ResourceArn in collection:
                tags = getattr(collection[ResourceArn], "Tags", {})
                tag_list = [{"Key": k, "Value": v} for k, v in tags.items()]
                return {"Tags": tag_list}
        raise ResourceNotFoundException(f"Resource {ResourceArn} not found")
