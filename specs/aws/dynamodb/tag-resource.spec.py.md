---
id: "@specs/aws/dynamodb/tag-resource"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/dynamodb/plan"
tags: [aws, dynamodb, tag-resource, tags]
short: "TagResource operation — add tags to a DynamoDB resource ARN"
---

# TagResource

> **spec:trace:** specs/aws/dynamodb/enriched-aws-reference.json#TagResource

Associates a set of tags with a DynamoDB resource (table or index). Tags are key-value pairs for cost allocation, access control, and resource organization.

TagResource is an **eventually consistent** operation. ListTagsOfResource may not reflect changes for a few seconds. Rate limit: 5 calls/sec/account.

**Required:** `ResourceArn`, `Tags`
**Input shape:** `TagResourceInput`
**Output shape:** (empty — HTTP 200, no body)
**Errors:** `LimitExceededException`, `ResourceNotFoundException`, `InternalServerError`, `ResourceInUseException`

## Constraints

- Tag keys: 1–128 characters, must be unique within the resource
- Tag values: 0–256 characters (can be empty string but not missing)
- Adding a tag with an existing key overwrites its value
- ResourceArn must be a valid DynamoDB ARN (table or index)

## Implementation

```speclang
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

    @kind:operation TagResource

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
```

