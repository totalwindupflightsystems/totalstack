---
id: "@specs/aws/storagegateway/docs/API_ListTapePools"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS ListTapePools"
status: active
depends_on:
  - "@specs/aws/storagegateway/meta"
---

# ListTapePools

> **source:** AWS Documentation
> **spec:id:** @specs/aws/storagegateway/docs/API_ListTapePools
> **target_lang:** meta — documentation tier. ALL sections preserved.



# ListTapePools
<a name="API_ListTapePools"></a>

Lists custom tape pools. You specify custom tape pools to list by specifying one or more custom tape pool Amazon Resource Names (ARNs). If you don't specify a custom tape pool ARN, the operation lists all custom tape pools.

This operation supports pagination. You can optionally specify the `Limit` parameter in the body to limit the number of tape pools in the response. If the number of tape pools returned in the response is truncated, the response includes a `Marker` element that you can use in your subsequent request to retrieve the next set of tape pools.

## Request Syntax
<a name="API_ListTapePools_RequestSyntax"></a>

```
{
   "Limit": {{number}},
   "Marker": "{{string}}",
   "PoolARNs": [ "{{string}}" ]
}
```

## Request Parameters
<a name="API_ListTapePools_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [Limit](#API_ListTapePools_RequestSyntax) **   <a name="StorageGateway-ListTapePools-request-Limit"></a>
An optional number limit for the tape pools in the list returned by this call.  
Type: Integer  
Valid Range: Minimum value of 1.  
Required: No

 ** [Marker](#API_ListTapePools_RequestSyntax) **   <a name="StorageGateway-ListTapePools-request-Marker"></a>
A string that indicates the position at which to begin the returned list of tape pools.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 2000.  
Required: No

 ** [PoolARNs](#API_ListTapePools_RequestSyntax) **   <a name="StorageGateway-ListTapePools-request-PoolARNs"></a>
The Amazon Resource Name (ARN) of each of the custom tape pools you want to list. If you don't specify a custom tape pool ARN, the response lists all custom tape pools.   
Type: Array of strings  
Length Constraints: Minimum length of 50. Maximum length of 500.  
Required: No

## Response Syntax
<a name="API_ListTapePools_ResponseSyntax"></a>

```
{
   "Marker": "string",
   "PoolInfos": [ 
      { 
         "PoolARN": "string",
         "PoolName": "string",
         "PoolStatus": "string",
         "RetentionLockTimeInDays": number,
         "RetentionLockType": "string",
         "StorageClass": "string"
      }
   ]
}
```

## Response Elements
<a name="API_ListTapePools_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Marker](#API_ListTapePools_ResponseSyntax) **   <a name="StorageGateway-ListTapePools-response-Marker"></a>
A string that indicates the position at which to begin the returned list of tape pools. Use the marker in your next request to continue pagination of tape pools. If there are no more tape pools to list, this element does not appear in the response body.   
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 2000.

 ** [PoolInfos](#API_ListTapePools_ResponseSyntax) **   <a name="StorageGateway-ListTapePools-response-PoolInfos"></a>
An array of `PoolInfo` objects, where each object describes a single custom tape pool. If there are no custom tape pools, the `PoolInfos` is an empty array.   
Type: Array of [PoolInfo](API_PoolInfo.md) objects

## Errors
<a name="API_ListTapePools_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalServerError **   
An internal server error has occurred during the request. For more information, see the error and message fields.    
 ** error **   
A [StorageGatewayError](API_StorageGatewayError.md) that provides more information about the cause of the error.  
 ** message **   
A human-readable message describing the error that occurred.
HTTP Status Code: 400

 ** InvalidGatewayRequestException **   
An exception occurred because an invalid gateway request was issued to the service. For more information, see the error and message fields.    
 ** error **   
A [StorageGatewayError](API_StorageGatewayError.md) that provides more detail about the cause of the error.  
 ** message **   
A human-readable message describing the error that occurred.
HTTP Status Code: 400

## See Also
<a name="API_ListTapePools_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/storagegateway-2013-06-30/ListTapePools) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/storagegateway-2013-06-30/ListTapePools) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/storagegateway-2013-06-30/ListTapePools) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/storagegateway-2013-06-30/ListTapePools) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/storagegateway-2013-06-30/ListTapePools) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/storagegateway-2013-06-30/ListTapePools) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/storagegateway-2013-06-30/ListTapePools) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/storagegateway-2013-06-30/ListTapePools) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/storagegateway-2013-06-30/ListTapePools) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/storagegateway-2013-06-30/ListTapePools) 