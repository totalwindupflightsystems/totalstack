"""AWS Signer service — models and store for TotalStack.
Signer is AWS's code signing service for creating digitally signed code packages.
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

class ServiceLimitExceededException(Exception):
    pass

class ConflictException(Exception):
    pass

class TooManyRequestsException(Exception):
    pass

class InternalServiceErrorException(Exception):
    pass

class BadRequestException(Exception):
    pass

class NotFoundException(Exception):
    pass

class ThrottlingException(Exception):
    pass

class SigningProfileNotFoundException(ResourceNotFoundException):
    pass


# ===================== Data/Record Classes =====================

class SignatureValidityPeriod:
    def __init__(self, value=None, type=None):
        self.value = value
        self.type = type

    def to_dict(self):
        return {"value": self.value, "type": self.type}


class SigningMaterial:
    def __init__(self, certificateArn=None):
        self.certificateArn = certificateArn

    def to_dict(self):
        return {"certificateArn": self.certificateArn}


class SigningPlatformOverrides:
    def __init__(self, signingConfiguration=None, signingImageFormat=None):
        self.signingConfiguration = signingConfiguration
        self.signingImageFormat = signingImageFormat

    def to_dict(self):
        d = {}
        if self.signingConfiguration:
            d["signingConfiguration"] = self.signingConfiguration
        if self.signingImageFormat:
            d["signingImageFormat"] = self.signingImageFormat
        return d


class Source:
    def __init__(self, s3=None):
        self.s3 = s3

    def to_dict(self):
        d = {}
        if self.s3:
            d["s3"] = self.s3
        return d


class S3Source:
    def __init__(self, bucketName=None, key=None, version=None):
        self.bucketName = bucketName
        self.key = key
        self.version = version

    def to_dict(self):
        d = {"bucketName": self.bucketName, "key": self.key}
        if self.version:
            d["version"] = self.version
        return d


class Destination:
    def __init__(self, s3=None):
        self.s3 = s3

    def to_dict(self):
        d = {}
        if self.s3:
            d["s3"] = self.s3
        return d


class S3Destination:
    def __init__(self, bucketName=None, prefix=None):
        self.bucketName = bucketName
        self.prefix = prefix

    def to_dict(self):
        d = {"bucketName": self.bucketName}
        if self.prefix:
            d["prefix"] = self.prefix
        return d


class SigningConfiguration:
    def __init__(self, encryptionAlgorithmOptions=None, hashAlgorithmOptions=None):
        self.encryptionAlgorithmOptions = encryptionAlgorithmOptions
        self.hashAlgorithmOptions = hashAlgorithmOptions

    def to_dict(self):
        d = {}
        if self.encryptionAlgorithmOptions:
            d["encryptionAlgorithmOptions"] = self.encryptionAlgorithmOptions
        if self.hashAlgorithmOptions:
            d["hashAlgorithmOptions"] = self.hashAlgorithmOptions
        return d


class SigningImageFormat:
    def __init__(self, supportedFormats=None, defaultFormat=None):
        self.supportedFormats = supportedFormats or []
        self.defaultFormat = defaultFormat

    def to_dict(self):
        return {"supportedFormats": self.supportedFormats, "defaultFormat": self.defaultFormat}


class SignedObject:
    def __init__(self, s3=None):
        self.s3 = s3

    def to_dict(self):
        d = {}
        if self.s3:
            d["s3"] = self.s3
        return d


class SigningJobRevocationRecord:
    def __init__(self, reason=None, revokedAt=None, revokedBy=None):
        self.reason = reason
        self.revokedAt = revokedAt
        self.revokedBy = revokedBy

    def to_dict(self):
        return {"reason": self.reason, "revokedAt": self.revokedAt, "revokedBy": self.revokedBy}


class SigningProfileRevocationRecord:
    def __init__(self, revocationEffectiveFrom=None, revokedAt=None, revokedBy=None):
        self.revocationEffectiveFrom = revocationEffectiveFrom
        self.revokedAt = revokedAt
        self.revokedBy = revokedBy

    def to_dict(self):
        return {
            "revocationEffectiveFrom": self.revocationEffectiveFrom,
            "revokedAt": self.revokedAt,
            "revokedBy": self.revokedBy,
        }


class Permission:
    def __init__(self, action=None, principal=None, statementId=None, profileVersion=None):
        self.action = action
        self.principal = principal
        self.statementId = statementId
        self.profileVersion = profileVersion

    def to_dict(self):
        return {
            "action": self.action,
            "principal": self.principal,
            "statementId": self.statementId,
            "profileVersion": self.profileVersion,
        }


class ProfileRecord:
    def __init__(self, profileName, platformId, profileVersion=None, profileVersionArn=None,
                 arn=None, status="Active", statusReason=None, signingMaterial=None,
                 signatureValidityPeriod=None, overrides=None, signingParameters=None,
                 platformDisplayName=None, tags=None, revocationRecord=None):
        self.profileName = profileName
        self.platformId = platformId
        self.profileVersion = profileVersion or str(_uuid.uuid4())[:8]
        self.profileVersionArn = profileVersionArn or f"arn:aws:signer:us-east-1:123456789012:/signing-profiles/{profileName}/{self.profileVersion}"
        self.arn = arn or f"arn:aws:signer:us-east-1:123456789012:/signing-profiles/{profileName}"
        self.status = status
        self.statusReason = statusReason
        self.signingMaterial = signingMaterial
        self.signatureValidityPeriod = signatureValidityPeriod
        self.overrides = overrides
        self.signingParameters = signingParameters or {}
        self.platformDisplayName = platformDisplayName or platformId
        self.tags = tags or {}
        self.revocationRecord = revocationRecord

    def to_dict(self):
        d = {
            "profileName": self.profileName,
            "profileVersion": self.profileVersion,
            "profileVersionArn": self.profileVersionArn,
            "arn": self.arn,
            "status": self.status,
            "platformId": self.platformId,
            "platformDisplayName": self.platformDisplayName,
            "signingParameters": self.signingParameters,
            "tags": self.tags,
        }
        if self.signingMaterial:
            d["signingMaterial"] = self.signingMaterial.to_dict() if hasattr(self.signingMaterial, 'to_dict') else self.signingMaterial
        if self.signatureValidityPeriod:
            d["signatureValidityPeriod"] = self.signatureValidityPeriod.to_dict() if hasattr(self.signatureValidityPeriod, 'to_dict') else self.signatureValidityPeriod
        if self.overrides:
            d["overrides"] = self.overrides.to_dict() if hasattr(self.overrides, 'to_dict') else self.overrides
        if self.statusReason:
            d["statusReason"] = self.statusReason
        if self.revocationRecord:
            d["revocationRecord"] = self.revocationRecord.to_dict() if hasattr(self.revocationRecord, 'to_dict') else self.revocationRecord
        return d


class JobRecord:
    def __init__(self, jobId, source, destination, profileName, profileVersion=None,
                 platformId=None, profileOwner=None, createdBy=None, status="InProgress",
                 statusReason=None, signedObject=None, signingMaterial=None,
                 overrides=None, signingParameters=None, createdAt=None,
                 completedAt=None, signatureExpiresAt=None, revocationRecord=None,
                 jobOwner=None, jobInvoker=None):
        self.jobId = jobId
        self.source = source
        self.destination = destination
        self.profileName = profileName
        self.profileVersion = profileVersion or "1"
        self.platformId = platformId
        self.profileOwner = profileOwner or "123456789012"
        self.createdBy = createdBy or "test-user"
        self.status = status
        self.statusReason = statusReason
        self.signedObject = signedObject
        self.signingMaterial = signingMaterial
        self.overrides = overrides
        self.signingParameters = signingParameters or {}
        self.createdAt = createdAt or _time.time()
        self.completedAt = completedAt
        self.signatureExpiresAt = signatureExpiresAt
        self.revocationRecord = revocationRecord
        self.jobOwner = jobOwner or "123456789012"
        self.jobInvoker = jobInvoker or "123456789012"

    def to_dict(self):
        d = {
            "jobId": self.jobId,
            "profileName": self.profileName,
            "profileVersion": self.profileVersion,
            "profileOwner": self.profileOwner,
            "createdBy": self.createdBy,
            "status": self.status,
            "signingParameters": self.signingParameters,
            "createdAt": self.createdAt,
            "jobOwner": self.jobOwner,
            "jobInvoker": self.jobInvoker,
        }
        if self.source:
            d["source"] = self.source.to_dict() if hasattr(self.source, 'to_dict') else self.source
        if self.destination:
            d["destination"] = self.destination.to_dict() if hasattr(self.destination, 'to_dict') else self.destination
        if self.platformId:
            d["platformId"] = self.platformId
        if self.statusReason:
            d["statusReason"] = self.statusReason
        if self.signedObject:
            d["signedObject"] = self.signedObject.to_dict() if hasattr(self.signedObject, 'to_dict') else self.signedObject
        if self.signingMaterial:
            d["signingMaterial"] = self.signingMaterial.to_dict() if hasattr(self.signingMaterial, 'to_dict') else self.signingMaterial
        if self.overrides:
            d["overrides"] = self.overrides.to_dict() if hasattr(self.overrides, 'to_dict') else self.overrides
        if self.completedAt:
            d["completedAt"] = self.completedAt
        if self.signatureExpiresAt:
            d["signatureExpiresAt"] = self.signatureExpiresAt
        if self.revocationRecord:
            d["revocationRecord"] = self.revocationRecord.to_dict() if hasattr(self.revocationRecord, 'to_dict') else self.revocationRecord
        return d


class PlatformRecord:
    def __init__(self, platformId, displayName=None, partner=None, target=None,
                 category=None, signingConfiguration=None, signingImageFormat=None,
                 maxSizeInMB=None, revocationSupported=None):
        self.platformId = platformId
        self.displayName = displayName or platformId
        self.partner = partner or "AWS"
        self.target = target or "AWS Lambda"
        self.category = category or "AWSIoT"
        self.signingConfiguration = signingConfiguration
        self.signingImageFormat = signingImageFormat
        self.maxSizeInMB = maxSizeInMB or 250
        self.revocationSupported = revocationSupported if revocationSupported is not None else False

    def to_dict(self):
        d = {
            "platformId": self.platformId,
            "displayName": self.displayName,
            "partner": self.partner,
            "target": self.target,
            "category": self.category,
            "maxSizeInMB": self.maxSizeInMB,
            "revocationSupported": self.revocationSupported,
        }
        if self.signingConfiguration:
            d["signingConfiguration"] = self.signingConfiguration.to_dict() if hasattr(self.signingConfiguration, 'to_dict') else self.signingConfiguration
        if self.signingImageFormat:
            d["signingImageFormat"] = self.signingImageFormat.to_dict() if hasattr(self.signingImageFormat, 'to_dict') else self.signingImageFormat
        return d


# ===================== Store =====================

class SignerStore:
    def __init__(self):
        self._profiles = {}
        self._jobs = {}
        self._platforms = {}
        self._profile_permissions = defaultdict(dict)  # profileName -> {statementId: Permission}
        self._tags = {}  # resourceArn -> {key: value}

        # Pre-populate common signing platforms
        self._init_default_platforms()

    def _init_default_platforms(self):
        for pid in ["AWSLambda-SHA384-ECDSA", "AmazonFreeRTOS-TI-CC3220SF", "AmazonFreeRTOS-Default",
                     "Notation-OCI-SHA384-ECDSA"]:
            self._platforms[pid] = PlatformRecord(
                platformId=pid,
                displayName=pid.replace("-", " "),
                category="AWSIoT" if "FreeRTOS" in pid else "AWS Lambda",
                revocationSupported=True,
            )

    # ---- Platform accessors (read-only, method-style) ----
    def platforms(self, platformId=None):
        if platformId is not None:
            return self._platforms.get(platformId)
        return list(self._platforms.values())

    # ---- Profile accessors ----
    def profiles(self, profileName=None):
        if profileName is not None:
            return self._profiles.get(profileName)
        return list(self._profiles.values())

    def create_profile(self, profileName, platformId, signingMaterial=None,
                       signatureValidityPeriod=None, overrides=None,
                       signingParameters=None, tags=None):
        if profileName in self._profiles:
            raise ConflictException(f"Signing profile {profileName} already exists")

        if isinstance(signingMaterial, dict):
            signingMaterial = SigningMaterial(**signingMaterial)
        if isinstance(signatureValidityPeriod, dict):
            signatureValidityPeriod = SignatureValidityPeriod(**signatureValidityPeriod)
        if isinstance(overrides, dict):
            overrides = SigningPlatformOverrides(**overrides)

        record = ProfileRecord(
            profileName=profileName,
            platformId=platformId,
            signingMaterial=signingMaterial,
            signatureValidityPeriod=signatureValidityPeriod,
            overrides=overrides,
            signingParameters=signingParameters,
        )

        # Handle tags conversion
        if tags:
            if isinstance(tags, list):
                tag_dict = {}
                for t in tags:
                    tag_dict[t.get("key", t.get("Key", ""))] = t.get("value", t.get("Value", ""))
                record.tags = tag_dict
            elif isinstance(tags, dict):
                record.tags = tags

        self._profiles[profileName] = record
        if record.tags:
            self._tags[record.arn] = dict(record.tags)
        return record

    def update_profile(self, profileName, signingMaterial=None,
                       signatureValidityPeriod=None, overrides=None,
                       signingParameters=None, tags=None):
        record = self._profiles.get(profileName)
        if not record:
            raise ResourceNotFoundException(f"Signing profile {profileName} not found")

        # Generate new version
        record.profileVersion = str(_uuid.uuid4())[:8]
        record.profileVersionArn = f"arn:aws:signer:us-east-1:123456789012:/signing-profiles/{profileName}/{record.profileVersion}"

        if signingMaterial is not None:
            if isinstance(signingMaterial, dict):
                signingMaterial = SigningMaterial(**signingMaterial)
            record.signingMaterial = signingMaterial
        if signatureValidityPeriod is not None:
            if isinstance(signatureValidityPeriod, dict):
                signatureValidityPeriod = SignatureValidityPeriod(**signatureValidityPeriod)
            record.signatureValidityPeriod = signatureValidityPeriod
        if overrides is not None:
            if isinstance(overrides, dict):
                overrides = SigningPlatformOverrides(**overrides)
            record.overrides = overrides
        if signingParameters is not None:
            record.signingParameters = signingParameters
        if tags is not None:
            if isinstance(tags, list):
                tag_dict = {}
                for t in tags:
                    tag_dict[t.get("key", t.get("Key", ""))] = t.get("value", t.get("Value", ""))
                record.tags = tag_dict
            elif isinstance(tags, dict):
                record.tags = tags
            if record.tags:
                self._tags[record.arn] = dict(record.tags)

        return record

    def cancel_profile(self, profileName):
        record = self._profiles.get(profileName)
        if not record:
            raise ResourceNotFoundException(f"Signing profile {profileName} not found")
        record.status = "Canceled"

    def revoke_profile(self, profileName, profileVersion, reason, effectiveTime):
        record = self._profiles.get(profileName)
        if not record:
            raise ResourceNotFoundException(f"Signing profile {profileName} not found")
        record.status = "Revoked"
        record.revocationRecord = SigningProfileRevocationRecord(
            revocationEffectiveFrom=effectiveTime,
            revokedAt=_time.time(),
            revokedBy="test-user",
        )

    # ---- Job accessors ----
    def jobs(self, jobId=None):
        if jobId is not None:
            return self._jobs.get(jobId)
        return list(self._jobs.values())

    def start_job(self, source, destination, profileName, clientRequestToken,
                  profileOwner=None):
        # Check profile exists
        if profileName not in self._profiles:
            raise ResourceNotFoundException(f"Signing profile {profileName} not found")

        profile = self._profiles[profileName]

        jobId = str(_uuid.uuid4())
        if isinstance(source, dict):
            source = Source(**source)
        if isinstance(destination, dict):
            destination = Destination(**destination)

        record = JobRecord(
            jobId=jobId,
            source=source,
            destination=destination,
            profileName=profileName,
            profileVersion=profile.profileVersion,
            platformId=profile.platformId,
            profileOwner=profileOwner,
            status="Succeeded",
        )
        self._jobs[jobId] = record
        return record

    def revoke_signature(self, jobId, reason, jobOwner=None):
        record = self._jobs.get(jobId)
        if not record:
            raise ResourceNotFoundException(f"Signing job {jobId} not found")
        record.revocationRecord = SigningJobRevocationRecord(
            reason=reason,
            revokedAt=_time.time(),
            revokedBy=jobOwner or "123456789012",
        )

    # ---- Profile Permissions ----
    def add_permission(self, profileName, action, principal, statementId,
                       profileVersion=None, revisionId=None):
        if profileName not in self._profiles:
            raise ResourceNotFoundException(f"Signing profile {profileName} not found")

        if statementId in self._profile_permissions[profileName]:
            raise ConflictException(f"Permission statement {statementId} already exists")

        perm = Permission(action=action, principal=principal, statementId=statementId,
                         profileVersion=profileVersion)
        self._profile_permissions[profileName][statementId] = perm
        return str(_uuid.uuid4())[:8]  # revisionId

    def remove_permission(self, profileName, statementId, revisionId):
        if profileName not in self._profile_permissions:
            raise ResourceNotFoundException(f"No permissions for profile {profileName}")
        if statementId not in self._profile_permissions[profileName]:
            raise ResourceNotFoundException(f"Permission {statementId} not found")
        del self._profile_permissions[profileName][statementId]
        return str(_uuid.uuid4())[:8]  # new revisionId

    def list_permissions(self, profileName, nextToken=None):
        if profileName not in self._profiles:
            raise ResourceNotFoundException(f"Signing profile {profileName} not found")
        perms = list(self._profile_permissions.get(profileName, {}).values())
        rev_id = str(_uuid.uuid4())[:8]
        return perms, rev_id, None  # permissions, revisionId, nextToken

    # ---- Tags ----
    def tag_resource(self, resourceArn, tags):
        if isinstance(tags, list):
            tag_dict = {}
            for t in tags:
                tag_dict[t.get("key", t.get("Key", ""))] = t.get("value", t.get("Value", ""))
            tags = tag_dict
        if resourceArn not in self._tags:
            self._tags[resourceArn] = {}
        self._tags[resourceArn].update(tags)

    def untag_resource(self, resourceArn, tagKeys):
        if resourceArn in self._tags:
            for k in tagKeys:
                self._tags[resourceArn].pop(k, None)

    def list_tags(self, resourceArn):
        return self._tags.get(resourceArn, {})

    # ---- Sign Payload ----
    def sign_payload(self, profileName, payload, payloadFormat, profileOwner=None):
        if profileName not in self._profiles:
            raise ResourceNotFoundException(f"Signing profile {profileName} not found")
        jobId = str(_uuid.uuid4())
        return {
            "jobId": jobId,
            "jobOwner": profileOwner or "123456789012",
            "metadata": {},
            "signature": b"signed-data-mock",
        }

    # ---- Revocation Status ----
    def get_revocation_status(self, signatureTimestamp, platformId, profileVersionArn,
                              jobArn, certificateHashes):
        return {"revokedEntities": []}
