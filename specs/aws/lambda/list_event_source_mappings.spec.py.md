---
id: "@specs/aws/lambda/list_event_source_mappings"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/lambda/plan"
  - "@specs/aws/lambda/docs/API_ListEventSourceMappings"
---

# ListEventSourceMappings

> **spec:trace:** specs/aws/lambda/lambda.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/lambda/list_event_source_mappings
> **spec:implements:** @kind:operation ListEventSourceMappings
> **AWS Protocol:** rest-json
> **HTTP:** GET /2015-03-31/event-source-mappings
> **@ref:** specs/aws/lambda/docs/API_ListEventSourceMappings.spec.md

Lists event source mappings. Specify an EventSourceArn to show only event source mappings for a single event source.

## Input Shape: ListEventSourceMappingsRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| EventSourceArn | Any  # complex shape |  | The Amazon Resource Name (ARN) of the event source. Amazon Kinesis – The ARN of the data stream or a stream consumer. Am |
| FunctionName | Any  # complex shape |  | The name or ARN of the Lambda function. Name formats Function name – MyFunction . Function ARN – arn:aws:lambda:us-west- |
| Marker | str |  | A pagination token returned by a previous call. |
| MaxItems | Any  # complex shape |  | The maximum number of event source mappings to return. Note that ListEventSourceMappings returns a maximum of 100 items  |

## Output Shape: ListEventSourceMappingsResponse

- **EventSourceMappings** (list[Any  # complex shape]): A list of event source mappings.
- **NextMarker** (str): A pagination token that's returned when the response doesn't contain all event source mappings.

## Errors
- **InvalidParameterValueException**: One of the parameters in the request is not valid.
- **ServiceException**: The Lambda service encountered an internal error.
- **TooManyRequestsException**: The request throughput limit was exceeded. For more information, see Lambda quotas .
- **ResourceNotFoundException**: The resource specified in the request does not exist.

## Implementation

```speclang
def list_event_source_mappings(store, request: dict) -> dict:
    """Lists event source mappings. Specify an EventSourceArn to show only event source mappings for a single event source."""

    items = store.list_event_source_mappingss()
    return {"EventSourceMappings": list(items.values())}
```
