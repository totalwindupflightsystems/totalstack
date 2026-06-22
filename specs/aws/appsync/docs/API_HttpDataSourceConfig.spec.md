---
id: "@specs/aws/appsync/docs/API_HttpDataSourceConfig"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS HttpDataSourceConfig"
status: active
depends_on:
  - "@specs/aws/appsync/meta"
---

# HttpDataSourceConfig

> **source:** AWS Documentation
> **spec:id:** @specs/aws/appsync/docs/API_HttpDataSourceConfig
> **target_lang:** meta — documentation tier. ALL sections preserved.



# HttpDataSourceConfig
<a name="API_HttpDataSourceConfig"></a>

Describes an HTTP data source configuration.

## Contents
<a name="API_HttpDataSourceConfig_Contents"></a>

 ** authorizationConfig **   <a name="appsync-Type-HttpDataSourceConfig-authorizationConfig"></a>
The authorization configuration in case the HTTP endpoint requires authorization.  
Type: [AuthorizationConfig](API_AuthorizationConfig.md) object  
Required: No

 ** endpoint **   <a name="appsync-Type-HttpDataSourceConfig-endpoint"></a>
The HTTP URL endpoint. You can specify either the domain name or IP, and port combination, and the URL scheme must be HTTP or HTTPS. If you don't specify the port, AWS AppSync uses the default port 80 for the HTTP endpoint and port 443 for HTTPS endpoints.  
Type: String  
Required: No

## See Also
<a name="API_HttpDataSourceConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/appsync-2017-07-25/HttpDataSourceConfig) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/appsync-2017-07-25/HttpDataSourceConfig) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/appsync-2017-07-25/HttpDataSourceConfig) 