---
id: "@specs/aws/quicksight/docs/API_DeleteAccountCustomization"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS DeleteAccountCustomization"
status: active
depends_on:
  - "@specs/aws/quicksight/meta"
---

# DeleteAccountCustomization

> **source:** AWS Documentation
> **spec:id:** @specs/aws/quicksight/docs/API_DeleteAccountCustomization
> **target_lang:** meta — documentation tier. ALL sections preserved.



# DeleteAccountCustomization
<a name="API_DeleteAccountCustomization"></a>

**Important**  
This API permanently deletes all Quick Sight customizations for the specified AWS account and namespace. When you delete account customizations:  
All customizations are removed including themes, branding, and visual settings
This action cannot be undone through the API
Users will see default Quick Sight styling after customizations are deleted
 **Before proceeding:** Ensure you have backups of any custom themes or branding elements you may want to recreate.

Deletes all Amazon Quick Sight customizations for the specified AWS account and Quick Sight namespace.

## Request Syntax
<a name="API_DeleteAccountCustomization_RequestSyntax"></a>

```
DELETE /accounts/{{AwsAccountId}}/customizations?namespace={{Namespace}} HTTP/1.1
```

## URI Request Parameters
<a name="API_DeleteAccountCustomization_RequestParameters"></a>

The request uses the following URI parameters.

 ** [AwsAccountId](#API_DeleteAccountCustomization_RequestSyntax) **   <a name="QS-DeleteAccountCustomization-request-uri-AwsAccountId"></a>
The ID for the AWS account that you want to delete Quick Sight customizations from.  
Length Constraints: Fixed length of 12.  
Pattern: `^[0-9]{12}$`   
Required: Yes

 ** [Namespace](#API_DeleteAccountCustomization_RequestSyntax) **   <a name="QS-DeleteAccountCustomization-request-uri-Namespace"></a>
The Quick Sight namespace that you're deleting the customizations from.  
Length Constraints: Maximum length of 64.  
Pattern: `^[a-zA-Z0-9._-]*$` 

## Request Body
<a name="API_DeleteAccountCustomization_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_DeleteAccountCustomization_ResponseSyntax"></a>

```
HTTP/1.1 {{Status}}
Content-type: application/json

{
   "RequestId": "string"
}
```

## Response Elements
<a name="API_DeleteAccountCustomization_ResponseElements"></a>

If the action is successful, the service sends back the following HTTP response.

 ** [Status](#API_DeleteAccountCustomization_ResponseSyntax) **   <a name="QS-DeleteAccountCustomization-response-Status"></a>
The HTTP status of the request.

The following data is returned in JSON format by the service.

 ** [RequestId](#API_DeleteAccountCustomization_ResponseSyntax) **   <a name="QS-DeleteAccountCustomization-response-RequestId"></a>
The AWS request ID for this operation.  
Type: String

## Errors
<a name="API_DeleteAccountCustomization_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **   
You don't have access to this item. The provided credentials couldn't be validated. You might not be authorized to carry out the request. Make sure that your account is authorized to use the Amazon Quick Sight service, that your policies have the correct permissions, and that you are using the correct credentials.    
 ** RequestId **   
The AWS request ID for this request.
HTTP Status Code: 401

 ** ConflictException **   
Updating or deleting a resource can cause an inconsistent state.    
 ** RequestId **   
The AWS request ID for this request.
HTTP Status Code: 409

 ** InternalFailureException **   
An internal failure occurred.    
 ** RequestId **   
The AWS request ID for this request.
HTTP Status Code: 500

 ** InvalidParameterValueException **   
One or more parameters has a value that isn't valid.    
 ** RequestId **   
The AWS request ID for this request.
HTTP Status Code: 400

 ** LimitExceededException **   
A limit is exceeded.    
 ** RequestId **   
The AWS request ID for this request.  
 ** ResourceType **   
Limit exceeded.
HTTP Status Code: 409

 ** PreconditionNotMetException **   
One or more preconditions aren't met.    
 ** RequestId **   
The AWS request ID for this request.
HTTP Status Code: 400

 ** ResourceNotFoundException **   
One or more resources can't be found.    
 ** RequestId **   
The AWS request ID for this request.  
 ** ResourceType **   
The resource type for this request.
HTTP Status Code: 404

 ** ResourceUnavailableException **   
This resource is currently unavailable.    
 ** RequestId **   
The AWS request ID for this request.  
 ** ResourceType **   
The resource type for this request.
HTTP Status Code: 503

 ** ThrottlingException **   
Access is throttled.    
 ** RequestId **   
The AWS request ID for this request.
HTTP Status Code: 429

## See Also
<a name="API_DeleteAccountCustomization_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/quicksight-2018-04-01/DeleteAccountCustomization) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/quicksight-2018-04-01/DeleteAccountCustomization) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/DeleteAccountCustomization) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/quicksight-2018-04-01/DeleteAccountCustomization) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/DeleteAccountCustomization) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/quicksight-2018-04-01/DeleteAccountCustomization) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/quicksight-2018-04-01/DeleteAccountCustomization) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/quicksight-2018-04-01/DeleteAccountCustomization) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/quicksight-2018-04-01/DeleteAccountCustomization) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/DeleteAccountCustomization) 