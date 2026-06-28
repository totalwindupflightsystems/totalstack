"""IoT Store — Thing, ThingGroup, ThingType, Policy, Certificate entities."""
import time as _time
import uuid as _uuid


class ResourceNotFoundException(Exception):
    pass


class ResourceInUseException(Exception):
    pass


class ResourceAlreadyExistsException(Exception):
    pass


class ValidationException(Exception):
    pass


class ThingRecord:
    def __init__(self, thingName, thingArn=None, thingTypeName=None,
                 attributes=None, billingGroupName=None,
                 version=1):
        self.thingName = thingName
        self.thingArn = thingArn or f"arn:aws:iot:us-east-1:000000000000:thing/{thingName}"
        self.thingTypeName = thingTypeName
        self.attributes = attributes or {}
        self.billingGroupName = billingGroupName
        self.version = version

    def to_dict(self):
        return {
            "thingName": self.thingName,
            "thingArn": self.thingArn,
            "thingTypeName": self.thingTypeName,
            "attributes": self.attributes,
            "billingGroupName": self.billingGroupName,
            "version": self.version,
        }


class ThingGroupRecord:
    def __init__(self, thingGroupName, thingGroupArn=None,
                 parentGroupName=None, thingGroupProperties=None,
                 version=1):
        self.thingGroupName = thingGroupName
        self.thingGroupArn = thingGroupArn or f"arn:aws:iot:us-east-1:000000000000:thinggroup/{thingGroupName}"
        self.parentGroupName = parentGroupName
        self.thingGroupProperties = thingGroupProperties or {}
        self.version = version

    def to_dict(self):
        return {
            "thingGroupName": self.thingGroupName,
            "thingGroupArn": self.thingGroupArn,
            "parentGroupName": self.parentGroupName,
            "thingGroupProperties": self.thingGroupProperties,
            "version": self.version,
        }


class ThingTypeRecord:
    def __init__(self, thingTypeName, thingTypeArn=None,
                 thingTypeProperties=None, deprecationStatus=None,
                 creationDate=None):
        self.thingTypeName = thingTypeName
        self.thingTypeArn = thingTypeArn or f"arn:aws:iot:us-east-1:000000000000:thingtype/{thingTypeName}"
        self.thingTypeProperties = thingTypeProperties or {}
        self.deprecationStatus = deprecationStatus
        self.creationDate = creationDate or _time.time()

    def to_dict(self):
        return {
            "thingTypeName": self.thingTypeName,
            "thingTypeArn": self.thingTypeArn,
            "thingTypeProperties": self.thingTypeProperties,
            "deprecationStatus": self.deprecationStatus,
            "creationDate": self.creationDate,
        }


class PolicyRecord:
    def __init__(self, policyName, policyArn=None, policyDocument=None,
                 version=None, creationDate=None):
        self.policyName = policyName
        self.policyArn = policyArn or f"arn:aws:iot:us-east-1:000000000000:policy/{policyName}"
        self.policyDocument = policyDocument or '{"Version":"2012-10-17","Statement":[]}'
        self.version = version or 1
        self.creationDate = creationDate or _time.time()

    def to_dict(self):
        return {
            "policyName": self.policyName,
            "policyArn": self.policyArn,
            "policyDocument": self.policyDocument,
            "version": self.version,
            "creationDate": self.creationDate,
        }


class CertificateRecord:
    def __init__(self, certificateId, certificateArn=None,
                 certificatePem=None, certificateStatus="ACTIVE",
                 creationDate=None):
        self.certificateId = certificateId
        self.certificateArn = certificateArn or f"arn:aws:iot:us-east-1:000000000000:cert/{certificateId}"
        self.certificatePem = certificatePem or "-----BEGIN CERTIFICATE-----\nTEST\n-----END CERTIFICATE-----"
        self.certificateStatus = certificateStatus
        self.creationDate = creationDate or _time.time()

    def to_dict(self):
        return {
            "certificateId": self.certificateId,
            "certificateArn": self.certificateArn,
            "certificateStatus": self.certificateStatus,
            "creationDate": self.creationDate,
        }


