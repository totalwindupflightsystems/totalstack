// spec:trace spec=/home/kara/totalstack/specs/aws/dynamodb/update-global-table.spec.py.md#implementation
// spec:generated DO NOT EDIT — edit the spec instead

# spec:trace: specs/aws/dynamodb/dynamodb.spec.plan.md#operation-inventory-57-total
# spec:id: @specs/aws/dynamodb/update-global-table
# spec:implements: @kind:operation UpdateGlobalTable

from typing import Dict, Any, List, Optional
from localstack.services.dynamodb.models import DynamoDBStore


def update_global_table(
    store: DynamoDBStore,
    account_id: str,
    region_name: str,
    global_table_name: str,
    replica_updates: List[Dict[str, Optional[Dict[str, str]]]],
) -> Dict[str, Any]:
    """
    Add or remove replicas from a global table.


    replica_updates is a list of update actions, each containing
    either "Create" (add replica) or "Delete" (remove replica):
        [
            {"Create": {"RegionName": "us-west-2"}},
            {"Delete": {"RegionName": "eu-west-1"}},
        ]

    Although both Create and Delete can appear in a single request,
    for simplicity separate requests are recommended per AWS docs.

    Returns GlobalTableDescription with updated ReplicationGroup.
    """
    details = store.GLOBAL_TABLES.get(global_table_name)
    if not details:
        raise GlobalTableNotFoundException(
            "Global table with this name does not exist"
        )

    repl_group: List[Dict[str, str]] = details.get("ReplicationGroup", [])

    for update in replica_updates or []:
        _apply_replica_update(repl_group, update)

    details["ReplicationGroup"] = repl_group
    details["GlobalTableStatus"] = "UPDATING"

    return {"GlobalTableDescription": details}


def _apply_replica_update(
    repl_group: List[Dict[str, str]],
    update: Dict[str, Optional[Dict[str, str]]],
) -> None:
    """Apply a single replica update (Create or Delete)."""
    # Handle Delete: remove replica by RegionName
    delete = update.get("Delete")
    if delete:
        region_to_delete = delete.get("RegionName")
        existing = [
            g for g in repl_group
            if g.get("RegionName") == region_to_delete
        ]
        if not existing:
            raise ReplicaNotFoundException(
                f"Replica not found for region: {region_to_delete}"
            )
        repl_group[:] = [
            g for g in repl_group
            if g.get("RegionName") != region_to_delete
        ]
        return

    # Handle Create: add replica if not already present
    create = update.get("Create")
    if create:
        region_to_create = create.get("RegionName")
        already_exists = any(
            g.get("RegionName") == region_to_create
            for g in repl_group
        )
        if already_exists:
            raise ReplicaAlreadyExistsException(
                f"Replica already exists for region: {region_to_create}"
            )

        new_group: Dict[str, str] = {
            "RegionName": region_to_create,
            "ReplicaStatus": "ACTIVE",
            "ReplicaStatusDescription": "Replica active",
        }
        repl_group.append(new_group)


class GlobalTableNotFoundException(Exception):
    """Global table with this name does not exist."""
    pass


class ReplicaAlreadyExistsException(Exception):
    """Replica already exists in the specified region."""
    pass


class ReplicaNotFoundException(Exception):
    """Replica not found in the specified region."""
    pass