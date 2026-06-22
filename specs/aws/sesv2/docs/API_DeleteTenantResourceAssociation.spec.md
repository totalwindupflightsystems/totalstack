---
id: "@specs/aws/sesv2/docs/API_DeleteTenantResourceAssociation"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS DeleteTenantResourceAssociation"
status: active
depends_on:
  - "@specs/aws/sesv2/meta"
---

# DeleteTenantResourceAssociation

> **source:** AWS Documentation
> **spec:id:** @specs/aws/sesv2/docs/API_DeleteTenantResourceAssociation
> **target_lang:** meta — documentation tier. ALL sections preserved.



# DeleteTenantResourceAssociation
<a name="API_DeleteTenantResourceAssociation"></a>

Delete an association between a tenant and a resource.

When you delete a tenant-resource association, the resource itself is not deleted, only its association with the specific tenant is removed. After removal, the resource will no longer be available for use with that tenant's email sending operations.

## Request Syntax
<a name="API_DeleteTenantResourceAssociation_RequestSyntax"></a>

```
POST /v2/email/tenants/resources/delete HTTP/1.1
Content-type: application/json

{
   "ResourceArn": "{{string}}",
   "TenantName": "{{string}}"
}
```

## URI Request Parameters
<a name="API_DeleteTenantResourceAssociation_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_DeleteTenantResourceAssociation_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [ResourceArn](#API_DeleteTenantResourceAssociation_RequestSyntax) **   <a name="SES-DeleteTenantResourceAssociation-request-ResourceArn"></a>
The Amazon Resource Name (ARN) of the resource to remove from the tenant association.  
Type: String  
Length Constraints: Minimum length of 1.  
Required: Yes

 ** [TenantName](#API_DeleteTenantResourceAssociation_RequestSyntax) **   <a name="SES-DeleteTenantResourceAssociation-request-TenantName"></a>
The name of the tenant to remove the resource association from.  
Type: String  
Length Constraints: Minimum length of 1.  
Required: Yes

## Response Syntax
<a name="API_DeleteTenantResourceAssociation_ResponseSyntax"></a>

```
HTTP/1.1 200
```

## Response Elements
<a name="API_DeleteTenantResourceAssociation_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_DeleteTenantResourceAssociation_Errors"></a>

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
<a name="API_DeleteTenantResourceAssociation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/sesv2-2019-09-27/DeleteTenantResourceAssociation) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/sesv2-2019-09-27/DeleteTenantResourceAssociation) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sesv2-2019-09-27/DeleteTenantResourceAssociation) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/sesv2-2019-09-27/DeleteTenantResourceAssociation) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sesv2-2019-09-27/DeleteTenantResourceAssociation) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/sesv2-2019-09-27/DeleteTenantResourceAssociation) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/sesv2-2019-09-27/DeleteTenantResourceAssociation) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/sesv2-2019-09-27/DeleteTenantResourceAssociation) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/sesv2-2019-09-27/DeleteTenantResourceAssociation) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sesv2-2019-09-27/DeleteTenantResourceAssociation) 