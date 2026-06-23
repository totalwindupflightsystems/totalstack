---
id: "@specs/aws/amplify/docs/API_SubDomain"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS SubDomain"
status: active
depends_on:
  - "@specs/aws/amplify/meta"
---

# SubDomain

> **source:** AWS Documentation
> **spec:id:** @specs/aws/amplify/docs/API_SubDomain
> **target_lang:** meta — documentation tier. ALL sections preserved.



# SubDomain
<a name="API_SubDomain"></a>

 The subdomain for the domain association. 

## Contents
<a name="API_SubDomain_Contents"></a>

 ** dnsRecord **   <a name="amplify-Type-SubDomain-dnsRecord"></a>
 The DNS record for the subdomain.   
Type: String  
Length Constraints: Maximum length of 1000.  
Required: Yes

 ** subDomainSetting **   <a name="amplify-Type-SubDomain-subDomainSetting"></a>
 Describes the settings for the subdomain.   
Type: [SubDomainSetting](API_SubDomainSetting.md) object  
Required: Yes

 ** verified **   <a name="amplify-Type-SubDomain-verified"></a>
 The verified status of the subdomain   
Type: Boolean  
Required: Yes

## See Also
<a name="API_SubDomain_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/amplify-2017-07-25/SubDomain) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/amplify-2017-07-25/SubDomain) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/amplify-2017-07-25/SubDomain) 