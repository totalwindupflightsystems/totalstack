---
id: "@specs/aws/lambda/docs/configuration-tags"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Tags"
status: active
depends_on:
  - "@specs/aws/lambda/meta"
---

# Tags

> **source:** AWS Documentation
> **spec:id:** @specs/aws/lambda/docs/configuration-tags
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Using tags on Lambda functions
<a name="configuration-tags"></a>

You can tag functions to organize and manage your resources. Tags are free-form key-value pairs associated with your resources that are supported across AWS services. For more information about use cases for tags, see [Common tagging strategies](https://docs.aws.amazon.com//tag-editor/latest/userguide/best-practices-and-strats.html#tag-strategies) in the *Tagging AWS Resources and Tag Editor Guide*. 

Tags apply at the function level, not to versions or aliases. Tags are not part of the version-specific configuration that AWS Lambda creates a snapshot of when you publish a version. You can use the Lambda API to view and update tags. You can also view and update tags while managing a specific function in the Lambda console.

**Topics**
+ [Permissions required for working with tags](#fxn-tags-required-permissions)
+ [Using tags with the Lambda console](#using-tags-with-the-console)
+ [Using tags with the AWS CLI](#configuration-tags-cli)

## Permissions required for working with tags
<a name="fxn-tags-required-permissions"></a>

To allow an AWS Identity and Access Management (IAM) identity (user, group, or role) to read or set tags on a resource, grant it the corresponding permissions:
+ **lambda:ListTags**–When a resource has tags, grant this permission to anyone who needs to call `ListTags` on it. For tagged functions, this permission is also necessary for `GetFunction`.
+ **lambda:TagResource**–Grant this permission to anyone who needs to call `TagResource` or perform a tag on create.

Optionally, consider granting the **lambda:UntagResource** permission as well to allow `UntagResource` calls to the resource.

For more information, see [Identity-based IAM policies for Lambda](access-control-identity-based.md).

## Using tags with the Lambda console
<a name="using-tags-with-the-console"></a>

You can use the Lambda console to create functions that have tags, add tags to existing functions, and filter functions by tags that you add.

**To add tags when you create a function**

1. Open the [Functions page](https://console.aws.amazon.com/lambda/home#/functions) of the Lambda console.

1. Choose **Create function**.

1. Choose **Author from scratch** or **Container image**. 

1. Under **Basic information**, set up your function. For more information about configuring functions, see [Configuring AWS Lambda functions](lambda-functions.md). 

1. Expand **Advanced settings**, and then select **Enable tags**.

1. Choose **Add new tag**, and then enter a **Key** and an optional **Value**. To add more tags, repeat this step.

1. Choose **Create function**.

**To add tags to an existing function**

1. Open the [Functions page](https://console.aws.amazon.com/lambda/home#/functions) of the Lambda console.

1. Choose the name of a function.

1. Choose **Configuration**, and then choose **Tags**.

1. Under **Tags**, choose **Manage tags**.

1. Choose **Add new tag**, and then enter a **Key** and an optional **Value**. To add more tags, repeat this step.

1. Choose **Save**.

**To filter functions with tags**

1. Open the [Functions page](https://console.aws.amazon.com/lambda/home#/functions) of the Lambda console.

1. Choose the search box to see a list of function properties and tag keys.

1. Choose a tag key to see a list of values that are in use in the current AWS Region.

1. Select **Use: "tag-name"** to see all functions tagged with this key, or choose an **Operator** to further filter by value.

1. Select your tag value to filter by a combination of tag key and value.

The search bar also supports searching for tag keys. Enter `tag` to see only a list of tag keys, or enter the name of a key to find it in the list.

## Using tags with the AWS CLI
<a name="configuration-tags-cli"></a>

You can add and remove tags on existing Lambda resources, including functions, with the Lambda API. You can also add tags when creating a function, which allows you to keep a resource tagged through its entire lifecycle.

### Updating tags with the Lambda tag APIs
<a name="tags-fxn-api-config"></a>

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

### Adding tags when creating a function
<a name="creating-tags-when-you-create-a-function-cli"></a>

To create a new Lambda function with tags, use the [CreateFunction](https://docs.aws.amazon.com//lambda/latest/api/API_CreateFunction.html) API operation. Specify the `Tags` parameter. You can call this operation with the `create-function` CLI command and the --tags option. Before using the tags parameter with `CreateFunction`, ensure that your role has permission to tag resources alongside the usual permissions needed for this operation. For more information about permissions for tagging, see [Permissions required for working with tags](#fxn-tags-required-permissions). This example adds two tags, one with the key {{Department}} and one with the key {{CostCenter}}.

```
aws lambda create-function --function-name {{my-function}}
--handler index.js --runtime nodejs24.x \
--role arn:aws:iam::{{123456789012}}:role/{{lambda-role}} \
--tags Department=Marketing,CostCenter=1234ABCD
```

### Viewing tags on a function
<a name="viewing-tags-on-a-function-cli"></a>

To view the tags that are applied to a specific Lambda resource, use the `ListTags` API operation. For more information, see [ListTags](https://docs.aws.amazon.com/lambda/latest/api/API_ListTags.html).

You can call this operation with the `list-tags` AWS CLI command by providing an ARN (Amazon Resource Name).

```
aws lambda list-tags --resource {{arn:aws:lambda:us-east-1:123456789012:resource-type:resource-identifier}}
```

You can view the tags that are applied to a specific resource with the [GetFunction](https://docs.aws.amazon.com/lambda/latest/api/API_GetFunction.html) API operation. Comparable functionality is not available for other resource types.

You can call this operation with the `get-function` CLI command:

```
aws lambda get-function --function-name {{my-function}}
```

### Filtering resources by tag
<a name="tags-fxn-filtering"></a>

You can use the AWS Resource Groups Tagging API [GetResources](https://docs.aws.amazon.com/resourcegroupstagging/latest/APIReference/API_GetResources.html) API operation to filter your resources by tags. The `GetResources` operation receives up to 10 filters, with each filter containing a tag key and up to 10 tag values. You provide `GetResources` with a `ResourceType` to filter by specific resource types.

You can call this operation using the `get-resources` AWS CLI command. For examples of using `get-resources`, see [get-resources](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/resourcegroupstaggingapi/get-resources.html#examples) in the *AWS CLI Command Reference*. 