// spec:trace spec=/home/kara/totalstack/specs/aws/dynamodb/describe-contributor-insights.spec.py.md#output-fields
// spec:generated DO NOT EDIT — edit the spec instead

# spec:trace: specs/aws/dynamodb/enriched-aws-reference.json#DescribeContributorInsights
# spec:id: @specs/aws/dynamodb/describe-contributor-insights
# spec:implements: @kind:operation DescribeContributorInsights

from typing import Dict, Any, Optional
from localstack.services.dynamodb.models import DynamoDBStore


def describe_contributor_insights(
    store: DynamoDBStore,
    account_id: str,
    region_name: str,
    table_name: str,
    *,
    index_name: Optional[str] = None,
) -> Dict[str, Any]:
    """
    Return Contributor Insights status for a table or index.


    Contributor Insights is not implemented locally and always reports
    DISABLED status. Returns table and index name for correlation.

    Returns ``{"TableName": str, "ContributorInsightsStatus": "DISABLED", ...}``.
    """
    # Check if table exists
    if table_name not in store.table_definitions:
        raise TableNotFoundException(f"Table not found: {table_name}")

    # If index_name is provided, verify the index exists
    if index_name:
        table_def = store.table_definitions[table_name]
        index_found = _index_exists(table_def, index_name)
        if not index_found:
            raise IndexNotFoundException(
                f"Index not found: {index_name} on table {table_name}"
            )

    response: Dict[str, Any] = {
        "TableName": table_name,
        "ContributorInsightsStatus": "DISABLED",
        "ContributorInsightsRuleList": [],
        "LastUpdateDateTime": None,
        "ContributorInsightsMode": "ALL",
    }

    if index_name:
        response["IndexName"] = index_name

    return response


def _index_exists(
    table_def: Dict[str, Any],
    index_name: str,
) -> bool:
    """Check if a GSI or LSI exists in the table definition."""
    for gsi in table_def.get("GlobalSecondaryIndexes", []):
        if gsi.get("IndexName") == index_name:
            return True
    for lsi in table_def.get("LocalSecondaryIndexes", []):
        if lsi.get("IndexName") == index_name:
            return True
    return False


class TableNotFoundException(Exception):
    """Table not found."""
    pass


class IndexNotFoundException(Exception):
    """Index not found on table."""
    pass