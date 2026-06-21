"""CodeDeploy in-memory store, data classes, and exceptions."""
import time
import uuid
from collections import defaultdict


# ╔══════════════════════════════════════════════════════════════╗
# ║                        EXCEPTIONS                           ║
# ╚══════════════════════════════════════════════════════════════╝

class CodeDeployException(Exception):
    status_code = 400

class InvalidInputException(CodeDeployException):
    status_code = 400

class ThrottlingException(CodeDeployException):
    status_code = 429

class InvalidNextTokenException(CodeDeployException):
    status_code = 400

# Application exceptions
class ApplicationNameRequiredException(CodeDeployException):
    status_code = 400

class InvalidApplicationNameException(CodeDeployException):
    status_code = 400

class ApplicationDoesNotExistException(CodeDeployException):
    status_code = 404

class ApplicationAlreadyExistsException(CodeDeployException):
    status_code = 409

class ApplicationLimitExceededException(CodeDeployException):
    status_code = 400

# DeploymentConfig exceptions
class DeploymentConfigNameRequiredException(CodeDeployException):
    status_code = 400

class InvalidDeploymentConfigNameException(CodeDeployException):
    status_code = 400

class DeploymentConfigDoesNotExistException(CodeDeployException):
    status_code = 404

class DeploymentConfigAlreadyExistsException(CodeDeployException):
    status_code = 409

class DeploymentConfigLimitExceededException(CodeDeployException):
    status_code = 400

class DeploymentConfigInUseException(CodeDeployException):
    status_code = 400

class InvalidMinimumHealthyHostValueException(CodeDeployException):
    status_code = 400

class InvalidComputePlatformException(CodeDeployException):
    status_code = 400

# DeploymentGroup exceptions
class DeploymentGroupNameRequiredException(CodeDeployException):
    status_code = 400

class InvalidDeploymentGroupNameException(CodeDeployException):
    status_code = 400

class DeploymentGroupDoesNotExistException(CodeDeployException):
    status_code = 404

class DeploymentGroupAlreadyExistsException(CodeDeployException):
    status_code = 409

class DeploymentGroupLimitExceededException(CodeDeployException):
    status_code = 400

class InvalidRoleException(CodeDeployException):
    status_code = 400

class RoleRequiredException(CodeDeployException):
    status_code = 400

# Deployment exceptions
class DeploymentIdRequiredException(CodeDeployException):
    status_code = 400

class InvalidDeploymentIdException(CodeDeployException):
    status_code = 400

class DeploymentDoesNotExistException(CodeDeployException):
    status_code = 404

class DeploymentAlreadyCompletedException(CodeDeployException):
    status_code = 400

class DeploymentLimitExceededException(CodeDeployException):
    status_code = 400

class RevisionRequiredException(CodeDeployException):
    status_code = 400

class RevisionDoesNotExistException(CodeDeployException):
    status_code = 404

class InvalidRevisionException(CodeDeployException):
    status_code = 400

class DescriptionTooLongException(CodeDeployException):
    status_code = 400

# Generic resource exception (used by batch get)
class ResourceNotFoundException(CodeDeployException):
    status_code = 404


# ╔══════════════════════════════════════════════════════════════╗
# ║                     DATA CLASSES                            ║
# ╚══════════════════════════════════════════════════════════════╝

class ApplicationRecord:
    def __init__(self, application_name, compute_platform='Server', linked_to_github=False, **kwargs):
        self.applicationName = application_name
        self.applicationId = kwargs.get('applicationId', str(uuid.uuid4()))
        self.computePlatform = compute_platform
        self.linkedToGitHub = linked_to_github
        self.createTime = time.time()

    def to_dict(self):
        return {
            'applicationName': self.applicationName,
            'applicationId': self.applicationId,
            'computePlatform': self.computePlatform,
            'linkedToGitHub': self.linkedToGitHub,
            'createTime': self.createTime,
        }


