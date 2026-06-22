---
id: "@specs/aws/sesv2/docs/API_CreateTenantResourceAssociation"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS CreateTenantResourceAssociation"
status: active
depends_on:
  - "@specs/aws/sesv2/meta"
---

# CreateTenantResourceAssociation

> **source:** AWS Documentation
> **spec:id:** @specs/aws/sesv2/docs/API_CreateTenantResourceAssociation
> **target_lang:** meta — documentation tier. ALL sections preserved.



# CreateTenantResourceAssociation
<a name="API_CreateTenantResourceAssociation"></a>

Associate a resource with a tenant.

 *Resources* can be email identities, configuration sets, or email templates. When you associate a resource with a tenant, you can use that resource when sending emails on behalf of that tenant.

A single resource can be associated with multiple tenants, allowing for resource sharing across different tenants while maintaining isolation in email sending operations.

## Request Syntax
<a name="API_CreateTenantResourceAssociation_RequestSyntax"></a>

```
POST /v2/email/tenants/resources HTTP/1.1
Content-type: application/json

{
   "ResourceArn": "{{string}}",
   "TenantName": "{{string}}"
}
```

## URI Request Parameters
<a name="API_CreateTenantResourceAssociation_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_CreateTenantResourceAssociation_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [ResourceArn](#API_CreateTenantResourceAssociation_RequestSyntax) **   <a name="SES-CreateTenantResourceAssociation-request-ResourceArn"></a>
The Amazon Resource Name (ARN) of the resource to associate with the tenant.  
Type: String  
Length Constraints: Minimum length of 1.  
Required: Yes

 ** [TenantName](#API_CreateTenantResourceAssociation_RequestSyntax) **   <a name="SES-CreateTenantResourceAssociation-request-TenantName"></a>
The name of the tenant to associate the resource with.  
Type: String  
Length Constraints: Minimum length of 1.  
Required: Yes

## Response Syntax
<a name="API_CreateTenantResourceAssociation_ResponseSyntax"></a>

```
HTTP/1.1 200
```

## Response Elements
<a name="API_CreateTenantResourceAssociation_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_CreateTenantResourceAssociation_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AlreadyExistsException **   
The resource specified in your request already exists.  
HTTP Status Code: 400

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
<a name="API_CreateTenantResourceAssociation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/sesv2-2019-09-27/CreateTenantResourceAssociation) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/sesv2-2019-09-27/CreateTenantResourceAssociation) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sesv2-2019-09-27/CreateTenantResourceAssociation) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/sesv2-2019-09-27/CreateTenantResourceAssociation) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sesv2-2019-09-27/CreateTenantResourceAssociation) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/sesv2-2019-09-27/CreateTenantResourceAssociation) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/sesv2-2019-09-27/CreateTenantResourceAssociation) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/sesv2-2019-09-27/CreateTenantResourceAssociation) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/sesv2-2019-09-27/CreateTenantResourceAssociation) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sesv2-2019-09-27/CreateTenantResourceAssociation) 