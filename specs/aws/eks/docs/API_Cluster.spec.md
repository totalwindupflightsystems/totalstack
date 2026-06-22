---
id: "@specs/aws/eks/docs/API_Cluster"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Cluster"
status: active
depends_on:
  - "@specs/aws/eks/meta"
---

# Cluster

> **source:** AWS Documentation
> **spec:id:** @specs/aws/eks/docs/API_Cluster
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Cluster
<a name="API_Cluster"></a>

An object representing an Amazon EKS cluster.

## Contents
<a name="API_Cluster_Contents"></a>

 ** accessConfig **   <a name="AmazonEKS-Type-Cluster-accessConfig"></a>
The access configuration for the cluster.  
Type: [AccessConfigResponse](API_AccessConfigResponse.md) object  
Required: No

 ** arn **   <a name="AmazonEKS-Type-Cluster-arn"></a>
The Amazon Resource Name (ARN) of the cluster.  
Type: String  
Required: No

 ** certificateAuthority **   <a name="AmazonEKS-Type-Cluster-certificateAuthority"></a>
The `certificate-authority-data` for your cluster.  
Type: [Certificate](API_Certificate.md) object  
Required: No

 ** clientRequestToken **   <a name="AmazonEKS-Type-Cluster-clientRequestToken"></a>
A unique, case-sensitive identifier that you provide to ensure the idempotency of the request.  
Type: String  
Required: No

 ** computeConfig **   <a name="AmazonEKS-Type-Cluster-computeConfig"></a>
Indicates the current configuration of the compute capability on your EKS Auto Mode cluster. For example, if the capability is enabled or disabled. If the compute capability is enabled, EKS Auto Mode will create and delete EC2 Managed Instances in your AWS account. For more information, see EKS Auto Mode compute capability in the *Amazon EKS User Guide*.  
Type: [ComputeConfigResponse](API_ComputeConfigResponse.md) object  
Required: No

 ** connectorConfig **   <a name="AmazonEKS-Type-Cluster-connectorConfig"></a>
The configuration used to connect to a cluster for registration.  
Type: [ConnectorConfigResponse](API_ConnectorConfigResponse.md) object  
Required: No

 ** controlPlaneScalingConfig **   <a name="AmazonEKS-Type-Cluster-controlPlaneScalingConfig"></a>
The control plane scaling tier configuration. For more information, see EKS Provisioned Control Plane in the Amazon EKS User Guide.  
Type: [ControlPlaneScalingConfig](API_ControlPlaneScalingConfig.md) object  
Required: No

 ** createdAt **   <a name="AmazonEKS-Type-Cluster-createdAt"></a>
The Unix epoch timestamp at object creation.  
Type: Timestamp  
Required: No

 ** deletionProtection **   <a name="AmazonEKS-Type-Cluster-deletionProtection"></a>
The current deletion protection setting for the cluster. When `true`, deletion protection is enabled and the cluster cannot be deleted until protection is disabled. When `false`, the cluster can be deleted normally. This setting only applies to clusters in an active state.  
Type: Boolean  
Required: No

 ** encryptionConfig **   <a name="AmazonEKS-Type-Cluster-encryptionConfig"></a>
The encryption configuration for the cluster.  
Type: Array of [EncryptionConfig](API_EncryptionConfig.md) objects  
Array Members: Maximum number of 1 item.  
Required: No

 ** endpoint **   <a name="AmazonEKS-Type-Cluster-endpoint"></a>
The endpoint for your Kubernetes API server.  
Type: String  
Required: No

 ** health **   <a name="AmazonEKS-Type-Cluster-health"></a>
An object representing the health of your Amazon EKS cluster.  
Type: [ClusterHealth](API_ClusterHealth.md) object  
Required: No

 ** id **   <a name="AmazonEKS-Type-Cluster-id"></a>
The ID of your local Amazon EKS cluster on an AWS Outpost. This property isn't available for an Amazon EKS cluster on the AWS cloud.  
Type: String  
Required: No

 ** identity **   <a name="AmazonEKS-Type-Cluster-identity"></a>
The identity provider information for the cluster.  
Type: [Identity](API_Identity.md) object  
Required: No

 ** kubernetesNetworkConfig **   <a name="AmazonEKS-Type-Cluster-kubernetesNetworkConfig"></a>
The Kubernetes network configuration for the cluster.  
Type: [KubernetesNetworkConfigResponse](API_KubernetesNetworkConfigResponse.md) object  
Required: No

 ** logging **   <a name="AmazonEKS-Type-Cluster-logging"></a>
