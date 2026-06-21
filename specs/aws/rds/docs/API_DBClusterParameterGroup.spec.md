---
id: "@specs/aws/rds/docs/API_DBClusterParameterGroup"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS DBClusterParameterGroup"
status: active
depends_on:
  - "@specs/aws/rds/meta"
---

# DBClusterParameterGroup

> **source:** AWS Documentation
> **spec:id:** @specs/aws/rds/docs/API_DBClusterParameterGroup
> **target_lang:** meta — documentation tier. ALL sections preserved.



# DBClusterParameterGroup
<a name="API_DBClusterParameterGroup"></a>

Contains the details of an Amazon RDS DB cluster parameter group.

This data type is used as a response element in the `DescribeDBClusterParameterGroups` action.

## Contents
<a name="API_DBClusterParameterGroup_Contents"></a>

**Note**  
In the following list, the required parameters are described first.

 ** DBClusterParameterGroupArn **   
The Amazon Resource Name (ARN) for the DB cluster parameter group.  
Type: String  
Required: No

 ** DBClusterParameterGroupName **   
The name of the DB cluster parameter group.  
Type: String  
Required: No

 ** DBParameterGroupFamily **   
The name of the DB parameter group family that this DB cluster parameter group is compatible with.  
Type: String  
Required: No

 ** Description **   
Provides the customer-specified description for this DB cluster parameter group.  
Type: String  
Required: No

## See Also
<a name="API_DBClusterParameterGroup_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/rds-2014-10-31/DBClusterParameterGroup) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/rds-2014-10-31/DBClusterParameterGroup) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/rds-2014-10-31/DBClusterParameterGroup) 