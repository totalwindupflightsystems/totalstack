---
id: "@specs/aws/lambda/docs/using-aliases"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Using aliases"
status: active
depends_on:
  - "@specs/aws/lambda/meta"
---

# Using aliases

> **source:** AWS Documentation
> **spec:id:** @specs/aws/lambda/docs/using-aliases
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Using Lambda aliases in event sources and permissions policies
<a name="using-aliases"></a>

Each alias has a unique ARN. An alias can point only to a function version, not to another alias. You can update an alias to point to a new version of the function.

Event sources such as Amazon Simple Storage Service (Amazon S3) invoke your Lambda function. These event sources maintain a mapping that identifies the function to invoke when events occur. If you specify a Lambda function alias in the mapping configuration, you don't need to update the mapping when the function version changes. For more information, see [How Lambda processes records from stream and queue-based event sources](invocation-eventsourcemapping.md).

In a resource policy, you can grant permissions for event sources to use your Lambda function. If you specify an alias ARN in the policy, you don't need to update the policy when the function version changes.

## Resource policies
<a name="versioning-permissions-alias"></a>

You can use a [resource-based policy](access-control-resource-based.md) to give a service, resource, or account access to your function. The scope of that permission depends on whether you apply it to an alias, a version, or the entire function. For example, if you use an alias name (such as `helloworld:PROD`), the permission allows you to invoke the `helloworld` function using the alias ARN (`helloworld:PROD`).

If you attempt to invoke the function without an alias or a specific version, then you get a permission error. This permission error still occurs even if you attempt to directly invoke the function version associated with the alias.

For example, the following AWS CLI command grants Amazon S3 permissions to invoke the PROD alias of the `helloworld` function when Amazon S3 is acting on behalf of `amzn-s3-demo-bucket`.

```
aws lambda add-permission \
  --function-name helloworld \
  --qualifier PROD \
  --statement-id 1 \
  --principal s3.amazonaws.com \
  --action lambda:InvokeFunction \
  --source-arn arn:aws:s3:::amzn-s3-demo-bucket \
  --source-account 123456789012
```

For more information about using resource names in policies, see [Fine-tuning the Resources and Conditions sections of policies](lambda-api-permissions-ref.md).