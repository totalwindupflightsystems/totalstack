---
id: "@specs/aws/lambda/docs/tags-esm"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Event source mapping tags"
status: active
depends_on:
  - "@specs/aws/lambda/meta"
---

# Event source mapping tags

> **source:** AWS Documentation
> **spec:id:** @specs/aws/lambda/docs/tags-esm
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Using tags on event source mappings
<a name="tags-esm"></a>

You can tag event source mappings to organize and manage your resources. Tags are free-form key-value pairs associated with your resources that are supported across AWS services. For more information about use cases for tags, see [Common tagging strategies](https://docs.aws.amazon.com//tag-editor/latest/userguide/best-practices-and-strats.html#tag-strategies) in the *Tagging AWS Resources and Tag Editor Guide*. 

Event source mappings are associated with functions, which can have their own tags. Event source mappings do not automatically inherit tags from functions. You can use the AWS Lambda API to view and update tags. You can also view and update tags while managing a specific event source mapping in the Lambda console, including those using Provisioned Mode for Amazon SQS.

## Permissions required for working with tags
<a name="esm-tags-required-permissions"></a>

To allow an AWS Identity and Access Management (IAM) identity (user, group, or role) to read or set tags on a resource, grant it the corresponding permissions:
+ **lambda:ListTags**–When a resource has tags, grant this permission to anyone who needs to call `ListTags` on it. For tagged functions, this permission is also necessary for `GetFunction`.
+ **lambda:TagResource**–Grant this permission to anyone who needs to call `TagResource` or perform a tag on create.

Optionally, consider granting the **lambda:UntagResource** permission as well to allow `UntagResource` calls to the resource.

For more information, see [Identity-based IAM policies for Lambda](access-control-identity-based.md).

## Using tags with the Lambda console
<a name="tags-esm-console"></a>

You can use the Lambda console to create event source mappings that have tags, add tags to existing event source mappings, and filter event source mappings by tag, including those configured in Provisioned Mode for Amazon SQS.

When you add a trigger for supported stream and queue-based services using the Lambda console, Lambda automatically creates an event source mapping. For more information about these event sources, see [How Lambda processes records from stream and queue-based event sources](invocation-eventsourcemapping.md). To create an event source mapping in the console, you will need the following prerequisites:
+ A function.
+ An event source from an affected service.

You can add the tags as part of the same user interface you use to create or update triggers.

**To add a tag when you create a event source mapping**

1. Open the [Functions page](https://console.aws.amazon.com/lambda/home#/functions) of the Lambda console.

1. Choose the name of your function.

1. Under **Function overview**, choose **Add trigger**.

1. Under **Trigger configuration**, in the dropdown list, choose the name of the service your event source comes from.

1. Provide the core configuration for your event source. For more information about configuring your event source, consult the section for the related service in [Invoking Lambda with events from other AWS services](lambda-services.md).

1. Under **Event source mapping configuration**, choose **Additional settings**.

1. Under **Tags**, choose **Add new tag**

1. In the **Key** field, enter your tag key. For information about tagging restrictions, see [Tag naming limits and requirements](https://docs.aws.amazon.com//tag-editor/latest/userguide/best-practices-and-strats.html#id_tags_naming_best_practices) in the *Tagging AWS Resources and Tag Editor Guide*.

1. Choose **Add**.

**To add tags to an existing event source mapping**

1. Open [Event source mappings](https://console.aws.amazon.com/lambda/home#/event-source-mappings) in the Lambda console.

1. From the resource list, choose the **UUID** for the event source mapping corresponding to your **Function** and **Event source ARN**.

1. From the tab list below the **General configuration pane**, choose **Tags**.

1. Choose **Manage tags**.

1. Choose **Add new tag**.

1. In the **Key** field, enter your tag key. For information about tagging restrictions, see [Tag naming limits and requirements](https://docs.aws.amazon.com//tag-editor/latest/userguide/best-practices-and-strats.html#id_tags_naming_best_practices) in the *Tagging AWS Resources and Tag Editor Guide*.

1. Choose **Save**.

**To filter event source mappings by tag**

1. Open [Event source mappings](https://console.aws.amazon.com/lambda/home#/event-source-mappings) in the Lambda console.

1. Choose the search box.

1. From the dropdown list, select your tag key from below the **Tags** subheading.

1. Select **Use: "tag-name"** to see all event source mappings tagged with this key, or choose an **Operator** to further filter by value.

1. Select your tag value to filter by a combination of tag key and value.

The search box also supports searching for tag keys. Enter the name of a key to find it in the list.

## Using tags with the AWS CLI
<a name="tags-esm-cli"></a>

You can add and remove tags on existing Lambda resources, including event source mappings, with the Lambda API. You can also add tags when creating an event source mapping, which allows you to keep a resource tagged through its entire lifecycle.

### Updating tags with the Lambda tag APIs
<a name="tags-esm-api-config"></a>

You can add and remove tags for supported Lambda resources through the [TagResource](https://docs.aws.amazon.com/lambda/latest/api/API_TagResource.html) and [UntagResource](https://docs.aws.amazon.com/lambda/latest/api/API_UntagResource.html) API operations.

You can call these operations using the AWS CLI. To add tags to an existing resource, use the `tag-resource` command. This example adds two tags, one with the key {{Department}} and one with the key {{CostCenter}}.

```
aws lambda tag-resource \
--resource arn:aws:lambda:{{us-east-2:123456789012:resource-type:my-resource}} \
--tags {{Department}}={{Marketing}},{{CostCenter}}={{1234ABCD}}
```

To remove tags, use the `untag-resource` command. This example removes the tag with the key {{Department}}.

```
aws lambda untag-resource --resource {{arn:aws:lambda:us-east-1:123456789012:resource-type:resource-identifier}} \
--tag-keys {{Department}}
```

### Adding tags when you create an event source mapping
<a name="tags-esm-on-create"></a>

To create a new Lambda event source mapping with tags, use the [CreateEventSourceMapping](https://docs.aws.amazon.com/lambda/latest/api/API_CreateEventSourceMapping.html) API operation. Specify the `Tags` parameter. You can call this operation with the `create-event-source-mapping` AWS CLI command and the `--tags` option. For more information about the CLI command, see [create-event-source-mapping](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lambda/create-event-source-mapping.html) in the *AWS CLI Command Reference*.

Before using the `Tags` parameter with `CreateEventSourceMapping`, ensure that your role has permission to tag resources alongside the usual permissions needed for this operation. For more information about permissions for tagging, see [Permissions required for working with tags](#esm-tags-required-permissions).

### Viewing tags with the Lambda tag APIs
<a name="tags-esm-api-view"></a>

To view the tags that are applied to a specific Lambda resource, use the `ListTags` API operation. For more information, see [ListTags](https://docs.aws.amazon.com/lambda/latest/api/API_ListTags.html).

You can call this operation with the `list-tags` AWS CLI command by providing an ARN (Amazon Resource Name).

```
aws lambda list-tags --resource {{arn:aws:lambda:us-east-1:123456789012:resource-type:resource-identifier}}
```

### Filtering resources by tag
<a name="tags-esm-filtering"></a>

You can use the AWS Resource Groups Tagging API [GetResources](https://docs.aws.amazon.com/resourcegroupstagging/latest/APIReference/API_GetResources.html) API operation to filter your resources by tags. The `GetResources` operation receives up to 10 filters, with each filter containing a tag key and up to 10 tag values. You provide `GetResources` with a `ResourceType` to filter by specific resource types.

You can call this operation using the `get-resources` AWS CLI command. For examples of using `get-resources`, see [get-resources](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/resourcegroupstaggingapi/get-resources.html#examples) in the *AWS CLI Command Reference*. 