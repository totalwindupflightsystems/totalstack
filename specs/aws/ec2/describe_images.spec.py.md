---
id: "@specs/aws/ec2/describe_images"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_DescribeImages"
---

# DescribeImages

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/describe_images
> **spec:implements:** @kind:operation DescribeImages
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_DescribeImages.spec.md

Describes the specified images (AMIs, AKIs, and ARIs) available to you or all of the images available to you. The images available to you include public images, private images that you own, and private images owned by other Amazon Web Services accounts for which you have explicit launch permissions. Recently deregistered images appear in the returned results for a short interval and then return empty results. After all instances that reference a deregistered AMI are terminated, specifying the ID of the image will eventually return an error indicating that the AMI ID cannot be found. When Allowed AMIs is set to enabled , only allowed images are returned in the results, with the imageAllowed field set to true for each image. In audit-mode , the imageAllowed field is set to true for images that meet the account's Allowed AMIs criteria, and false for images that don't meet the criteria. For more information, see Allowed AMIs . The Amazon EC2 API follows an eventual consistency model. This means that the result of an API command you run that creates or modifies resources might not be immediately available to all subsequent commands you run. For guidance on how to manage eventual consistency, see Eventual consistency in the Amazon EC2 API in the Amazon EC2 Developer Guide . We strongly recommend using only paginated requests. Unpaginated requests are susceptible to throttling and timeouts. The order of the elements in the response, including those within nested structures, might vary. Applications should not assume the elements appear in a particular order.

## Input Shape: DescribeImagesRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| DryRun | bool |  | Checks whether you have the required permissions for the action, without actually making the request, and provides an er |
| ExecutableUsers | list[str] |  | Scopes the images by users with explicit launch permissions. Specify an Amazon Web Services account ID, self (the sender |
| Filters | list[Any  # complex shape] |  | The filters. architecture - The image architecture ( i386 | x86_64 | arm64 | x86_64_mac | arm64_mac ). block-device-mapp |
| ImageIds | list[Any  # complex shape] |  | The image IDs. Default: Describes all images available to you. |
| IncludeDeprecated | bool |  | Specifies whether to include deprecated AMIs. Default: No deprecated AMIs are included in the response. If you are the A |
| IncludeDisabled | bool |  | Specifies whether to include disabled AMIs. Default: No disabled AMIs are included in the response. |
| MaxResults | int |  | The maximum number of items to return for this request. To get the next page of items, make another request with the tok |
| NextToken | str |  | The token returned from a previous paginated request. Pagination continues from the end of the items returned by the pre |
| Owners | list[str] |  | Scopes the results to images with the specified owners. You can specify a combination of Amazon Web Services account IDs |

## Output Shape: DescribeImagesResult

- **Images** (list[Any  # complex shape]): Information about the images.
- **NextToken** (str): The token to include in another request to get the next page of items. This value is null when there are no more items t

## Implementation

```speclang
def describe_images(store, request: dict) -> dict:
    """Describes the specified images (AMIs, AKIs, and ARIs) available to you or all of the images available to you. The images available to you include public images, private images that you own, and privat"""

    # Auto-generated get handler — verify resource key
    return store.get_resource(request)
```
