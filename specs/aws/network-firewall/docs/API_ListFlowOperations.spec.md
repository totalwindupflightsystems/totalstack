---
id: "@specs/aws/network-firewall/docs/API_ListFlowOperations"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS ListFlowOperations"
status: active
depends_on:
  - "@specs/aws/network-firewall/meta"
---

# ListFlowOperations

> **source:** AWS Documentation
> **spec:id:** @specs/aws/network-firewall/docs/API_ListFlowOperations
> **target_lang:** meta — documentation tier. ALL sections preserved.



# ListFlowOperations
<a name="API_ListFlowOperations"></a>

Returns a list of all flow operations ran in a specific firewall. You can optionally narrow the request scope by specifying the operation type or Availability Zone associated with a firewall's flow operations. 

Flow operations let you manage the flows tracked in the flow table, also known as the firewall table.

A flow is network traffic that is monitored by a firewall, either by stateful or stateless rules. For traffic to be considered part of a flow, it must share Destination, DestinationPort, Direction, Protocol, Source, and SourcePort. 

## Request Syntax
<a name="API_ListFlowOperations_RequestSyntax"></a>

```
{
   "AvailabilityZone": "{{string}}",
   "FirewallArn": "{{string}}",
   "FlowOperationType": "{{string}}",
   "MaxResults": {{number}},
   "NextToken": "{{string}}",
   "VpcEndpointAssociationArn": "{{string}}",
   "VpcEndpointId": "{{string}}"
}
```

## Request Parameters
<a name="API_ListFlowOperations_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [AvailabilityZone](#API_ListFlowOperations_RequestSyntax) **   <a name="networkfirewall-ListFlowOperations-request-AvailabilityZone"></a>
The ID of the Availability Zone where the firewall is located. For example, `us-east-2a`.  
Defines the scope a flow operation. You can use up to 20 filters to configure a single flow operation.  
Type: String  
Required: No

 ** [FirewallArn](#API_ListFlowOperations_RequestSyntax) **   <a name="networkfirewall-ListFlowOperations-request-FirewallArn"></a>
The Amazon Resource Name (ARN) of the firewall.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 256.  
Pattern: `^arn:aws.*`   
Required: Yes

 ** [FlowOperationType](#API_ListFlowOperations_RequestSyntax) **   <a name="networkfirewall-ListFlowOperations-request-FlowOperationType"></a>
An optional string that defines whether any or all operation types are returned.  
Type: String  
Valid Values: `FLOW_FLUSH | FLOW_CAPTURE`   
Required: No

 ** [MaxResults](#API_ListFlowOperations_RequestSyntax) **   <a name="networkfirewall-ListFlowOperations-request-MaxResults"></a>
The maximum number of objects that you want Network Firewall to return for this request. If more objects are available, in the response, Network Firewall provides a `NextToken` value that you can use in a subsequent call to get the next batch of objects.  
Type: Integer  
Valid Range: Minimum value of 1. Maximum value of 100.  
Required: No

 ** [NextToken](#API_ListFlowOperations_RequestSyntax) **   <a name="networkfirewall-ListFlowOperations-request-NextToken"></a>
When you request a list of objects with a `MaxResults` setting, if the number of objects that are still available for retrieval exceeds the maximum you requested, Network Firewall returns a `NextToken` value in the response. To retrieve the next batch of objects, use the token returned from the prior request in your next request.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 4096.  
Pattern: `[0-9A-Za-z:\/+=]+$`   
Required: No

 ** [VpcEndpointAssociationArn](#API_ListFlowOperations_RequestSyntax) **   <a name="networkfirewall-ListFlowOperations-request-VpcEndpointAssociationArn"></a>
The Amazon Resource Name (ARN) of a VPC endpoint association.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 256.  
Pattern: `^arn:aws.*`   
Required: No

 ** [VpcEndpointId](#API_ListFlowOperations_RequestSyntax) **   <a name="networkfirewall-ListFlowOperations-request-VpcEndpointId"></a>
A unique identifier for the primary endpoint associated with a firewall.  
Type: String  
Length Constraints: Minimum length of 5. Maximum length of 256.  
Pattern: `^vpce-[a-zA-Z0-9]*$`   
Required: No

## Response Syntax
<a name="API_ListFlowOperations_ResponseSyntax"></a>

```
{
   "FlowOperations": [ 
      { 
         "FlowOperationId": "string",
         "FlowOperationStatus": "string",
         "FlowOperationType": "string",
         "FlowRequestTimestamp": number
      }
   ],
   "NextToken": "string"
}
```

## Response Elements
<a name="API_ListFlowOperations_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [FlowOperations](#API_ListFlowOperations_ResponseSyntax) **   <a name="networkfirewall-ListFlowOperations-response-FlowOperations"></a>
Flow operations let you manage the flows tracked in the flow table, also known as the firewall table.  
A flow is network traffic that is monitored by a firewall, either by stateful or stateless rules. For traffic to be considered part of a flow, it must share Destination, DestinationPort, Direction, Protocol, Source, and SourcePort.   
Type: Array of [FlowOperationMetadata](API_FlowOperationMetadata.md) objects

 ** [NextToken](#API_ListFlowOperations_ResponseSyntax) **   <a name="networkfirewall-ListFlowOperations-response-NextToken"></a>
When you request a list of objects with a `MaxResults` setting, if the number of objects that are still available for retrieval exceeds the maximum you requested, Network Firewall returns a `NextToken` value in the response. To retrieve the next batch of objects, use the token returned from the prior request in your next request.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 4096.  
Pattern: `[0-9A-Za-z:\/+=]+$` 

## Errors
<a name="API_ListFlowOperations_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalServerError **   
Your request is valid, but Network Firewall couldn't perform the operation because of a system problem. Retry your request.   
HTTP Status Code: 500

 ** InvalidRequestException **   
The operation failed because of a problem with your request. Examples include:   
+ You specified an unsupported parameter name or value.
+ You tried to update a property with a value that isn't among the available types.
+ Your request references an ARN that is malformed, or corresponds to a resource that isn't valid in the context of the request.
HTTP Status Code: 400

 ** ResourceNotFoundException **   
Unable to locate a resource using the parameters that you provided.  
HTTP Status Code: 400

 ** ThrottlingException **   
Unable to process the request due to throttling limitations.  
HTTP Status Code: 400

## See Also
<a name="API_ListFlowOperations_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/network-firewall-2020-11-12/ListFlowOperations) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/network-firewall-2020-11-12/ListFlowOperations) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/network-firewall-2020-11-12/ListFlowOperations) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/network-firewall-2020-11-12/ListFlowOperations) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/network-firewall-2020-11-12/ListFlowOperations) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/network-firewall-2020-11-12/ListFlowOperations) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/network-firewall-2020-11-12/ListFlowOperations) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/network-firewall-2020-11-12/ListFlowOperations) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/network-firewall-2020-11-12/ListFlowOperations) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/network-firewall-2020-11-12/ListFlowOperations) 