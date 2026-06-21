---
id: "@specs/aws/shield/docs/API_AssociateDRTLogBucket"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS AssociateDRTLogBucket"
status: active
depends_on:
  - "@specs/aws/shield/meta"
---

# AssociateDRTLogBucket

> **source:** AWS Documentation
> **spec:id:** @specs/aws/shield/docs/API_AssociateDRTLogBucket
> **target_lang:** meta — documentation tier. ALL sections preserved.



# AssociateDRTLogBucket
<a name="API_AssociateDRTLogBucket"></a>

Authorizes the Shield Response Team (SRT) to access the specified Amazon S3 bucket containing log data such as Application Load Balancer access logs, CloudFront logs, or logs from third party sources. You can associate up to 10 Amazon S3 buckets with your subscription.

Use this to share information with the SRT that's not available in AWS WAF logs. 

To use the services of the SRT, you must be subscribed to the [Business Support plan](http://aws.amazon.com/premiumsupport/business-support/) or the [Enterprise Support plan](http://aws.amazon.com/premiumsupport/enterprise-support/). 

## Request Syntax
<a name="API_AssociateDRTLogBucket_RequestSyntax"></a>

```
{
   "LogBucket": "{{string}}"
}
```

## Request Parameters
<a name="API_AssociateDRTLogBucket_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [LogBucket](#API_AssociateDRTLogBucket_RequestSyntax) **   <a name="AWSShield-AssociateDRTLogBucket-request-LogBucket"></a>
The Amazon S3 bucket that contains the logs that you want to share.  
Type: String  
Length Constraints: Minimum length of 3. Maximum length of 63.  
Pattern: `^([a-z]|(\d(?!\d{0,2}\.\d{1,3}\.\d{1,3}\.\d{1,3})))([a-z\d]|(\.(?!(\.|-)))|(-(?!\.))){1,61}[a-z\d]$`   
Required: Yes

## Response Elements
<a name="API_AssociateDRTLogBucket_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_AssociateDRTLogBucket_Errors"></a>

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

 ** InvalidParameterException **   
Exception that indicates that the parameters passed to the API are invalid. If available, this exception includes details in additional properties.     
 ** fields **   
Fields that caused the exception.  
 ** reason **   
Additional information about the exception.
HTTP Status Code: 400

 ** LimitsExceededException **   
Exception that indicates that the operation would exceed a limit.    
 ** Limit **   
The threshold that would be exceeded.  
 ** Type **   
The type of limit that would be exceeded.
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
<a name="API_AssociateDRTLogBucket_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/shield-2016-06-02/AssociateDRTLogBucket) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/shield-2016-06-02/AssociateDRTLogBucket) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/shield-2016-06-02/AssociateDRTLogBucket) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/shield-2016-06-02/AssociateDRTLogBucket) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/shield-2016-06-02/AssociateDRTLogBucket) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/shield-2016-06-02/AssociateDRTLogBucket) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/shield-2016-06-02/AssociateDRTLogBucket) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/shield-2016-06-02/AssociateDRTLogBucket) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/shield-2016-06-02/AssociateDRTLogBucket) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/shield-2016-06-02/AssociateDRTLogBucket) 