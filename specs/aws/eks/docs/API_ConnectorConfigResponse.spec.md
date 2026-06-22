---
id: "@specs/aws/eks/docs/API_ConnectorConfigResponse"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS ConnectorConfigResponse"
status: active
depends_on:
  - "@specs/aws/eks/meta"
---

# ConnectorConfigResponse

> **source:** AWS Documentation
> **spec:id:** @specs/aws/eks/docs/API_ConnectorConfigResponse
> **target_lang:** meta — documentation tier. ALL sections preserved.



# ConnectorConfigResponse
<a name="API_ConnectorConfigResponse"></a>

The full description of your connected cluster.

## Contents
<a name="API_ConnectorConfigResponse_Contents"></a>

 ** activationCode **   <a name="AmazonEKS-Type-ConnectorConfigResponse-activationCode"></a>
A unique code associated with the cluster for registration purposes.  
Type: String  
Required: No

 ** activationExpiry **   <a name="AmazonEKS-Type-ConnectorConfigResponse-activationExpiry"></a>
The expiration time of the connected cluster. The cluster's YAML file must be applied through the native provider.  
Type: Timestamp  
Required: No

 ** activationId **   <a name="AmazonEKS-Type-ConnectorConfigResponse-activationId"></a>
A unique ID associated with the cluster for registration purposes.  
Type: String  
Required: No

 ** provider **   <a name="AmazonEKS-Type-ConnectorConfigResponse-provider"></a>
The cluster's cloud service provider.  
Type: String  
Required: No

 ** roleArn **   <a name="AmazonEKS-Type-ConnectorConfigResponse-roleArn"></a>
The Amazon Resource Name (ARN) of the role to communicate with services from the connected Kubernetes cluster.  
Type: String  
Required: No

## See Also
<a name="API_ConnectorConfigResponse_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/eks-2017-11-01/ConnectorConfigResponse) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/eks-2017-11-01/ConnectorConfigResponse) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/eks-2017-11-01/ConnectorConfigResponse) 