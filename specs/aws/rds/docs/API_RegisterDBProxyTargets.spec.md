---
id: "@specs/aws/rds/docs/API_RegisterDBProxyTargets"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS RegisterDBProxyTargets"
status: active
depends_on:
  - "@specs/aws/rds/meta"
---

# RegisterDBProxyTargets

> **source:** AWS Documentation
> **spec:id:** @specs/aws/rds/docs/API_RegisterDBProxyTargets
> **target_lang:** meta — documentation tier. ALL sections preserved.



# RegisterDBProxyTargets
<a name="API_RegisterDBProxyTargets"></a>

Associate one or more `DBProxyTarget` data structures with a `DBProxyTargetGroup`.

## Request Parameters
<a name="API_RegisterDBProxyTargets_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 ** DBProxyName **   
The identifier of the `DBProxy` that is associated with the `DBProxyTargetGroup`.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 63.  
Pattern: `[a-zA-Z](?:-?[a-zA-Z0-9]+)*`   
Required: Yes

 **DBClusterIdentifiers.member.N**   
One or more DB cluster identifiers.  
Type: Array of strings  
Required: No

 **DBInstanceIdentifiers.member.N**   
One or more DB instance identifiers.  
Type: Array of strings  
Required: No

 ** TargetGroupName **   
The identifier of the `DBProxyTargetGroup`.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 63.  
Pattern: `[a-zA-Z](?:-?[a-zA-Z0-9]+)*`   
Required: No

## Response Elements
<a name="API_RegisterDBProxyTargets_ResponseElements"></a>

The following element is returned by the service.

 **DBProxyTargets.member.N**   
One or more `DBProxyTarget` objects that are created when you register targets with a target group.  
Type: Array of [DBProxyTarget](API_DBProxyTarget.md) objects

## Errors
<a name="API_RegisterDBProxyTargets_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** DBClusterNotFoundFault **   
 `DBClusterIdentifier` doesn't refer to an existing DB cluster.  
HTTP Status Code: 404

 ** DBInstanceNotFound **   
 `DBInstanceIdentifier` doesn't refer to an existing DB instance.  
HTTP Status Code: 404

 ** DBProxyNotFoundFault **   
The specified proxy name doesn't correspond to a proxy owned by your AWS account in the specified AWS Region.  
HTTP Status Code: 404

 ** DBProxyTargetAlreadyRegisteredFault **   
The proxy is already associated with the specified RDS DB instance or Aurora DB cluster.  
HTTP Status Code: 400

 ** DBProxyTargetGroupNotFoundFault **   
The specified target group isn't available for a proxy owned by your AWS account in the specified AWS Region.  
HTTP Status Code: 404

 ** InsufficientAvailableIPsInSubnetFault **   
The requested operation can't be performed because there aren't enough available IP addresses in the proxy's subnets. Add more CIDR blocks to the VPC or remove IP address that aren't required from the subnets.  
HTTP Status Code: 400

 ** InvalidDBClusterStateFault **   
The requested operation can't be performed while the cluster is in this state.  
HTTP Status Code: 400

 ** InvalidDBInstanceState **   
The DB instance isn't in a valid state.  
HTTP Status Code: 400

 ** InvalidDBProxyStateFault **   
The requested operation can't be performed while the proxy is in this state.  
HTTP Status Code: 400

## See Also
<a name="API_RegisterDBProxyTargets_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/rds-2014-10-31/RegisterDBProxyTargets) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/rds-2014-10-31/RegisterDBProxyTargets) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/rds-2014-10-31/RegisterDBProxyTargets) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/rds-2014-10-31/RegisterDBProxyTargets) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/rds-2014-10-31/RegisterDBProxyTargets) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/rds-2014-10-31/RegisterDBProxyTargets) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/rds-2014-10-31/RegisterDBProxyTargets) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/rds-2014-10-31/RegisterDBProxyTargets) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/rds-2014-10-31/RegisterDBProxyTargets) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/rds-2014-10-31/RegisterDBProxyTargets) 