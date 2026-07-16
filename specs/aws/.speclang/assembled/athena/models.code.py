"""Athena Store — in-memory state for Athena emulation."""


class InvalidRequestException(Exception):
    """Raised when a required parameter is missing or invalid."""
    pass


class ResourceNotFoundException(Exception):
    """Raised when a requested resource does not exist."""
    pass


class AthenaStore:
    """In-memory store for Athena workgroups, query executions, and tags."""

    def __init__(self):
        self.work_groups: dict[str, dict] = {}
        self.query_executions: dict[str, dict] = {}
        self.tags: dict[str, dict[str, str]] = {}
