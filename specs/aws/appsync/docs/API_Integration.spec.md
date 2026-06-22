---
id: "@specs/aws/appsync/docs/API_Integration"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Integration"
status: active
depends_on:
  - "@specs/aws/appsync/meta"
---

# Integration

> **source:** AWS Documentation
> **spec:id:** @specs/aws/appsync/docs/API_Integration
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Integration
<a name="API_Integration"></a>

The integration data source configuration for the handler.

## Contents
<a name="API_Integration_Contents"></a>

 ** dataSourceName **   <a name="appsync-Type-Integration-dataSourceName"></a>
The unique name of the data source that has been configured on the API.  
Type: String  
Required: Yes

 ** lambdaConfig **   <a name="appsync-Type-Integration-lambdaConfig"></a>
The configuration for a Lambda data source.  
Type: [LambdaConfig](API_LambdaConfig.md) object  
Required: No

## See Also
<a name="API_Integration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/appsync-2017-07-25/Integration) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/appsync-2017-07-25/Integration) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/appsync-2017-07-25/Integration) 