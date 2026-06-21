"""CodeBuild in-memory store, data classes, and exceptions."""
import time
import uuid
from collections import defaultdict


# ╔══════════════════════════════════════════════════════════════╗
# ║                        EXCEPTIONS                           ║
# ╚══════════════════════════════════════════════════════════════╝

class CodeBuildException(Exception):
    """Base exception for CodeBuild."""
    status_code = 400

class InvalidInputException(CodeBuildException):
    """Invalid or malformed request."""
    status_code = 400

class ResourceNotFoundException(CodeBuildException):
    """Resource not found."""
    status_code = 404

class ResourceAlreadyExistsException(CodeBuildException):
    """Resource already exists."""
    status_code = 409

class AccountLimitExceededException(CodeBuildException):
    """Account limit exceeded."""
    status_code = 400

class OAuthProviderException(CodeBuildException):
    """OAuth token/provider error."""
    status_code = 400


# ╔══════════════════════════════════════════════════════════════╗
# ║                     DATA CLASSES                            ║
# ╚══════════════════════════════════════════════════════════════╝

class ProjectRecord:
    """Represents a CodeBuild project."""
    def __init__(self, name, source, environment, artifacts, service_role, **kwargs):
        self.name = name
        self.arn = kwargs.get('arn', '')
        self.source = source
        self.artifacts = artifacts
        self.environment = environment
        self.serviceRole = service_role
        self.timeoutInMinutes = kwargs.get('timeoutInMinutes', 60)
        self.queuedTimeoutInMinutes = kwargs.get('queuedTimeoutInMinutes', 480)
        self.encryptionKey = kwargs.get('encryptionKey', '')
        self.tags = kwargs.get('tags', [])
        self.badgeEnabled = kwargs.get('badgeEnabled', False)
        self.buildBatchConfig = kwargs.get('buildBatchConfig')
        self.cache = kwargs.get('cache')
        self.concurrentBuildLimit = kwargs.get('concurrentBuildLimit', 1)
        self.description = kwargs.get('description', '')
        self.fileSystemLocations = kwargs.get('fileSystemLocations', [])
        self.logsConfig = kwargs.get('logsConfig')
        self.queuedTimeoutInMinutes = kwargs.get('queuedTimeoutInMinutes', 480)
        self.secondaryArtifacts = kwargs.get('secondaryArtifacts', [])
        self.secondarySources = kwargs.get('secondarySources', [])
        self.secondarySourceVersions = kwargs.get('secondarySourceVersions', [])
        self.sourceVersion = kwargs.get('sourceVersion', '')
        self.vpcConfig = kwargs.get('vpcConfig')
        self.created = time.time()
        self.lastModified = self.created
        self.buildBatchConfig = kwargs.get('buildBatchConfig')
        self.visibility = kwargs.get('visibility', 'PRIVATE')

    def to_dict(self):
        return {
            'name': self.name,
            'arn': self.arn,
            'source': self.source,
            'artifacts': self.artifacts,
            'environment': self.environment,
            'serviceRole': self.serviceRole,
            'timeoutInMinutes': self.timeoutInMinutes,
            'queuedTimeoutInMinutes': self.queuedTimeoutInMinutes,
            'encryptionKey': self.encryptionKey,
            'tags': self.tags,
            'created': self.created,
            'lastModified': self.lastModified,
        }


class BuildRecord:
    """Represents a CodeBuild build execution."""
    def __init__(self, project_name, **kwargs):
        self.id = kwargs.get('id', f"{project_name}:{uuid.uuid4().hex[:8]}")
        self.arn = kwargs.get('arn', '')
        self.projectName = project_name
        self.buildNumber = kwargs.get('buildNumber', 0)
        self.buildStatus = kwargs.get('buildStatus', 'QUEUED')
        self.startTime = kwargs.get('startTime', time.time())
        self.endTime = kwargs.get('endTime')
        self.currentPhase = kwargs.get('currentPhase', 'QUEUED')
        self.phases = kwargs.get('phases', [])
        self.source = kwargs.get('source')
        self.artifacts = kwargs.get('artifacts')
        self.environment = kwargs.get('environment')
        self.logs = kwargs.get('logs')
        self.initiator = kwargs.get('initiator', '')
        self.buildComplete = kwargs.get('buildComplete', False)
        self.sourceVersion = kwargs.get('sourceVersion', '')
        self.queuedTimeoutInMinutes = kwargs.get('queuedTimeoutInMinutes', 480)
        self.timeoutInMinutes = kwargs.get('timeoutInMinutes', 60)

    def to_dict(self):
        return {
            'id': self.id,
            'arn': self.arn,
            'projectName': self.projectName,
            'buildNumber': self.buildNumber,
            'buildStatus': self.buildStatus,
            'startTime': self.startTime,
            'endTime': self.endTime,
            'currentPhase': self.currentPhase,
            'initiator': self.initiator,
            'buildComplete': self.buildComplete,
        }


