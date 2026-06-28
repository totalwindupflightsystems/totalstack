---
id: "@specs/aws/quicksight/docs/API_CreateTemplateAlias"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS CreateTemplateAlias"
status: active
depends_on:
  - "@specs/aws/quicksight/meta"
---

# CreateTemplateAlias

> **source:** AWS Documentation
> **spec:id:** @specs/aws/quicksight/docs/API_CreateTemplateAlias
> **target_lang:** meta — documentation tier. ALL sections preserved.



# CreateTemplateAlias
<a name="API_CreateTemplateAlias"></a>

Creates a template alias for a template.

## Request Syntax
<a name="API_CreateTemplateAlias_RequestSyntax"></a>

```
POST /accounts/{{AwsAccountId}}/templates/{{TemplateId}}/aliases/{{AliasName}} HTTP/1.1
Content-type: application/json

{
   "TemplateVersionNumber": {{number}}
}
```

## URI Request Parameters
<a name="API_CreateTemplateAlias_RequestParameters"></a>

The request uses the following URI parameters.

 ** [AliasName](#API_CreateTemplateAlias_RequestSyntax) **   <a name="QS-CreateTemplateAlias-request-uri-AliasName"></a>
The name that you want to give to the template alias that you're creating. Don't start the alias name with the `$` character. Alias names that start with `$` are reserved by Quick Sight.   
Length Constraints: Minimum length of 1. Maximum length of 2048.  
Pattern: `[\w\-]+|(\$LATEST)|(\$PUBLISHED)`   
Required: Yes

 ** [AwsAccountId](#API_CreateTemplateAlias_RequestSyntax) **   <a name="QS-CreateTemplateAlias-request-uri-AwsAccountId"></a>
The ID of the AWS account that contains the template that you creating an alias for.  
Length Constraints: Fixed length of 12.  
Pattern: `^[0-9]{12}$`   
Required: Yes

 ** [TemplateId](#API_CreateTemplateAlias_RequestSyntax) **   <a name="QS-CreateTemplateAlias-request-uri-TemplateId"></a>
An ID for the template.  
Length Constraints: Minimum length of 1. Maximum length of 512.  
Pattern: `[\w\-]+`   
Required: Yes

## Request Body
<a name="API_CreateTemplateAlias_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [TemplateVersionNumber](#API_CreateTemplateAlias_RequestSyntax) **   <a name="QS-CreateTemplateAlias-request-TemplateVersionNumber"></a>
The version number of the template.  
Type: Long  
Valid Range: Minimum value of 1.  
Required: Yes

## Response Syntax
<a name="API_CreateTemplateAlias_ResponseSyntax"></a>

```
HTTP/1.1 {{Status}}
Content-type: application/json

{
   "RequestId": "string",
   "TemplateAlias": { 
      "AliasName": "string",
      "Arn": "string",
      "TemplateVersionNumber": number
   }
}
```

## Response Elements
<a name="API_CreateTemplateAlias_ResponseElements"></a>

If the action is successful, the service sends back the following HTTP response.

 ** [Status](#API_CreateTemplateAlias_ResponseSyntax) **   <a name="QS-CreateTemplateAlias-response-Status"></a>
The HTTP status of the request.

The following data is returned in JSON format by the service.

 ** [RequestId](#API_CreateTemplateAlias_ResponseSyntax) **   <a name="QS-CreateTemplateAlias-response-RequestId"></a>
The AWS request ID for this operation.  
Type: String

 ** [TemplateAlias](#API_CreateTemplateAlias_ResponseSyntax) **   <a name="QS-CreateTemplateAlias-response-TemplateAlias"></a>
Information about the template alias.  
Type: [TemplateAlias](API_TemplateAlias.md) object

## Errors
<a name="API_CreateTemplateAlias_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ConflictException **   
Updating or deleting a resource can cause an inconsistent state.    
 ** RequestId **   
The AWS request ID for this request.
HTTP Status Code: 409

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

 ** LimitExceededException **   
A limit is exceeded.    
 ** RequestId **   
The AWS request ID for this request.  
 ** ResourceType **   
Limit exceeded.
HTTP Status Code: 409

 ** ResourceExistsException **   
The resource specified already exists.     
 ** RequestId **   
The AWS request ID for this request.  
 ** ResourceType **   
The resource type for this request.
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
<a name="API_CreateTemplateAlias_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/quicksight-2018-04-01/CreateTemplateAlias) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/quicksight-2018-04-01/CreateTemplateAlias) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/CreateTemplateAlias) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/quicksight-2018-04-01/CreateTemplateAlias) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/CreateTemplateAlias) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/quicksight-2018-04-01/CreateTemplateAlias) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/quicksight-2018-04-01/CreateTemplateAlias) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/quicksight-2018-04-01/CreateTemplateAlias) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/quicksight-2018-04-01/CreateTemplateAlias) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/CreateTemplateAlias) 