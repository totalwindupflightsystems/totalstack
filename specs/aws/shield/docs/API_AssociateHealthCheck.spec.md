---
id: "@specs/aws/shield/docs/API_AssociateHealthCheck"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS AssociateHealthCheck"
status: active
depends_on:
  - "@specs/aws/shield/meta"
---

# AssociateHealthCheck

> **source:** AWS Documentation
> **spec:id:** @specs/aws/shield/docs/API_AssociateHealthCheck
> **target_lang:** meta — documentation tier. ALL sections preserved.



# AssociateHealthCheck
<a name="API_AssociateHealthCheck"></a>

Adds health-based detection to the Shield Advanced protection for a resource. Shield Advanced health-based detection uses the health of your AWS resource to improve responsiveness and accuracy in attack detection and response. 

You define the health check in Route 53 and then associate it with your Shield Advanced protection. For more information, see [Configuring health-based detection using health checks](https://docs.aws.amazon.com/waf/latest/developerguide/ddos-advanced-health-checks.html) in the * AWS WAF Developer Guide* and [Creating, updating, and deleting health checks](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/health-checks-creating-deleting.html) in the *Amazon Route 53 Developer Guide*. 

## Request Syntax
<a name="API_AssociateHealthCheck_RequestSyntax"></a>

```
{
   "HealthCheckArn": "{{string}}",
   "ProtectionId": "{{string}}"
}
```

## Request Parameters
<a name="API_AssociateHealthCheck_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [HealthCheckArn](#API_AssociateHealthCheck_RequestSyntax) **   <a name="AWSShield-AssociateHealthCheck-request-HealthCheckArn"></a>
The Amazon Resource Name (ARN) of the health check to associate with the protection.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 2048.  
Pattern: `^arn:aws:route53:::healthcheck/\S{36}$`   
Required: Yes

 ** [ProtectionId](#API_AssociateHealthCheck_RequestSyntax) **   <a name="AWSShield-AssociateHealthCheck-request-ProtectionId"></a>
The unique identifier (ID) for the [Protection](API_Protection.md) object to add the health check association to.   
Type: String  
Length Constraints: Fixed length of 36.  
Pattern: `[a-zA-Z0-9\\-]*`   
Required: Yes

## Response Elements
<a name="API_AssociateHealthCheck_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_AssociateHealthCheck_Errors"></a>

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

 ** InvalidResourceException **   
Exception that indicates that the resource is invalid. You might not have access to the resource, or the resource might not exist.  
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
<a name="API_AssociateHealthCheck_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/shield-2016-06-02/AssociateHealthCheck) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/shield-2016-06-02/AssociateHealthCheck) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/shield-2016-06-02/AssociateHealthCheck) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/shield-2016-06-02/AssociateHealthCheck) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/shield-2016-06-02/AssociateHealthCheck) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/shield-2016-06-02/AssociateHealthCheck) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/shield-2016-06-02/AssociateHealthCheck) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/shield-2016-06-02/AssociateHealthCheck) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/shield-2016-06-02/AssociateHealthCheck) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/shield-2016-06-02/AssociateHealthCheck) 