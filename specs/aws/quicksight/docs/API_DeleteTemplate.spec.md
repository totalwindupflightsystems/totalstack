---
id: "@specs/aws/quicksight/docs/API_DeleteTemplate"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS DeleteTemplate"
status: active
depends_on:
  - "@specs/aws/quicksight/meta"
---

# DeleteTemplate

> **source:** AWS Documentation
> **spec:id:** @specs/aws/quicksight/docs/API_DeleteTemplate
> **target_lang:** meta — documentation tier. ALL sections preserved.



# DeleteTemplate
<a name="API_DeleteTemplate"></a>

Deletes a template.

## Request Syntax
<a name="API_DeleteTemplate_RequestSyntax"></a>

```
DELETE /accounts/{{AwsAccountId}}/templates/{{TemplateId}}?version-number={{VersionNumber}} HTTP/1.1
```

## URI Request Parameters
<a name="API_DeleteTemplate_RequestParameters"></a>

The request uses the following URI parameters.

 ** [AwsAccountId](#API_DeleteTemplate_RequestSyntax) **   <a name="QS-DeleteTemplate-request-uri-AwsAccountId"></a>
The ID of the AWS account that contains the template that you're deleting.  
Length Constraints: Fixed length of 12.  
Pattern: `^[0-9]{12}$`   
Required: Yes

 ** [TemplateId](#API_DeleteTemplate_RequestSyntax) **   <a name="QS-DeleteTemplate-request-uri-TemplateId"></a>
An ID for the template you want to delete.  
Length Constraints: Minimum length of 1. Maximum length of 512.  
Pattern: `[\w\-]+`   
Required: Yes

 ** [VersionNumber](#API_DeleteTemplate_RequestSyntax) **   <a name="QS-DeleteTemplate-request-uri-VersionNumber"></a>
Specifies the version of the template that you want to delete. If you don't provide a version number, `DeleteTemplate` deletes all versions of the template.   
Valid Range: Minimum value of 1.

## Request Body
<a name="API_DeleteTemplate_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_DeleteTemplate_ResponseSyntax"></a>

```
HTTP/1.1 {{Status}}
Content-type: application/json

{
   "Arn": "string",
   "RequestId": "string",
   "TemplateId": "string"
}
```

## Response Elements
<a name="API_DeleteTemplate_ResponseElements"></a>

If the action is successful, the service sends back the following HTTP response.

 ** [Status](#API_DeleteTemplate_ResponseSyntax) **   <a name="QS-DeleteTemplate-response-Status"></a>
The HTTP status of the request.

The following data is returned in JSON format by the service.

 ** [Arn](#API_DeleteTemplate_ResponseSyntax) **   <a name="QS-DeleteTemplate-response-Arn"></a>
The Amazon Resource Name (ARN) of the resource.  
Type: String

 ** [RequestId](#API_DeleteTemplate_ResponseSyntax) **   <a name="QS-DeleteTemplate-response-RequestId"></a>
The AWS request ID for this operation.  
Type: String

 ** [TemplateId](#API_DeleteTemplate_ResponseSyntax) **   <a name="QS-DeleteTemplate-response-TemplateId"></a>
An ID for the template.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 512.  
Pattern: `[\w\-]+` 

## Errors
<a name="API_DeleteTemplate_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

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

 ** ResourceNotFoundException **   
One or more resources can't be found.    
 ** RequestId **   
The AWS request ID for this request.  
 ** ResourceType **   
The resource type for this request.
HTTP Status Code: 404

 ** ThrottlingException **   
Access is throttled.    
 ** RequestId **   
The AWS request ID for this request.
HTTP Status Code: 429

 ** UnsupportedUserEditionException **   
This error indicates that you are calling an operation on an Amazon Quick Suite subscription where the edition doesn't include support for that operation. Amazon Quick Suite currently has Standard Edition and Enterprise Edition. Not every operation and capability is available in every edition.    
 ** RequestId **   
The AWS request ID for this request.
HTTP Status Code: 403

## See Also
<a name="API_DeleteTemplate_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/quicksight-2018-04-01/DeleteTemplate) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/quicksight-2018-04-01/DeleteTemplate) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/DeleteTemplate) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/quicksight-2018-04-01/DeleteTemplate) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/DeleteTemplate) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/quicksight-2018-04-01/DeleteTemplate) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/quicksight-2018-04-01/DeleteTemplate) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/quicksight-2018-04-01/DeleteTemplate) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/quicksight-2018-04-01/DeleteTemplate) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/DeleteTemplate) 