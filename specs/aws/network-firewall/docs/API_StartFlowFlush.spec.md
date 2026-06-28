---
id: "@specs/aws/network-firewall/docs/API_StartFlowFlush"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS StartFlowFlush"
status: active
depends_on:
  - "@specs/aws/network-firewall/meta"
---

# StartFlowFlush

> **source:** AWS Documentation
> **spec:id:** @specs/aws/network-firewall/docs/API_StartFlowFlush
> **target_lang:** meta — documentation tier. ALL sections preserved.



# StartFlowFlush
<a name="API_StartFlowFlush"></a>

Begins the flushing of traffic from the firewall, according to the filters you define. When the operation starts, impacted flows are temporarily marked as timed out before the Suricata engine prunes, or flushes, the flows from the firewall table.

**Important**  
While the flush completes, impacted flows are processed as midstream traffic. This may result in a temporary increase in midstream traffic metrics. We recommend that you double check your stream exception policy before you perform a flush operation.

## Request Syntax
<a name="API_StartFlowFlush_RequestSyntax"></a>

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
<a name="API_StartFlowFlush_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [AvailabilityZone](#API_StartFlowFlush_RequestSyntax) **   <a name="networkfirewall-StartFlowFlush-request-AvailabilityZone"></a>
The ID of the Availability Zone where the firewall is located. For example, `us-east-2a`.  
Defines the scope a flow operation. You can use up to 20 filters to configure a single flow operation.  
Type: String  
Required: No

 ** [FirewallArn](#API_StartFlowFlush_RequestSyntax) **   <a name="networkfirewall-StartFlowFlush-request-FirewallArn"></a>
The Amazon Resource Name (ARN) of the firewall.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 256.  
Pattern: `^arn:aws.*`   
Required: Yes

 ** [FlowFilters](#API_StartFlowFlush_RequestSyntax) **   <a name="networkfirewall-StartFlowFlush-request-FlowFilters"></a>
Defines the scope a flow operation. You can use up to 20 filters to configure a single flow operation.  
Type: Array of [FlowFilter](API_FlowFilter.md) objects  
Required: Yes

 ** [MinimumFlowAgeInSeconds](#API_StartFlowFlush_RequestSyntax) **   <a name="networkfirewall-StartFlowFlush-request-MinimumFlowAgeInSeconds"></a>
The reqested `FlowOperation` ignores flows with an age (in seconds) lower than `MinimumFlowAgeInSeconds`. You provide this for start commands.  
Type: Integer  
Required: No

 ** [VpcEndpointAssociationArn](#API_StartFlowFlush_RequestSyntax) **   <a name="networkfirewall-StartFlowFlush-request-VpcEndpointAssociationArn"></a>
The Amazon Resource Name (ARN) of a VPC endpoint association.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 256.  
Pattern: `^arn:aws.*`   
Required: No

 ** [VpcEndpointId](#API_StartFlowFlush_RequestSyntax) **   <a name="networkfirewall-StartFlowFlush-request-VpcEndpointId"></a>
A unique identifier for the primary endpoint associated with a firewall.  
Type: String  
Length Constraints: Minimum length of 5. Maximum length of 256.  
Pattern: `^vpce-[a-zA-Z0-9]*$`   
Required: No

## Response Syntax
<a name="API_StartFlowFlush_ResponseSyntax"></a>

```
{
   "FirewallArn": "string",
   "FlowOperationId": "string",
   "FlowOperationStatus": "string"
}
```

## Response Elements
<a name="API_StartFlowFlush_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [FirewallArn](#API_StartFlowFlush_ResponseSyntax) **   <a name="networkfirewall-StartFlowFlush-response-FirewallArn"></a>
The Amazon Resource Name (ARN) of the firewall.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 256.  
Pattern: `^arn:aws.*` 

 ** [FlowOperationId](#API_StartFlowFlush_ResponseSyntax) **   <a name="networkfirewall-StartFlowFlush-response-FlowOperationId"></a>
A unique identifier for the flow operation. This ID is returned in the responses to start and list commands. You provide to describe commands.  
Type: String  
Length Constraints: Fixed length of 36.  
Pattern: `^([0-9a-f]{8})-([0-9a-f]{4}-){3}([0-9a-f]{12})$` 

 ** [FlowOperationStatus](#API_StartFlowFlush_ResponseSyntax) **   <a name="networkfirewall-StartFlowFlush-response-FlowOperationStatus"></a>
Returns the status of the flow operation. This string is returned in the responses to start, list, and describe commands.  
If the status is `COMPLETED_WITH_ERRORS`, results may be returned with any number of `Flows` missing from the response. If the status is `FAILED`, `Flows` returned will be empty.  
Type: String  
Valid Values: `COMPLETED | IN_PROGRESS | FAILED | COMPLETED_WITH_ERRORS` 

## Errors
<a name="API_StartFlowFlush_Errors"></a>

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
<a name="API_StartFlowFlush_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/network-firewall-2020-11-12/StartFlowFlush) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/network-firewall-2020-11-12/StartFlowFlush) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/network-firewall-2020-11-12/StartFlowFlush) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/network-firewall-2020-11-12/StartFlowFlush) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/network-firewall-2020-11-12/StartFlowFlush) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/network-firewall-2020-11-12/StartFlowFlush) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/network-firewall-2020-11-12/StartFlowFlush) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/network-firewall-2020-11-12/StartFlowFlush) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/network-firewall-2020-11-12/StartFlowFlush) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/network-firewall-2020-11-12/StartFlowFlush) 