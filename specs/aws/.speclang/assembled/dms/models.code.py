"""DMS Store — ReplicationInstance, Endpoint, ReplicationTask entities."""
import time as _time


class ResourceNotFoundException(Exception):
    pass


class ResourceAlreadyExistsException(Exception):
    pass


class InvalidResourceStateException(Exception):
    pass


class ReplicationInstanceRecord:
    def __init__(self, ReplicationInstanceIdentifier=None,
                 ReplicationInstanceArn=None, ReplicationInstanceClass=None,
                 AllocatedStorage=None, EngineVersion=None,
                 ReplicationInstanceStatus="available",
                 InstanceCreateTime=None):
        self.ReplicationInstanceIdentifier = ReplicationInstanceIdentifier
        self.ReplicationInstanceArn = ReplicationInstanceArn or f"arn:aws:dms:us-east-1:000000000000:rep:{ReplicationInstanceIdentifier}"
        self.ReplicationInstanceClass = ReplicationInstanceClass or "dms.t3.micro"
        self.AllocatedStorage = AllocatedStorage or 50
        self.EngineVersion = EngineVersion or "3.4.7"
        self.ReplicationInstanceStatus = ReplicationInstanceStatus
        self.InstanceCreateTime = InstanceCreateTime or _time.time()

    def to_dict(self):
        return {
            "ReplicationInstanceIdentifier": self.ReplicationInstanceIdentifier,
            "ReplicationInstanceArn": self.ReplicationInstanceArn,
            "ReplicationInstanceClass": self.ReplicationInstanceClass,
            "ReplicationInstanceStatus": self.ReplicationInstanceStatus,
            "EngineVersion": self.EngineVersion,
            "AllocatedStorage": self.AllocatedStorage,
            "InstanceCreateTime": self.InstanceCreateTime,
        }


class EndpointRecord:
    def __init__(self, EndpointIdentifier=None, EndpointArn=None,
                 EndpointType=None, EngineName=None,
                 ServerName=None, Port=None, DatabaseName=None,
                 Username=None, Status="active"):
        self.EndpointIdentifier = EndpointIdentifier
        self.EndpointArn = EndpointArn or f"arn:aws:dms:us-east-1:000000000000:endpoint:{EndpointIdentifier}"
        self.EndpointType = EndpointType or "source"
        self.EngineName = EngineName or "mysql"
        self.ServerName = ServerName
        self.Port = Port
        self.DatabaseName = DatabaseName
        self.Username = Username
        self.Status = Status

    def to_dict(self):
        return {
            "EndpointIdentifier": self.EndpointIdentifier,
            "EndpointArn": self.EndpointArn,
            "EndpointType": self.EndpointType,
            "EngineName": self.EngineName,
            "ServerName": self.ServerName,
            "Port": self.Port,
            "DatabaseName": self.DatabaseName,
            "Status": self.Status,
        }


class ReplicationTaskRecord:
    def __init__(self, ReplicationTaskIdentifier=None,
                 ReplicationTaskArn=None,
                 SourceEndpointArn=None, TargetEndpointArn=None,
                 ReplicationInstanceArn=None,
                 MigrationType=None,
                 Status="ready",
                 ReplicationTaskCreationDate=None):
        self.ReplicationTaskIdentifier = ReplicationTaskIdentifier
        self.ReplicationTaskArn = ReplicationTaskArn or f"arn:aws:dms:us-east-1:000000000000:task:{ReplicationTaskIdentifier}"
        self.SourceEndpointArn = SourceEndpointArn
        self.TargetEndpointArn = TargetEndpointArn
        self.ReplicationInstanceArn = ReplicationInstanceArn
        self.MigrationType = MigrationType or "full-load"
        self.Status = Status
        self.ReplicationTaskCreationDate = ReplicationTaskCreationDate or _time.time()

    def to_dict(self):
        return {
            "ReplicationTaskIdentifier": self.ReplicationTaskIdentifier,
            "ReplicationTaskArn": self.ReplicationTaskArn,
            "SourceEndpointArn": self.SourceEndpointArn,
            "TargetEndpointArn": self.TargetEndpointArn,
            "ReplicationInstanceArn": self.ReplicationInstanceArn,
            "MigrationType": self.MigrationType,
            "Status": self.Status,
            "ReplicationTaskCreationDate": self.ReplicationTaskCreationDate,
        }


class DMSStore:
    def __init__(self):
        self._instances: dict[str, ReplicationInstanceRecord] = {}
        self._endpoints: dict[str, EndpointRecord] = {}
        self._tasks: dict[str, ReplicationTaskRecord] = {}

    # ── ReplicationInstance ──
    def create_replication_instance(self, **kwargs):
        name = kwargs["ReplicationInstanceIdentifier"]
        if name in self._instances:
            raise ResourceAlreadyExistsException(f"Instance {name} already exists")
        record = ReplicationInstanceRecord(**kwargs)
        self._instances[name] = record
        return record.to_dict()

    def describe_replication_instances(self, **kwargs):
        return [r.to_dict() for r in self._instances.values()]

    def delete_replication_instance(self, ReplicationInstanceIdentifier):
        if ReplicationInstanceIdentifier not in self._instances:
            raise ResourceNotFoundException(f"Instance {ReplicationInstanceIdentifier} not found")
        del self._instances[ReplicationInstanceIdentifier]

    # ── Endpoint ──
    def create_endpoint(self, **kwargs):
        name = kwargs["EndpointIdentifier"]
        if name in self._endpoints:
            raise ResourceAlreadyExistsException(f"Endpoint {name} already exists")
        record = EndpointRecord(**kwargs)
        self._endpoints[name] = record
        return record.to_dict()

    def describe_endpoints(self, **kwargs):
        return [r.to_dict() for r in self._endpoints.values()]

    def delete_endpoint(self, EndpointIdentifier):
        if EndpointIdentifier not in self._endpoints:
            raise ResourceNotFoundException(f"Endpoint {EndpointIdentifier} not found")
        del self._endpoints[EndpointIdentifier]

    # ── ReplicationTask ──
    def create_replication_task(self, **kwargs):
        name = kwargs["ReplicationTaskIdentifier"]
        if name in self._tasks:
            raise ResourceAlreadyExistsException(f"Task {name} already exists")
        record = ReplicationTaskRecord(**kwargs)
        self._tasks[name] = record
        return record.to_dict()

    def describe_replication_tasks(self, **kwargs):
        return [r.to_dict() for r in self._tasks.values()]

    def delete_replication_task(self, ReplicationTaskIdentifier):
        if ReplicationTaskIdentifier not in self._tasks:
            raise ResourceNotFoundException(f"Task {ReplicationTaskIdentifier} not found")
        del self._tasks[ReplicationTaskIdentifier]

    def start_replication_task(self, ReplicationTaskIdentifier):
        record = self._tasks.get(ReplicationTaskIdentifier)
        if not record:
            raise ResourceNotFoundException(f"Task {ReplicationTaskIdentifier} not found")
        record.Status = "running"

    def stop_replication_task(self, ReplicationTaskIdentifier):
        record = self._tasks.get(ReplicationTaskIdentifier)
        if not record:
            raise ResourceNotFoundException(f"Task {ReplicationTaskIdentifier} not found")
        record.Status = "stopped"
