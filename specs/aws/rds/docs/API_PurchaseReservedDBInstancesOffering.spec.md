---
id: "@specs/aws/rds/docs/API_PurchaseReservedDBInstancesOffering"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS PurchaseReservedDBInstancesOffering"
status: active
depends_on:
  - "@specs/aws/rds/meta"
---

# PurchaseReservedDBInstancesOffering

> **source:** AWS Documentation
> **spec:id:** @specs/aws/rds/docs/API_PurchaseReservedDBInstancesOffering
> **target_lang:** meta — documentation tier. ALL sections preserved.



# PurchaseReservedDBInstancesOffering
<a name="API_PurchaseReservedDBInstancesOffering"></a>

Purchases a reserved DB instance offering.

## Request Parameters
<a name="API_PurchaseReservedDBInstancesOffering_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 ** ReservedDBInstancesOfferingId **   
The ID of the Reserved DB instance offering to purchase.  
Example: 438012d3-4052-4cc7-b2e3-8d3372e0e706  
Type: String  
Required: Yes

 ** DBInstanceCount **   
The number of instances to reserve.  
Default: `1`   
Type: Integer  
Required: No

 ** ReservedDBInstanceId **   
Customer-specified identifier to track this reservation.  
Example: myreservationID  
Type: String  
Required: No

 **Tags.Tag.N**   
A list of tags.  
For more information, see [Tagging Amazon RDS resources](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_Tagging.html) in the *Amazon RDS User Guide* or [Tagging Amazon Aurora and Amazon RDS resources](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/USER_Tagging.html) in the *Amazon Aurora User Guide*.   
Type: Array of [Tag](API_Tag.md) objects  
Required: No

## Response Elements
<a name="API_PurchaseReservedDBInstancesOffering_ResponseElements"></a>

The following element is returned by the service.

 ** ReservedDBInstance **   
This data type is used as a response element in the `DescribeReservedDBInstances` and `PurchaseReservedDBInstancesOffering` actions.  
Type: [ReservedDBInstance](API_ReservedDBInstance.md) object

## Errors
<a name="API_PurchaseReservedDBInstancesOffering_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ReservedDBInstanceAlreadyExists **   
User already has a reservation with the given identifier.  
HTTP Status Code: 404

 ** ReservedDBInstanceQuotaExceeded **   
Request would exceed the user's DB Instance quota.  
HTTP Status Code: 400

 ** ReservedDBInstancesOfferingNotFound **   
Specified offering does not exist.  
HTTP Status Code: 404

## Examples
<a name="API_PurchaseReservedDBInstancesOffering_Examples"></a>

### Example
<a name="API_PurchaseReservedDBInstancesOffering_Example_1"></a>

This example illustrates one usage of PurchaseReservedDBInstancesOffering.

#### Sample Request
<a name="API_PurchaseReservedDBInstancesOffering_Example_1_Request"></a>

```
https://rds.us-east-1.amazonaws.com/
   ?Action=PurchaseReservedDBInstancesOffering
   &ReservedDBInstanceId=myreservationID
   &ReservedDBInstancesOfferingId=438012d3-4052-4cc7-b2e3-8d3372e0e706
   &DBInstanceCount=10
   &SignatureMethod=HmacSHA256
   &SignatureVersion=4
   &Version=2014-10-31
   &X-Amz-Algorithm=AWS4-HMAC-SHA256
   &X-Amz-Credential=AKIADQKE4SARGYLE/20140415/us-east-1/rds/aws4_request
   &X-Amz-Date=20140415T232655Z
   &X-Amz-SignedHeaders=content-type;host;user-agent;x-amz-content-sha256;x-amz-date
   &X-Amz-Signature=c2ac761e8c8f54a8c0727f5a87ad0a766fbb0024510b9aa34ea6d1f7df52fb11
```

#### Sample Response
<a name="API_PurchaseReservedDBInstancesOffering_Example_1_Response"></a>

```
<PurchaseReservedDBInstancesOfferingResponse xmlns="http://rds.amazonaws.com/doc/2014-10-31/">
  <PurchaseReservedDBInstancesOfferingResult>
    <ReservedDBInstance>
      <OfferingType>Partial Upfront</OfferingType>
      <CurrencyCode>USD</CurrencyCode>
      <RecurringCharges/>
      <ProductDescription>mysql</ProductDescription>
      <ReservedDBInstancesOfferingId>438012d3-4052-4cc7-b2e3-8d3372e0e706</ReservedDBInstancesOfferingId>
      <MultiAZ>true</MultiAZ>
      <State>payment-pending</State>
      <ReservedDBInstanceId>myreservationID</ReservedDBInstanceId>
      <DBInstanceCount>10</DBInstanceCount>
      <StartTime>2014-05-18T23:24:56.577Z</StartTime>
      <Duration>31536000</Duration>
      <FixedPrice>123.0</FixedPrice>
      <UsagePrice>0.123</UsagePrice>
      <DBInstanceClass>db.m1.small</DBInstanceClass>
    </ReservedDBInstance>
  </PurchaseReservedDBInstancesOfferingResult>
  <ResponseMetadata>
    <RequestId>7f099901-29cf-11e1-bd06-6fe008f046c3</RequestId>
  </ResponseMetadata>
</PurchaseReservedDBInstancesOfferingResponse>
```

## See Also
<a name="API_PurchaseReservedDBInstancesOffering_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/rds-2014-10-31/PurchaseReservedDBInstancesOffering) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/rds-2014-10-31/PurchaseReservedDBInstancesOffering) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/rds-2014-10-31/PurchaseReservedDBInstancesOffering) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/rds-2014-10-31/PurchaseReservedDBInstancesOffering) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/rds-2014-10-31/PurchaseReservedDBInstancesOffering) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/rds-2014-10-31/PurchaseReservedDBInstancesOffering) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/rds-2014-10-31/PurchaseReservedDBInstancesOffering) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/rds-2014-10-31/PurchaseReservedDBInstancesOffering) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/rds-2014-10-31/PurchaseReservedDBInstancesOffering) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/rds-2014-10-31/PurchaseReservedDBInstancesOffering) 