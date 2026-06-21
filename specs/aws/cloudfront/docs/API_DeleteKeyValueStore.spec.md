---
id: "@specs/aws/cloudfront/docs/API_DeleteKeyValueStore"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS DeleteKeyValueStore"
status: active
depends_on:
  - "@specs/aws/cloudfront/meta"
---

# DeleteKeyValueStore

> **source:** AWS Documentation
> **spec:id:** @specs/aws/cloudfront/docs/API_DeleteKeyValueStore
> **target_lang:** meta — documentation tier. ALL sections preserved.



# DeleteKeyValueStore
<a name="API_DeleteKeyValueStore"></a>

Specifies the key value store to delete.

## Request Syntax
<a name="API_DeleteKeyValueStore_RequestSyntax"></a>

```
DELETE /2020-05-31/key-value-store/{{Name}} HTTP/1.1
If-Match: {{IfMatch}}
```

## URI Request Parameters
<a name="API_DeleteKeyValueStore_RequestParameters"></a>

The request uses the following URI parameters.

 ** [If-Match](#API_DeleteKeyValueStore_RequestSyntax) **   <a name="cloudfront-DeleteKeyValueStore-request-IfMatch"></a>
The key value store to delete, if a match occurs.  
Required: Yes

 ** [Name](#API_DeleteKeyValueStore_RequestSyntax) **   <a name="cloudfront-DeleteKeyValueStore-request-uri-Name"></a>
The name of the key value store.  
Length Constraints: Minimum length of 1. Maximum length of 64.  
Pattern: `[a-zA-Z0-9-_]{1,64}`   
Required: Yes

## Request Body
<a name="API_DeleteKeyValueStore_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_DeleteKeyValueStore_ResponseSyntax"></a>

```
HTTP/1.1 204
```

## Response Elements
<a name="API_DeleteKeyValueStore_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 204 response with an empty HTTP body.

## Errors
<a name="API_DeleteKeyValueStore_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDenied **   
Access denied.  
HTTP Status Code: 403

 ** CannotDeleteEntityWhileInUse **   
The entity cannot be deleted while it is in use.  
HTTP Status Code: 409

 ** EntityNotFound **   
The entity was not found.  
HTTP Status Code: 404

 ** InvalidArgument **   
An argument is invalid.  
HTTP Status Code: 400

 ** InvalidIfMatchVersion **   
The `If-Match` version is missing or not valid.  
HTTP Status Code: 400

 ** PreconditionFailed **   
The precondition in one or more of the request fields evaluated to `false`.  
HTTP Status Code: 412

 ** UnsupportedOperation **   
This operation is not supported in this AWS Region.  
HTTP Status Code: 400

## See Also
<a name="API_DeleteKeyValueStore_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/cloudfront-2020-05-31/DeleteKeyValueStore) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/cloudfront-2020-05-31/DeleteKeyValueStore) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cloudfront-2020-05-31/DeleteKeyValueStore) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/cloudfront-2020-05-31/DeleteKeyValueStore) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudfront-2020-05-31/DeleteKeyValueStore) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cloudfront-2020-05-31/DeleteKeyValueStore) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/cloudfront-2020-05-31/DeleteKeyValueStore) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/cloudfront-2020-05-31/DeleteKeyValueStore) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/cloudfront-2020-05-31/DeleteKeyValueStore) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudfront-2020-05-31/DeleteKeyValueStore) 