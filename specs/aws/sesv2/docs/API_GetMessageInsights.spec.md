---
id: "@specs/aws/sesv2/docs/API_GetMessageInsights"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS GetMessageInsights"
status: active
depends_on:
  - "@specs/aws/sesv2/meta"
---

# GetMessageInsights

> **source:** AWS Documentation
> **spec:id:** @specs/aws/sesv2/docs/API_GetMessageInsights
> **target_lang:** meta — documentation tier. ALL sections preserved.



# GetMessageInsights
<a name="API_GetMessageInsights"></a>

Provides information about a specific message, including the from address, the subject, the recipient address, email tags, as well as events associated with the message.

You can execute this operation no more than once per second.

## Request Syntax
<a name="API_GetMessageInsights_RequestSyntax"></a>

```
GET /v2/email/insights/{{MessageId}}/ HTTP/1.1
```

## URI Request Parameters
<a name="API_GetMessageInsights_RequestParameters"></a>

The request uses the following URI parameters.

 ** [MessageId](#API_GetMessageInsights_RequestSyntax) **   <a name="SES-GetMessageInsights-request-uri-MessageId"></a>
 A `MessageId` is a unique identifier for a message, and is returned when sending emails through Amazon SES.   
Required: Yes

## Request Body
<a name="API_GetMessageInsights_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetMessageInsights_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "EmailTags": [ 
      { 
         "Name": "string",
         "Value": "string"
      }
   ],
   "FromEmailAddress": "string",
   "Insights": [ 
      { 
         "Destination": "string",
         "Events": [ 
            { 
               "Details": { 
                  "Bounce": { 
                     "BounceSubType": "string",
                     "BounceType": "string",
                     "DiagnosticCode": "string"
                  },
                  "Complaint": { 
                     "ComplaintFeedbackType": "string",
                     "ComplaintSubType": "string"
                  }
               },
               "Timestamp": number,
               "Type": "string"
            }
         ],
         "Isp": "string"
      }
   ],
   "MessageId": "string",
   "Subject": "string"
}
```

## Response Elements
<a name="API_GetMessageInsights_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [EmailTags](#API_GetMessageInsights_ResponseSyntax) **   <a name="SES-GetMessageInsights-response-EmailTags"></a>
 A list of tags, in the form of name/value pairs, that were applied to the email you sent, along with Amazon SES [Auto-Tags](https://docs.aws.amazon.com/ses/latest/dg/monitor-using-event-publishing.html).   
Type: Array of [MessageTag](API_MessageTag.md) objects

 ** [FromEmailAddress](#API_GetMessageInsights_ResponseSyntax) **   <a name="SES-GetMessageInsights-response-FromEmailAddress"></a>
The from address used to send the message.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 320.

 ** [Insights](#API_GetMessageInsights_ResponseSyntax) **   <a name="SES-GetMessageInsights-response-Insights"></a>
A set of insights associated with the message.  
Type: Array of [EmailInsights](API_EmailInsights.md) objects

 ** [MessageId](#API_GetMessageInsights_ResponseSyntax) **   <a name="SES-GetMessageInsights-response-MessageId"></a>
A unique identifier for the message.  
Type: String

 ** [Subject](#API_GetMessageInsights_ResponseSyntax) **   <a name="SES-GetMessageInsights-response-Subject"></a>
The subject line of the message.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 998.

## Errors
<a name="API_GetMessageInsights_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** BadRequestException **   
The input you provided is invalid.  
HTTP Status Code: 400

 ** NotFoundException **   
The resource you attempted to access doesn't exist.  
HTTP Status Code: 404

 ** TooManyRequestsException **   
Too many requests have been made to the operation.  
HTTP Status Code: 429

## See Also
<a name="API_GetMessageInsights_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/sesv2-2019-09-27/GetMessageInsights) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/sesv2-2019-09-27/GetMessageInsights) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sesv2-2019-09-27/GetMessageInsights) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/sesv2-2019-09-27/GetMessageInsights) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sesv2-2019-09-27/GetMessageInsights) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/sesv2-2019-09-27/GetMessageInsights) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/sesv2-2019-09-27/GetMessageInsights) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/sesv2-2019-09-27/GetMessageInsights) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/sesv2-2019-09-27/GetMessageInsights) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sesv2-2019-09-27/GetMessageInsights) 