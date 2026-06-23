---
id: "@specs/aws/appmesh/docs/API_VirtualGatewayFileAccessLog"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS VirtualGatewayFileAccessLog"
status: active
depends_on:
  - "@specs/aws/appmesh/meta"
---

# VirtualGatewayFileAccessLog

> **source:** AWS Documentation
> **spec:id:** @specs/aws/appmesh/docs/API_VirtualGatewayFileAccessLog
> **target_lang:** meta — documentation tier. ALL sections preserved.



# VirtualGatewayFileAccessLog
<a name="API_VirtualGatewayFileAccessLog"></a>

An object that represents an access log file.

## Contents
<a name="API_VirtualGatewayFileAccessLog_Contents"></a>

 ** path **   <a name="appmesh-Type-VirtualGatewayFileAccessLog-path"></a>
The file path to write access logs to. You can use `/dev/stdout` to send access logs to standard out and configure your Envoy container to use a log driver, such as `awslogs`, to export the access logs to a log storage service such as Amazon CloudWatch Logs. You can also specify a path in the Envoy container's file system to write the files to disk.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 255.  
Required: Yes

 ** format **   <a name="appmesh-Type-VirtualGatewayFileAccessLog-format"></a>
The specified format for the virtual gateway access logs. It can be either `json_format` or `text_format`.  
Type: [LoggingFormat](API_LoggingFormat.md) object  
 **Note: **This object is a Union. Only one member of this object can be specified or returned.  
Required: No

## See Also
<a name="API_VirtualGatewayFileAccessLog_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/appmesh-2019-01-25/VirtualGatewayFileAccessLog) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/appmesh-2019-01-25/VirtualGatewayFileAccessLog) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/appmesh-2019-01-25/VirtualGatewayFileAccessLog) 