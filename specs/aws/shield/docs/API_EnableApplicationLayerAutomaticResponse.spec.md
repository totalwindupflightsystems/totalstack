---
id: "@specs/aws/shield/docs/API_EnableApplicationLayerAutomaticResponse"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS EnableApplicationLayerAutomaticResponse"
status: active
depends_on:
  - "@specs/aws/shield/meta"
---

# EnableApplicationLayerAutomaticResponse

> **source:** AWS Documentation
> **spec:id:** @specs/aws/shield/docs/API_EnableApplicationLayerAutomaticResponse
> **target_lang:** meta — documentation tier. ALL sections preserved.



# EnableApplicationLayerAutomaticResponse
<a name="API_EnableApplicationLayerAutomaticResponse"></a>

Enable the Shield Advanced automatic application layer DDoS mitigation for the protected resource. 

**Note**  
This feature is available for Amazon CloudFront distributions and Application Load Balancers only.

This causes Shield Advanced to create, verify, and apply AWS WAF rules for DDoS attacks that it detects for the resource. Shield Advanced applies the rules in a Shield rule group inside the web ACL that you've associated with the resource. For information about how automatic mitigation works and the requirements for using it, see [AWS Shield Advanced automatic application layer DDoS mitigation](https://docs.aws.amazon.com/waf/latest/developerguide/ddos-advanced-automatic-app-layer-response.html).

**Note**  
Don't use this action to make changes to automatic mitigation settings when it's already enabled for a resource. Instead, use [UpdateApplicationLayerAutomaticResponse](API_UpdateApplicationLayerAutomaticResponse.md).

To use this feature, you must associate a web ACL with the protected resource. The web ACL must be created using the latest version of AWS WAF (v2). You can associate the web ACL through the [Shield Advanced console](https://console.aws.amazon.com/wafv2/shieldv2#/). For more information, see [Getting Started with AWS Shield Advanced](https://docs.aws.amazon.com/waf/latest/developerguide/getting-started-ddos.html). You can also associate the web ACL to the resource through the AWS WAF console or the AWS WAF API, but you must manage Shield Advanced automatic mitigation through Shield Advanced. For information about AWS WAF, see [AWS WAF Developer Guide](https://docs.aws.amazon.com/waf/latest/developerguide/).

## Request Syntax
<a name="API_EnableApplicationLayerAutomaticResponse_RequestSyntax"></a>

```
{
   "Action": { 
      "Block": { 
      },
      "Count": { 
      }
   },
   "ResourceArn": "{{string}}"
}
```

## Request Parameters
<a name="API_EnableApplicationLayerAutomaticResponse_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [Action](#API_EnableApplicationLayerAutomaticResponse_RequestSyntax) **   <a name="AWSShield-EnableApplicationLayerAutomaticResponse-request-Action"></a>
Specifies the action setting that Shield Advanced should use in the AWS WAF rules that it creates on behalf of the protected resource in response to DDoS attacks. You specify this as part of the configuration for the automatic application layer DDoS mitigation feature, when you enable or update automatic mitigation. Shield Advanced creates the AWS WAF rules in a Shield Advanced-managed rule group, inside the web ACL that you have associated with the resource.   
Type: [ResponseAction](API_ResponseAction.md) object  
Required: Yes

 ** [ResourceArn](#API_EnableApplicationLayerAutomaticResponse_RequestSyntax) **   <a name="AWSShield-EnableApplicationLayerAutomaticResponse-request-ResourceArn"></a>
The ARN (Amazon Resource Name) of the protected resource.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 2048.  
Pattern: `^arn:aws.*`   
Required: Yes

## Response Elements
<a name="API_EnableApplicationLayerAutomaticResponse_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_EnableApplicationLayerAutomaticResponse_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

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

 ** OptimisticLockException **   
Exception that indicates that the resource state has been modified by another client. Retrieve the resource and then retry your request.  
HTTP Status Code: 400

 ** ResourceNotFoundException **   
Exception indicating the specified resource does not exist. If available, this exception includes details in additional properties.     
 ** resourceType **   
Type of resource.
HTTP Status Code: 400

## See Also
<a name="API_EnableApplicationLayerAutomaticResponse_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/shield-2016-06-02/EnableApplicationLayerAutomaticResponse) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/shield-2016-06-02/EnableApplicationLayerAutomaticResponse) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/shield-2016-06-02/EnableApplicationLayerAutomaticResponse) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/shield-2016-06-02/EnableApplicationLayerAutomaticResponse) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/shield-2016-06-02/EnableApplicationLayerAutomaticResponse) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/shield-2016-06-02/EnableApplicationLayerAutomaticResponse) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/shield-2016-06-02/EnableApplicationLayerAutomaticResponse) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/shield-2016-06-02/EnableApplicationLayerAutomaticResponse) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/shield-2016-06-02/EnableApplicationLayerAutomaticResponse) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/shield-2016-06-02/EnableApplicationLayerAutomaticResponse) 