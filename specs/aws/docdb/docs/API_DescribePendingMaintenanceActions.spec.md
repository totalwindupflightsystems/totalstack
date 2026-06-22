---
id: "@specs/aws/docdb/docs/API_DescribePendingMaintenanceActions"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS DescribePendingMaintenanceActions"
status: active
depends_on:
  - "@specs/aws/docdb/meta"
---

# DescribePendingMaintenanceActions

> **source:** AWS Documentation
> **spec:id:** @specs/aws/docdb/docs/API_DescribePendingMaintenanceActions
> **target_lang:** meta — documentation tier. ALL sections preserved.



# DescribePendingMaintenanceActions
<a name="API_DescribePendingMaintenanceActions"></a>

Returns a list of resources (for example, instances) that have at least one pending maintenance action.

## Request Parameters
<a name="API_DescribePendingMaintenanceActions_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 **Filters.Filter.N**   
A filter that specifies one or more resources to return pending maintenance actions for.  
Supported filters:  
+  `db-cluster-id` - Accepts cluster identifiers and cluster Amazon Resource Names (ARNs). The results list includes only pending maintenance actions for the clusters identified by these ARNs.
+  `db-instance-id` - Accepts instance identifiers and instance ARNs. The results list includes only pending maintenance actions for the DB instances identified by these ARNs.
Type: Array of [Filter](API_Filter.md) objects  
Required: No

 ** Marker **   
An optional pagination token provided by a previous request. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by `MaxRecords`.  
Type: String  
Required: No

 ** MaxRecords **   
 The maximum number of records to include in the response. If more records exist than the specified `MaxRecords` value, a pagination token (marker) is included in the response so that the remaining results can be retrieved.  
Default: 100  
Constraints: Minimum 20, maximum 100.  
Type: Integer  
Required: No

 ** ResourceIdentifier **   
The ARN of a resource to return pending maintenance actions for.  
Type: String  
Required: No

## Response Elements
<a name="API_DescribePendingMaintenanceActions_ResponseElements"></a>

The following elements are returned by the service.

 ** Marker **   
An optional pagination token provided by a previous request. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by `MaxRecords`.  
Type: String

 **PendingMaintenanceActions.ResourcePendingMaintenanceActions.N**   
The maintenance actions to be applied.  
Type: Array of [ResourcePendingMaintenanceActions](API_ResourcePendingMaintenanceActions.md) objects

## Errors
<a name="API_DescribePendingMaintenanceActions_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ResourceNotFoundFault **   
The specified resource ID was not found.  
HTTP Status Code: 404

## See Also
<a name="API_DescribePendingMaintenanceActions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/docdb-2014-10-31/DescribePendingMaintenanceActions) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/docdb-2014-10-31/DescribePendingMaintenanceActions) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/docdb-2014-10-31/DescribePendingMaintenanceActions) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/docdb-2014-10-31/DescribePendingMaintenanceActions) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/docdb-2014-10-31/DescribePendingMaintenanceActions) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/docdb-2014-10-31/DescribePendingMaintenanceActions) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/docdb-2014-10-31/DescribePendingMaintenanceActions) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/docdb-2014-10-31/DescribePendingMaintenanceActions) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/docdb-2014-10-31/DescribePendingMaintenanceActions) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/docdb-2014-10-31/DescribePendingMaintenanceActions) 