The logging configuration for your cluster.  
Type: [Logging](API_Logging.md) object  
Required: No

 ** name **   <a name="AmazonEKS-Type-Cluster-name"></a>
The name of your cluster.  
Type: String  
Required: No

 ** outpostConfig **   <a name="AmazonEKS-Type-Cluster-outpostConfig"></a>
An object representing the configuration of your local Amazon EKS cluster on an AWS Outpost. This object isn't available for clusters on the AWS cloud.  
Type: [OutpostConfigResponse](API_OutpostConfigResponse.md) object  
Required: No

 ** platformVersion **   <a name="AmazonEKS-Type-Cluster-platformVersion"></a>
The platform version of your Amazon EKS cluster. For more information about clusters deployed on the AWS Cloud, see [Platform versions](https://docs.aws.amazon.com/eks/latest/userguide/platform-versions.html) in the * *Amazon EKS User Guide* *. For more information about local clusters deployed on an Outpost, see [Amazon EKS local cluster platform versions](https://docs.aws.amazon.com/eks/latest/userguide/eks-outposts-platform-versions.html) in the * *Amazon EKS User Guide* *.  
Type: String  
Required: No

 ** remoteNetworkConfig **   <a name="AmazonEKS-Type-Cluster-remoteNetworkConfig"></a>
The configuration in the cluster for EKS Hybrid Nodes. You can add, change, or remove this configuration after the cluster is created.  
Type: [RemoteNetworkConfigResponse](API_RemoteNetworkConfigResponse.md) object  
Required: No

 ** resourcesVpcConfig **   <a name="AmazonEKS-Type-Cluster-resourcesVpcConfig"></a>
The VPC configuration used by the cluster control plane. Amazon EKS VPC resources have specific requirements to work properly with Kubernetes. For more information, see [Cluster VPC considerations](https://docs.aws.amazon.com/eks/latest/userguide/network_reqs.html) and [Cluster security group considerations](https://docs.aws.amazon.com/eks/latest/userguide/sec-group-reqs.html) in the *Amazon EKS User Guide*.  
Type: [VpcConfigResponse](API_VpcConfigResponse.md) object  
Required: No

 ** roleArn **   <a name="AmazonEKS-Type-Cluster-roleArn"></a>
The Amazon Resource Name (ARN) of the IAM role that provides permissions for the Kubernetes control plane to make calls to AWS API operations on your behalf.  
Type: String  
Required: No

 ** status **   <a name="AmazonEKS-Type-Cluster-status"></a>
The current status of the cluster.  
Type: String  
Valid Values: `CREATING | ACTIVE | DELETING | FAILED | UPDATING | PENDING`   
Required: No

 ** storageConfig **   <a name="AmazonEKS-Type-Cluster-storageConfig"></a>
Indicates the current configuration of the block storage capability on your EKS Auto Mode cluster. For example, if the capability is enabled or disabled. If the block storage capability is enabled, EKS Auto Mode will create and delete EBS volumes in your AWS account. For more information, see EKS Auto Mode block storage capability in the *Amazon EKS User Guide*.  
Type: [StorageConfigResponse](API_StorageConfigResponse.md) object  
Required: No

 ** tags **   <a name="AmazonEKS-Type-Cluster-tags"></a>
Metadata that assists with categorization and organization. Each tag consists of a key and an optional value. You define both. Tags don't propagate to any other cluster or AWS resources.  
Type: String to string map  
Map Entries: Maximum number of 50 items.  
Key Length Constraints: Minimum length of 1. Maximum length of 128.  
Value Length Constraints: Maximum length of 256.  
Required: No

 ** upgradePolicy **   <a name="AmazonEKS-Type-Cluster-upgradePolicy"></a>
This value indicates if extended support is enabled or disabled for the cluster.  
 [Learn more about EKS Extended Support in the *Amazon EKS User Guide*.](https://docs.aws.amazon.com/eks/latest/userguide/extended-support-control.html)   
Type: [UpgradePolicyResponse](API_UpgradePolicyResponse.md) object  
Required: No

 ** version **   <a name="AmazonEKS-Type-Cluster-version"></a>
The Kubernetes server version for the cluster.  
Type: String  
Required: No

 ** zonalShiftConfig **   <a name="AmazonEKS-Type-Cluster-zonalShiftConfig"></a>
The configuration for zonal shift for the cluster.  
Type: [ZonalShiftConfigResponse](API_ZonalShiftConfigResponse.md) object  
Required: No

## See Also
<a name="API_Cluster_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/eks-2017-11-01/Cluster) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/eks-2017-11-01/Cluster) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/eks-2017-11-01/Cluster) 