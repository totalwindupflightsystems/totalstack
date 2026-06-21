---
id: "@specs/aws/rds/docs/API_BacktrackDBCluster"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS BacktrackDBCluster"
status: active
depends_on:
  - "@specs/aws/rds/meta"
---

# BacktrackDBCluster

> **source:** AWS Documentation
> **spec:id:** @specs/aws/rds/docs/API_BacktrackDBCluster
> **target_lang:** meta — documentation tier. ALL sections preserved.



# BacktrackDBCluster
<a name="API_BacktrackDBCluster"></a>

Backtracks a DB cluster to a specific time, without creating a new DB cluster.

For more information on backtracking, see [ Backtracking an Aurora DB Cluster](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraMySQL.Managing.Backtrack.html) in the *Amazon Aurora User Guide*.

**Note**  
This action applies only to Aurora MySQL DB clusters.

## Request Parameters
<a name="API_BacktrackDBCluster_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 ** BacktrackTo **   
The timestamp of the time to backtrack the DB cluster to, specified in ISO 8601 format. For more information about ISO 8601, see the [ISO8601 Wikipedia page.](http://en.wikipedia.org/wiki/ISO_8601)   
If the specified time isn't a consistent time for the DB cluster, Aurora automatically chooses the nearest possible consistent time for the DB cluster.
Constraints:  
+ Must contain a valid ISO 8601 timestamp.
+ Can't contain a timestamp set in the future.
Example: `2017-07-08T18:00Z`   
Type: Timestamp  
Required: Yes

 ** DBClusterIdentifier **   
The DB cluster identifier of the DB cluster to be backtracked. This parameter is stored as a lowercase string.  
Constraints:  
+ Must contain from 1 to 63 alphanumeric characters or hyphens.
+ First character must be a letter.
+ Can't end with a hyphen or contain two consecutive hyphens.
Example: `my-cluster1`   
Type: String  
Required: Yes

 ** Force **   
Specifies whether to force the DB cluster to backtrack when binary logging is enabled. Otherwise, an error occurs when binary logging is enabled.  
Type: Boolean  
Required: No

 ** UseEarliestTimeOnPointInTimeUnavailable **   
Specifies whether to backtrack the DB cluster to the earliest possible backtrack time when *BacktrackTo* is set to a timestamp earlier than the earliest backtrack time. When this parameter is disabled and *BacktrackTo* is set to a timestamp earlier than the earliest backtrack time, an error occurs.  
Type: Boolean  
Required: No

## Response Elements
<a name="API_BacktrackDBCluster_ResponseElements"></a>

The following elements are returned by the service.

 ** BacktrackedFrom **   
The timestamp of the time from which the DB cluster was backtracked.  
Type: Timestamp

 ** BacktrackIdentifier **   
Contains the backtrack identifier.  
Type: String

 ** BacktrackRequestCreationTime **   
The timestamp of the time at which the backtrack was requested.  
Type: Timestamp

 ** BacktrackTo **   
The timestamp of the time to which the DB cluster was backtracked.  
Type: Timestamp

 ** DBClusterIdentifier **   
Contains a user-supplied DB cluster identifier. This identifier is the unique key that identifies a DB cluster.  
Type: String

 ** Status **   
The status of the backtrack. This property returns one of the following values:  
+  `applying` - The backtrack is currently being applied to or rolled back from the DB cluster.
+  `completed` - The backtrack has successfully been applied to or rolled back from the DB cluster.
+  `failed` - An error occurred while the backtrack was applied to or rolled back from the DB cluster.
+  `pending` - The backtrack is currently pending application to or rollback from the DB cluster.
Type: String

## Errors
<a name="API_BacktrackDBCluster_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** DBClusterNotFoundFault **   
 `DBClusterIdentifier` doesn't refer to an existing DB cluster.  
HTTP Status Code: 404

 ** InvalidDBClusterStateFault **   
The requested operation can't be performed while the cluster is in this state.  
HTTP Status Code: 400

## See Also
<a name="API_BacktrackDBCluster_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/rds-2014-10-31/BacktrackDBCluster) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/rds-2014-10-31/BacktrackDBCluster) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/rds-2014-10-31/BacktrackDBCluster) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/rds-2014-10-31/BacktrackDBCluster) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/rds-2014-10-31/BacktrackDBCluster) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/rds-2014-10-31/BacktrackDBCluster) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/rds-2014-10-31/BacktrackDBCluster) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/rds-2014-10-31/BacktrackDBCluster) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/rds-2014-10-31/BacktrackDBCluster) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/rds-2014-10-31/BacktrackDBCluster) 