---
id: "@specs/aws/network-firewall/docs/API_TransitGatewayAttachmentSyncState"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS TransitGatewayAttachmentSyncState"
status: active
depends_on:
  - "@specs/aws/network-firewall/meta"
---

# TransitGatewayAttachmentSyncState

> **source:** AWS Documentation
> **spec:id:** @specs/aws/network-firewall/docs/API_TransitGatewayAttachmentSyncState
> **target_lang:** meta — documentation tier. ALL sections preserved.



# TransitGatewayAttachmentSyncState
<a name="API_TransitGatewayAttachmentSyncState"></a>

Contains information about the synchronization state of a transit gateway attachment, including its current status and any error messages. Network Firewall uses this to track the state of your transit gateway configuration changes.

## Contents
<a name="API_TransitGatewayAttachmentSyncState_Contents"></a>

 ** AttachmentId **   <a name="networkfirewall-Type-TransitGatewayAttachmentSyncState-AttachmentId"></a>
The unique identifier of the transit gateway attachment.  
Type: String  
Required: No

 ** StatusMessage **   <a name="networkfirewall-Type-TransitGatewayAttachmentSyncState-StatusMessage"></a>
A message providing additional information about the current status, particularly useful when the transit gateway attachment is in a non-`READY` state.  
Valid values are:  
+  `CREATING` - The attachment is being created
+  `DELETING` - The attachment is being deleted
+  `DELETED` - The attachment has been deleted
+  `FAILED` - The attachment creation has failed and cannot be recovered
+  `ERROR` - The attachment is in an error state that might be recoverable
+  `READY` - The attachment is active and processing traffic
+  `PENDING_ACCEPTANCE` - The attachment is waiting to be accepted
+  `REJECTING` - The attachment is in the process of being rejected
+  `REJECTED` - The attachment has been rejected
For information about troubleshooting endpoint failures, see [Troubleshooting firewall endpoint failures](https://docs.aws.amazon.com/network-firewall/latest/developerguide/firewall-troubleshooting-endpoint-failures.html) in the * AWS Network Firewall Developer Guide*.  
Type: String  
Required: No

 ** TransitGatewayAttachmentStatus **   <a name="networkfirewall-Type-TransitGatewayAttachmentSyncState-TransitGatewayAttachmentStatus"></a>
The current status of the transit gateway attachment.  
Valid values are:  
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
Required: No

## See Also
<a name="API_TransitGatewayAttachmentSyncState_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/network-firewall-2020-11-12/TransitGatewayAttachmentSyncState) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/network-firewall-2020-11-12/TransitGatewayAttachmentSyncState) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/network-firewall-2020-11-12/TransitGatewayAttachmentSyncState) 