---
id: "@specs/aws/shield/docs/API_CreateProtection"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS CreateProtection"
status: active
depends_on:
  - "@specs/aws/shield/meta"
---

# CreateProtection

> **source:** AWS Documentation
> **spec:id:** @specs/aws/shield/docs/API_CreateProtection
> **target_lang:** meta — documentation tier. ALL sections preserved.



# CreateProtection
<a name="API_CreateProtection"></a>

Enables AWS Shield Advanced for a specific AWS resource. The resource can be an Amazon CloudFront distribution, Amazon Route 53 hosted zone, AWS Global Accelerator standard accelerator, Elastic IP Address, Application Load Balancer, or a Classic Load Balancer. You can protect Amazon EC2 instances and Network Load Balancers by association with protected Amazon EC2 Elastic IP addresses.

You can add protection to only a single resource with each `CreateProtection` request. You can add protection to multiple resources at once through the [Shield Advanced console](https://console.aws.amazon.com/wafv2/shieldv2#/). For more information see [Getting Started with AWS Shield Advanced](https://docs.aws.amazon.com/waf/latest/developerguide/getting-started-ddos.html) and [Managing resource protections in AWS Shield Advanced](https://docs.aws.amazon.com/waf/latest/developerguide/ddos-manage-protected-resources.html).

## Request Syntax
<a name="API_CreateProtection_RequestSyntax"></a>

```
{
   "Name": "{{string}}",
   "ResourceArn": "{{string}}",
   "Tags": [ 
      { 
         "Key": "{{string}}",
         "Value": "{{string}}"
      }
   ]
}
```

## Request Parameters
<a name="API_CreateProtection_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [Name](#API_CreateProtection_RequestSyntax) **   <a name="AWSShield-CreateProtection-request-Name"></a>
Friendly name for the `Protection` you are creating.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 128.  
Pattern: `[ a-zA-Z0-9_\\.\\-]*`   
Required: Yes

 ** [ResourceArn](#API_CreateProtection_RequestSyntax) **   <a name="AWSShield-CreateProtection-request-ResourceArn"></a>
The ARN (Amazon Resource Name) of the resource to be protected.  
The ARN should be in one of the following formats:  
+ For an Application Load Balancer: `arn:aws:elasticloadbalancing:region:account-id:loadbalancer/app/load-balancer-name/load-balancer-id ` 
+ For an Elastic Load Balancer (Classic Load Balancer): `arn:aws:elasticloadbalancing:region:account-id:loadbalancer/load-balancer-name ` 
+ For an Amazon CloudFront distribution: `arn:aws:cloudfront::account-id:distribution/distribution-id ` 
+ For an AWS Global Accelerator standard accelerator: `arn:aws:globalaccelerator::account-id:accelerator/accelerator-id ` 
+ For Amazon Route 53: `arn:aws:route53:::hostedzone/hosted-zone-id ` 
+ For an Elastic IP address: `arn:aws:ec2:region:account-id:eip-allocation/allocation-id ` 
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 2048.  
Pattern: `^arn:aws.*`   
Required: Yes

 ** [Tags](#API_CreateProtection_RequestSyntax) **   <a name="AWSShield-CreateProtection-request-Tags"></a>
One or more tag key-value pairs for the [Protection](API_Protection.md) object that is created.  
Type: Array of [Tag](API_Tag.md) objects  
Array Members: Minimum number of 0 items. Maximum number of 200 items.  
Required: No

## Response Syntax
<a name="API_CreateProtection_ResponseSyntax"></a>

```
{
   "ProtectionId": "string"
}
```

## Response Elements
<a name="API_CreateProtection_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ProtectionId](#API_CreateProtection_ResponseSyntax) **   <a name="AWSShield-CreateProtection-response-ProtectionId"></a>
The unique identifier (ID) for the [Protection](API_Protection.md) object that is created.  
Type: String  
Length Constraints: Fixed length of 36.  
Pattern: `[a-zA-Z0-9\\-]*` 

## Errors
<a name="API_CreateProtection_Errors"></a>

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

 ** ResourceAlreadyExistsException **   
Exception indicating the specified resource already exists. If available, this exception includes details in additional properties.     
 ** resourceType **   
The type of resource that already exists.
HTTP Status Code: 400

 ** ResourceNotFoundException **   
Exception indicating the specified resource does not exist. If available, this exception includes details in additional properties.     
 ** resourceType **   
Type of resource.
HTTP Status Code: 400

## See Also
<a name="API_CreateProtection_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/shield-2016-06-02/CreateProtection) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/shield-2016-06-02/CreateProtection) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/shield-2016-06-02/CreateProtection) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/shield-2016-06-02/CreateProtection) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/shield-2016-06-02/CreateProtection) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/shield-2016-06-02/CreateProtection) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/shield-2016-06-02/CreateProtection) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/shield-2016-06-02/CreateProtection) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/shield-2016-06-02/CreateProtection) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/shield-2016-06-02/CreateProtection) 