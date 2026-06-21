---
id: "@specs/aws/rds/docs/API_ModifyDBProxyTargetGroup"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS ModifyDBProxyTargetGroup"
status: active
depends_on:
  - "@specs/aws/rds/meta"
---

# ModifyDBProxyTargetGroup

> **source:** AWS Documentation
> **spec:id:** @specs/aws/rds/docs/API_ModifyDBProxyTargetGroup
> **target_lang:** meta — documentation tier. ALL sections preserved.



# ModifyDBProxyTargetGroup
<a name="API_ModifyDBProxyTargetGroup"></a>

Modifies the properties of a `DBProxyTargetGroup`.

## Request Parameters
<a name="API_ModifyDBProxyTargetGroup_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 ** DBProxyName **   
The name of the proxy.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 63.  
Pattern: `[a-zA-Z](?:-?[a-zA-Z0-9]+)*`   
Required: Yes

 ** TargetGroupName **   
The name of the target group to modify.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 63.  
Pattern: `[a-zA-Z](?:-?[a-zA-Z0-9]+)*`   
Required: Yes

 ** ConnectionPoolConfig **   
The settings that determine the size and behavior of the connection pool for the target group.  
Type: [ConnectionPoolConfiguration](API_ConnectionPoolConfiguration.md) object  
Required: No

 ** NewName **   
The new name for the modified `DBProxyTarget`. An identifier must begin with a letter and must contain only ASCII letters, digits, and hyphens; it can't end with a hyphen or contain two consecutive hyphens.  
You can't rename the `default` target group.  
Type: String  
Required: No

## Response Elements
<a name="API_ModifyDBProxyTargetGroup_ResponseElements"></a>

The following element is returned by the service.

 ** DBProxyTargetGroup **   
The settings of the modified `DBProxyTarget`.  
Type: [DBProxyTargetGroup](API_DBProxyTargetGroup.md) object

## Errors
<a name="API_ModifyDBProxyTargetGroup_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** DBProxyNotFoundFault **   
The specified proxy name doesn't correspond to a proxy owned by your AWS account in the specified AWS Region.  
HTTP Status Code: 404

 ** DBProxyTargetGroupNotFoundFault **   
The specified target group isn't available for a proxy owned by your AWS account in the specified AWS Region.  
HTTP Status Code: 404

 ** InvalidDBProxyStateFault **   
The requested operation can't be performed while the proxy is in this state.  
HTTP Status Code: 400

## See Also
<a name="API_ModifyDBProxyTargetGroup_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/rds-2014-10-31/ModifyDBProxyTargetGroup) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/rds-2014-10-31/ModifyDBProxyTargetGroup) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/rds-2014-10-31/ModifyDBProxyTargetGroup) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/rds-2014-10-31/ModifyDBProxyTargetGroup) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/rds-2014-10-31/ModifyDBProxyTargetGroup) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/rds-2014-10-31/ModifyDBProxyTargetGroup) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/rds-2014-10-31/ModifyDBProxyTargetGroup) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/rds-2014-10-31/ModifyDBProxyTargetGroup) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/rds-2014-10-31/ModifyDBProxyTargetGroup) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/rds-2014-10-31/ModifyDBProxyTargetGroup) 