"""AWS RolesAnywhere service — models and store for TotalStack.
RolesAnywhere enables workloads to obtain temporary AWS credentials using
X.509 certificates without needing IAM roles.
"""
import uuid as _uuid
import time as _time
from collections import defaultdict


# ===================== Exception Classes =====================

class ValidationException(Exception):
    pass

class ResourceNotFoundException(Exception):
    pass

class AccessDeniedException(Exception):
    pass

class TooManyRequestsException(Exception):
    pass


# ===================== Record Classes =====================

class ProfileRecord:
    def __init__(self, profileId=None, name=None, enabled=True, roleArns=None,
                 sessionPolicy=None, durationSeconds=None, managedPolicyArns=None,
                 requireInstanceProperties=None, createdAt=None, updatedAt=None,
                 createdBy=None, tags=None):
        self.profileId = profileId or str(_uuid.uuid4())
        self.name = name
        self.enabled = enabled
        self.roleArns = roleArns or []
        self.sessionPolicy = sessionPolicy or ""
        self.durationSeconds = durationSeconds or 3600
        self.managedPolicyArns = managedPolicyArns or []
        self.requireInstanceProperties = requireInstanceProperties or False
        self.createdAt = createdAt or _time.time()
        self.updatedAt = updatedAt or _time.time()
        self.createdBy = createdBy or "test-user"
        self.tags = tags or {}
        self._profileArn = f"arn:aws:rolesanywhere:us-east-1:123456789012:profile/{self.profileId}"

    @property
    def profileArn(self):
        return self._profileArn

    def to_dict(self):
        return {
            "profileId": self.profileId,
            "profileArn": self.profileArn,
            "name": self.name,
            "enabled": self.enabled,
            "roleArns": self.roleArns,
            "sessionPolicy": self.sessionPolicy,
            "durationSeconds": self.durationSeconds,
            "managedPolicyArns": self.managedPolicyArns,
            "requireInstanceProperties": self.requireInstanceProperties,
            "createdAt": self.createdAt,
            "updatedAt": self.updatedAt,
            "createdBy": self.createdBy,
            "tags": self.tags,
        }


class SourceData:
    def __init__(self, x509CertificateData=None, acmPcaArn=None):
        self.x509CertificateData = x509CertificateData
        self.acmPcaArn = acmPcaArn

    def to_dict(self):
        d = {}
        if self.x509CertificateData:
            d["x509CertificateData"] = self.x509CertificateData
        if self.acmPcaArn:
            d["acmPcaArn"] = self.acmPcaArn
        return d


class Source:
    def __init__(self, sourceData=None, sourceType=None):
        self.sourceData = sourceData
        self.sourceType = sourceType or "CERTIFICATE_BUNDLE"

    def to_dict(self):
        d = {"sourceType": self.sourceType}
        if self.sourceData:
            d["sourceData"] = self.sourceData.to_dict() if hasattr(self.sourceData, 'to_dict') else self.sourceData
        return d


class TrustAnchorRecord:
    def __init__(self, trustAnchorId=None, name=None, enabled=True, source=None,
                 createdAt=None, updatedAt=None, tags=None):
        self.trustAnchorId = trustAnchorId or str(_uuid.uuid4())
        self.name = name
        self.enabled = enabled
        self.source = source
        self.createdAt = createdAt or _time.time()
        self.updatedAt = updatedAt or _time.time()
        self.tags = tags or {}
        self._trustAnchorArn = f"arn:aws:rolesanywhere:us-east-1:123456789012:trust-anchor/{self.trustAnchorId}"

    @property
    def trustAnchorArn(self):
        return self._trustAnchorArn

    def to_dict(self):
        d = {
            "trustAnchorId": self.trustAnchorId,
            "trustAnchorArn": self.trustAnchorArn,
            "name": self.name,
            "enabled": self.enabled,
            "createdAt": self.createdAt,
            "updatedAt": self.updatedAt,
            "tags": self.tags,
        }
        if self.source:
            d["source"] = self.source.to_dict() if hasattr(self.source, 'to_dict') else self.source
        return d


