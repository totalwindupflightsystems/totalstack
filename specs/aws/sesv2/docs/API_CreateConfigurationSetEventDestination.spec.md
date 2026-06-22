---
id: "@specs/aws/sesv2/docs/API_CreateConfigurationSetEventDestination"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS CreateConfigurationSetEventDestination"
status: active
depends_on:
  - "@specs/aws/sesv2/meta"
---

# CreateConfigurationSetEventDestination

> **source:** AWS Documentation
> **spec:id:** @specs/aws/sesv2/docs/API_CreateConfigurationSetEventDestination
> **target_lang:** meta — documentation tier. ALL sections preserved.



# CreateConfigurationSetEventDestination
<a name="API_CreateConfigurationSetEventDestination"></a>

Create an event destination. *Events* include message sends, deliveries, opens, clicks, bounces, and complaints. *Event destinations* are places that you can send information about these events to. For example, you can send event data to Amazon EventBridge and associate a rule to send the event to the specified target.

A single configuration set can include more than one event destination.

## Request Syntax
<a name="API_CreateConfigurationSetEventDestination_RequestSyntax"></a>

```
POST /v2/email/configuration-sets/{{ConfigurationSetName}}/event-destinations HTTP/1.1
Content-type: application/json

{
   "EventDestination": { 
      "CloudWatchDestination": { 
         "DimensionConfigurations": [ 
            { 
               "DefaultDimensionValue": "{{string}}",
               "DimensionName": "{{string}}",
               "DimensionValueSource": "{{string}}"
            }
         ]
      },
      "Enabled": {{boolean}},
      "EventBridgeDestination": { 
         "EventBusArn": "{{string}}"
      },
      "KinesisFirehoseDestination": { 
         "DeliveryStreamArn": "{{string}}",
         "IamRoleArn": "{{string}}"
      },
      "MatchingEventTypes": [ "{{string}}" ],
      "PinpointDestination": { 
         "ApplicationArn": "{{string}}"
      },
      "SnsDestination": { 
         "TopicArn": "{{string}}"
      }
   },
   "EventDestinationName": "{{string}}"
}
```

## URI Request Parameters
<a name="API_CreateConfigurationSetEventDestination_RequestParameters"></a>

The request uses the following URI parameters.

 ** [ConfigurationSetName](#API_CreateConfigurationSetEventDestination_RequestSyntax) **   <a name="SES-CreateConfigurationSetEventDestination-request-uri-ConfigurationSetName"></a>
The name of the configuration set .  
Required: Yes

## Request Body
<a name="API_CreateConfigurationSetEventDestination_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [EventDestination](#API_CreateConfigurationSetEventDestination_RequestSyntax) **   <a name="SES-CreateConfigurationSetEventDestination-request-EventDestination"></a>
An object that defines the event destination.  
Type: [EventDestinationDefinition](API_EventDestinationDefinition.md) object  
Required: Yes

 ** [EventDestinationName](#API_CreateConfigurationSetEventDestination_RequestSyntax) **   <a name="SES-CreateConfigurationSetEventDestination-request-EventDestinationName"></a>
A name that identifies the event destination within the configuration set.  
Type: String  
Required: Yes

## Response Syntax
<a name="API_CreateConfigurationSetEventDestination_ResponseSyntax"></a>

```
HTTP/1.1 200
```

## Response Elements
<a name="API_CreateConfigurationSetEventDestination_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_CreateConfigurationSetEventDestination_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AlreadyExistsException **   
The resource specified in your request already exists.  
HTTP Status Code: 400

 ** BadRequestException **   
The input you provided is invalid.  
HTTP Status Code: 400

 ** LimitExceededException **   
There are too many instances of the specified resource type.  
HTTP Status Code: 400

 ** NotFoundException **   
The resource you attempted to access doesn't exist.  
HTTP Status Code: 404

 ** TooManyRequestsException **   
Too many requests have been made to the operation.  
HTTP Status Code: 429

## See Also
<a name="API_CreateConfigurationSetEventDestination_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/sesv2-2019-09-27/CreateConfigurationSetEventDestination) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/sesv2-2019-09-27/CreateConfigurationSetEventDestination) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sesv2-2019-09-27/CreateConfigurationSetEventDestination) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/sesv2-2019-09-27/CreateConfigurationSetEventDestination) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sesv2-2019-09-27/CreateConfigurationSetEventDestination) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/sesv2-2019-09-27/CreateConfigurationSetEventDestination) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/sesv2-2019-09-27/CreateConfigurationSetEventDestination) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/sesv2-2019-09-27/CreateConfigurationSetEventDestination) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/sesv2-2019-09-27/CreateConfigurationSetEventDestination) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sesv2-2019-09-27/CreateConfigurationSetEventDestination) 