---
id: "@specs/aws/rds/docs/API_DeregisterDBProxyTargets"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS DeregisterDBProxyTargets"
status: active
depends_on:
  - "@specs/aws/rds/meta"
---

# DeregisterDBProxyTargets

> **source:** AWS Documentation
> **spec:id:** @specs/aws/rds/docs/API_DeregisterDBProxyTargets
> **target_lang:** meta — documentation tier. ALL sections preserved.



# DeregisterDBProxyTargets
<a name="API_DeregisterDBProxyTargets"></a>

Remove the association between one or more `DBProxyTarget` data structures and a `DBProxyTargetGroup`.

## Request Parameters
<a name="API_DeregisterDBProxyTargets_RequestParameters"></a>

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

## Errors
<a name="API_DeregisterDBProxyTargets_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** DBProxyNotFoundFault **   
The specified proxy name doesn't correspond to a proxy owned by your AWS account in the specified AWS Region.  
HTTP Status Code: 404

 ** DBProxyTargetGroupNotFoundFault **   
The specified target group isn't available for a proxy owned by your AWS account in the specified AWS Region.  
HTTP Status Code: 404

 ** DBProxyTargetNotFoundFault **   
The specified RDS DB instance or Aurora DB cluster isn't available for a proxy owned by your AWS account in the specified AWS Region.  
HTTP Status Code: 404

 ** InvalidDBProxyStateFault **   
The requested operation can't be performed while the proxy is in this state.  
HTTP Status Code: 400

## See Also
<a name="API_DeregisterDBProxyTargets_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/rds-2014-10-31/DeregisterDBProxyTargets) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/rds-2014-10-31/DeregisterDBProxyTargets) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/rds-2014-10-31/DeregisterDBProxyTargets) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/rds-2014-10-31/DeregisterDBProxyTargets) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/rds-2014-10-31/DeregisterDBProxyTargets) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/rds-2014-10-31/DeregisterDBProxyTargets) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/rds-2014-10-31/DeregisterDBProxyTargets) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/rds-2014-10-31/DeregisterDBProxyTargets) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/rds-2014-10-31/DeregisterDBProxyTargets) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/rds-2014-10-31/DeregisterDBProxyTargets) 