"""GlobalAccelerator store — real in-memory implementation."""
import uuid
import time as _time


# ── Exception Classes ──────────────────────────────────────────────

class AcceleratorNotFoundException(Exception):
    pass

class AcceleratorNotDisabledException(Exception):
    pass

class AccessDeniedException(Exception):
    pass

class AssociatedEndpointGroupFoundException(Exception):
    pass

class AssociatedListenerFoundException(Exception):
    pass

class AttachmentNotFoundException(Exception):
    pass

class ConflictException(Exception):
    pass

class EndpointGroupAlreadyExistsException(Exception):
    pass

class EndpointGroupNotFoundException(Exception):
    pass

class EndpointNotFoundException(Exception):
    pass

class InternalServiceErrorException(Exception):
    pass

class InvalidArgumentException(Exception):
    pass

class InvalidNextTokenException(Exception):
    pass

class InvalidPortRangeException(Exception):
    pass

class LimitExceededException(Exception):
    pass

class ListenerNotFoundException(Exception):
    pass

class TransactionInProgressException(Exception):
    pass


# ── Record Classes ─────────────────────────────────────────────────

class AcceleratorRecord:
    def __init__(self, Name, IdempotencyToken=None, Enabled=True,
                 IpAddressType="IPV4", IpAddresses=None, Tags=None):
        self.Name = Name
        self.Enabled = Enabled
        self.IpAddressType = IpAddressType or "IPV4"
        self.IpAddresses = IpAddresses or ["127.0.0.1", "127.0.0.2"]
        self.Tags = Tags or []
        self.AcceleratorArn = f"arn:aws:globalaccelerator::000000000000:accelerator/{uuid.uuid4().hex[:8]}"
        self.Status = "DEPLOYED"
        self.CreatedTime = _time.time()
        self.DnsName = f"{uuid.uuid4().hex[:8]}.awsglobalaccelerator.com"
        self.DualStackDnsName = f"{uuid.uuid4().hex[:8]}.dualstack.awsglobalaccelerator.com"
        self.IpSets = [
            {"IpFamily": "IPv4", "IpAddresses": self.IpAddresses, "IpAddressFamily": "IPv4"}
        ]
        self.FlowLogsEnabled = False
        self.FlowLogsS3Bucket = None
        self.FlowLogsS3Prefix = None

    def to_dict(self):
        return {
            "AcceleratorArn": self.AcceleratorArn,
            "Name": self.Name,
            "IpAddressType": self.IpAddressType,
            "Enabled": self.Enabled,
            "IpSets": self.IpSets,
            "DnsName": self.DnsName,
            "DualStackDnsName": self.DualStackDnsName,
            "Status": self.Status,
            "CreatedTime": self.CreatedTime,
            "LastModifiedTime": self.CreatedTime,
        }


class PortRange:
    def __init__(self, FromPort=80, ToPort=80):
        self.FromPort = FromPort
        self.ToPort = ToPort

    def to_dict(self):
        return {"FromPort": self.FromPort, "ToPort": self.ToPort}


class ListenerRecord:
    def __init__(self, AcceleratorArn, PortRanges, Protocol, IdempotencyToken=None,
                 ClientAffinity="NONE"):
        self.AcceleratorArn = AcceleratorArn
        if isinstance(PortRanges, list) and PortRanges and isinstance(PortRanges[0], dict):
            self.PortRanges = [PortRange(**p) for p in PortRanges]
        elif isinstance(PortRanges, list) and PortRanges and isinstance(PortRanges[0], PortRange):
            self.PortRanges = PortRanges
        else:
            self.PortRanges = [PortRange()]
        self.Protocol = Protocol or "TCP"
        self.ClientAffinity = ClientAffinity or "NONE"
        self.ListenerArn = f"arn:aws:globalaccelerator::000000000000:accelerator/{uuid.uuid4().hex[:8]}/listener/{uuid.uuid4().hex[:8]}"

    def to_dict(self):
        return {
            "ListenerArn": self.ListenerArn,
            "PortRanges": [p.to_dict() if hasattr(p, 'to_dict') else p for p in self.PortRanges],
            "Protocol": self.Protocol,
            "ClientAffinity": self.ClientAffinity,
        }


