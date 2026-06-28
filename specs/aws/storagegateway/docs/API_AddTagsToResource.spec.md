---
id: "@specs/aws/storagegateway/docs/API_AddTagsToResource"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS AddTagsToResource"
status: active
depends_on:
  - "@specs/aws/storagegateway/meta"
---

# AddTagsToResource

> **source:** AWS Documentation
> **spec:id:** @specs/aws/storagegateway/docs/API_AddTagsToResource
> **target_lang:** meta — documentation tier. ALL sections preserved.



# AddTagsToResource
<a name="API_AddTagsToResource"></a>

Adds one or more tags to the specified resource. You use tags to add metadata to resources, which you can use to categorize these resources. For example, you can categorize resources by purpose, owner, environment, or team. Each tag consists of a key and a value, which you define. You can add tags to the following Storage Gateway resources:
+ Storage gateways of all types
+ Storage volumes
+ Virtual tapes
+ NFS and SMB file shares
+ File System associations

You can create a maximum of 50 tags for each resource. Virtual tapes and storage volumes that are recovered to a new gateway maintain their tags.

## Request Syntax
<a name="API_AddTagsToResource_RequestSyntax"></a>

```
{
   "ResourceARN": "{{string}}",
   "Tags": [ 
      { 
         "Key": "{{string}}",
         "Value": "{{string}}"
      }
   ]
}
```

## Request Parameters
<a name="API_AddTagsToResource_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [ResourceARN](#API_AddTagsToResource_RequestSyntax) **   <a name="StorageGateway-AddTagsToResource-request-ResourceARN"></a>
The Amazon Resource Name (ARN) of the resource you want to add tags to.  
Type: String  
Length Constraints: Minimum length of 50. Maximum length of 500.  
Required: Yes

 ** [Tags](#API_AddTagsToResource_RequestSyntax) **   <a name="StorageGateway-AddTagsToResource-request-Tags"></a>
The key-value pair that represents the tag you want to add to the resource. The value can be an empty string.  
Valid characters for key and value are letters, spaces, and numbers representable in UTF-8 format, and the following special characters: \+ - = . \_ : / @. The maximum length of a tag's key is 128 characters, and the maximum length for a tag's value is 256.
Type: Array of [Tag](API_Tag.md) objects  
Required: Yes

## Response Syntax
<a name="API_AddTagsToResource_ResponseSyntax"></a>

```
{
   "ResourceARN": "string"
}
```

## Response Elements
<a name="API_AddTagsToResource_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ResourceARN](#API_AddTagsToResource_ResponseSyntax) **   <a name="StorageGateway-AddTagsToResource-response-ResourceARN"></a>
The Amazon Resource Name (ARN) of the resource you want to add tags to.  
Type: String  
Length Constraints: Minimum length of 50. Maximum length of 500.

## Errors
<a name="API_AddTagsToResource_Errors"></a>

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
<a name="API_AddTagsToResource_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/storagegateway-2013-06-30/AddTagsToResource) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/storagegateway-2013-06-30/AddTagsToResource) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/storagegateway-2013-06-30/AddTagsToResource) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/storagegateway-2013-06-30/AddTagsToResource) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/storagegateway-2013-06-30/AddTagsToResource) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/storagegateway-2013-06-30/AddTagsToResource) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/storagegateway-2013-06-30/AddTagsToResource) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/storagegateway-2013-06-30/AddTagsToResource) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/storagegateway-2013-06-30/AddTagsToResource) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/storagegateway-2013-06-30/AddTagsToResource) 