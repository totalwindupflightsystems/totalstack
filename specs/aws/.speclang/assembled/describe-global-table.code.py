
# spec:trace: specs/aws/dynamodb/dynamodb.spec.plan.md#operation-inventory-57-total
# spec:id: @specs/aws/dynamodb/describe-global-table
# spec:implements: @kind:operation DescribeGlobalTable

from typing import Dict, Any
from localstack.services.dynamodb.models import DynamoDBStore


def describe_global_table(
    store: DynamoDBStore,
    account_id: str,
    region_name: str,
    global_table_name: str,
) -> Dict[str, Any]:
    """
    Return metadata about a global table.


    Returns GlobalTableDescription with:
        - GlobalTableName
        - ReplicationGroup (list of replicas with RegionName, ReplicaStatus,
          ReplicaStatusDescription)
        - GlobalTableStatus: CREATING | ACTIVE | DELETING | UPDATING
    """
    details = store.GLOBAL_TABLES.get(global_table_name)
    if not details:
        raise GlobalTableNotFoundException(
            "Global table with this name does not exist"
        )

    return {"GlobalTableDescription": details}


class GlobalTableNotFoundException(Exception):
    """Global table with this name does not exist."""
    pass
