---
id: "@specs/aws/batch/docs/API_Secret"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Secret"
status: active
depends_on:
  - "@specs/aws/batch/meta"
---

# Secret

> **source:** AWS Documentation
> **spec:id:** @specs/aws/batch/docs/API_Secret
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Secret
<a name="API_Secret"></a>

An object that represents the secret to expose to your container. Secrets can be exposed to a container in the following ways:
+ To inject sensitive data into your containers as environment variables, use the `secrets` container definition parameter.
+ To reference sensitive information in the log configuration of a container, use the `secretOptions` container definition parameter.

For more information, see [Specifying sensitive data](https://docs.aws.amazon.com/batch/latest/userguide/specifying-sensitive-data.html) in the * AWS Batch User Guide*.

## Contents
<a name="API_Secret_Contents"></a>

 ** name **   <a name="Batch-Type-Secret-name"></a>
The name of the secret.  
Type: String  
Required: Yes

 ** valueFrom **   <a name="Batch-Type-Secret-valueFrom"></a>
The secret to expose to the container. The supported values are either the full Amazon Resource Name (ARN) of the AWS Secrets Manager secret or the full ARN of the parameter in the AWS Systems Manager Parameter Store.  
If the AWS Systems Manager Parameter Store parameter exists in the same Region as the job you're launching, then you can use either the full Amazon Resource Name (ARN) or name of the parameter. If the parameter exists in a different Region, then the full ARN must be specified.
Type: String  
Required: Yes

## See Also
<a name="API_Secret_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/batch-2016-08-10/Secret) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/batch-2016-08-10/Secret) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/batch-2016-08-10/Secret) 