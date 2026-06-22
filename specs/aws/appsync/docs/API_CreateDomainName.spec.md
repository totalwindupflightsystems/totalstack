---
id: "@specs/aws/appsync/docs/API_CreateDomainName"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS CreateDomainName"
status: active
depends_on:
  - "@specs/aws/appsync/meta"
---

# CreateDomainName

> **source:** AWS Documentation
> **spec:id:** @specs/aws/appsync/docs/API_CreateDomainName
> **target_lang:** meta — documentation tier. ALL sections preserved.



# CreateDomainName
<a name="API_CreateDomainName"></a>

Creates a custom `DomainName` object.

## Request Syntax
<a name="API_CreateDomainName_RequestSyntax"></a>

```
POST /v1/domainnames HTTP/1.1
Content-type: application/json

{
   "certificateArn": "{{string}}",
   "description": "{{string}}",
   "domainName": "{{string}}",
   "tags": { 
      "{{string}}" : "{{string}}" 
   }
}
```

## URI Request Parameters
<a name="API_CreateDomainName_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_CreateDomainName_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [certificateArn](#API_CreateDomainName_RequestSyntax) **   <a name="appsync-CreateDomainName-request-certificateArn"></a>
The Amazon Resource Name (ARN) of the certificate. This can be an AWS Certificate Manager (ACM) certificate or an AWS Identity and Access Management (IAM) server certificate.  
Type: String  
Length Constraints: Minimum length of 20. Maximum length of 2048.  
Pattern: `^arn:[a-z-]*:(acm|iam):[a-z0-9-]*:\d{12}:(certificate|server-certificate)/[0-9A-Za-z_/-]*$`   
Required: Yes

 ** [description](#API_CreateDomainName_RequestSyntax) **   <a name="appsync-CreateDomainName-request-description"></a>
A description of the `DomainName`.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 255.  
Pattern: `^.*$`   
Required: No

 ** [domainName](#API_CreateDomainName_RequestSyntax) **   <a name="appsync-CreateDomainName-request-domainName"></a>
The domain name.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 253.  
Pattern: `^(\*[\w\d-]*\.)?([\w\d-]+\.)+[\w\d-]+$`   
Required: Yes

 ** [tags](#API_CreateDomainName_RequestSyntax) **   <a name="appsync-CreateDomainName-request-tags"></a>
A map with keys of `TagKey` objects and values of `TagValue` objects.  
Type: String to string map  
Map Entries: Maximum number of 50 items.  
Key Length Constraints: Minimum length of 1. Maximum length of 128.  
Key Pattern: `^(?!aws:)[ a-zA-Z+-=._:/]+$`   
Value Length Constraints: Maximum length of 256.  
Value Pattern: `^[\s\w+-=\.:/@]*$`   
Required: No

## Response Syntax
<a name="API_CreateDomainName_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "domainNameConfig": { 
      "appsyncDomainName": "string",
      "certificateArn": "string",
      "description": "string",
      "domainName": "string",
      "domainNameArn": "string",
      "hostedZoneId": "string",
      "tags": { 
         "string" : "string" 
      }
   }
}
```

## Response Elements
<a name="API_CreateDomainName_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [domainNameConfig](#API_CreateDomainName_ResponseSyntax) **   <a name="appsync-CreateDomainName-response-domainNameConfig"></a>
The configuration for the `DomainName`.  
Type: [DomainNameConfig](API_DomainNameConfig.md) object

## Errors
<a name="API_CreateDomainName_Errors"></a>

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

 ** InternalFailureException **   
An internal AWS AppSync error occurred. Try your request again.  
HTTP Status Code: 500

## See Also
<a name="API_CreateDomainName_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/appsync-2017-07-25/CreateDomainName) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/appsync-2017-07-25/CreateDomainName) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/appsync-2017-07-25/CreateDomainName) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/appsync-2017-07-25/CreateDomainName) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/appsync-2017-07-25/CreateDomainName) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/appsync-2017-07-25/CreateDomainName) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/appsync-2017-07-25/CreateDomainName) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/appsync-2017-07-25/CreateDomainName) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/appsync-2017-07-25/CreateDomainName) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/appsync-2017-07-25/CreateDomainName) 