"""
AthenaStore — shared store for Athena integration tests.
Greenfield pattern: dict-backed storage for all Athena resource types.
"""
from collections import defaultdict


class InvalidRequestException(Exception):
    """Invalid request — bad parameters."""
    pass


class ResourceNotFoundException(Exception):
    """Resource not found."""
    pass


class InternalServerException(Exception):
    """Internal server error."""
    pass


class AthenaStore:
    """Dict-backed store for all Athena resources."""

    def __init__(self):
        self.data_catalogs = {}
        self.work_groups = {}
        self.named_queries = {}
        self.prepared_statements = {}  # keyed by (workgroup, statement_name) tuple
        self.query_executions = {}
        self.databases = {}  # keyed by (catalog, db_name) tuple
        self.table_metadata = {}  # keyed by (catalog, db_name, table_name) tuple
        self.tags = {}  # keyed by resource ARN
