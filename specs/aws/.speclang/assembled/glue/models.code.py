"""
Glue service store for TotalStack — AWS Glue Data Catalog emulation.

Provides dict-backed storage for Databases, Tables, Jobs, Crawlers, and Triggers.
Method-style accessors match what generated handlers expect.
"""


class EntityNotFoundException(Exception):
    """Resource not found in the Glue Data Catalog."""
    pass


class AlreadyExistsException(Exception):
    """Resource already exists — cannot create duplicate."""
    pass


class InvalidInputException(Exception):
    """Invalid input parameter."""
    pass


class GlueStore:
    """In-memory store for Glue entities."""

    def __init__(self):
        self._databases: dict[str, dict] = {}       # (name, catalog_id) → record
        self._tables: dict[str, dict] = {}           # (db_name, table_name) → record
        self._jobs: dict[str, dict] = {}              # name → record
        self._crawlers: dict[str, dict] = {}          # name → record
        self._triggers: dict[str, dict] = {}          # name → record

    # ── Databases ─────────────────────────────────────────

    def databases(self, name: str, catalog_id: str = "default", record: dict = None):
        """Method accessor for generated handler code.
        - 2 args (name, catalog_id): get a database, returns record or None
        - 3 args (name, catalog_id, record): store a database
        """
        key = f"{catalog_id}/{name}"
        if record is not None:
            self._databases[key] = record
            return record
        return self._databases.get(key)

    def list_databases(self, catalog_id: str = "default"):
        """List all databases in a catalog."""
        prefix = f"{catalog_id}/"
        return [v for k, v in self._databases.items() if k.startswith(prefix)]

    def delete_database(self, name: str, catalog_id: str = "default"):
        """Delete a database from the catalog."""
        key = f"{catalog_id}/{name}"
        if key not in self._databases:
            raise EntityNotFoundException(f"Database '{name}' not found in catalog '{catalog_id}'")
        del self._databases[key]

    # ── Tables ────────────────────────────────────────────

    def tables(self, db_name: str = None, table_name: str = None, record: dict = None):
        """Method accessor for tables."""
        if db_name is not None and table_name is not None and record is not None:
            key = f"{db_name}/{table_name}"
            self._tables[key] = record
            return record
        if db_name is not None and table_name is not None:
            return self._tables.get(f"{db_name}/{table_name}")
        # List all tables (optionally filtered by db)
        if db_name is not None:
            prefix = f"{db_name}/"
            return [v for k, v in self._tables.items() if k.startswith(prefix)]
        return list(self._tables.values())

    # ── Jobs ──────────────────────────────────────────────

    def jobs(self, name: str = None, record: dict = None):
        """Method accessor for jobs."""
        if record is not None:
            self._jobs[name] = record
            return record
        if name is not None:
            return self._jobs.get(name)
        return list(self._jobs.values())

    def delete_job(self, name: str):
        """Delete a job."""
        if name not in self._jobs:
            raise EntityNotFoundException(f"Job '{name}' not found")
        del self._jobs[name]

    # ── Crawlers ──────────────────────────────────────────

    def crawlers(self, name: str = None, record: dict = None):
        """Method accessor for crawlers."""
        if record is not None:
            self._crawlers[name] = record
            return record
        if name is not None:
            return self._crawlers.get(name)
        return list(self._crawlers.values())

    def delete_crawler(self, name: str):
        """Delete a crawler."""
        if name not in self._crawlers:
            raise EntityNotFoundException(f"Crawler '{name}' not found")
        del self._crawlers[name]

    # ── Triggers ──────────────────────────────────────────

    def triggers(self, name: str = None, record: dict = None):
        """Method accessor for triggers."""
        if record is not None:
            self._triggers[name] = record
            return record
        if name is not None:
            return self._triggers.get(name)
        return list(self._triggers.values())

    def delete_trigger(self, name: str):
        """Delete a trigger."""
        if name not in self._triggers:
            raise EntityNotFoundException(f"Trigger '{name}' not found")
        del self._triggers[name]
