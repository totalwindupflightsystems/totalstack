---
id: "@specs/aws/fsx/docs/API_DeleteStorageVirtualMachine"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS DeleteStorageVirtualMachine"
status: active
depends_on:
  - "@specs/aws/fsx/meta"
---

# DeleteStorageVirtualMachine

> **source:** AWS Documentation
> **spec:id:** @specs/aws/fsx/docs/API_DeleteStorageVirtualMachine
> **target_lang:** meta — documentation tier. ALL sections preserved.



# DeleteStorageVirtualMachine
<a name="API_DeleteStorageVirtualMachine"></a>

Deletes an existing Amazon FSx for ONTAP storage virtual machine (SVM). Prior to deleting an SVM, you must delete all non-root volumes in the SVM, otherwise the operation will fail.

## Request Syntax
<a name="API_DeleteStorageVirtualMachine_RequestSyntax"></a>

```
{
   "ClientRequestToken": "{{string}}",
   "StorageVirtualMachineId": "{{string}}"
}
```

## Request Parameters
<a name="API_DeleteStorageVirtualMachine_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [ClientRequestToken](#API_DeleteStorageVirtualMachine_RequestSyntax) **   <a name="FSx-DeleteStorageVirtualMachine-request-ClientRequestToken"></a>
(Optional) An idempotency token for resource creation, in a string of up to 63 ASCII characters. This token is automatically filled on your behalf when you use the AWS Command Line Interface (AWS CLI) or an AWS SDK.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 63.  
Pattern: `[A-za-z0-9_.-]{0,63}$`   
Required: No

 ** [StorageVirtualMachineId](#API_DeleteStorageVirtualMachine_RequestSyntax) **   <a name="FSx-DeleteStorageVirtualMachine-request-StorageVirtualMachineId"></a>
The ID of the SVM that you want to delete.  
Type: String  
Length Constraints: Fixed length of 21.  
Pattern: `^(svm-[0-9a-f]{17,})$`   
Required: Yes

## Response Syntax
<a name="API_DeleteStorageVirtualMachine_ResponseSyntax"></a>

```
{
   "Lifecycle": "string",
   "StorageVirtualMachineId": "string"
}
```

## Response Elements
<a name="API_DeleteStorageVirtualMachine_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Lifecycle](#API_DeleteStorageVirtualMachine_ResponseSyntax) **   <a name="FSx-DeleteStorageVirtualMachine-response-Lifecycle"></a>
Describes the lifecycle state of the SVM being deleted.  
Type: String  
Valid Values: `CREATED | CREATING | DELETING | FAILED | MISCONFIGURED | PENDING` 

 ** [StorageVirtualMachineId](#API_DeleteStorageVirtualMachine_ResponseSyntax) **   <a name="FSx-DeleteStorageVirtualMachine-response-StorageVirtualMachineId"></a>
The ID of the SVM Amazon FSx is deleting.  
Type: String  
Length Constraints: Fixed length of 21.  
Pattern: `^(svm-[0-9a-f]{17,})$` 

## Errors
<a name="API_DeleteStorageVirtualMachine_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** BadRequest **   
A generic error indicating a failure with a client request.    
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

 ** StorageVirtualMachineNotFound **   
No FSx for ONTAP SVMs were found based upon the supplied parameters.    
 ** Message **   
A detailed error message.
HTTP Status Code: 400

## See Also
<a name="API_DeleteStorageVirtualMachine_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/fsx-2018-03-01/DeleteStorageVirtualMachine) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/fsx-2018-03-01/DeleteStorageVirtualMachine) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/fsx-2018-03-01/DeleteStorageVirtualMachine) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/fsx-2018-03-01/DeleteStorageVirtualMachine) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/fsx-2018-03-01/DeleteStorageVirtualMachine) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/fsx-2018-03-01/DeleteStorageVirtualMachine) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/fsx-2018-03-01/DeleteStorageVirtualMachine) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/fsx-2018-03-01/DeleteStorageVirtualMachine) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/fsx-2018-03-01/DeleteStorageVirtualMachine) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/fsx-2018-03-01/DeleteStorageVirtualMachine) 