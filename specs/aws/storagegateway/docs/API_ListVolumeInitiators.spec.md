---
id: "@specs/aws/storagegateway/docs/API_ListVolumeInitiators"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS ListVolumeInitiators"
status: active
depends_on:
  - "@specs/aws/storagegateway/meta"
---

# ListVolumeInitiators

> **source:** AWS Documentation
> **spec:id:** @specs/aws/storagegateway/docs/API_ListVolumeInitiators
> **target_lang:** meta — documentation tier. ALL sections preserved.



# ListVolumeInitiators
<a name="API_ListVolumeInitiators"></a>

Lists iSCSI initiators that are connected to a volume. You can use this operation to determine whether a volume is being used or not. This operation is only supported in the cached volume and stored volume gateway types.

## Request Syntax
<a name="API_ListVolumeInitiators_RequestSyntax"></a>

```
{
   "VolumeARN": "{{string}}"
}
```

## Request Parameters
<a name="API_ListVolumeInitiators_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [VolumeARN](#API_ListVolumeInitiators_RequestSyntax) **   <a name="StorageGateway-ListVolumeInitiators-request-VolumeARN"></a>
The Amazon Resource Name (ARN) of the volume. Use the [ListVolumes](API_ListVolumes.md) operation to return a list of gateway volumes for the gateway.  
Type: String  
Length Constraints: Minimum length of 50. Maximum length of 500.  
Pattern: `arn:(aws(|-cn|-us-gov|-iso[A-Za-z0-9_-]*)):storagegateway:[a-z\-0-9]+:[0-9]+:gateway\/(.+)\/volume\/vol-(\S+)`   
Required: Yes

## Response Syntax
<a name="API_ListVolumeInitiators_ResponseSyntax"></a>

```
{
   "Initiators": [ "string" ]
}
```

## Response Elements
<a name="API_ListVolumeInitiators_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Initiators](#API_ListVolumeInitiators_ResponseSyntax) **   <a name="StorageGateway-ListVolumeInitiators-response-Initiators"></a>
The host names and port numbers of all iSCSI initiators that are connected to the gateway.  
Type: Array of strings  
Length Constraints: Minimum length of 1. Maximum length of 50.

## Errors
<a name="API_ListVolumeInitiators_Errors"></a>

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
<a name="API_ListVolumeInitiators_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/storagegateway-2013-06-30/ListVolumeInitiators) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/storagegateway-2013-06-30/ListVolumeInitiators) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/storagegateway-2013-06-30/ListVolumeInitiators) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/storagegateway-2013-06-30/ListVolumeInitiators) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/storagegateway-2013-06-30/ListVolumeInitiators) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/storagegateway-2013-06-30/ListVolumeInitiators) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/storagegateway-2013-06-30/ListVolumeInitiators) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/storagegateway-2013-06-30/ListVolumeInitiators) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/storagegateway-2013-06-30/ListVolumeInitiators) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/storagegateway-2013-06-30/ListVolumeInitiators) 