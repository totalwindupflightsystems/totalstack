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
        self.data_catalogs: dict[str, dict] = {}
        self.named_queries: dict[str, dict] = {}
        self.prepared_statements: dict[str, dict] = {}

    # ── Convenience methods for validator test inputs ──

    def create_work_group(self, Name):
        wg = {'Name': Name, 'State': 'ENABLED', 'Description': '', 'Configuration': {}}
        self.work_groups[Name] = wg
        return {'WorkGroup': wg}

    def start_query_execution(self, QueryString, WorkGroup='primary'):
        import uuid
        exec_id = str(uuid.uuid4())
        self.query_executions[exec_id] = {
            'QueryExecutionId': exec_id, 'Query': QueryString,
            'WorkGroup': WorkGroup, 'Status': {'State': 'SUCCEEDED'}}
        return {'QueryExecutionId': exec_id}

    def create_data_catalog(self, Name, Type='GLUE'):
        self.data_catalogs[Name] = {'Name': Name, 'Type': Type}
        return {'DataCatalog': {'CatalogName': Name}}

    def create_named_query(self, Name, Database, QueryString):
        import uuid
        nq_id = str(uuid.uuid4())
        self.named_queries[nq_id] = {
            'NamedQueryId': nq_id, 'Name': Name,
            'Database': Database, 'QueryString': QueryString}
        return {'NamedQueryId': nq_id}

    def create_prepared_statement(self, StatementName, WorkGroup, QueryStatement):
        key = f"{WorkGroup}/{StatementName}"
        self.prepared_statements[key] = {
            'StatementName': StatementName, 'WorkGroup': WorkGroup,
            'QueryStatement': QueryStatement}
        return {}
