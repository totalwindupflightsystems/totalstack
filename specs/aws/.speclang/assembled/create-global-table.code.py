
# spec:trace: specs/aws/dynamodb/dynamodb.spec.plan.md#operation-inventory-57-total
# spec:id: @specs/aws/dynamodb/create-global-table
# spec:implements: @kind:operation CreateGlobalTable

from typing import Dict, Any, List
from localstack.services.dynamodb.models import DynamoDBStore


def create_global_table(
    store: DynamoDBStore,
    account_id: str,
    region_name: str,
    global_table_name: str,
    replication_group: List[Dict[str, str]],
) -> Dict[str, Any]:
    """
    Create a new global table spanning multiple regions.


    ReplicationGroup is a list of replicas, each with:
        {
            "RegionName": "us-east-1"
        }

    Output returns GlobalTableDescription containing:
        - GlobalTableName
        - ReplicationGroup (list of replicas with ReplicaStatus, RegionName,
          ReplicaStatusDescription)
        - GlobalTableStatus: CREATING | ACTIVE | DELETING | UPDATING
    """
    # Validate global table name
    if not global_table_name or not global_table_name.strip():
        raise ValueError("GlobalTableName must not be empty")

    # Check if global table already exists
    if global_table_name in store.GLOBAL_TABLES:
        raise GlobalTableAlreadyExistsException(
            "Global table with this name already exists"
        )

    # Deep-copy replication group to avoid mutating caller data
    replication_group = [grp.copy() for grp in (replication_group or [])]

    # Build global table description
    data: Dict[str, Any] = {
        "GlobalTableName": global_table_name,
        "ReplicationGroup": replication_group,
        "GlobalTableStatus": "CREATING",
    }

    # Mark each replica as ACTIVE with region info
    for group in replication_group:
        group.setdefault("ReplicaStatus", "ACTIVE")
        group.setdefault(
            "ReplicaStatusDescription", "Replica active"
        )

    # Persist
    store.GLOBAL_TABLES[global_table_name] = data

    return {"GlobalTableDescription": data}


class GlobalTableAlreadyExistsException(Exception):
    """Global table with this name already exists."""
    pass
