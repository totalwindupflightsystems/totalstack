---
id: "@specs/aws/fsx/docs/API_DeleteDataRepositoryAssociation"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS DeleteDataRepositoryAssociation"
status: active
depends_on:
  - "@specs/aws/fsx/meta"
---

# DeleteDataRepositoryAssociation

> **source:** AWS Documentation
> **spec:id:** @specs/aws/fsx/docs/API_DeleteDataRepositoryAssociation
> **target_lang:** meta — documentation tier. ALL sections preserved.



# DeleteDataRepositoryAssociation
<a name="API_DeleteDataRepositoryAssociation"></a>

Deletes a data repository association on an Amazon FSx for Lustre file system. Deleting the data repository association unlinks the file system from the Amazon S3 bucket. When deleting a data repository association, you have the option of deleting the data in the file system that corresponds to the data repository association. Data repository associations are supported on all FSx for Lustre 2.12 and 2.15 file systems, excluding `scratch_1` deployment type.

## Request Syntax
<a name="API_DeleteDataRepositoryAssociation_RequestSyntax"></a>

```
{
   "AssociationId": "{{string}}",
   "ClientRequestToken": "{{string}}",
   "DeleteDataInFileSystem": {{boolean}}
}
```

## Request Parameters
<a name="API_DeleteDataRepositoryAssociation_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [AssociationId](#API_DeleteDataRepositoryAssociation_RequestSyntax) **   <a name="FSx-DeleteDataRepositoryAssociation-request-AssociationId"></a>
The ID of the data repository association that you want to delete.  
Type: String  
Length Constraints: Minimum length of 13. Maximum length of 23.  
Pattern: `^(dra-[0-9a-f]{8,})$`   
Required: Yes

 ** [ClientRequestToken](#API_DeleteDataRepositoryAssociation_RequestSyntax) **   <a name="FSx-DeleteDataRepositoryAssociation-request-ClientRequestToken"></a>
(Optional) An idempotency token for resource creation, in a string of up to 63 ASCII characters. This token is automatically filled on your behalf when you use the AWS Command Line Interface (AWS CLI) or an AWS SDK.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 63.  
Pattern: `[A-za-z0-9_.-]{0,63}$`   
Required: No

 ** [DeleteDataInFileSystem](#API_DeleteDataRepositoryAssociation_RequestSyntax) **   <a name="FSx-DeleteDataRepositoryAssociation-request-DeleteDataInFileSystem"></a>
Set to `true` to delete the data in the file system that corresponds to the data repository association.  
Type: Boolean  
Required: No

## Response Syntax
<a name="API_DeleteDataRepositoryAssociation_ResponseSyntax"></a>

```
{
   "AssociationId": "string",
   "DeleteDataInFileSystem": boolean,
   "Lifecycle": "string"
}
```

## Response Elements
<a name="API_DeleteDataRepositoryAssociation_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [AssociationId](#API_DeleteDataRepositoryAssociation_ResponseSyntax) **   <a name="FSx-DeleteDataRepositoryAssociation-response-AssociationId"></a>
The ID of the data repository association being deleted.  
Type: String  
Length Constraints: Minimum length of 13. Maximum length of 23.  
Pattern: `^(dra-[0-9a-f]{8,})$` 

 ** [DeleteDataInFileSystem](#API_DeleteDataRepositoryAssociation_ResponseSyntax) **   <a name="FSx-DeleteDataRepositoryAssociation-response-DeleteDataInFileSystem"></a>
Indicates whether data in the file system that corresponds to the data repository association is being deleted. Default is `false`.  
Type: Boolean

 ** [Lifecycle](#API_DeleteDataRepositoryAssociation_ResponseSyntax) **   <a name="FSx-DeleteDataRepositoryAssociation-response-Lifecycle"></a>
Describes the lifecycle state of the data repository association being deleted.  
Type: String  
Valid Values: `CREATING | AVAILABLE | MISCONFIGURED | UPDATING | DELETING | FAILED` 

## Errors
<a name="API_DeleteDataRepositoryAssociation_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** BadRequest **   
A generic error indicating a failure with a client request.    
 ** Message **   
A detailed error message.
HTTP Status Code: 400

 ** DataRepositoryAssociationNotFound **   
No data repository associations were found based upon the supplied parameters.    
 ** Message **   
A detailed error message.
HTTP Status Code: 400

 ** IncompatibleParameterError **   
The error returned when a second request is received with the same client request token but different parameters settings. A client request token should always uniquely identify a single request.    
 ** Message **   
A detailed error message.  
 ** Parameter **   
A parameter that is incompatible with the earlier request.
HTTP Status Code: 400

 ** InternalServerError **   
A generic error indicating a server-side failure.    
 ** Message **   
A detailed error message.
HTTP Status Code: 500

 ** ServiceLimitExceeded **   
An error indicating that a particular service limit was exceeded. You can increase some service limits by contacting AWS Support.    
 ** Limit **   
Enumeration of the service limit that was exceeded.   
 ** Message **   
A detailed error message.
HTTP Status Code: 400

## See Also
<a name="API_DeleteDataRepositoryAssociation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/fsx-2018-03-01/DeleteDataRepositoryAssociation) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/fsx-2018-03-01/DeleteDataRepositoryAssociation) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/fsx-2018-03-01/DeleteDataRepositoryAssociation) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/fsx-2018-03-01/DeleteDataRepositoryAssociation) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/fsx-2018-03-01/DeleteDataRepositoryAssociation) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/fsx-2018-03-01/DeleteDataRepositoryAssociation) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/fsx-2018-03-01/DeleteDataRepositoryAssociation) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/fsx-2018-03-01/DeleteDataRepositoryAssociation) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/fsx-2018-03-01/DeleteDataRepositoryAssociation) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/fsx-2018-03-01/DeleteDataRepositoryAssociation) 