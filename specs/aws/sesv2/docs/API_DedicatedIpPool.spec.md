---
id: "@specs/aws/sesv2/docs/API_DedicatedIpPool"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS DedicatedIpPool"
status: active
depends_on:
  - "@specs/aws/sesv2/meta"
---

# DedicatedIpPool

> **source:** AWS Documentation
> **spec:id:** @specs/aws/sesv2/docs/API_DedicatedIpPool
> **target_lang:** meta — documentation tier. ALL sections preserved.



# DedicatedIpPool
<a name="API_DedicatedIpPool"></a>

Contains information about a dedicated IP pool.

## Contents
<a name="API_DedicatedIpPool_Contents"></a>

 ** PoolName **   <a name="SES-Type-DedicatedIpPool-PoolName"></a>
The name of the dedicated IP pool.  
Type: String  
Required: Yes

 ** ScalingMode **   <a name="SES-Type-DedicatedIpPool-ScalingMode"></a>
The type of the dedicated IP pool.  
+  `STANDARD` – A dedicated IP pool where you can control which IPs are part of the pool.
+  `MANAGED` – A dedicated IP pool where the reputation and number of IPs are automatically managed by Amazon SES.
Type: String  
Valid Values: `STANDARD | MANAGED`   
Required: Yes

## See Also
<a name="API_DedicatedIpPool_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sesv2-2019-09-27/DedicatedIpPool) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sesv2-2019-09-27/DedicatedIpPool) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sesv2-2019-09-27/DedicatedIpPool) 