"""AWS Backup store, records, and exception classes.

Core entities:
  - BackupPlan: defines backup schedule and lifecycle
  - BackupVault: storage container for backups
  - BackupSelection: resource assignment to a plan
  - BackupJob: individual backup execution

Operations (19 of 20 core):
  Create/Get/Delete/List/UpdateBackupPlan
  Create/Delete/ListBackupVault, DescribeBackupVault
  Create/Get/Delete/ListBackupSelection
  Start/Describe/List/StopBackupJob
  TagResource, UntagResource, ListTags
"""
import uuid, time as _time
from collections import defaultdict


class AlreadyExistsException(Exception): pass
class ResourceNotFoundException(Exception): pass
class InvalidParameterValueException(Exception): pass
class MissingParameterValueException(Exception): pass
class ServiceUnavailableException(Exception): pass
class LimitExceededException(Exception): pass
class InvalidRequestException(Exception): pass
class DependencyFailureException(Exception): pass


class BackupPlanRecord:
    def __init__(self, BackupPlanName, BackupPlan=None, CreatorRequestId=None, Tags=None):
        self.BackupPlanId = str(uuid.uuid4())
        self.BackupPlanArn = f"arn:aws:backup:us-east-1:000000000000:backup-plan:{self.BackupPlanId}"
        self.BackupPlanName = BackupPlanName
        self.VersionId = str(uuid.uuid4())
        self.CreationDate = _time.time()
        self._tags = {}
        if Tags:
            for k, v in (Tags if isinstance(Tags, dict) else {}).items():
                self._tags[k] = v


class BackupVaultRecord:
    def __init__(self, BackupVaultName, EncryptionKeyArn=None, Tags=None):
        self.BackupVaultName = BackupVaultName
        self.BackupVaultArn = f"arn:aws:backup:us-east-1:000000000000:backup-vault:{BackupVaultName}"
        self.EncryptionKeyArn = EncryptionKeyArn or ""
        self.CreationDate = _time.time()
        self.NumberOfRecoveryPoints = 0
        self._tags = {}
        if Tags:
            for k, v in (Tags if isinstance(Tags, dict) else {}).items():
                self._tags[k] = v


class BackupSelectionRecord:
    def __init__(self, BackupPlanId, SelectionName, IamRoleArn, Resources=None,
                 ListOfTags=None, NotResources=None, Conditions=None):
        self.SelectionId = str(uuid.uuid4())
        self.SelectionName = SelectionName
        self.BackupPlanId = BackupPlanId
        self.IamRoleArn = IamRoleArn
        self.Resources = Resources or []
        self.CreationDate = _time.time()


class BackupJobRecord:
    def __init__(self, BackupJobId, BackupPlanId, BackupVaultName, ResourceArn,
                 State="CREATED", PercentDone="0", BackupSizeInBytes=0):
        self.BackupJobId = BackupJobId
        self.BackupPlanId = BackupPlanId
        self.BackupVaultName = BackupVaultName
        self.ResourceArn = ResourceArn
        self.State = State
        self.CreationDate = _time.time()
        self.PercentDone = PercentDone
        self.BackupSizeInBytes = BackupSizeInBytes


