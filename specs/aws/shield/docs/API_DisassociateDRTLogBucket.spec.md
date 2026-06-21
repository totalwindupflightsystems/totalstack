---
id: "@specs/aws/shield/docs/API_DisassociateDRTLogBucket"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS DisassociateDRTLogBucket"
status: active
depends_on:
  - "@specs/aws/shield/meta"
---

# DisassociateDRTLogBucket

> **source:** AWS Documentation
> **spec:id:** @specs/aws/shield/docs/API_DisassociateDRTLogBucket
> **target_lang:** meta — documentation tier. ALL sections preserved.



# DisassociateDRTLogBucket
<a name="API_DisassociateDRTLogBucket"></a>

Removes the Shield Response Team's (SRT) access to the specified Amazon S3 bucket containing the logs that you shared previously.

## Request Syntax
<a name="API_DisassociateDRTLogBucket_RequestSyntax"></a>

```
{
   "LogBucket": "{{string}}"
}
```

## Request Parameters
<a name="API_DisassociateDRTLogBucket_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [LogBucket](#API_DisassociateDRTLogBucket_RequestSyntax) **   <a name="AWSShield-DisassociateDRTLogBucket-request-LogBucket"></a>
The Amazon S3 bucket that contains the logs that you want to share.  
Type: String  
Length Constraints: Minimum length of 3. Maximum length of 63.  
Pattern: `^([a-z]|(\d(?!\d{0,2}\.\d{1,3}\.\d{1,3}\.\d{1,3})))([a-z\d]|(\.(?!(\.|-)))|(-(?!\.))){1,61}[a-z\d]$`   
Required: Yes

## Response Elements
<a name="API_DisassociateDRTLogBucket_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_DisassociateDRTLogBucket_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedForDependencyException **   
In order to grant the necessary access to the Shield Response Team (SRT) the user submitting the request must have the `iam:PassRole` permission. This error indicates the user did not have the appropriate permissions. For more information, see [Granting a User Permissions to Pass a Role to an AWS Service](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html).   
HTTP Status Code: 400

 ** InternalErrorException **   
Exception that indicates that a problem occurred with the service infrastructure. You can retry the request.  
HTTP Status Code: 500

 ** InvalidOperationException **   
Exception that indicates that the operation would not cause any change to occur.  
HTTP Status Code: 400

 ** NoAssociatedRoleException **   
The ARN of the role that you specified does not exist.  
HTTP Status Code: 400

 ** OptimisticLockException **   
Exception that indicates that the resource state has been modified by another client. Retrieve the resource and then retry your request.  
HTTP Status Code: 400

 ** ResourceNotFoundException **   
Exception indicating the specified resource does not exist. If available, this exception includes details in additional properties.     
 ** resourceType **   
Type of resource.
HTTP Status Code: 400

## See Also
<a name="API_DisassociateDRTLogBucket_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/shield-2016-06-02/DisassociateDRTLogBucket) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/shield-2016-06-02/DisassociateDRTLogBucket) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/shield-2016-06-02/DisassociateDRTLogBucket) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/shield-2016-06-02/DisassociateDRTLogBucket) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/shield-2016-06-02/DisassociateDRTLogBucket) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/shield-2016-06-02/DisassociateDRTLogBucket) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/shield-2016-06-02/DisassociateDRTLogBucket) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/shield-2016-06-02/DisassociateDRTLogBucket) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/shield-2016-06-02/DisassociateDRTLogBucket) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/shield-2016-06-02/DisassociateDRTLogBucket) 