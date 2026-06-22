---
id: "@specs/aws/appsync/docs/API_AuthMode"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS AuthMode"
status: active
depends_on:
  - "@specs/aws/appsync/meta"
---

# AuthMode

> **source:** AWS Documentation
> **spec:id:** @specs/aws/appsync/docs/API_AuthMode
> **target_lang:** meta — documentation tier. ALL sections preserved.



# AuthMode
<a name="API_AuthMode"></a>

Describes an authorization configuration. Use `AuthMode` to specify the publishing and subscription authorization configuration for an Event API.

## Contents
<a name="API_AuthMode_Contents"></a>

 ** authType **   <a name="appsync-Type-AuthMode-authType"></a>
The authorization type.  
Type: String  
Valid Values: `API_KEY | AWS_IAM | AMAZON_COGNITO_USER_POOLS | OPENID_CONNECT | AWS_LAMBDA`   
Required: Yes

## See Also
<a name="API_AuthMode_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/appsync-2017-07-25/AuthMode) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/appsync-2017-07-25/AuthMode) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/appsync-2017-07-25/AuthMode) 