class DeploymentConfigRecord:
    def __init__(self, deployment_config_name, minimum_healthy_hosts=None, compute_platform='Server', **kwargs):
        self.deploymentConfigName = deployment_config_name
        self.deploymentConfigId = kwargs.get('deploymentConfigId', str(uuid.uuid4()))
        self.minimumHealthyHosts = minimum_healthy_hosts or {'type': 'HOST_COUNT', 'value': 1}
        self.computePlatform = compute_platform
        self.createTime = time.time()
        self.trafficRoutingConfig = kwargs.get('trafficRoutingConfig')
        self.zonalConfig = kwargs.get('zonalConfig')

    def to_dict(self):
        return {
            'deploymentConfigName': self.deploymentConfigName,
            'deploymentConfigId': self.deploymentConfigId,
            'minimumHealthyHosts': self.minimumHealthyHosts,
            'computePlatform': self.computePlatform,
            'createTime': self.createTime,
        }


class DeploymentGroupRecord:
    def __init__(self, application_name, deployment_group_name, service_role_arn, **kwargs):
        self.applicationName = application_name
        self.deploymentGroupName = deployment_group_name
        self.deploymentGroupId = kwargs.get('deploymentGroupId', str(uuid.uuid4()))
        self.serviceRoleArn = service_role_arn
        self.deploymentConfigName = kwargs.get('deploymentConfigName', 'CodeDeployDefault.OneAtATime')
        self.ec2TagFilters = kwargs.get('ec2TagFilters', [])
        self.onPremisesInstanceTagFilters = kwargs.get('onPremisesInstanceTagFilters', [])
        self.autoScalingGroups = kwargs.get('autoScalingGroups', [])
        self.triggerConfigurations = kwargs.get('triggerConfigurations', [])
        self.alarmConfiguration = kwargs.get('alarmConfiguration')
        self.autoRollbackConfiguration = kwargs.get('autoRollbackConfiguration')
        self.deploymentStyle = kwargs.get('deploymentStyle')
        self.loadBalancerInfo = kwargs.get('loadBalancerInfo')
        self.blueGreenDeploymentConfiguration = kwargs.get('blueGreenDeploymentConfiguration')
        self.outdatedInstancesStrategy = kwargs.get('outdatedInstancesStrategy', 'UPDATE')
        self.tags = kwargs.get('tags', [])
        self.computePlatform = kwargs.get('computePlatform', 'Server')

    def to_dict(self):
        return {
            'applicationName': self.applicationName,
            'deploymentGroupName': self.deploymentGroupName,
            'deploymentGroupId': self.deploymentGroupId,
            'serviceRoleArn': self.serviceRoleArn,
            'deploymentConfigName': self.deploymentConfigName,
            'ec2TagFilters': self.ec2TagFilters,
            'onPremisesInstanceTagFilters': self.onPremisesInstanceTagFilters,
            'autoScalingGroups': self.autoScalingGroups,
            'triggerConfigurations': self.triggerConfigurations,
            'alarmConfiguration': self.alarmConfiguration,
            'autoRollbackConfiguration': self.autoRollbackConfiguration,
            'deploymentStyle': self.deploymentStyle,
            'loadBalancerInfo': self.loadBalancerInfo,
            'computePlatform': self.computePlatform,
        }


class DeploymentRecord:
    def __init__(self, application_name, deployment_group_name, **kwargs):
        self.deploymentId = kwargs.get('deploymentId', f"d-{uuid.uuid4().hex[:8].upper()}")
        self.applicationName = application_name
        self.deploymentGroupName = deployment_group_name
        self.deploymentConfigName = kwargs.get('deploymentConfigName', 'CodeDeployDefault.OneAtATime')
        self.status = kwargs.get('status', 'Created')
        self.creator = kwargs.get('creator', 'user')
        self.revision = kwargs.get('revision')
        self.description = kwargs.get('description', '')
        self.createTime = time.time()
        self.startTime = kwargs.get('startTime')
        self.completeTime = kwargs.get('completeTime')
        self.fileExistsBehavior = kwargs.get('fileExistsBehavior', 'DISALLOW')
        self.updateOutdatedInstancesOnly = kwargs.get('updateOutdatedInstancesOnly', False)
        self.ignoreApplicationStopFailures = kwargs.get('ignoreApplicationStopFailures', False)
        self.targetInstances = kwargs.get('targetInstances')

    def to_dict(self):
        return {
            'deploymentId': self.deploymentId,
            'applicationName': self.applicationName,
            'deploymentGroupName': self.deploymentGroupName,
            'deploymentConfigName': self.deploymentConfigName,
            'status': self.status,
            'creator': self.creator,
            'revision': self.revision,
            'description': self.description,
            'createTime': self.createTime,
            'startTime': self.startTime,
            'completeTime': self.completeTime,
        }


