---
id: "@specs/aws/docdb/docs/API_RebootDBInstance"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS RebootDBInstance"
status: active
depends_on:
  - "@specs/aws/docdb/meta"
---

# RebootDBInstance

> **source:** AWS Documentation
> **spec:id:** @specs/aws/docdb/docs/API_RebootDBInstance
> **target_lang:** meta — documentation tier. ALL sections preserved.



# RebootDBInstance
<a name="API_RebootDBInstance"></a>

You might need to reboot your instance, usually for maintenance reasons. For example, if you make certain changes, or if you change the cluster parameter group that is associated with the instance, you must reboot the instance for the changes to take effect. 

Rebooting an instance restarts the database engine service. Rebooting an instance results in a momentary outage, during which the instance status is set to *rebooting*. 

## Request Parameters
<a name="API_RebootDBInstance_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 ** DBInstanceIdentifier **   
The instance identifier. This parameter is stored as a lowercase string.  
Constraints:  
+ Must match the identifier of an existing `DBInstance`.
Type: String  
Required: Yes

 ** ForceFailover **   
 When `true`, the reboot is conducted through a Multi-AZ failover.   
Constraint: You can't specify `true` if the instance is not configured for Multi-AZ.  
Type: Boolean  
Required: No

## Response Elements
<a name="API_RebootDBInstance_ResponseElements"></a>

The following element is returned by the service.

 ** DBInstance **   
Detailed information about an instance.   
Type: [DBInstance](API_DBInstance.md) object

## Errors
<a name="API_RebootDBInstance_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** DBInstanceNotFound **   
 `DBInstanceIdentifier` doesn't refer to an existing instance.   
HTTP Status Code: 404

 ** InvalidDBInstanceState **   
 The specified instance isn't in the *available* state.   
HTTP Status Code: 400

## See Also
<a name="API_RebootDBInstance_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/docdb-2014-10-31/RebootDBInstance) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/docdb-2014-10-31/RebootDBInstance) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/docdb-2014-10-31/RebootDBInstance) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/docdb-2014-10-31/RebootDBInstance) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/docdb-2014-10-31/RebootDBInstance) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/docdb-2014-10-31/RebootDBInstance) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/docdb-2014-10-31/RebootDBInstance) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/docdb-2014-10-31/RebootDBInstance) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/docdb-2014-10-31/RebootDBInstance) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/docdb-2014-10-31/RebootDBInstance) 