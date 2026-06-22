---
id: "@specs/aws/sesv2/docs/API_ListResourceTenants"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS ListResourceTenants"
status: active
depends_on:
  - "@specs/aws/sesv2/meta"
---

# ListResourceTenants

> **source:** AWS Documentation
> **spec:id:** @specs/aws/sesv2/docs/API_ListResourceTenants
> **target_lang:** meta — documentation tier. ALL sections preserved.



# ListResourceTenants
<a name="API_ListResourceTenants"></a>

List all tenants associated with a specific resource.

This operation returns a list of tenants that are associated with the specified resource. This is useful for understanding which tenants are currently using a particular resource such as an email identity, configuration set, or email template.

## Request Syntax
<a name="API_ListResourceTenants_RequestSyntax"></a>

```
POST /v2/email/resources/tenants/list HTTP/1.1
Content-type: application/json

{
   "NextToken": "{{string}}",
   "PageSize": {{number}},
   "ResourceArn": "{{string}}"
}
```

## URI Request Parameters
<a name="API_ListResourceTenants_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_ListResourceTenants_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [NextToken](#API_ListResourceTenants_RequestSyntax) **   <a name="SES-ListResourceTenants-request-NextToken"></a>
A token returned from a previous call to `ListResourceTenants` to indicate the position in the list of resource tenants.  
Type: String  
Required: No

 ** [PageSize](#API_ListResourceTenants_RequestSyntax) **   <a name="SES-ListResourceTenants-request-PageSize"></a>
The number of results to show in a single call to `ListResourceTenants`. If the number of results is larger than the number you specified in this parameter, then the response includes a `NextToken` element, which you can use to obtain additional results.  
Type: Integer  
Required: No

 ** [ResourceArn](#API_ListResourceTenants_RequestSyntax) **   <a name="SES-ListResourceTenants-request-ResourceArn"></a>
The Amazon Resource Name (ARN) of the resource to list associated tenants for.  
Type: String  
Length Constraints: Minimum length of 1.  
Required: Yes

## Response Syntax
<a name="API_ListResourceTenants_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "NextToken": "string",
   "ResourceTenants": [ 
      { 
         "AssociatedTimestamp": number,
         "ResourceArn": "string",
         "TenantId": "string",
         "TenantName": "string"
      }
   ]
}
```

## Response Elements
<a name="API_ListResourceTenants_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [NextToken](#API_ListResourceTenants_ResponseSyntax) **   <a name="SES-ListResourceTenants-response-NextToken"></a>
A token that indicates that there are additional tenants to list. To view additional tenants, issue another request to `ListResourceTenants`, and pass this token in the `NextToken` parameter.  
Type: String

 ** [ResourceTenants](#API_ListResourceTenants_ResponseSyntax) **   <a name="SES-ListResourceTenants-response-ResourceTenants"></a>
An array that contains information about each tenant associated with the resource.  
Type: Array of [ResourceTenantMetadata](API_ResourceTenantMetadata.md) objects

## Errors
<a name="API_ListResourceTenants_Errors"></a>

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
<a name="API_ListResourceTenants_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/sesv2-2019-09-27/ListResourceTenants) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/sesv2-2019-09-27/ListResourceTenants) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sesv2-2019-09-27/ListResourceTenants) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/sesv2-2019-09-27/ListResourceTenants) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sesv2-2019-09-27/ListResourceTenants) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/sesv2-2019-09-27/ListResourceTenants) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/sesv2-2019-09-27/ListResourceTenants) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/sesv2-2019-09-27/ListResourceTenants) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/sesv2-2019-09-27/ListResourceTenants) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sesv2-2019-09-27/ListResourceTenants) 