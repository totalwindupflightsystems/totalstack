---
id: "@specs/aws/cloudfront/docs/API_GetRealtimeLogConfig"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS GetRealtimeLogConfig"
status: active
depends_on:
  - "@specs/aws/cloudfront/meta"
---

# GetRealtimeLogConfig

> **source:** AWS Documentation
> **spec:id:** @specs/aws/cloudfront/docs/API_GetRealtimeLogConfig
> **target_lang:** meta — documentation tier. ALL sections preserved.



# GetRealtimeLogConfig
<a name="API_GetRealtimeLogConfig"></a>

Gets a real-time log configuration.

To get a real-time log configuration, you can provide the configuration's name or its Amazon Resource Name (ARN). You must provide at least one. If you provide both, CloudFront uses the name to identify the real-time log configuration to get.

## Request Syntax
<a name="API_GetRealtimeLogConfig_RequestSyntax"></a>

```
POST /2020-05-31/get-realtime-log-config HTTP/1.1
<?xml version="1.0" encoding="UTF-8"?>
<GetRealtimeLogConfigRequest xmlns="http://cloudfront.amazonaws.com/doc/2020-05-31/">
   <ARN>{{string}}</ARN>
   <Name>{{string}}</Name>
</GetRealtimeLogConfigRequest>
```

## URI Request Parameters
<a name="API_GetRealtimeLogConfig_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_GetRealtimeLogConfig_RequestBody"></a>

The request accepts the following data in XML format.

 ** [GetRealtimeLogConfigRequest](#API_GetRealtimeLogConfig_RequestSyntax) **   <a name="cloudfront-GetRealtimeLogConfig-request-GetRealtimeLogConfigRequest"></a>
Root level tag for the GetRealtimeLogConfigRequest parameters.  
Required: Yes

 ** [ARN](#API_GetRealtimeLogConfig_RequestSyntax) **   <a name="cloudfront-GetRealtimeLogConfig-request-ARN"></a>
The Amazon Resource Name (ARN) of the real-time log configuration to get.  
Type: String  
Required: No

 ** [Name](#API_GetRealtimeLogConfig_RequestSyntax) **   <a name="cloudfront-GetRealtimeLogConfig-request-Name"></a>
The name of the real-time log configuration to get.  
Type: String  
Required: No

## Response Syntax
<a name="API_GetRealtimeLogConfig_ResponseSyntax"></a>

```
HTTP/1.1 200
<?xml version="1.0" encoding="UTF-8"?>
<GetRealtimeLogConfigResult>
   <RealtimeLogConfig>
      <ARN>string</ARN>
      <EndPoints>
         <EndPoint>
            <KinesisStreamConfig>
               <RoleARN>string</RoleARN>
               <StreamARN>string</StreamARN>
            </KinesisStreamConfig>
            <StreamType>string</StreamType>
         </EndPoint>
      </EndPoints>
      <Fields>
         <Field>string</Field>
      </Fields>
      <Name>string</Name>
      <SamplingRate>long</SamplingRate>
   </RealtimeLogConfig>
</GetRealtimeLogConfigResult>
```

## Response Elements
<a name="API_GetRealtimeLogConfig_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in XML format by the service.

 ** [GetRealtimeLogConfigResult](#API_GetRealtimeLogConfig_ResponseSyntax) **   <a name="cloudfront-GetRealtimeLogConfig-response-GetRealtimeLogConfigResult"></a>
Root level tag for the GetRealtimeLogConfigResult parameters.  
Required: Yes

 ** [RealtimeLogConfig](#API_GetRealtimeLogConfig_ResponseSyntax) **   <a name="cloudfront-GetRealtimeLogConfig-response-RealtimeLogConfig"></a>
A real-time log configuration.  
Type: [RealtimeLogConfig](API_RealtimeLogConfig.md) object

## Errors
<a name="API_GetRealtimeLogConfig_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDenied **   
Access denied.  
HTTP Status Code: 403

 ** InvalidArgument **   
An argument is invalid.  
HTTP Status Code: 400

 ** NoSuchRealtimeLogConfig **   
The real-time log configuration does not exist.  
HTTP Status Code: 404

## See Also
<a name="API_GetRealtimeLogConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/cloudfront-2020-05-31/GetRealtimeLogConfig) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/cloudfront-2020-05-31/GetRealtimeLogConfig) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cloudfront-2020-05-31/GetRealtimeLogConfig) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/cloudfront-2020-05-31/GetRealtimeLogConfig) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudfront-2020-05-31/GetRealtimeLogConfig) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cloudfront-2020-05-31/GetRealtimeLogConfig) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/cloudfront-2020-05-31/GetRealtimeLogConfig) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/cloudfront-2020-05-31/GetRealtimeLogConfig) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/cloudfront-2020-05-31/GetRealtimeLogConfig) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudfront-2020-05-31/GetRealtimeLogConfig) 