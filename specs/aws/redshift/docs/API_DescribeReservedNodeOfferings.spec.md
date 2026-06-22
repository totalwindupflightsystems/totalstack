---
id: "@specs/aws/redshift/docs/API_DescribeReservedNodeOfferings"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS DescribeReservedNodeOfferings"
status: active
depends_on:
  - "@specs/aws/redshift/meta"
---

# DescribeReservedNodeOfferings

> **source:** AWS Documentation
> **spec:id:** @specs/aws/redshift/docs/API_DescribeReservedNodeOfferings
> **target_lang:** meta — documentation tier. ALL sections preserved.



# DescribeReservedNodeOfferings
<a name="API_DescribeReservedNodeOfferings"></a>

Returns a list of the available reserved node offerings by Amazon Redshift with their descriptions including the node type, the fixed and recurring costs of reserving the node and duration the node will be reserved for you. These descriptions help you determine which reserve node offering you want to purchase. You then use the unique offering ID in you call to [PurchaseReservedNodeOffering](API_PurchaseReservedNodeOffering.md) to reserve one or more nodes for your Amazon Redshift cluster. 

 For more information about reserved node offerings, go to [Purchasing Reserved Nodes](https://docs.aws.amazon.com/redshift/latest/mgmt/purchase-reserved-node-instance.html) in the *Amazon Redshift Cluster Management Guide*.

## Request Parameters
<a name="API_DescribeReservedNodeOfferings_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 ** Marker **   
An optional parameter that specifies the starting point to return a set of response records. When the results of a [DescribeReservedNodeOfferings](#API_DescribeReservedNodeOfferings) request exceed the value specified in `MaxRecords`, AWS returns a value in the `Marker` field of the response. You can retrieve the next set of response records by providing the returned marker value in the `Marker` parameter and retrying the request.   
Type: String  
Length Constraints: Maximum length of 2147483647.  
Required: No

 ** MaxRecords **   
The maximum number of response records to return in each call. If the number of remaining response records exceeds the specified `MaxRecords` value, a value is returned in a `marker` field of the response. You can retrieve the next set of records by retrying the command with the returned marker value.   
Default: `100`   
Constraints: minimum 20, maximum 100.  
Type: Integer  
Required: No

 ** ReservedNodeOfferingId **   
The unique identifier for the offering.  
Type: String  
Length Constraints: Maximum length of 2147483647.  
Required: No

## Response Elements
<a name="API_DescribeReservedNodeOfferings_ResponseElements"></a>

The following elements are returned by the service.

 ** Marker **   
A value that indicates the starting point for the next set of response records in a subsequent request. If a value is returned in a response, you can retrieve the next set of records by providing this returned marker value in the `Marker` parameter and retrying the command. If the `Marker` field is empty, all response records have been retrieved for the request.   
Type: String  
Length Constraints: Maximum length of 2147483647.

 **ReservedNodeOfferings.ReservedNodeOffering.N**   
A list of `ReservedNodeOffering` objects.  
Type: Array of [ReservedNodeOffering](API_ReservedNodeOffering.md) objects

## Errors
<a name="API_DescribeReservedNodeOfferings_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** DependentServiceUnavailableFault **   
Your request cannot be completed because a dependent internal service is temporarily unavailable. Wait 30 to 60 seconds and try again.  
HTTP Status Code: 400

 ** ReservedNodeOfferingNotFound **   
Specified offering does not exist.  
HTTP Status Code: 404

 ** UnsupportedOperation **   
The requested operation isn't supported.  
HTTP Status Code: 400

## Examples
<a name="API_DescribeReservedNodeOfferings_Examples"></a>

### Example
<a name="API_DescribeReservedNodeOfferings_Example_1"></a>

This example illustrates one usage of DescribeReservedNodeOfferings.

#### Sample Request
<a name="API_DescribeReservedNodeOfferings_Example_1_Request"></a>

```
https://redshift.us-east-2.amazonaws.com/
       ?Action=DescribeReservedNodeOfferings
&SignatureMethod=HmacSHA256&SignatureVersion=4
&Version=2012-12-01
&X-Amz-Algorithm=AWS4-HMAC-SHA256
&X-Amz-Credential=AKIAIOSFODNN7EXAMPLE/20190817/us-east-2/redshift/aws4_request
&X-Amz-Date=20190825T160000Z
&X-Amz-SignedHeaders=content-type;host;user-agent;x-amz-content-sha256;x-amz-date
&X-Amz-Signature=0aa1234bb5cc678ddddd901ee2ff3aa45678b90c12d345e6ff789012345a6b7b
```

#### Sample Response
<a name="API_DescribeReservedNodeOfferings_Example_1_Response"></a>

```
<DescribeReservedNodeOfferingsResponse xmlns="http://redshift.amazonaws.com/doc/2012-12-01/">
  <DescribeReservedNodeOfferingsResult>
    <ReservedNodeOfferings>
      <ReservedNodeOffering>
        <Duration>94608000</Duration>
        <UsagePrice>0.0</UsagePrice>
        <ReservedNodeOfferingId>12345678-12ab-12a1-1a2a-12ab-12a12aEXAMPLE</ReservedNodeOfferingId>
        <OfferingType>No Upfront</OfferingType>
        <ReservedNodeOfferingType>Regular</ReservedNodeOfferingType>
        <RecurringCharges>
          <RecurringCharge>
            <RecurringChargeAmount>5.6724</RecurringChargeAmount>
            <RecurringChargeFrequency>Hourly</RecurringChargeFrequency>
          </RecurringCharge>
        </RecurringCharges>
        <NodeType>ra3.16xlarge</NodeType>
        <FixedPrice>0.0</FixedPrice>
        <CurrencyCode>USD</CurrencyCode>
      </ReservedNodeOffering>
      <ReservedNodeOffering>
        <Duration>31536000</Duration>
        <UsagePrice>0.0</UsagePrice>
        <ReservedNodeOfferingId>12345678-12ab-12a1-1a2a-12ab-12a12bEXAMPLE</ReservedNodeOfferingId>
        <OfferingType>Partial Upfront</OfferingType>
        <ReservedNodeOfferingType>Regular</ReservedNodeOfferingType>
        <RecurringCharges>
          <RecurringCharge>
            <RecurringChargeAmount>0.075</RecurringChargeAmount>
            <RecurringChargeFrequency>Hourly</RecurringChargeFrequency>
          </RecurringCharge>
        </RecurringCharges>
        <NodeType>dc2.large</NodeType>
        <FixedPrice>750.0</FixedPrice>
        <CurrencyCode>USD</CurrencyCode>
      </ReservedNodeOffering>
    </ReservedNodeOfferings>
  </DescribeReservedNodeOfferingsResult>
  <ResponseMetadata>
    <RequestId>680f96a7-28cd-11ea-8314-974e2ba81189</RequestId>
  </ResponseMetadata>
</DescribeReservedNodeOfferingsResponse>
```

## See Also
<a name="API_DescribeReservedNodeOfferings_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/redshift-2012-12-01/DescribeReservedNodeOfferings) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/redshift-2012-12-01/DescribeReservedNodeOfferings) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/redshift-2012-12-01/DescribeReservedNodeOfferings) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/redshift-2012-12-01/DescribeReservedNodeOfferings) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/redshift-2012-12-01/DescribeReservedNodeOfferings) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/redshift-2012-12-01/DescribeReservedNodeOfferings) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/redshift-2012-12-01/DescribeReservedNodeOfferings) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/redshift-2012-12-01/DescribeReservedNodeOfferings) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/redshift-2012-12-01/DescribeReservedNodeOfferings) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/redshift-2012-12-01/DescribeReservedNodeOfferings) 