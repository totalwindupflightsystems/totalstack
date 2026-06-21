---
id: "@specs/aws/shield/docs/API_DescribeProtection"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS DescribeProtection"
status: active
depends_on:
  - "@specs/aws/shield/meta"
---

# DescribeProtection

> **source:** AWS Documentation
> **spec:id:** @specs/aws/shield/docs/API_DescribeProtection
> **target_lang:** meta — documentation tier. ALL sections preserved.



# DescribeProtection
<a name="API_DescribeProtection"></a>

Lists the details of a [Protection](API_Protection.md) object.

## Request Syntax
<a name="API_DescribeProtection_RequestSyntax"></a>

```
{
   "ProtectionId": "{{string}}",
   "ResourceArn": "{{string}}"
}
```

## Request Parameters
<a name="API_DescribeProtection_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [ProtectionId](#API_DescribeProtection_RequestSyntax) **   <a name="AWSShield-DescribeProtection-request-ProtectionId"></a>
The unique identifier (ID) for the [Protection](API_Protection.md) object to describe. You must provide either the `ResourceArn` of the protected resource or the `ProtectionID` of the protection, but not both.  
Type: String  
Length Constraints: Fixed length of 36.  
Pattern: `[a-zA-Z0-9\\-]*`   
Required: No

 ** [ResourceArn](#API_DescribeProtection_RequestSyntax) **   <a name="AWSShield-DescribeProtection-request-ResourceArn"></a>
The ARN (Amazon Resource Name) of the protected AWS resource. You must provide either the `ResourceArn` of the protected resource or the `ProtectionID` of the protection, but not both.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 2048.  
Pattern: `^arn:aws.*`   
Required: No

## Response Syntax
<a name="API_DescribeProtection_ResponseSyntax"></a>

```
{
   "Protection": { 
      "ApplicationLayerAutomaticResponseConfiguration": { 
         "Action": { 
            "Block": { 
            },
            "Count": { 
            }
         },
         "Status": "string"
      },
      "HealthCheckIds": [ "string" ],
      "Id": "string",
      "Name": "string",
      "ProtectionArn": "string",
      "ResourceArn": "string"
   }
}
```

## Response Elements
<a name="API_DescribeProtection_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Protection](#API_DescribeProtection_ResponseSyntax) **   <a name="AWSShield-DescribeProtection-response-Protection"></a>
The [Protection](API_Protection.md) that you requested.   
Type: [Protection](API_Protection.md) object

## Errors
<a name="API_DescribeProtection_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalErrorException **   
Exception that indicates that a problem occurred with the service infrastructure. You can retry the request.  
HTTP Status Code: 500

 ** InvalidParameterException **   
Exception that indicates that the parameters passed to the API are invalid. If available, this exception includes details in additional properties.     
 ** fields **   
Fields that caused the exception.  
 ** reason **   
Additional information about the exception.
HTTP Status Code: 400

 ** ResourceNotFoundException **   
Exception indicating the specified resource does not exist. If available, this exception includes details in additional properties.     
 ** resourceType **   
Type of resource.
HTTP Status Code: 400

## See Also
<a name="API_DescribeProtection_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/shield-2016-06-02/DescribeProtection) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/shield-2016-06-02/DescribeProtection) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/shield-2016-06-02/DescribeProtection) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/shield-2016-06-02/DescribeProtection) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/shield-2016-06-02/DescribeProtection) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/shield-2016-06-02/DescribeProtection) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/shield-2016-06-02/DescribeProtection) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/shield-2016-06-02/DescribeProtection) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/shield-2016-06-02/DescribeProtection) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/shield-2016-06-02/DescribeProtection) 