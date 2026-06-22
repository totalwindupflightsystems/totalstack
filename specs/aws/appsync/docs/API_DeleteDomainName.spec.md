---
id: "@specs/aws/appsync/docs/API_DeleteDomainName"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS DeleteDomainName"
status: active
depends_on:
  - "@specs/aws/appsync/meta"
---

# DeleteDomainName

> **source:** AWS Documentation
> **spec:id:** @specs/aws/appsync/docs/API_DeleteDomainName
> **target_lang:** meta — documentation tier. ALL sections preserved.



# DeleteDomainName
<a name="API_DeleteDomainName"></a>

Deletes a custom `DomainName` object.

## Request Syntax
<a name="API_DeleteDomainName_RequestSyntax"></a>

```
DELETE /v1/domainnames/{{domainName}} HTTP/1.1
```

## URI Request Parameters
<a name="API_DeleteDomainName_RequestParameters"></a>

The request uses the following URI parameters.

 ** [domainName](#API_DeleteDomainName_RequestSyntax) **   <a name="appsync-DeleteDomainName-request-uri-domainName"></a>
The domain name.  
Length Constraints: Minimum length of 1. Maximum length of 253.  
Pattern: `^(\*[\w\d-]*\.)?([\w\d-]+\.)+[\w\d-]+$`   
Required: Yes

## Request Body
<a name="API_DeleteDomainName_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_DeleteDomainName_ResponseSyntax"></a>

```
HTTP/1.1 200
```

## Response Elements
<a name="API_DeleteDomainName_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_DeleteDomainName_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **   
You don't have access to perform this operation on this resource.  
HTTP Status Code: 403

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

## See Also
<a name="API_DeleteDomainName_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/appsync-2017-07-25/DeleteDomainName) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/appsync-2017-07-25/DeleteDomainName) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/appsync-2017-07-25/DeleteDomainName) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/appsync-2017-07-25/DeleteDomainName) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/appsync-2017-07-25/DeleteDomainName) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/appsync-2017-07-25/DeleteDomainName) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/appsync-2017-07-25/DeleteDomainName) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/appsync-2017-07-25/DeleteDomainName) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/appsync-2017-07-25/DeleteDomainName) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/appsync-2017-07-25/DeleteDomainName) 