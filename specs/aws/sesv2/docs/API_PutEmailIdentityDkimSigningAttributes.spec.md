---
id: "@specs/aws/sesv2/docs/API_PutEmailIdentityDkimSigningAttributes"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS PutEmailIdentityDkimSigningAttributes"
status: active
depends_on:
  - "@specs/aws/sesv2/meta"
---

# PutEmailIdentityDkimSigningAttributes

> **source:** AWS Documentation
> **spec:id:** @specs/aws/sesv2/docs/API_PutEmailIdentityDkimSigningAttributes
> **target_lang:** meta — documentation tier. ALL sections preserved.



# PutEmailIdentityDkimSigningAttributes
<a name="API_PutEmailIdentityDkimSigningAttributes"></a>

Used to configure or change the DKIM authentication settings for an email domain identity. You can use this operation to do any of the following:
+ Update the signing attributes for an identity that uses Bring Your Own DKIM (BYODKIM).
+ Update the key length that should be used for Easy DKIM.
+ Change from using no DKIM authentication to using Easy DKIM.
+ Change from using no DKIM authentication to using BYODKIM.
+ Change from using Easy DKIM to using BYODKIM.
+ Change from using BYODKIM to using Easy DKIM.

## Request Syntax
<a name="API_PutEmailIdentityDkimSigningAttributes_RequestSyntax"></a>

```
PUT /v2/email/identities/{{EmailIdentity}}/dkim/signing HTTP/1.1
Content-type: application/json

{
   "SigningAttributes": { 
      "DomainSigningAttributesOrigin": "{{string}}",
      "DomainSigningPrivateKey": "{{string}}",
      "DomainSigningSelector": "{{string}}",
      "NextSigningKeyLength": "{{string}}"
   },
   "SigningAttributesOrigin": "{{string}}"
}
```

## URI Request Parameters
<a name="API_PutEmailIdentityDkimSigningAttributes_RequestParameters"></a>