class WebhookRecord:
    """Represents a CodeBuild webhook."""
    def __init__(self, project_name, **kwargs):
        self.projectName = project_name
        self.url = kwargs.get('url', '')
        self.payloadUrl = kwargs.get('payloadUrl', '')
        self.secret = kwargs.get('secret', '')
        self.branchFilter = kwargs.get('branchFilter', '')
        self.filterGroups = kwargs.get('filterGroups', [])
        self.buildType = kwargs.get('buildType', 'BUILD')
        self.lastModifiedSecret = time.time()

    def to_dict(self):
        return {
            'projectName': self.projectName,
            'url': self.url,
            'payloadUrl': self.payloadUrl,
            'secret': self.secret,
            'branchFilter': self.branchFilter,
            'filterGroups': self.filterGroups,
            'buildType': self.buildType,
            'lastModifiedSecret': self.lastModifiedSecret,
        }


class FleetRecord:
    """Represents a CodeBuild compute fleet."""
    def __init__(self, name, **kwargs):
        self.name = name
        self.arn = kwargs.get('arn', '')
        self.baseCapacity = kwargs.get('baseCapacity', 1)
        self.computeType = kwargs.get('computeType', 'BUILD_GENERAL1_SMALL')
        self.environmentType = kwargs.get('environmentType', 'LINUX_CONTAINER')
        self.created = time.time()
        self.lastModified = self.created

    def to_dict(self):
        return {
            'name': self.name,
            'arn': self.arn,
            'baseCapacity': self.baseCapacity,
            'computeType': self.computeType,
            'environmentType': self.environmentType,
            'created': self.created,
            'lastModified': self.lastModified,
        }


class ReportGroupRecord:
    """Represents a CodeBuild report group."""
    def __init__(self, name, **kwargs):
        self.name = name
        self.arn = kwargs.get('arn', '')
        self.type = kwargs.get('type', 'TEST')
        self.exportConfig = kwargs.get('exportConfig')
        self.created = time.time()
        self.lastModified = self.created

    def to_dict(self):
        return {
            'name': self.name,
            'arn': self.arn,
            'type': self.type,
            'exportConfig': self.exportConfig,
            'created': self.created,
            'lastModified': self.lastModified,
        }


class SourceCredentialsRecord:
    """Represents source credentials (OAuth tokens)."""
    def __init__(self, **kwargs):
        self.arn = kwargs.get('arn', '')
        self.serverType = kwargs.get('serverType', 'GITHUB')
        self.authType = kwargs.get('authType', 'PERSONAL_ACCESS_TOKEN')
        self.token = kwargs.get('token', '')


# ╔══════════════════════════════════════════════════════════════╗
# ║                        STORES                               ║
# ╚══════════════════════════════════════════════════════════════╝

class ProjectStore:
    """In-memory store for CodeBuild projects."""
    def __init__(self, region='us-east-1', account_id='123456789012'):
        self._projects = {}
        self._region = region
        self._account_id = account_id
        self._build_counter = defaultdict(int)

    def _make_arn(self, resource_type, name):
        return f"arn:aws:codebuild:{self._region}:{self._account_id}:{resource_type}/{name}"

    def create_project(self, name, source, environment, artifacts, service_role, **kwargs):
        if not name:
            raise InvalidInputException("Project name is required")
        if name in self._projects:
            raise ResourceAlreadyExistsException(f"Project '{name}' already exists")
        if len(self._projects) >= 1000:
            raise AccountLimitExceededException("Maximum number of projects reached")
        arn = self._make_arn('project', name)
        project = ProjectRecord(name, source, environment, artifacts, service_role, arn=arn, **kwargs)
        self._projects[name] = project
        return project

    def get_project(self, name):
        if name not in self._projects:
            raise ResourceNotFoundException(f"Project '{name}' not found")
        return self._projects[name]

    def update_project(self, name, **kwargs):
        project = self.get_project(name)
        for key, value in kwargs.items():
            if hasattr(project, key):
                setattr(project, key, value)
        project.lastModified = time.time()
        return project

    def delete_project(self, name):
        if name not in self._projects:
            raise ResourceNotFoundException(f"Project '{name}' not found")
        del self._projects[name]

    def list_projects(self, sort_by='NAME', sort_order='ASCENDING', next_token=None, max_results=100):
        names = sorted(self._projects.keys())
        if sort_order == 'DESCENDING':
            names.reverse()
        return names

    def batch_get_projects(self, names):
        projects = []
        not_found = []
        for name in names:
            if name in self._projects:
                projects.append(self._projects[name])
            else:
                not_found.append(name)
        return projects, not_found


