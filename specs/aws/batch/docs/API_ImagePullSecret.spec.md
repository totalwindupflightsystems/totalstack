---
id: "@specs/aws/batch/docs/API_ImagePullSecret"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS ImagePullSecret"
status: active
depends_on:
  - "@specs/aws/batch/meta"
---

# ImagePullSecret

> **source:** AWS Documentation
> **spec:id:** @specs/aws/batch/docs/API_ImagePullSecret
> **target_lang:** meta — documentation tier. ALL sections preserved.



# ImagePullSecret
<a name="API_ImagePullSecret"></a>

References a Kubernetes secret resource. This name of the secret must start and end with an alphanumeric character, is required to be lowercase, can include periods (.) and hyphens (-), and can't contain more than 253 characters.

## Contents
<a name="API_ImagePullSecret_Contents"></a>

 ** name **   <a name="Batch-Type-ImagePullSecret-name"></a>
Provides a unique identifier for the `ImagePullSecret`. This object is required when `EksPodProperties$imagePullSecrets` is used.  
Type: String  
Required: Yes

## See Also
<a name="API_ImagePullSecret_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/batch-2016-08-10/ImagePullSecret) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/batch-2016-08-10/ImagePullSecret) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/batch-2016-08-10/ImagePullSecret) 