---
id: "@specs/aws/rds/docs/API_DBInstanceRole"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS DBInstanceRole"
status: active
depends_on:
  - "@specs/aws/rds/meta"
---

# DBInstanceRole

> **source:** AWS Documentation
> **spec:id:** @specs/aws/rds/docs/API_DBInstanceRole
> **target_lang:** meta — documentation tier. ALL sections preserved.



# DBInstanceRole
<a name="API_DBInstanceRole"></a>

Information about an AWS Identity and Access Management (IAM) role that is associated with a DB instance.

## Contents
<a name="API_DBInstanceRole_Contents"></a>

**Note**  
In the following list, the required parameters are described first.

 ** FeatureName **   
The name of the feature associated with the AWS Identity and Access Management (IAM) role. For information about supported feature names, see `DBEngineVersion`.  
Type: String  
Required: No

 ** RoleArn **   
The Amazon Resource Name (ARN) of the IAM role that is associated with the DB instance.  
Type: String  
Required: No

 ** Status **   
Information about the state of association between the IAM role and the DB instance. The Status property returns one of the following values:  
+  `ACTIVE` - the IAM role ARN is associated with the DB instance and can be used to access other AWS services on your behalf.
+  `PENDING` - the IAM role ARN is being associated with the DB instance.
+  `INVALID` - the IAM role ARN is associated with the DB instance, but the DB instance is unable to assume the IAM role in order to access other AWS services on your behalf.
Type: String  
Required: No

## See Also
<a name="API_DBInstanceRole_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/rds-2014-10-31/DBInstanceRole) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/rds-2014-10-31/DBInstanceRole) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/rds-2014-10-31/DBInstanceRole) 