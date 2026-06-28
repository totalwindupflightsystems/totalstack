---
id: "@specs/aws/globalaccelerator/docs/API_CidrAuthorizationContext"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS CidrAuthorizationContext"
status: active
depends_on:
  - "@specs/aws/globalaccelerator/meta"
---

# CidrAuthorizationContext

> **source:** AWS Documentation
> **spec:id:** @specs/aws/globalaccelerator/docs/API_CidrAuthorizationContext
> **target_lang:** meta — documentation tier. ALL sections preserved.



# CidrAuthorizationContext
<a name="API_CidrAuthorizationContext"></a>

Provides authorization for Amazon to bring a specific IP address range to a specific AWS account using bring your own IP addresses (BYOIP). 

For more information, see [Bring your own IP addresses (BYOIP)](https://docs.aws.amazon.com/global-accelerator/latest/dg/using-byoip.html) in the * AWS Global Accelerator Developer Guide*.

## Contents
<a name="API_CidrAuthorizationContext_Contents"></a>

 ** Message **   <a name="globalaccelerator-Type-CidrAuthorizationContext-Message"></a>
The plain-text authorization message for the prefix and account.  
Type: String  
Length Constraints: Maximum length of 255.  
Required: Yes

 ** Signature **   <a name="globalaccelerator-Type-CidrAuthorizationContext-Signature"></a>
The signed authorization message for the prefix and account.  
Type: String  
Length Constraints: Maximum length of 255.  
Required: Yes

## See Also
<a name="API_CidrAuthorizationContext_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/globalaccelerator-2018-08-08/CidrAuthorizationContext) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/globalaccelerator-2018-08-08/CidrAuthorizationContext) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/globalaccelerator-2018-08-08/CidrAuthorizationContext) 