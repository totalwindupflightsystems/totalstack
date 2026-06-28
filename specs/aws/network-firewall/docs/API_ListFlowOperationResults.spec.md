---
id: "@specs/aws/network-firewall/docs/API_ListFlowOperationResults"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS ListFlowOperationResults"
status: active
depends_on:
  - "@specs/aws/network-firewall/meta"
---

# ListFlowOperationResults

> **source:** AWS Documentation
> **spec:id:** @specs/aws/network-firewall/docs/API_ListFlowOperationResults
> **target_lang:** meta — documentation tier. ALL sections preserved.



# ListFlowOperationResults
<a name="API_ListFlowOperationResults"></a>

Returns the results of a specific flow operation. 

Flow operations let you manage the flows tracked in the flow table, also known as the firewall table.

A flow is network traffic that is monitored by a firewall, either by stateful or stateless rules. For traffic to be considered part of a flow, it must share Destination, DestinationPort, Direction, Protocol, Source, and SourcePort. 

## Request Syntax
<a name="API_ListFlowOperationResults_RequestSyntax"></a>

```
{
   "AvailabilityZone": "{{string}}",
   "FirewallArn": "{{string}}",
   "FlowOperationId": "{{string}}",
   "MaxResults": {{number}},
   "NextToken": "{{string}}",
   "VpcEndpointAssociationArn": "{{string}}",
   "VpcEndpointId": "{{string}}"
}
```