class RevisionRecord:
    def __init__(self, application_name, revision, **kwargs):
        self.applicationName = application_name
        self.revision = revision
        self.registerTime = time.time()

    def to_dict(self):
        return {
            'applicationName': self.applicationName,
            'revision': self.revision,
            'registerTime': self.registerTime,
        }


# ╔══════════════════════════════════════════════════════════════╗
# ║                        STORES                               ║
# ╚══════════════════════════════════════════════════════════════╝

class ApplicationStore:
    def __init__(self, region='us-east-1', account_id='123456789012'):
        self._apps = {}
        self._region = region
        self._account_id = account_id

    def create_application(self, application_name, compute_platform='Server', **kwargs):
        if not application_name:
            raise ApplicationNameRequiredException("Application name is required")
        if len(application_name) < 1 or len(application_name) > 100:
            raise InvalidApplicationNameException("Application name must be 1-100 characters")
        if application_name in self._apps:
            raise ApplicationAlreadyExistsException(f"Application '{application_name}' already exists")
        if len(self._apps) >= 1000:
            raise ApplicationLimitExceededException("Maximum number of applications reached")
        app = ApplicationRecord(application_name, compute_platform=compute_platform, **kwargs)
        self._apps[application_name] = app
        return app

    def get_application(self, application_name):
        if not application_name:
            raise ApplicationNameRequiredException("Application name is required")
        if application_name not in self._apps:
            raise ApplicationDoesNotExistException(f"Application '{application_name}' does not exist")
        return self._apps[application_name]

    def update_application(self, application_name=None, new_application_name=None):
        # applicationName is optional in UpdateApplication request
        if not application_name and not new_application_name:
            raise ApplicationNameRequiredException("Application name is required")
        # The AWS API uses whichever is present; if only newApplicationName, look up by current
        lookup_name = application_name or new_application_name
        if lookup_name not in self._apps:
            raise ApplicationDoesNotExistException(f"Application '{lookup_name}' does not exist")
        if new_application_name and new_application_name != lookup_name:
            if new_application_name in self._apps:
                raise ApplicationAlreadyExistsException(f"Application '{new_application_name}' already exists")
            app = self._apps.pop(lookup_name)
            app.applicationName = new_application_name
            self._apps[new_application_name] = app
        return self._apps.get(new_application_name or lookup_name)

    def delete_application(self, application_name):
        if not application_name:
            raise ApplicationNameRequiredException("Application name is required")
        if application_name not in self._apps:
            return  # idempotent
        del self._apps[application_name]

    def list_applications(self, next_token=None):
        names = sorted(self._apps.keys())
        return names, None  # full list, no pagination for simplicity

    def batch_get_applications(self, application_names):
        apps = []
        for name in application_names:
            if name in self._apps:
                apps.append(self._apps[name])
        return apps


