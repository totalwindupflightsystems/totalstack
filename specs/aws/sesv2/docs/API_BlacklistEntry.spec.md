---
id: "@specs/aws/sesv2/docs/API_BlacklistEntry"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS BlacklistEntry"
status: active
depends_on:
  - "@specs/aws/sesv2/meta"
---

# BlacklistEntry

> **source:** AWS Documentation
> **spec:id:** @specs/aws/sesv2/docs/API_BlacklistEntry
> **target_lang:** meta — documentation tier. ALL sections preserved.



# BlacklistEntry
<a name="API_BlacklistEntry"></a>

An object that contains information about a blacklisting event that impacts one of the dedicated IP addresses that is associated with your account.

## Contents
<a name="API_BlacklistEntry_Contents"></a>

 ** Description **   <a name="SES-Type-BlacklistEntry-Description"></a>
Additional information about the blacklisting event, as provided by the blacklist maintainer.  
Type: String  
Required: No

 ** ListingTime **   <a name="SES-Type-BlacklistEntry-ListingTime"></a>
The time when the blacklisting event occurred.  
Type: Timestamp  
Required: No

 ** RblName **   <a name="SES-Type-BlacklistEntry-RblName"></a>
The name of the blacklist that the IP address appears on.  
Type: String  
Required: No

## See Also
<a name="API_BlacklistEntry_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sesv2-2019-09-27/BlacklistEntry) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sesv2-2019-09-27/BlacklistEntry) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sesv2-2019-09-27/BlacklistEntry) 