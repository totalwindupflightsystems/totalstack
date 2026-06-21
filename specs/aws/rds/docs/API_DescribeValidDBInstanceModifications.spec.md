---
id: "@specs/aws/rds/docs/API_DescribeValidDBInstanceModifications"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS DescribeValidDBInstanceModifications"
status: active
depends_on:
  - "@specs/aws/rds/meta"
---

# DescribeValidDBInstanceModifications

> **source:** AWS Documentation
> **spec:id:** @specs/aws/rds/docs/API_DescribeValidDBInstanceModifications
> **target_lang:** meta — documentation tier. ALL sections preserved.



# DescribeValidDBInstanceModifications
<a name="API_DescribeValidDBInstanceModifications"></a>

You can call `DescribeValidDBInstanceModifications` to learn what modifications you can make to your DB instance. You can use this information when you call `ModifyDBInstance`.

This command doesn't apply to RDS Custom.

## Request Parameters
<a name="API_DescribeValidDBInstanceModifications_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 ** DBInstanceIdentifier **   
The customer identifier or the ARN of your DB instance.  
Type: String  
Required: Yes

## Response Elements
<a name="API_DescribeValidDBInstanceModifications_ResponseElements"></a>

The following element is returned by the service.

 ** ValidDBInstanceModificationsMessage **   
Information about valid modifications that you can make to your DB instance. Contains the result of a successful call to the `DescribeValidDBInstanceModifications` action. You can use this information when you call `ModifyDBInstance`.  
Type: [ValidDBInstanceModificationsMessage](API_ValidDBInstanceModificationsMessage.md) object

## Errors
<a name="API_DescribeValidDBInstanceModifications_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** DBInstanceNotFound **   
 `DBInstanceIdentifier` doesn't refer to an existing DB instance.  
HTTP Status Code: 404

 ** InvalidDBInstanceState **   
The DB instance isn't in a valid state.  
HTTP Status Code: 400

## See Also
<a name="API_DescribeValidDBInstanceModifications_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/rds-2014-10-31/DescribeValidDBInstanceModifications) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/rds-2014-10-31/DescribeValidDBInstanceModifications) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/rds-2014-10-31/DescribeValidDBInstanceModifications) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/rds-2014-10-31/DescribeValidDBInstanceModifications) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/rds-2014-10-31/DescribeValidDBInstanceModifications) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/rds-2014-10-31/DescribeValidDBInstanceModifications) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/rds-2014-10-31/DescribeValidDBInstanceModifications) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/rds-2014-10-31/DescribeValidDBInstanceModifications) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/rds-2014-10-31/DescribeValidDBInstanceModifications) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/rds-2014-10-31/DescribeValidDBInstanceModifications) 