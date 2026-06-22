---
id: "@specs/aws/batch/docs/API_EksHostPath"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS EksHostPath"
status: active
depends_on:
  - "@specs/aws/batch/meta"
---

# EksHostPath

> **source:** AWS Documentation
> **spec:id:** @specs/aws/batch/docs/API_EksHostPath
> **target_lang:** meta — documentation tier. ALL sections preserved.



# EksHostPath
<a name="API_EksHostPath"></a>

Specifies the configuration of a Kubernetes `hostPath` volume. A `hostPath` volume mounts an existing file or directory from the host node's filesystem into your pod. For more information, see [hostPath](https://kubernetes.io/docs/concepts/storage/volumes/#hostpath) in the *Kubernetes documentation*.

## Contents
<a name="API_EksHostPath_Contents"></a>

 ** path **   <a name="Batch-Type-EksHostPath-path"></a>
The path of the file or directory on the host to mount into containers on the pod.  
Type: String  
Required: No

## See Also
<a name="API_EksHostPath_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/batch-2016-08-10/EksHostPath) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/batch-2016-08-10/EksHostPath) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/batch-2016-08-10/EksHostPath) 