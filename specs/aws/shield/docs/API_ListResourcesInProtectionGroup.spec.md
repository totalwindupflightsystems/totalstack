---
id: "@specs/aws/shield/docs/API_ListResourcesInProtectionGroup"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS ListResourcesInProtectionGroup"
status: active
depends_on:
  - "@specs/aws/shield/meta"
---

# ListResourcesInProtectionGroup

> **source:** AWS Documentation
> **spec:id:** @specs/aws/shield/docs/API_ListResourcesInProtectionGroup
> **target_lang:** meta — documentation tier. ALL sections preserved.



# ListResourcesInProtectionGroup
<a name="API_ListResourcesInProtectionGroup"></a>

Retrieves the resources that are included in the protection group. 

## Request Syntax
<a name="API_ListResourcesInProtectionGroup_RequestSyntax"></a>

```
{
   "MaxResults": {{number}},
   "NextToken": "{{string}}",
   "ProtectionGroupId": "{{string}}"
}
```

## Request Parameters
<a name="API_ListResourcesInProtectionGroup_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [MaxResults](#API_ListResourcesInProtectionGroup_RequestSyntax) **   <a name="AWSShield-ListResourcesInProtectionGroup-request-MaxResults"></a>
The greatest number of objects that you want Shield Advanced to return to the list request. Shield Advanced might return fewer objects than you indicate in this setting, even if more objects are available. If there are more objects remaining, Shield Advanced will always also return a `NextToken` value in the response.  
The default setting is 20.  
Type: Integer  
Valid Range: Minimum value of 0. Maximum value of 10000.  
Required: No

 ** [NextToken](#API_ListResourcesInProtectionGroup_RequestSyntax) **   <a name="AWSShield-ListResourcesInProtectionGroup-request-NextToken"></a>
When you request a list of objects from AWS Shield Advanced, if the response does not include all of the remaining available objects, Shield Advanced includes a `NextToken` value in the response. You can retrieve the next batch of objects by requesting the list again and providing the token that was returned by the prior call in your request.   
You can indicate the maximum number of objects that you want Shield Advanced to return for a single call with the `MaxResults` setting. Shield Advanced will not return more than `MaxResults` objects, but may return fewer, even if more objects are still available.  
Whenever more objects remain that Shield Advanced has not yet returned to you, the response will include a `NextToken` value.  
On your first call to a list operation, leave this setting empty.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 4096.  
Pattern: `^.*$`   
Required: No

 ** [ProtectionGroupId](#API_ListResourcesInProtectionGroup_RequestSyntax) **   <a name="AWSShield-ListResourcesInProtectionGroup-request-ProtectionGroupId"></a>
The name of the protection group. You use this to identify the protection group in lists and to manage the protection group, for example to update, delete, or describe it.   
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 36.  
Pattern: `[a-zA-Z0-9\\-]*`   
Required: Yes

## Response Syntax
<a name="API_ListResourcesInProtectionGroup_ResponseSyntax"></a>

```
{
   "NextToken": "string",
   "ResourceArns": [ "string" ]
}
```

## Response Elements
<a name="API_ListResourcesInProtectionGroup_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [NextToken](#API_ListResourcesInProtectionGroup_ResponseSyntax) **   <a name="AWSShield-ListResourcesInProtectionGroup-response-NextToken"></a>
When you request a list of objects from AWS Shield Advanced, if the response does not include all of the remaining available objects, Shield Advanced includes a `NextToken` value in the response. You can retrieve the next batch of objects by requesting the list again and providing the token that was returned by the prior call in your request.   
You can indicate the maximum number of objects that you want Shield Advanced to return for a single call with the `MaxResults` setting. Shield Advanced will not return more than `MaxResults` objects, but may return fewer, even if more objects are still available.  
Whenever more objects remain that Shield Advanced has not yet returned to you, the response will include a `NextToken` value.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 4096.  
Pattern: `^.*$` 

 ** [ResourceArns](#API_ListResourcesInProtectionGroup_ResponseSyntax) **   <a name="AWSShield-ListResourcesInProtectionGroup-response-ResourceArns"></a>
The Amazon Resource Names (ARNs) of the resources that are included in the protection group.  
Type: Array of strings  
Length Constraints: Minimum length of 1. Maximum length of 2048.  
Pattern: `^arn:aws.*` 

## Errors
<a name="API_ListResourcesInProtectionGroup_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalErrorException **   
Exception that indicates that a problem occurred with the service infrastructure. You can retry the request.  
HTTP Status Code: 500

 ** InvalidPaginationTokenException **   
Exception that indicates that the `NextToken` specified in the request is invalid. Submit the request using the `NextToken` value that was returned in the prior response.  
HTTP Status Code: 400

 ** ResourceNotFoundException **   
Exception indicating the specified resource does not exist. If available, this exception includes details in additional properties.     
 ** resourceType **   
Type of resource.
HTTP Status Code: 400

## See Also
<a name="API_ListResourcesInProtectionGroup_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/shield-2016-06-02/ListResourcesInProtectionGroup) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/shield-2016-06-02/ListResourcesInProtectionGroup) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/shield-2016-06-02/ListResourcesInProtectionGroup) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/shield-2016-06-02/ListResourcesInProtectionGroup) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/shield-2016-06-02/ListResourcesInProtectionGroup) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/shield-2016-06-02/ListResourcesInProtectionGroup) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/shield-2016-06-02/ListResourcesInProtectionGroup) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/shield-2016-06-02/ListResourcesInProtectionGroup) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/shield-2016-06-02/ListResourcesInProtectionGroup) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/shield-2016-06-02/ListResourcesInProtectionGroup) 