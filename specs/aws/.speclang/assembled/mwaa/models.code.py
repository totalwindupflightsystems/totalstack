"""MWAA (Managed Workflows for Apache Airflow) — TotalStack store.

Entity: Environment (one per account). Named key (Name).
"""

import time as _time
import uuid as _uuid


# ==================== Exception Classes ====================

class ResourceNotFoundException(Exception):
    """Environment not found."""
    def __init__(self, message="Environment not found"):
        self.message = message
        super().__init__(message)


class ValidationException(Exception):
    """Invalid request (missing fields, bad values)."""
    def __init__(self, message="Validation error"):
        self.message = message
        super().__init__(message)


class InternalServerException(Exception):
    """Internal error."""
    def __init__(self, message="Internal server error"):
        self.message = message
        super().__init__(message)


class AccessDeniedException(Exception):
    """Access denied."""
    def __init__(self, message="Access denied"):
        self.message = message
        super().__init__(message)


class RestApiClientException(Exception):
    """Airflow REST API client error."""
    def __init__(self, message="Rest API client error",
                 RestApiStatusCode=None, RestApiResponse=None):
        self.message = message
        self.RestApiStatusCode = RestApiStatusCode
        self.RestApiResponse = RestApiResponse
        super().__init__(message)


class RestApiServerException(Exception):
    """Airflow REST API server error."""
    def __init__(self, message="Rest API server error",
                 RestApiStatusCode=None, RestApiResponse=None):
        self.message = message
        self.RestApiStatusCode = RestApiStatusCode
        self.RestApiResponse = RestApiResponse
        super().__init__(message)


# ==================== Record Classes ====================

class NetworkConfiguration:
    def __init__(self, SecurityGroupIds=None, SubnetIds=None):
        self.SecurityGroupIds = SecurityGroupIds or []
        self.SubnetIds = SubnetIds or []

    def to_dict(self):
        return {
            "SecurityGroupIds": list(self.SecurityGroupIds),
            "SubnetIds": list(self.SubnetIds),
        }


class ModuleLoggingConfiguration:
    def __init__(self, CloudWatchLogGroupArn=None,
                 Enabled=None, LogLevel=None):
        self.CloudWatchLogGroupArn = CloudWatchLogGroupArn
        self.Enabled = Enabled
        self.LogLevel = LogLevel

    def to_dict(self):
        return {
            "CloudWatchLogGroupArn": self.CloudWatchLogGroupArn,
            "Enabled": self.Enabled,
            "LogLevel": self.LogLevel,
        }


class LoggingConfiguration:
    def __init__(self, DagProcessingLogs=None,
                 SchedulerLogs=None, TaskLogs=None, WebserverLogs=None,
                 WorkerLogs=None):
        self.DagProcessingLogs = (
            ModuleLoggingConfiguration(**DagProcessingLogs)
            if isinstance(DagProcessingLogs, dict) else DagProcessingLogs
        )
        self.SchedulerLogs = (
            ModuleLoggingConfiguration(**SchedulerLogs)
            if isinstance(SchedulerLogs, dict) else SchedulerLogs
        )
        self.TaskLogs = (
            ModuleLoggingConfiguration(**TaskLogs)
            if isinstance(TaskLogs, dict) else TaskLogs
        )
        self.WebserverLogs = (
            ModuleLoggingConfiguration(**WebserverLogs)
            if isinstance(WebserverLogs, dict) else WebserverLogs
        )
        self.WorkerLogs = (
            ModuleLoggingConfiguration(**WorkerLogs)
            if isinstance(WorkerLogs, dict) else WorkerLogs
        )

    def to_dict(self):
        return {
            "DagProcessingLogs": (self.DagProcessingLogs.to_dict()
                                  if self.DagProcessingLogs else None),
            "SchedulerLogs": (self.SchedulerLogs.to_dict()
                              if self.SchedulerLogs else None),
            "TaskLogs": (self.TaskLogs.to_dict()
                         if self.TaskLogs else None),
            "WebserverLogs": (self.WebserverLogs.to_dict()
                              if self.WebserverLogs else None),
            "WorkerLogs": (self.WorkerLogs.to_dict()
                           if self.WorkerLogs else None),
        }


