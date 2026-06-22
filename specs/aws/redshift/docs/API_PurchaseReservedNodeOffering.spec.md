---
id: "@specs/aws/redshift/docs/API_PurchaseReservedNodeOffering"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS PurchaseReservedNodeOffering"
status: active
depends_on:
  - "@specs/aws/redshift/meta"
---

# PurchaseReservedNodeOffering

> **source:** AWS Documentation
> **spec:id:** @specs/aws/redshift/docs/API_PurchaseReservedNodeOffering
> **target_lang:** meta — documentation tier. ALL sections preserved.



# PurchaseReservedNodeOffering
<a name="API_PurchaseReservedNodeOffering"></a>

Allows you to purchase reserved nodes. Amazon Redshift offers a predefined set of reserved node offerings. You can purchase one or more of the offerings. You can call the [DescribeReservedNodeOfferings](API_DescribeReservedNodeOfferings.md) API to obtain the available reserved node offerings. You can call this API by providing a specific reserved node offering and the number of nodes you want to reserve. 

 For more information about reserved node offerings, go to [Purchasing Reserved Nodes](https://docs.aws.amazon.com/redshift/latest/mgmt/purchase-reserved-node-instance.html) in the *Amazon Redshift Cluster Management Guide*.

## Request Parameters
<a name="API_PurchaseReservedNodeOffering_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 ** ReservedNodeOfferingId **   
The unique identifier of the reserved node offering you want to purchase.  
Type: String  
Length Constraints: Maximum length of 2147483647.  
Required: Yes

 ** NodeCount **   
The number of reserved nodes that you want to purchase.  
Default: `1`   
Type: Integer  
Required: No

## Response Elements
<a name="API_PurchaseReservedNodeOffering_ResponseElements"></a>

The following element is returned by the service.

 ** ReservedNode **   
Describes a reserved node. You can call the [DescribeReservedNodeOfferings](API_DescribeReservedNodeOfferings.md) API to obtain the available reserved node offerings.   
Type: [ReservedNode](API_ReservedNode.md) object

## Errors
<a name="API_PurchaseReservedNodeOffering_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ReservedNodeAlreadyExists **   
User already has a reservation with the given identifier.  
HTTP Status Code: 404

 ** ReservedNodeOfferingNotFound **   
Specified offering does not exist.  
HTTP Status Code: 404

 ** ReservedNodeQuotaExceeded **   
Request would exceed the user's compute node quota. For information about increasing your quota, go to [Limits in Amazon Redshift](https://docs.aws.amazon.com/redshift/latest/mgmt/amazon-redshift-limits.html) in the *Amazon Redshift Cluster Management Guide*.   
HTTP Status Code: 400

 ** UnsupportedOperation **   
The requested operation isn't supported.  
HTTP Status Code: 400

## Examples
<a name="API_PurchaseReservedNodeOffering_Examples"></a>

### Example
<a name="API_PurchaseReservedNodeOffering_Example_1"></a>

This example illustrates one usage of PurchaseReservedNodeOffering.

#### Sample Request
<a name="API_PurchaseReservedNodeOffering_Example_1_Request"></a>

```
https://redshift.us-east-2.amazonaws.com/
       ?Action=PurchaseReservedNodeOffering
&ReservedNodeOfferingId=12345678-12ab-12a1-1a2a-12ab-12a12bEXAMPLE
&SignatureMethod=HmacSHA256&SignatureVersion=4
&Version=2012-12-01
&X-Amz-Algorithm=AWS4-HMAC-SHA256
&X-Amz-Credential=AKIAIOSFODNN7EXAMPLE/20190817/us-east-2/redshift/aws4_request
&X-Amz-Date=20190825T160000Z
&X-Amz-SignedHeaders=content-type;host;user-agent;x-amz-content-sha256;x-amz-date
&X-Amz-Signature=0aa1234bb5cc678ddddd901ee2ff3aa45678b90c12d345e6ff789012345a6b7b
```

#### Sample Response
<a name="API_PurchaseReservedNodeOffering_Example_1_Response"></a>

```
<PurchaseReservedNodeOfferingResponse xmlns="http://redshift.amazonaws.com/doc/2012-12-01/">
  <PurchaseReservedNodeOfferingResult>
    <ReservedNode>
      <ReservedNodeId>12345678-12ab-12a1-1a2a-12ab-12a12aEXAMPLE</ReservedNodeId>
      <OfferingType>All Upfront</OfferingType>
      <ReservedNodeOfferingType>Regular</ReservedNodeOfferingType>
      <RecurringCharges/>
      <NodeType>ra3.4xlarge</NodeType>
      <FixedPrice>4295.0</FixedPrice>
      <Duration>31536000</Duration>
      <UsagePrice>0.0</UsagePrice>
      <ReservedNodeOfferingId>12345678-12ab-12a1-1a2a-12ab-12a12bEXAMPLE</ReservedNodeOfferingId>
      <StartTime>2019-12-27T22:06:20.054Z</StartTime>
      <NodeCount>1</NodeCount>
      <State>payment-pending</State>
      <CurrencyCode>USD</CurrencyCode>
    </ReservedNode>
  </PurchaseReservedNodeOfferingResult>
  <ResponseMetadata>
    <RequestId>1c8a0fe4-28f5-11ea-8314-974e2ba81189</RequestId>
  </ResponseMetadata>
</PurchaseReservedNodeOfferingResponse>
```

## See Also
<a name="API_PurchaseReservedNodeOffering_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/redshift-2012-12-01/PurchaseReservedNodeOffering) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/redshift-2012-12-01/PurchaseReservedNodeOffering) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/redshift-2012-12-01/PurchaseReservedNodeOffering) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/redshift-2012-12-01/PurchaseReservedNodeOffering) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/redshift-2012-12-01/PurchaseReservedNodeOffering) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/redshift-2012-12-01/PurchaseReservedNodeOffering) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/redshift-2012-12-01/PurchaseReservedNodeOffering) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/redshift-2012-12-01/PurchaseReservedNodeOffering) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/redshift-2012-12-01/PurchaseReservedNodeOffering) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/redshift-2012-12-01/PurchaseReservedNodeOffering) 