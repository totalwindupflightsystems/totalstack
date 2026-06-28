---
id: "@specs/aws/fsx/docs/API_DeleteSnapshot"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS DeleteSnapshot"
status: active
depends_on:
  - "@specs/aws/fsx/meta"
---

# DeleteSnapshot

> **source:** AWS Documentation
> **spec:id:** @specs/aws/fsx/docs/API_DeleteSnapshot
> **target_lang:** meta — documentation tier. ALL sections preserved.



# DeleteSnapshot
<a name="API_DeleteSnapshot"></a>

Deletes an Amazon FSx for OpenZFS snapshot. After deletion, the snapshot no longer exists, and its data is gone. Deleting a snapshot doesn't affect snapshots stored in a file system backup. 

The `DeleteSnapshot` operation returns instantly. The snapshot appears with the lifecycle status of `DELETING` until the deletion is complete.

## Request Syntax
<a name="API_DeleteSnapshot_RequestSyntax"></a>

```
{
   "ClientRequestToken": "{{string}}",
   "SnapshotId": "{{string}}"
}
```

## Request Parameters
<a name="API_DeleteSnapshot_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [ClientRequestToken](#API_DeleteSnapshot_RequestSyntax) **   <a name="FSx-DeleteSnapshot-request-ClientRequestToken"></a>
(Optional) An idempotency token for resource creation, in a string of up to 63 ASCII characters. This token is automatically filled on your behalf when you use the AWS Command Line Interface (AWS CLI) or an AWS SDK.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 63.  
Pattern: `[A-za-z0-9_.-]{0,63}$`   
Required: No

 ** [SnapshotId](#API_DeleteSnapshot_RequestSyntax) **   <a name="FSx-DeleteSnapshot-request-SnapshotId"></a>
The ID of the snapshot that you want to delete.  
Type: String  
Length Constraints: Minimum length of 11. Maximum length of 28.  
Pattern: `^((fs)?volsnap-[0-9a-f]{8,})$`   
Required: Yes

## Response Syntax
<a name="API_DeleteSnapshot_ResponseSyntax"></a>

```
{
   "Lifecycle": "string",
   "SnapshotId": "string"
}
```

## Response Elements
<a name="API_DeleteSnapshot_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Lifecycle](#API_DeleteSnapshot_ResponseSyntax) **   <a name="FSx-DeleteSnapshot-response-Lifecycle"></a>
The lifecycle status of the snapshot. If the `DeleteSnapshot` operation is successful, this status is `DELETING`.  
Type: String  
Valid Values: `PENDING | CREATING | DELETING | AVAILABLE` 

 ** [SnapshotId](#API_DeleteSnapshot_ResponseSyntax) **   <a name="FSx-DeleteSnapshot-response-SnapshotId"></a>
The ID of the deleted snapshot.  
Type: String  
Length Constraints: Minimum length of 11. Maximum length of 28.  
Pattern: `^((fs)?volsnap-[0-9a-f]{8,})$` 

## Errors
<a name="API_DeleteSnapshot_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** BadRequest **   
A generic error indicating a failure with a client request.    
 ** Message **   
A detailed error message.
HTTP Status Code: 400

 ** InternalServerError **   
A generic error indicating a server-side failure.    
 ** Message **   
A detailed error message.
HTTP Status Code: 500

 ** SnapshotNotFound **   
No Amazon FSx snapshots were found based on the supplied parameters.    
 ** Message **   
A detailed error message.
HTTP Status Code: 400

## See Also
<a name="API_DeleteSnapshot_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/fsx-2018-03-01/DeleteSnapshot) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/fsx-2018-03-01/DeleteSnapshot) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/fsx-2018-03-01/DeleteSnapshot) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/fsx-2018-03-01/DeleteSnapshot) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/fsx-2018-03-01/DeleteSnapshot) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/fsx-2018-03-01/DeleteSnapshot) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/fsx-2018-03-01/DeleteSnapshot) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/fsx-2018-03-01/DeleteSnapshot) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/fsx-2018-03-01/DeleteSnapshot) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/fsx-2018-03-01/DeleteSnapshot) 