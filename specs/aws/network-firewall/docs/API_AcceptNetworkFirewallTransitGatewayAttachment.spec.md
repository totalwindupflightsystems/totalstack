---
id: "@specs/aws/network-firewall/docs/API_AcceptNetworkFirewallTransitGatewayAttachment"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS AcceptNetworkFirewallTransitGatewayAttachment"
status: active
depends_on:
  - "@specs/aws/network-firewall/meta"
---

# AcceptNetworkFirewallTransitGatewayAttachment

> **source:** AWS Documentation
> **spec:id:** @specs/aws/network-firewall/docs/API_AcceptNetworkFirewallTransitGatewayAttachment
> **target_lang:** meta — documentation tier. ALL sections preserved.



# AcceptNetworkFirewallTransitGatewayAttachment
<a name="API_AcceptNetworkFirewallTransitGatewayAttachment"></a>

Accepts a transit gateway attachment request for Network Firewall. When you accept the attachment request, Network Firewall creates the necessary routing components to enable traffic flow between the transit gateway and firewall endpoints.

You must accept a transit gateway attachment to complete the creation of a transit gateway-attached firewall, unless auto-accept is enabled on the transit gateway. After acceptance, use [DescribeFirewall](API_DescribeFirewall.md) to verify the firewall status.

To reject an attachment instead of accepting it, use [RejectNetworkFirewallTransitGatewayAttachment](API_RejectNetworkFirewallTransitGatewayAttachment.md).

**Note**  
It can take several minutes for the attachment acceptance to complete and the firewall to become available.

## Request Syntax
<a name="API_AcceptNetworkFirewallTransitGatewayAttachment_RequestSyntax"></a>

```
{
   "TransitGatewayAttachmentId": "{{string}}"
}
```

## Request Parameters
<a name="API_AcceptNetworkFirewallTransitGatewayAttachment_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [TransitGatewayAttachmentId](#API_AcceptNetworkFirewallTransitGatewayAttachment_RequestSyntax) **   <a name="networkfirewall-AcceptNetworkFirewallTransitGatewayAttachment-request-TransitGatewayAttachmentId"></a>
Required. The unique identifier of the transit gateway attachment to accept. This ID is returned in the response when creating a transit gateway-attached firewall.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 128.  
Pattern: `^tgw-attach-[0-9a-z]+$`   
Required: Yes

## Response Syntax
<a name="API_AcceptNetworkFirewallTransitGatewayAttachment_ResponseSyntax"></a>

```
{
   "TransitGatewayAttachmentId": "string",
   "TransitGatewayAttachmentStatus": "string"
}
```

## Response Elements
<a name="API_AcceptNetworkFirewallTransitGatewayAttachment_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [TransitGatewayAttachmentId](#API_AcceptNetworkFirewallTransitGatewayAttachment_ResponseSyntax) **   <a name="networkfirewall-AcceptNetworkFirewallTransitGatewayAttachment-response-TransitGatewayAttachmentId"></a>
The unique identifier of the transit gateway attachment that was accepted.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 128.  
Pattern: `^tgw-attach-[0-9a-z]+$` 

 ** [TransitGatewayAttachmentStatus](#API_AcceptNetworkFirewallTransitGatewayAttachment_ResponseSyntax) **   <a name="networkfirewall-AcceptNetworkFirewallTransitGatewayAttachment-response-TransitGatewayAttachmentStatus"></a>
The current status of the transit gateway attachment. Valid values are:  
+  `CREATING` - The attachment is being created
+  `DELETING` - The attachment is being deleted
+  `DELETED` - The attachment has been deleted
+  `FAILED` - The attachment creation has failed and cannot be recovered
+  `ERROR` - The attachment is in an error state that might be recoverable
+  `READY` - The attachment is active and processing traffic
+  `PENDING_ACCEPTANCE` - The attachment is waiting to be accepted
+  `REJECTING` - The attachment is in the process of being rejected
+  `REJECTED` - The attachment has been rejected
Type: String  
Valid Values: `CREATING | DELETING | DELETED | FAILED | ERROR | READY | PENDING_ACCEPTANCE | REJECTING | REJECTED` 

## Errors
<a name="API_AcceptNetworkFirewallTransitGatewayAttachment_Errors"></a>

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
<a name="API_AcceptNetworkFirewallTransitGatewayAttachment_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/network-firewall-2020-11-12/AcceptNetworkFirewallTransitGatewayAttachment) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/network-firewall-2020-11-12/AcceptNetworkFirewallTransitGatewayAttachment) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/network-firewall-2020-11-12/AcceptNetworkFirewallTransitGatewayAttachment) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/network-firewall-2020-11-12/AcceptNetworkFirewallTransitGatewayAttachment) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/network-firewall-2020-11-12/AcceptNetworkFirewallTransitGatewayAttachment) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/network-firewall-2020-11-12/AcceptNetworkFirewallTransitGatewayAttachment) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/network-firewall-2020-11-12/AcceptNetworkFirewallTransitGatewayAttachment) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/network-firewall-2020-11-12/AcceptNetworkFirewallTransitGatewayAttachment) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/network-firewall-2020-11-12/AcceptNetworkFirewallTransitGatewayAttachment) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/network-firewall-2020-11-12/AcceptNetworkFirewallTransitGatewayAttachment) 