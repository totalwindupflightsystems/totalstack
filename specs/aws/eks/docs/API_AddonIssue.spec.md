---
id: "@specs/aws/eks/docs/API_AddonIssue"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS AddonIssue"
status: active
depends_on:
  - "@specs/aws/eks/meta"
---

# AddonIssue

> **source:** AWS Documentation
> **spec:id:** @specs/aws/eks/docs/API_AddonIssue
> **target_lang:** meta — documentation tier. ALL sections preserved.



# AddonIssue
<a name="API_AddonIssue"></a>

An issue related to an add-on.

## Contents
<a name="API_AddonIssue_Contents"></a>

 ** code **   <a name="AmazonEKS-Type-AddonIssue-code"></a>
A code that describes the type of issue.  
Type: String  
Valid Values: `AccessDenied | InternalFailure | ClusterUnreachable | InsufficientNumberOfReplicas | ConfigurationConflict | AdmissionRequestDenied | UnsupportedAddonModification | K8sResourceNotFound | AddonSubscriptionNeeded | AddonPermissionFailure`   
Required: No

 ** message **   <a name="AmazonEKS-Type-AddonIssue-message"></a>
A message that provides details about the issue and what might cause it.  
Type: String  
Required: No

 ** resourceIds **   <a name="AmazonEKS-Type-AddonIssue-resourceIds"></a>
The resource IDs of the issue.  
Type: Array of strings  
Required: No

## See Also
<a name="API_AddonIssue_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/eks-2017-11-01/AddonIssue) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/eks-2017-11-01/AddonIssue) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/eks-2017-11-01/AddonIssue) 