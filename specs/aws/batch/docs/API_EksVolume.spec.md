---
id: "@specs/aws/batch/docs/API_EksVolume"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS EksVolume"
status: active
depends_on:
  - "@specs/aws/batch/meta"
---

# EksVolume

> **source:** AWS Documentation
> **spec:id:** @specs/aws/batch/docs/API_EksVolume
> **target_lang:** meta — documentation tier. ALL sections preserved.



# EksVolume
<a name="API_EksVolume"></a>

Specifies an Amazon EKS volume for a job definition.

## Contents
<a name="API_EksVolume_Contents"></a>

 ** name **   <a name="Batch-Type-EksVolume-name"></a>
The name of the volume. The name must be allowed as a DNS subdomain name. For more information, see [DNS subdomain names](https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#dns-subdomain-names) in the *Kubernetes documentation*.  
Type: String  
Required: Yes

 ** emptyDir **   <a name="Batch-Type-EksVolume-emptyDir"></a>
Specifies the configuration of a Kubernetes `emptyDir` volume. For more information, see [emptyDir](https://kubernetes.io/docs/concepts/storage/volumes/#emptydir) in the *Kubernetes documentation*.  
Type: [EksEmptyDir](API_EksEmptyDir.md) object  
Required: No

 ** hostPath **   <a name="Batch-Type-EksVolume-hostPath"></a>
Specifies the configuration of a Kubernetes `hostPath` volume. For more information, see [hostPath](https://kubernetes.io/docs/concepts/storage/volumes/#hostpath) in the *Kubernetes documentation*.  
Type: [EksHostPath](API_EksHostPath.md) object  
Required: No

 ** persistentVolumeClaim **   <a name="Batch-Type-EksVolume-persistentVolumeClaim"></a>
Specifies the configuration of a Kubernetes `persistentVolumeClaim` bounded to a `persistentVolume`. For more information, see [ Persistent Volume Claims](https://kubernetes.io/docs/concepts/storage/persistent-volumes/#persistentvolumeclaims) in the *Kubernetes documentation*.  
Type: [EksPersistentVolumeClaim](API_EksPersistentVolumeClaim.md) object  
Required: No

 ** secret **   <a name="Batch-Type-EksVolume-secret"></a>
Specifies the configuration of a Kubernetes `secret` volume. For more information, see [secret](https://kubernetes.io/docs/concepts/storage/volumes/#secret) in the *Kubernetes documentation*.  
Type: [EksSecret](API_EksSecret.md) object  
Required: No

## See Also
<a name="API_EksVolume_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/batch-2016-08-10/EksVolume) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/batch-2016-08-10/EksVolume) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/batch-2016-08-10/EksVolume) 