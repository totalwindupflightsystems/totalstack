---
id: "@specs/aws/batch/docs/API_EksPersistentVolumeClaim"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS EksPersistentVolumeClaim"
status: active
depends_on:
  - "@specs/aws/batch/meta"
---

# EksPersistentVolumeClaim

> **source:** AWS Documentation
> **spec:id:** @specs/aws/batch/docs/API_EksPersistentVolumeClaim
> **target_lang:** meta — documentation tier. ALL sections preserved.



# EksPersistentVolumeClaim
<a name="API_EksPersistentVolumeClaim"></a>

A `persistentVolumeClaim` volume is used to mount a [PersistentVolume](https://kubernetes.io/docs/concepts/storage/persistent-volumes/) into a Pod. PersistentVolumeClaims are a way for users to "claim" durable storage without knowing the details of the particular cloud environment. See the information about [PersistentVolumes](https://kubernetes.io/docs/concepts/storage/persistent-volumes/) in the *Kubernetes documentation*.

## Contents
<a name="API_EksPersistentVolumeClaim_Contents"></a>

 ** claimName **   <a name="Batch-Type-EksPersistentVolumeClaim-claimName"></a>
The name of the `persistentVolumeClaim` bounded to a `persistentVolume`. For more information, see [ Persistent Volume Claims](https://kubernetes.io/docs/concepts/storage/persistent-volumes/#persistentvolumeclaims) in the *Kubernetes documentation*.  
Type: String  
Required: Yes

 ** readOnly **   <a name="Batch-Type-EksPersistentVolumeClaim-readOnly"></a>
An optional boolean value indicating if the mount is read only. Default is false. For more information, see [ Read Only Mounts](https://kubernetes.io/docs/concepts/storage/volumes/#read-only-mounts) in the *Kubernetes documentation*.  
Type: Boolean  
Required: No

## See Also
<a name="API_EksPersistentVolumeClaim_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/batch-2016-08-10/EksPersistentVolumeClaim) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/batch-2016-08-10/EksPersistentVolumeClaim) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/batch-2016-08-10/EksPersistentVolumeClaim) 