class IoTStore:
    def __init__(self):
        self._things: dict[str, ThingRecord] = {}
        self._thing_groups: dict[str, ThingGroupRecord] = {}
        self._thing_types: dict[str, ThingTypeRecord] = {}
        self._policies: dict[str, PolicyRecord] = {}
        self._certificates: dict[str, CertificateRecord] = {}

    # ── Thing CRUD ──
    def create_thing(self, **kwargs):
        name = kwargs["thingName"]
        if name in self._things:
            raise ResourceAlreadyExistsException(f"Thing {name} already exists")
        record = ThingRecord(**kwargs)
        self._things[name] = record
        return record.to_dict()

    def describe_thing(self, thingName):
        record = self._things.get(thingName)
        if not record:
            raise ResourceNotFoundException(f"Thing {thingName} not found")
        return record.to_dict()

    def list_things(self, **kwargs):
        return [r.to_dict() for r in self._things.values()]

    def delete_thing(self, thingName):
        if thingName not in self._things:
            raise ResourceNotFoundException(f"Thing {thingName} not found")
        del self._things[thingName]

    def update_thing(self, **kwargs):
        name = kwargs["thingName"]
        record = self._things.get(name)
        if not record:
            raise ResourceNotFoundException(f"Thing {name} not found")
        for key in ("thingTypeName", "attributes", "billingGroupName"):
            if key in kwargs:
                setattr(record, key, kwargs[key])
        return record.to_dict()

    # ── ThingGroup CRUD ──
    def create_thing_group(self, **kwargs):
        name = kwargs["thingGroupName"]
        if name in self._thing_groups:
            raise ResourceAlreadyExistsException(f"ThingGroup {name} already exists")
        record = ThingGroupRecord(**kwargs)
        self._thing_groups[name] = record
        return record.to_dict()

    def describe_thing_group(self, thingGroupName):
        record = self._thing_groups.get(thingGroupName)
        if not record:
            raise ResourceNotFoundException(f"ThingGroup {thingGroupName} not found")
        return record.to_dict()

    def list_thing_groups(self, **kwargs):
        return [r.to_dict() for r in self._thing_groups.values()]

    def delete_thing_group(self, thingGroupName):
        if thingGroupName not in self._thing_groups:
            raise ResourceNotFoundException(f"ThingGroup {thingGroupName} not found")
        del self._thing_groups[thingGroupName]

    def update_thing_group(self, **kwargs):
        name = kwargs["thingGroupName"]
        record = self._thing_groups.get(name)
        if not record:
            raise ResourceNotFoundException(f"ThingGroup {name} not found")
        for key in ("thingGroupProperties",):
            if key in kwargs:
                setattr(record, key, kwargs[key])
        return record.to_dict()

    # ── ThingType CRUD ──
    def create_thing_type(self, **kwargs):
        name = kwargs["thingTypeName"]
        if name in self._thing_types:
            raise ResourceAlreadyExistsException(f"ThingType {name} already exists")
        record = ThingTypeRecord(**kwargs)
        self._thing_types[name] = record
        return record.to_dict()

    def describe_thing_type(self, thingTypeName):
        record = self._thing_types.get(thingTypeName)
        if not record:
            raise ResourceNotFoundException(f"ThingType {thingTypeName} not found")
        return record.to_dict()

    def list_thing_types(self, **kwargs):
        return [r.to_dict() for r in self._thing_types.values()]

    def delete_thing_type(self, thingTypeName):
        if thingTypeName not in self._thing_types:
            raise ResourceNotFoundException(f"ThingType {thingTypeName} not found")
        del self._thing_types[thingTypeName]

    # ── Policy CRUD ──
    def create_policy(self, **kwargs):
        name = kwargs["policyName"]
        if name in self._policies:
            raise ResourceAlreadyExistsException(f"Policy {name} already exists")
        record = PolicyRecord(**kwargs)
        self._policies[name] = record
        return record.to_dict()

    def describe_policy(self, policyName):
        record = self._policies.get(policyName)
        if not record:
            raise ResourceNotFoundException(f"Policy {policyName} not found")
        return record.to_dict()

    def list_policies(self, **kwargs):
        return [r.to_dict() for r in self._policies.values()]

    def delete_policy(self, policyName):
        if policyName not in self._policies:
            raise ResourceNotFoundException(f"Policy {policyName} not found")
        del self._policies[policyName]

    # ── Certificate CRUD ──
    def create_keys_and_certificate(self, **kwargs):
        cert_id = f"cert-{_uuid.uuid4().hex[:10]}"
        record = CertificateRecord(certificateId=cert_id, **kwargs)
        self._certificates[cert_id] = record
        return record.to_dict()

    def describe_certificate(self, certificateId):
        record = self._certificates.get(certificateId)
        if not record:
            raise ResourceNotFoundException(f"Certificate {certificateId} not found")
        return record.to_dict()

    def list_certificates(self, **kwargs):
        return [r.to_dict() for r in self._certificates.values()]

    def delete_certificate(self, certificateId):
        if certificateId not in self._certificates:
            raise ResourceNotFoundException(f"Certificate {certificateId} not found")
        del self._certificates[certificateId]
