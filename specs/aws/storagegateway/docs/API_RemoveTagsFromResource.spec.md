---
id: "@specs/aws/storagegateway/docs/API_RemoveTagsFromResource"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS RemoveTagsFromResource"
status: active
depends_on:
  - "@specs/aws/storagegateway/meta"
---

# RemoveTagsFromResource

> **source:** AWS Documentation
> **spec:id:** @specs/aws/storagegateway/docs/API_RemoveTagsFromResource
> **target_lang:** meta — documentation tier. ALL sections preserved.



# RemoveTagsFromResource
<a name="API_RemoveTagsFromResource"></a>

Removes one or more tags from the specified resource. This operation is supported in storage gateways of all types.

## Request Syntax
<a name="API_RemoveTagsFromResource_RequestSyntax"></a>

```
{
   "ResourceARN": "{{string}}",
   "TagKeys": [ "{{string}}" ]
}
```

## Request Parameters
<a name="API_RemoveTagsFromResource_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [ResourceARN](#API_RemoveTagsFromResource_RequestSyntax) **   <a name="StorageGateway-RemoveTagsFromResource-request-ResourceARN"></a>
The Amazon Resource Name (ARN) of the resource you want to remove the tags from.  
Type: String  
Length Constraints: Minimum length of 50. Maximum length of 500.  
Required: Yes

 ** [TagKeys](#API_RemoveTagsFromResource_RequestSyntax) **   <a name="StorageGateway-RemoveTagsFromResource-request-TagKeys"></a>
The keys of the tags you want to remove from the specified resource. A tag is composed of a key-value pair.  
Type: Array of strings  
Length Constraints: Minimum length of 1. Maximum length of 128.  
Pattern: `^([\p{L}\p{Z}\p{N}_.:/=+\-@]*)$`   
Required: Yes

## Response Syntax
<a name="API_RemoveTagsFromResource_ResponseSyntax"></a>

```
{
   "ResourceARN": "string"
}
```

## Response Elements
<a name="API_RemoveTagsFromResource_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ResourceARN](#API_RemoveTagsFromResource_ResponseSyntax) **   <a name="StorageGateway-RemoveTagsFromResource-response-ResourceARN"></a>
The Amazon Resource Name (ARN) of the resource that the tags were removed from.  
Type: String  
Length Constraints: Minimum length of 50. Maximum length of 500.

## Errors
<a name="API_RemoveTagsFromResource_Errors"></a>

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
<a name="API_RemoveTagsFromResource_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/storagegateway-2013-06-30/RemoveTagsFromResource) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/storagegateway-2013-06-30/RemoveTagsFromResource) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/storagegateway-2013-06-30/RemoveTagsFromResource) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/storagegateway-2013-06-30/RemoveTagsFromResource) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/storagegateway-2013-06-30/RemoveTagsFromResource) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/storagegateway-2013-06-30/RemoveTagsFromResource) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/storagegateway-2013-06-30/RemoveTagsFromResource) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/storagegateway-2013-06-30/RemoveTagsFromResource) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/storagegateway-2013-06-30/RemoveTagsFromResource) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/storagegateway-2013-06-30/RemoveTagsFromResource) 