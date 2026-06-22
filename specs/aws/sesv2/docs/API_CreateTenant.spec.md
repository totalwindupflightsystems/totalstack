---
id: "@specs/aws/sesv2/docs/API_CreateTenant"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS CreateTenant"
status: active
depends_on:
  - "@specs/aws/sesv2/meta"
---

# CreateTenant

> **source:** AWS Documentation
> **spec:id:** @specs/aws/sesv2/docs/API_CreateTenant
> **target_lang:** meta — documentation tier. ALL sections preserved.



# CreateTenant
<a name="API_CreateTenant"></a>

Create a tenant.

 *Tenants* are logical containers that group related SES resources together. Each tenant can have its own set of resources like email identities, configuration sets, and templates, along with reputation metrics and sending status. This helps isolate and manage email sending for different customers or business units within your Amazon SES API v2 account.

You can optionally specify `SuppressionAttributes` to configure tenant-level suppression at creation time. When tenant-level suppression is enabled, Amazon SES maintains a separate suppression list for the tenant instead of using the account-level suppression list.

## Request Syntax
<a name="API_CreateTenant_RequestSyntax"></a>

```
POST /v2/email/tenants HTTP/1.1
Content-type: application/json

{
   "SuppressionAttributes": { 
      "SuppressedReasons": [ "{{string}}" ],
      "SuppressionScope": "{{string}}"
   },
   "Tags": [ 
      { 
         "Key": "{{string}}",
         "Value": "{{string}}"
      }
   ],
   "TenantName": "{{string}}"
}
```

## URI Request Parameters
<a name="API_CreateTenant_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_CreateTenant_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [SuppressionAttributes](#API_CreateTenant_RequestSyntax) **   <a name="SES-CreateTenant-request-SuppressionAttributes"></a>
An object that contains information about the suppression list preferences for the tenant. Use this to configure tenant-level suppression at creation time.  
Type: [TenantSuppressionAttributes](API_TenantSuppressionAttributes.md) object  
Required: No

 ** [Tags](#API_CreateTenant_RequestSyntax) **   <a name="SES-CreateTenant-request-Tags"></a>
An array of objects that define the tags (keys and values) to associate with the tenant  
Type: Array of [Tag](API_Tag.md) objects  
Required: No

 ** [TenantName](#API_CreateTenant_RequestSyntax) **   <a name="SES-CreateTenant-request-TenantName"></a>
The name of the tenant to create. The name can contain up to 64 alphanumeric characters, including letters, numbers, hyphens (-) and underscores (\_) only.  
Type: String  
Length Constraints: Minimum length of 1.  
Required: Yes

## Response Syntax
<a name="API_CreateTenant_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "CreatedTimestamp": number,
   "SendingStatus": "string",
   "SuppressionAttributes": { 
      "SuppressedReasons": [ "string" ],
      "SuppressionScope": "string"
   },
   "Tags": [ 
      { 
         "Key": "string",
         "Value": "string"
      }
   ],
   "TenantArn": "string",
   "TenantId": "string",
   "TenantName": "string"
}
```

## Response Elements
<a name="API_CreateTenant_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [CreatedTimestamp](#API_CreateTenant_ResponseSyntax) **   <a name="SES-CreateTenant-response-CreatedTimestamp"></a>
The date and time when the tenant was created.  
Type: Timestamp

 ** [SendingStatus](#API_CreateTenant_ResponseSyntax) **   <a name="SES-CreateTenant-response-SendingStatus"></a>
The status of email sending capability for the tenant.  
Type: String  
Valid Values: `ENABLED | REINSTATED | DISABLED` 

 ** [SuppressionAttributes](#API_CreateTenant_ResponseSyntax) **   <a name="SES-CreateTenant-response-SuppressionAttributes"></a>
An object that contains the suppression list preferences for a tenant.  
Type: [TenantSuppressionAttributes](API_TenantSuppressionAttributes.md) object

 ** [Tags](#API_CreateTenant_ResponseSyntax) **   <a name="SES-CreateTenant-response-Tags"></a>
An array of objects that define the tags (keys and values) associated with the tenant.  
Type: Array of [Tag](API_Tag.md) objects

 ** [TenantArn](#API_CreateTenant_ResponseSyntax) **   <a name="SES-CreateTenant-response-TenantArn"></a>
The Amazon Resource Name (ARN) of the tenant.  
Type: String  
Length Constraints: Minimum length of 1.

 ** [TenantId](#API_CreateTenant_ResponseSyntax) **   <a name="SES-CreateTenant-response-TenantId"></a>
A unique identifier for the tenant.  
Type: String

 ** [TenantName](#API_CreateTenant_ResponseSyntax) **   <a name="SES-CreateTenant-response-TenantName"></a>
The name of the tenant.  
Type: String  
Length Constraints: Minimum length of 1.

## Errors
<a name="API_CreateTenant_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AlreadyExistsException **   
The resource specified in your request already exists.  
HTTP Status Code: 400

 ** BadRequestException **   
The input you provided is invalid.  
HTTP Status Code: 400

 ** LimitExceededException **   
There are too many instances of the specified resource type.  
HTTP Status Code: 400

 ** TooManyRequestsException **   
Too many requests have been made to the operation.  
HTTP Status Code: 429

## See Also
<a name="API_CreateTenant_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/sesv2-2019-09-27/CreateTenant) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/sesv2-2019-09-27/CreateTenant) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sesv2-2019-09-27/CreateTenant) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/sesv2-2019-09-27/CreateTenant) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sesv2-2019-09-27/CreateTenant) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/sesv2-2019-09-27/CreateTenant) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/sesv2-2019-09-27/CreateTenant) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/sesv2-2019-09-27/CreateTenant) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/sesv2-2019-09-27/CreateTenant) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sesv2-2019-09-27/CreateTenant) 