class BuildStore:
    """In-memory store for CodeBuild builds."""
    def __init__(self, region='us-east-1', account_id='123456789012'):
        self._builds = {}
        self._region = region
        self._account_id = account_id
        self._counter = 0

    def _make_arn(self, resource_type, name):
        return f"arn:aws:codebuild:{self._region}:{self._account_id}:{resource_type}/{name}"

    def _next_id(self, project_name):
        self._counter += 1
        base = project_name.split('#')[0][:20]
        return f"{base}:{uuid.uuid4().hex[:8]}"

    def start_build(self, project_name, **kwargs):
        build_id = self._next_id(project_name)
        arn = self._make_arn('build', build_id)
        record = BuildRecord(project_name, id=build_id, arn=arn, buildNumber=self._counter, **kwargs)
        record.buildStatus = 'IN_PROGRESS'
        self._builds[build_id] = record
        return record

    def get_build(self, build_id):
        if build_id not in self._builds:
            raise ResourceNotFoundException(f"Build '{build_id}' not found")
        return self._builds[build_id]

    def stop_build(self, build_id):
        build = self.get_build(build_id)
        if build.buildStatus not in ('IN_PROGRESS', 'QUEUED', 'PROVISIONING'):
            raise InvalidInputException(f"Cannot stop build in status '{build.buildStatus}'")
        build.buildStatus = 'STOPPED'
        build.endTime = time.time()
        build.buildComplete = True
        return build

    def delete_build(self, build_id):
        if build_id not in self._builds:
            raise ResourceNotFoundException(f"Build '{build_id}' not found")
        del self._builds[build_id]

    def batch_get_builds(self, ids):
        builds = []
        not_found = []
        for bid in ids:
            if bid in self._builds:
                builds.append(self._builds[bid])
            else:
                not_found.append(bid)
        return builds, not_found

    def list_builds(self, sort_order='ASCENDING', next_token=None, max_results=100):
        ids = sorted(self._builds.keys(), key=lambda x: self._builds[x].startTime, reverse=(sort_order == 'DESCENDING'))
        return ids

    def list_builds_for_project(self, project_name, sort_order='ASCENDING', next_token=None, max_results=100):
        ids = sorted(
            [bid for bid, b in self._builds.items() if b.projectName == project_name],
            key=lambda x: self._builds[x].startTime,
            reverse=(sort_order == 'DESCENDING')
        )
        return ids


class FleetStore:
    """In-memory store for CodeBuild fleets."""
    def __init__(self, region='us-east-1', account_id='123456789012'):
        self._fleets = {}
        self._region = region
        self._account_id = account_id

    def _make_arn(self, resource_type, name):
        return f"arn:aws:codebuild:{self._region}:{self._account_id}:{resource_type}/{name}"

    def create_fleet(self, name, **kwargs):
        if not name:
            raise InvalidInputException("Fleet name is required")
        if name in self._fleets:
            raise ResourceAlreadyExistsException(f"Fleet '{name}' already exists")
        arn = self._make_arn('fleet', name)
        fleet = FleetRecord(name, arn=arn, **kwargs)
        self._fleets[name] = fleet
        return fleet

    def get_fleet(self, name):
        if name not in self._fleets:
            raise ResourceNotFoundException(f"Fleet '{name}' not found")
        return self._fleets[name]

    def delete_fleet(self, name):
        if name not in self._fleets:
            raise ResourceNotFoundException(f"Fleet '{name}' not found")
        del self._fleets[name]

    def list_fleets(self, sort_order='ASCENDING', next_token=None, max_results=100):
        names = sorted(self._fleets.keys())
        return names


