---
id: "@specs/aws/docdb/docs/API_DBClusterRole"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS DBClusterRole"
status: active
depends_on:
  - "@specs/aws/docdb/meta"
---

# DBClusterRole

> **source:** AWS Documentation
> **spec:id:** @specs/aws/docdb/docs/API_DBClusterRole
> **target_lang:** meta — documentation tier. ALL sections preserved.



# DBClusterRole
<a name="API_DBClusterRole"></a>

Describes an AWS Identity and Access Management (IAM) role that is associated with a cluster.

## Contents
<a name="API_DBClusterRole_Contents"></a>

**Note**  
In the following list, the required parameters are described first.

 ** RoleArn **   
The Amazon Resource Name (ARN) of the IAMrole that is associated with the DB cluster.  
Type: String  
Required: No

 ** Status **   
Describes the state of association between the IAMrole and the cluster. The `Status` property returns one of the following values:  
+  `ACTIVE` - The IAMrole ARN is associated with the cluster and can be used to access other AWS services on your behalf.
+  `PENDING` - The IAMrole ARN is being associated with the cluster.
+  `INVALID` - The IAMrole ARN is associated with the cluster, but the cluster cannot assume the IAMrole to access other AWS services on your behalf.
Type: String  
Required: No

## See Also
<a name="API_DBClusterRole_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/docdb-2014-10-31/DBClusterRole) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/docdb-2014-10-31/DBClusterRole) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/docdb-2014-10-31/DBClusterRole) 