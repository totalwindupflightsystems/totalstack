---
id: "@specs/aws/docdb/docs/API_DeleteDBInstance"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS DeleteDBInstance"
status: active
depends_on:
  - "@specs/aws/docdb/meta"
---

# DeleteDBInstance

> **source:** AWS Documentation
> **spec:id:** @specs/aws/docdb/docs/API_DeleteDBInstance
> **target_lang:** meta — documentation tier. ALL sections preserved.



# DeleteDBInstance
<a name="API_DeleteDBInstance"></a>

Deletes a previously provisioned instance.

## Request Parameters
<a name="API_DeleteDBInstance_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 ** DBInstanceIdentifier **   
The instance identifier for the instance to be deleted. This parameter isn't case sensitive.  
Constraints:  
+ Must match the name of an existing instance.
Type: String  
Required: Yes

## Response Elements
<a name="API_DeleteDBInstance_ResponseElements"></a>

The following element is returned by the service.

 ** DBInstance **   
Detailed information about an instance.   
Type: [DBInstance](API_DBInstance.md) object

## Errors
<a name="API_DeleteDBInstance_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** DBInstanceNotFound **   
 `DBInstanceIdentifier` doesn't refer to an existing instance.   
HTTP Status Code: 404

 ** DBSnapshotAlreadyExists **   
 `DBSnapshotIdentifier` is already being used by an existing snapshot.   
HTTP Status Code: 400

 ** InvalidDBClusterStateFault **   
The cluster isn't in a valid state.  
HTTP Status Code: 400

 ** InvalidDBInstanceState **   
 The specified instance isn't in the *available* state.   
HTTP Status Code: 400

 ** SnapshotQuotaExceeded **   
The request would cause you to exceed the allowed number of snapshots.  
HTTP Status Code: 400

## See Also
<a name="API_DeleteDBInstance_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/docdb-2014-10-31/DeleteDBInstance) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/docdb-2014-10-31/DeleteDBInstance) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/docdb-2014-10-31/DeleteDBInstance) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/docdb-2014-10-31/DeleteDBInstance) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/docdb-2014-10-31/DeleteDBInstance) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/docdb-2014-10-31/DeleteDBInstance) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/docdb-2014-10-31/DeleteDBInstance) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/docdb-2014-10-31/DeleteDBInstance) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/docdb-2014-10-31/DeleteDBInstance) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/docdb-2014-10-31/DeleteDBInstance) 