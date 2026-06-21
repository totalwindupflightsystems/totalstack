---
id: "@specs/aws/rds/docs/API_DescribeReservedDBInstances"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS DescribeReservedDBInstances"
status: active
depends_on:
  - "@specs/aws/rds/meta"
---

# DescribeReservedDBInstances

> **source:** AWS Documentation
> **spec:id:** @specs/aws/rds/docs/API_DescribeReservedDBInstances
> **target_lang:** meta — documentation tier. ALL sections preserved.



# DescribeReservedDBInstances
<a name="API_DescribeReservedDBInstances"></a>

Returns information about reserved DB instances for this account, or about a specified reserved DB instance.

## Request Parameters
<a name="API_DescribeReservedDBInstances_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 ** DBInstanceClass **   
The DB instance class filter value. Specify this parameter to show only those reservations matching the specified DB instances class.  
Type: String  
Required: No

 ** Duration **   
The duration filter value, specified in years or seconds. Specify this parameter to show only reservations for this duration.  
Valid Values: `1 | 3 | 31536000 | 94608000`   
Type: String  
Required: No

 **Filters.Filter.N**   
This parameter isn't currently supported.  
Type: Array of [Filter](API_Filter.md) objects  
Required: No

 ** LeaseId **   
The lease identifier filter value. Specify this parameter to show only the reservation that matches the specified lease ID.  
 AWS Support might request the lease ID for an issue related to a reserved DB instance.
Type: String  
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
The product description filter value. Specify this parameter to show only those reservations matching the specified product description.  
Type: String  
Required: No

 ** ReservedDBInstanceId **   
The reserved DB instance identifier filter value. Specify this parameter to show only the reservation that matches the specified reservation ID.  
Type: String  
Required: No

 ** ReservedDBInstancesOfferingId **   
The offering identifier filter value. Specify this parameter to show only purchased reservations matching the specified offering identifier.  
Type: String  
Required: No

## Response Elements
<a name="API_DescribeReservedDBInstances_ResponseElements"></a>

The following elements are returned by the service.

 ** Marker **   
An optional pagination token provided by a previous request. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by `MaxRecords`.  
Type: String

 **ReservedDBInstances.ReservedDBInstance.N**   
A list of reserved DB instances.  
Type: Array of [ReservedDBInstance](API_ReservedDBInstance.md) objects

## Errors
<a name="API_DescribeReservedDBInstances_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ReservedDBInstanceNotFound **   
The specified reserved DB Instance not found.  
HTTP Status Code: 404

## Examples
<a name="API_DescribeReservedDBInstances_Examples"></a>

### Example
<a name="API_DescribeReservedDBInstances_Example_1"></a>

This example illustrates one usage of DescribeReservedDBInstances.

#### Sample Request
<a name="API_DescribeReservedDBInstances_Example_1_Request"></a>

```
https://rds.us-west-2.amazonaws.com/
   ?Action=DescribeReservedDBInstances
   &ReservedDBInstanceId=customerSpecifiedID
   &SignatureMethod=HmacSHA256 
   &SignatureVersion=4
   &Version=2014-10-31
   &X-Amz-Algorithm=AWS4-HMAC-SHA256
   &X-Amz-Credential=AKIADQKE4SARGYLE/20140420/us-west-2/rds/aws4_request
   &X-Amz-Date=20140420T162211Z
   &X-Amz-SignedHeaders=content-type;host;user-agent;x-amz-content-sha256;x-amz-date
   &X-Amz-Signature=3312d17a4c43bcd209bc22a0778dd23e73f8434254abbd7ac53b89ade3dae88e
```

#### Sample Response
<a name="API_DescribeReservedDBInstances_Example_1_Response"></a>

```
<DescribeReservedDBInstancesResponse xmlns="http://rds.amazonaws.com/doc/2014-10-31/">
  <DescribeReservedDBInstancesResult>
    <ReservedDBInstances>
      <ReservedDBInstance>
        <OfferingType>Partial Upfront</OfferingType>
        <CurrencyCode>USD</CurrencyCode>
        <RecurringCharges/>
        <ProductDescription>mysql</ProductDescription>
        <ReservedDBInstancesOfferingId>649fd0c8-cf6d-47a0-bfa6-060f8e75e95f</ReservedDBInstancesOfferingId>
        <MultiAZ>false</MultiAZ>
        <State>active</State>
        <ReservedDBInstanceId>myreservationid</ReservedDBInstanceId>
        <DBInstanceCount>1</DBInstanceCount>
        <StartTime>2014-05-15T00:25:14.131Z</StartTime>
        <Duration>31536000</Duration>
        <FixedPrice>227.5</FixedPrice>
        <UsagePrice>0.046</UsagePrice>
        <DBInstanceClass>db.m1.small</DBInstanceClass>
      </ReservedDBInstance>      
  </DescribeReservedDBInstancesResult>
  <ResponseMetadata>
    <RequestId>c695119b-2961-11e1-bd06-6fe008f046c3</RequestId>
  </ResponseMetadata>
</DescribeReservedDBInstancesResponse>
```

## See Also
<a name="API_DescribeReservedDBInstances_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/rds-2014-10-31/DescribeReservedDBInstances) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/rds-2014-10-31/DescribeReservedDBInstances) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/rds-2014-10-31/DescribeReservedDBInstances) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/rds-2014-10-31/DescribeReservedDBInstances) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/rds-2014-10-31/DescribeReservedDBInstances) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/rds-2014-10-31/DescribeReservedDBInstances) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/rds-2014-10-31/DescribeReservedDBInstances) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/rds-2014-10-31/DescribeReservedDBInstances) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/rds-2014-10-31/DescribeReservedDBInstances) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/rds-2014-10-31/DescribeReservedDBInstances) 