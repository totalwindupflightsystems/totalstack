"""MediaConvert store, data classes, and exception classes.

Greenfield service — no existing LocalStack provider. All stores and
exception classes are defined here and imported by integration tests.
"""

import time
import uuid
from collections import defaultdict
from typing import Any, Dict, List, Optional


# ── Exception Classes ───────────────────────────────────────────

class InvalidParameterException(Exception):
    """Bad request — invalid parameters."""
    def __init__(self, message="Invalid parameter"):
        super().__init__(message)
        self.code = "InvalidParameterException"


class ResourceNotFoundException(Exception):
    """Requested resource does not exist."""
    def __init__(self, message="Resource not found"):
        super().__init__(message)
        self.code = "ResourceNotFoundException"


class ConflictException(Exception):
    """Resource already exists or conflict with current state."""
    def __init__(self, message="Resource conflict"):
        super().__init__(message)
        self.code = "ConflictException"


class TooManyRequestsException(Exception):
    """Rate limit exceeded."""
    def __init__(self, message="Too many requests"):
        super().__init__(message)
        self.code = "TooManyRequestsException"


class InternalServerException(Exception):
    """Unexpected internal error."""
    def __init__(self, message="Internal server error"):
        super().__init__(message)
        self.code = "InternalServerException"


# ── Data Classes ───────────────────────────────────────────────

class JobRecord:
    """Represents a MediaConvert job."""
    def __init__(self, id: str, role: str, settings: Dict, **kwargs):
        self.id = id
        self.role = role
        self.settings = settings
        self.status = "SUBMITTED"
        self.created_at = time.time()
        self.queue = kwargs.get('Queue', 'Default')
        self.job_template = kwargs.get('JobTemplate', '')
        self.priority = kwargs.get('Priority', 0)
        self.tags = kwargs.get('Tags', {})
        self.user_metadata = kwargs.get('UserMetadata', {})
        self.acceleration_settings = kwargs.get('AccelerationSettings', None)
        self.status_update_interval = kwargs.get('StatusUpdateInterval', None)
        self.hop_destinations = kwargs.get('HopDestinations', None)
        self.output_group_details = None
        self.error_message = None
        self.error_code = None
        self.job_percent_complete = 0
        self.timing = None

    def to_dict(self) -> Dict:
        result = {
            'Id': self.id,
            'Arn': f'arn:aws:mediaconvert:us-east-1:000000000000:job/{self.id}',
            'Role': self.role,
            'Settings': self.settings,
            'Status': self.status,
            'CreatedAt': self.created_at,
            'Queue': self.queue,
            'JobTemplate': self.job_template,
            'Priority': self.priority,
            'JobPercentComplete': self.job_percent_complete,
        }
        if self.tags:
            result['Tags'] = self.tags
        return result


class JobTemplateRecord:
    """Represents a job template."""
    def __init__(self, name: str, settings: Dict, **kwargs):
        self.name = name
        self.settings = settings
        self.description = kwargs.get('Description', '')
        self.category = kwargs.get('Category', '')
        self.queue = kwargs.get('Queue', '')
        self.priority = kwargs.get('Priority', 0)
        self.tags = kwargs.get('Tags', {})
        self.created_at = time.time()
        self.last_updated = time.time()
        self.acceleration_settings = kwargs.get('AccelerationSettings', None)
        self.status_update_interval = kwargs.get('StatusUpdateInterval', None)

    def to_dict(self) -> Dict:
        return {
            'Name': self.name,
            'Settings': self.settings,
            'Description': self.description,
            'Category': self.category,
            'Queue': self.queue,
            'Priority': self.priority,
            'CreatedAt': self.created_at,
            'LastUpdated': self.last_updated,
            'Type': 'CUSTOM',
        }


class PresetRecord:
    """Represents an output preset."""
    def __init__(self, name: str, settings: Dict, **kwargs):
        self.name = name
        self.settings = settings
        self.description = kwargs.get('Description', '')
        self.category = kwargs.get('Category', '')
        self.tags = kwargs.get('Tags', {})
        self.created_at = time.time()
        self.last_updated = time.time()

    def to_dict(self) -> Dict:
        return {
            'Name': self.name,
            'Settings': self.settings,
            'Description': self.description,
            'Category': self.category,
            'CreatedAt': self.created_at,
            'LastUpdated': self.last_updated,
            'Type': 'CUSTOM',
        }


class QueueRecord:
    """Represents a transcoding queue."""
    def __init__(self, name: str, **kwargs):
        self.name = name
        self.description = kwargs.get('Description', '')
        self.status = kwargs.get('Status', 'ACTIVE')
        self.pricing_plan = kwargs.get('PricingPlan', 'ON_DEMAND')
        self.concurrent_jobs = kwargs.get('ConcurrentJobs', 3)
        self.tags = kwargs.get('Tags', {})
        self.created_at = time.time()
        self.last_updated = time.time()

    def to_dict(self) -> Dict:
        return {
            'Name': self.name,
            'Description': self.description,
            'Status': self.status,
            'PricingPlan': self.pricing_plan,
            'ConcurrentJobs': self.concurrent_jobs,
            'CreatedAt': self.created_at,
            'LastUpdated': self.last_updated,
        }


# ── Store ──────────────────────────────────────────────────────

class MediaConvertStore:
    """In-memory store for all MediaConvert resources."""

    def __init__(self):
        self.jobs: Dict[str, JobRecord] = {}
        self.job_templates: Dict[str, JobTemplateRecord] = {}
        self.presets: Dict[str, PresetRecord] = {}
        self.queues: Dict[str, QueueRecord] = {}
        self.tags: Dict[str, Dict[str, str]] = defaultdict(dict)


# ── Helpers ────────────────────────────────────────────────────

def _generate_arn(resource_type: str, resource_id: str) -> str:
    return f"arn:aws:mediaconvert:us-east-1:000000000000:{resource_type}/{resource_id}"


def _now() -> float:
    return time.time()
