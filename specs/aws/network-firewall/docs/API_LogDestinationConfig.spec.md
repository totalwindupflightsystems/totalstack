---
id: "@specs/aws/network-firewall/docs/API_LogDestinationConfig"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS LogDestinationConfig"
status: active
depends_on:
  - "@specs/aws/network-firewall/meta"
---

# LogDestinationConfig

> **source:** AWS Documentation
> **spec:id:** @specs/aws/network-firewall/docs/API_LogDestinationConfig
> **target_lang:** meta — documentation tier. ALL sections preserved.



# LogDestinationConfig
<a name="API_LogDestinationConfig"></a>

Defines where AWS Network Firewall sends logs for the firewall for one log type. This is used in [LoggingConfiguration](API_LoggingConfiguration.md). You can send each type of log to an Amazon S3 bucket, a CloudWatch log group, or a Firehose delivery stream.

Network Firewall generates logs for stateful rule groups. You can save alert, flow, and TLS log types. 

## Contents
<a name="API_LogDestinationConfig_Contents"></a>

 ** LogDestination **   <a name="networkfirewall-Type-LogDestinationConfig-LogDestination"></a>
The named location for the logs, provided in a key:value mapping that is specific to the chosen destination type.   
+ For an Amazon S3 bucket, provide the name of the bucket, with key `bucketName`, and optionally provide a prefix, with key `prefix`. 

  The following example specifies an Amazon S3 bucket named `DOC-EXAMPLE-BUCKET` and the prefix `alerts`: 

   `"LogDestination": { "bucketName": "DOC-EXAMPLE-BUCKET", "prefix": "alerts" }` 
+ For a CloudWatch log group, provide the name of the CloudWatch log group, with key `logGroup`. The following example specifies a log group named `alert-log-group`: 

   `"LogDestination": { "logGroup": "alert-log-group" }` 
+ For a Firehose delivery stream, provide the name of the delivery stream, with key `deliveryStream`. The following example specifies a delivery stream named `alert-delivery-stream`: 

   `"LogDestination": { "deliveryStream": "alert-delivery-stream" }` 
Type: String to string map  
Key Length Constraints: Minimum length of 3. Maximum length of 50.  
Key Pattern: `^[0-9A-Za-z.\-_@\/]+$`   
Value Length Constraints: Minimum length of 1. Maximum length of 1024.  
Value Pattern: `[\s\S]*$`   
Required: Yes

 ** LogDestinationType **   <a name="networkfirewall-Type-LogDestinationConfig-LogDestinationType"></a>
The type of storage destination to send these logs to. You can send logs to an Amazon S3 bucket, a CloudWatch log group, or a Firehose delivery stream.  
Type: String  
Length Constraints: Minimum length of 2. Maximum length of 30.  
Pattern: `[0-9A-Za-z]+`   
Valid Values: `S3 | CloudWatchLogs | KinesisDataFirehose`   
Required: Yes

 ** LogType **   <a name="networkfirewall-Type-LogDestinationConfig-LogType"></a>
The type of log to record. You can record the following types of logs from your AWS Network Firewall stateful engine.  
+  `ALERT` - Logs for traffic that matches your stateful rules and that have an action that sends an alert. A stateful rule sends alerts for the rule actions DROP, ALERT, and REJECT. For more information, see [StatefulRule](API_StatefulRule.md).
+  `FLOW` - Standard network traffic flow logs. The stateful rules engine records flow logs for all network traffic that it receives. Each flow log record captures the network flow for a specific standard stateless rule group.
+  `TLS` - Logs for events that are related to TLS inspection. For more information, see [Inspecting SSL/TLS traffic with TLS inspection configurations](https://docs.aws.amazon.com/network-firewall/latest/developerguide/tls-inspection-configurations.html) in the *Network Firewall Developer Guide*.
Type: String  
Valid Values: `ALERT | FLOW | TLS`   
Required: Yes

## See Also
<a name="API_LogDestinationConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/network-firewall-2020-11-12/LogDestinationConfig) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/network-firewall-2020-11-12/LogDestinationConfig) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/network-firewall-2020-11-12/LogDestinationConfig) 