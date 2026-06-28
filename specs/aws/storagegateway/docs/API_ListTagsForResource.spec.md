---
id: "@specs/aws/storagegateway/docs/API_ListTagsForResource"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS ListTagsForResource"
status: active
depends_on:
  - "@specs/aws/storagegateway/meta"
---

# ListTagsForResource

> **source:** AWS Documentation
> **spec:id:** @specs/aws/storagegateway/docs/API_ListTagsForResource
> **target_lang:** meta — documentation tier. ALL sections preserved.



# ListTagsForResource
<a name="API_ListTagsForResource"></a>

Lists the tags that have been added to the specified resource. This operation is supported in storage gateways of all types.

## Request Syntax
<a name="API_ListTagsForResource_RequestSyntax"></a>

```
{
   "Limit": {{number}},
   "Marker": "{{string}}",
   "ResourceARN": "{{string}}"
}
```

## Request Parameters
<a name="API_ListTagsForResource_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [Limit](#API_ListTagsForResource_RequestSyntax) **   <a name="StorageGateway-ListTagsForResource-request-Limit"></a>
Specifies that the list of tags returned be limited to the specified number of items.  
Type: Integer  
Valid Range: Minimum value of 1.  
Required: No

 ** [Marker](#API_ListTagsForResource_RequestSyntax) **   <a name="StorageGateway-ListTagsForResource-request-Marker"></a>
An opaque string that indicates the position at which to begin returning the list of tags.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 2000.  
Required: No

 ** [ResourceARN](#API_ListTagsForResource_RequestSyntax) **   <a name="StorageGateway-ListTagsForResource-request-ResourceARN"></a>
The Amazon Resource Name (ARN) of the resource for which you want to list tags.  
Type: String  
Length Constraints: Minimum length of 50. Maximum length of 500.  
Required: Yes

## Response Syntax
<a name="API_ListTagsForResource_ResponseSyntax"></a>

```
{
   "Marker": "string",
   "ResourceARN": "string",
   "Tags": [ 
      { 
         "Key": "string",
         "Value": "string"
      }
   ]
}
```

## Response Elements
<a name="API_ListTagsForResource_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Marker](#API_ListTagsForResource_ResponseSyntax) **   <a name="StorageGateway-ListTagsForResource-response-Marker"></a>
An opaque string that indicates the position at which to stop returning the list of tags.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 2000.

 ** [ResourceARN](#API_ListTagsForResource_ResponseSyntax) **   <a name="StorageGateway-ListTagsForResource-response-ResourceARN"></a>
The Amazon Resource Name (ARN) of the resource for which you want to list tags.  
Type: String  
Length Constraints: Minimum length of 50. Maximum length of 500.

 ** [Tags](#API_ListTagsForResource_ResponseSyntax) **   <a name="StorageGateway-ListTagsForResource-response-Tags"></a>
An array that contains the tags for the specified resource.  
Type: Array of [Tag](API_Tag.md) objects

## Errors
<a name="API_ListTagsForResource_Errors"></a>

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
<a name="API_ListTagsForResource_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/storagegateway-2013-06-30/ListTagsForResource) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/storagegateway-2013-06-30/ListTagsForResource) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/storagegateway-2013-06-30/ListTagsForResource) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/storagegateway-2013-06-30/ListTagsForResource) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/storagegateway-2013-06-30/ListTagsForResource) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/storagegateway-2013-06-30/ListTagsForResource) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/storagegateway-2013-06-30/ListTagsForResource) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/storagegateway-2013-06-30/ListTagsForResource) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/storagegateway-2013-06-30/ListTagsForResource) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/storagegateway-2013-06-30/ListTagsForResource) 