class DeploymentConfigStore:
    def __init__(self, region='us-east-1', account_id='123456789012'):
        self._configs = {}
        self._region = region
        self._account_id = account_id
        # Seed predefined configs
        self._seed_defaults()

    def _seed_defaults(self):
        defaults = [
            ('CodeDeployDefault.OneAtATime', {'type': 'HOST_COUNT', 'value': 1}),
            ('CodeDeployDefault.HalfAtATime', {'type': 'FLEET_PERCENT', 'value': 50}),
            ('CodeDeployDefault.AllAtOnce', {'type': 'HOST_COUNT', 'value': 0}),
        ]
        for name, mhh in defaults:
            self._configs[name] = DeploymentConfigRecord(name, minimum_healthy_hosts=mhh)

    def create_deployment_config(self, deployment_config_name, minimum_healthy_hosts=None,
                                  compute_platform='Server', **kwargs):
        if not deployment_config_name:
            raise DeploymentConfigNameRequiredException("Deployment config name is required")
        if deployment_config_name in self._configs:
            raise DeploymentConfigAlreadyExistsException(
                f"Deployment config '{deployment_config_name}' already exists")
        if len(self._configs) >= 100:
            raise DeploymentConfigLimitExceededException("Maximum number of deployment configs reached")
        config = DeploymentConfigRecord(deployment_config_name,
                                         minimum_healthy_hosts=minimum_healthy_hosts,
                                         compute_platform=compute_platform, **kwargs)
        self._configs[deployment_config_name] = config
        return config

    def get_deployment_config(self, deployment_config_name):
        if not deployment_config_name:
            raise DeploymentConfigNameRequiredException("Deployment config name is required")
        if deployment_config_name not in self._configs:
            raise DeploymentConfigDoesNotExistException(
                f"Deployment config '{deployment_config_name}' does not exist")
        return self._configs[deployment_config_name]

    def delete_deployment_config(self, deployment_config_name):
        if not deployment_config_name:
            raise DeploymentConfigNameRequiredException("Deployment config name is required")
        if deployment_config_name not in self._configs:
            return  # idempotent
        if deployment_config_name.startswith('CodeDeployDefault.'):
            raise InvalidDeploymentConfigNameException("Cannot delete predefined deployment config")
        del self._configs[deployment_config_name]

    def list_deployment_configs(self, next_token=None):
        names = sorted(self._configs.keys())
        return names, None


class DeploymentGroupStore:
    def __init__(self, region='us-east-1', account_id='123456789012'):
        self._groups = defaultdict(dict)
        self._region = region
        self._account_id = account_id

    def create_deployment_group(self, application_name, deployment_group_name, service_role_arn, **kwargs):
        if not application_name:
            raise ApplicationNameRequiredException("Application name is required")
        if not deployment_group_name:
            raise DeploymentGroupNameRequiredException("Deployment group name is required")
        if not service_role_arn:
            raise RoleRequiredException("serviceRoleArn is required")
        if deployment_group_name in self._groups[application_name]:
            raise DeploymentGroupAlreadyExistsException(
                f"Deployment group '{deployment_group_name}' already exists")
        if sum(len(g) for g in self._groups.values()) >= 1000:
            raise DeploymentGroupLimitExceededException("Maximum number of deployment groups reached")
        group = DeploymentGroupRecord(application_name, deployment_group_name, service_role_arn, **kwargs)
        self._groups[application_name][deployment_group_name] = group
        return group

    def get_deployment_group(self, application_name, deployment_group_name):
        if not application_name:
            raise ApplicationNameRequiredException("Application name is required")
        if not deployment_group_name:
            raise DeploymentGroupNameRequiredException("Deployment group name is required")
        if deployment_group_name not in self._groups.get(application_name, {}):
            raise DeploymentGroupDoesNotExistException(
                f"Deployment group '{deployment_group_name}' not found")
        return self._groups[application_name][deployment_group_name]

    def update_deployment_group(self, application_name, current_deployment_group_name,
                                 new_deployment_group_name=None, **kwargs):
        group = self.get_deployment_group(application_name, current_deployment_group_name)
        if new_deployment_group_name and new_deployment_group_name != current_deployment_group_name:
            if new_deployment_group_name in self._groups[application_name]:
                raise DeploymentGroupAlreadyExistsException(
                    f"Deployment group '{new_deployment_group_name}' already exists")
            del self._groups[application_name][current_deployment_group_name]
            group.deploymentGroupName = new_deployment_group_name
            self._groups[application_name][new_deployment_group_name] = group

        for key, value in kwargs.items():
            if value is not None and hasattr(group, key):
                setattr(group, key, value)
        return group

    def delete_deployment_group(self, application_name, deployment_group_name):
        if not application_name:
            raise ApplicationNameRequiredException("Application name is required")
        if not deployment_group_name:
            raise DeploymentGroupNameRequiredException("Deployment group name is required")
        if application_name in self._groups:
            self._groups[application_name].pop(deployment_group_name, None)

    def list_deployment_groups(self, application_name, next_token=None):
        if not application_name:
            raise ApplicationNameRequiredException("Application name is required")
        names = sorted(self._groups.get(application_name, {}).keys())
        return names, None

    def get_groups_for_app(self, application_name):
        return list(self._groups.get(application_name, {}).values())


