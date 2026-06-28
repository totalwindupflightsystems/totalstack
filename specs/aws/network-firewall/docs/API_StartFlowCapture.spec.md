---
id: "@specs/aws/network-firewall/docs/API_StartFlowCapture"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS StartFlowCapture"
status: active
depends_on:
  - "@specs/aws/network-firewall/meta"
---

# StartFlowCapture

> **source:** AWS Documentation
> **spec:id:** @specs/aws/network-firewall/docs/API_StartFlowCapture
> **target_lang:** meta — documentation tier. ALL sections preserved.



# StartFlowCapture
<a name="API_StartFlowCapture"></a>

Begins capturing the flows in a firewall, according to the filters you define. Captures are similar, but not identical to snapshots. Capture operations provide visibility into flows that are not closed and are tracked by a firewall's flow table. Unlike snapshots, captures are a time-boxed view. 

A flow is network traffic that is monitored by a firewall, either by stateful or stateless rules. For traffic to be considered part of a flow, it must share Destination, DestinationPort, Direction, Protocol, Source, and SourcePort. 

**Note**  
To avoid encountering operation limits, you should avoid starting captures with broad filters, like wide IP ranges. Instead, we recommend you define more specific criteria with `FlowFilters`, like narrow IP ranges, ports, or protocols.

## Request Syntax
<a name="API_StartFlowCapture_RequestSyntax"></a>

```
{
   "AvailabilityZone": "{{string}}",
   "FirewallArn": "{{string}}",
   "FlowFilters": [ 
      { 
         "DestinationAddress": { 
            "AddressDefinition": "{{string}}"
         },
         "DestinationPort": "{{string}}",
         "Protocols": [ "{{string}}" ],
         "SourceAddress": { 
            "AddressDefinition": "{{string}}"
         },
         "SourcePort": "{{string}}"
      }
   ],
   "MinimumFlowAgeInSeconds": {{number}},
   "VpcEndpointAssociationArn": "{{string}}",
   "VpcEndpointId": "{{string}}"
}
```

## Request Parameters
<a name="API_StartFlowCapture_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [AvailabilityZone](#API_StartFlowCapture_RequestSyntax) **   <a name="networkfirewall-StartFlowCapture-request-AvailabilityZone"></a>
The ID of the Availability Zone where the firewall is located. For example, `us-east-2a`.  
Defines the scope a flow operation. You can use up to 20 filters to configure a single flow operation.  
Type: String  
Required: No

 ** [FirewallArn](#API_StartFlowCapture_RequestSyntax) **   <a name="networkfirewall-StartFlowCapture-request-FirewallArn"></a>
The Amazon Resource Name (ARN) of the firewall.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 256.  
Pattern: `^arn:aws.*`   
Required: Yes

 ** [FlowFilters](#API_StartFlowCapture_RequestSyntax) **   <a name="networkfirewall-StartFlowCapture-request-FlowFilters"></a>
Defines the scope a flow operation. You can use up to 20 filters to configure a single flow operation.  
Type: Array of [FlowFilter](API_FlowFilter.md) objects  
Required: Yes

 ** [MinimumFlowAgeInSeconds](#API_StartFlowCapture_RequestSyntax) **   <a name="networkfirewall-StartFlowCapture-request-MinimumFlowAgeInSeconds"></a>
The reqested `FlowOperation` ignores flows with an age (in seconds) lower than `MinimumFlowAgeInSeconds`. You provide this for start commands.  
We recommend setting this value to at least 1 minute (60 seconds) to reduce chance of capturing flows that are not yet established.
Type: Integer  
Required: No

 ** [VpcEndpointAssociationArn](#API_StartFlowCapture_RequestSyntax) **   <a name="networkfirewall-StartFlowCapture-request-VpcEndpointAssociationArn"></a>
The Amazon Resource Name (ARN) of a VPC endpoint association.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 256.  
Pattern: `^arn:aws.*`   
Required: No

 ** [VpcEndpointId](#API_StartFlowCapture_RequestSyntax) **   <a name="networkfirewall-StartFlowCapture-request-VpcEndpointId"></a>
A unique identifier for the primary endpoint associated with a firewall.  
Type: String  
Length Constraints: Minimum length of 5. Maximum length of 256.  
Pattern: `^vpce-[a-zA-Z0-9]*$`   
Required: No

## Response Syntax
<a name="API_StartFlowCapture_ResponseSyntax"></a>

```
{
   "FirewallArn": "string",
   "FlowOperationId": "string",
   "FlowOperationStatus": "string"
}
```

## Response Elements
<a name="API_StartFlowCapture_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [FirewallArn](#API_StartFlowCapture_ResponseSyntax) **   <a name="networkfirewall-StartFlowCapture-response-FirewallArn"></a>
The Amazon Resource Name (ARN) of the firewall.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 256.  
Pattern: `^arn:aws.*` 

 ** [FlowOperationId](#API_StartFlowCapture_ResponseSyntax) **   <a name="networkfirewall-StartFlowCapture-response-FlowOperationId"></a>
A unique identifier for the flow operation. This ID is returned in the responses to start and list commands. You provide to describe commands.  
Type: String  
Length Constraints: Fixed length of 36.  
Pattern: `^([0-9a-f]{8})-([0-9a-f]{4}-){3}([0-9a-f]{12})$` 

 ** [FlowOperationStatus](#API_StartFlowCapture_ResponseSyntax) **   <a name="networkfirewall-StartFlowCapture-response-FlowOperationStatus"></a>
Returns the status of the flow operation. This string is returned in the responses to start, list, and describe commands.  
If the status is `COMPLETED_WITH_ERRORS`, results may be returned with any number of `Flows` missing from the response. If the status is `FAILED`, `Flows` returned will be empty.  
Type: String  
Valid Values: `COMPLETED | IN_PROGRESS | FAILED | COMPLETED_WITH_ERRORS` 

## Errors
<a name="API_StartFlowCapture_Errors"></a>

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
<a name="API_StartFlowCapture_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/network-firewall-2020-11-12/StartFlowCapture) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/network-firewall-2020-11-12/StartFlowCapture) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/network-firewall-2020-11-12/StartFlowCapture) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/network-firewall-2020-11-12/StartFlowCapture) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/network-firewall-2020-11-12/StartFlowCapture) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/network-firewall-2020-11-12/StartFlowCapture) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/network-firewall-2020-11-12/StartFlowCapture) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/network-firewall-2020-11-12/StartFlowCapture) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/network-firewall-2020-11-12/StartFlowCapture) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/network-firewall-2020-11-12/StartFlowCapture) 