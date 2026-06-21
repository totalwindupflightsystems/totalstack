---
id: "@specs/aws/shield/docs/API_DescribeDRTAccess"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS DescribeDRTAccess"
status: active
depends_on:
  - "@specs/aws/shield/meta"
---

# DescribeDRTAccess

> **source:** AWS Documentation
> **spec:id:** @specs/aws/shield/docs/API_DescribeDRTAccess
> **target_lang:** meta — documentation tier. ALL sections preserved.



# DescribeDRTAccess
<a name="API_DescribeDRTAccess"></a>

Returns the current role and list of Amazon S3 log buckets used by the Shield Response Team (SRT) to access your AWS account while assisting with attack mitigation.

## Response Syntax
<a name="API_DescribeDRTAccess_ResponseSyntax"></a>

```
{
   "LogBucketList": [ "string" ],
   "RoleArn": "string"
}
```

## Response Elements
<a name="API_DescribeDRTAccess_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [LogBucketList](#API_DescribeDRTAccess_ResponseSyntax) **   <a name="AWSShield-DescribeDRTAccess-response-LogBucketList"></a>
The list of Amazon S3 buckets accessed by the SRT.  
Type: Array of strings  
Array Members: Minimum number of 0 items. Maximum number of 10 items.  
Length Constraints: Minimum length of 3. Maximum length of 63.  
Pattern: `^([a-z]|(\d(?!\d{0,2}\.\d{1,3}\.\d{1,3}\.\d{1,3})))([a-z\d]|(\.(?!(\.|-)))|(-(?!\.))){1,61}[a-z\d]$` 

 ** [RoleArn](#API_DescribeDRTAccess_ResponseSyntax) **   <a name="AWSShield-DescribeDRTAccess-response-RoleArn"></a>
The Amazon Resource Name (ARN) of the role the SRT used to access your AWS account.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 2048.  
Pattern: `^arn:aws:iam::\d{12}:role/?[a-zA-Z_0-9+=,.@\-_/]+` 

## Errors
<a name="API_DescribeDRTAccess_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalErrorException **   
Exception that indicates that a problem occurred with the service infrastructure. You can retry the request.  
HTTP Status Code: 500

 ** ResourceNotFoundException **   
Exception indicating the specified resource does not exist. If available, this exception includes details in additional properties.     
 ** resourceType **   
Type of resource.
HTTP Status Code: 400

## See Also
<a name="API_DescribeDRTAccess_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/shield-2016-06-02/DescribeDRTAccess) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/shield-2016-06-02/DescribeDRTAccess) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/shield-2016-06-02/DescribeDRTAccess) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/shield-2016-06-02/DescribeDRTAccess) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/shield-2016-06-02/DescribeDRTAccess) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/shield-2016-06-02/DescribeDRTAccess) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/shield-2016-06-02/DescribeDRTAccess) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/shield-2016-06-02/DescribeDRTAccess) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/shield-2016-06-02/DescribeDRTAccess) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/shield-2016-06-02/DescribeDRTAccess) 