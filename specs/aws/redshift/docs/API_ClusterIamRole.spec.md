---
id: "@specs/aws/redshift/docs/API_ClusterIamRole"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS ClusterIamRole"
status: active
depends_on:
  - "@specs/aws/redshift/meta"
---

# ClusterIamRole

> **source:** AWS Documentation
> **spec:id:** @specs/aws/redshift/docs/API_ClusterIamRole
> **target_lang:** meta — documentation tier. ALL sections preserved.



# ClusterIamRole
<a name="API_ClusterIamRole"></a>

An AWS Identity and Access Management (IAM) role that can be used by the associated Amazon Redshift cluster to access other AWS services.

## Contents
<a name="API_ClusterIamRole_Contents"></a>

**Note**  
In the following list, the required parameters are described first.

 ** ApplyStatus **   
A value that describes the status of the IAM role's association with an Amazon Redshift cluster.  
The following are possible statuses and descriptions.  
+  `in-sync`: The role is available for use by the cluster.
+  `adding`: The role is in the process of being associated with the cluster.
+  `removing`: The role is in the process of being disassociated with the cluster.
Type: String  
Length Constraints: Maximum length of 2147483647.  
Required: No

 ** IamRoleArn **   
The Amazon Resource Name (ARN) of the IAM role, for example, `arn:aws:iam::123456789012:role/RedshiftCopyUnload`.   
Type: String  
Length Constraints: Maximum length of 2147483647.  
Required: No

## See Also
<a name="API_ClusterIamRole_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/redshift-2012-12-01/ClusterIamRole) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/redshift-2012-12-01/ClusterIamRole) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/redshift-2012-12-01/ClusterIamRole) 