---
id: "@specs/aws/redshift/docs/API_DescribeReservedNodeExchangeStatus"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS DescribeReservedNodeExchangeStatus"
status: active
depends_on:
  - "@specs/aws/redshift/meta"
---

# DescribeReservedNodeExchangeStatus

> **source:** AWS Documentation
> **spec:id:** @specs/aws/redshift/docs/API_DescribeReservedNodeExchangeStatus
> **target_lang:** meta — documentation tier. ALL sections preserved.



# DescribeReservedNodeExchangeStatus
<a name="API_DescribeReservedNodeExchangeStatus"></a>

Returns exchange status details and associated metadata for a reserved-node exchange. Statuses include such values as in progress and requested.

## Request Parameters
<a name="API_DescribeReservedNodeExchangeStatus_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 ** Marker **   
An optional pagination token provided by a previous `DescribeReservedNodeExchangeStatus` request. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by the `MaxRecords` parameter. You can retrieve the next set of response records by providing the returned marker value in the `Marker` parameter and retrying the request.  
Type: String  
Length Constraints: Maximum length of 2147483647.  
Required: No

 ** MaxRecords **   
The maximum number of response records to return in each call. If the number of remaining response records exceeds the specified `MaxRecords` value, a value is returned in a `Marker` field of the response. You can retrieve the next set of records by retrying the command with the returned marker value.  
Type: Integer  
Required: No

 ** ReservedNodeExchangeRequestId **   
The identifier of the reserved-node exchange request.  
Type: String  
Length Constraints: Maximum length of 2147483647.  
Required: No

 ** ReservedNodeId **   
The identifier of the source reserved node in a reserved-node exchange request.  
Type: String  
Length Constraints: Maximum length of 2147483647.  
Required: No

## Response Elements
<a name="API_DescribeReservedNodeExchangeStatus_ResponseElements"></a>

The following elements are returned by the service.

 ** Marker **   
A pagination token provided by a previous `DescribeReservedNodeExchangeStatus` request.  
Type: String  
Length Constraints: Maximum length of 2147483647.

 **ReservedNodeExchangeStatusDetails.ReservedNodeExchangeStatus.N**   
The details of the reserved-node exchange request, including the status, request time, source reserved-node identifier, and additional details.  
Type: Array of [ReservedNodeExchangeStatus](API_ReservedNodeExchangeStatus.md) objects

## Errors
<a name="API_DescribeReservedNodeExchangeStatus_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ReservedNodeExchangeNotFond **   
The reserved-node exchange status wasn't found.  
HTTP Status Code: 404

 ** ReservedNodeNotFound **   
The specified reserved compute node not found.  
HTTP Status Code: 404

 ** UnsupportedOperation **   
The requested operation isn't supported.  
HTTP Status Code: 400

## See Also
<a name="API_DescribeReservedNodeExchangeStatus_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/redshift-2012-12-01/DescribeReservedNodeExchangeStatus) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/redshift-2012-12-01/DescribeReservedNodeExchangeStatus) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/redshift-2012-12-01/DescribeReservedNodeExchangeStatus) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/redshift-2012-12-01/DescribeReservedNodeExchangeStatus) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/redshift-2012-12-01/DescribeReservedNodeExchangeStatus) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/redshift-2012-12-01/DescribeReservedNodeExchangeStatus) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/redshift-2012-12-01/DescribeReservedNodeExchangeStatus) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/redshift-2012-12-01/DescribeReservedNodeExchangeStatus) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/redshift-2012-12-01/DescribeReservedNodeExchangeStatus) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/redshift-2012-12-01/DescribeReservedNodeExchangeStatus) 