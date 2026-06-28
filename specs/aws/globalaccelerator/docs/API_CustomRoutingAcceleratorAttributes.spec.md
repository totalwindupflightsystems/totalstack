---
id: "@specs/aws/globalaccelerator/docs/API_CustomRoutingAcceleratorAttributes"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS CustomRoutingAcceleratorAttributes"
status: active
depends_on:
  - "@specs/aws/globalaccelerator/meta"
---

# CustomRoutingAcceleratorAttributes

> **source:** AWS Documentation
> **spec:id:** @specs/aws/globalaccelerator/docs/API_CustomRoutingAcceleratorAttributes
> **target_lang:** meta — documentation tier. ALL sections preserved.



# CustomRoutingAcceleratorAttributes
<a name="API_CustomRoutingAcceleratorAttributes"></a>

Attributes of a custom routing accelerator.

## Contents
<a name="API_CustomRoutingAcceleratorAttributes_Contents"></a>

 ** FlowLogsEnabled **   <a name="globalaccelerator-Type-CustomRoutingAcceleratorAttributes-FlowLogsEnabled"></a>
Indicates whether flow logs are enabled. The default value is false. If the value is true, `FlowLogsS3Bucket` and `FlowLogsS3Prefix` must be specified.  
For more information, see [Flow logs](https://docs.aws.amazon.com/global-accelerator/latest/dg/monitoring-global-accelerator.flow-logs.html) in the * AWS Global Accelerator Developer Guide*.  
Type: Boolean  
Required: No

 ** FlowLogsS3Bucket **   <a name="globalaccelerator-Type-CustomRoutingAcceleratorAttributes-FlowLogsS3Bucket"></a>
The name of the Amazon S3 bucket for the flow logs. Attribute is required if `FlowLogsEnabled` is `true`. The bucket must exist and have a bucket policy that grants AWS Global Accelerator permission to write to the bucket.  
Type: String  
Length Constraints: Maximum length of 255.  
Required: No

 ** FlowLogsS3Prefix **   <a name="globalaccelerator-Type-CustomRoutingAcceleratorAttributes-FlowLogsS3Prefix"></a>
The prefix for the location in the Amazon S3 bucket for the flow logs. Attribute is required if `FlowLogsEnabled` is `true`.  
If you specify slash (/) for the S3 bucket prefix, the log file bucket folder structure will include a double slash (//), like the following:  
DOC-EXAMPLE-BUCKET//AWSLogs/aws\_account\_id  
Type: String  
Length Constraints: Maximum length of 255.  
Required: No

## See Also
<a name="API_CustomRoutingAcceleratorAttributes_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/globalaccelerator-2018-08-08/CustomRoutingAcceleratorAttributes) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/globalaccelerator-2018-08-08/CustomRoutingAcceleratorAttributes) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/globalaccelerator-2018-08-08/CustomRoutingAcceleratorAttributes) 