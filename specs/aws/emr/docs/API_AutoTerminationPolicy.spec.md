---
id: "@specs/aws/emr/docs/API_AutoTerminationPolicy"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS AutoTerminationPolicy"
status: active
depends_on:
  - "@specs/aws/emr/meta"
---

# AutoTerminationPolicy

> **source:** AWS Documentation
> **spec:id:** @specs/aws/emr/docs/API_AutoTerminationPolicy
> **target_lang:** meta — documentation tier. ALL sections preserved.



# AutoTerminationPolicy
<a name="API_AutoTerminationPolicy"></a>

An auto-termination policy for an Amazon EMR cluster. An auto-termination policy defines the amount of idle time in seconds after which a cluster automatically terminates. For alternative cluster termination options, see [Control cluster termination](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-plan-termination.html).

## Contents
<a name="API_AutoTerminationPolicy_Contents"></a>

 ** IdleTimeout **   <a name="EMR-Type-AutoTerminationPolicy-IdleTimeout"></a>
Specifies the amount of idle time in seconds after which the cluster automatically terminates. You can specify a minimum of 60 seconds and a maximum of 604800 seconds (seven days).  
Type: Long  
Required: No

## See Also
<a name="API_AutoTerminationPolicy_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/elasticmapreduce-2009-03-31/AutoTerminationPolicy) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/elasticmapreduce-2009-03-31/AutoTerminationPolicy) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/elasticmapreduce-2009-03-31/AutoTerminationPolicy) 