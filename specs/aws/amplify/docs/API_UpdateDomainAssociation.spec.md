---
id: "@specs/aws/amplify/docs/API_UpdateDomainAssociation"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS UpdateDomainAssociation"
status: active
depends_on:
  - "@specs/aws/amplify/meta"
---

# UpdateDomainAssociation

> **source:** AWS Documentation
> **spec:id:** @specs/aws/amplify/docs/API_UpdateDomainAssociation
> **target_lang:** meta — documentation tier. ALL sections preserved.



# UpdateDomainAssociation
<a name="API_UpdateDomainAssociation"></a>

Creates a new domain association for an Amplify app.

## Request Syntax
<a name="API_UpdateDomainAssociation_RequestSyntax"></a>

```
POST /apps/{{appId}}/domains/{{domainName}} HTTP/1.1
Content-type: application/json

{
   "autoSubDomainCreationPatterns": [ "{{string}}" ],
   "autoSubDomainIAMRole": "{{string}}",
   "certificateSettings": { 
      "customCertificateArn": "{{string}}",
      "type": "{{string}}"
   },
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
<a name="API_UpdateDomainAssociation_RequestParameters"></a>

The request uses the following URI parameters.

 ** [appId](#API_UpdateDomainAssociation_RequestSyntax) **   <a name="amplify-UpdateDomainAssociation-request-uri-appId"></a>
 The unique ID for an Amplify app.   
Length Constraints: Minimum length of 1. Maximum length of 20.  
Pattern: `d[a-z0-9]+`   
Required: Yes

 ** [domainName](#API_UpdateDomainAssociation_RequestSyntax) **   <a name="amplify-UpdateDomainAssociation-request-uri-domainName"></a>
 The name of the domain.   
Length Constraints: Maximum length of 64.  
Pattern: `^(((?!-)[A-Za-z0-9-]{0,62}[A-Za-z0-9])\.)+((?!-)[A-Za-z0-9-]{1,62}[A-Za-z0-9])(\.)?$`   
Required: Yes

## Request Body
<a name="API_UpdateDomainAssociation_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [autoSubDomainCreationPatterns](#API_UpdateDomainAssociation_RequestSyntax) **   <a name="amplify-UpdateDomainAssociation-request-autoSubDomainCreationPatterns"></a>
 Sets the branch patterns for automatic subdomain creation.   
Type: Array of strings  
Length Constraints: Minimum length of 1. Maximum length of 2048.  
Pattern: `(?s).+`   
Required: No

 ** [autoSubDomainIAMRole](#API_UpdateDomainAssociation_RequestSyntax) **   <a name="amplify-UpdateDomainAssociation-request-autoSubDomainIAMRole"></a>
 The required AWS Identity and Access Management (IAM) service role for the Amazon Resource Name (ARN) for automatically creating subdomains.   
Type: String  
Length Constraints: Maximum length of 1000.  
Pattern: `^$|^arn:aws:iam::\d{12}:role.+`   
Required: No

 ** [certificateSettings](#API_UpdateDomainAssociation_RequestSyntax) **   <a name="amplify-UpdateDomainAssociation-request-certificateSettings"></a>
The type of SSL/TLS certificate to use for your custom domain.  
Type: [CertificateSettings](API_CertificateSettings.md) object  
Required: No

 ** [enableAutoSubDomain](#API_UpdateDomainAssociation_RequestSyntax) **   <a name="amplify-UpdateDomainAssociation-request-enableAutoSubDomain"></a>
 Enables the automated creation of subdomains for branches.   
Type: Boolean  
Required: No

 ** [subDomainSettings](#API_UpdateDomainAssociation_RequestSyntax) **   <a name="amplify-UpdateDomainAssociation-request-subDomainSettings"></a>
 Describes the settings for the subdomain.   
Type: Array of [SubDomainSetting](API_SubDomainSetting.md) objects  
Array Members: Maximum number of 500 items.  
Required: No

## Response Syntax
<a name="API_UpdateDomainAssociation_ResponseSyntax"></a>

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
<a name="API_UpdateDomainAssociation_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [domainAssociation](#API_UpdateDomainAssociation_ResponseSyntax) **   <a name="amplify-UpdateDomainAssociation-response-domainAssociation"></a>
 Describes a domain association, which associates a custom domain with an Amplify app.   
Type: [DomainAssociation](API_DomainAssociation.md) object

## Errors
<a name="API_UpdateDomainAssociation_Errors"></a>

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

 ** NotFoundException **   
An entity was not found during an operation.   
HTTP Status Code: 404

 ** UnauthorizedException **   
An operation failed due to a lack of access.   
HTTP Status Code: 401

## See Also
<a name="API_UpdateDomainAssociation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/amplify-2017-07-25/UpdateDomainAssociation) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/amplify-2017-07-25/UpdateDomainAssociation) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/amplify-2017-07-25/UpdateDomainAssociation) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/amplify-2017-07-25/UpdateDomainAssociation) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/amplify-2017-07-25/UpdateDomainAssociation) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/amplify-2017-07-25/UpdateDomainAssociation) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/amplify-2017-07-25/UpdateDomainAssociation) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/amplify-2017-07-25/UpdateDomainAssociation) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/amplify-2017-07-25/UpdateDomainAssociation) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/amplify-2017-07-25/UpdateDomainAssociation) 