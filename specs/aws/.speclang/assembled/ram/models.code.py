"""RAM (Resource Access Manager) store — resource sharing and permissions.

Entities:
  - ResourceShare: shared resources with principals
  - Permission: customer-managed permissions with versions
  - ResourceShareInvitation: cross-account share invitations
  - ResourceShareAssociation: links between shares and resources/principals
"""

import uuid
from datetime import datetime


# ─── Exception classes ───

class InvalidParameterException(Exception):
    def __init__(self, message="Invalid parameter"):
        super().__init__(message)

class ResourceNotFoundException(Exception):
    def __init__(self, message="Resource not found"):
        super().__init__(message)

class UnknownResourceException(Exception):
    def __init__(self, message="Unknown resource"):
        super().__init__(message)

class MalformedArnException(Exception):
    def __init__(self, message="Malformed ARN"):
        super().__init__(message)

class OperationNotPermittedException(Exception):
    def __init__(self, message="Operation not permitted"):
        super().__init__(message)

class ServerInternalException(Exception):
    def __init__(self, message="Internal server error"):
        super().__init__(message)

class ServiceUnavailableException(Exception):
    def __init__(self, message="Service unavailable"):
        super().__init__(message)

class ResourceShareInvitationArnNotFoundException(Exception):
    def __init__(self, message="Invitation ARN not found"):
        super().__init__(message)

class IdempotentParameterMismatchException(Exception):
    def __init__(self, message="Idempotent parameter mismatch"):
        super().__init__(message)

class InvalidClientTokenException(Exception):
    def __init__(self, message="Invalid client token"):
        super().__init__(message)

class TagLimitExceededException(Exception):
    def __init__(self, message="Tag limit exceeded"):
        super().__init__(message)

class TagPolicyViolationException(Exception):
    def __init__(self, message="Tag policy violation"):
        super().__init__(message)

class InvalidPolicyException(Exception):
    def __init__(self, message="Invalid policy"):
        super().__init__(message)

class MalformedPolicyTemplateException(Exception):
    def __init__(self, message="Malformed policy template"):
        super().__init__(message)

class PermissionAlreadyExistsException(Exception):
    def __init__(self, message="Permission already exists"):
        super().__init__(message)

class PermissionLimitExceededException(Exception):
    def __init__(self, message="Permission limit exceeded"):
        super().__init__(message)

class PermissionVersionsLimitExceededException(Exception):
    def __init__(self, message="Permission versions limit exceeded"):
        super().__init__(message)

class InvalidStateTransitionException(Exception):
    def __init__(self, message="Invalid state transition"):
        super().__init__(message)

class MissingRequiredParameterException(Exception):
    def __init__(self, message="Missing required parameter"):
        super().__init__(message)

class ResourceShareLimitExceededException(Exception):
    def __init__(self, message="Resource share limit exceeded"):
        super().__init__(message)

class InvalidResourceTypeException(Exception):
    def __init__(self, message="Invalid resource type"):
        super().__init__(message)

class ResourceArnNotFoundException(Exception):
    def __init__(self, message="Resource ARN not found"):
        super().__init__(message)

class ResourceShareInvitationAlreadyAcceptedException(Exception):
    def __init__(self, message="Invitation already accepted"):
        super().__init__(message)

class ResourceShareInvitationAlreadyRejectedException(Exception):
    def __init__(self, message="Invitation already rejected"):
        super().__init__(message)

class ResourceShareInvitationExpiredException(Exception):
    def __init__(self, message="Invitation expired"):
        super().__init__(message)


# ─── Data records ───

class ResourceShareRecord:
    def __init__(self, name, resourceShareArn=None, owningAccountId=None,
                 allowExternalPrincipals=None, status="ACTIVE", statusMessage=None,
                 tags=None, creationTime=None, lastUpdatedTime=None, featureSet="STANDARD",
                 permissionArns=None):
        self.name = name
        self.resourceShareArn = resourceShareArn or f"arn:aws:ram:us-east-1:000000000000:resource-share/{uuid.uuid4().hex[:12]}"
        self.owningAccountId = owningAccountId or "000000000000"
        self.allowExternalPrincipals = allowExternalPrincipals or False
        self.status = status
        self.statusMessage = statusMessage or ""
        self.tags = tags or []
        self.creationTime = creationTime or datetime.utcnow().isoformat() + "Z"
        self.lastUpdatedTime = lastUpdatedTime or self.creationTime
        self.featureSet = featureSet
        self.permissionArns = permissionArns or []

    def to_dict(self):
        """Convert to AWS response dict."""
        return {
            "resourceShareArn": self.resourceShareArn,
            "name": self.name,
            "owningAccountId": self.owningAccountId,
            "allowExternalPrincipals": self.allowExternalPrincipals,
            "status": self.status,
            "statusMessage": self.statusMessage,
            "tags": self.tags,
            "creationTime": self.creationTime,
            "lastUpdatedTime": self.lastUpdatedTime,
            "featureSet": self.featureSet,
        }


