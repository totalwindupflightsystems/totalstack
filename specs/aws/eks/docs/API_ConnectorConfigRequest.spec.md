---
id: "@specs/aws/eks/docs/API_ConnectorConfigRequest"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS ConnectorConfigRequest"
status: active
depends_on:
  - "@specs/aws/eks/meta"
---

# ConnectorConfigRequest

> **source:** AWS Documentation
> **spec:id:** @specs/aws/eks/docs/API_ConnectorConfigRequest
> **target_lang:** meta — documentation tier. ALL sections preserved.



# ConnectorConfigRequest
<a name="API_ConnectorConfigRequest"></a>

The configuration sent to a cluster for configuration.

## Contents
<a name="API_ConnectorConfigRequest_Contents"></a>

 ** provider **   <a name="AmazonEKS-Type-ConnectorConfigRequest-provider"></a>
The cloud provider for the target cluster to connect.  
Type: String  
Valid Values: `EKS_ANYWHERE | ANTHOS | GKE | AKS | OPENSHIFT | TANZU | RANCHER | EC2 | OTHER`   
Required: Yes

 ** roleArn **   <a name="AmazonEKS-Type-ConnectorConfigRequest-roleArn"></a>
The Amazon Resource Name (ARN) of the role that is authorized to request the connector configuration.  
Type: String  
Required: Yes

## See Also
<a name="API_ConnectorConfigRequest_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/eks-2017-11-01/ConnectorConfigRequest) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/eks-2017-11-01/ConnectorConfigRequest) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/eks-2017-11-01/ConnectorConfigRequest) 