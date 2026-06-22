
# spec:trace: specs/aws/dynamodb/enriched-aws-reference.json#TagResource
# spec:id: @specs/aws/dynamodb/tag-resource
# spec:implements: @kind:operation TagResource

from typing import Dict, Any, List
from localstack.services.dynamodb.models import DynamoDBStore


def tag_resource(
    store: DynamoDBStore,
    account_id: str,
    region_name: str,
    resource_arn: str,
    tags: List[Dict[str, str]],
) -> None:
    """
    Add tags to a DynamoDB resource (table or index).


    Each tag is a ``{"Key": str, "Value": str}`` pair. If a tag key
    already exists on the resource, its value is overwritten.

    Tags are stored in ``store.TABLE_TAGS`` keyed by resource ARN,
    mapping to ``{tag_key: tag_value}`` dicts.

    Returns an empty response (HTTP 200).
    """
    # Validate resource ARN
    if not resource_arn or not resource_arn.startswith("arn:"):
        raise ValidationException(
            f"Invalid ResourceArn: {resource_arn}"
        )

    # Validate tags list is non-empty
    if not tags:
        raise ValidationException(
            "1 validation error detected: "
            "Value '[]' at 'tags' failed to satisfy constraint: "
            "Member must have length greater than or equal to 1"
        )

    # Validate each tag
    for tag in tags:
        if "Key" not in tag:
            raise ValidationException(
                "Missing required parameter in Tags[].Key"
            )
        if "Value" not in tag:
            raise ValidationException(
                "Missing required parameter in Tags[].Value"
            )

        key = tag["Key"]
        if not key or len(key) > 128:
            raise ValidationException(
                "Tag key must be between 1 and 128 characters"
            )

        value = tag["Value"]
        if len(value) > 256:
            raise ValidationException(
                "Tag value must not exceed 256 characters"
            )

    # Upsert tags into store
    table_tags = store.TABLE_TAGS

    if resource_arn not in table_tags:
        table_tags[resource_arn] = {}

    for tag in tags:
        table_tags[resource_arn][tag["Key"]] = tag["Value"]


class ValidationException(Exception):
    """Input validation failed."""
    pass