class EndpointConfiguration:
    def __init__(self, EndpointId=None, Weight=128, ClientIPPreservationEnabled=True):
        self.EndpointId = EndpointId
        self.Weight = Weight or 128
        self.ClientIPPreservationEnabled = ClientIPPreservationEnabled

    def to_dict(self):
        return {
            "EndpointId": self.EndpointId,
            "Weight": self.Weight,
            "ClientIPPreservationEnabled": self.ClientIPPreservationEnabled,
        }


class PortOverride:
    def __init__(self, ListenerPort=80, EndpointPort=80):
        self.ListenerPort = ListenerPort
        self.EndpointPort = EndpointPort

    def to_dict(self):
        return {"ListenerPort": self.ListenerPort, "EndpointPort": self.EndpointPort}


class EndpointGroupRecord:
    def __init__(self, EndpointGroupRegion, ListenerArn,
                 EndpointConfigurations=None, HealthCheckIntervalSeconds=30,
                 HealthCheckPath="/", HealthCheckPort=80, HealthCheckProtocol="TCP",
                 IdempotencyToken=None, PortOverrides=None, ThresholdCount=3,
                 TrafficDialPercentage=100):
        self.EndpointGroupRegion = EndpointGroupRegion
        self.ListenerArn = ListenerArn
        if isinstance(EndpointConfigurations, list):
            self.EndpointConfigurations = [
                EndpointConfiguration(**e) if isinstance(e, dict) else e
                for e in EndpointConfigurations
            ]
        else:
            self.EndpointConfigurations = []
        self.HealthCheckIntervalSeconds = HealthCheckIntervalSeconds or 30
        self.HealthCheckPath = HealthCheckPath or "/"
        self.HealthCheckPort = HealthCheckPort or 80
        self.HealthCheckProtocol = HealthCheckProtocol or "TCP"
        if isinstance(PortOverrides, list):
            self.PortOverrides = [
                PortOverride(**p) if isinstance(p, dict) else p
                for p in PortOverrides
            ]
        else:
            self.PortOverrides = []
        self.ThresholdCount = ThresholdCount or 3
        self.TrafficDialPercentage = TrafficDialPercentage or 100
        self.EndpointGroupArn = f"arn:aws:globalaccelerator::000000000000:accelerator/{uuid.uuid4().hex[:8]}/listener/{uuid.uuid4().hex[:8]}/endpoint-group/{uuid.uuid4().hex[:8]}"

    def to_dict(self):
        return {
            "EndpointGroupArn": self.EndpointGroupArn,
            "EndpointGroupRegion": self.EndpointGroupRegion,
            "EndpointDescriptions": [e.to_dict() if hasattr(e, 'to_dict') else e for e in self.EndpointConfigurations],
            "HealthCheckIntervalSeconds": self.HealthCheckIntervalSeconds,
            "HealthCheckPath": self.HealthCheckPath,
            "HealthCheckPort": self.HealthCheckPort,
            "HealthCheckProtocol": self.HealthCheckProtocol,
            "PortOverrides": [p.to_dict() if hasattr(p, 'to_dict') else p for p in self.PortOverrides],
            "ThresholdCount": self.ThresholdCount,
            "TrafficDialPercentage": self.TrafficDialPercentage,
        }

    def add_endpoints(self, endpoint_configs):
        for ec in endpoint_configs:
            self.EndpointConfigurations.append(
                EndpointConfiguration(**ec) if isinstance(ec, dict) else ec
            )

    def remove_endpoints(self, endpoint_ids):
        self.EndpointConfigurations = [
            e for e in self.EndpointConfigurations
            if (e.EndpointId if hasattr(e, 'EndpointId') else e.get('EndpointId', '')) not in endpoint_ids
        ]


# ── Store Class ────────────────────────────────────────────────────