class EnvironmentRecord:
    def __init__(self, Name,
                 ExecutionRoleArn=None,
                 SourceBucketArn=None,
                 DagS3Path=None,
                 NetworkConfiguration=None,
                 PluginsS3Path=None,
                 PluginsS3ObjectVersion=None,
                 RequirementsS3Path=None,
                 RequirementsS3ObjectVersion=None,
                 StartupScriptS3Path=None,
                 StartupScriptS3ObjectVersion=None,
                 AirflowConfigurationOptions=None,
                 EnvironmentClass=None,
                 MaxWorkers=None,
                 KmsKey=None,
                 AirflowVersion=None,
                 LoggingConfiguration=None,
                 WeeklyMaintenanceWindowStart=None,
                 Tags=None,
                 WebserverAccessMode=None,
                 MinWorkers=None,
                 Schedulers=None,
                 EndpointManagement=None,
                 MinWebservers=None,
                 MaxWebservers=None,
                 Arn=None,
                 Status="CREATING",
                 CreatedAt=None,
                 ServiceRoleArn=None,
                 WebserverUrl=None,
                 LastUpdate=None):
        self.Name = Name
        self.ExecutionRoleArn = ExecutionRoleArn
        self.SourceBucketArn = SourceBucketArn
        self.DagS3Path = DagS3Path
        if isinstance(NetworkConfiguration, dict):
            self.NetworkConfiguration = _NetworkConfiguration(**NetworkConfiguration)
        elif NetworkConfiguration is not None:
            self.NetworkConfiguration = NetworkConfiguration
        else:
            self.NetworkConfiguration = _NetworkConfiguration()
        self.PluginsS3Path = PluginsS3Path
        self.PluginsS3ObjectVersion = PluginsS3ObjectVersion
        self.RequirementsS3Path = RequirementsS3Path
        self.RequirementsS3ObjectVersion = RequirementsS3ObjectVersion
        self.StartupScriptS3Path = StartupScriptS3Path
        self.StartupScriptS3ObjectVersion = StartupScriptS3ObjectVersion
        self.AirflowConfigurationOptions = AirflowConfigurationOptions or {}
        self.EnvironmentClass = EnvironmentClass or "mw1.small"
        self.MaxWorkers = MaxWorkers or 10
        self.KmsKey = KmsKey
        self.AirflowVersion = AirflowVersion or "2.10.1"
        if isinstance(LoggingConfiguration, dict):
            self.LoggingConfiguration = _LoggingConfiguration(**LoggingConfiguration)
        elif LoggingConfiguration is not None:
            self.LoggingConfiguration = LoggingConfiguration
        else:
            self.LoggingConfiguration = _LoggingConfiguration()
        self.WeeklyMaintenanceWindowStart = WeeklyMaintenanceWindowStart
        self.Tags = Tags or {}
        self.WebserverAccessMode = WebserverAccessMode or "PUBLIC_ONLY"
        self.MinWorkers = MinWorkers or 1
        self.Schedulers = Schedulers or 2
        self.EndpointManagement = EndpointManagement or "CUSTOMER"
        self.MinWebservers = MinWebservers or 1
        self.MaxWebservers = MaxWebservers or 2
        self.Arn = Arn
        self.Status = Status
        self.CreatedAt = CreatedAt or _time.time()
        self.ServiceRoleArn = ServiceRoleArn
        self.WebserverUrl = WebserverUrl
        self.LastUpdate = LastUpdate

    def to_dict(self):
        return {
            "Name": self.Name,
            "ExecutionRoleArn": self.ExecutionRoleArn,
            "SourceBucketArn": self.SourceBucketArn,
            "DagS3Path": self.DagS3Path,
            "NetworkConfiguration": (self.NetworkConfiguration.to_dict()
                                     if self.NetworkConfiguration else None),
            "PluginsS3Path": self.PluginsS3Path,
            "PluginsS3ObjectVersion": self.PluginsS3ObjectVersion,
            "RequirementsS3Path": self.RequirementsS3Path,
            "RequirementsS3ObjectVersion": self.RequirementsS3ObjectVersion,
            "StartupScriptS3Path": self.StartupScriptS3Path,
            "StartupScriptS3ObjectVersion": self.StartupScriptS3ObjectVersion,
            "AirflowConfigurationOptions": self.AirflowConfigurationOptions,
            "EnvironmentClass": self.EnvironmentClass,
            "MaxWorkers": self.MaxWorkers,
            "KmsKey": self.KmsKey,
            "AirflowVersion": self.AirflowVersion,
            "LoggingConfiguration": (self.LoggingConfiguration.to_dict()
                                     if self.LoggingConfiguration else None),
            "WeeklyMaintenanceWindowStart": self.WeeklyMaintenanceWindowStart,
            "Tags": self.Tags,
            "WebserverAccessMode": self.WebserverAccessMode,
            "MinWorkers": self.MinWorkers,
            "Schedulers": self.Schedulers,
            "EndpointManagement": self.EndpointManagement,
            "MinWebservers": self.MinWebservers,
            "MaxWebservers": self.MaxWebservers,
            "Arn": self.Arn,
            "Status": self.Status,
            "CreatedAt": self.CreatedAt,
            "ServiceRoleArn": self.ServiceRoleArn,
            "WebserverUrl": self.WebserverUrl,
            "LastUpdate": self.LastUpdate,
        }


