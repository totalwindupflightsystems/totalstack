---
id: "@specs/aws/network-firewall/docs/API_FlowOperationMetadata"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS FlowOperationMetadata"
status: active
depends_on:
  - "@specs/aws/network-firewall/meta"
---

# FlowOperationMetadata

> **source:** AWS Documentation
> **spec:id:** @specs/aws/network-firewall/docs/API_FlowOperationMetadata
> **target_lang:** meta — documentation tier. ALL sections preserved.



# FlowOperationMetadata
<a name="API_FlowOperationMetadata"></a>

An array of objects with metadata about the requested `FlowOperation`.

## Contents
<a name="API_FlowOperationMetadata_Contents"></a>

 ** FlowOperationId **   <a name="networkfirewall-Type-FlowOperationMetadata-FlowOperationId"></a>
A unique identifier for the flow operation. This ID is returned in the responses to start and list commands. You provide to describe commands.  
Type: String  
Length Constraints: Fixed length of 36.  
Pattern: `^([0-9a-f]{8})-([0-9a-f]{4}-){3}([0-9a-f]{12})$`   
Required: No

 ** FlowOperationStatus **   <a name="networkfirewall-Type-FlowOperationMetadata-FlowOperationStatus"></a>
Returns the status of the flow operation. This string is returned in the responses to start, list, and describe commands.  
If the status is `COMPLETED_WITH_ERRORS`, results may be returned with any number of `Flows` missing from the response. If the status is `FAILED`, `Flows` returned will be empty.  
Type: String  
Valid Values: `COMPLETED | IN_PROGRESS | FAILED | COMPLETED_WITH_ERRORS`   
Required: No

 ** FlowOperationType **   <a name="networkfirewall-Type-FlowOperationMetadata-FlowOperationType"></a>
Defines the type of `FlowOperation`.  
Type: String  
Valid Values: `FLOW_FLUSH | FLOW_CAPTURE`   
Required: No

 ** FlowRequestTimestamp **   <a name="networkfirewall-Type-FlowOperationMetadata-FlowRequestTimestamp"></a>
A timestamp indicating when the Suricata engine identified flows impacted by an operation.   
Type: Timestamp  
Required: No

## See Also
<a name="API_FlowOperationMetadata_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/network-firewall-2020-11-12/FlowOperationMetadata) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/network-firewall-2020-11-12/FlowOperationMetadata) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/network-firewall-2020-11-12/FlowOperationMetadata) 