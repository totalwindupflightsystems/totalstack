---
id: "@specs/aws/redshift/docs/API_GetReservedNodeExchangeConfigurationOptions"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS GetReservedNodeExchangeConfigurationOptions"
status: active
depends_on:
  - "@specs/aws/redshift/meta"
---

# GetReservedNodeExchangeConfigurationOptions

> **source:** AWS Documentation
> **spec:id:** @specs/aws/redshift/docs/API_GetReservedNodeExchangeConfigurationOptions
> **target_lang:** meta — documentation tier. ALL sections preserved.



# GetReservedNodeExchangeConfigurationOptions
<a name="API_GetReservedNodeExchangeConfigurationOptions"></a>

Gets the configuration options for the reserved-node exchange. These options include information about the source reserved node and target reserved node offering. Details include the node type, the price, the node count, and the offering type.

## Request Parameters
<a name="API_GetReservedNodeExchangeConfigurationOptions_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 ** ActionType **   
The action type of the reserved-node configuration. The action type can be an exchange initiated from either a snapshot or a resize.  
Type: String  
Valid Values: `restore-cluster | resize-cluster`   
Required: Yes

 ** ClusterIdentifier **   
The identifier for the cluster that is the source for a reserved-node exchange.  
Type: String  
Length Constraints: Maximum length of 2147483647.  
Required: No

 ** Marker **   
An optional pagination token provided by a previous `GetReservedNodeExchangeConfigurationOptions` request. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by the `MaxRecords` parameter. You can retrieve the next set of response records by providing the returned marker value in the `Marker` parameter and retrying the request.  
Type: String  
Length Constraints: Maximum length of 2147483647.  
Required: No

 ** MaxRecords **   
The maximum number of response records to return in each call. If the number of remaining response records exceeds the specified `MaxRecords` value, a value is returned in a `Marker` field of the response. You can retrieve the next set of records by retrying the command with the returned marker value.  
Type: Integer  
Required: No

 ** SnapshotIdentifier **   
The identifier for the snapshot that is the source for the reserved-node exchange.  
Type: String  
Length Constraints: Maximum length of 2147483647.  
Required: No

## Response Elements
<a name="API_GetReservedNodeExchangeConfigurationOptions_ResponseElements"></a>

The following elements are returned by the service.

 ** Marker **   
A pagination token provided by a previous `GetReservedNodeExchangeConfigurationOptions` request.  
Type: String  
Length Constraints: Maximum length of 2147483647.

 **ReservedNodeConfigurationOptionList.ReservedNodeConfigurationOption.N**   
the configuration options for the reserved-node exchange. These options include information about the source reserved node and target reserved node. Details include the node type, the price, the node count, and the offering type.  
Type: Array of [ReservedNodeConfigurationOption](API_ReservedNodeConfigurationOption.md) objects

## Errors
<a name="API_GetReservedNodeExchangeConfigurationOptions_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ClusterNotFound **   
The `ClusterIdentifier` parameter does not refer to an existing cluster.   
HTTP Status Code: 404

 ** ClusterSnapshotNotFound **   
The snapshot identifier does not refer to an existing cluster snapshot.  
HTTP Status Code: 404

 ** DependentServiceUnavailableFault **   
Your request cannot be completed because a dependent internal service is temporarily unavailable. Wait 30 to 60 seconds and try again.  
HTTP Status Code: 400

 ** InvalidReservedNodeState **   
Indicates that the Reserved Node being exchanged is not in an active state.  
HTTP Status Code: 400

 ** ReservedNodeAlreadyMigrated **   
Indicates that the reserved node has already been exchanged.  
HTTP Status Code: 400

 ** ReservedNodeNotFound **   
The specified reserved compute node not found.  
HTTP Status Code: 404

 ** ReservedNodeOfferingNotFound **   
Specified offering does not exist.  
HTTP Status Code: 404

 ** UnsupportedOperation **   
The requested operation isn't supported.  
HTTP Status Code: 400

## See Also
<a name="API_GetReservedNodeExchangeConfigurationOptions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/redshift-2012-12-01/GetReservedNodeExchangeConfigurationOptions) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/redshift-2012-12-01/GetReservedNodeExchangeConfigurationOptions) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/redshift-2012-12-01/GetReservedNodeExchangeConfigurationOptions) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/redshift-2012-12-01/GetReservedNodeExchangeConfigurationOptions) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/redshift-2012-12-01/GetReservedNodeExchangeConfigurationOptions) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/redshift-2012-12-01/GetReservedNodeExchangeConfigurationOptions) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/redshift-2012-12-01/GetReservedNodeExchangeConfigurationOptions) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/redshift-2012-12-01/GetReservedNodeExchangeConfigurationOptions) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/redshift-2012-12-01/GetReservedNodeExchangeConfigurationOptions) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/redshift-2012-12-01/GetReservedNodeExchangeConfigurationOptions) 