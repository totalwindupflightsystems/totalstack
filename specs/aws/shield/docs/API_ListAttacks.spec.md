---
id: "@specs/aws/shield/docs/API_ListAttacks"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS ListAttacks"
status: active
depends_on:
  - "@specs/aws/shield/meta"
---

# ListAttacks

> **source:** AWS Documentation
> **spec:id:** @specs/aws/shield/docs/API_ListAttacks
> **target_lang:** meta — documentation tier. ALL sections preserved.



# ListAttacks
<a name="API_ListAttacks"></a>

Returns all ongoing DDoS attacks or all DDoS attacks during a specified time period.

## Request Syntax
<a name="API_ListAttacks_RequestSyntax"></a>

```
{
   "EndTime": { 
      "FromInclusive": {{number}},
      "ToExclusive": {{number}}
   },
   "MaxResults": {{number}},
   "NextToken": "{{string}}",
   "ResourceArns": [ "{{string}}" ],
   "StartTime": { 
      "FromInclusive": {{number}},
      "ToExclusive": {{number}}
   }
}
```

## Request Parameters
<a name="API_ListAttacks_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [EndTime](#API_ListAttacks_RequestSyntax) **   <a name="AWSShield-ListAttacks-request-EndTime"></a>
The end of the time period for the attacks. This is a `timestamp` type. The request syntax listing for this call indicates a `number` type, but you can provide the time in any valid [timestamp format](https://docs.aws.amazon.com/cli/latest/userguide/cli-usage-parameters-types.html#parameter-type-timestamp) setting.   
Type: [TimeRange](API_TimeRange.md) object  
Required: No

 ** [MaxResults](#API_ListAttacks_RequestSyntax) **   <a name="AWSShield-ListAttacks-request-MaxResults"></a>
The greatest number of objects that you want Shield Advanced to return to the list request. Shield Advanced might return fewer objects than you indicate in this setting, even if more objects are available. If there are more objects remaining, Shield Advanced will always also return a `NextToken` value in the response.  
The default setting is 20.  
Type: Integer  
Valid Range: Minimum value of 0. Maximum value of 10000.  
Required: No

 ** [NextToken](#API_ListAttacks_RequestSyntax) **   <a name="AWSShield-ListAttacks-request-NextToken"></a>
When you request a list of objects from AWS Shield Advanced, if the response does not include all of the remaining available objects, Shield Advanced includes a `NextToken` value in the response. You can retrieve the next batch of objects by requesting the list again and providing the token that was returned by the prior call in your request.   
You can indicate the maximum number of objects that you want Shield Advanced to return for a single call with the `MaxResults` setting. Shield Advanced will not return more than `MaxResults` objects, but may return fewer, even if more objects are still available.  
Whenever more objects remain that Shield Advanced has not yet returned to you, the response will include a `NextToken` value.  
On your first call to a list operation, leave this setting empty.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 4096.  
Pattern: `^.*$`   
Required: No

 ** [ResourceArns](#API_ListAttacks_RequestSyntax) **   <a name="AWSShield-ListAttacks-request-ResourceArns"></a>
The ARNs (Amazon Resource Names) of the resources that were attacked. If you leave this blank, all applicable resources for this account will be included.  
Type: Array of strings  
Length Constraints: Minimum length of 1. Maximum length of 2048.  
Pattern: `^arn:aws.*`   
Required: No

 ** [StartTime](#API_ListAttacks_RequestSyntax) **   <a name="AWSShield-ListAttacks-request-StartTime"></a>
The start of the time period for the attacks. This is a `timestamp` type. The request syntax listing for this call indicates a `number` type, but you can provide the time in any valid [timestamp format](https://docs.aws.amazon.com/cli/latest/userguide/cli-usage-parameters-types.html#parameter-type-timestamp) setting.   
Type: [TimeRange](API_TimeRange.md) object  
Required: No

## Response Syntax
<a name="API_ListAttacks_ResponseSyntax"></a>

```
{
   "AttackSummaries": [ 
      { 
         "AttackId": "string",
         "AttackVectors": [ 
            { 
               "VectorType": "string"
            }
         ],
         "EndTime": number,
         "ResourceArn": "string",
         "StartTime": number
      }
   ],
   "NextToken": "string"
}
```

## Response Elements
<a name="API_ListAttacks_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [AttackSummaries](#API_ListAttacks_ResponseSyntax) **   <a name="AWSShield-ListAttacks-response-AttackSummaries"></a>
The attack information for the specified time range.  
Type: Array of [AttackSummary](API_AttackSummary.md) objects

 ** [NextToken](#API_ListAttacks_ResponseSyntax) **   <a name="AWSShield-ListAttacks-response-NextToken"></a>
When you request a list of objects from AWS Shield Advanced, if the response does not include all of the remaining available objects, Shield Advanced includes a `NextToken` value in the response. You can retrieve the next batch of objects by requesting the list again and providing the token that was returned by the prior call in your request.   
You can indicate the maximum number of objects that you want Shield Advanced to return for a single call with the `MaxResults` setting. Shield Advanced will not return more than `MaxResults` objects, but may return fewer, even if more objects are still available.  
Whenever more objects remain that Shield Advanced has not yet returned to you, the response will include a `NextToken` value.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 4096.  
Pattern: `^.*$` 

## Errors
<a name="API_ListAttacks_Errors"></a>

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

## See Also
<a name="API_ListAttacks_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/shield-2016-06-02/ListAttacks) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/shield-2016-06-02/ListAttacks) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/shield-2016-06-02/ListAttacks) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/shield-2016-06-02/ListAttacks) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/shield-2016-06-02/ListAttacks) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/shield-2016-06-02/ListAttacks) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/shield-2016-06-02/ListAttacks) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/shield-2016-06-02/ListAttacks) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/shield-2016-06-02/ListAttacks) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/shield-2016-06-02/ListAttacks) 