class DeploymentStore:
    def __init__(self, region='us-east-1', account_id='123456789012'):
        self._deployments = {}
        self._region = region
        self._account_id = account_id

        # Self-deletion handler — see DeleteResourcesByExternalId
        self.delete_deployment = self._delete_deployment

    def create_deployment(self, application_name, deployment_group_name=None, **kwargs):
        if not application_name:
            raise ApplicationNameRequiredException("Application name is required")
        deployment = DeploymentRecord(application_name, deployment_group_name, **kwargs)
        self._deployments[deployment.deploymentId] = deployment
        return deployment

    def get_deployment(self, deployment_id):
        if not deployment_id:
            raise DeploymentIdRequiredException("Deployment ID is required")
        if deployment_id not in self._deployments:
            raise DeploymentDoesNotExistException(f"Deployment '{deployment_id}' does not exist")
        return self._deployments[deployment_id]

    def _delete_deployment(self, deployment_id):
        self._deployments.pop(deployment_id, None)

    def stop_deployment(self, deployment_id):
        deployment = self.get_deployment(deployment_id)
        if deployment.status in ('Succeeded', 'Failed', 'Stopped'):
            raise DeploymentAlreadyCompletedException(
                f"Deployment '{deployment_id}' has already completed with status '{deployment.status}'")
        deployment.status = 'Stopped'
        deployment.completeTime = time.time()
        return deployment

    def list_deployments(self, application_name=None, deployment_group_name=None,
                          include_only_statuses=None, create_time_range=None, next_token=None):
        results = list(self._deployments.values())

        if application_name:
            results = [d for d in results if d.applicationName == application_name]
        if deployment_group_name:
            results = [d for d in results if d.deploymentGroupName == deployment_group_name]
        if include_only_statuses:
            results = [d for d in results if d.status in include_only_statuses]
        if create_time_range:
            start = create_time_range.get('start', 0)
            end = create_time_range.get('end', float('inf'))
            results = [d for d in results if start <= d.createTime <= end]

        results.sort(key=lambda d: d.createTime, reverse=True)
        return [d.deploymentId for d in results], None

    def batch_get_deployments(self, deployment_ids):
        deployments = []
        for did in deployment_ids:
            if did in self._deployments:
                deployments.append(self._deployments[did])
        return deployments


class RevisionStore:
    def __init__(self):
        self._revisions = defaultdict(list)

    def register_revision(self, application_name, revision, **kwargs):
        rec = RevisionRecord(application_name, revision, **kwargs)
        self._revisions[application_name].append(rec)
        return rec

    def get_revision(self, application_name, revision):
        for r in self._revisions.get(application_name, []):
            if r.revision == revision:
                return r
        raise RevisionDoesNotExistException("Revision not found")

    def list_revisions(self, application_name, next_token=None):
        revs = self._revisions.get(application_name, [])
        return [r.revision for r in revs], None


# ╔══════════════════════════════════════════════════════════════╗
# ║                     AGGREGATE STORE                         ║
# ╚══════════════════════════════════════════════════════════════╝

class CodeDeployStore:
    def __init__(self, region='us-east-1', account_id='123456789012'):
        self.applications = ApplicationStore(region, account_id)
        self.deployment_configs = DeploymentConfigStore(region, account_id)
        self.deployment_groups = DeploymentGroupStore(region, account_id)
        self.deployments = DeploymentStore(region, account_id)
        self.revisions = RevisionStore()
        self._region = region
        self._account_id = account_id


def _now_millis():
    return int(time.time() * 1000)
