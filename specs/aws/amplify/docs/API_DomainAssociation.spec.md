---
id: "@specs/aws/amplify/docs/API_DomainAssociation"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS DomainAssociation"
status: active
depends_on:
  - "@specs/aws/amplify/meta"
---

# DomainAssociation

> **source:** AWS Documentation
> **spec:id:** @specs/aws/amplify/docs/API_DomainAssociation
> **target_lang:** meta — documentation tier. ALL sections preserved.



# DomainAssociation
<a name="API_DomainAssociation"></a>

Describes the association between a custom domain and an Amplify app. 

## Contents
<a name="API_DomainAssociation_Contents"></a>

 ** domainAssociationArn **   <a name="amplify-Type-DomainAssociation-domainAssociationArn"></a>
 The Amazon Resource Name (ARN) for the domain association.   
Type: String  
Length Constraints: Maximum length of 1000.  
Required: Yes

 ** domainName **   <a name="amplify-Type-DomainAssociation-domainName"></a>
 The name of the domain.   
Type: String  
Length Constraints: Maximum length of 64.  
Pattern: `^(((?!-)[A-Za-z0-9-]{0,62}[A-Za-z0-9])\.)+((?!-)[A-Za-z0-9-]{1,62}[A-Za-z0-9])(\.)?$`   
Required: Yes

 ** domainStatus **   <a name="amplify-Type-DomainAssociation-domainStatus"></a>
 The current status of the domain association.   
Type: String  
Valid Values: `PENDING_VERIFICATION | IN_PROGRESS | AVAILABLE | IMPORTING_CUSTOM_CERTIFICATE | PENDING_DEPLOYMENT | AWAITING_APP_CNAME | FAILED | CREATING | REQUESTING_CERTIFICATE | UPDATING`   
Required: Yes

 ** enableAutoSubDomain **   <a name="amplify-Type-DomainAssociation-enableAutoSubDomain"></a>
 Enables the automated creation of subdomains for branches.   
Type: Boolean  
Required: Yes

 ** statusReason **   <a name="amplify-Type-DomainAssociation-statusReason"></a>
 Additional information that describes why the domain association is in the current state.  
Type: String  
Length Constraints: Maximum length of 1000.  
Required: Yes

 ** subDomains **   <a name="amplify-Type-DomainAssociation-subDomains"></a>
 The subdomains for the domain association.   
Type: Array of [SubDomain](API_SubDomain.md) objects  
Array Members: Maximum number of 500 items.  
Required: Yes

 ** autoSubDomainCreationPatterns **   <a name="amplify-Type-DomainAssociation-autoSubDomainCreationPatterns"></a>
 Sets branch patterns for automatic subdomain creation.   
Type: Array of strings  
Length Constraints: Minimum length of 1. Maximum length of 2048.  
Pattern: `(?s).+`   
Required: No

 ** autoSubDomainIAMRole **   <a name="amplify-Type-DomainAssociation-autoSubDomainIAMRole"></a>
 The required AWS Identity and Access Management (IAM) service role for the Amazon Resource Name (ARN) for automatically creating subdomains.   
Type: String  
Length Constraints: Maximum length of 1000.  
Pattern: `^$|^arn:aws:iam::\d{12}:role.+`   
Required: No

 ** certificate **   <a name="amplify-Type-DomainAssociation-certificate"></a>
Describes the SSL/TLS certificate for the domain association. This can be your own custom certificate or the default certificate that Amplify provisions for you.  
If you are updating your domain to use a different certificate, `certificate` points to the new certificate that is being created instead of the current active certificate. Otherwise, `certificate` points to the current active certificate.  
Type: [Certificate](API_Certificate.md) object  
Required: No

 ** certificateVerificationDNSRecord **   <a name="amplify-Type-DomainAssociation-certificateVerificationDNSRecord"></a>
 The DNS record for certificate verification.   
Type: String  
Length Constraints: Maximum length of 1000.  
Required: No

 ** updateStatus **   <a name="amplify-Type-DomainAssociation-updateStatus"></a>
The status of the domain update operation that is currently in progress. The following list describes the valid update states.    
REQUESTING\_CERTIFICATE  
The certificate is in the process of being updated.  
PENDING\_VERIFICATION  
Indicates that an Amplify managed certificate is in the process of being verified. This occurs during the creation of a custom domain or when a custom domain is updated to use a managed certificate.  
IMPORTING\_CUSTOM\_CERTIFICATE  
Indicates that an Amplify custom certificate is in the process of being imported. This occurs during the creation of a custom domain or when a custom domain is updated to use a custom certificate.  
PENDING\_DEPLOYMENT  
Indicates that the subdomain or certificate changes are being propagated.  
AWAITING\_APP\_CNAME  
Amplify is waiting for CNAME records corresponding to subdomains to be propagated. If your custom domain is on Route 53, Amplify handles this for you automatically. For more information about custom domains, see [Setting up custom domains](https://docs.aws.amazon.com/amplify/latest/userguide/custom-domains.html) in the *Amplify Hosting User Guide*.   
UPDATE\_COMPLETE  
The certificate has been associated with a domain.  
UPDATE\_FAILED  
The certificate has failed to be provisioned or associated, and there is no existing active certificate to roll back to.
Type: String  
Valid Values: `REQUESTING_CERTIFICATE | PENDING_VERIFICATION | IMPORTING_CUSTOM_CERTIFICATE | PENDING_DEPLOYMENT | AWAITING_APP_CNAME | UPDATE_COMPLETE | UPDATE_FAILED`   
Required: No

## See Also
<a name="API_DomainAssociation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/amplify-2017-07-25/DomainAssociation) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/amplify-2017-07-25/DomainAssociation) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/amplify-2017-07-25/DomainAssociation) 