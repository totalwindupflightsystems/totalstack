---
id: "@specs/aws/appsync/docs/API_CreateGraphqlApi"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS CreateGraphqlApi"
status: active
depends_on:
  - "@specs/aws/appsync/meta"
---

# CreateGraphqlApi

> **source:** AWS Documentation
> **spec:id:** @specs/aws/appsync/docs/API_CreateGraphqlApi
> **target_lang:** meta — documentation tier. ALL sections preserved.



# CreateGraphqlApi
<a name="API_CreateGraphqlApi"></a>

Creates a `GraphqlApi` object.

## Request Syntax
<a name="API_CreateGraphqlApi_RequestSyntax"></a>

```
POST /v1/apis HTTP/1.1
Content-type: application/json

{
   "additionalAuthenticationProviders": [ 
      { 
         "authenticationType": "{{string}}",
         "lambdaAuthorizerConfig": { 
            "authorizerResultTtlInSeconds": {{number}},
            "authorizerUri": "{{string}}",
            "identityValidationExpression": "{{string}}"
         },
         "openIDConnectConfig": { 
            "authTTL": {{number}},
            "clientId": "{{string}}",
            "iatTTL": {{number}},
            "issuer": "{{string}}"
         },
         "userPoolConfig": { 
            "appIdClientRegex": "{{string}}",
            "awsRegion": "{{string}}",
            "userPoolId": "{{string}}"
         }
      }
   ],
   "apiType": "{{string}}",
   "authenticationType": "{{string}}",
   "enhancedMetricsConfig": { 
      "dataSourceLevelMetricsBehavior": "{{string}}",
      "operationLevelMetricsConfig": "{{string}}",
      "resolverLevelMetricsBehavior": "{{string}}"
   },
   "introspectionConfig": "{{string}}",
   "lambdaAuthorizerConfig": { 
      "authorizerResultTtlInSeconds": {{number}},
      "authorizerUri": "{{string}}",
      "identityValidationExpression": "{{string}}"
   },
   "logConfig": { 
      "cloudWatchLogsRoleArn": "{{string}}",
      "excludeVerboseContent": {{boolean}},
      "fieldLogLevel": "{{string}}"
   },
   "mergedApiExecutionRoleArn": "{{string}}",
   "name": "{{string}}",
   "openIDConnectConfig": { 
      "authTTL": {{number}},
      "clientId": "{{string}}",
      "iatTTL": {{number}},
      "issuer": "{{string}}"
   },
   "ownerContact": "{{string}}",
   "queryDepthLimit": {{number}},
   "resolverCountLimit": {{number}},
   "tags": { 
      "{{string}}" : "{{string}}" 
   },
   "userPoolConfig": { 
      "appIdClientRegex": "{{string}}",
      "awsRegion": "{{string}}",
      "defaultAction": "{{string}}",
      "userPoolId": "{{string}}"
   },
   "visibility": "{{string}}",
   "xrayEnabled": {{boolean}}
}
```

