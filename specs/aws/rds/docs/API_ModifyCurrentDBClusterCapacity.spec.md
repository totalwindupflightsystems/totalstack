---
id: "@specs/aws/rds/docs/API_ModifyCurrentDBClusterCapacity"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS ModifyCurrentDBClusterCapacity"
status: active
depends_on:
  - "@specs/aws/rds/meta"
---

# ModifyCurrentDBClusterCapacity

> **source:** AWS Documentation
> **spec:id:** @specs/aws/rds/docs/API_ModifyCurrentDBClusterCapacity
> **target_lang:** meta — documentation tier. ALL sections preserved.



# ModifyCurrentDBClusterCapacity
<a name="API_ModifyCurrentDBClusterCapacity"></a>

Set the capacity of an Aurora Serverless v1 DB cluster to a specific value.

Aurora Serverless v1 scales seamlessly based on the workload on the DB cluster. In some cases, the capacity might not scale fast enough to meet a sudden change in workload, such as a large number of new transactions. Call `ModifyCurrentDBClusterCapacity` to set the capacity explicitly.

After this call sets the DB cluster capacity, Aurora Serverless v1 can automatically scale the DB cluster based on the cooldown period for scaling up and the cooldown period for scaling down.

For more information about Aurora Serverless v1, see [Using Amazon Aurora Serverless v1](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/aurora-serverless.html) in the *Amazon Aurora User Guide*.

**Important**  
If you call `ModifyCurrentDBClusterCapacity` with the default `TimeoutAction`, connections that prevent Aurora Serverless v1 from finding a scaling point might be dropped. For more information about scaling points, see [ Autoscaling for Aurora Serverless v1](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/aurora-serverless.how-it-works.html#aurora-serverless.how-it-works.auto-scaling) in the *Amazon Aurora User Guide*.

**Note**  
This operation only applies to Aurora Serverless v1 DB clusters.

## Request Parameters
<a name="API_ModifyCurrentDBClusterCapacity_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 ** DBClusterIdentifier **   
The DB cluster identifier for the cluster being modified. This parameter isn't case-sensitive.  
Constraints:  
+ Must match the identifier of an existing DB cluster.
Type: String  
Required: Yes

 ** Capacity **   
The DB cluster capacity.  
When you change the capacity of a paused Aurora Serverless v1 DB cluster, it automatically resumes.  
Constraints:  
+ For Aurora MySQL, valid capacity values are `1`, `2`, `4`, `8`, `16`, `32`, `64`, `128`, and `256`.
+ For Aurora PostgreSQL, valid capacity values are `2`, `4`, `8`, `16`, `32`, `64`, `192`, and `384`.
Type: Integer  
Required: No

 ** SecondsBeforeTimeout **   
The amount of time, in seconds, that Aurora Serverless v1 tries to find a scaling point to perform seamless scaling before enforcing the timeout action. The default is 300.  
Specify a value between 10 and 600 seconds.  
Type: Integer  
Required: No

 ** TimeoutAction **   
The action to take when the timeout is reached, either `ForceApplyCapacityChange` or `RollbackCapacityChange`.  
 `ForceApplyCapacityChange`, the default, sets the capacity to the specified value as soon as possible.  
 `RollbackCapacityChange` ignores the capacity change if a scaling point isn't found in the timeout period.  
Type: String  
Required: No

## Response Elements
<a name="API_ModifyCurrentDBClusterCapacity_ResponseElements"></a>

The following elements are returned by the service.

 ** CurrentCapacity **   
The current capacity of the DB cluster.  
Type: Integer

 ** DBClusterIdentifier **   
A user-supplied DB cluster identifier. This identifier is the unique key that identifies a DB cluster.  
Type: String

 ** PendingCapacity **   
A value that specifies the capacity that the DB cluster scales to next.  
Type: Integer

 ** SecondsBeforeTimeout **   
The number of seconds before a call to `ModifyCurrentDBClusterCapacity` times out.  
Type: Integer

 ** TimeoutAction **   
The timeout action of a call to `ModifyCurrentDBClusterCapacity`, either `ForceApplyCapacityChange` or `RollbackCapacityChange`.  
Type: String

## Errors
<a name="API_ModifyCurrentDBClusterCapacity_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** DBClusterNotFoundFault **   
 `DBClusterIdentifier` doesn't refer to an existing DB cluster.  
HTTP Status Code: 404

 ** InvalidDBClusterCapacityFault **   
 `Capacity` isn't a valid Aurora Serverless DB cluster capacity. Valid capacity values are `2`, `4`, `8`, `16`, `32`, `64`, `128`, and `256`.  
HTTP Status Code: 400

 ** InvalidDBClusterStateFault **   
The requested operation can't be performed while the cluster is in this state.  
HTTP Status Code: 400

## See Also
<a name="API_ModifyCurrentDBClusterCapacity_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/rds-2014-10-31/ModifyCurrentDBClusterCapacity) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/rds-2014-10-31/ModifyCurrentDBClusterCapacity) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/rds-2014-10-31/ModifyCurrentDBClusterCapacity) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/rds-2014-10-31/ModifyCurrentDBClusterCapacity) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/rds-2014-10-31/ModifyCurrentDBClusterCapacity) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/rds-2014-10-31/ModifyCurrentDBClusterCapacity) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/rds-2014-10-31/ModifyCurrentDBClusterCapacity) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/rds-2014-10-31/ModifyCurrentDBClusterCapacity) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/rds-2014-10-31/ModifyCurrentDBClusterCapacity) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/rds-2014-10-31/ModifyCurrentDBClusterCapacity) 