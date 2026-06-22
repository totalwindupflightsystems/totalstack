---
id: "@specs/aws/eks/docs/API_ClusterVersionInformation"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS ClusterVersionInformation"
status: active
depends_on:
  - "@specs/aws/eks/meta"
---

# ClusterVersionInformation

> **source:** AWS Documentation
> **spec:id:** @specs/aws/eks/docs/API_ClusterVersionInformation
> **target_lang:** meta — documentation tier. ALL sections preserved.



# ClusterVersionInformation
<a name="API_ClusterVersionInformation"></a>

Contains details about a specific EKS cluster version.

## Contents
<a name="API_ClusterVersionInformation_Contents"></a>

 ** clusterType **   <a name="AmazonEKS-Type-ClusterVersionInformation-clusterType"></a>
The type of cluster this version is for.  
Type: String  
Required: No

 ** clusterVersion **   <a name="AmazonEKS-Type-ClusterVersionInformation-clusterVersion"></a>
The Kubernetes version for the cluster.  
Type: String  
Required: No

 ** defaultPlatformVersion **   <a name="AmazonEKS-Type-ClusterVersionInformation-defaultPlatformVersion"></a>
Default platform version for this Kubernetes version.  
Type: String  
Required: No

 ** defaultVersion **   <a name="AmazonEKS-Type-ClusterVersionInformation-defaultVersion"></a>
Indicates if this is a default version.  
Type: Boolean  
Required: No

 ** endOfExtendedSupportDate **   <a name="AmazonEKS-Type-ClusterVersionInformation-endOfExtendedSupportDate"></a>
Date when extended support ends for this version.  
Type: Timestamp  
Required: No

 ** endOfStandardSupportDate **   <a name="AmazonEKS-Type-ClusterVersionInformation-endOfStandardSupportDate"></a>
Date when standard support ends for this version.  
Type: Timestamp  
Required: No

 ** kubernetesPatchVersion **   <a name="AmazonEKS-Type-ClusterVersionInformation-kubernetesPatchVersion"></a>
The patch version of Kubernetes for this cluster version.  
Type: String  
Required: No

 ** releaseDate **   <a name="AmazonEKS-Type-ClusterVersionInformation-releaseDate"></a>
The release date of this cluster version.  
Type: Timestamp  
Required: No

 ** status **   <a name="AmazonEKS-Type-ClusterVersionInformation-status"></a>
This field is deprecated. Use `versionStatus` instead, as that field matches for input and output of this action.
Current status of this cluster version.  
Type: String  
Valid Values: `unsupported | standard-support | extended-support`   
Required: No

 ** versionStatus **   <a name="AmazonEKS-Type-ClusterVersionInformation-versionStatus"></a>
Current status of this cluster version.  
Type: String  
Valid Values: `UNSUPPORTED | STANDARD_SUPPORT | EXTENDED_SUPPORT`   
Required: No

## See Also
<a name="API_ClusterVersionInformation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/eks-2017-11-01/ClusterVersionInformation) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/eks-2017-11-01/ClusterVersionInformation) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/eks-2017-11-01/ClusterVersionInformation) 