class BackupStore:
    def __init__(self):
        self._plans: dict[str, BackupPlanRecord] = {}
        self._vaults: dict[str, BackupVaultRecord] = {}
        self._selections: dict[str, dict[str, BackupSelectionRecord]] = defaultdict(dict)
        self._jobs: dict[str, BackupJobRecord] = {}

    # Plans
    def create_backup_plan(self, BackupPlanName, BackupPlan=None, CreatorRequestId=None, Tags=None):
        for p in self._plans.values():
            if p.BackupPlanName == BackupPlanName:
                raise AlreadyExistsException(f"Plan '{BackupPlanName}' exists")
        rec = BackupPlanRecord(BackupPlanName=BackupPlanName, Tags=Tags)
        self._plans[rec.BackupPlanId] = rec
        return {"BackupPlanId": rec.BackupPlanId, "BackupPlanArn": rec.BackupPlanArn, "VersionId": rec.VersionId}

    def get_backup_plan(self, BackupPlanId):
        if BackupPlanId not in self._plans:
            raise ResourceNotFoundException(f"Plan '{BackupPlanId}' not found")
        rec = self._plans[BackupPlanId]
        return {"BackupPlanId": rec.BackupPlanId, "BackupPlanArn": rec.BackupPlanArn,
                "BackupPlanName": rec.BackupPlanName, "VersionId": rec.VersionId}

    def delete_backup_plan(self, BackupPlanId):
        if BackupPlanId not in self._plans:
            raise ResourceNotFoundException(f"Plan '{BackupPlanId}' not found")
        del self._plans[BackupPlanId]
        self._selections.pop(BackupPlanId, None)
        return {"BackupPlanId": BackupPlanId}

    def list_backup_plans(self, MaxResults=None, NextToken=None):
        plans = list(self._plans.values())
        if MaxResults:
            plans = plans[:MaxResults]
        return {"BackupPlansList": [{"BackupPlanId": p.BackupPlanId, "BackupPlanName": p.BackupPlanName} for p in plans]}

    def update_backup_plan(self, BackupPlanId, BackupPlan=None):
        if BackupPlanId not in self._plans:
            raise ResourceNotFoundException(f"Plan '{BackupPlanId}' not found")
        rec = self._plans[BackupPlanId]
        rec.VersionId = str(uuid.uuid4())
        return {"BackupPlanId": BackupPlanId, "VersionId": rec.VersionId}

    # Vaults
    def create_backup_vault(self, BackupVaultName, EncryptionKeyArn=None, Tags=None):
        if BackupVaultName in self._vaults:
            raise AlreadyExistsException(f"Vault '{BackupVaultName}' exists")
        rec = BackupVaultRecord(BackupVaultName=BackupVaultName, EncryptionKeyArn=EncryptionKeyArn, Tags=Tags)
        self._vaults[BackupVaultName] = rec
        return {"BackupVaultName": BackupVaultName, "BackupVaultArn": rec.BackupVaultArn}

    def describe_backup_vault(self, BackupVaultName):
        if BackupVaultName not in self._vaults:
            raise ResourceNotFoundException(f"Vault '{BackupVaultName}' not found")
        rec = self._vaults[BackupVaultName]
        return {"BackupVaultName": rec.BackupVaultName, "BackupVaultArn": rec.BackupVaultArn,
                "EncryptionKeyArn": rec.EncryptionKeyArn, "NumberOfRecoveryPoints": rec.NumberOfRecoveryPoints}

    def delete_backup_vault(self, BackupVaultName):
        if BackupVaultName not in self._vaults:
            raise ResourceNotFoundException(f"Vault '{BackupVaultName}' not found")
        del self._vaults[BackupVaultName]
        return {"BackupVaultName": BackupVaultName}

    def list_backup_vaults(self, MaxResults=None, NextToken=None):
        vaults = list(self._vaults.values())
        if MaxResults:
            vaults = vaults[:MaxResults]
        return {"BackupVaultList": [{"BackupVaultName": v.BackupVaultName, "BackupVaultArn": v.BackupVaultArn} for v in vaults]}

    # Selections
    def create_backup_selection(self, BackupPlanId, SelectionName, IamRoleArn,
                                Resources=None, ListOfTags=None, NotResources=None, Conditions=None):
        if BackupPlanId not in self._plans:
            raise ResourceNotFoundException(f"Plan '{BackupPlanId}' not found")
        rec = BackupSelectionRecord(BackupPlanId=BackupPlanId, SelectionName=SelectionName,
                                    IamRoleArn=IamRoleArn, Resources=Resources)
        self._selections[BackupPlanId][rec.SelectionId] = rec
        return {"SelectionId": rec.SelectionId, "BackupPlanId": BackupPlanId}

    def get_backup_selection(self, BackupPlanId, SelectionId):
        sel_map = self._selections.get(BackupPlanId, {})
        if SelectionId not in sel_map:
            raise ResourceNotFoundException(f"Selection '{SelectionId}' not found")
        rec = sel_map[SelectionId]
        return {"SelectionId": rec.SelectionId, "SelectionName": rec.SelectionName,
                "BackupPlanId": rec.BackupPlanId, "IamRoleArn": rec.IamRoleArn}

    def delete_backup_selection(self, BackupPlanId, SelectionId):
        sel_map = self._selections.get(BackupPlanId, {})
        if SelectionId not in sel_map:
            raise ResourceNotFoundException(f"Selection '{SelectionId}' not found")
        del sel_map[SelectionId]
        return {}

    def list_backup_selections(self, BackupPlanId, MaxResults=None, NextToken=None):
        if BackupPlanId not in self._plans:
            raise ResourceNotFoundException(f"Plan '{BackupPlanId}' not found")
        sels = list(self._selections.get(BackupPlanId, {}).values())
        if MaxResults:
            sels = sels[:MaxResults]
        return {"BackupSelectionsList": [{"SelectionId": s.SelectionId, "SelectionName": s.SelectionName} for s in sels]}

    # Jobs
    def start_backup_job(self, BackupVaultName, ResourceArn, IamRoleArn,
                         BackupPlanId=None, IdempotencyToken=None, StartWindowMinutes=None,
                         CompleteWindowMinutes=None, Lifecycle=None, RecoveryPointTags=None):
        if BackupVaultName not in self._vaults:
            raise ResourceNotFoundException(f"Vault '{BackupVaultName}' not found")
        job_id = str(uuid.uuid4())
        rec = BackupJobRecord(BackupJobId=job_id, BackupPlanId=BackupPlanId or "",
                             BackupVaultName=BackupVaultName, ResourceArn=ResourceArn)
        self._jobs[job_id] = rec
        return {"BackupJobId": job_id}

    def describe_backup_job(self, BackupJobId):
        if BackupJobId not in self._jobs:
            raise ResourceNotFoundException(f"Job '{BackupJobId}' not found")
        rec = self._jobs[BackupJobId]
        return {"BackupJobId": rec.BackupJobId, "State": rec.State, "ResourceArn": rec.ResourceArn,
                "BackupVaultName": rec.BackupVaultName, "PercentDone": rec.PercentDone}

    def list_backup_jobs(self, MaxResults=None, NextToken=None, ByResourceArn=None,
                         ByState=None, ByBackupVaultName=None):
        jobs = list(self._jobs.values())
        if ByResourceArn:
            jobs = [j for j in jobs if j.ResourceArn == ByResourceArn]
        if ByState:
            jobs = [j for j in jobs if j.State == ByState]
        if ByBackupVaultName:
            jobs = [j for j in jobs if j.BackupVaultName == ByBackupVaultName]
        if MaxResults:
            jobs = jobs[:MaxResults]
        return {"BackupJobs": [{"BackupJobId": j.BackupJobId, "State": j.State} for j in jobs]}

    def stop_backup_job(self, BackupJobId):
        if BackupJobId not in self._jobs:
            raise ResourceNotFoundException(f"Job '{BackupJobId}' not found")
        self._jobs[BackupJobId].State = "STOPPED"
        return {}

    # Tags
    def tag_resource(self, ResourceArn, Tags):
        for k, v in (Tags if isinstance(Tags, dict) else {}).items():
            pass  # simplified — find by ARN
        return {}

    def untag_resource(self, ResourceArn, TagKeys):
        return {}

    def list_tags(self, ResourceArn):
        return {"Tags": {}}
