---
id: "@specs/aws/quicksight/docs/API_DeleteTemplateAlias"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS DeleteTemplateAlias"
status: active
depends_on:
  - "@specs/aws/quicksight/meta"
---

# DeleteTemplateAlias

> **source:** AWS Documentation
> **spec:id:** @specs/aws/quicksight/docs/API_DeleteTemplateAlias
> **target_lang:** meta — documentation tier. ALL sections preserved.



# DeleteTemplateAlias
<a name="API_DeleteTemplateAlias"></a>

Deletes the item that the specified template alias points to. If you provide a specific alias, you delete the version of the template that the alias points to.

## Request Syntax
<a name="API_DeleteTemplateAlias_RequestSyntax"></a>

```
DELETE /accounts/{{AwsAccountId}}/templates/{{TemplateId}}/aliases/{{AliasName}} HTTP/1.1
```

## URI Request Parameters
<a name="API_DeleteTemplateAlias_RequestParameters"></a>

The request uses the following URI parameters.

 ** [AliasName](#API_DeleteTemplateAlias_RequestSyntax) **   <a name="QS-DeleteTemplateAlias-request-uri-AliasName"></a>
The name for the template alias. To delete a specific alias, you delete the version that the alias points to. You can specify the alias name, or specify the latest version of the template by providing the keyword `$LATEST` in the `AliasName` parameter.   
Length Constraints: Minimum length of 1. Maximum length of 2048.  
Pattern: `[\w\-]+|(\$LATEST)|(\$PUBLISHED)`   
Required: Yes

 ** [AwsAccountId](#API_DeleteTemplateAlias_RequestSyntax) **   <a name="QS-DeleteTemplateAlias-request-uri-AwsAccountId"></a>
The ID of the AWS account that contains the item to delete.  
Length Constraints: Fixed length of 12.  
Pattern: `^[0-9]{12}$`   
Required: Yes

 ** [TemplateId](#API_DeleteTemplateAlias_RequestSyntax) **   <a name="QS-DeleteTemplateAlias-request-uri-TemplateId"></a>
The ID for the template that the specified alias is for.  
Length Constraints: Minimum length of 1. Maximum length of 512.  
Pattern: `[\w\-]+`   
Required: Yes

## Request Body
<a name="API_DeleteTemplateAlias_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_DeleteTemplateAlias_ResponseSyntax"></a>

```
HTTP/1.1 {{Status}}
Content-type: application/json

{
   "AliasName": "string",
   "Arn": "string",
   "RequestId": "string",
   "TemplateId": "string"
}
```

## Response Elements
<a name="API_DeleteTemplateAlias_ResponseElements"></a>

If the action is successful, the service sends back the following HTTP response.

 ** [Status](#API_DeleteTemplateAlias_ResponseSyntax) **   <a name="QS-DeleteTemplateAlias-response-Status"></a>
The HTTP status of the request.

The following data is returned in JSON format by the service.

 ** [AliasName](#API_DeleteTemplateAlias_ResponseSyntax) **   <a name="QS-DeleteTemplateAlias-response-AliasName"></a>
The name for the template alias.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 2048.  
Pattern: `[\w\-]+|(\$LATEST)|(\$PUBLISHED)` 

 ** [Arn](#API_DeleteTemplateAlias_ResponseSyntax) **   <a name="QS-DeleteTemplateAlias-response-Arn"></a>
The Amazon Resource Name (ARN) of the template you want to delete.  
Type: String

 ** [RequestId](#API_DeleteTemplateAlias_ResponseSyntax) **   <a name="QS-DeleteTemplateAlias-response-RequestId"></a>
The AWS request ID for this operation.  
Type: String

 ** [TemplateId](#API_DeleteTemplateAlias_ResponseSyntax) **   <a name="QS-DeleteTemplateAlias-response-TemplateId"></a>
An ID for the template associated with the deletion.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 512.  
Pattern: `[\w\-]+` 

## Errors
<a name="API_DeleteTemplateAlias_Errors"></a>

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
<a name="API_DeleteTemplateAlias_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/quicksight-2018-04-01/DeleteTemplateAlias) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/quicksight-2018-04-01/DeleteTemplateAlias) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/DeleteTemplateAlias) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/quicksight-2018-04-01/DeleteTemplateAlias) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/DeleteTemplateAlias) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/quicksight-2018-04-01/DeleteTemplateAlias) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/quicksight-2018-04-01/DeleteTemplateAlias) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/quicksight-2018-04-01/DeleteTemplateAlias) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/quicksight-2018-04-01/DeleteTemplateAlias) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/DeleteTemplateAlias) 