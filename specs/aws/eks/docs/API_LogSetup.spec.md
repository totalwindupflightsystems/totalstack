---
id: "@specs/aws/eks/docs/API_LogSetup"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS LogSetup"
status: active
depends_on:
  - "@specs/aws/eks/meta"
---

# LogSetup

> **source:** AWS Documentation
> **spec:id:** @specs/aws/eks/docs/API_LogSetup
> **target_lang:** meta — documentation tier. ALL sections preserved.



# LogSetup
<a name="API_LogSetup"></a>

An object representing the enabled or disabled Kubernetes control plane logs for your cluster.

## Contents
<a name="API_LogSetup_Contents"></a>

 ** enabled **   <a name="AmazonEKS-Type-LogSetup-enabled"></a>
If a log type is enabled, that log type exports its control plane logs to CloudWatch Logs . If a log type isn't enabled, that log type doesn't export its control plane logs. Each individual log type can be enabled or disabled independently.  
Type: Boolean  
Required: No

 ** types **   <a name="AmazonEKS-Type-LogSetup-types"></a>
The available cluster control plane log types.  
Type: Array of strings  
Valid Values: `api | audit | authenticator | controllerManager | scheduler`   
Required: No

## See Also
<a name="API_LogSetup_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/eks-2017-11-01/LogSetup) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/eks-2017-11-01/LogSetup) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/eks-2017-11-01/LogSetup) 