The request uses the following URI parameters.

 ** [EmailIdentity](#API_PutEmailIdentityDkimSigningAttributes_RequestSyntax) **   <a name="SES-PutEmailIdentityDkimSigningAttributes-request-uri-EmailIdentity"></a>
The email identity.  
Length Constraints: Minimum length of 1.  
Required: Yes

## Request Body
<a name="API_PutEmailIdentityDkimSigningAttributes_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [SigningAttributes](#API_PutEmailIdentityDkimSigningAttributes_RequestSyntax) **   <a name="SES-PutEmailIdentityDkimSigningAttributes-request-SigningAttributes"></a>
An object that contains information about the private key and selector that you want to use to configure DKIM for the identity for Bring Your Own DKIM (BYODKIM) for the identity, or, configures the key length to be used for [Easy DKIM](https://docs.aws.amazon.com/ses/latest/DeveloperGuide/easy-dkim.html).  
Type: [DkimSigningAttributes](API_DkimSigningAttributes.md) object  
Required: No

 ** [SigningAttributesOrigin](#API_PutEmailIdentityDkimSigningAttributes_RequestSyntax) **   <a name="SES-PutEmailIdentityDkimSigningAttributes-request-SigningAttributesOrigin"></a>
The method to use to configure DKIM for the identity. There are the following possible values:  
+  `AWS_SES` – Configure DKIM for the identity by using [Easy DKIM](https://docs.aws.amazon.com/ses/latest/DeveloperGuide/easy-dkim.html).
+  `EXTERNAL` – Configure DKIM for the identity by using Bring Your Own DKIM (BYODKIM).
Type: String  
Valid Values: `AWS_SES | EXTERNAL | AWS_SES_AF_SOUTH_1 | AWS_SES_EU_NORTH_1 | AWS_SES_AP_SOUTH_1 | AWS_SES_EU_WEST_3 | AWS_SES_EU_WEST_2 | AWS_SES_EU_SOUTH_1 | AWS_SES_EU_WEST_1 | AWS_SES_AP_NORTHEAST_3 | AWS_SES_AP_NORTHEAST_2 | AWS_SES_ME_SOUTH_1 | AWS_SES_AP_NORTHEAST_1 | AWS_SES_IL_CENTRAL_1 | AWS_SES_SA_EAST_1 | AWS_SES_CA_CENTRAL_1 | AWS_SES_AP_SOUTHEAST_1 | AWS_SES_AP_SOUTHEAST_2 | AWS_SES_AP_SOUTHEAST_3 | AWS_SES_EU_CENTRAL_1 | AWS_SES_US_EAST_1 | AWS_SES_US_EAST_2 | AWS_SES_US_WEST_1 | AWS_SES_US_WEST_2 | AWS_SES_ME_CENTRAL_1 | AWS_SES_AP_SOUTH_2 | AWS_SES_EU_CENTRAL_2 | AWS_SES_AP_SOUTHEAST_5 | AWS_SES_CA_WEST_1`   
Required: Yes

## Response Syntax
<a name="API_PutEmailIdentityDkimSigningAttributes_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "DkimStatus": "string",
   "DkimTokens": [ "string" ],
   "SigningHostedZone": "string"
}
```

## Response Elements
<a name="API_PutEmailIdentityDkimSigningAttributes_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [DkimStatus](#API_PutEmailIdentityDkimSigningAttributes_ResponseSyntax) **   <a name="SES-PutEmailIdentityDkimSigningAttributes-response-DkimStatus"></a>
The DKIM authentication status of the identity. Amazon SES determines the authentication status by searching for specific records in the DNS configuration for your domain. If you used [Easy DKIM](https://docs.aws.amazon.com/ses/latest/DeveloperGuide/easy-dkim.html) to set up DKIM authentication, Amazon SES tries to find three unique CNAME records in the DNS configuration for your domain.  
If you provided a public key to perform DKIM authentication, Amazon SES tries to find a TXT record that uses the selector that you specified. The value of the TXT record must be a public key that's paired with the private key that you specified in the process of creating the identity.  
The status can be one of the following:  
+  `PENDING` – The verification process was initiated, but Amazon SES hasn't yet detected the DKIM records in the DNS configuration for the domain.
+  `SUCCESS` – The verification process completed successfully.
+  `FAILED` – The verification process failed. This typically occurs when Amazon SES fails to find the DKIM records in the DNS configuration of the domain.
+  `TEMPORARY_FAILURE` – A temporary issue is preventing Amazon SES from determining the DKIM authentication status of the domain.
+  `NOT_STARTED` – The DKIM verification process hasn't been initiated for the domain.
Type: String  
Valid Values: `PENDING | SUCCESS | FAILED | TEMPORARY_FAILURE | NOT_STARTED` 

 ** [DkimTokens](#API_PutEmailIdentityDkimSigningAttributes_ResponseSyntax) **   <a name="SES-PutEmailIdentityDkimSigningAttributes-response-DkimTokens"></a>
If you used [Easy DKIM](https://docs.aws.amazon.com/ses/latest/DeveloperGuide/easy-dkim.html) to configure DKIM authentication for the domain, then this object contains a set of unique strings that you use to create a set of CNAME records that you add to the DNS configuration for your domain. When Amazon SES detects these records in the DNS configuration for your domain, the DKIM authentication process is complete.  
If you configured DKIM authentication for the domain by providing your own public-private key pair, then this object contains the selector that's associated with your public key.  
Regardless of the DKIM authentication method you use, Amazon SES searches for the appropriate records in the DNS configuration of the domain for up to 72 hours.  
Type: Array of strings

 ** [SigningHostedZone](#API_PutEmailIdentityDkimSigningAttributes_ResponseSyntax) **   <a name="SES-PutEmailIdentityDkimSigningAttributes-response-SigningHostedZone"></a>
The hosted zone where Amazon SES publishes the DKIM public key TXT records for this email identity. This value indicates the DNS zone that customers must reference when configuring their CNAME records for DKIM authentication.  
When configuring DKIM for your domain, create CNAME records in your DNS that point to the selectors in this hosted zone. For example:  
 ` selector1._domainkey.yourdomain.com CNAME selector1.<SigningHostedZone> `   
 ` selector2._domainkey.yourdomain.com CNAME selector2.<SigningHostedZone> `   
 ` selector3._domainkey.yourdomain.com CNAME selector3.<SigningHostedZone> `   
Type: String

## Errors
<a name="API_PutEmailIdentityDkimSigningAttributes_Errors"></a>

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
<a name="API_PutEmailIdentityDkimSigningAttributes_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/sesv2-2019-09-27/PutEmailIdentityDkimSigningAttributes) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/sesv2-2019-09-27/PutEmailIdentityDkimSigningAttributes) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sesv2-2019-09-27/PutEmailIdentityDkimSigningAttributes) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/sesv2-2019-09-27/PutEmailIdentityDkimSigningAttributes) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sesv2-2019-09-27/PutEmailIdentityDkimSigningAttributes) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/sesv2-2019-09-27/PutEmailIdentityDkimSigningAttributes) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/sesv2-2019-09-27/PutEmailIdentityDkimSigningAttributes) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/sesv2-2019-09-27/PutEmailIdentityDkimSigningAttributes) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/sesv2-2019-09-27/PutEmailIdentityDkimSigningAttributes) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sesv2-2019-09-27/PutEmailIdentityDkimSigningAttributes) 