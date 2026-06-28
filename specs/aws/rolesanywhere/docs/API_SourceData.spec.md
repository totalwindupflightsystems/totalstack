---
id: "@specs/aws/rolesanywhere/docs/API_SourceData"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS SourceData"
status: active
depends_on:
  - "@specs/aws/rolesanywhere/meta"
---

# SourceData

> **source:** AWS Documentation
> **spec:id:** @specs/aws/rolesanywhere/docs/API_SourceData
> **target_lang:** meta — documentation tier. ALL sections preserved.



# SourceData
<a name="API_SourceData"></a>

The data field of the trust anchor depending on its type. 

## Contents
<a name="API_SourceData_Contents"></a>

**Important**  
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** acmPcaArn **   <a name="rolesanywhere-Type-SourceData-acmPcaArn"></a>
 The root certificate of the AWS Private Certificate Authority specified by this ARN is used in trust validation for temporary credential requests. Included for trust anchors of type `AWS_ACM_PCA`.   
Type: String  
Required: No

 ** x509CertificateData **   <a name="rolesanywhere-Type-SourceData-x509CertificateData"></a>
The PEM-encoded data for the certificate anchor. Included for trust anchors of type `CERTIFICATE_BUNDLE`.   
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 8000.  
Required: No

## See Also
<a name="API_SourceData_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/rolesanywhere-2018-05-10/SourceData) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/rolesanywhere-2018-05-10/SourceData) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/rolesanywhere-2018-05-10/SourceData) 