class PermissionRecord:
    def __init__(self, name, resourceType, policyTemplate, permissionArn=None,
                 defaultVersion=None, permissionType="CUSTOMER_MANAGED",
                 creationTime=None, lastUpdatedTime=None, tags=None):
        self.name = name
        self.resourceType = resourceType
        self.policyTemplate = policyTemplate
        self.permissionArn = permissionArn or f"arn:aws:ram:us-east-1:000000000000:permission/{uuid.uuid4().hex[:12]}"
        self.defaultVersion = defaultVersion or 1
        self.permissionType = permissionType
        self.creationTime = creationTime or datetime.utcnow().isoformat() + "Z"
        self.lastUpdatedTime = lastUpdatedTime or self.creationTime
        self.tags = tags or []
        self._versions = {1: policyTemplate}  # version_number → policy_template

    def add_version(self, policy_template):
        """Add a new version, returns the new version number."""
        new_version = max(self._versions.keys()) + 1
        self._versions[new_version] = policy_template
        self.lastUpdatedTime = datetime.utcnow().isoformat() + "Z"
        return new_version

    def get_version(self, version=None):
        """Get a specific version or default."""
        v = version or self.defaultVersion
        return self._versions.get(v)

    def to_dict(self):
        """Convert to AWS response dict."""
        return {
            "permissionArn": self.permissionArn,
            "name": self.name,
            "resourceType": self.resourceType,
            "defaultVersion": True,
            "permissionType": self.permissionType,
            "creationTime": self.creationTime,
            "lastUpdatedTime": self.lastUpdatedTime,
            "tags": self.tags if self.tags else [],
        }


class ResourceShareInvitationRecord:
    def __init__(self, resourceShareInvitationArn=None, resourceShareName=None,
                 resourceShareArn=None, senderAccountId=None, receiverAccountId=None,
                 invitationTimestamp=None, status="PENDING", receiverArn=None):
        self.resourceShareInvitationArn = resourceShareInvitationArn or f"arn:aws:ram:us-east-1:000000000000:resource-share-invitation/{uuid.uuid4().hex[:12]}"
        self.resourceShareName = resourceShareName or ""
        self.resourceShareArn = resourceShareArn or ""
        self.senderAccountId = senderAccountId or ""
        self.receiverAccountId = receiverAccountId or ""
        self.invitationTimestamp = invitationTimestamp or datetime.utcnow().isoformat() + "Z"
        self.status = status
        self.receiverArn = receiverArn or ""

    def to_dict(self):
        return {
            "resourceShareInvitationArn": self.resourceShareInvitationArn,
            "resourceShareName": self.resourceShareName,
            "resourceShareArn": self.resourceShareArn,
            "senderAccountId": self.senderAccountId,
            "receiverAccountId": self.receiverAccountId,
            "invitationTimestamp": self.invitationTimestamp,
            "status": self.status,
            "receiverArn": self.receiverArn,
        }


class ResourceShareAssociationRecord:
    def __init__(self, resourceShareArn, associatedEntity, associationType,
                 resourceShareName=None, status="ASSOCIATING", statusMessage=None,
                 creationTime=None, lastUpdatedTime=None, external=False):
        self.resourceShareArn = resourceShareArn
        self.resourceShareName = resourceShareName or ""
        self.associatedEntity = associatedEntity
        self.associationType = associationType  # PRINCIPAL or RESOURCE
        self.status = status
        self.statusMessage = statusMessage or ""
        self.creationTime = creationTime or datetime.utcnow().isoformat() + "Z"
        self.lastUpdatedTime = lastUpdatedTime or self.creationTime
        self.external = external

    def to_dict(self):
        return {
            "resourceShareArn": self.resourceShareArn,
            "resourceShareName": self.resourceShareName,
            "associatedEntity": self.associatedEntity,
            "associationType": self.associationType,
            "status": self.status,
            "statusMessage": self.statusMessage,
            "creationTime": self.creationTime,
            "lastUpdatedTime": self.lastUpdatedTime,
            "external": self.external,
        }


