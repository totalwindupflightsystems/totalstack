---
id: "@specs/aws/rds/docs/API_DBClusterRole"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS DBClusterRole"
status: active
depends_on:
  - "@specs/aws/rds/meta"
---

# DBClusterRole

> **source:** AWS Documentation
> **spec:id:** @specs/aws/rds/docs/API_DBClusterRole
> **target_lang:** meta — documentation tier. ALL sections preserved.



# DBClusterRole
<a name="API_DBClusterRole"></a>

Describes an AWS Identity and Access Management (IAM) role that is associated with a DB cluster.

## Contents
<a name="API_DBClusterRole_Contents"></a>

**Note**  
In the following list, the required parameters are described first.

 ** FeatureName **   
The name of the feature associated with the AWS Identity and Access Management (IAM) role. For information about supported feature names, see [DBEngineVersion](API_DBEngineVersion.md).  
Type: String  
Required: No

 ** RoleArn **   
The Amazon Resource Name (ARN) of the IAM role that is associated with the DB cluster.  
Type: String  
Required: No

 ** Status **   
Describes the state of association between the IAM role and the DB cluster. The Status property returns one of the following values:  
+  `ACTIVE` - the IAM role ARN is associated with the DB cluster and can be used to access other Amazon Web Services on your behalf.
+  `PENDING` - the IAM role ARN is being associated with the DB cluster.
+  `INVALID` - the IAM role ARN is associated with the DB cluster, but the DB cluster is unable to assume the IAM role in order to access other Amazon Web Services on your behalf.
Type: String  
Required: No

## See Also
<a name="API_DBClusterRole_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/rds-2014-10-31/DBClusterRole) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/rds-2014-10-31/DBClusterRole) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/rds-2014-10-31/DBClusterRole) 