---
id: "@specs/aws/redshift/docs/API_DescribeReservedNodes"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS DescribeReservedNodes"
status: active
depends_on:
  - "@specs/aws/redshift/meta"
---

# DescribeReservedNodes

> **source:** AWS Documentation
> **spec:id:** @specs/aws/redshift/docs/API_DescribeReservedNodes
> **target_lang:** meta — documentation tier. ALL sections preserved.



# DescribeReservedNodes
<a name="API_DescribeReservedNodes"></a>

Returns the descriptions of the reserved nodes.

## Request Parameters
<a name="API_DescribeReservedNodes_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 ** Marker **   
An optional parameter that specifies the starting point to return a set of response records. When the results of a [DescribeReservedNodes](#API_DescribeReservedNodes) request exceed the value specified in `MaxRecords`, AWS returns a value in the `Marker` field of the response. You can retrieve the next set of response records by providing the returned marker value in the `Marker` parameter and retrying the request.   
Type: String  
Length Constraints: Maximum length of 2147483647.  
Required: No

 ** MaxRecords **   
The maximum number of response records to return in each call. If the number of remaining response records exceeds the specified `MaxRecords` value, a value is returned in a `marker` field of the response. You can retrieve the next set of records by retrying the command with the returned marker value.   
Default: `100`   
Constraints: minimum 20, maximum 100.  
Type: Integer  
Required: No

 ** ReservedNodeId **   
Identifier for the node reservation.  
Type: String  
Length Constraints: Maximum length of 2147483647.  
Required: No

## Response Elements
<a name="API_DescribeReservedNodes_ResponseElements"></a>

The following elements are returned by the service.

 ** Marker **   
A value that indicates the starting point for the next set of response records in a subsequent request. If a value is returned in a response, you can retrieve the next set of records by providing this returned marker value in the `Marker` parameter and retrying the command. If the `Marker` field is empty, all response records have been retrieved for the request.   
Type: String  
Length Constraints: Maximum length of 2147483647.

 **ReservedNodes.ReservedNode.N**   
The list of `ReservedNode` objects.  
Type: Array of [ReservedNode](API_ReservedNode.md) objects

## Errors
<a name="API_DescribeReservedNodes_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** DependentServiceUnavailableFault **   
Your request cannot be completed because a dependent internal service is temporarily unavailable. Wait 30 to 60 seconds and try again.  
HTTP Status Code: 400

 ** ReservedNodeNotFound **   
The specified reserved compute node not found.  
HTTP Status Code: 404

## Examples
<a name="API_DescribeReservedNodes_Examples"></a>

### Example
<a name="API_DescribeReservedNodes_Example_1"></a>

This example illustrates one usage of DescribeReservedNodes.

#### Sample Request
<a name="API_DescribeReservedNodes_Example_1_Request"></a>

```
https://redshift.us-east-2.amazonaws.com/
       ?Action=DescribeReservedNodes
&SignatureMethod=HmacSHA256&SignatureVersion=4
&Version=2012-12-01
&X-Amz-Algorithm=AWS4-HMAC-SHA256
&X-Amz-Credential=AKIAIOSFODNN7EXAMPLE/20190817/us-east-2/redshift/aws4_request
&X-Amz-Date=20190825T160000Z
&X-Amz-SignedHeaders=content-type;host;user-agent;x-amz-content-sha256;x-amz-date
&X-Amz-Signature=0aa1234bb5cc678ddddd901ee2ff3aa45678b90c12d345e6ff789012345a6b7b
```

#### Sample Response
<a name="API_DescribeReservedNodes_Example_1_Response"></a>

```
<DescribeReservedNodesResponse xmlns="http://redshift.amazonaws.com/doc/2012-12-01/">
  <DescribeReservedNodesResult>
    <ReservedNodes>
      <ReservedNode>
        <ReservedNodeId>12345678-12ab-12a1-1a2a-12ab-12a12aEXAMPLE</ReservedNodeId>
        <OfferingType>All Upfront</OfferingType>
        <ReservedNodeOfferingType>Regular</ReservedNodeOfferingType>
        <RecurringCharges>
          <RecurringCharge>
            <RecurringChargeAmount>0.0</RecurringChargeAmount>
            <RecurringChargeFrequency>Hourly</RecurringChargeFrequency>
          </RecurringCharge>
        </RecurringCharges>
        <NodeType>dc2.large</NodeType>
        <FixedPrice>1380.0</FixedPrice>
        <Duration>31536000</Duration>
        <UsagePrice>0.0</UsagePrice>
        <ReservedNodeOfferingId>12345678-12ab-12a1-1a2a-12ab-12a12bEXAMPLE</ReservedNodeOfferingId>
        <StartTime>2019-12-23T22:33:53.881Z</StartTime>
        <NodeCount>1</NodeCount>
        <State>active</State>
        <CurrencyCode>USD</CurrencyCode>
      </ReservedNode>
    </ReservedNodes>
  </DescribeReservedNodesResult>
  <ResponseMetadata>
    <RequestId>d451d255-28cd-11ea-8314-974e2ba81189</RequestId>
  </ResponseMetadata>
</DescribeReservedNodesResponse>
```

## See Also
<a name="API_DescribeReservedNodes_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/redshift-2012-12-01/DescribeReservedNodes) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/redshift-2012-12-01/DescribeReservedNodes) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/redshift-2012-12-01/DescribeReservedNodes) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/redshift-2012-12-01/DescribeReservedNodes) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/redshift-2012-12-01/DescribeReservedNodes) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/redshift-2012-12-01/DescribeReservedNodes) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/redshift-2012-12-01/DescribeReservedNodes) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/redshift-2012-12-01/DescribeReservedNodes) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/redshift-2012-12-01/DescribeReservedNodes) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/redshift-2012-12-01/DescribeReservedNodes) 