# ─── Store ───

class RamStore:
    """RAM in-memory store with dict-backed collections."""

    def __init__(self):
        self._resource_shares: dict[str, ResourceShareRecord] = {}
        self._permissions: dict[str, PermissionRecord] = {}
        self._invitations: dict[str, ResourceShareInvitationRecord] = {}
        self._associations: dict[str, list[ResourceShareAssociationRecord]] = {}  # arn → associations
        self._next_id = 0
        self._sharing_enabled = False

    def _generate_id(self):
        self._next_id += 1
        return self._next_id

    def _parse_tags(self, tags):
        """Convert AWS-style tag list [{key, value}] to flat dict."""
        if not tags:
            return []
        result = []
        for t in tags:
            k = t.get("key", t.get("Key", ""))
            v = t.get("value", t.get("Value", ""))
            result.append({"key": k, "value": v})
        return result

    # ─── Resource Shares ───

    def resource_shares(self, arn=None):
        """Method-style accessor for generated handlers."""
        if arn:
            return self._resource_shares.get(arn)
        return list(self._resource_shares.values())

    def create_resource_share(self, name, resourceArns=None, principals=None,
                              tags=None, allowExternalPrincipals=None,
                              clientToken=None, permissionArns=None, sources=None, **kwargs):
        record = ResourceShareRecord(
            name=name,
            allowExternalPrincipals=allowExternalPrincipals,
            tags=self._parse_tags(tags),
            permissionArns=permissionArns or [],
        )
        self._resource_shares[record.resourceShareArn] = record

        # Create associations for resources and principals
        if resourceArns:
            for ra in resourceArns:
                assoc = ResourceShareAssociationRecord(
                    resourceShareArn=record.resourceShareArn,
                    associatedEntity=ra,
                    associationType="RESOURCE",
                    resourceShareName=name,
                )
                self._associations.setdefault(record.resourceShareArn, []).append(assoc)
        if principals:
            for pa in principals:
                assoc = ResourceShareAssociationRecord(
                    resourceShareArn=record.resourceShareArn,
                    associatedEntity=pa,
                    associationType="PRINCIPAL",
                    resourceShareName=name,
                )
                self._associations.setdefault(record.resourceShareArn, []).append(assoc)

        return record.to_dict()

    def get_resource_shares(self, resourceShareArns=None, resourceShareStatus=None,
                            resourceOwner="SELF", name=None, tagFilters=None,
                            nextToken=None, maxResults=None, permissionArn=None,
                            permissionVersion=None, **kwargs):
        if resourceShareArns:
            results = [self._resource_shares[a].to_dict() for a in resourceShareArns if a in self._resource_shares]
        else:
            results = [r.to_dict() for r in self._resource_shares.values()]
            if name:
                results = [r for r in results if name in r.get("name", "")]
            if resourceShareStatus:
                results = [r for r in results if r.get("status") == resourceShareStatus]
        return {"resourceShares": results}

    def update_resource_share(self, resourceShareArn, name=None,
                              allowExternalPrincipals=None, clientToken=None, **kwargs):
        record = self._resource_shares.get(resourceShareArn)
        if not record:
            raise UnknownResourceException(f"Resource share {resourceShareArn} not found")
        if name is not None:
            record.name = name
        if allowExternalPrincipals is not None:
            record.allowExternalPrincipals = allowExternalPrincipals
        record.lastUpdatedTime = datetime.utcnow().isoformat() + "Z"
        return record.to_dict()

    def delete_resource_share(self, resourceShareArn, clientToken=None, **kwargs):
        record = self._resource_shares.pop(resourceShareArn, None)
        if not record:
            raise UnknownResourceException(f"Resource share {resourceShareArn} not found")
        return record.to_dict()

    # ─── Permissions ───

    def permissions(self, arn=None):
        """Method-style accessor for generated handlers."""
        if arn:
            return self._permissions.get(arn)
        return list(self._permissions.values())

    def create_permission(self, name, resourceType, policyTemplate,
                          clientToken=None, tags=None, **kwargs):
        # Check for duplicate name+resourceType
        for p in self._permissions.values():
            if p.name == name and p.resourceType == resourceType:
                raise PermissionAlreadyExistsException(
                    f"Permission {name} for {resourceType} already exists")
        record = PermissionRecord(
            name=name,
            resourceType=resourceType,
            policyTemplate=policyTemplate,
            tags=self._parse_tags(tags),
        )
        self._permissions[record.permissionArn] = record
        return record.to_dict()

    def create_permission_version(self, permissionArn, policyTemplate,
                                  clientToken=None, **kwargs):
        record = self._permissions.get(permissionArn)
        if not record:
            raise ResourceNotFoundException(f"Permission {permissionArn} not found")
        new_version = record.add_version(policyTemplate)
        return {"permissionArn": permissionArn, "version": new_version}

    def get_permission(self, permissionArn, permissionVersion=None, **kwargs):
        record = self._permissions.get(permissionArn)
        if not record:
            raise ResourceNotFoundException(f"Permission {permissionArn} not found")
        result = record.to_dict()
        if permissionVersion:
            result["permissionVersion"] = permissionVersion
            result["policyTemplate"] = record.get_version(permissionVersion)
        else:
            result["permissionVersion"] = record.defaultVersion
            result["policyTemplate"] = record.get_version()
        return result

    def list_permissions(self, resourceType=None, nextToken=None,
                         maxResults=None, permissionType=None, **kwargs):
        results = []
        for p in self._permissions.values():
            if resourceType and p.resourceType != resourceType:
                continue
            if permissionType and p.permissionType != permissionType:
                continue
            results.append(p.to_dict())
        return {"permissions": results}

    def list_permission_versions(self, permissionArn, nextToken=None,
                                 maxResults=None, **kwargs):
        record = self._permissions.get(permissionArn)
        if not record:
            raise ResourceNotFoundException(f"Permission {permissionArn} not found")
        versions = []
        for v_num in sorted(record._versions.keys()):
            versions.append({
                "version": v_num,
                "isDefaultVersion": v_num == record.defaultVersion,
                "creationTime": record.creationTime,
                "lastUpdatedTime": record.lastUpdatedTime,
            })
        return {"versions": versions}

    def set_default_permission_version(self, permissionArn, permissionVersion,
                                       clientToken=None, **kwargs):
        record = self._permissions.get(permissionArn)
        if not record:
            raise ResourceNotFoundException(f"Permission {permissionArn} not found")
        if permissionVersion not in record._versions:
            raise InvalidParameterException(f"Version {permissionVersion} not found")
        record.defaultVersion = permissionVersion
        return {"returnValue": True}

    def delete_permission(self, permissionArn, clientToken=None, **kwargs):
        record = self._permissions.pop(permissionArn, None)
        if not record:
            raise ResourceNotFoundException(f"Permission {permissionArn} not found")
        return {"returnValue": True}

    def delete_permission_version(self, permissionArn, permissionVersion,
                                  clientToken=None, **kwargs):
        record = self._permissions.get(permissionArn)
        if not record:
            raise ResourceNotFoundException(f"Permission {permissionArn} not found")
        if permissionVersion not in record._versions:
            raise InvalidParameterException(f"Version {permissionVersion} not found")
        if permissionVersion == record.defaultVersion:
            raise OperationNotPermittedException("Cannot delete default version")
        del record._versions[permissionVersion]
        return {"returnValue": True}

    # ─── Associations (resource share ↔ resource/principal) ───

    def associate_resource_share(self, resourceShareArn, resourceArns=None,
                                 principals=None, clientToken=None, sources=None, **kwargs):
        record = self._resource_shares.get(resourceShareArn)
        if not record:
            raise UnknownResourceException(f"Resource share {resourceShareArn} not found")
        result_associations = []
        if resourceArns:
            for ra in resourceArns:
                assoc = ResourceShareAssociationRecord(
                    resourceShareArn=resourceShareArn,
                    associatedEntity=ra,
                    associationType="RESOURCE",
                    resourceShareName=record.name,
                    status="ASSOCIATED",
                )
                self._associations.setdefault(resourceShareArn, []).append(assoc)
                result_associations.append(assoc)
        if principals:
            for pa in principals:
                assoc = ResourceShareAssociationRecord(
                    resourceShareArn=resourceShareArn,
                    associatedEntity=pa,
                    associationType="PRINCIPAL",
                    resourceShareName=record.name,
                    status="ASSOCIATED",
                )
                self._associations.setdefault(resourceShareArn, []).append(assoc)
                result_associations.append(assoc)
        return {"resourceShareAssociations": [a.to_dict() for a in result_associations]}

    def disassociate_resource_share(self, resourceShareArn, resourceArns=None,
                                    principals=None, clientToken=None, sources=None, **kwargs):
        record = self._resource_shares.get(resourceShareArn)
        if not record:
            raise UnknownResourceException(f"Resource share {resourceShareArn} not found")
        to_remove = set()
        if resourceArns:
            to_remove.update(resourceArns)
        if principals:
            to_remove.update(principals)
        assocs = self._associations.get(resourceShareArn, [])
        removed = [a for a in assocs if a.associatedEntity in to_remove]
        self._associations[resourceShareArn] = [a for a in assocs if a.associatedEntity not in to_remove]
        return {"resourceShareAssociations": [a.to_dict() for a in removed]}

    def associate_resource_share_permission(self, resourceShareArn, permissionArn,
                                            replace=False, clientToken=None,
                                            permissionVersion=None, **kwargs):
        record = self._resource_shares.get(resourceShareArn)
        if not record:
            raise UnknownResourceException(f"Resource share {resourceShareArn} not found")
        perm = self._permissions.get(permissionArn)
        if not perm:
            raise ResourceNotFoundException(f"Permission {permissionArn} not found")
        if replace:
            record.permissionArns = [permissionArn]
        elif permissionArn not in record.permissionArns:
            record.permissionArns.append(permissionArn)
        return {"returnValue": True}

    def disassociate_resource_share_permission(self, resourceShareArn, permissionArn,
                                               clientToken=None, **kwargs):
        record = self._resource_shares.get(resourceShareArn)
        if not record:
            raise UnknownResourceException(f"Resource share {resourceShareArn} not found")
        if permissionArn in record.permissionArns:
            record.permissionArns.remove(permissionArn)
        return {"returnValue": True}

    def get_resource_share_associations(self, associationType, resourceShareArns=None,
                                        resourceArn=None, principal=None,
                                        associationStatus=None, nextToken=None,
                                        maxResults=None, **kwargs):
        results = []
        for share_arn, assocs in self._associations.items():
            if resourceShareArns and share_arn not in resourceShareArns:
                continue
            for a in assocs:
                if a.associationType != associationType:
                    continue
                if associationStatus and a.status != associationStatus:
                    continue
                if resourceArn and a.associatedEntity != resourceArn:
                    continue
                if principal and a.associatedEntity != principal:
                    continue
                results.append(a.to_dict())
        return {"resourceShareAssociations": results}

    def list_principals(self, resourceOwner="SELF", resourceArn=None,
                        principals=None, resourceType=None,
                        resourceShareArns=None, nextToken=None,
                        maxResults=None, **kwargs):
        results = []
        for share_arn, share in self._resource_shares.items():
            if resourceShareArns and share_arn not in resourceShareArns:
                continue
            assocs = self._associations.get(share_arn, [])
            for a in assocs:
                if a.associationType == "PRINCIPAL":
                    results.append({
                        "id": a.associatedEntity,
                        "resourceShareArn": a.resourceShareArn,
                        "creationTime": a.creationTime,
                        "lastUpdatedTime": a.lastUpdatedTime,
                        "external": a.external,
                    })
        return {"principals": results}

    def list_resources(self, resourceOwner="SELF", principal=None,
                       resourceType=None, resourceArns=None,
                       resourceShareArns=None, nextToken=None,
                       maxResults=None, resourceRegionScope=None, **kwargs):
        results = []
        for share_arn, share in self._resource_shares.items():
            if resourceShareArns and share_arn not in resourceShareArns:
                continue
            assocs = self._associations.get(share_arn, [])
            for a in assocs:
                if a.associationType == "RESOURCE":
                    if resourceArns and a.associatedEntity not in resourceArns:
                        continue
                    if resourceType and resourceType != "ec2:Instance":
                        continue
                    results.append({
                        "arn": a.associatedEntity,
                        "type": resourceType or "ec2:Instance",
                        "resourceShareArn": a.resourceShareArn,
                        "status": "AVAILABLE",
                        "creationTime": a.creationTime,
                        "lastUpdatedTime": a.lastUpdatedTime,
                    })
        return {"resources": results}

    def list_resource_share_permissions(self, resourceShareArn, nextToken=None,
                                        maxResults=None, **kwargs):
        record = self._resource_shares.get(resourceShareArn)
        if not record:
            raise UnknownResourceException(f"Resource share {resourceShareArn} not found")
        perms = []
        for pa in record.permissionArns:
            perm = self._permissions.get(pa)
            if perm:
                perms.append(perm.to_dict())
        return {"permissions": perms}

    # ─── Tags ───

    def tag_resource(self, resourceShareArn=None, tags=None, resourceArn=None, **kwargs):
        target_arn = resourceShareArn or resourceArn
        if not target_arn:
            raise InvalidParameterException("Either resourceShareArn or resourceArn required")
        record = self._resource_shares.get(target_arn)
        if not record:
            raise UnknownResourceException(f"Resource {target_arn} not found")
        parsed = self._parse_tags(tags)
        existing_keys = {t["key"] for t in record.tags}
        for t in parsed:
            if t["key"] in existing_keys:
                # overwrite
                for i, et in enumerate(record.tags):
                    if et["key"] == t["key"]:
                        record.tags[i] = t
            else:
                record.tags.append(t)
        return {}

    def untag_resource(self, resourceShareArn=None, tagKeys=None, resourceArn=None, **kwargs):
        target_arn = resourceShareArn or resourceArn
        if not target_arn:
            raise InvalidParameterException("Either resourceShareArn or resourceArn required")
        record = self._resource_shares.get(target_arn)
        if not record:
            raise UnknownResourceException(f"Resource {target_arn} not found")
        if tagKeys:
            record.tags = [t for t in record.tags if t["key"] not in tagKeys]
        return {}

    # ─── Invitations ───

    def invitations(self, arn=None):
        """Method-style accessor for generated handlers."""
        if arn:
            return self._invitations.get(arn)
        return list(self._invitations.values())

    def create_invitation(self, resourceShareArn, senderAccountId=None,
                          receiverAccountId=None):
        share = self._resource_shares.get(resourceShareArn)
        if not share:
            raise UnknownResourceException(f"Resource share {resourceShareArn} not found")
        invite = ResourceShareInvitationRecord(
            resourceShareName=share.name,
            resourceShareArn=resourceShareArn,
            senderAccountId=senderAccountId or "000000000000",
            receiverAccountId=receiverAccountId or "111111111111",
            status="PENDING",
        )
        self._invitations[invite.resourceShareInvitationArn] = invite
        return invite

    def accept_resource_share_invitation(self, resourceShareInvitationArn,
                                         clientToken=None, **kwargs):
        invite = self._invitations.get(resourceShareInvitationArn)
        if not invite:
            raise ResourceShareInvitationArnNotFoundException(
                f"Invitation {resourceShareInvitationArn} not found")
        if invite.status == "ACCEPTED":
            raise ResourceShareInvitationAlreadyAcceptedException("Already accepted")
        if invite.status == "REJECTED":
            raise ResourceShareInvitationAlreadyRejectedException("Already rejected")
        if invite.status == "EXPIRED":
            raise ResourceShareInvitationExpiredException("Invitation expired")
        invite.status = "ACCEPTED"
        return invite.to_dict()

    def get_resource_share_invitations(self, resourceShareInvitationArns=None,
                                       resourceShareArns=None, nextToken=None,
                                       maxResults=None, **kwargs):
        results = []
        for i in self._invitations.values():
            if resourceShareInvitationArns and i.resourceShareInvitationArn not in resourceShareInvitationArns:
                continue
            if resourceShareArns and i.resourceShareArn not in resourceShareArns:
                continue
            results.append(i.to_dict())
        return {"resourceShareInvitations": results}

    def reject_resource_share_invitation(self, resourceShareInvitationArn,
                                         clientToken=None, **kwargs):
        invite = self._invitations.get(resourceShareInvitationArn)
        if not invite:
            raise ResourceShareInvitationArnNotFoundException(
                f"Invitation {resourceShareInvitationArn} not found")
        if invite.status == "ACCEPTED":
            raise ResourceShareInvitationAlreadyAcceptedException("Already accepted")
        if invite.status == "REJECTED":
            raise ResourceShareInvitationAlreadyRejectedException("Already rejected")
        invite.status = "REJECTED"
        return invite.to_dict()

    # ─── Misc ───

    def enable_sharing_with_aws_organization(self, **kwargs):
        self._sharing_enabled = True
        return {"returnValue": True}

    def list_resource_types(self, nextToken=None, maxResults=None,
                            resourceRegionScope=None, **kwargs):
        return {
            "resourceTypes": [
                {"resourceType": "ec2:Instance", "serviceName": "ec2"},
                {"resourceType": "ec2:Subnet", "serviceName": "ec2"},
                {"resourceType": "rds:Cluster", "serviceName": "rds"},
            ]
        }
