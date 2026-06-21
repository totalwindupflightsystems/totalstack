---
id: "@specs/aws/rds/docs/API_DescribeReservedDBInstancesOfferings"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS DescribeReservedDBInstancesOfferings"
status: active
depends_on:
  - "@specs/aws/rds/meta"
---

# DescribeReservedDBInstancesOfferings

> **source:** AWS Documentation
> **spec:id:** @specs/aws/rds/docs/API_DescribeReservedDBInstancesOfferings
> **target_lang:** meta — documentation tier. ALL sections preserved.



# DescribeReservedDBInstancesOfferings
<a name="API_DescribeReservedDBInstancesOfferings"></a>

Lists available reserved DB instance offerings.

## Request Parameters
<a name="API_DescribeReservedDBInstancesOfferings_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 ** DBInstanceClass **   
The DB instance class filter value. Specify this parameter to show only the available offerings matching the specified DB instance class.  
Type: String  
Required: No

 ** Duration **   
Duration filter value, specified in years or seconds. Specify this parameter to show only reservations for this duration.  
Valid Values: `1 | 3 | 31536000 | 94608000`   
Type: String  
Required: No

 **Filters.Filter.N**   
This parameter isn't currently supported.  
Type: Array of [Filter](API_Filter.md) objects  
Required: No

 ** Marker **   
An optional pagination token provided by a previous request. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by `MaxRecords`.  
Type: String  
Required: No

 ** MaxRecords **   
The maximum number of records to include in the response. If more than the `MaxRecords` value is available, a pagination token called a marker is included in the response so you can retrieve the remaining results.  
Default: 100  
Constraints: Minimum 20, maximum 100.  
Type: Integer  
Required: No

 ** MultiAZ **   
Specifies whether to show only those reservations that support Multi-AZ.  
Type: Boolean  
Required: No

 ** OfferingType **   
The offering type filter value. Specify this parameter to show only the available offerings matching the specified offering type.  
Valid Values: `"Partial Upfront" | "All Upfront" | "No Upfront" `   
Type: String  
Required: No

 ** ProductDescription **   
Product description filter value. Specify this parameter to show only the available offerings that contain the specified product description.  
The results show offerings that partially match the filter value.
Type: String  
Required: No

 ** ReservedDBInstancesOfferingId **   
The offering identifier filter value. Specify this parameter to show only the available offering that matches the specified reservation identifier.  
Example: `438012d3-4052-4cc7-b2e3-8d3372e0e706`   
Type: String  
Required: No

## Response Elements
<a name="API_DescribeReservedDBInstancesOfferings_ResponseElements"></a>

The following elements are returned by the service.

 ** Marker **   
An optional pagination token provided by a previous request. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by `MaxRecords`.  
Type: String

 **ReservedDBInstancesOfferings.ReservedDBInstancesOffering.N**   
A list of reserved DB instance offerings.  
Type: Array of [ReservedDBInstancesOffering](API_ReservedDBInstancesOffering.md) objects

## Errors
<a name="API_DescribeReservedDBInstancesOfferings_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ReservedDBInstancesOfferingNotFound **   
Specified offering does not exist.  
HTTP Status Code: 404

## Examples
<a name="API_DescribeReservedDBInstancesOfferings_Examples"></a>

### Example
<a name="API_DescribeReservedDBInstancesOfferings_Example_1"></a>

This example illustrates one usage of DescribeReservedDBInstancesOfferings.

#### Sample Request
<a name="API_DescribeReservedDBInstancesOfferings_Example_1_Request"></a>

```
https://rds.us-east-1.amazonaws.com/
   ?Action=DescribeReservedDBInstancesOfferings
   &ReservedDBInstancesOfferingId=438012d3-4052-4cc7-b2e3-8d3372e0e706
   &SignatureMethod=HmacSHA256
   &SignatureVersion=4
   &Version=2014-10-31
   &X-Amz-Algorithm=AWS4-HMAC-SHA256
   &X-Amz-Credential=AKIADQKE4SARGYLE/20140411/us-east-1/rds/aws4_request
   &X-Amz-Date=20140411T203327Z
   &X-Amz-SignedHeaders=content-type;host;user-agent;x-amz-content-sha256;x-amz-date
   &X-Amz-Signature=545f04acffeb4b80d2e778526b1c9da79d0b3097151c24f28e83e851d65422e2
```

#### Sample Response
<a name="API_DescribeReservedDBInstancesOfferings_Example_1_Response"></a>

```
<DescribeReservedDBInstancesOfferingsResponse xmlns="http://rds.amazonaws.com/doc/2014-10-31/">
  <DescribeReservedDBInstancesOfferingsResult>
    <ReservedDBInstancesOfferings>
      <ReservedDBInstancesOffering>
        <Duration>31536000</Duration>
        <OfferingType>Partial Upfront</OfferingType>
        <CurrencyCode>USD</CurrencyCode>
        <RecurringCharges>          
          <RecurringCharge>
            <RecurringChargeFrequency>Hourly</RecurringChargeFrequency>
            <RecurringChargeAmount>0.123</RecurringChargeAmount>
          </RecurringCharge>
        </RecurringCharges>
        <FixedPrice>162.0</FixedPrice>
        <ProductDescription>mysql</ProductDescription>
        <UsagePrice>0.0</UsagePrice>
        <MultiAZ>false</MultiAZ>
        <ReservedDBInstancesOfferingId>SampleOfferingId</ReservedDBInstancesOfferingId>
        <DBInstanceClass>db.m1.small</DBInstanceClass>
      </ReservedDBInstancesOffering>
    </ReservedDBInstancesOfferings>
  </DescribeReservedDBInstancesOfferingsResult>
  <ResponseMetadata>
    <RequestId>521b420a-2961-11e1-bd06-6fe008f046c3</RequestId>
  </ResponseMetadata>
</DescribeReservedDBInstancesOfferingsResponse>
```

## See Also
<a name="API_DescribeReservedDBInstancesOfferings_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/rds-2014-10-31/DescribeReservedDBInstancesOfferings) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/rds-2014-10-31/DescribeReservedDBInstancesOfferings) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/rds-2014-10-31/DescribeReservedDBInstancesOfferings) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/rds-2014-10-31/DescribeReservedDBInstancesOfferings) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/rds-2014-10-31/DescribeReservedDBInstancesOfferings) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/rds-2014-10-31/DescribeReservedDBInstancesOfferings) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/rds-2014-10-31/DescribeReservedDBInstancesOfferings) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/rds-2014-10-31/DescribeReservedDBInstancesOfferings) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/rds-2014-10-31/DescribeReservedDBInstancesOfferings) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/rds-2014-10-31/DescribeReservedDBInstancesOfferings) 