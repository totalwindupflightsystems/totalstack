---
id: "@specs/aws/sesv2/docs/API_ListTenants"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS ListTenants"
status: active
depends_on:
  - "@specs/aws/sesv2/meta"
---

# ListTenants

> **source:** AWS Documentation
> **spec:id:** @specs/aws/sesv2/docs/API_ListTenants
> **target_lang:** meta — documentation tier. ALL sections preserved.



# ListTenants
<a name="API_ListTenants"></a>

List all tenants associated with your account in the current AWS Region.

This operation returns basic information about each tenant, such as tenant name, ID, ARN, and creation timestamp.

## Request Syntax
<a name="API_ListTenants_RequestSyntax"></a>

```
POST /v2/email/tenants/list HTTP/1.1
Content-type: application/json

{
   "NextToken": "{{string}}",
   "PageSize": {{number}}
}
```

## URI Request Parameters
<a name="API_ListTenants_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_ListTenants_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [NextToken](#API_ListTenants_RequestSyntax) **   <a name="SES-ListTenants-request-NextToken"></a>
A token returned from a previous call to `ListTenants` to indicate the position in the list of tenants.  
Type: String  
Required: No

 ** [PageSize](#API_ListTenants_RequestSyntax) **   <a name="SES-ListTenants-request-PageSize"></a>
The number of results to show in a single call to `ListTenants`. If the number of results is larger than the number you specified in this parameter, then the response includes a `NextToken` element, which you can use to obtain additional results.  
Type: Integer  
Required: No

## Response Syntax
<a name="API_ListTenants_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "NextToken": "string",
   "Tenants": [ 
      { 
         "CreatedTimestamp": number,
         "TenantArn": "string",
         "TenantId": "string",
         "TenantName": "string"
      }
   ]
}
```

## Response Elements
<a name="API_ListTenants_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [NextToken](#API_ListTenants_ResponseSyntax) **   <a name="SES-ListTenants-response-NextToken"></a>
A token that indicates that there are additional tenants to list. To view additional tenants, issue another request to `ListTenants`, and pass this token in the `NextToken` parameter.  
Type: String

 ** [Tenants](#API_ListTenants_ResponseSyntax) **   <a name="SES-ListTenants-response-Tenants"></a>
An array that contains basic information about each tenant.  
Type: Array of [TenantInfo](API_TenantInfo.md) objects

## Errors
<a name="API_ListTenants_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** BadRequestException **   
The input you provided is invalid.  
HTTP Status Code: 400

 ** TooManyRequestsException **   
Too many requests have been made to the operation.  
HTTP Status Code: 429

## See Also
<a name="API_ListTenants_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/sesv2-2019-09-27/ListTenants) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/sesv2-2019-09-27/ListTenants) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sesv2-2019-09-27/ListTenants) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/sesv2-2019-09-27/ListTenants) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sesv2-2019-09-27/ListTenants) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/sesv2-2019-09-27/ListTenants) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/sesv2-2019-09-27/ListTenants) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/sesv2-2019-09-27/ListTenants) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/sesv2-2019-09-27/ListTenants) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sesv2-2019-09-27/ListTenants) 