---
id: "@specs/aws/eks/docs/API_UpdateRoleMappings"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS UpdateRoleMappings"
status: active
depends_on:
  - "@specs/aws/eks/meta"
---

# UpdateRoleMappings

> **source:** AWS Documentation
> **spec:id:** @specs/aws/eks/docs/API_UpdateRoleMappings
> **target_lang:** meta — documentation tier. ALL sections preserved.



# UpdateRoleMappings
<a name="API_UpdateRoleMappings"></a>

Updates to RBAC role mappings for an Argo CD capability. You can add, update, or remove role mappings in a single operation.

## Contents
<a name="API_UpdateRoleMappings_Contents"></a>

 ** addOrUpdateRoleMappings **   <a name="AmazonEKS-Type-UpdateRoleMappings-addOrUpdateRoleMappings"></a>
A list of role mappings to add or update. If a mapping for the specified role already exists, it will be updated with the new identities. If it doesn't exist, a new mapping will be created.  
Type: Array of [ArgoCdRoleMapping](API_ArgoCdRoleMapping.md) objects  
Required: No

 ** removeRoleMappings **   <a name="AmazonEKS-Type-UpdateRoleMappings-removeRoleMappings"></a>
A list of role mappings to remove from the RBAC configuration. Each mapping specifies an Argo CD role (`ADMIN`, `EDITOR`, or `VIEWER`) and the identities to remove from that role.  
Type: Array of [ArgoCdRoleMapping](API_ArgoCdRoleMapping.md) objects  
Required: No

## See Also
<a name="API_UpdateRoleMappings_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/eks-2017-11-01/UpdateRoleMappings) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/eks-2017-11-01/UpdateRoleMappings) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/eks-2017-11-01/UpdateRoleMappings) 