---
id: "@specs/aws/amplify/docs/API_CreateDomainAssociation"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS CreateDomainAssociation"
status: active
depends_on:
  - "@specs/aws/amplify/meta"
---

# CreateDomainAssociation

> **source:** AWS Documentation
> **spec:id:** @specs/aws/amplify/docs/API_CreateDomainAssociation
> **target_lang:** meta — documentation tier. ALL sections preserved.



# CreateDomainAssociation
<a name="API_CreateDomainAssociation"></a>

Creates a new domain association for an Amplify app. This action associates a custom domain with the Amplify app 

## Request Syntax
<a name="API_CreateDomainAssociation_RequestSyntax"></a>

```
POST /apps/{{appId}}/domains HTTP/1.1
Content-type: application/json

{
   "autoSubDomainCreationPatterns": [ "{{string}}" ],
   "autoSubDomainIAMRole": "{{string}}",
   "certificateSettings": { 
      "customCertificateArn": "{{string}}",
      "type": "{{string}}"
   },
   "domainName": "{{string}}",
   "enableAutoSubDomain": {{boolean}},
   "subDomainSettings": [ 
      { 
         "branchName": "{{string}}",
         "prefix": "{{string}}"
      }
   ]
}
```

## URI Request Parameters
<a name="API_CreateDomainAssociation_RequestParameters"></a>

The request uses the following URI parameters.

 ** [appId](#API_CreateDomainAssociation_RequestSyntax) **   <a name="amplify-CreateDomainAssociation-request-uri-appId"></a>
 The unique ID for an Amplify app.   
Length Constraints: Minimum length of 1. Maximum length of 20.  
Pattern: `d[a-z0-9]+`   
Required: Yes

## Request Body
<a name="API_CreateDomainAssociation_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [autoSubDomainCreationPatterns](#API_CreateDomainAssociation_RequestSyntax) **   <a name="amplify-CreateDomainAssociation-request-autoSubDomainCreationPatterns"></a>
 Sets the branch patterns for automatic subdomain creation.   
Type: Array of strings  
Length Constraints: Minimum length of 1. Maximum length of 2048.  
Pattern: `(?s).+`   
Required: No

 ** [autoSubDomainIAMRole](#API_CreateDomainAssociation_RequestSyntax) **   <a name="amplify-CreateDomainAssociation-request-autoSubDomainIAMRole"></a>
 The required AWS Identity and Access Management (IAM) service role for the Amazon Resource Name (ARN) for automatically creating subdomains.   
Type: String  
Length Constraints: Maximum length of 1000.  
Pattern: `^$|^arn:aws:iam::\d{12}:role.+`   
Required: No

 ** [certificateSettings](#API_CreateDomainAssociation_RequestSyntax) **   <a name="amplify-CreateDomainAssociation-request-certificateSettings"></a>
The type of SSL/TLS certificate to use for your custom domain. If you don't specify a certificate type, Amplify uses the default certificate that it provisions and manages for you.  
Type: [CertificateSettings](API_CertificateSettings.md) object  
Required: No

 ** [domainName](#API_CreateDomainAssociation_RequestSyntax) **   <a name="amplify-CreateDomainAssociation-request-domainName"></a>
 The domain name for the domain association.   
Type: String  
Length Constraints: Maximum length of 64.  
Pattern: `^(((?!-)[A-Za-z0-9-]{0,62}[A-Za-z0-9])\.)+((?!-)[A-Za-z0-9-]{1,62}[A-Za-z0-9])(\.)?$`   
Required: Yes

 ** [enableAutoSubDomain](#API_CreateDomainAssociation_RequestSyntax) **   <a name="amplify-CreateDomainAssociation-request-enableAutoSubDomain"></a>
 Enables the automated creation of subdomains for branches.   
Type: Boolean  
Required: No

 ** [subDomainSettings](#API_CreateDomainAssociation_RequestSyntax) **   <a name="amplify-CreateDomainAssociation-request-subDomainSettings"></a>
 The setting for the subdomain.   
Type: Array of [SubDomainSetting](API_SubDomainSetting.md) objects  
Array Members: Maximum number of 500 items.  
Required: Yes

## Response Syntax
<a name="API_CreateDomainAssociation_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "domainAssociation": { 
      "autoSubDomainCreationPatterns": [ "string" ],
      "autoSubDomainIAMRole": "string",
      "certificate": { 
         "certificateVerificationDNSRecord": "string",
         "customCertificateArn": "string",
         "type": "string"
      },
      "certificateVerificationDNSRecord": "string",
      "domainAssociationArn": "string",
      "domainName": "string",
      "domainStatus": "string",
      "enableAutoSubDomain": boolean,
      "statusReason": "string",
      "subDomains": [ 
         { 
            "dnsRecord": "string",
            "subDomainSetting": { 
               "branchName": "string",
               "prefix": "string"
            },
            "verified": boolean
         }
      ],
      "updateStatus": "string"
   }
}
```

## Response Elements
<a name="API_CreateDomainAssociation_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [domainAssociation](#API_CreateDomainAssociation_ResponseSyntax) **   <a name="amplify-CreateDomainAssociation-response-domainAssociation"></a>
 Describes the structure of a domain association, which associates a custom domain with an Amplify app.   
Type: [DomainAssociation](API_DomainAssociation.md) object

## Errors
<a name="API_CreateDomainAssociation_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** BadRequestException **   
A request contains unexpected data.   
HTTP Status Code: 400

 ** DependentServiceFailureException **   
An operation failed because a dependent service threw an exception.   
HTTP Status Code: 503

 ** InternalFailureException **   
The service failed to perform an operation due to an internal issue.   
HTTP Status Code: 500

 ** LimitExceededException **   
A resource could not be created because service quotas were exceeded.   
HTTP Status Code: 429

 ** NotFoundException **   
An entity was not found during an operation.   
HTTP Status Code: 404

 ** UnauthorizedException **   
An operation failed due to a lack of access.   
HTTP Status Code: 401

## See Also
<a name="API_CreateDomainAssociation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/amplify-2017-07-25/CreateDomainAssociation) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/amplify-2017-07-25/CreateDomainAssociation) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/amplify-2017-07-25/CreateDomainAssociation) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/amplify-2017-07-25/CreateDomainAssociation) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/amplify-2017-07-25/CreateDomainAssociation) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/amplify-2017-07-25/CreateDomainAssociation) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/amplify-2017-07-25/CreateDomainAssociation) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/amplify-2017-07-25/CreateDomainAssociation) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/amplify-2017-07-25/CreateDomainAssociation) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/amplify-2017-07-25/CreateDomainAssociation) 