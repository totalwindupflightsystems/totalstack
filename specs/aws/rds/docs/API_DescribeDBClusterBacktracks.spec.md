---
id: "@specs/aws/rds/docs/API_DescribeDBClusterBacktracks"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS DescribeDBClusterBacktracks"
status: active
depends_on:
  - "@specs/aws/rds/meta"
---

# DescribeDBClusterBacktracks

> **source:** AWS Documentation
> **spec:id:** @specs/aws/rds/docs/API_DescribeDBClusterBacktracks
> **target_lang:** meta — documentation tier. ALL sections preserved.



# DescribeDBClusterBacktracks
<a name="API_DescribeDBClusterBacktracks"></a>

Returns information about backtracks for a DB cluster.

For more information on Amazon Aurora, see [ What is Amazon Aurora?](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/CHAP_AuroraOverview.html) in the *Amazon Aurora User Guide*.

**Note**  
This action only applies to Aurora MySQL DB clusters.

## Request Parameters
<a name="API_DescribeDBClusterBacktracks_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 ** DBClusterIdentifier **   
The DB cluster identifier of the DB cluster to be described. This parameter is stored as a lowercase string.  
Constraints:  
+ Must contain from 1 to 63 alphanumeric characters or hyphens.
+ First character must be a letter.
+ Can't end with a hyphen or contain two consecutive hyphens.
Example: `my-cluster1`   
Type: String  
Required: Yes

 ** BacktrackIdentifier **   
If specified, this value is the backtrack identifier of the backtrack to be described.  
Constraints:  
+ Must contain a valid universally unique identifier (UUID). For more information about UUIDs, see [Universally unique identifier](https://en.wikipedia.org/wiki/Universally_unique_identifier).
Example: `123e4567-e89b-12d3-a456-426655440000`   
Type: String  
Required: No

 **Filters.Filter.N**   
A filter that specifies one or more DB clusters to describe. Supported filters include the following:  
+  `db-cluster-backtrack-id` - Accepts backtrack identifiers. The results list includes information about only the backtracks identified by these identifiers.
+  `db-cluster-backtrack-status` - Accepts any of the following backtrack status values:
  +  `applying` 
  +  `completed` 
  +  `failed` 
  +  `pending` 

  The results list includes information about only the backtracks identified by these values.
Type: Array of [Filter](API_Filter.md) objects  
Required: No

 ** Marker **   
An optional pagination token provided by a previous `DescribeDBClusterBacktracks` request. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by `MaxRecords`.  
Type: String  
Required: No

 ** MaxRecords **   
The maximum number of records to include in the response. If more records exist than the specified `MaxRecords` value, a pagination token called a marker is included in the response so you can retrieve the remaining results.  
Default: 100  
Constraints: Minimum 20, maximum 100.  
Type: Integer  
Required: No

## Response Elements
<a name="API_DescribeDBClusterBacktracks_ResponseElements"></a>

The following elements are returned by the service.

 **DBClusterBacktracks.DBClusterBacktrack.N**   
Contains a list of backtracks for the user.  
Type: Array of [DBClusterBacktrack](API_DBClusterBacktrack.md) objects

 ** Marker **   
A pagination token that can be used in a later `DescribeDBClusterBacktracks` request.  
Type: String

## Errors
<a name="API_DescribeDBClusterBacktracks_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** DBClusterBacktrackNotFoundFault **   
 `BacktrackIdentifier` doesn't refer to an existing backtrack.  
HTTP Status Code: 404

 ** DBClusterNotFoundFault **   
 `DBClusterIdentifier` doesn't refer to an existing DB cluster.  
HTTP Status Code: 404

## See Also
<a name="API_DescribeDBClusterBacktracks_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/rds-2014-10-31/DescribeDBClusterBacktracks) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/rds-2014-10-31/DescribeDBClusterBacktracks) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/rds-2014-10-31/DescribeDBClusterBacktracks) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/rds-2014-10-31/DescribeDBClusterBacktracks) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/rds-2014-10-31/DescribeDBClusterBacktracks) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/rds-2014-10-31/DescribeDBClusterBacktracks) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/rds-2014-10-31/DescribeDBClusterBacktracks) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/rds-2014-10-31/DescribeDBClusterBacktracks) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/rds-2014-10-31/DescribeDBClusterBacktracks) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/rds-2014-10-31/DescribeDBClusterBacktracks) 