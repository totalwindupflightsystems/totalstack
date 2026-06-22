---
id: "@specs/aws/sesv2/docs/API_DeleteTenant"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS DeleteTenant"
status: active
depends_on:
  - "@specs/aws/sesv2/meta"
---

# DeleteTenant

> **source:** AWS Documentation
> **spec:id:** @specs/aws/sesv2/docs/API_DeleteTenant
> **target_lang:** meta — documentation tier. ALL sections preserved.



# DeleteTenant
<a name="API_DeleteTenant"></a>

Delete an existing tenant.

When you delete a tenant, its associations with resources are removed, but the resources themselves are not deleted.

## Request Syntax
<a name="API_DeleteTenant_RequestSyntax"></a>

```
POST /v2/email/tenants/delete HTTP/1.1
Content-type: application/json

{
   "TenantName": "{{string}}"
}
```

## URI Request Parameters
<a name="API_DeleteTenant_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_DeleteTenant_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [TenantName](#API_DeleteTenant_RequestSyntax) **   <a name="SES-DeleteTenant-request-TenantName"></a>
The name of the tenant to delete.  
Type: String  
Length Constraints: Minimum length of 1.  
Required: Yes

## Response Syntax
<a name="API_DeleteTenant_ResponseSyntax"></a>

```
HTTP/1.1 200
```

## Response Elements
<a name="API_DeleteTenant_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_DeleteTenant_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** BadRequestException **   
The input you provided is invalid.  
HTTP Status Code: 400

 ** NotFoundException **   
The resource you attempted to access doesn't exist.  
HTTP Status Code: 404

 ** TooManyRequestsException **   
Too many requests have been made to the operation.  
HTTP Status Code: 429

## See Also
<a name="API_DeleteTenant_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/sesv2-2019-09-27/DeleteTenant) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/sesv2-2019-09-27/DeleteTenant) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sesv2-2019-09-27/DeleteTenant) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/sesv2-2019-09-27/DeleteTenant) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sesv2-2019-09-27/DeleteTenant) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/sesv2-2019-09-27/DeleteTenant) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/sesv2-2019-09-27/DeleteTenant) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/sesv2-2019-09-27/DeleteTenant) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/sesv2-2019-09-27/DeleteTenant) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sesv2-2019-09-27/DeleteTenant) 