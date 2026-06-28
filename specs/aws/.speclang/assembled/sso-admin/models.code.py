"""SSO Admin store — IAM Identity Center management.

Entities:
  - Instance: SSO instance
  - PermissionSet: permission sets with policy attachments
  - AccountAssignment: principal→account→permissionSet assignments
  - Application: managed applications
"""

import uuid
from datetime import datetime


# ─── Exception classes ───

class ResourceNotFoundException(Exception):
    def __init__(self, message="Resource not found"):
        super().__init__(message)

class ValidationException(Exception):
    def __init__(self, message="Validation error"):
        super().__init__(message)

class ConflictException(Exception):
    def __init__(self, message="Conflict"):
        super().__init__(message)

class ThrottlingException(Exception):
    def __init__(self, message="Too many requests"):
        super().__init__(message)

class InternalServerException(Exception):
    def __init__(self, message="Internal server error"):
        super().__init__(message)

class ServiceQuotaExceededException(Exception):
    def __init__(self, message="Service quota exceeded"):
        super().__init__(message)

class AccessDeniedException(Exception):
    def __init__(self, message="Access denied"):
        super().__init__(message)


# ─── Data records ───

class InstanceRecord:
    def __init__(self, instanceArn=None, identityStoreId=None, name=None,
                 ownerAccountId=None, status="ACTIVE", createdDate=None):
        self.instanceArn = instanceArn or f"arn:aws:sso:::instance/ssoins-{uuid.uuid4().hex[:16]}"
        self.identityStoreId = identityStoreId or f"d-{uuid.uuid4().hex[:8]}"
        self.name = name or "Default"
        self.ownerAccountId = ownerAccountId or "000000000000"
        self.status = status
        self.createdDate = createdDate or datetime.utcnow().isoformat() + "Z"
        self._accessControlAttributes = None
        self._regions = set()

    def to_dict(self):
        return {
            "instanceArn": self.instanceArn,
            "identityStoreId": self.identityStoreId,
            "name": self.name,
            "ownerAccountId": self.ownerAccountId,
            "status": self.status,
            "createdDate": self.createdDate,
        }


class PermissionSetRecord:
    def __init__(self, instanceArn, name, permissionSetArn=None,
                 description=None, relayState=None, sessionDuration=None,
                 createdDate=None, tags=None):
        self.instanceArn = instanceArn
        self.name = name
        self.permissionSetArn = permissionSetArn or f"arn:aws:sso:::permissionSet/{instanceArn.split('/')[-1]}/ps-{uuid.uuid4().hex[:16]}"
        self.description = description or ""
        self.relayState = relayState or ""
        self.sessionDuration = sessionDuration or "PT1H"
        self.createdDate = createdDate or datetime.utcnow().isoformat() + "Z"
        self.tags = tags or []
        self._inlinePolicy = None
        self._permissionsBoundary = None
        self._managedPolicies = []
        self._customerManagedPolicyRefs = []

    def to_dict(self):
        return {
            "instanceArn": self.instanceArn,
            "name": self.name,
            "permissionSetArn": self.permissionSetArn,
            "description": self.description,
            "relayState": self.relayState,
            "sessionDuration": self.sessionDuration,
            "createdDate": self.createdDate,
        }


class AccountAssignmentRecord:
    def __init__(self, instanceArn, targetId, targetType, permissionSetArn,
                 principalType, principalId, status="SUCCEEDED",
                 requestId=None):
        self.instanceArn = instanceArn
        self.targetId = targetId
        self.targetType = targetType
        self.permissionSetArn = permissionSetArn
        self.principalType = principalType
        self.principalId = principalId
        self.status = status
        self.requestId = requestId or f"ar-{uuid.uuid4().hex[:16]}"
        self.createdDate = datetime.utcnow().isoformat() + "Z"

    def to_dict(self):
        return {
            "instanceArn": self.instanceArn,
            "targetId": self.targetId,
            "targetType": self.targetType,
            "permissionSetArn": self.permissionSetArn,
            "principalType": self.principalType,
            "principalId": self.principalId,
            "status": self.status,
            "requestId": self.requestId,
            "createdDate": self.createdDate,
        }


class ApplicationRecord:
    def __init__(self, instanceArn, applicationProviderArn, name,
                 applicationArn=None, description=None, status="ENABLED",
                 portalOptions=None):
        self.instanceArn = instanceArn
        self.applicationProviderArn = applicationProviderArn
        self.name = name
        self.applicationArn = applicationArn or f"arn:aws:sso:::application/{instanceArn.split('/')[-1]}/apl-{uuid.uuid4().hex[:16]}"
        self.description = description or ""
        self.status = status
        self.portalOptions = portalOptions or {}

    def to_dict(self):
        return {
            "instanceArn": self.instanceArn,
            "applicationProviderArn": self.applicationProviderArn,
            "name": self.name,
            "applicationArn": self.applicationArn,
            "description": self.description,
            "status": self.status,
        }


# ─── Store ───