## Request Parameters
<a name="API_ListFlowOperationResults_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [AvailabilityZone](#API_ListFlowOperationResults_RequestSyntax) **   <a name="networkfirewall-ListFlowOperationResults-request-AvailabilityZone"></a>
The ID of the Availability Zone where the firewall is located. For example, `us-east-2a`.  
Defines the scope a flow operation. You can use up to 20 filters to configure a single flow operation.  
Type: String  
Required: No

 ** [FirewallArn](#API_ListFlowOperationResults_RequestSyntax) **   <a name="networkfirewall-ListFlowOperationResults-request-FirewallArn"></a>
The Amazon Resource Name (ARN) of the firewall.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 256.  
Pattern: `^arn:aws.*`   
Required: Yes

 ** [FlowOperationId](#API_ListFlowOperationResults_RequestSyntax) **   <a name="networkfirewall-ListFlowOperationResults-request-FlowOperationId"></a>
A unique identifier for the flow operation. This ID is returned in the responses to start and list commands. You provide to describe commands.  
Type: String  
Length Constraints: Fixed length of 36.  
Pattern: `^([0-9a-f]{8})-([0-9a-f]{4}-){3}([0-9a-f]{12})$`   
Required: Yes

 ** [MaxResults](#API_ListFlowOperationResults_RequestSyntax) **   <a name="networkfirewall-ListFlowOperationResults-request-MaxResults"></a>
The maximum number of objects that you want Network Firewall to return for this request. If more objects are available, in the response, Network Firewall provides a `NextToken` value that you can use in a subsequent call to get the next batch of objects.  
Type: Integer  
Valid Range: Minimum value of 1. Maximum value of 100.  
Required: No

 ** [NextToken](#API_ListFlowOperationResults_RequestSyntax) **   <a name="networkfirewall-ListFlowOperationResults-request-NextToken"></a>
When you request a list of objects with a `MaxResults` setting, if the number of objects that are still available for retrieval exceeds the maximum you requested, Network Firewall returns a `NextToken` value in the response. To retrieve the next batch of objects, use the token returned from the prior request in your next request.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 4096.  
Pattern: `[0-9A-Za-z:\/+=]+$`   
Required: No

 ** [VpcEndpointAssociationArn](#API_ListFlowOperationResults_RequestSyntax) **   <a name="networkfirewall-ListFlowOperationResults-request-VpcEndpointAssociationArn"></a>
The Amazon Resource Name (ARN) of a VPC endpoint association.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 256.  
Pattern: `^arn:aws.*`   
Required: No

 ** [VpcEndpointId](#API_ListFlowOperationResults_RequestSyntax) **   <a name="networkfirewall-ListFlowOperationResults-request-VpcEndpointId"></a>
A unique identifier for the primary endpoint associated with a firewall.  
Type: String  
Length Constraints: Minimum length of 5. Maximum length of 256.  
Pattern: `^vpce-[a-zA-Z0-9]*$`   
Required: No

## Response Syntax
<a name="API_ListFlowOperationResults_ResponseSyntax"></a>

```
{
   "AvailabilityZone": "string",
   "FirewallArn": "string",
   "FlowOperationId": "string",
   "FlowOperationStatus": "string",
   "FlowRequestTimestamp": number,
   "Flows": [ 
      { 
         "Age": number,
         "ByteCount": number,
         "DestinationAddress": { 
            "AddressDefinition": "string"
         },
         "DestinationPort": "string",
         "PacketCount": number,
         "Protocol": "string",
         "SourceAddress": { 
            "AddressDefinition": "string"
         },
         "SourcePort": "string"
      }
   ],
   "NextToken": "string",
   "StatusMessage": "string",
   "VpcEndpointAssociationArn": "string",
   "VpcEndpointId": "string"
}
```

## Response Elements
<a name="API_ListFlowOperationResults_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [AvailabilityZone](#API_ListFlowOperationResults_ResponseSyntax) **   <a name="networkfirewall-ListFlowOperationResults-response-AvailabilityZone"></a>
The ID of the Availability Zone where the firewall is located. For example, `us-east-2a`.  
Defines the scope a flow operation. You can use up to 20 filters to configure a single flow operation.  
Type: String

 ** [FirewallArn](#API_ListFlowOperationResults_ResponseSyntax) **   <a name="networkfirewall-ListFlowOperationResults-response-FirewallArn"></a>
The Amazon Resource Name (ARN) of the firewall.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 256.  
Pattern: `^arn:aws.*` 

 ** [FlowOperationId](#API_ListFlowOperationResults_ResponseSyntax) **   <a name="networkfirewall-ListFlowOperationResults-response-FlowOperationId"></a>
A unique identifier for the flow operation. This ID is returned in the responses to start and list commands. You provide to describe commands.  
Type: String  
Length Constraints: Fixed length of 36.  
Pattern: `^([0-9a-f]{8})-([0-9a-f]{4}-){3}([0-9a-f]{12})$` 

 ** [FlowOperationStatus](#API_ListFlowOperationResults_ResponseSyntax) **   <a name="networkfirewall-ListFlowOperationResults-response-FlowOperationStatus"></a>
Returns the status of the flow operation. This string is returned in the responses to start, list, and describe commands.  
If the status is `COMPLETED_WITH_ERRORS`, results may be returned with any number of `Flows` missing from the response. If the status is `FAILED`, `Flows` returned will be empty.  
Type: String  
Valid Values: `COMPLETED | IN_PROGRESS | FAILED | COMPLETED_WITH_ERRORS` 

 ** [FlowRequestTimestamp](#API_ListFlowOperationResults_ResponseSyntax) **   <a name="networkfirewall-ListFlowOperationResults-response-FlowRequestTimestamp"></a>
A timestamp indicating when the Suricata engine identified flows impacted by an operation.   
Type: Timestamp

 ** [Flows](#API_ListFlowOperationResults_ResponseSyntax) **   <a name="networkfirewall-ListFlowOperationResults-response-Flows"></a>
Any number of arrays, where each array is a single flow identified in the scope of the operation. If multiple flows were in the scope of the operation, multiple `Flows` arrays are returned.  
Type: Array of [Flow](API_Flow.md) objects

 ** [NextToken](#API_ListFlowOperationResults_ResponseSyntax) **   <a name="networkfirewall-ListFlowOperationResults-response-NextToken"></a>
When you request a list of objects with a `MaxResults` setting, if the number of objects that are still available for retrieval exceeds the maximum you requested, Network Firewall returns a `NextToken` value in the response. To retrieve the next batch of objects, use the token returned from the prior request in your next request.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 4096.  
Pattern: `[0-9A-Za-z:\/+=]+$` 

 ** [StatusMessage](#API_ListFlowOperationResults_ResponseSyntax) **   <a name="networkfirewall-ListFlowOperationResults-response-StatusMessage"></a>
If the asynchronous operation fails, Network Firewall populates this with the reason for the error or failure. Options include `Flow operation error` and `Flow timeout`.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 256.  
Pattern: `^[a-zA-Z0-9- ]+$` 

 ** [VpcEndpointAssociationArn](#API_ListFlowOperationResults_ResponseSyntax) **   <a name="networkfirewall-ListFlowOperationResults-response-VpcEndpointAssociationArn"></a>
  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 256.  
Pattern: `^arn:aws.*` 

 ** [VpcEndpointId](#API_ListFlowOperationResults_ResponseSyntax) **   <a name="networkfirewall-ListFlowOperationResults-response-VpcEndpointId"></a>
  
Type: String  
Length Constraints: Minimum length of 5. Maximum length of 256.  
Pattern: `^vpce-[a-zA-Z0-9]*$` 

## Errors
<a name="API_ListFlowOperationResults_Errors"></a>

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
<a name="API_ListFlowOperationResults_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/network-firewall-2020-11-12/ListFlowOperationResults) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/network-firewall-2020-11-12/ListFlowOperationResults) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/network-firewall-2020-11-12/ListFlowOperationResults) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/network-firewall-2020-11-12/ListFlowOperationResults) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/network-firewall-2020-11-12/ListFlowOperationResults) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/network-firewall-2020-11-12/ListFlowOperationResults) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/network-firewall-2020-11-12/ListFlowOperationResults) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/network-firewall-2020-11-12/ListFlowOperationResults) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/network-firewall-2020-11-12/ListFlowOperationResults) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/network-firewall-2020-11-12/ListFlowOperationResults) 