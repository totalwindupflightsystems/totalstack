
# spec:trace: specs/aws/dynamodb/enriched-aws-reference.json#UntagResource
# spec:id: @specs/aws/dynamodb/untag-resource
# spec:implements: @kind:operation UntagResource

from typing import List
from localstack.services.dynamodb.models import DynamoDBStore


def untag_resource(
    store: DynamoDBStore,
    account_id: str,
    region_name: str,
    resource_arn: str,
    tag_keys: List[str],
) -> None:
    """
    Remove tags from a DynamoDB resource (table or index).


    ``tag_keys`` is a list of tag key strings to remove. If a key
    does not exist on the resource, it is silently ignored (no-op).

    Returns an empty response (HTTP 200).
    """
    # Validate resource ARN
    if not resource_arn or not resource_arn.startswith("arn:"):
        raise ValidationException(
            f"Invalid ResourceArn: {resource_arn}"
        )

    # Validate tag keys list is non-empty
    if not tag_keys:
        raise ValidationException(
            "1 validation error detected: "
            "Value '[]' at 'tagKeys' failed to satisfy constraint: "
            "Member must have length greater than or equal to 1"
        )

    # Validate each key
    for key in tag_keys:
        if not key or len(key) > 128:
            raise ValidationException(
                "Tag keys must be between 1 and 128 characters"
            )

    # Remove tags from store (no-op if ARN or key not found)
    table_tags = store.TABLE_TAGS
    resource_tags = table_tags.get(resource_arn, {})

    for tag_key in tag_keys:
        resource_tags.pop(tag_key, None)


class ValidationException(Exception):
    """Input validation failed."""
    pass
