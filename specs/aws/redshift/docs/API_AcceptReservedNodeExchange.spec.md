---
id: "@specs/aws/redshift/docs/API_AcceptReservedNodeExchange"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS AcceptReservedNodeExchange"
status: active
depends_on:
  - "@specs/aws/redshift/meta"
---

# AcceptReservedNodeExchange

> **source:** AWS Documentation
> **spec:id:** @specs/aws/redshift/docs/API_AcceptReservedNodeExchange
> **target_lang:** meta — documentation tier. ALL sections preserved.



# AcceptReservedNodeExchange
<a name="API_AcceptReservedNodeExchange"></a>

Exchanges a DC1 Reserved Node for a DC2 Reserved Node with no changes to the configuration (term, payment type, or number of nodes) and no additional costs. 

## Request Parameters
<a name="API_AcceptReservedNodeExchange_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 ** ReservedNodeId **   
A string representing the node identifier of the DC1 Reserved Node to be exchanged.  
Type: String  
Length Constraints: Maximum length of 2147483647.  
Required: Yes

 ** TargetReservedNodeOfferingId **   
The unique identifier of the DC2 Reserved Node offering to be used for the exchange. You can obtain the value for the parameter by calling [GetReservedNodeExchangeOfferings](API_GetReservedNodeExchangeOfferings.md)   
Type: String  
Length Constraints: Maximum length of 2147483647.  
Required: Yes

## Response Elements
<a name="API_AcceptReservedNodeExchange_ResponseElements"></a>

The following element is returned by the service.

 ** ExchangedReservedNode **   
  
Type: [ReservedNode](API_ReservedNode.md) object

## Errors
<a name="API_AcceptReservedNodeExchange_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** DependentServiceUnavailableFault **   
Your request cannot be completed because a dependent internal service is temporarily unavailable. Wait 30 to 60 seconds and try again.  
HTTP Status Code: 400

 ** InvalidReservedNodeState **   
Indicates that the Reserved Node being exchanged is not in an active state.  
HTTP Status Code: 400

 ** ReservedNodeAlreadyExists **   
User already has a reservation with the given identifier.  
HTTP Status Code: 404

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
<a name="API_AcceptReservedNodeExchange_Examples"></a>

### Example
<a name="API_AcceptReservedNodeExchange_Example_1"></a>

This example illustrates one usage of AcceptReservedNodeExchange.

#### Sample Request
<a name="API_AcceptReservedNodeExchange_Example_1_Request"></a>

```
https://redshift.us-east-2.amazonaws.com/
    ?Action=AcceptReservedNodeExchange
&ReservedNodeId=12345678-12ab-12a1-1a2a-12ab-12a12aEXAMPLE
&TargetReservedNodeOfferingId=12345678-12ab-12a1-1a2a-12ab-12a12bEXAMPLE
&SignatureMethod=HmacSHA256&SignatureVersion=4
&Version=2012-12-01
&X-Amz-Algorithm=AWS4-HMAC-SHA256
&X-Amz-Credential=AKIAIOSFODNN7EXAMPLE/20190817/us-east-2/redshift/aws4_request
&X-Amz-Date=20190825T160000Z
&X-Amz-SignedHeaders=content-type;host;user-agent;x-amz-content-sha256;x-amz-date
&X-Amz-Signature=0aa1234bb5cc678ddddd901ee2ff3aa45678b90c12d345e6ff789012345a6b7b
```

#### Sample Response
<a name="API_AcceptReservedNodeExchange_Example_1_Response"></a>

```
<AcceptReservedNodeExchangeResponse xmlns="http://redshift.amazonaws.com/doc/2012-12-01/">
  <AcceptReservedNodeExchangeResult>
    <ExchangedReservedNode>
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
      <FixedPrice>0.0</FixedPrice>
      <Duration>31536000</Duration>
      <UsagePrice>0.0</UsagePrice>
      <ReservedNodeOfferingId>12345678-12ab-12a1-1a2a-12ab-12a12bEXAMPLE</ReservedNodeOfferingId>
      <StartTime>2019-12-26T22:27:56Z</StartTime>
      <NodeCount>1</NodeCount>
      <State>exchanging</State>
      <CurrencyCode>USD</CurrencyCode>
    </ExchangedReservedNode>
  </AcceptReservedNodeExchangeResult>
  <ResponseMetadata>
    <RequestId>0b899aa4-2830-11ea-8a28-2fd1719d0e86</RequestId>
  </ResponseMetadata>
</AcceptReservedNodeExchangeResponse>
```

## See Also
<a name="API_AcceptReservedNodeExchange_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/redshift-2012-12-01/AcceptReservedNodeExchange) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/redshift-2012-12-01/AcceptReservedNodeExchange) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/redshift-2012-12-01/AcceptReservedNodeExchange) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/redshift-2012-12-01/AcceptReservedNodeExchange) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/redshift-2012-12-01/AcceptReservedNodeExchange) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/redshift-2012-12-01/AcceptReservedNodeExchange) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/redshift-2012-12-01/AcceptReservedNodeExchange) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/redshift-2012-12-01/AcceptReservedNodeExchange) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/redshift-2012-12-01/AcceptReservedNodeExchange) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/redshift-2012-12-01/AcceptReservedNodeExchange) 