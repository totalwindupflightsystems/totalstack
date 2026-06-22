---
id: "@specs/aws/appsync/docs/API_DomainNameConfig"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS DomainNameConfig"
status: active
depends_on:
  - "@specs/aws/appsync/meta"
---

# DomainNameConfig

> **source:** AWS Documentation
> **spec:id:** @specs/aws/appsync/docs/API_DomainNameConfig
> **target_lang:** meta — documentation tier. ALL sections preserved.



# DomainNameConfig
<a name="API_DomainNameConfig"></a>

Describes a configuration for a custom domain.

## Contents
<a name="API_DomainNameConfig_Contents"></a>

 ** appsyncDomainName **   <a name="appsync-Type-DomainNameConfig-appsyncDomainName"></a>
The domain name that AWS AppSync provides.  
Type: String  
Required: No

 ** certificateArn **   <a name="appsync-Type-DomainNameConfig-certificateArn"></a>
The Amazon Resource Name (ARN) of the certificate. This can be an AWS Certificate Manager (ACM) certificate or an AWS Identity and Access Management (IAM) server certificate.  
Type: String  
Length Constraints: Minimum length of 20. Maximum length of 2048.  
Pattern: `^arn:[a-z-]*:(acm|iam):[a-z0-9-]*:\d{12}:(certificate|server-certificate)/[0-9A-Za-z_/-]*$`   
Required: No

 ** description **   <a name="appsync-Type-DomainNameConfig-description"></a>
A description of the `DomainName` configuration.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 255.  
Pattern: `^.*$`   
Required: No

 ** domainName **   <a name="appsync-Type-DomainNameConfig-domainName"></a>
The domain name.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 253.  
Pattern: `^(\*[\w\d-]*\.)?([\w\d-]+\.)+[\w\d-]+$`   
Required: No

 ** domainNameArn **   <a name="appsync-Type-DomainNameConfig-domainNameArn"></a>
The Amazon Resource Name (ARN) of the domain name.  
Type: String  
Required: No

 ** hostedZoneId **   <a name="appsync-Type-DomainNameConfig-hostedZoneId"></a>
The ID of your Amazon Route 53 hosted zone.  
Type: String  
Required: No

 ** tags **   <a name="appsync-Type-DomainNameConfig-tags"></a>
A map with keys of `TagKey` objects and values of `TagValue` objects.  
Type: String to string map  
Map Entries: Maximum number of 50 items.  
Key Length Constraints: Minimum length of 1. Maximum length of 128.  
Key Pattern: `^(?!aws:)[ a-zA-Z+-=._:/]+$`   
Value Length Constraints: Maximum length of 256.  
Value Pattern: `^[\s\w+-=\.:/@]*$`   
Required: No

## See Also
<a name="API_DomainNameConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/appsync-2017-07-25/DomainNameConfig) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/appsync-2017-07-25/DomainNameConfig) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/appsync-2017-07-25/DomainNameConfig) 