---
id: "@specs/aws/batch/docs/API_EksSecret"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS EksSecret"
status: active
depends_on:
  - "@specs/aws/batch/meta"
---

# EksSecret

> **source:** AWS Documentation
> **spec:id:** @specs/aws/batch/docs/API_EksSecret
> **target_lang:** meta — documentation tier. ALL sections preserved.



# EksSecret
<a name="API_EksSecret"></a>

Specifies the configuration of a Kubernetes `secret` volume. For more information, see [secret](https://kubernetes.io/docs/concepts/storage/volumes/#secret) in the *Kubernetes documentation*.

## Contents
<a name="API_EksSecret_Contents"></a>

 ** secretName **   <a name="Batch-Type-EksSecret-secretName"></a>
The name of the secret. The name must be allowed as a DNS subdomain name. For more information, see [DNS subdomain names](https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#dns-subdomain-names) in the *Kubernetes documentation*.  
Type: String  
Required: Yes

 ** optional **   <a name="Batch-Type-EksSecret-optional"></a>
Specifies whether the secret or the secret's keys must be defined.  
Type: Boolean  
Required: No

## See Also
<a name="API_EksSecret_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/batch-2016-08-10/EksSecret) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/batch-2016-08-10/EksSecret) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/batch-2016-08-10/EksSecret) 