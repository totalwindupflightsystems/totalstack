---
id: "@specs/aws/appsync/docs/API_CreateApi"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS CreateApi"
status: active
depends_on:
  - "@specs/aws/appsync/meta"
---

# CreateApi

> **source:** AWS Documentation
> **spec:id:** @specs/aws/appsync/docs/API_CreateApi
> **target_lang:** meta — documentation tier. ALL sections preserved.



# CreateApi
<a name="API_CreateApi"></a>

Creates an `Api` object. Use this operation to create an AWS AppSync API with your preferred configuration, such as an Event API that provides real-time message publishing and message subscriptions over WebSockets.

## Request Syntax
<a name="API_CreateApi_RequestSyntax"></a>

```
POST /v2/apis HTTP/1.1
Content-type: application/json

{
   "eventConfig": { 
      "authProviders": [ 
         { 
            "authType": "{{string}}",
            "cognitoConfig": { 
               "appIdClientRegex": "{{string}}",
               "awsRegion": "{{string}}",
               "userPoolId": "{{string}}"
            },
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
            }
         }
      ],
      "connectionAuthModes": [ 
         { 
            "authType": "{{string}}"
         }
      ],
      "defaultPublishAuthModes": [ 
         { 
            "authType": "{{string}}"
         }
      ],
      "defaultSubscribeAuthModes": [ 
         { 
            "authType": "{{string}}"
         }
      ],
      "logConfig": { 
         "cloudWatchLogsRoleArn": "{{string}}",
         "logLevel": "{{string}}"
      }
   },
   "name": "{{string}}",
   "ownerContact": "{{string}}",
   "tags": { 
      "{{string}}" : "{{string}}" 
   }
}
```

## URI Request Parameters
<a name="API_CreateApi_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_CreateApi_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [eventConfig](#API_CreateApi_RequestSyntax) **   <a name="appsync-CreateApi-request-eventConfig"></a>
The Event API configuration. This includes the default authorization configuration for connecting, publishing, and subscribing to an Event API.  
Type: [EventConfig](API_EventConfig.md) object  
Required: No

 ** [name](#API_CreateApi_RequestSyntax) **   <a name="appsync-CreateApi-request-name"></a>
The name for the `Api`.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 50.  
Pattern: `[A-Za-z0-9_\-\ ]+`   
Required: Yes

 ** [ownerContact](#API_CreateApi_RequestSyntax) **   <a name="appsync-CreateApi-request-ownerContact"></a>
The owner contact information for the `Api`.  
Type: String  
Required: No

 ** [tags](#API_CreateApi_RequestSyntax) **   <a name="appsync-CreateApi-request-tags"></a>
A map with keys of `TagKey` objects and values of `TagValue` objects.  
Type: String to string map  
Map Entries: Maximum number of 50 items.  
Key Length Constraints: Minimum length of 1. Maximum length of 128.  
Key Pattern: `^(?!aws:)[ a-zA-Z+-=._:/]+$`   
Value Length Constraints: Maximum length of 256.  
Value Pattern: `^[\s\w+-=\.:/@]*$`   
Required: No

## Response Syntax
<a name="API_CreateApi_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "api": { 
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
}
```

## Response Elements
<a name="API_CreateApi_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [api](#API_CreateApi_ResponseSyntax) **   <a name="appsync-CreateApi-response-api"></a>
The `Api` object.  
Type: [Api](API_Api.md) object

## Errors
<a name="API_CreateApi_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

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

 ** ServiceQuotaExceededException **   
The operation exceeded the service quota for this resource.  
HTTP Status Code: 402

 ** UnauthorizedException **   
You aren't authorized to perform this operation.  
HTTP Status Code: 401

## See Also
<a name="API_CreateApi_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/appsync-2017-07-25/CreateApi) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/appsync-2017-07-25/CreateApi) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/appsync-2017-07-25/CreateApi) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/appsync-2017-07-25/CreateApi) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/appsync-2017-07-25/CreateApi) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/appsync-2017-07-25/CreateApi) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/appsync-2017-07-25/CreateApi) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/appsync-2017-07-25/CreateApi) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/appsync-2017-07-25/CreateApi) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/appsync-2017-07-25/CreateApi) 