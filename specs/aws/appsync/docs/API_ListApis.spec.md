---
id: "@specs/aws/appsync/docs/API_ListApis"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS ListApis"
status: active
depends_on:
  - "@specs/aws/appsync/meta"
---

# ListApis

> **source:** AWS Documentation
> **spec:id:** @specs/aws/appsync/docs/API_ListApis
> **target_lang:** meta — documentation tier. ALL sections preserved.



# ListApis
<a name="API_ListApis"></a>

Lists the APIs in your AWS AppSync account.

 `ListApis` returns only the high level API details. For more detailed information about an API, use `GetApi`.

## Request Syntax
<a name="API_ListApis_RequestSyntax"></a>

```
GET /v2/apis?maxResults={{maxResults}}&nextToken={{nextToken}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListApis_RequestParameters"></a>

The request uses the following URI parameters.

 ** [maxResults](#API_ListApis_RequestSyntax) **   <a name="appsync-ListApis-request-uri-maxResults"></a>
The maximum number of results that you want the request to return.  
Valid Range: Minimum value of 0. Maximum value of 25.

 ** [nextToken](#API_ListApis_RequestSyntax) **   <a name="appsync-ListApis-request-uri-nextToken"></a>
An identifier that was returned from the previous call to this operation, which you can use to return the next set of items in the list.  
Length Constraints: Minimum length of 1. Maximum length of 65536.  
Pattern: `[\S]+` 

## Request Body
<a name="API_ListApis_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListApis_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "apis": [ 
      { 
         "apiArn": "string",
         "apiId": "string",
         "created": number,
         "dns": { 
            "string" : "string" 
         },
         "eventConfig": { 
            "authProviders": [ 
               { 
                  "authType": "string",
                  "cognitoConfig": { 
                     "appIdClientRegex": "string",
                     "awsRegion": "string",
                     "userPoolId": "string"
                  },
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
                  }
               }
            ],
            "connectionAuthModes": [ 
               { 
                  "authType": "string"
               }
            ],
            "defaultPublishAuthModes": [ 
               { 
                  "authType": "string"
               }
            ],
            "defaultSubscribeAuthModes": [ 
               { 
                  "authType": "string"
               }
            ],
            "logConfig": { 
               "cloudWatchLogsRoleArn": "string",
               "logLevel": "string"
            }
         },
         "name": "string",
         "ownerContact": "string",
         "tags": { 
            "string" : "string" 
         },
         "wafWebAclArn": "string",
         "xrayEnabled": boolean
      }
   ],
   "nextToken": "string"
}
```

## Response Elements
<a name="API_ListApis_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [apis](#API_ListApis_ResponseSyntax) **   <a name="appsync-ListApis-response-apis"></a>
The `Api` objects.  
Type: Array of [Api](API_Api.md) objects

 ** [nextToken](#API_ListApis_ResponseSyntax) **   <a name="appsync-ListApis-response-nextToken"></a>
An identifier that was returned from the previous call to this operation, which you can use to return the next set of items in the list.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 65536.  
Pattern: `[\S]+` 

## Errors
<a name="API_ListApis_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** BadRequestException **   
The request is not well formed. For example, a value is invalid or a required field is missing. Check the field values, and then try again.    
 ** detail **   
Provides further details for the reason behind the bad request. For reason type `CODE_ERROR`, the detail will contain a list of code errors.  
 ** reason **   
Provides context for the cause of the bad request. The only supported value is `CODE_ERROR`.
HTTP Status Code: 400

 ** InternalFailureException **   
An internal AWS AppSync error occurred. Try your request again.  
HTTP Status Code: 500

 ** UnauthorizedException **   
You aren't authorized to perform this operation.  
HTTP Status Code: 401

## See Also
<a name="API_ListApis_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/appsync-2017-07-25/ListApis) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/appsync-2017-07-25/ListApis) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/appsync-2017-07-25/ListApis) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/appsync-2017-07-25/ListApis) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/appsync-2017-07-25/ListApis) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/appsync-2017-07-25/ListApis) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/appsync-2017-07-25/ListApis) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/appsync-2017-07-25/ListApis) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/appsync-2017-07-25/ListApis) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/appsync-2017-07-25/ListApis) 