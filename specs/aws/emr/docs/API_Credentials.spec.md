---
id: "@specs/aws/emr/docs/API_Credentials"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Credentials"
status: active
depends_on:
  - "@specs/aws/emr/meta"
---

# Credentials

> **source:** AWS Documentation
> **spec:id:** @specs/aws/emr/docs/API_Credentials
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Credentials
<a name="API_Credentials"></a>

The credentials that you can use to connect to cluster endpoints. Credentials consist of a username and a password.

## Contents
<a name="API_Credentials_Contents"></a>

**Important**  
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** UsernamePassword **   <a name="EMR-Type-Credentials-UsernamePassword"></a>
The username and password that you use to connect to cluster endpoints.  
Type: [UsernamePassword](API_UsernamePassword.md) object  
Required: No

## See Also
<a name="API_Credentials_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/elasticmapreduce-2009-03-31/Credentials) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/elasticmapreduce-2009-03-31/Credentials) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/elasticmapreduce-2009-03-31/Credentials) 