class ReportGroupStore:
    """In-memory store for CodeBuild report groups."""
    def __init__(self, region='us-east-1', account_id='123456789012'):
        self._groups = {}
        self._region = region
        self._account_id = account_id

    def _make_arn(self, resource_type, name):
        return f"arn:aws:codebuild:{self._region}:{self._account_id}:{resource_type}/{name}"

    def create_report_group(self, name, **kwargs):
        if not name:
            raise InvalidInputException("Report group name is required")
        if name in self._groups:
            raise ResourceAlreadyExistsException(f"Report group '{name}' already exists")
        arn = self._make_arn('report-group', name)
        group = ReportGroupRecord(name, arn=arn, **kwargs)
        self._groups[name] = group
        return group

    def get_report_group(self, name):
        if name not in self._groups:
            raise ResourceNotFoundException(f"Report group '{name}' not found")
        return self._groups[name]

    def delete_report_group(self, name):
        if name not in self._groups:
            raise ResourceNotFoundException(f"Report group '{name}' not found")
        del self._groups[name]

    def batch_get_report_groups(self, names):
        groups = []
        not_found = []
        for name in names:
            if name in self._groups:
                groups.append(self._groups[name])
            else:
                not_found.append(name)
        return groups, not_found


class WebhookStore:
    """In-memory store for CodeBuild webhooks."""
    def __init__(self):
        self._webhooks = {}

    def create_webhook(self, project_name, **kwargs):
        if project_name in self._webhooks:
            raise ResourceAlreadyExistsException(f"Webhook for project '{project_name}' already exists")
        webhook = WebhookRecord(project_name, **kwargs)
        webhook.url = f"https://codebuild.us-east-1.amazonaws.com/webhooks/{project_name}"
        webhook.payloadUrl = webhook.url
        self._webhooks[project_name] = webhook
        return webhook

    def get_webhook(self, project_name):
        if project_name not in self._webhooks:
            raise ResourceNotFoundException(f"Webhook for project '{project_name}' not found")
        return self._webhooks[project_name]

    def delete_webhook(self, project_name):
        if project_name not in self._webhooks:
            raise ResourceNotFoundException(f"Webhook for project '{project_name}' not found")
        del self._webhooks[project_name]

    def update_webhook(self, project_name, **kwargs):
        webhook = self.get_webhook(project_name)
        for key, value in kwargs.items():
            if hasattr(webhook, key):
                setattr(webhook, key, value)
        webhook.lastModifiedSecret = time.time()
        return webhook


class SourceCredentialsStore:
    """In-memory store for source credentials."""
    def __init__(self, region='us-east-1', account_id='123456789012'):
        self._credentials = {}
        self._region = region
        self._account_id = account_id

    def _make_arn(self, resource_type, name):
        return f"arn:aws:codebuild:{self._region}:{self._account_id}:{resource_type}/{name}"

    def import_credentials(self, token, server_type='GITHUB', auth_type='PERSONAL_ACCESS_TOKEN', username=''):
        arn = self._make_arn('token', server_type.lower())
        creds = SourceCredentialsRecord(arn=arn, serverType=server_type, authType=auth_type, token=token)
        self._credentials[arn] = creds
        if username:
            self._credentials[f"user:{username}"] = creds
        return creds

    def list_credentials(self):
        return [c for k, c in self._credentials.items() if not k.startswith('user:')]

    def delete_credentials(self, arn):
        if arn not in self._credentials:
            raise ResourceNotFoundException(f"Source credentials '{arn}' not found")
        del self._credentials[arn]


class CodeBuildStore:
    """Aggregate store for all CodeBuild resources."""
    def __init__(self, region='us-east-1', account_id='123456789012'):
        self.projects = ProjectStore(region, account_id)
        self.builds = BuildStore(region, account_id)
        self.fleets = FleetStore(region, account_id)
        self.report_groups = ReportGroupStore(region, account_id)
        self.webhooks = WebhookStore()
        self.source_credentials = SourceCredentialsStore(region, account_id)
        self._region = region
        self._account_id = account_id


# Helpers for generated handler files
def _generate_project_arn(region, account_id, name):
    return f"arn:aws:codebuild:{region}:{account_id}:project/{name}"

def _generate_build_arn(region, account_id, build_id):
    return f"arn:aws:codebuild:{region}:{account_id}:build/{build_id}"

def _now_millis():
    return int(time.time() * 1000)
