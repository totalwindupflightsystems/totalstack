---
id: "@specs/aws/rds/docs/API_DBClusterBacktrack"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS DBClusterBacktrack"
status: active
depends_on:
  - "@specs/aws/rds/meta"
---

# DBClusterBacktrack

> **source:** AWS Documentation
> **spec:id:** @specs/aws/rds/docs/API_DBClusterBacktrack
> **target_lang:** meta — documentation tier. ALL sections preserved.



# DBClusterBacktrack
<a name="API_DBClusterBacktrack"></a>

This data type is used as a response element in the `DescribeDBClusterBacktracks` action.

## Contents
<a name="API_DBClusterBacktrack_Contents"></a>

**Note**  
In the following list, the required parameters are described first.

 ** BacktrackedFrom **   
The timestamp of the time from which the DB cluster was backtracked.  
Type: Timestamp  
Required: No

 ** BacktrackIdentifier **   
Contains the backtrack identifier.  
Type: String  
Required: No

 ** BacktrackRequestCreationTime **   
The timestamp of the time at which the backtrack was requested.  
Type: Timestamp  
Required: No

 ** BacktrackTo **   
The timestamp of the time to which the DB cluster was backtracked.  
Type: Timestamp  
Required: No

 ** DBClusterIdentifier **   
Contains a user-supplied DB cluster identifier. This identifier is the unique key that identifies a DB cluster.  
Type: String  
Required: No

 ** Status **   
The status of the backtrack. This property returns one of the following values:  
+  `applying` - The backtrack is currently being applied to or rolled back from the DB cluster.
+  `completed` - The backtrack has successfully been applied to or rolled back from the DB cluster.
+  `failed` - An error occurred while the backtrack was applied to or rolled back from the DB cluster.
+  `pending` - The backtrack is currently pending application to or rollback from the DB cluster.
Type: String  
Required: No

## See Also
<a name="API_DBClusterBacktrack_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/rds-2014-10-31/DBClusterBacktrack) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/rds-2014-10-31/DBClusterBacktrack) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/rds-2014-10-31/DBClusterBacktrack) 