class GlobalAcceleratorStore:
    def __init__(self):
        self._accelerators: dict[str, AcceleratorRecord] = {}
        self._listeners: dict[str, ListenerRecord] = {}
        self._endpoint_groups: dict[str, EndpointGroupRecord] = {}
        self._tags: dict[str, dict] = {}

    # ── Method accessors (NOT bare dicts — generated handlers call as methods) ─

    def accelerators(self, arn: str = None):
        """Method-style accessor: get by ARN or list all."""
        if arn is not None:
            return self._accelerators.get(arn)
        return list(self._accelerators.values())

    def listeners(self, arn: str = None):
        if arn is not None:
            return self._listeners.get(arn)
        return list(self._listeners.values())

    def endpoint_groups(self, arn: str = None):
        if arn is not None:
            return self._endpoint_groups.get(arn)
        return list(self._endpoint_groups.values())

    # ── Accelerator CRUD ───────────────────────────────────────────

    def create_accelerator(self, Name, IdempotencyToken=None, Enabled=True,
                           IpAddressType="IPV4", IpAddresses=None, Tags=None):
        # Check for duplicate name
        for a in self._accelerators.values():
            if a.Name == Name:
                raise InvalidArgumentException(f"Accelerator with name '{Name}' already exists")
        record = AcceleratorRecord(
            Name=Name, IdempotencyToken=IdempotencyToken, Enabled=Enabled,
            IpAddressType=IpAddressType, IpAddresses=IpAddresses, Tags=Tags)
        self._accelerators[record.AcceleratorArn] = record
        if Tags:
            tag_dict = {}
            for t in Tags:
                tag_dict[t.get("Key", t.get("key", ""))] = t.get("Value", t.get("value", ""))
            self._tags[record.AcceleratorArn] = tag_dict
        return {"Accelerator": record.to_dict()}

    def describe_accelerator(self, AcceleratorArn):
        record = self._accelerators.get(AcceleratorArn)
        if not record:
            raise AcceleratorNotFoundException(f"Accelerator {AcceleratorArn} not found")
        return {"Accelerator": record.to_dict()}

    def update_accelerator(self, AcceleratorArn, Name=None, Enabled=None,
                           IpAddressType=None, IpAddresses=None):
        record = self._accelerators.get(AcceleratorArn)
        if not record:
            raise AcceleratorNotFoundException(f"Accelerator {AcceleratorArn} not found")
        if Name is not None:
            record.Name = Name
        if Enabled is not None:
            record.Enabled = Enabled
        if IpAddressType is not None:
            record.IpAddressType = IpAddressType
        if IpAddresses is not None:
            record.IpAddresses = IpAddresses
            record.IpSets = [{"IpFamily": "IPv4", "IpAddresses": IpAddresses, "IpAddressFamily": "IPv4"}]
        record.LastModifiedTime = _time.time()
        return {"Accelerator": record.to_dict()}

    def delete_accelerator(self, AcceleratorArn):
        record = self._accelerators.get(AcceleratorArn)
        if not record:
            raise AcceleratorNotFoundException(f"Accelerator {AcceleratorArn} not found")
        if record.Enabled:
            raise AcceleratorNotDisabledException(f"Accelerator {AcceleratorArn} must be disabled first")
        # Check for associated listeners
        for listener in self._listeners.values():
            if listener.AcceleratorArn == AcceleratorArn:
                raise AssociatedListenerFoundException(
                    f"Accelerator {AcceleratorArn} has associated listeners")
        del self._accelerators[AcceleratorArn]
        self._tags.pop(AcceleratorArn, None)
        return {}

    def list_accelerators(self, MaxResults=None, NextToken=None):
        all_acc = list(self._accelerators.values())
        token = None
        if MaxResults and len(all_acc) > MaxResults:
            token = all_acc[MaxResults].AcceleratorArn
            all_acc = all_acc[:MaxResults]
        return {"Accelerators": [a.to_dict() for a in all_acc],
                "NextToken": token}

    def describe_accelerator_attributes(self, AcceleratorArn):
        record = self._accelerators.get(AcceleratorArn)
        if not record:
            raise AcceleratorNotFoundException(f"Accelerator {AcceleratorArn} not found")
        return {
            "FlowLogsEnabled": record.FlowLogsEnabled,
            "FlowLogsS3Bucket": record.FlowLogsS3Bucket,
            "FlowLogsS3Prefix": record.FlowLogsS3Prefix,
        }

    def update_accelerator_attributes(self, AcceleratorArn,
                                      FlowLogsEnabled=None, FlowLogsS3Bucket=None,
                                      FlowLogsS3Prefix=None):
        record = self._accelerators.get(AcceleratorArn)
        if not record:
            raise AcceleratorNotFoundException(f"Accelerator {AcceleratorArn} not found")
        if FlowLogsEnabled is not None:
            record.FlowLogsEnabled = FlowLogsEnabled
        if FlowLogsS3Bucket is not None:
            record.FlowLogsS3Bucket = FlowLogsS3Bucket
        if FlowLogsS3Prefix is not None:
            record.FlowLogsS3Prefix = FlowLogsS3Prefix
        return {
            "FlowLogsEnabled": record.FlowLogsEnabled,
            "FlowLogsS3Bucket": record.FlowLogsS3Bucket,
            "FlowLogsS3Prefix": record.FlowLogsS3Prefix,
        }

    # ── Listener CRUD ──────────────────────────────────────────────

    def create_listener(self, AcceleratorArn, PortRanges, Protocol,
                        IdempotencyToken=None, ClientAffinity="NONE"):
        if AcceleratorArn not in self._accelerators:
            raise AcceleratorNotFoundException(f"Accelerator {AcceleratorArn} not found")
        record = ListenerRecord(
            AcceleratorArn=AcceleratorArn, PortRanges=PortRanges,
            Protocol=Protocol, IdempotencyToken=IdempotencyToken,
            ClientAffinity=ClientAffinity)
        self._listeners[record.ListenerArn] = record
        return {"Listener": record.to_dict()}

    def describe_listener(self, ListenerArn):
        record = self._listeners.get(ListenerArn)
        if not record:
            raise ListenerNotFoundException(f"Listener {ListenerArn} not found")
        return {"Listener": record.to_dict()}

    def update_listener(self, ListenerArn, PortRanges=None, Protocol=None,
                        ClientAffinity=None):
        record = self._listeners.get(ListenerArn)
        if not record:
            raise ListenerNotFoundException(f"Listener {ListenerArn} not found")
        if PortRanges is not None:
            if isinstance(PortRanges, list) and PortRanges and isinstance(PortRanges[0], dict):
                record.PortRanges = [PortRange(**p) for p in PortRanges]
            else:
                record.PortRanges = PortRanges
        if Protocol is not None:
            record.Protocol = Protocol
        if ClientAffinity is not None:
            record.ClientAffinity = ClientAffinity
        return {"Listener": record.to_dict()}

    def delete_listener(self, ListenerArn):
        record = self._listeners.get(ListenerArn)
        if not record:
            raise ListenerNotFoundException(f"Listener {ListenerArn} not found")
        # Check for associated endpoint groups
        for eg in self._endpoint_groups.values():
            if eg.ListenerArn == ListenerArn:
                raise AssociatedEndpointGroupFoundException(
                    f"Listener {ListenerArn} has associated endpoint groups")
        del self._listeners[ListenerArn]
        return {}

    def list_listeners(self, AcceleratorArn, MaxResults=None, NextToken=None):
        if AcceleratorArn not in self._accelerators:
            raise AcceleratorNotFoundException(f"Accelerator {AcceleratorArn} not found")
        listeners = [listener for listener in self._listeners.values() if listener.AcceleratorArn == AcceleratorArn]
        token = None
        if MaxResults and len(listeners) > MaxResults:
            token = listeners[MaxResults].ListenerArn
            listeners = listeners[:MaxResults]
        return {"Listeners": [listener.to_dict() for listener in listeners],
                "NextToken": token}

    # ── EndpointGroup CRUD ─────────────────────────────────────────

    def create_endpoint_group(self, EndpointGroupRegion, ListenerArn,
                              EndpointConfigurations=None,
                              HealthCheckIntervalSeconds=30,
                              HealthCheckPath="/", HealthCheckPort=80,
                              HealthCheckProtocol="TCP", IdempotencyToken=None,
                              PortOverrides=None, ThresholdCount=3,
                              TrafficDialPercentage=100):
        if ListenerArn not in self._listeners:
            raise ListenerNotFoundException(f"Listener {ListenerArn} not found")
        # Check duplicate
        for eg in self._endpoint_groups.values():
            if eg.ListenerArn == ListenerArn and eg.EndpointGroupRegion == EndpointGroupRegion:
                raise EndpointGroupAlreadyExistsException(
                    f"Endpoint group in {EndpointGroupRegion} already exists for this listener")
        record = EndpointGroupRecord(
            EndpointGroupRegion=EndpointGroupRegion, ListenerArn=ListenerArn,
            EndpointConfigurations=EndpointConfigurations,
            HealthCheckIntervalSeconds=HealthCheckIntervalSeconds,
            HealthCheckPath=HealthCheckPath, HealthCheckPort=HealthCheckPort,
            HealthCheckProtocol=HealthCheckProtocol,
            IdempotencyToken=IdempotencyToken, PortOverrides=PortOverrides,
            ThresholdCount=ThresholdCount, TrafficDialPercentage=TrafficDialPercentage)
        self._endpoint_groups[record.EndpointGroupArn] = record
        return {"EndpointGroup": record.to_dict()}

    def describe_endpoint_group(self, EndpointGroupArn):
        record = self._endpoint_groups.get(EndpointGroupArn)
        if not record:
            raise EndpointGroupNotFoundException(f"Endpoint group {EndpointGroupArn} not found")
        return {"EndpointGroup": record.to_dict()}

    def update_endpoint_group(self, EndpointGroupArn,
                              EndpointConfigurations=None,
                              HealthCheckIntervalSeconds=None,
                              HealthCheckPath=None, HealthCheckPort=None,
                              HealthCheckProtocol=None, PortOverrides=None,
                              ThresholdCount=None, TrafficDialPercentage=None):
        record = self._endpoint_groups.get(EndpointGroupArn)
        if not record:
            raise EndpointGroupNotFoundException(f"Endpoint group {EndpointGroupArn} not found")
        if EndpointConfigurations is not None:
            record.EndpointConfigurations = [
                EndpointConfiguration(**e) if isinstance(e, dict) else e
                for e in EndpointConfigurations
            ]
        if HealthCheckIntervalSeconds is not None:
            record.HealthCheckIntervalSeconds = HealthCheckIntervalSeconds
        if HealthCheckPath is not None:
            record.HealthCheckPath = HealthCheckPath
        if HealthCheckPort is not None:
            record.HealthCheckPort = HealthCheckPort
        if HealthCheckProtocol is not None:
            record.HealthCheckProtocol = HealthCheckProtocol
        if PortOverrides is not None:
            record.PortOverrides = [
                PortOverride(**p) if isinstance(p, dict) else p
                for p in PortOverrides
            ]
        if ThresholdCount is not None:
            record.ThresholdCount = ThresholdCount
        if TrafficDialPercentage is not None:
            record.TrafficDialPercentage = TrafficDialPercentage
        return {"EndpointGroup": record.to_dict()}

    def delete_endpoint_group(self, EndpointGroupArn):
        record = self._endpoint_groups.get(EndpointGroupArn)
        if not record:
            raise EndpointGroupNotFoundException(f"Endpoint group {EndpointGroupArn} not found")
        del self._endpoint_groups[EndpointGroupArn]
        return {}

    def list_endpoint_groups(self, ListenerArn, MaxResults=None, NextToken=None):
        egs = [eg for eg in self._endpoint_groups.values() if eg.ListenerArn == ListenerArn]
        token = None
        if MaxResults and len(egs) > MaxResults:
            token = egs[MaxResults].EndpointGroupArn
            egs = egs[:MaxResults]
        return {"EndpointGroups": [eg.to_dict() for eg in egs],
                "NextToken": token}

    # ── Endpoints ──────────────────────────────────────────────────

    def add_endpoints(self, EndpointGroupArn, EndpointConfigurations):
        record = self._endpoint_groups.get(EndpointGroupArn)
        if not record:
            raise EndpointGroupNotFoundException(f"Endpoint group {EndpointGroupArn} not found")
        record.add_endpoints(EndpointConfigurations)
        return {"EndpointDescriptions": [
            e.to_dict() if hasattr(e, 'to_dict') else e
            for e in record.EndpointConfigurations
        ]}

    def remove_endpoints(self, EndpointGroupArn, EndpointIdentifiers):
        record = self._endpoint_groups.get(EndpointGroupArn)
        if not record:
            raise EndpointGroupNotFoundException(f"Endpoint group {EndpointGroupArn} not found")
        record.remove_endpoints(EndpointIdentifiers)
        return {}

    # ── Tags ───────────────────────────────────────────────────────

    def tag_resource(self, ResourceArn, Tags):
        if isinstance(Tags, list):
            tag_dict = self._tags.get(ResourceArn, {})
            for t in Tags:
                tag_dict[t.get("Key", t.get("key", ""))] = t.get("Value", t.get("value", ""))
            self._tags[ResourceArn] = tag_dict
        return {}

    def untag_resource(self, ResourceArn, TagKeys):
        if ResourceArn in self._tags:
            for k in TagKeys:
                self._tags[ResourceArn].pop(k, None)
        return {}

    def list_tags_for_resource(self, ResourceArn):
        tags = self._tags.get(ResourceArn, {})
        return {"Tags": [{"Key": k, "Value": v} for k, v in tags.items()]}