class SsoAdminStore:
    """SSO Admin in-memory store."""

    def __init__(self):
        self._instances: dict[str, InstanceRecord] = {}
        self._permission_sets: dict[str, PermissionSetRecord] = {}
        self._account_assignments: list[AccountAssignmentRecord] = []
        self._applications: dict[str, ApplicationRecord] = {}

    def _parse_tags(self, tags):
        if not tags:
            return []
        return [{"key": t.get("key", t.get("Key", "")), "value": t.get("value", t.get("Value", ""))} for t in tags]

    # ─── Instance ───

    def instances(self, arn=None):
        if arn:
            return self._instances.get(arn)
        return list(self._instances.values())

    def create_instance(self, name=None, tags=None, **kwargs):
        record = InstanceRecord(name=name)
        self._instances[record.instanceArn] = record
        return record.to_dict()

    def describe_instance(self, instanceArn, **kwargs):
        record = self._instances.get(instanceArn)
        if not record:
            raise ResourceNotFoundException(f"Instance {instanceArn} not found")
        return record.to_dict()

    def update_instance(self, instanceArn, name=None, **kwargs):
        record = self._instances.get(instanceArn)
        if not record:
            raise ResourceNotFoundException(f"Instance {instanceArn} not found")
        if name is not None:
            record.name = name
        return record.to_dict()

    def delete_instance(self, instanceArn, **kwargs):
        record = self._instances.pop(instanceArn, None)
        if not record:
            raise ResourceNotFoundException(f"Instance {instanceArn} not found")
        return {}

    def list_instances(self, maxResults=None, nextToken=None, **kwargs):
        return {"instances": [i.to_dict() for i in self._instances.values()]}

    # ─── Permission Set ───

    def permission_sets(self, arn=None):
        if arn:
            return self._permission_sets.get(arn)
        return list(self._permission_sets.values())

    def create_permission_set(self, name, instanceArn, description=None,
                              relayState=None, sessionDuration=None,
                              tags=None, **kwargs):
        record = PermissionSetRecord(
            instanceArn=instanceArn, name=name,
            description=description, relayState=relayState,
            sessionDuration=sessionDuration, tags=self._parse_tags(tags),
        )
        self._permission_sets[record.permissionSetArn] = record
        resp = record.to_dict()
        resp["permissionSet"] = resp.copy()
        return resp

    def describe_permission_set(self, instanceArn, permissionSetArn, **kwargs):
        record = self._permission_sets.get(permissionSetArn)
        if not record:
            raise ResourceNotFoundException(f"PermissionSet {permissionSetArn} not found")
        resp = record.to_dict()
        resp["permissionSet"] = resp.copy()
        return resp

    def update_permission_set(self, instanceArn, permissionSetArn,
                              description=None, relayState=None,
                              sessionDuration=None, **kwargs):
        record = self._permission_sets.get(permissionSetArn)
        if not record:
            raise ResourceNotFoundException(f"PermissionSet {permissionSetArn} not found")
        if description is not None:
            record.description = description
        if relayState is not None:
            record.relayState = relayState
        if sessionDuration is not None:
            record.sessionDuration = sessionDuration
        return {}

    def delete_permission_set(self, instanceArn, permissionSetArn, **kwargs):
        record = self._permission_sets.pop(permissionSetArn, None)
        if not record:
            raise ResourceNotFoundException(f"PermissionSet {permissionSetArn} not found")
        return {}

    def list_permission_sets(self, instanceArn, maxResults=None, nextToken=None, **kwargs):
        psts = [ps.permissionSetArn for ps in self._permission_sets.values()
                if ps.instanceArn == instanceArn]
        return {"permissionSets": psts}

    def put_inline_policy_to_permission_set(self, instanceArn, permissionSetArn,
                                            inlinePolicy, **kwargs):
        record = self._permission_sets.get(permissionSetArn)
        if not record:
            raise ResourceNotFoundException(f"PermissionSet {permissionSetArn} not found")
        record._inlinePolicy = inlinePolicy
        return {}

    def get_inline_policy_for_permission_set(self, instanceArn, permissionSetArn, **kwargs):
        record = self._permission_sets.get(permissionSetArn)
        if not record:
            raise ResourceNotFoundException(f"PermissionSet {permissionSetArn} not found")
        return {"inlinePolicy": record._inlinePolicy or ""}

    def delete_inline_policy_from_permission_set(self, instanceArn, permissionSetArn, **kwargs):
        record = self._permission_sets.get(permissionSetArn)
        if not record:
            raise ResourceNotFoundException(f"PermissionSet {permissionSetArn} not found")
        record._inlinePolicy = None
        return {}

    def attach_managed_policy_to_permission_set(self, instanceArn, permissionSetArn,
                                                managedPolicyArn, **kwargs):
        record = self._permission_sets.get(permissionSetArn)
        if not record:
            raise ResourceNotFoundException(f"PermissionSet {permissionSetArn} not found")
        if managedPolicyArn not in record._managedPolicies:
            record._managedPolicies.append(managedPolicyArn)
        return {}

    def detach_managed_policy_from_permission_set(self, instanceArn, permissionSetArn,
                                                  managedPolicyArn, **kwargs):
        record = self._permission_sets.get(permissionSetArn)
        if not record:
            raise ResourceNotFoundException(f"PermissionSet {permissionSetArn} not found")
        if managedPolicyArn in record._managedPolicies:
            record._managedPolicies.remove(managedPolicyArn)
        return {}

    def list_managed_policies_in_permission_set(self, instanceArn, permissionSetArn,
                                                maxResults=None, nextToken=None, **kwargs):
        record = self._permission_sets.get(permissionSetArn)
        if not record:
            raise ResourceNotFoundException(f"PermissionSet {permissionSetArn} not found")
        return {"attachedManagedPolicies": [{"arn": p} for p in record._managedPolicies]}

    # ─── Account Assignment ───

    def create_account_assignment(self, instanceArn, targetId, targetType,
                                  permissionSetArn, principalType, principalId, **kwargs):
        record = AccountAssignmentRecord(
            instanceArn=instanceArn, targetId=targetId, targetType=targetType,
            permissionSetArn=permissionSetArn, principalType=principalType,
            principalId=principalId,
        )
        self._account_assignments.append(record)
        return {"accountAssignmentCreationStatus": record.to_dict()}

    def delete_account_assignment(self, instanceArn, targetId, targetType,
                                  permissionSetArn, principalType, principalId, **kwargs):
        to_remove = None
        for aa in self._account_assignments:
            if (aa.instanceArn == instanceArn and aa.targetId == targetId
                    and aa.targetType == targetType and aa.permissionSetArn == permissionSetArn
                    and aa.principalType == principalType and aa.principalId == principalId
                    and aa.status == "SUCCEEDED"):
                to_remove = aa
                break
        if not to_remove:
            raise ResourceNotFoundException("Account assignment not found")
        to_remove.status = "DELETED"
        return {"accountAssignmentDeletionStatus": to_remove.to_dict()}

    def list_account_assignments(self, instanceArn, accountId, permissionSetArn,
                                 maxResults=None, nextToken=None, **kwargs):
        results = []
        for aa in self._account_assignments:
            if (aa.instanceArn == instanceArn and aa.targetId == accountId
                    and aa.permissionSetArn == permissionSetArn and aa.status == "SUCCEEDED"):
                results.append(aa.to_dict())
        return {"accountAssignments": results}

    def list_account_assignments_for_principal(self, instanceArn, principalId,
                                               principalType, maxResults=None,
                                               nextToken=None, **kwargs):
        results = []
        for aa in self._account_assignments:
            if (aa.instanceArn == instanceArn and aa.principalId == principalId
                    and aa.principalType == principalType and aa.status == "SUCCEEDED"):
                results.append(aa.to_dict())
        return {"accountAssignments": results}

    def describe_account_assignment_creation_status(self, instanceArn,
                                                    accountAssignmentCreationRequestId, **kwargs):
        for aa in self._account_assignments:
            if aa.requestId == accountAssignmentCreationRequestId:
                return {"accountAssignmentCreationStatus": aa.to_dict()}
        raise ResourceNotFoundException("Creation status not found")

    def describe_account_assignment_deletion_status(self, instanceArn,
                                                    accountAssignmentDeletionRequestId, **kwargs):
        for aa in self._account_assignments:
            if aa.requestId == accountAssignmentDeletionRequestId:
                return {"accountAssignmentDeletionStatus": aa.to_dict()}
        raise ResourceNotFoundException("Deletion status not found")

    # ─── Application ───

    def applications(self, arn=None):
        if arn:
            return self._applications.get(arn)
        return list(self._applications.values())

    def create_application(self, instanceArn, applicationProviderArn, name,
                           description=None, portalOptions=None, tags=None, **kwargs):
        record = ApplicationRecord(
            instanceArn=instanceArn,
            applicationProviderArn=applicationProviderArn,
            name=name, description=description,
        )
        self._applications[record.applicationArn] = record
        return record.to_dict()

    def describe_application(self, applicationArn, **kwargs):
        record = self._applications.get(applicationArn)
        if not record:
            raise ResourceNotFoundException(f"Application {applicationArn} not found")
        return record.to_dict()

    def update_application(self, applicationArn, name=None, description=None,
                           status=None, portalOptions=None, **kwargs):
        record = self._applications.get(applicationArn)
        if not record:
            raise ResourceNotFoundException(f"Application {applicationArn} not found")
        if name is not None:
            record.name = name
        if description is not None:
            record.description = description
        if status is not None:
            record.status = status
        return record.to_dict()

    def delete_application(self, applicationArn, **kwargs):
        record = self._applications.pop(applicationArn, None)
        if not record:
            raise ResourceNotFoundException(f"Application {applicationArn} not found")
        return {}

    def list_applications(self, instanceArn, maxResults=None, nextToken=None, **kwargs):
        apps = [a.to_dict() for a in self._applications.values()
                if a.instanceArn == instanceArn]
        return {"applications": apps}

    # ─── Tags ───

    def tag_resource(self, resourceArn, tags, **kwargs):
        return {}

    def untag_resource(self, resourceArn, tagKeys, **kwargs):
        return {}

    def list_tags_for_resource(self, resourceArn, **kwargs):
        return {"tags": []}
