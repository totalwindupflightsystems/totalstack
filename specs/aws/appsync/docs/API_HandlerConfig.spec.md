---
id: "@specs/aws/appsync/docs/API_HandlerConfig"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS HandlerConfig"
status: active
depends_on:
  - "@specs/aws/appsync/meta"
---

# HandlerConfig

> **source:** AWS Documentation
> **spec:id:** @specs/aws/appsync/docs/API_HandlerConfig
> **target_lang:** meta — documentation tier. ALL sections preserved.



# HandlerConfig
<a name="API_HandlerConfig"></a>

The configuration for a handler.

## Contents
<a name="API_HandlerConfig_Contents"></a>

 ** behavior **   <a name="appsync-Type-HandlerConfig-behavior"></a>
The behavior for the handler.  
Type: String  
Valid Values: `CODE | DIRECT`   
Required: Yes

 ** integration **   <a name="appsync-Type-HandlerConfig-integration"></a>
The integration data source configuration for the handler.  
Type: [Integration](API_Integration.md) object  
Required: Yes

## See Also
<a name="API_HandlerConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/appsync-2017-07-25/HandlerConfig) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/appsync-2017-07-25/HandlerConfig) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/appsync-2017-07-25/HandlerConfig) 