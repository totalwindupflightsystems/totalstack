---
id: "@specs/aws/shield/docs/API_CreateProtectionGroup"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS CreateProtectionGroup"
status: active
depends_on:
  - "@specs/aws/shield/meta"
---

# CreateProtectionGroup

> **source:** AWS Documentation
> **spec:id:** @specs/aws/shield/docs/API_CreateProtectionGroup
> **target_lang:** meta — documentation tier. ALL sections preserved.



# CreateProtectionGroup
<a name="API_CreateProtectionGroup"></a>

Creates a grouping of protected resources so they can be handled as a collective. This resource grouping improves the accuracy of detection and reduces false positives. 

## Request Syntax
<a name="API_CreateProtectionGroup_RequestSyntax"></a>

```
{
   "Aggregation": "{{string}}",
   "Members": [ "{{string}}" ],
   "Pattern": "{{string}}",
   "ProtectionGroupId": "{{string}}",
   "ResourceType": "{{string}}",
   "Tags": [ 
      { 
         "Key": "{{string}}",
         "Value": "{{string}}"
      }
   ]
}
```

## Request Parameters
<a name="API_CreateProtectionGroup_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [Aggregation](#API_CreateProtectionGroup_RequestSyntax) **   <a name="AWSShield-CreateProtectionGroup-request-Aggregation"></a>
Defines how AWS Shield combines resource data for the group in order to detect, mitigate, and report events.  
+ Sum - Use the total traffic across the group. This is a good choice for most cases. Examples include Elastic IP addresses for EC2 instances that scale manually or automatically.
+ Mean - Use the average of the traffic across the group. This is a good choice for resources that share traffic uniformly. Examples include accelerators and load balancers.
+ Max - Use the highest traffic from each resource. This is useful for resources that don't share traffic and for resources that share that traffic in a non-uniform way. Examples include Amazon CloudFront and origin resources for CloudFront distributions.
Type: String  
Valid Values: `SUM | MEAN | MAX`   
Required: Yes

 ** [Members](#API_CreateProtectionGroup_RequestSyntax) **   <a name="AWSShield-CreateProtectionGroup-request-Members"></a>
The Amazon Resource Names (ARNs) of the resources to include in the protection group. You must set this when you set `Pattern` to `ARBITRARY` and you must not set it for any other `Pattern` setting.   
Type: Array of strings  
Array Members: Minimum number of 0 items. Maximum number of 10000 items.  
Length Constraints: Minimum length of 1. Maximum length of 2048.  
Pattern: `^arn:aws.*`   
Required: No

 ** [Pattern](#API_CreateProtectionGroup_RequestSyntax) **   <a name="AWSShield-CreateProtectionGroup-request-Pattern"></a>
The criteria to use to choose the protected resources for inclusion in the group. You can include all resources that have protections, provide a list of resource Amazon Resource Names (ARNs), or include all resources of a specified resource type.   
Type: String  
Valid Values: `ALL | ARBITRARY | BY_RESOURCE_TYPE`   
Required: Yes

 ** [ProtectionGroupId](#API_CreateProtectionGroup_RequestSyntax) **   <a name="AWSShield-CreateProtectionGroup-request-ProtectionGroupId"></a>
The name of the protection group. You use this to identify the protection group in lists and to manage the protection group, for example to update, delete, or describe it.   
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 36.  
Pattern: `[a-zA-Z0-9\\-]*`   
Required: Yes

 ** [ResourceType](#API_CreateProtectionGroup_RequestSyntax) **   <a name="AWSShield-CreateProtectionGroup-request-ResourceType"></a>
The resource type to include in the protection group. All protected resources of this type are included in the protection group. Newly protected resources of this type are automatically added to the group. You must set this when you set `Pattern` to `BY_RESOURCE_TYPE` and you must not set it for any other `Pattern` setting.   
Type: String  
Valid Values: `CLOUDFRONT_DISTRIBUTION | ROUTE_53_HOSTED_ZONE | ELASTIC_IP_ALLOCATION | CLASSIC_LOAD_BALANCER | APPLICATION_LOAD_BALANCER | GLOBAL_ACCELERATOR`   
Required: No

 ** [Tags](#API_CreateProtectionGroup_RequestSyntax) **   <a name="AWSShield-CreateProtectionGroup-request-Tags"></a>
One or more tag key-value pairs for the protection group.  
Type: Array of [Tag](API_Tag.md) objects  
Array Members: Minimum number of 0 items. Maximum number of 200 items.  
Required: No

## Response Elements
<a name="API_CreateProtectionGroup_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_CreateProtectionGroup_Errors"></a>

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
<a name="API_CreateProtectionGroup_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/shield-2016-06-02/CreateProtectionGroup) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/shield-2016-06-02/CreateProtectionGroup) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/shield-2016-06-02/CreateProtectionGroup) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/shield-2016-06-02/CreateProtectionGroup) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/shield-2016-06-02/CreateProtectionGroup) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/shield-2016-06-02/CreateProtectionGroup) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/shield-2016-06-02/CreateProtectionGroup) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/shield-2016-06-02/CreateProtectionGroup) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/shield-2016-06-02/CreateProtectionGroup) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/shield-2016-06-02/CreateProtectionGroup) 