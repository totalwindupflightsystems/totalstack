---
id: "@specs/aws/docdb/docs/API_ApplyPendingMaintenanceAction"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS ApplyPendingMaintenanceAction"
status: active
depends_on:
  - "@specs/aws/docdb/meta"
---

# ApplyPendingMaintenanceAction

> **source:** AWS Documentation
> **spec:id:** @specs/aws/docdb/docs/API_ApplyPendingMaintenanceAction
> **target_lang:** meta — documentation tier. ALL sections preserved.



# ApplyPendingMaintenanceAction
<a name="API_ApplyPendingMaintenanceAction"></a>

Applies a pending maintenance action to a resource (for example, to an Amazon DocumentDB instance).

## Request Parameters
<a name="API_ApplyPendingMaintenanceAction_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 ** ApplyAction **   
The pending maintenance action to apply to this resource.  
Valid values: `system-update`, `db-upgrade`   
Type: String  
Required: Yes

 ** OptInType **   
A value that specifies the type of opt-in request or undoes an opt-in request. An opt-in request of type `immediate` can't be undone.  
Valid values:  
+  `immediate` - Apply the maintenance action immediately.
+  `next-maintenance` - Apply the maintenance action during the next maintenance window for the resource. 
+  `undo-opt-in` - Cancel any existing `next-maintenance` opt-in requests.
Type: String  
Required: Yes

 ** ResourceIdentifier **   
The Amazon Resource Name (ARN) of the resource that the pending maintenance action applies to.  
Type: String  
Required: Yes

## Response Elements
<a name="API_ApplyPendingMaintenanceAction_ResponseElements"></a>

The following element is returned by the service.

 ** ResourcePendingMaintenanceActions **   
Represents the output of [ApplyPendingMaintenanceAction](#API_ApplyPendingMaintenanceAction).   
Type: [ResourcePendingMaintenanceActions](API_ResourcePendingMaintenanceActions.md) object

## Errors
<a name="API_ApplyPendingMaintenanceAction_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InvalidDBClusterStateFault **   
The cluster isn't in a valid state.  
HTTP Status Code: 400

 ** InvalidDBInstanceState **   
 The specified instance isn't in the *available* state.   
HTTP Status Code: 400

 ** ResourceNotFoundFault **   
The specified resource ID was not found.  
HTTP Status Code: 404

## See Also
<a name="API_ApplyPendingMaintenanceAction_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/docdb-2014-10-31/ApplyPendingMaintenanceAction) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/docdb-2014-10-31/ApplyPendingMaintenanceAction) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/docdb-2014-10-31/ApplyPendingMaintenanceAction) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/docdb-2014-10-31/ApplyPendingMaintenanceAction) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/docdb-2014-10-31/ApplyPendingMaintenanceAction) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/docdb-2014-10-31/ApplyPendingMaintenanceAction) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/docdb-2014-10-31/ApplyPendingMaintenanceAction) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/docdb-2014-10-31/ApplyPendingMaintenanceAction) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/docdb-2014-10-31/ApplyPendingMaintenanceAction) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/docdb-2014-10-31/ApplyPendingMaintenanceAction) 