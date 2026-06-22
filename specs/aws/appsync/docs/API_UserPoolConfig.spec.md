---
id: "@specs/aws/appsync/docs/API_UserPoolConfig"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS UserPoolConfig"
status: active
depends_on:
  - "@specs/aws/appsync/meta"
---

# UserPoolConfig

> **source:** AWS Documentation
> **spec:id:** @specs/aws/appsync/docs/API_UserPoolConfig
> **target_lang:** meta — documentation tier. ALL sections preserved.



# UserPoolConfig
<a name="API_UserPoolConfig"></a>

Describes an Amazon Cognito user pool configuration.

## Contents
<a name="API_UserPoolConfig_Contents"></a>

 ** awsRegion **   <a name="appsync-Type-UserPoolConfig-awsRegion"></a>
The AWS Region in which the user pool was created.  
Type: String  
Required: Yes

 ** defaultAction **   <a name="appsync-Type-UserPoolConfig-defaultAction"></a>
The action that you want your GraphQL API to take when a request that uses Amazon Cognito user pool authentication doesn't match the Amazon Cognito user pool configuration.  
Type: String  
Valid Values: `ALLOW | DENY`   
Required: Yes

 ** userPoolId **   <a name="appsync-Type-UserPoolConfig-userPoolId"></a>
The user pool ID.  
Type: String  
Required: Yes

 ** appIdClientRegex **   <a name="appsync-Type-UserPoolConfig-appIdClientRegex"></a>
A regular expression for validating the incoming Amazon Cognito user pool app client ID. If this value isn't set, no filtering is applied.  
Type: String  
Required: No

## See Also
<a name="API_UserPoolConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/appsync-2017-07-25/UserPoolConfig) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/appsync-2017-07-25/UserPoolConfig) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/appsync-2017-07-25/UserPoolConfig) 