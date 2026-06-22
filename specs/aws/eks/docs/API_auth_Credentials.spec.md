---
id: "@specs/aws/eks/docs/API_auth_Credentials"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Credentials"
status: active
depends_on:
  - "@specs/aws/eks/meta"
---

# Credentials

> **source:** AWS Documentation
> **spec:id:** @specs/aws/eks/docs/API_auth_Credentials
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Credentials
<a name="API_auth_Credentials"></a>

The * AWS Signature Version 4* type of temporary credentials.

## Contents
<a name="API_auth_Credentials_Contents"></a>

 ** accessKeyId **   <a name="AmazonEKS-Type-auth_Credentials-accessKeyId"></a>
The access key ID that identifies the temporary security credentials.  
Type: String  
Required: Yes

 ** expiration **   <a name="AmazonEKS-Type-auth_Credentials-expiration"></a>
The Unix epoch timestamp in seconds when the current credentials expire.  
Type: Timestamp  
Required: Yes

 ** secretAccessKey **   <a name="AmazonEKS-Type-auth_Credentials-secretAccessKey"></a>
The secret access key that applications inside the pods use to sign requests.  
Type: String  
Required: Yes

 ** sessionToken **   <a name="AmazonEKS-Type-auth_Credentials-sessionToken"></a>
The token that applications inside the pods must pass to any service API to use the temporary credentials.  
Type: String  
Required: Yes

## See Also
<a name="API_auth_Credentials_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/eks-auth-2023-11-26/Credentials) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/eks-auth-2023-11-26/Credentials) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/eks-auth-2023-11-26/Credentials) 