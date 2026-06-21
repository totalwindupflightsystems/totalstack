---
id: "@specs/aws/cloudfront/docs/API_DeleteAnycastIpList"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS DeleteAnycastIpList"
status: active
depends_on:
  - "@specs/aws/cloudfront/meta"
---

# DeleteAnycastIpList

> **source:** AWS Documentation
> **spec:id:** @specs/aws/cloudfront/docs/API_DeleteAnycastIpList
> **target_lang:** meta — documentation tier. ALL sections preserved.



# DeleteAnycastIpList
<a name="API_DeleteAnycastIpList"></a>

Deletes an Anycast static IP list.

## Request Syntax
<a name="API_DeleteAnycastIpList_RequestSyntax"></a>

```
DELETE /2020-05-31/anycast-ip-list/{{Id}} HTTP/1.1
If-Match: {{IfMatch}}
```

## URI Request Parameters
<a name="API_DeleteAnycastIpList_RequestParameters"></a>

The request uses the following URI parameters.

 ** [Id](#API_DeleteAnycastIpList_RequestSyntax) **   <a name="cloudfront-DeleteAnycastIpList-request-uri-Id"></a>
The ID of the Anycast static IP list.  
Required: Yes

 ** [If-Match](#API_DeleteAnycastIpList_RequestSyntax) **   <a name="cloudfront-DeleteAnycastIpList-request-IfMatch"></a>
The current version (`ETag` value) of the Anycast static IP list that you are deleting.  
Required: Yes

## Request Body
<a name="API_DeleteAnycastIpList_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_DeleteAnycastIpList_ResponseSyntax"></a>

```
HTTP/1.1 204
```

## Response Elements
<a name="API_DeleteAnycastIpList_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 204 response with an empty HTTP body.

## Errors
<a name="API_DeleteAnycastIpList_Errors"></a>

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

 ** IllegalDelete **   
Deletion is not allowed for this entity.  
HTTP Status Code: 400

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
<a name="API_DeleteAnycastIpList_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/cloudfront-2020-05-31/DeleteAnycastIpList) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/cloudfront-2020-05-31/DeleteAnycastIpList) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cloudfront-2020-05-31/DeleteAnycastIpList) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/cloudfront-2020-05-31/DeleteAnycastIpList) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudfront-2020-05-31/DeleteAnycastIpList) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cloudfront-2020-05-31/DeleteAnycastIpList) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/cloudfront-2020-05-31/DeleteAnycastIpList) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/cloudfront-2020-05-31/DeleteAnycastIpList) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/cloudfront-2020-05-31/DeleteAnycastIpList) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudfront-2020-05-31/DeleteAnycastIpList) 