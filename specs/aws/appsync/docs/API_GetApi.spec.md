---
id: "@specs/aws/appsync/docs/API_GetApi"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS GetApi"
status: active
depends_on:
  - "@specs/aws/appsync/meta"
---

# GetApi

> **source:** AWS Documentation
> **spec:id:** @specs/aws/appsync/docs/API_GetApi
> **target_lang:** meta — documentation tier. ALL sections preserved.



# GetApi
<a name="API_GetApi"></a>

Retrieves an `Api` object.

## Request Syntax
<a name="API_GetApi_RequestSyntax"></a>

```
GET /v2/apis/{{apiId}} HTTP/1.1
```

## URI Request Parameters
<a name="API_GetApi_RequestParameters"></a>

The request uses the following URI parameters.

 ** [apiId](#API_GetApi_RequestSyntax) **   <a name="appsync-GetApi-request-uri-apiId"></a>
The `Api` ID.  
Required: Yes

## Request Body
<a name="API_GetApi_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetApi_ResponseSyntax"></a>

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
<a name="API_GetApi_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [api](#API_GetApi_ResponseSyntax) **   <a name="appsync-GetApi-response-api"></a>
The `Api` object.  
Type: [Api](API_Api.md) object

## Errors
<a name="API_GetApi_Errors"></a>

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
<a name="API_GetApi_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/appsync-2017-07-25/GetApi) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/appsync-2017-07-25/GetApi) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/appsync-2017-07-25/GetApi) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/appsync-2017-07-25/GetApi) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/appsync-2017-07-25/GetApi) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/appsync-2017-07-25/GetApi) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/appsync-2017-07-25/GetApi) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/appsync-2017-07-25/GetApi) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/appsync-2017-07-25/GetApi) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/appsync-2017-07-25/GetApi) 