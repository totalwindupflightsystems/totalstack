---
id: "@specs/aws/storagegateway/docs/API_ListFileSystemAssociations"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS ListFileSystemAssociations"
status: active
depends_on:
  - "@specs/aws/storagegateway/meta"
---

# ListFileSystemAssociations

> **source:** AWS Documentation
> **spec:id:** @specs/aws/storagegateway/docs/API_ListFileSystemAssociations
> **target_lang:** meta — documentation tier. ALL sections preserved.



# ListFileSystemAssociations
<a name="API_ListFileSystemAssociations"></a>

Gets a list of `FileSystemAssociationSummary` objects. Each object contains a summary of a file system association. This operation is only supported for FSx File Gateways.

## Request Syntax
<a name="API_ListFileSystemAssociations_RequestSyntax"></a>

```
{
   "GatewayARN": "{{string}}",
   "Limit": {{number}},
   "Marker": "{{string}}"
}
```

## Request Parameters
<a name="API_ListFileSystemAssociations_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [GatewayARN](#API_ListFileSystemAssociations_RequestSyntax) **   <a name="StorageGateway-ListFileSystemAssociations-request-GatewayARN"></a>
The Amazon Resource Name (ARN) of the gateway. Use the [ListGateways](API_ListGateways.md) operation to return a list of gateways for your account and AWS Region.  
Type: String  
Length Constraints: Minimum length of 50. Maximum length of 500.  
Required: No

 ** [Limit](#API_ListFileSystemAssociations_RequestSyntax) **   <a name="StorageGateway-ListFileSystemAssociations-request-Limit"></a>
The maximum number of file system associations to return in the response. If present, `Limit` must be an integer with a value greater than zero. Optional.  
Type: Integer  
Valid Range: Minimum value of 1.  
Required: No

 ** [Marker](#API_ListFileSystemAssociations_RequestSyntax) **   <a name="StorageGateway-ListFileSystemAssociations-request-Marker"></a>
Opaque pagination token returned from a previous `ListFileSystemAssociations` operation. If present, `Marker` specifies where to continue the list from after a previous call to `ListFileSystemAssociations`. Optional.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 2000.  
Required: No

## Response Syntax
<a name="API_ListFileSystemAssociations_ResponseSyntax"></a>

```
{
   "FileSystemAssociationSummaryList": [ 
      { 
         "FileSystemAssociationARN": "string",
         "FileSystemAssociationId": "string",
         "FileSystemAssociationStatus": "string",
         "GatewayARN": "string"
      }
   ],
   "Marker": "string",
   "NextMarker": "string"
}
```

## Response Elements
<a name="API_ListFileSystemAssociations_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [FileSystemAssociationSummaryList](#API_ListFileSystemAssociations_ResponseSyntax) **   <a name="StorageGateway-ListFileSystemAssociations-response-FileSystemAssociationSummaryList"></a>
An array of information about the Amazon FSx gateway's file system associations.  
Type: Array of [FileSystemAssociationSummary](API_FileSystemAssociationSummary.md) objects

 ** [Marker](#API_ListFileSystemAssociations_ResponseSyntax) **   <a name="StorageGateway-ListFileSystemAssociations-response-Marker"></a>
If the request includes `Marker`, the response returns that value in this field.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 2000.

 ** [NextMarker](#API_ListFileSystemAssociations_ResponseSyntax) **   <a name="StorageGateway-ListFileSystemAssociations-response-NextMarker"></a>
If a value is present, there are more file system associations to return. In a subsequent request, use `NextMarker` as the value for `Marker` to retrieve the next set of file system associations.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 2000.

## Errors
<a name="API_ListFileSystemAssociations_Errors"></a>

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
<a name="API_ListFileSystemAssociations_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/storagegateway-2013-06-30/ListFileSystemAssociations) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/storagegateway-2013-06-30/ListFileSystemAssociations) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/storagegateway-2013-06-30/ListFileSystemAssociations) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/storagegateway-2013-06-30/ListFileSystemAssociations) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/storagegateway-2013-06-30/ListFileSystemAssociations) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/storagegateway-2013-06-30/ListFileSystemAssociations) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/storagegateway-2013-06-30/ListFileSystemAssociations) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/storagegateway-2013-06-30/ListFileSystemAssociations) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/storagegateway-2013-06-30/ListFileSystemAssociations) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/storagegateway-2013-06-30/ListFileSystemAssociations) 