---
id: "@specs/aws/appsync/docs/API_UpdateType"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS UpdateType"
status: active
depends_on:
  - "@specs/aws/appsync/meta"
---

# UpdateType

> **source:** AWS Documentation
> **spec:id:** @specs/aws/appsync/docs/API_UpdateType
> **target_lang:** meta — documentation tier. ALL sections preserved.



# UpdateType
<a name="API_UpdateType"></a>

Updates a `Type` object.

## Request Syntax
<a name="API_UpdateType_RequestSyntax"></a>

```
POST /v1/apis/{{apiId}}/types/{{typeName}} HTTP/1.1
Content-type: application/json

{
   "definition": "{{string}}",
   "format": "{{string}}"
}
```

## URI Request Parameters
<a name="API_UpdateType_RequestParameters"></a>

The request uses the following URI parameters.

 ** [apiId](#API_UpdateType_RequestSyntax) **   <a name="appsync-UpdateType-request-uri-apiId"></a>
The API ID.  
Required: Yes

 ** [typeName](#API_UpdateType_RequestSyntax) **   <a name="appsync-UpdateType-request-uri-typeName"></a>
The new type name.  
Length Constraints: Minimum length of 1. Maximum length of 65536.  
Pattern: `[_A-Za-z][_0-9A-Za-z]*`   
Required: Yes

## Request Body
<a name="API_UpdateType_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [definition](#API_UpdateType_RequestSyntax) **   <a name="appsync-UpdateType-request-definition"></a>
The new definition.  
Type: String  
Required: No

 ** [format](#API_UpdateType_RequestSyntax) **   <a name="appsync-UpdateType-request-format"></a>
The new type format: SDL or JSON.  
Type: String  
Valid Values: `SDL | JSON`   
Required: Yes

## Response Syntax
<a name="API_UpdateType_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "type": { 
      "arn": "string",
      "definition": "string",
      "description": "string",
      "format": "string",
      "name": "string"
   }
}
```

## Response Elements
<a name="API_UpdateType_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [type](#API_UpdateType_ResponseSyntax) **   <a name="appsync-UpdateType-response-type"></a>
The updated `Type` object.  
Type: [Type](API_Type.md) object

## Errors
<a name="API_UpdateType_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** BadRequestException **   
The request is not well formed. For example, a value is invalid or a required field is missing. Check the field values, and then try again.    
 ** detail **   
Provides further details for the reason behind the bad request. For reason type `CODE_ERROR`, the detail will contain a list of code errors.  
 ** reason **   
Provides context for the cause of the bad request. The only supported value is `CODE_ERROR`.
HTTP Status Code: 400

 ** ConcurrentModificationException **   
Another modification is in progress at this time and it must complete before you can make your change.  
HTTP Status Code: 409

 ** InternalFailureException **   
An internal AWS AppSync error occurred. Try your request again.  
HTTP Status Code: 500

 ** NotFoundException **   
The resource specified in the request was not found. Check the resource, and then try again.  
HTTP Status Code: 404

 ** UnauthorizedException **   
You aren't authorized to perform this operation.  
HTTP Status Code: 401

## See Also
<a name="API_UpdateType_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/appsync-2017-07-25/UpdateType) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/appsync-2017-07-25/UpdateType) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/appsync-2017-07-25/UpdateType) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/appsync-2017-07-25/UpdateType) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/appsync-2017-07-25/UpdateType) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/appsync-2017-07-25/UpdateType) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/appsync-2017-07-25/UpdateType) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/appsync-2017-07-25/UpdateType) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/appsync-2017-07-25/UpdateType) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/appsync-2017-07-25/UpdateType) 