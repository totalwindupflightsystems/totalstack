---
id: "@specs/aws/redshift/docs/API_AuthenticationProfile"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS AuthenticationProfile"
status: active
depends_on:
  - "@specs/aws/redshift/meta"
---

# AuthenticationProfile

> **source:** AWS Documentation
> **spec:id:** @specs/aws/redshift/docs/API_AuthenticationProfile
> **target_lang:** meta — documentation tier. ALL sections preserved.



# AuthenticationProfile
<a name="API_AuthenticationProfile"></a>

Describes an authentication profile.

## Contents
<a name="API_AuthenticationProfile_Contents"></a>

**Note**  
In the following list, the required parameters are described first.

 ** AuthenticationProfileContent **   
The content of the authentication profile in JSON format. The maximum length of the JSON string is determined by a quota for your account.  
Type: String  
Length Constraints: Maximum length of 2147483647.  
Required: No

 ** AuthenticationProfileName **   
The name of the authentication profile.  
Type: String  
Length Constraints: Maximum length of 63.  
Pattern: `^[a-zA-Z0-9\-]+$`   
Required: No

## See Also
<a name="API_AuthenticationProfile_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/redshift-2012-12-01/AuthenticationProfile) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/redshift-2012-12-01/AuthenticationProfile) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/redshift-2012-12-01/AuthenticationProfile) 