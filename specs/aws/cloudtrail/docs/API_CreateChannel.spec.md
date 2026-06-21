---
id: "@specs/aws/cloudtrail/docs/API_CreateChannel"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS CreateChannel"
status: active
depends_on:
  - "@specs/aws/cloudtrail/meta"
---

# CreateChannel

> **source:** AWS Documentation
> **spec:id:** @specs/aws/cloudtrail/docs/API_CreateChannel
> **target_lang:** meta — documentation tier. ALL sections preserved.



# CreateChannel
<a name="API_CreateChannel"></a>

**Important**  
CloudTrail Lake will no longer be open to new customers starting May 31, 2026. If you would like to use CloudTrail Lake, sign up prior to that date. Existing customers can continue to use the service as normal. For more information, see [CloudTrail Lake availability change](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-lake-service-availability-change.html).

Creates a channel for CloudTrail to ingest events from a partner or external source. After you create a channel, a CloudTrail Lake event data store can log events from the partner or source that you specify.

## Request Syntax
<a name="API_CreateChannel_RequestSyntax"></a>

```
{
   "Destinations": [ 
      { 
         "Location": "{{string}}",
         "Type": "{{string}}"
      }
   ],
   "Name": "{{string}}",
   "Source": "{{string}}",
   "Tags": [ 
      { 
         "Key": "{{string}}",
         "Value": "{{string}}"
      }
   ]
}
```

## Request Parameters
<a name="API_CreateChannel_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [Destinations](#API_CreateChannel_RequestSyntax) **   <a name="awscloudtrail-CreateChannel-request-Destinations"></a>
One or more event data stores to which events arriving through a channel will be logged.  
Type: Array of [Destination](API_Destination.md) objects  
Array Members: Minimum number of 1 item. Maximum number of 200 items.  
Required: Yes

 ** [Name](#API_CreateChannel_RequestSyntax) **   <a name="awscloudtrail-CreateChannel-request-Name"></a>
The name of the channel.  
Type: String  
Length Constraints: Minimum length of 3. Maximum length of 128.  
Pattern: `^[a-zA-Z0-9._\-]+$`   
Required: Yes

 ** [Source](#API_CreateChannel_RequestSyntax) **   <a name="awscloudtrail-CreateChannel-request-Source"></a>
The name of the partner or external event source. You cannot change this name after you create the channel. A maximum of one channel is allowed per source.  
 A source can be either `Custom` for all valid non-AWS events, or the name of a partner event source. For information about the source names for available partners, see [Additional information about integration partners](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/query-event-data-store-integration.html#cloudtrail-lake-partner-information) in the CloudTrail User Guide.   
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 256.  
Pattern: `.*`   
Required: Yes

 ** [Tags](#API_CreateChannel_RequestSyntax) **   <a name="awscloudtrail-CreateChannel-request-Tags"></a>
A list of tags.  
Type: Array of [Tag](API_Tag.md) objects  
Array Members: Maximum number of 200 items.  
Required: No

## Response Syntax
<a name="API_CreateChannel_ResponseSyntax"></a>

```
{
   "ChannelArn": "string",
   "Destinations": [ 
      { 
         "Location": "string",
         "Type": "string"
      }
   ],
   "Name": "string",
   "Source": "string",
   "Tags": [ 
      { 
         "Key": "string",
         "Value": "string"
      }
   ]
}
```

## Response Elements
<a name="API_CreateChannel_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ChannelArn](#API_CreateChannel_ResponseSyntax) **   <a name="awscloudtrail-CreateChannel-response-ChannelArn"></a>
The Amazon Resource Name (ARN) of the new channel.  
Type: String  
Length Constraints: Minimum length of 3. Maximum length of 256.  
Pattern: `^[a-zA-Z0-9._/\-:]+$` 

 ** [Destinations](#API_CreateChannel_ResponseSyntax) **   <a name="awscloudtrail-CreateChannel-response-Destinations"></a>
The event data stores that log the events arriving through the channel.  
Type: Array of [Destination](API_Destination.md) objects  
Array Members: Minimum number of 1 item. Maximum number of 200 items.

 ** [Name](#API_CreateChannel_ResponseSyntax) **   <a name="awscloudtrail-CreateChannel-response-Name"></a>
The name of the new channel.  
Type: String  
Length Constraints: Minimum length of 3. Maximum length of 128.  
Pattern: `^[a-zA-Z0-9._\-]+$` 

 ** [Source](#API_CreateChannel_ResponseSyntax) **   <a name="awscloudtrail-CreateChannel-response-Source"></a>
The partner or external event source name.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 256.  
Pattern: `.*` 

 ** [Tags](#API_CreateChannel_ResponseSyntax) **   <a name="awscloudtrail-CreateChannel-response-Tags"></a>
A list of tags.  
Type: Array of [Tag](API_Tag.md) objects  
Array Members: Maximum number of 200 items.

## Errors
<a name="API_CreateChannel_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ChannelAlreadyExistsException **   
 This exception is thrown when the provided channel already exists.   
HTTP Status Code: 400

 ** ChannelMaxLimitExceededException **   
 This exception is thrown when the maximum number of channels limit is exceeded.   
HTTP Status Code: 400

 ** EventDataStoreARNInvalidException **   
The specified event data store ARN is not valid or does not map to an event data store in your account.  
HTTP Status Code: 400

 ** EventDataStoreNotFoundException **   
The specified event data store was not found.  
HTTP Status Code: 400

 ** InactiveEventDataStoreException **   
The event data store is inactive.  
HTTP Status Code: 400

 ** InvalidEventDataStoreCategoryException **   
This exception is thrown when event categories of specified event data stores are not valid.  
HTTP Status Code: 400

 ** InvalidParameterException **   
The request includes a parameter that is not valid.  
HTTP Status Code: 400

 ** InvalidSourceException **   
This exception is thrown when the specified value of `Source` is not valid.  
HTTP Status Code: 400

 ** InvalidTagParameterException **   
This exception is thrown when the specified tag key or values are not valid. It can also occur if there are duplicate tags or too many tags on the resource.  
HTTP Status Code: 400

 ** OperationNotPermittedException **   
This exception is thrown when the requested operation is not permitted.  
HTTP Status Code: 400

 ** TagsLimitExceededException **   
The number of tags per trail, event data store, dashboard, or channel has exceeded the permitted amount. Currently, the limit is 50.  
HTTP Status Code: 400

 ** UnsupportedOperationException **   
This exception is thrown when the requested operation is not supported.  
HTTP Status Code: 400

## See Also
<a name="API_CreateChannel_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/cloudtrail-2013-11-01/CreateChannel) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/cloudtrail-2013-11-01/CreateChannel) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cloudtrail-2013-11-01/CreateChannel) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/cloudtrail-2013-11-01/CreateChannel) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudtrail-2013-11-01/CreateChannel) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cloudtrail-2013-11-01/CreateChannel) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/cloudtrail-2013-11-01/CreateChannel) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/cloudtrail-2013-11-01/CreateChannel) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/cloudtrail-2013-11-01/CreateChannel) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudtrail-2013-11-01/CreateChannel) 