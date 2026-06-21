---
id: "@specs/aws/dynamodb/untag-resource"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/dynamodb/plan"
tags: [aws, dynamodb, untag-resource, tags]
short: "UntagResource operation — remove tags from a DynamoDB resource ARN"
---

# UntagResource

> **spec:trace:** specs/aws/dynamodb/enriched-aws-reference.json#UntagResource

Removes one or more tags from a DynamoDB resource (table or index) identified by its ARN. Only tag keys are required — values are not needed.

UntagResource is an **eventually consistent** operation. ListTagsOfResource may return the previous tag set for a few seconds after this call. Rate limit: 5 calls/sec/account.

**Required:** `ResourceArn`, `TagKeys`
**Input shape:** `UntagResourceInput`
**Output shape:** (empty — HTTP 200, no body)
**Errors:** `LimitExceededException`, `ResourceNotFoundException`, `InternalServerError`, `ResourceInUseException`

## Behavior

- Removing a tag key that does not exist is a silent **no-op** (no error)
- Tag keys must be 1–128 characters
- ResourceArn must be a valid DynamoDB ARN

## Implementation

```speclang
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

    @kind:operation UntagResource

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
```

