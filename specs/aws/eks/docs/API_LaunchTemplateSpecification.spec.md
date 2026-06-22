---
id: "@specs/aws/eks/docs/API_LaunchTemplateSpecification"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS LaunchTemplateSpecification"
status: active
depends_on:
  - "@specs/aws/eks/meta"
---

# LaunchTemplateSpecification

> **source:** AWS Documentation
> **spec:id:** @specs/aws/eks/docs/API_LaunchTemplateSpecification
> **target_lang:** meta — documentation tier. ALL sections preserved.



# LaunchTemplateSpecification
<a name="API_LaunchTemplateSpecification"></a>

An object representing a node group launch template specification. The launch template can't include [https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CreateNetworkInterface.html](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CreateNetworkInterface.html), [https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_IamInstanceProfile.html](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_IamInstanceProfile.html), [https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_RequestSpotInstances.html](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_RequestSpotInstances.html), [https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_HibernationOptionsRequest.html](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_HibernationOptionsRequest.html), or [https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_TerminateInstances.html](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_TerminateInstances.html), or the node group deployment or update will fail. For more information about launch templates, see [https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CreateLaunchTemplate.html](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CreateLaunchTemplate.html) in the Amazon EC2 API Reference. For more information about using launch templates with Amazon EKS, see [Customizing managed nodes with launch templates](https://docs.aws.amazon.com/eks/latest/userguide/launch-templates.html) in the *Amazon EKS User Guide*.

You must specify either the launch template ID or the launch template name in the request, but not both.

## Contents
<a name="API_LaunchTemplateSpecification_Contents"></a>

 ** id **   <a name="AmazonEKS-Type-LaunchTemplateSpecification-id"></a>
The ID of the launch template.  
You must specify either the launch template ID or the launch template name in the request, but not both. After node group creation, you cannot use a different ID.  
Type: String  
Required: No

 ** name **   <a name="AmazonEKS-Type-LaunchTemplateSpecification-name"></a>
The name of the launch template.  
You must specify either the launch template name or the launch template ID in the request, but not both. After node group creation, you cannot use a different name.  
Type: String  
Required: No

 ** version **   <a name="AmazonEKS-Type-LaunchTemplateSpecification-version"></a>
The version number of the launch template to use. If no version is specified, then the template's default version is used. You can use a different version for node group updates.  
Type: String  
Required: No

## See Also
<a name="API_LaunchTemplateSpecification_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/eks-2017-11-01/LaunchTemplateSpecification) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/eks-2017-11-01/LaunchTemplateSpecification) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/eks-2017-11-01/LaunchTemplateSpecification) 