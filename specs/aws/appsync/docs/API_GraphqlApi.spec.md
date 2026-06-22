---
id: "@specs/aws/appsync/docs/API_GraphqlApi"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS GraphqlApi"
status: active
depends_on:
  - "@specs/aws/appsync/meta"
---

# GraphqlApi

> **source:** AWS Documentation
> **spec:id:** @specs/aws/appsync/docs/API_GraphqlApi
> **target_lang:** meta — documentation tier. ALL sections preserved.



# GraphqlApi
<a name="API_GraphqlApi"></a>

Describes a GraphQL API.

## Contents
<a name="API_GraphqlApi_Contents"></a>

 ** additionalAuthenticationProviders **   <a name="appsync-Type-GraphqlApi-additionalAuthenticationProviders"></a>
A list of additional authentication providers for the `GraphqlApi` API.  
Type: Array of [AdditionalAuthenticationProvider](API_AdditionalAuthenticationProvider.md) objects  
Required: No

 ** apiId **   <a name="appsync-Type-GraphqlApi-apiId"></a>
The API ID.  
Type: String  
Required: No

 ** apiType **   <a name="appsync-Type-GraphqlApi-apiType"></a>
The value that indicates whether the GraphQL API is a standard API (`GRAPHQL`) or merged API (`MERGED`).  
Type: String  
Valid Values: `GRAPHQL | MERGED`   
Required: No

 ** arn **   <a name="appsync-Type-GraphqlApi-arn"></a>
The Amazon Resource Name (ARN).  
Type: String  
Required: No

 ** authenticationType **   <a name="appsync-Type-GraphqlApi-authenticationType"></a>
The authentication type.  
Type: String  
Valid Values: `API_KEY | AWS_IAM | AMAZON_COGNITO_USER_POOLS | OPENID_CONNECT | AWS_LAMBDA`   
Required: No

 ** dns **   <a name="appsync-Type-GraphqlApi-dns"></a>
The DNS records for the API.  
Type: String to string map  
Required: No

 ** enhancedMetricsConfig **   <a name="appsync-Type-GraphqlApi-enhancedMetricsConfig"></a>
The `enhancedMetricsConfig` object.  
Type: [EnhancedMetricsConfig](API_EnhancedMetricsConfig.md) object  
Required: No

 ** introspectionConfig **   <a name="appsync-Type-GraphqlApi-introspectionConfig"></a>
Sets the value of the GraphQL API to enable (`ENABLED`) or disable (`DISABLED`) introspection. If no value is provided, the introspection configuration will be set to `ENABLED` by default. This field will produce an error if the operation attempts to use the introspection feature while this field is disabled.  
For more information about introspection, see [GraphQL introspection](https://graphql.org/learn/introspection/).  
Type: String  
Valid Values: `ENABLED | DISABLED`   
Required: No

 ** lambdaAuthorizerConfig **   <a name="appsync-Type-GraphqlApi-lambdaAuthorizerConfig"></a>
Configuration for Lambda function authorization.  
Type: [LambdaAuthorizerConfig](API_LambdaAuthorizerConfig.md) object  
Required: No

 ** logConfig **   <a name="appsync-Type-GraphqlApi-logConfig"></a>
The Amazon CloudWatch Logs configuration.  
Type: [LogConfig](API_LogConfig.md) object  
Required: No

 ** mergedApiExecutionRoleArn **   <a name="appsync-Type-GraphqlApi-mergedApiExecutionRoleArn"></a>
The Identity and Access Management service role ARN for a merged API. The AppSync service assumes this role on behalf of the Merged API to validate access to source APIs at runtime and to prompt the `AUTO_MERGE` to update the merged API endpoint with the source API changes automatically.  
Type: String  
Required: No

 ** name **   <a name="appsync-Type-GraphqlApi-name"></a>
The API name.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 65536.  
Pattern: `[_A-Za-z][_0-9A-Za-z]*`   
Required: No

 ** openIDConnectConfig **   <a name="appsync-Type-GraphqlApi-openIDConnectConfig"></a>
The OpenID Connect configuration.  
Type: [OpenIDConnectConfig](API_OpenIDConnectConfig.md) object  
Required: No

 ** owner **   <a name="appsync-Type-GraphqlApi-owner"></a>
The account owner of the GraphQL API.  
Type: String  
Required: No

 ** ownerContact **   <a name="appsync-Type-GraphqlApi-ownerContact"></a>
The owner contact information for an API resource.  
This field accepts any string input with a length of 0 - 256 characters.  
Type: String  
Required: No

 ** queryDepthLimit **   <a name="appsync-Type-GraphqlApi-queryDepthLimit"></a>
The maximum depth a query can have in a single request. Depth refers to the amount of nested levels allowed in the body of query. The default value is `0` (or unspecified), which indicates there's no depth limit. If you set a limit, it can be between `1` and `75` nested levels. This field will produce a limit error if the operation falls out of bounds.  
Note that fields can still be set to nullable or non-nullable. If a non-nullable field produces an error, the error will be thrown upwards to the first nullable field available.  
Type: Integer  
Valid Range: Minimum value of 0. Maximum value of 75.  
Required: No

 ** resolverCountLimit **   <a name="appsync-Type-GraphqlApi-resolverCountLimit"></a>
The maximum number of resolvers that can be invoked in a single request. The default value is `0` (or unspecified), which will set the limit to `10000`. When specified, the limit value can be between `1` and `10000`. This field will produce a limit error if the operation falls out of bounds.  
Type: Integer  
Valid Range: Minimum value of 0. Maximum value of 10000.  
Required: No

 ** tags **   <a name="appsync-Type-GraphqlApi-tags"></a>
The tags.  
Type: String to string map  
Map Entries: Maximum number of 50 items.  
Key Length Constraints: Minimum length of 1. Maximum length of 128.  
Key Pattern: `^(?!aws:)[ a-zA-Z+-=._:/]+$`   
Value Length Constraints: Maximum length of 256.  
Value Pattern: `^[\s\w+-=\.:/@]*$`   
Required: No

 ** uris **   <a name="appsync-Type-GraphqlApi-uris"></a>
The URIs.  
Type: String to string map  
Required: No

 ** userPoolConfig **   <a name="appsync-Type-GraphqlApi-userPoolConfig"></a>
The Amazon Cognito user pool configuration.  
Type: [UserPoolConfig](API_UserPoolConfig.md) object  
Required: No

 ** visibility **   <a name="appsync-Type-GraphqlApi-visibility"></a>
Sets the value of the GraphQL API to public (`GLOBAL`) or private (`PRIVATE`). If no value is provided, the visibility will be set to `GLOBAL` by default. This value cannot be changed once the API has been created.  
Type: String  
Valid Values: `GLOBAL | PRIVATE`   
Required: No

 ** wafWebAclArn **   <a name="appsync-Type-GraphqlApi-wafWebAclArn"></a>
The ARN of the AWS WAF access control list (ACL) associated with this `GraphqlApi`, if one exists.  
Type: String  
Required: No

 ** xrayEnabled **   <a name="appsync-Type-GraphqlApi-xrayEnabled"></a>
A flag indicating whether to use AWS X-Ray tracing for this `GraphqlApi`.  
Type: Boolean  
Required: No

## See Also
<a name="API_GraphqlApi_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/appsync-2017-07-25/GraphqlApi) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/appsync-2017-07-25/GraphqlApi) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/appsync-2017-07-25/GraphqlApi) 