class CrlRecord:
    def __init__(self, crlId=None, name=None, enabled=True, crlData=None,
                 trustAnchorArn=None, createdAt=None, updatedAt=None, tags=None):
        self.crlId = crlId or str(_uuid.uuid4())
        self.name = name
        self.enabled = enabled
        self.crlData = crlData
        self.trustAnchorArn = trustAnchorArn
        self.createdAt = createdAt or _time.time()
        self.updatedAt = updatedAt or _time.time()
        self.tags = tags or {}
        self._crlArn = f"arn:aws:rolesanywhere:us-east-1:123456789012:crl/{self.crlId}"

    @property
    def crlArn(self):
        return self._crlArn

    def to_dict(self):
        d = {
            "crlId": self.crlId,
            "crlArn": self.crlArn,
            "name": self.name,
            "enabled": self.enabled,
            "trustAnchorArn": self.trustAnchorArn,
            "createdAt": self.createdAt,
            "updatedAt": self.updatedAt,
            "tags": self.tags,
        }
        if self.crlData:
            d["crlData"] = self.crlData
        return d


# ===================== Store =====================

class RolesAnywhereStore:
    def __init__(self):
        self._profiles = {}
        self._trust_anchors = {}
        self._crls = {}
        self._subjects = {}
        self._attribute_mappings = defaultdict(dict)
        self._notification_settings = {}
        self._tags = {}

    # ---- Helpers ----
    def _conv_tags(self, tags):
        if not tags:
            return {}
        if isinstance(tags, list):
            d = {}
            for t in tags:
                d[t.get("key", t.get("Key", ""))] = t.get("value", t.get("Value", ""))
            return d
        return dict(tags)

    # ---- Profile Methods ----
    def profiles(self, profileId=None):
        if profileId is not None:
            return self._profiles.get(profileId)
        return list(self._profiles.values())

    def create_profile(self, name, roleArns=None, sessionPolicy=None,
                       durationSeconds=None, managedPolicyArns=None,
                       requireInstanceProperties=None, tags=None, enabled=True):
        record = ProfileRecord(
            name=name, roleArns=roleArns or [], sessionPolicy=sessionPolicy,
            durationSeconds=durationSeconds, managedPolicyArns=managedPolicyArns,
            requireInstanceProperties=requireInstanceProperties, enabled=enabled,
            tags=self._conv_tags(tags),
        )
        self._profiles[record.profileId] = record
        if record.tags:
            self._tags[record.profileArn] = dict(record.tags)
        return record

    def update_profile(self, profileId, name=None, roleArns=None, sessionPolicy=None,
                       durationSeconds=None, managedPolicyArns=None,
                       requireInstanceProperties=None):
        record = self._profiles.get(profileId)
        if not record:
            raise ResourceNotFoundException(f"Profile {profileId} not found")
        if name is not None:
            record.name = name
        if roleArns is not None:
            record.roleArns = roleArns
        if sessionPolicy is not None:
            record.sessionPolicy = sessionPolicy
        if durationSeconds is not None:
            record.durationSeconds = durationSeconds
        if managedPolicyArns is not None:
            record.managedPolicyArns = managedPolicyArns
        if requireInstanceProperties is not None:
            record.requireInstanceProperties = requireInstanceProperties
        record.updatedAt = _time.time()
        return record

    def delete_profile(self, profileId):
        if profileId not in self._profiles:
            raise ResourceNotFoundException(f"Profile {profileId} not found")
        record = self._profiles.pop(profileId)
        record.enabled = False
        return record

    def enable_profile(self, profileId):
        record = self._profiles.get(profileId)
        if not record:
            raise ResourceNotFoundException(f"Profile {profileId} not found")
        record.enabled = True
        return record

    def disable_profile(self, profileId):
        record = self._profiles.get(profileId)
        if not record:
            raise ResourceNotFoundException(f"Profile {profileId} not found")
        record.enabled = False
        return record

    # ---- TrustAnchor Methods ----
    def trust_anchors(self, trustAnchorId=None):
        if trustAnchorId is not None:
            return self._trust_anchors.get(trustAnchorId)
        return list(self._trust_anchors.values())

    def create_trust_anchor(self, name, source=None, enabled=True, tags=None):
        record = TrustAnchorRecord(
            name=name, source=source, enabled=enabled,
            tags=self._conv_tags(tags),
        )
        self._trust_anchors[record.trustAnchorId] = record
        if record.tags:
            self._tags[record.trustAnchorArn] = dict(record.tags)
        return record

    def update_trust_anchor(self, trustAnchorId, name=None, source=None):
        record = self._trust_anchors.get(trustAnchorId)
        if not record:
            raise ResourceNotFoundException(f"Trust anchor {trustAnchorId} not found")
        if name is not None:
            record.name = name
        if source is not None:
            record.source = source
        record.updatedAt = _time.time()
        return record

    def delete_trust_anchor(self, trustAnchorId):
        if trustAnchorId not in self._trust_anchors:
            raise ResourceNotFoundException(f"Trust anchor {trustAnchorId} not found")
        return self._trust_anchors.pop(trustAnchorId)

    def enable_trust_anchor(self, trustAnchorId):
        record = self._trust_anchors.get(trustAnchorId)
        if not record:
            raise ResourceNotFoundException(f"Trust anchor {trustAnchorId} not found")
        record.enabled = True
        return record

    def disable_trust_anchor(self, trustAnchorId):
        record = self._trust_anchors.get(trustAnchorId)
        if not record:
            raise ResourceNotFoundException(f"Trust anchor {trustAnchorId} not found")
        record.enabled = False
        return record

    # ---- CRL Methods ----
    def crls(self, crlId=None):
        if crlId is not None:
            return self._crls.get(crlId)
        return list(self._crls.values())

    def import_crl(self, name, crlData, trustAnchorArn=None, enabled=True, tags=None):
        record = CrlRecord(
            name=name, crlData=crlData, trustAnchorArn=trustAnchorArn,
            enabled=enabled, tags=self._conv_tags(tags),
        )
        self._crls[record.crlId] = record
        if record.tags:
            self._tags[record.crlArn] = dict(record.tags)
        return record

    def update_crl(self, crlId, name=None, crlData=None):
        record = self._crls.get(crlId)
        if not record:
            raise ResourceNotFoundException(f"CRL {crlId} not found")
        if name is not None:
            record.name = name
        if crlData is not None:
            record.crlData = crlData
        record.updatedAt = _time.time()
        return record

    def delete_crl(self, crlId):
        if crlId not in self._crls:
            raise ResourceNotFoundException(f"CRL {crlId} not found")
        return self._crls.pop(crlId)

    def enable_crl(self, crlId):
        record = self._crls.get(crlId)
        if not record:
            raise ResourceNotFoundException(f"CRL {crlId} not found")
        record.enabled = True
        return record

    def disable_crl(self, crlId):
        record = self._crls.get(crlId)
        if not record:
            raise ResourceNotFoundException(f"CRL {crlId} not found")
        record.enabled = False
        return record

    # ---- Subject Methods ----
    def subjects(self, subjectId=None):
        if subjectId is not None:
            return self._subjects.get(subjectId)
        return list(self._subjects.values())

    # ---- Attribute Mappings ----
    def put_attribute_mapping(self, profileId, certificateField, mappingRules):
        if profileId not in self._profiles:
            raise ResourceNotFoundException(f"Profile {profileId} not found")
        self._attribute_mappings[profileId][certificateField] = mappingRules
        return {"profileId": profileId, "certificateField": certificateField, "mappingRules": mappingRules}

    def delete_attribute_mapping(self, profileId, certificateField):
        self._attribute_mappings.get(profileId, {}).pop(certificateField, None)
        return {}

    # ---- Notification Settings ----
    def put_notification_settings(self, enabled=None, channel=None, threshold=None,
                                  eventTypes=None):
        self._notification_settings = {
            "enabled": enabled or True,
            "channel": channel or "ALL",
            "threshold": threshold or 0,
            "eventTypes": eventTypes or [],
        }
        return dict(self._notification_settings)

    def reset_notification_settings(self):
        self._notification_settings = {}
        return {}

    def get_notification_settings(self):
        return dict(self._notification_settings)

    # ---- Tags ----
    def tag_resource(self, resourceArn, tags):
        tag_dict = self._conv_tags(tags)
        if resourceArn not in self._tags:
            self._tags[resourceArn] = {}
        self._tags[resourceArn].update(tag_dict)

    def untag_resource(self, resourceArn, tagKeys):
        if resourceArn in self._tags:
            for k in tagKeys:
                self._tags[resourceArn].pop(k, None)

    def list_tags(self, resourceArn):
        return self._tags.get(resourceArn, {})
