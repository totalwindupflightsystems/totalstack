---
id: "@specs/aws/wafv2/docs/API_wafRegional_CreateWebACLMigrationStack"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS CreateWebACLMigrationStack"
status: active
depends_on:
  - "@specs/aws/wafv2/meta"
---

# CreateWebACLMigrationStack

> **source:** AWS Documentation
> **spec:id:** @specs/aws/wafv2/docs/API_wafRegional_CreateWebACLMigrationStack
> **target_lang:** meta — documentation tier. ALL sections preserved.



# CreateWebACLMigrationStack
<a name="API_wafRegional_CreateWebACLMigrationStack"></a>

Creates an AWS CloudFormation AWS WAFV2 template for the specified web ACL in the specified Amazon S3 bucket. Then, in CloudFormation, you create a stack from the template, to create the web ACL and its resources in AWS WAFV2. Use this to migrate your AWS WAF Classic web ACL to the latest version of AWS WAF.

**Note**  
 AWS WAF Classic support will end on September 30, 2025. 

This is part of a larger migration procedure for web ACLs from AWS WAF Classic to the latest version of AWS WAF. For the full procedure, including caveats and manual steps to complete the migration and switch over to the new web ACL, see [Migrating your AWS WAF Classic resources to AWS WAF](https://docs.aws.amazon.com/waf/latest/developerguide/waf-migrating-from-classic.html) in the [AWS WAF Developer Guide](https://docs.aws.amazon.com/waf/latest/developerguide/waf-chapter.html). 

## Request Syntax
<a name="API_wafRegional_CreateWebACLMigrationStack_RequestSyntax"></a>

```
{
   "IgnoreUnsupportedType": {{boolean}},
   "S3BucketName": "{{string}}",
   "WebACLId": "{{string}}"
}
```

## Request Parameters
<a name="API_wafRegional_CreateWebACLMigrationStack_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [IgnoreUnsupportedType](#API_wafRegional_CreateWebACLMigrationStack_RequestSyntax) **   <a name="WAF-wafRegional_CreateWebACLMigrationStack-request-IgnoreUnsupportedType"></a>
Indicates whether to exclude entities that can't be migrated or to stop the migration. Set this to true to ignore unsupported entities in the web ACL during the migration. Otherwise, if AWS WAF encounters unsupported entities, it stops the process and throws an exception.   
Type: Boolean  
Required: Yes

 ** [S3BucketName](#API_wafRegional_CreateWebACLMigrationStack_RequestSyntax) **   <a name="WAF-wafRegional_CreateWebACLMigrationStack-request-S3BucketName"></a>
The name of the Amazon S3 bucket to store the AWS CloudFormation template in. The S3 bucket must be configured as follows for the migration:   
+ If the bucket is encrypted, the encryption must use Amazon S3 (SSE-S3) keys. The migration doesn't support encryption with AWS Key Management Service (SSE-KMS) keys.
+ The bucket name must start with `aws-waf-migration-`. For example, `aws-waf-migration-my-web-acl`.
+ The bucket must be in the Region where you are deploying the template. For example, for a web ACL in `us-west-2`, you must use an Amazon S3 bucket in `us-west-2` and you must deploy the template stack to `us-west-2`. 
+ The bucket policies must permit the migration process to write data. For listings of the bucket policies, see the Examples section. 
Type: String  
Length Constraints: Minimum length of 3. Maximum length of 63.  
Pattern: `^aws-waf-migration-[0-9A-Za-z\.\-_]*`   
Required: Yes

 ** [WebACLId](#API_wafRegional_CreateWebACLMigrationStack_RequestSyntax) **   <a name="WAF-wafRegional_CreateWebACLMigrationStack-request-WebACLId"></a>
The UUID of the WAF Classic web ACL that you want to migrate to WAF v2.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 128.  
Pattern: `.*\S.*`   
Required: Yes

## Response Syntax
<a name="API_wafRegional_CreateWebACLMigrationStack_ResponseSyntax"></a>

```
{
   "S3ObjectUrl": "string"
}
```

## Response Elements
<a name="API_wafRegional_CreateWebACLMigrationStack_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [S3ObjectUrl](#API_wafRegional_CreateWebACLMigrationStack_ResponseSyntax) **   <a name="WAF-wafRegional_CreateWebACLMigrationStack-response-S3ObjectUrl"></a>
The URL of the template created in Amazon S3.   
Type: String  
Length Constraints: Minimum length of 1.

## Errors
<a name="API_wafRegional_CreateWebACLMigrationStack_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** WAFEntityMigrationException **   
The operation failed due to a problem with the migration. The failure cause is provided in the exception, in the `MigrationErrorType`:   
+  `ENTITY_NOT_SUPPORTED` - The web ACL has an unsupported entity but the `IgnoreUnsupportedType` is not set to true.
+  `ENTITY_NOT_FOUND` - The web ACL doesn't exist. 
+  `S3_BUCKET_NO_PERMISSION` - You don't have permission to perform the `PutObject` action to the specified Amazon S3 bucket.
+  `S3_BUCKET_NOT_ACCESSIBLE` - The bucket policy doesn't allow AWS WAF to perform the `PutObject` action in the bucket.
+  `S3_BUCKET_NOT_FOUND` - The S3 bucket doesn't exist. 
+  `S3_BUCKET_INVALID_REGION` - The S3 bucket is not in the same Region as the web ACL.
+  `S3_INTERNAL_ERROR` - AWS WAF failed to create the template in the S3 bucket for another reason.
In addition, the exception includes specific details about the failure in the `MigrationErrorReason`.   
HTTP Status Code: 400

 ** WAFInternalErrorException **   
The operation failed because of a system problem, even though the request was valid. Retry your request.  
HTTP Status Code: 500

 ** WAFInvalidOperationException **   
The operation failed because there was nothing to do. For example:  
+ You tried to remove a `Rule` from a `WebACL`, but the `Rule` isn't in the specified `WebACL`.
+ You tried to remove an IP address from an `IPSet`, but the IP address isn't in the specified `IPSet`.
+ You tried to remove a `ByteMatchTuple` from a `ByteMatchSet`, but the `ByteMatchTuple` isn't in the specified `WebACL`.
+ You tried to add a `Rule` to a `WebACL`, but the `Rule` already exists in the specified `WebACL`.
+ You tried to add a `ByteMatchTuple` to a `ByteMatchSet`, but the `ByteMatchTuple` already exists in the specified `WebACL`.
HTTP Status Code: 400

 ** WAFInvalidParameterException **   
The operation failed because AWS WAF didn't recognize a parameter in the request. For example:  
+ You specified an invalid parameter name.
+ You specified an invalid value.
+ You tried to update an object (`ByteMatchSet`, `IPSet`, `Rule`, or `WebACL`) using an action other than `INSERT` or `DELETE`.
+ You tried to create a `WebACL` with a `DefaultAction` `Type` other than `ALLOW`, `BLOCK`, or `COUNT`.
+ You tried to create a `RateBasedRule` with a `RateKey` value other than `IP`.
+ You tried to update a `WebACL` with a `WafAction` `Type` other than `ALLOW`, `BLOCK`, or `COUNT`.
+ You tried to update a `ByteMatchSet` with a `FieldToMatch` `Type` other than HEADER, METHOD, QUERY\_STRING, URI, or BODY.
+ You tried to update a `ByteMatchSet` with a `Field` of `HEADER` but no value for `Data`.
+ Your request references an ARN that is malformed, or corresponds to a resource with which a web ACL cannot be associated.
HTTP Status Code: 400

 ** WAFNonexistentItemException **   
The operation failed because the referenced object doesn't exist.  
HTTP Status Code: 400

## Examples
<a name="API_wafRegional_CreateWebACLMigrationStack_Examples"></a>

### Amazon S3 bucket policy for global Amazon CloudFront applications
<a name="API_wafRegional_CreateWebACLMigrationStack_Example_1"></a>

This example illustrates one usage of CreateWebACLMigrationStack.

```
{
    "Version": "2012-10-17",		 	 	 
    "Statement": [
        {
            "Effect": "Allow",
            "Principal": {
                "Service": "apiv2migration.waf.amazonaws.com"
            },
            "Action": "s3:PutObject",
            "Resource": "arn:aws:s3:::<BUCKET_NAME>/AWSWAF/<CUSTOMER_ACCOUNT_ID>/*"
        }
    ]
                }
```

### Amazon S3 bucket policy for Amazon API Gateway API or Application Load Balancer applications
<a name="API_wafRegional_CreateWebACLMigrationStack_Example_2"></a>

This example illustrates one usage of CreateWebACLMigrationStack.

```
{
    "Version": "2012-10-17",		 	 	 
    "Statement": [
        {
            "Effect": "Allow",
            "Principal": {
                "Service": "apiv2migration.waf-regional.amazonaws.com"
            },
            "Action": "s3:PutObject",
            "Resource": "arn:aws:s3:::<BUCKET_NAME>/AWSWAF/<CUSTOMER_ACCOUNT_ID>/*"
        }
    ]
}
```

## See Also
<a name="API_wafRegional_CreateWebACLMigrationStack_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/waf-regional-2016-11-28/CreateWebACLMigrationStack) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/waf-regional-2016-11-28/CreateWebACLMigrationStack) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/waf-regional-2016-11-28/CreateWebACLMigrationStack) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/waf-regional-2016-11-28/CreateWebACLMigrationStack) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/waf-regional-2016-11-28/CreateWebACLMigrationStack) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/waf-regional-2016-11-28/CreateWebACLMigrationStack) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/waf-regional-2016-11-28/CreateWebACLMigrationStack) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/waf-regional-2016-11-28/CreateWebACLMigrationStack) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/waf-regional-2016-11-28/CreateWebACLMigrationStack) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/waf-regional-2016-11-28/CreateWebACLMigrationStack) 