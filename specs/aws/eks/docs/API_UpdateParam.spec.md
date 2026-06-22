---
id: "@specs/aws/eks/docs/API_UpdateParam"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS UpdateParam"
status: active
depends_on:
  - "@specs/aws/eks/meta"
---

# UpdateParam

> **source:** AWS Documentation
> **spec:id:** @specs/aws/eks/docs/API_UpdateParam
> **target_lang:** meta — documentation tier. ALL sections preserved.



# UpdateParam
<a name="API_UpdateParam"></a>

An object representing the details of an update request.

## Contents
<a name="API_UpdateParam_Contents"></a>

 ** type **   <a name="AmazonEKS-Type-UpdateParam-type"></a>
The keys associated with an update request.  
Type: String  
Valid Values: `Version | PlatformVersion | EndpointPrivateAccess | EndpointPublicAccess | ClusterLogging | DesiredSize | LabelsToAdd | LabelsToRemove | TaintsToAdd | TaintsToRemove | MaxSize | MinSize | ReleaseVersion | PublicAccessCidrs | LaunchTemplateName | LaunchTemplateVersion | IdentityProviderConfig | EncryptionConfig | AddonVersion | ServiceAccountRoleArn | ResolveConflicts | MaxUnavailable | MaxUnavailablePercentage | NodeRepairEnabled | UpdateStrategy | ConfigurationValues | SecurityGroups | Subnets | AuthenticationMode | PodIdentityAssociations | UpgradePolicy | ZonalShiftConfig | ComputeConfig | StorageConfig | KubernetesNetworkConfig | RemoteNetworkConfig | DeletionProtection | NodeRepairConfig | RoleArn | RoleMappingsToAddOrUpdate | RoleMappingsToRemove | NetworkAccess | VendedLogs | UpdatedTier | PreviousTier | WarmPoolEnabled | WarmPoolMaxGroupPreparedCapacity | WarmPoolMinSize | WarmPoolState | WarmPoolReuseOnScaleIn | ControlPlaneEgressMode`   
Required: No

 ** value **   <a name="AmazonEKS-Type-UpdateParam-value"></a>
The value of the keys submitted as part of an update request.  
Type: String  
Required: No

## See Also
<a name="API_UpdateParam_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/eks-2017-11-01/UpdateParam) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/eks-2017-11-01/UpdateParam) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/eks-2017-11-01/UpdateParam) 