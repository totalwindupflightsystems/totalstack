---
id: "@specs/aws/network-firewall/docs/API_DescribeFlowOperation"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS DescribeFlowOperation"
status: active
depends_on:
  - "@specs/aws/network-firewall/meta"
---

# DescribeFlowOperation

> **source:** AWS Documentation
> **spec:id:** @specs/aws/network-firewall/docs/API_DescribeFlowOperation
> **target_lang:** meta — documentation tier. ALL sections preserved.



# DescribeFlowOperation
<a name="API_DescribeFlowOperation"></a>

Returns key information about a specific flow operation.

## Request Syntax
<a name="API_DescribeFlowOperation_RequestSyntax"></a>

```
{
   "AvailabilityZone": "{{string}}",
   "FirewallArn": "{{string}}",
   "FlowOperationId": "{{string}}",
   "VpcEndpointAssociationArn": "{{string}}",
   "VpcEndpointId": "{{string}}"
}
```

## Request Parameters
<a name="API_DescribeFlowOperation_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [AvailabilityZone](#API_DescribeFlowOperation_RequestSyntax) **   <a name="networkfirewall-DescribeFlowOperation-request-AvailabilityZone"></a>
The ID of the Availability Zone where the firewall is located. For example, `us-east-2a`.  
Defines the scope a flow operation. You can use up to 20 filters to configure a single flow operation.  
Type: String  
Required: No

 ** [FirewallArn](#API_DescribeFlowOperation_RequestSyntax) **   <a name="networkfirewall-DescribeFlowOperation-request-FirewallArn"></a>
The Amazon Resource Name (ARN) of the firewall.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 256.  
Pattern: `^arn:aws.*`   
Required: Yes

 ** [FlowOperationId](#API_DescribeFlowOperation_RequestSyntax) **   <a name="networkfirewall-DescribeFlowOperation-request-FlowOperationId"></a>
A unique identifier for the flow operation. This ID is returned in the responses to start and list commands. You provide to describe commands.  
Type: String  
Length Constraints: Fixed length of 36.  
Pattern: `^([0-9a-f]{8})-([0-9a-f]{4}-){3}([0-9a-f]{12})$`   
Required: Yes

 ** [VpcEndpointAssociationArn](#API_DescribeFlowOperation_RequestSyntax) **   <a name="networkfirewall-DescribeFlowOperation-request-VpcEndpointAssociationArn"></a>
The Amazon Resource Name (ARN) of a VPC endpoint association.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 256.  
Pattern: `^arn:aws.*`   
Required: No

 ** [VpcEndpointId](#API_DescribeFlowOperation_RequestSyntax) **   <a name="networkfirewall-DescribeFlowOperation-request-VpcEndpointId"></a>
A unique identifier for the primary endpoint associated with a firewall.  
Type: String  
Length Constraints: Minimum length of 5. Maximum length of 256.  
Pattern: `^vpce-[a-zA-Z0-9]*$`   
Required: No

## Response Syntax
<a name="API_DescribeFlowOperation_ResponseSyntax"></a>

```
{
   "AvailabilityZone": "string",
   "FirewallArn": "string",
   "FlowOperation": { 
      "FlowFilters": [ 
         { 
            "DestinationAddress": { 
               "AddressDefinition": "string"
            },
            "DestinationPort": "string",
            "Protocols": [ "string" ],
            "SourceAddress": { 
               "AddressDefinition": "string"
            },
            "SourcePort": "string"
         }
      ],
      "MinimumFlowAgeInSeconds": number
   },
   "FlowOperationId": "string",
   "FlowOperationStatus": "string",
   "FlowOperationType": "string",
   "FlowRequestTimestamp": number,
   "StatusMessage": "string",
   "VpcEndpointAssociationArn": "string",
   "VpcEndpointId": "string"
}
```

## Response Elements
<a name="API_DescribeFlowOperation_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [AvailabilityZone](#API_DescribeFlowOperation_ResponseSyntax) **   <a name="networkfirewall-DescribeFlowOperation-response-AvailabilityZone"></a>
The ID of the Availability Zone where the firewall is located. For example, `us-east-2a`.  
Defines the scope a flow operation. You can use up to 20 filters to configure a single flow operation.  
Type: String

 ** [FirewallArn](#API_DescribeFlowOperation_ResponseSyntax) **   <a name="networkfirewall-DescribeFlowOperation-response-FirewallArn"></a>
The Amazon Resource Name (ARN) of the firewall.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 256.  
Pattern: `^arn:aws.*` 

 ** [FlowOperation](#API_DescribeFlowOperation_ResponseSyntax) **   <a name="networkfirewall-DescribeFlowOperation-response-FlowOperation"></a>
Returns key information about a flow operation, such as related statuses, unique identifiers, and all filters defined in the operation.  
Type: [FlowOperation](API_FlowOperation.md) object

 ** [FlowOperationId](#API_DescribeFlowOperation_ResponseSyntax) **   <a name="networkfirewall-DescribeFlowOperation-response-FlowOperationId"></a>
A unique identifier for the flow operation. This ID is returned in the responses to start and list commands. You provide to describe commands.  
Type: String  
Length Constraints: Fixed length of 36.  
Pattern: `^([0-9a-f]{8})-([0-9a-f]{4}-){3}([0-9a-f]{12})$` 

 ** [FlowOperationStatus](#API_DescribeFlowOperation_ResponseSyntax) **   <a name="networkfirewall-DescribeFlowOperation-response-FlowOperationStatus"></a>
Returns the status of the flow operation. This string is returned in the responses to start, list, and describe commands.  
If the status is `COMPLETED_WITH_ERRORS`, results may be returned with any number of `Flows` missing from the response. If the status is `FAILED`, `Flows` returned will be empty.  
Type: String  
Valid Values: `COMPLETED | IN_PROGRESS | FAILED | COMPLETED_WITH_ERRORS` 

 ** [FlowOperationType](#API_DescribeFlowOperation_ResponseSyntax) **   <a name="networkfirewall-DescribeFlowOperation-response-FlowOperationType"></a>
Defines the type of `FlowOperation`.  
Type: String  
Valid Values: `FLOW_FLUSH | FLOW_CAPTURE` 

 ** [FlowRequestTimestamp](#API_DescribeFlowOperation_ResponseSyntax) **   <a name="networkfirewall-DescribeFlowOperation-response-FlowRequestTimestamp"></a>
A timestamp indicating when the Suricata engine identified flows impacted by an operation.   
Type: Timestamp

 ** [StatusMessage](#API_DescribeFlowOperation_ResponseSyntax) **   <a name="networkfirewall-DescribeFlowOperation-response-StatusMessage"></a>
If the asynchronous operation fails, Network Firewall populates this with the reason for the error or failure. Options include `Flow operation error` and `Flow timeout`.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 256.  
Pattern: `^[a-zA-Z0-9- ]+$` 

 ** [VpcEndpointAssociationArn](#API_DescribeFlowOperation_ResponseSyntax) **   <a name="networkfirewall-DescribeFlowOperation-response-VpcEndpointAssociationArn"></a>
The Amazon Resource Name (ARN) of a VPC endpoint association.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 256.  
Pattern: `^arn:aws.*` 

 ** [VpcEndpointId](#API_DescribeFlowOperation_ResponseSyntax) **   <a name="networkfirewall-DescribeFlowOperation-response-VpcEndpointId"></a>
A unique identifier for the primary endpoint associated with a firewall.  
Type: String  
Length Constraints: Minimum length of 5. Maximum length of 256.  
Pattern: `^vpce-[a-zA-Z0-9]*$` 

## Errors
<a name="API_DescribeFlowOperation_Errors"></a>

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
<a name="API_DescribeFlowOperation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/network-firewall-2020-11-12/DescribeFlowOperation) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/network-firewall-2020-11-12/DescribeFlowOperation) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/network-firewall-2020-11-12/DescribeFlowOperation) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/network-firewall-2020-11-12/DescribeFlowOperation) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/network-firewall-2020-11-12/DescribeFlowOperation) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/network-firewall-2020-11-12/DescribeFlowOperation) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/network-firewall-2020-11-12/DescribeFlowOperation) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/network-firewall-2020-11-12/DescribeFlowOperation) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/network-firewall-2020-11-12/DescribeFlowOperation) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/network-firewall-2020-11-12/DescribeFlowOperation) 