---
id: "@specs/aws/appsync/docs/API_UpdateApi"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS UpdateApi"
status: active
depends_on:
  - "@specs/aws/appsync/meta"
---

# UpdateApi

> **source:** AWS Documentation
> **spec:id:** @specs/aws/appsync/docs/API_UpdateApi
> **target_lang:** meta — documentation tier. ALL sections preserved.



# UpdateApi
<a name="API_UpdateApi"></a>

Updates an `Api`.

## Request Syntax
<a name="API_UpdateApi_RequestSyntax"></a>

```
POST /v2/apis/{{apiId}} HTTP/1.1
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
   "ownerContact": "{{string}}"
}
```

## URI Request Parameters
<a name="API_UpdateApi_RequestParameters"></a>

The request uses the following URI parameters.

 ** [apiId](#API_UpdateApi_RequestSyntax) **   <a name="appsync-UpdateApi-request-uri-apiId"></a>
The `Api` ID.  
Required: Yes

## Request Body
<a name="API_UpdateApi_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [eventConfig](#API_UpdateApi_RequestSyntax) **   <a name="appsync-UpdateApi-request-eventConfig"></a>
The new event configuration. This includes the default authorization configuration for connecting, publishing, and subscribing to an Event API.  
Type: [EventConfig](API_EventConfig.md) object  
Required: No

 ** [name](#API_UpdateApi_RequestSyntax) **   <a name="appsync-UpdateApi-request-name"></a>
The name of the Api.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 50.  
Pattern: `[A-Za-z0-9_\-\ ]+`   
Required: Yes

 ** [ownerContact](#API_UpdateApi_RequestSyntax) **   <a name="appsync-UpdateApi-request-ownerContact"></a>
The owner contact information for the `Api`.  
Type: String  
Required: No

## Response Syntax
<a name="API_UpdateApi_ResponseSyntax"></a>

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
<a name="API_UpdateApi_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [api](#API_UpdateApi_ResponseSyntax) **   <a name="appsync-UpdateApi-response-api"></a>
The `Api` object.  
Type: [Api](API_Api.md) object

## Errors
<a name="API_UpdateApi_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **   
You don't have access to perform this operation on this resource.  
HTTP Status Code: 403

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

 ** NotFoundException **   
The resource specified in the request was not found. Check the resource, and then try again.  
HTTP Status Code: 404

 ** UnauthorizedException **   
You aren't authorized to perform this operation.  
HTTP Status Code: 401

## See Also
<a name="API_UpdateApi_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/appsync-2017-07-25/UpdateApi) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/appsync-2017-07-25/UpdateApi) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/appsync-2017-07-25/UpdateApi) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/appsync-2017-07-25/UpdateApi) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/appsync-2017-07-25/UpdateApi) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/appsync-2017-07-25/UpdateApi) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/appsync-2017-07-25/UpdateApi) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/appsync-2017-07-25/UpdateApi) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/appsync-2017-07-25/UpdateApi) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/appsync-2017-07-25/UpdateApi) 