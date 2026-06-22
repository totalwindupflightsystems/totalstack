---
id: "@specs/aws/redshift/docs/API_GetReservedNodeExchangeOfferings"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS GetReservedNodeExchangeOfferings"
status: active
depends_on:
  - "@specs/aws/redshift/meta"
---

# GetReservedNodeExchangeOfferings

> **source:** AWS Documentation
> **spec:id:** @specs/aws/redshift/docs/API_GetReservedNodeExchangeOfferings
> **target_lang:** meta — documentation tier. ALL sections preserved.



# GetReservedNodeExchangeOfferings
<a name="API_GetReservedNodeExchangeOfferings"></a>

Returns an array of DC2 ReservedNodeOfferings that matches the payment type, term, and usage price of the given DC1 reserved node.

## Request Parameters
<a name="API_GetReservedNodeExchangeOfferings_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 ** ReservedNodeId **   
A string representing the node identifier for the DC1 Reserved Node to be exchanged.  
Type: String  
Length Constraints: Maximum length of 2147483647.  
Required: Yes

 ** Marker **   
A value that indicates the starting point for the next set of ReservedNodeOfferings.  
Type: String  
Length Constraints: Maximum length of 2147483647.  
Required: No

 ** MaxRecords **   
An integer setting the maximum number of ReservedNodeOfferings to retrieve.  
Type: Integer  
Required: No

## Response Elements
<a name="API_GetReservedNodeExchangeOfferings_ResponseElements"></a>

The following elements are returned by the service.

 ** Marker **   
An optional parameter that specifies the starting point for returning a set of response records. When the results of a `GetReservedNodeExchangeOfferings` request exceed the value specified in MaxRecords, Amazon Redshift returns a value in the marker field of the response. You can retrieve the next set of response records by providing the returned marker value in the marker parameter and retrying the request.   
Type: String  
Length Constraints: Maximum length of 2147483647.

 **ReservedNodeOfferings.ReservedNodeOffering.N**   
Returns an array of [ReservedNodeOffering](API_ReservedNodeOffering.md) objects.  
Type: Array of [ReservedNodeOffering](API_ReservedNodeOffering.md) objects

## Errors
<a name="API_GetReservedNodeExchangeOfferings_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

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

## Examples
<a name="API_GetReservedNodeExchangeOfferings_Examples"></a>

### Example
<a name="API_GetReservedNodeExchangeOfferings_Example_1"></a>

This example illustrates one usage of GetReservedNodeExchangeOfferings.

#### Sample Request
<a name="API_GetReservedNodeExchangeOfferings_Example_1_Request"></a>

```
https://redshift.us-east-2.amazonaws.com/
       ?Action=GetReservedNodeExchangeOfferings
&ReservedNodeId=12345678-12ab-12a1-1a2a-12ab-12a12EXAMPLE
&SignatureMethod=HmacSHA256&SignatureVersion=4
&Version=2012-12-01
&X-Amz-Algorithm=AWS4-HMAC-SHA256
&X-Amz-Credential=AKIAIOSFODNN7EXAMPLE/20190817/us-east-2/redshift/aws4_request
&X-Amz-Date=20190825T160000Z
&X-Amz-SignedHeaders=content-type;host;user-agent;x-amz-content-sha256;x-amz-date
&X-Amz-Signature=0aa1234bb5cc678ddddd901ee2ff3aa45678b90c12d345e6ff789012345a6b7b
```

#### Sample Response
<a name="API_GetReservedNodeExchangeOfferings_Example_1_Response"></a>

```
<GetReservedNodeExchangeOfferingsResponse xmlns="http://redshift.amazonaws.com/doc/2012-12-01/">
  <GetReservedNodeExchangeOfferingsResult>
    <ReservedNodeOfferings>
      <ReservedNodeOffering>
        <Duration>31536000</Duration>
        <UsagePrice>0.0</UsagePrice>
        <ReservedNodeOfferingId>12345678-12ab-12a1-1a2a-12ab-12a12EXAMPLE</ReservedNodeOfferingId>
        <OfferingType>All Upfront</OfferingType>
        <ReservedNodeOfferingType>Regular</ReservedNodeOfferingType>
        <RecurringCharges>
          <RecurringCharge>
            <RecurringChargeAmount>0.0</RecurringChargeAmount>
            <RecurringChargeFrequency>Hourly</RecurringChargeFrequency>
          </RecurringCharge>
        </RecurringCharges>
        <NodeType>dc2.large</NodeType>
        <FixedPrice>0.0</FixedPrice>
        <CurrencyCode>USD</CurrencyCode>
      </ReservedNodeOffering>
    </ReservedNodeOfferings>
  </GetReservedNodeExchangeOfferingsResult>
  <ResponseMetadata>
    <RequestId>c75f325d-282f-11ea-9caa-c956bec1ce87</RequestId>
  </ResponseMetadata>
</GetReservedNodeExchangeOfferingsResponse>
```

## See Also
<a name="API_GetReservedNodeExchangeOfferings_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/redshift-2012-12-01/GetReservedNodeExchangeOfferings) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/redshift-2012-12-01/GetReservedNodeExchangeOfferings) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/redshift-2012-12-01/GetReservedNodeExchangeOfferings) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/redshift-2012-12-01/GetReservedNodeExchangeOfferings) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/redshift-2012-12-01/GetReservedNodeExchangeOfferings) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/redshift-2012-12-01/GetReservedNodeExchangeOfferings) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/redshift-2012-12-01/GetReservedNodeExchangeOfferings) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/redshift-2012-12-01/GetReservedNodeExchangeOfferings) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/redshift-2012-12-01/GetReservedNodeExchangeOfferings) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/redshift-2012-12-01/GetReservedNodeExchangeOfferings) 