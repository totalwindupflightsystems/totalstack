---
id: "@specs/aws/rds/docs/API_RemoveRoleFromDBInstance"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS RemoveRoleFromDBInstance"
status: active
depends_on:
  - "@specs/aws/rds/meta"
---

# RemoveRoleFromDBInstance

> **source:** AWS Documentation
> **spec:id:** @specs/aws/rds/docs/API_RemoveRoleFromDBInstance
> **target_lang:** meta — documentation tier. ALL sections preserved.



# RemoveRoleFromDBInstance
<a name="API_RemoveRoleFromDBInstance"></a>

Disassociates an AWS Identity and Access Management (IAM) role from a DB instance.

## Request Parameters
<a name="API_RemoveRoleFromDBInstance_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 ** DBInstanceIdentifier **   
The name of the DB instance to disassociate the IAM role from.  
Type: String  
Required: Yes

 ** FeatureName **   
The name of the feature for the DB instance that the IAM role is to be disassociated from. For information about supported feature names, see `DBEngineVersion`.  
Type: String  
Required: Yes

 ** RoleArn **   
The Amazon Resource Name (ARN) of the IAM role to disassociate from the DB instance, for example, `arn:aws:iam::123456789012:role/AccessRole`.  
Type: String  
Required: Yes

## Errors
<a name="API_RemoveRoleFromDBInstance_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** DBInstanceNotFound **   
 `DBInstanceIdentifier` doesn't refer to an existing DB instance.  
HTTP Status Code: 404

 ** DBInstanceRoleNotFound **   
The specified `RoleArn` value doesn't match the specified feature for the DB instance.  
HTTP Status Code: 404

 ** InvalidDBInstanceState **   
The DB instance isn't in a valid state.  
HTTP Status Code: 400

## Examples
<a name="API_RemoveRoleFromDBInstance_Examples"></a>

### Example
<a name="API_RemoveRoleFromDBInstance_Example_1"></a>

This example illustrates one usage of RemoveRoleFromDBInstance.

#### Sample Request
<a name="API_RemoveRoleFromDBInstance_Example_1_Request"></a>

```
https://rds.us-east-1.amazonaws.com/
    ?Action=RemoveRoleFromDBInstance
    &DBInstanceIdentifier=sample-instance
    &RoleArn=arn%3Aaws%3Aiam%3A%3A123456789012%3Arole%2Fsample-role
    &FeatureName=s3Import
```

## See Also
<a name="API_RemoveRoleFromDBInstance_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/rds-2014-10-31/RemoveRoleFromDBInstance) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/rds-2014-10-31/RemoveRoleFromDBInstance) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/rds-2014-10-31/RemoveRoleFromDBInstance) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/rds-2014-10-31/RemoveRoleFromDBInstance) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/rds-2014-10-31/RemoveRoleFromDBInstance) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/rds-2014-10-31/RemoveRoleFromDBInstance) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/rds-2014-10-31/RemoveRoleFromDBInstance) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/rds-2014-10-31/RemoveRoleFromDBInstance) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/rds-2014-10-31/RemoveRoleFromDBInstance) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/rds-2014-10-31/RemoveRoleFromDBInstance) 