---
id: "@specs/aws/appsync/docs/API_UpdateChannelNamespace"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS UpdateChannelNamespace"
status: active
depends_on:
  - "@specs/aws/appsync/meta"
---

# UpdateChannelNamespace

> **source:** AWS Documentation
> **spec:id:** @specs/aws/appsync/docs/API_UpdateChannelNamespace
> **target_lang:** meta — documentation tier. ALL sections preserved.



# UpdateChannelNamespace
<a name="API_UpdateChannelNamespace"></a>

Updates a `ChannelNamespace` associated with an `Api`.

## Request Syntax
<a name="API_UpdateChannelNamespace_RequestSyntax"></a>

```
POST /v2/apis/{{apiId}}/channelNamespaces/{{name}} HTTP/1.1
Content-type: application/json

{
   "codeHandlers": "{{string}}",
   "handlerConfigs": { 
      "onPublish": { 
         "behavior": "{{string}}",
         "integration": { 
            "dataSourceName": "{{string}}",
            "lambdaConfig": { 
               "invokeType": "{{string}}"
            }
         }
      },
      "onSubscribe": { 
         "behavior": "{{string}}",
         "integration": { 
            "dataSourceName": "{{string}}",
            "lambdaConfig": { 
               "invokeType": "{{string}}"
            }
         }
      }
   },
   "publishAuthModes": [ 
      { 
         "authType": "{{string}}"
      }
   ],
   "subscribeAuthModes": [ 
      { 
         "authType": "{{string}}"
      }
   ]
}
```

## URI Request Parameters
<a name="API_UpdateChannelNamespace_RequestParameters"></a>

The request uses the following URI parameters.

 ** [apiId](#API_UpdateChannelNamespace_RequestSyntax) **   <a name="appsync-UpdateChannelNamespace-request-uri-apiId"></a>
The `Api` ID.  
Required: Yes

 ** [name](#API_UpdateChannelNamespace_RequestSyntax) **   <a name="appsync-UpdateChannelNamespace-request-uri-name"></a>
The name of the `ChannelNamespace`.  
Length Constraints: Minimum length of 1. Maximum length of 50.  
Pattern: `([A-Za-z0-9](?:[A-Za-z0-9\-]{0,48}[A-Za-z0-9])?)`   
Required: Yes

## Request Body
<a name="API_UpdateChannelNamespace_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [codeHandlers](#API_UpdateChannelNamespace_RequestSyntax) **   <a name="appsync-UpdateChannelNamespace-request-codeHandlers"></a>
The event handler functions that run custom business logic to process published events and subscribe requests.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 32768.  
Required: No

 ** [handlerConfigs](#API_UpdateChannelNamespace_RequestSyntax) **   <a name="appsync-UpdateChannelNamespace-request-handlerConfigs"></a>
The configuration for the `OnPublish` and `OnSubscribe` handlers.  
Type: [HandlerConfigs](API_HandlerConfigs.md) object  
Required: No

 ** [publishAuthModes](#API_UpdateChannelNamespace_RequestSyntax) **   <a name="appsync-UpdateChannelNamespace-request-publishAuthModes"></a>
The authorization mode to use for publishing messages on the channel namespace. This configuration overrides the default `Api` authorization configuration.  
Type: Array of [AuthMode](API_AuthMode.md) objects  
Required: No

 ** [subscribeAuthModes](#API_UpdateChannelNamespace_RequestSyntax) **   <a name="appsync-UpdateChannelNamespace-request-subscribeAuthModes"></a>
The authorization mode to use for subscribing to messages on the channel namespace. This configuration overrides the default `Api` authorization configuration.  
Type: Array of [AuthMode](API_AuthMode.md) objects  
Required: No

## Response Syntax
<a name="API_UpdateChannelNamespace_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "channelNamespace": { 
      "apiId": "string",
      "channelNamespaceArn": "string",
      "codeHandlers": "string",
      "created": number,
      "handlerConfigs": { 
         "onPublish": { 
            "behavior": "string",
            "integration": { 
               "dataSourceName": "string",
               "lambdaConfig": { 
                  "invokeType": "string"
               }
            }
         },
         "onSubscribe": { 
            "behavior": "string",
            "integration": { 
               "dataSourceName": "string",
               "lambdaConfig": { 
                  "invokeType": "string"
               }
            }
         }
      },
      "lastModified": number,
      "name": "string",
      "publishAuthModes": [ 
         { 
            "authType": "string"
         }
      ],
      "subscribeAuthModes": [ 
         { 
            "authType": "string"
         }
      ],
      "tags": { 
         "string" : "string" 
      }
   }
}
```

## Response Elements
<a name="API_UpdateChannelNamespace_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [channelNamespace](#API_UpdateChannelNamespace_ResponseSyntax) **   <a name="appsync-UpdateChannelNamespace-response-channelNamespace"></a>
The `ChannelNamespace` object.  
Type: [ChannelNamespace](API_ChannelNamespace.md) object

## Errors
<a name="API_UpdateChannelNamespace_Errors"></a>

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
<a name="API_UpdateChannelNamespace_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/appsync-2017-07-25/UpdateChannelNamespace) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/appsync-2017-07-25/UpdateChannelNamespace) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/appsync-2017-07-25/UpdateChannelNamespace) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/appsync-2017-07-25/UpdateChannelNamespace) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/appsync-2017-07-25/UpdateChannelNamespace) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/appsync-2017-07-25/UpdateChannelNamespace) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/appsync-2017-07-25/UpdateChannelNamespace) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/appsync-2017-07-25/UpdateChannelNamespace) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/appsync-2017-07-25/UpdateChannelNamespace) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/appsync-2017-07-25/UpdateChannelNamespace) 