# Module-level aliases to avoid parameter shadowing in __init__
_NetworkConfiguration = NetworkConfiguration
_LoggingConfiguration = LoggingConfiguration


# ==================== MWAA Store ====================

class MWAAStore:
    """In-memory store for MWAA environments."""

    def __init__(self):
        self._environments: dict[str, EnvironmentRecord] = {}
        self._tags: dict[str, dict] = {}  # arn → {key: value}
        self._arn_counter = 0

    # ---- Method accessor (not bare dict — handlers call store.environments(name)) ----
    def environments(self, name=None):
        if name is not None:
            return self._environments.get(name)
        return list(self._environments.values())

    def _generate_arn(self, name):
        self._arn_counter += 1
        return f"arn:aws:airflow:us-east-1:000000000000:environment/{name}"

    # ---- Tag helpers ----
    def _convert_tags(self, tags):
        """Convert AWS tag list [{key:..., value:...}] to flat dict."""
        if tags is None:
            return {}
        if isinstance(tags, dict):
            return dict(tags)
        tag_dict = {}
        for t in tags:
            tag_dict[t.get("key", t.get("Key", ""))] = t.get(
                "value", t.get("Value", ""))
        return tag_dict

    # ---- Environment CRUD ----

    def create_environment(self, **kwargs):
        name = kwargs.get("Name")
        if name in self._environments:
            raise ValidationException(
                f"Environment {name} already exists")
        tags_raw = kwargs.pop("Tags", None)
        record = EnvironmentRecord(**kwargs)
        record.Arn = self._generate_arn(name)
        self._environments[name] = record
        if tags_raw:
            self._tags[record.Arn] = self._convert_tags(tags_raw)
        return {"Arn": record.Arn}

    def get_environment(self, Name):
        record = self._environments.get(Name)
        if not record:
            raise ResourceNotFoundException(
                f"Environment {Name} not found")
        env_dict = record.to_dict()
        env_dict["Tags"] = self._tags.get(record.Arn, {})
        return {"Environment": env_dict}

    def list_environments(self, MaxResults=None, NextToken=None):
        all_envs = list(self._environments.keys())
        if MaxResults and int(MaxResults) < len(all_envs):
            return {
                "Environments": all_envs[:int(MaxResults)],
                "NextToken": str(int(MaxResults))
            }
        return {"Environments": all_envs}

    def update_environment(self, **kwargs):
        name = kwargs.get("Name")
        record = self._environments.get(name)
        if not record:
            raise ResourceNotFoundException(
                f"Environment {name} not found")
        for key, value in kwargs.items():
            if key == "Name":
                continue
            if key == "NetworkConfiguration" and isinstance(value, dict):
                value = NetworkConfiguration(**value)
            if key == "LoggingConfiguration" and isinstance(value, dict):
                value = LoggingConfiguration(**value)
            if hasattr(record, key):
                setattr(record, key, value)
        record.LastUpdate = {"Status": "SUCCESS", "CreatedAt": _time.time()}
        return {"Arn": record.Arn}

    def delete_environment(self, Name):
        record = self._environments.get(Name)
        if not record:
            raise ResourceNotFoundException(
                f"Environment {Name} not found")
        arn = record.Arn
        del self._environments[Name]
        self._tags.pop(arn, None)
        return {}

    # ---- CLI Token ----

    def create_cli_token(self, Name):
        record = self._environments.get(Name)
        if not record:
            raise ResourceNotFoundException(
                f"Environment {Name} not found")
        return {
            "CliToken": str(_uuid.uuid4()),
            "WebServerHostname": f"{Name}.airflow.localhost",
        }

    # ---- Web Login Token ----

    def create_web_login_token(self, Name):
        record = self._environments.get(Name)
        if not record:
            raise ResourceNotFoundException(
                f"Environment {Name} not found")
        return {
            "WebToken": str(_uuid.uuid4()),
            "WebServerHostname": f"{Name}.airflow.localhost",
            "IamIdentity": "arn:aws:iam::000000000000:user/test",
            "AirflowIdentity": "admin",
        }

    # ---- Invoke Rest API (passthrough) ----

    def invoke_rest_api(self, **kwargs):
        name = kwargs.get("Name")
        record = self._environments.get(name)
        if not record:
            raise ResourceNotFoundException(
                f"Environment {name} not found")
        path = kwargs.get("Path", "/")
        if not path.startswith("/"):
            raise ValidationException("Path must start with /")
        return {
            "RestApiStatusCode": 200,
            "RestApiResponse": {"message": "ok", "path": path},
        }

    # ---- Tag operations ----

    def list_tags_for_resource(self, ResourceArn):
        if ResourceArn not in [
            r.Arn for r in self._environments.values()
        ]:
            raise ResourceNotFoundException(
                f"Resource {ResourceArn} not found")
        return {"Tags": self._tags.get(ResourceArn, {})}

    def tag_resource(self, ResourceArn, Tags):
        if ResourceArn not in [
            r.Arn for r in self._environments.values()
        ]:
            raise ResourceNotFoundException(
                f"Resource {ResourceArn} not found")
        existing = self._tags.get(ResourceArn, {})
        existing.update(self._convert_tags(Tags))
        self._tags[ResourceArn] = existing
        return {}

    def untag_resource(self, ResourceArn, tagKeys):
        if ResourceArn not in [
            r.Arn for r in self._environments.values()
        ]:
            raise ResourceNotFoundException(
                f"Resource {ResourceArn} not found")
        existing = self._tags.get(ResourceArn, {})
        for key in tagKeys:
            existing.pop(key, None)
        self._tags[ResourceArn] = existing
        return {}

    # ---- Publish metrics ----

    def publish_metrics(self, EnvironmentName, MetricData):
        record = self._environments.get(EnvironmentName)
        if not record:
            raise ResourceNotFoundException(
                f"Environment {EnvironmentName} not found")
        return {}