## URI Request Parameters
<a name="API_CreateGraphqlApi_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_CreateGraphqlApi_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [additionalAuthenticationProviders](#API_CreateGraphqlApi_RequestSyntax) **   <a name="appsync-CreateGraphqlApi-request-additionalAuthenticationProviders"></a>
A list of additional authentication providers for the `GraphqlApi` API.  
Type: Array of [AdditionalAuthenticationProvider](API_AdditionalAuthenticationProvider.md) objects  
Required: No

 ** [apiType](#API_CreateGraphqlApi_RequestSyntax) **   <a name="appsync-CreateGraphqlApi-request-apiType"></a>
The value that indicates whether the GraphQL API is a standard API (`GRAPHQL`) or merged API (`MERGED`).  
Type: String  
Valid Values: `GRAPHQL | MERGED`   
Required: No

 ** [authenticationType](#API_CreateGraphqlApi_RequestSyntax) **   <a name="appsync-CreateGraphqlApi-request-authenticationType"></a>
The authentication type: API key, AWS Identity and Access Management (IAM), OpenID Connect (OIDC), Amazon Cognito user pools, or AWS Lambda.  
Type: String  
Valid Values: `API_KEY | AWS_IAM | AMAZON_COGNITO_USER_POOLS | OPENID_CONNECT | AWS_LAMBDA`   
Required: Yes

 ** [enhancedMetricsConfig](#API_CreateGraphqlApi_RequestSyntax) **   <a name="appsync-CreateGraphqlApi-request-enhancedMetricsConfig"></a>
The `enhancedMetricsConfig` object.  
Type: [EnhancedMetricsConfig](API_EnhancedMetricsConfig.md) object  
Required: No

 ** [introspectionConfig](#API_CreateGraphqlApi_RequestSyntax) **   <a name="appsync-CreateGraphqlApi-request-introspectionConfig"></a>
Sets the value of the GraphQL API to enable (`ENABLED`) or disable (`DISABLED`) introspection. If no value is provided, the introspection configuration will be set to `ENABLED` by default. This field will produce an error if the operation attempts to use the introspection feature while this field is disabled.  
For more information about introspection, see [GraphQL introspection](https://graphql.org/learn/introspection/).  
Type: String  
Valid Values: `ENABLED | DISABLED`   
Required: No

 ** [lambdaAuthorizerConfig](#API_CreateGraphqlApi_RequestSyntax) **   <a name="appsync-CreateGraphqlApi-request-lambdaAuthorizerConfig"></a>
Configuration for AWS Lambda function authorization.  
Type: [LambdaAuthorizerConfig](API_LambdaAuthorizerConfig.md) object  
Required: No

 ** [logConfig](#API_CreateGraphqlApi_RequestSyntax) **   <a name="appsync-CreateGraphqlApi-request-logConfig"></a>
The Amazon CloudWatch Logs configuration.  
Type: [LogConfig](API_LogConfig.md) object  
Required: No

 ** [mergedApiExecutionRoleArn](#API_CreateGraphqlApi_RequestSyntax) **   <a name="appsync-CreateGraphqlApi-request-mergedApiExecutionRoleArn"></a>
The Identity and Access Management service role ARN for a merged API. The AppSync service assumes this role on behalf of the Merged API to validate access to source APIs at runtime and to prompt the `AUTO_MERGE` to update the merged API endpoint with the source API changes automatically.  
Type: String  
Required: No

 ** [name](#API_CreateGraphqlApi_RequestSyntax) **   <a name="appsync-CreateGraphqlApi-request-name"></a>
A user-supplied name for the `GraphqlApi`.  
Type: String  
Required: Yes

 ** [openIDConnectConfig](#API_CreateGraphqlApi_RequestSyntax) **   <a name="appsync-CreateGraphqlApi-request-openIDConnectConfig"></a>
The OIDC configuration.  
Type: [OpenIDConnectConfig](API_OpenIDConnectConfig.md) object  
Required: No

 ** [ownerContact](#API_CreateGraphqlApi_RequestSyntax) **   <a name="appsync-CreateGraphqlApi-request-ownerContact"></a>
The owner contact information for an API resource.  
This field accepts any string input with a length of 0 - 256 characters.  
Type: String  
Required: No

 ** [queryDepthLimit](#API_CreateGraphqlApi_RequestSyntax) **   <a name="appsync-CreateGraphqlApi-request-queryDepthLimit"></a>
The maximum depth a query can have in a single request. Depth refers to the amount of nested levels allowed in the body of query. The default value is `0` (or unspecified), which indicates there's no depth limit. If you set a limit, it can be between `1` and `75` nested levels. This field will produce a limit error if the operation falls out of bounds.  
Note that fields can still be set to nullable or non-nullable. If a non-nullable field produces an error, the error will be thrown upwards to the first nullable field available.  
Type: Integer  
Valid Range: Minimum value of 0. Maximum value of 75.  
Required: No

 ** [resolverCountLimit](#API_CreateGraphqlApi_RequestSyntax) **   <a name="appsync-CreateGraphqlApi-request-resolverCountLimit"></a>
The maximum number of resolvers that can be invoked in a single request. The default value is `0` (or unspecified), which will set the limit to `10000`. When specified, the limit value can be between `1` and `10000`. This field will produce a limit error if the operation falls out of bounds.  
Type: Integer  
Valid Range: Minimum value of 0. Maximum value of 10000.  
Required: No

 ** [tags](#API_CreateGraphqlApi_RequestSyntax) **   <a name="appsync-CreateGraphqlApi-request-tags"></a>
A `TagMap` object.  
Type: String to string map  
Map Entries: Maximum number of 50 items.  
Key Length Constraints: Minimum length of 1. Maximum length of 128.  
Key Pattern: `^(?!aws:)[ a-zA-Z+-=._:/]+$`   
Value Length Constraints: Maximum length of 256.  
Value Pattern: `^[\s\w+-=\.:/@]*$`   
Required: No

 ** [userPoolConfig](#API_CreateGraphqlApi_RequestSyntax) **   <a name="appsync-CreateGraphqlApi-request-userPoolConfig"></a>
The Amazon Cognito user pool configuration.  
Type: [UserPoolConfig](API_UserPoolConfig.md) object  
Required: No

 ** [visibility](#API_CreateGraphqlApi_RequestSyntax) **   <a name="appsync-CreateGraphqlApi-request-visibility"></a>
Sets the value of the GraphQL API to public (`GLOBAL`) or private (`PRIVATE`). If no value is provided, the visibility will be set to `GLOBAL` by default. This value cannot be changed once the API has been created.  
Type: String  
Valid Values: `GLOBAL | PRIVATE`   
Required: No

 ** [xrayEnabled](#API_CreateGraphqlApi_RequestSyntax) **   <a name="appsync-CreateGraphqlApi-request-xrayEnabled"></a>
A flag indicating whether to use AWS X-Ray tracing for the `GraphqlApi`.  
Type: Boolean  
Required: No

## Response Syntax
<a name="API_CreateGraphqlApi_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "graphqlApi": { 
      "additionalAuthenticationProviders": [ 
         { 
            "authenticationType": "string",
            "lambdaAuthorizerConfig": { 
               "authorizerResultTtlInSeconds": number,
               "authorizerUri": "string",
               "identityValidationExpression": "string"
            },
            "openIDConnectConfig": { 
               "authTTL": number,
               "clientId": "string",
               "iatTTL": number,
               "issuer": "string"
            },
            "userPoolConfig": { 
               "appIdClientRegex": "string",
               "awsRegion": "string",
               "userPoolId": "string"
            }
         }
      ],
      "apiId": "string",
      "apiType": "string",
      "arn": "string",
      "authenticationType": "string",
      "dns": { 
         "string" : "string" 
      },
      "enhancedMetricsConfig": { 
         "dataSourceLevelMetricsBehavior": "string",
         "operationLevelMetricsConfig": "string",
         "resolverLevelMetricsBehavior": "string"
      },
      "introspectionConfig": "string",
      "lambdaAuthorizerConfig": { 
         "authorizerResultTtlInSeconds": number,
         "authorizerUri": "string",
         "identityValidationExpression": "string"
      },
      "logConfig": { 
         "cloudWatchLogsRoleArn": "string",
         "excludeVerboseContent": boolean,
         "fieldLogLevel": "string"
      },
      "mergedApiExecutionRoleArn": "string",
      "name": "string",
      "openIDConnectConfig": { 
         "authTTL": number,
         "clientId": "string",
         "iatTTL": number,
         "issuer": "string"
      },
      "owner": "string",
      "ownerContact": "string",
      "queryDepthLimit": number,
      "resolverCountLimit": number,
      "tags": { 
         "string" : "string" 
      },
      "uris": { 
         "string" : "string" 
      },
      "userPoolConfig": { 
         "appIdClientRegex": "string",
         "awsRegion": "string",
         "defaultAction": "string",
         "userPoolId": "string"
      },
      "visibility": "string",
      "wafWebAclArn": "string",
      "xrayEnabled": boolean
   }
}
```

## Response Elements
<a name="API_CreateGraphqlApi_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [graphqlApi](#API_CreateGraphqlApi_ResponseSyntax) **   <a name="appsync-CreateGraphqlApi-response-graphqlApi"></a>
The `GraphqlApi`.  
Type: [GraphqlApi](API_GraphqlApi.md) object

## Errors
<a name="API_CreateGraphqlApi_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ApiLimitExceededException **   
The GraphQL API exceeded a limit. Try your request again.  
HTTP Status Code: 400

 ** BadRequestException **   
The request is not well formed. For example, a value is invalid or a required field is missing. Check the field values, and then try again.    
 ** detail **   
Provides further details for the reason behind the bad request. For reason type `CODE_ERROR`, the detail will contain a list of code errors.  
 ** reason **   
Provides context for the cause of the bad request. The only supported value is `CODE_ERROR`.
HTTP Status Code: 400

 ** ConcurrentModificationException **   
Another modification is in progress at this time and it must complete before you can make your change.  
HTTP Status Code: 409

 ** InternalFailureException **   
An internal AWS AppSync error occurred. Try your request again.  
HTTP Status Code: 500

 ** LimitExceededException **   
The request exceeded a limit. Try your request again.  
HTTP Status Code: 429

 ** UnauthorizedException **   
You aren't authorized to perform this operation.  
HTTP Status Code: 401

## See Also
<a name="API_CreateGraphqlApi_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/appsync-2017-07-25/CreateGraphqlApi) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/appsync-2017-07-25/CreateGraphqlApi) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/appsync-2017-07-25/CreateGraphqlApi) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/appsync-2017-07-25/CreateGraphqlApi) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/appsync-2017-07-25/CreateGraphqlApi) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/appsync-2017-07-25/CreateGraphqlApi) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/appsync-2017-07-25/CreateGraphqlApi) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/appsync-2017-07-25/CreateGraphqlApi) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/appsync-2017-07-25/CreateGraphqlApi) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/appsync-2017-07-25/CreateGraphqlApi) 