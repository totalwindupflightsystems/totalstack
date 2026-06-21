---
id: "@specs/aws/shield/docs/API_ListProtections"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS ListProtections"
status: active
depends_on:
  - "@specs/aws/shield/meta"
---

# ListProtections

> **source:** AWS Documentation
> **spec:id:** @specs/aws/shield/docs/API_ListProtections
> **target_lang:** meta — documentation tier. ALL sections preserved.



# ListProtections
<a name="API_ListProtections"></a>

Retrieves [Protection](API_Protection.md) objects for the account. You can retrieve all protections or you can provide filtering criteria and retrieve just the subset of protections that match the criteria. 

## Request Syntax
<a name="API_ListProtections_RequestSyntax"></a>

```
{
   "InclusionFilters": { 
      "ProtectionNames": [ "{{string}}" ],
      "ResourceArns": [ "{{string}}" ],
      "ResourceTypes": [ "{{string}}" ]
   },
   "MaxResults": {{number}},
   "NextToken": "{{string}}"
}
```

## Request Parameters
<a name="API_ListProtections_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [InclusionFilters](#API_ListProtections_RequestSyntax) **   <a name="AWSShield-ListProtections-request-InclusionFilters"></a>
Narrows the set of protections that the call retrieves. You can retrieve a single protection by providing its name or the ARN (Amazon Resource Name) of its protected resource. You can also retrieve all protections for a specific resource type. You can provide up to one criteria per filter type. Shield Advanced returns protections that exactly match all of the filter criteria that you provide.  
Type: [InclusionProtectionFilters](API_InclusionProtectionFilters.md) object  
Required: No

 ** [MaxResults](#API_ListProtections_RequestSyntax) **   <a name="AWSShield-ListProtections-request-MaxResults"></a>
The greatest number of objects that you want Shield Advanced to return to the list request. Shield Advanced might return fewer objects than you indicate in this setting, even if more objects are available. If there are more objects remaining, Shield Advanced will always also return a `NextToken` value in the response.  
The default setting is 20.  
Type: Integer  
Valid Range: Minimum value of 0. Maximum value of 10000.  
Required: No

 ** [NextToken](#API_ListProtections_RequestSyntax) **   <a name="AWSShield-ListProtections-request-NextToken"></a>
When you request a list of objects from AWS Shield Advanced, if the response does not include all of the remaining available objects, Shield Advanced includes a `NextToken` value in the response. You can retrieve the next batch of objects by requesting the list again and providing the token that was returned by the prior call in your request.   
You can indicate the maximum number of objects that you want Shield Advanced to return for a single call with the `MaxResults` setting. Shield Advanced will not return more than `MaxResults` objects, but may return fewer, even if more objects are still available.  
Whenever more objects remain that Shield Advanced has not yet returned to you, the response will include a `NextToken` value.  
On your first call to a list operation, leave this setting empty.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 4096.  
Pattern: `^.*$`   
Required: No

## Response Syntax
<a name="API_ListProtections_ResponseSyntax"></a>

```
{
   "NextToken": "string",
   "Protections": [ 
      { 
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
   ]
}
```

## Response Elements
<a name="API_ListProtections_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [NextToken](#API_ListProtections_ResponseSyntax) **   <a name="AWSShield-ListProtections-response-NextToken"></a>
When you request a list of objects from AWS Shield Advanced, if the response does not include all of the remaining available objects, Shield Advanced includes a `NextToken` value in the response. You can retrieve the next batch of objects by requesting the list again and providing the token that was returned by the prior call in your request.   
You can indicate the maximum number of objects that you want Shield Advanced to return for a single call with the `MaxResults` setting. Shield Advanced will not return more than `MaxResults` objects, but may return fewer, even if more objects are still available.  
Whenever more objects remain that Shield Advanced has not yet returned to you, the response will include a `NextToken` value.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 4096.  
Pattern: `^.*$` 

 ** [Protections](#API_ListProtections_ResponseSyntax) **   <a name="AWSShield-ListProtections-response-Protections"></a>
The array of enabled [Protection](API_Protection.md) objects.  
Type: Array of [Protection](API_Protection.md) objects

## Errors
<a name="API_ListProtections_Errors"></a>

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
<a name="API_ListProtections_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/shield-2016-06-02/ListProtections) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/shield-2016-06-02/ListProtections) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/shield-2016-06-02/ListProtections) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/shield-2016-06-02/ListProtections) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/shield-2016-06-02/ListProtections) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/shield-2016-06-02/ListProtections) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/shield-2016-06-02/ListProtections) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/shield-2016-06-02/ListProtections) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/shield-2016-06-02/ListProtections) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/shield-2016-06-02/ListProtections) 