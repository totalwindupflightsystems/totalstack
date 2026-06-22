
# spec:trace: specs/aws/dynamodb/enriched-aws-reference.json#ListTagsOfResource
# spec:id: @specs/aws/dynamodb/list-tags-of-resource
# spec:implements: @kind:operation ListTagsOfResource

from typing import Dict, List, Any, Optional
from localstack.services.dynamodb.models import DynamoDBStore


def list_tags_of_resource(
    store: DynamoDBStore,
    account_id: str,
    region_name: str,
    resource_arn: str,
    *,
    next_token: Optional[str] = None,
) -> Dict[str, Any]:
    """
    List all tags associated with a DynamoDB resource.


    DynamoDB tags are stored per-resource-ARN in the TABLE_TAGS dictionary.
    Each tag is a {Key: str, Value: str} pair.

    Returns ``{"Tags": [...], "NextToken": str}`` if more pages exist,
    or ``{"Tags": [...]}`` when complete.
    """
    # TABLE_TAGS is keyed by resource ARN, each value is {tag_key: tag_value}
    resource_tags: Dict[str, str] = store.TABLE_TAGS.get(resource_arn, {})

    # Build tag list in AWS format
    tags: List[Dict[str, str]] = [
        {"Key": key, "Value": value}
        for key, value in resource_tags.items()
    ]

    response: Dict[str, Any] = {"Tags": tags}

    # Pagination — DynamoDB allows up to 50 tags per resource
    page_size = 50
    if next_token:
        try:
            start_idx = int(next_token)
        except ValueError:
            raise ValidationException(f"Invalid NextToken: {next_token}")
        tags = tags[start_idx:]

    if len(tags) > page_size:
        response["Tags"] = tags[:page_size]
        next_start = (int(next_token) if next_token else 0) + page_size
        response["NextToken"] = str(next_start)
    else:
        response["Tags"] = tags

    return response


class ValidationException(Exception):
    """Input validation failed."""
    pass
