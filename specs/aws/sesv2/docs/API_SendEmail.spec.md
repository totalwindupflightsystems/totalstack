---
id: "@specs/aws/sesv2/docs/API_SendEmail"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS SendEmail"
status: active
depends_on:
  - "@specs/aws/sesv2/meta"
---

# SendEmail

> **source:** AWS Documentation
> **spec:id:** @specs/aws/sesv2/docs/API_SendEmail
> **target_lang:** meta — documentation tier. ALL sections preserved.



# SendEmail
<a name="API_SendEmail"></a>

Sends an email message. You can use the Amazon SES API v2 to send the following types of messages:
+  **Simple** – A standard email message. When you create this type of message, you specify the sender, the recipient, and the message body, and Amazon SES assembles the message for you.
+  **Raw** – A raw, MIME-formatted email message. When you send this type of email, you have to specify all of the message headers, as well as the message body. You can use this message type to send messages that contain attachments. The message that you specify has to be a valid MIME message.
+  **Templated** – A message that contains personalization tags. When you send this type of email, Amazon SES API v2 automatically replaces the tags with values that you specify.

## Request Syntax
<a name="API_SendEmail_RequestSyntax"></a>

```
POST /v2/email/outbound-emails HTTP/1.1
Content-type: application/json

{
   "ConfigurationSetName": "{{string}}",
   "Content": { 
      "Raw": { 
         "Data": {{blob}}
      },
      "Simple": { 
         "Attachments": [ 
            { 
               "ContentDescription": "{{string}}",
               "ContentDisposition": "{{string}}",
               "ContentId": "{{string}}",
               "ContentTransferEncoding": "{{string}}",
               "ContentType": "{{string}}",
               "FileName": "{{string}}",
               "RawContent": {{blob}}
            }
         ],
         "Body": { 
            "Html": { 
               "Charset": "{{string}}",
               "Data": "{{string}}"
            },
            "Text": { 
               "Charset": "{{string}}",
               "Data": "{{string}}"
            }
         },
         "Headers": [ 
            { 
               "Name": "{{string}}",
               "Value": "{{string}}"
            }
         ],
         "Subject": { 
            "Charset": "{{string}}",
            "Data": "{{string}}"
         }
      },
      "Template": { 
         "Attachments": [ 
            { 
               "ContentDescription": "{{string}}",
               "ContentDisposition": "{{string}}",
               "ContentId": "{{string}}",
               "ContentTransferEncoding": "{{string}}",
               "ContentType": "{{string}}",
               "FileName": "{{string}}",
               "RawContent": {{blob}}
            }
         ],
         "Headers": [ 
            { 
               "Name": "{{string}}",
               "Value": "{{string}}"
            }
         ],
         "TemplateArn": "{{string}}",
         "TemplateContent": { 
            "Html": "{{string}}",
            "Subject": "{{string}}",
            "Text": "{{string}}"
         },
         "TemplateData": "{{string}}",
         "TemplateName": "{{string}}"
      }
   },
   "Destination": { 
      "BccAddresses": [ "{{string}}" ],
      "CcAddresses": [ "{{string}}" ],
      "ToAddresses": [ "{{string}}" ]
   },
   "EmailTags": [ 
      { 
         "Name": "{{string}}",
         "Value": "{{string}}"
      }
   ],
   "EndpointId": "{{string}}",
   "FeedbackForwardingEmailAddress": "{{string}}",
   "FeedbackForwardingEmailAddressIdentityArn": "{{string}}",
   "FromEmailAddress": "{{string}}",
   "FromEmailAddressIdentityArn": "{{string}}",
   "ListManagementOptions": { 
      "ContactListName": "{{string}}",
      "TopicName": "{{string}}"
   },
   "ReplyToAddresses": [ "{{string}}" ],
   "TenantName": "{{string}}"
}
```

## URI Request Parameters
<a name="API_SendEmail_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_SendEmail_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [ConfigurationSetName](#API_SendEmail_RequestSyntax) **   <a name="SES-SendEmail-request-ConfigurationSetName"></a>
The name of the configuration set to use when sending the email.  
Type: String  
Required: No

 ** [Content](#API_SendEmail_RequestSyntax) **   <a name="SES-SendEmail-request-Content"></a>
An object that contains the body of the message. You can send either a Simple message, Raw message, or a Templated message.  
Type: [EmailContent](API_EmailContent.md) object  
Required: Yes

 ** [Destination](#API_SendEmail_RequestSyntax) **   <a name="SES-SendEmail-request-Destination"></a>
An object that contains the recipients of the email message.  
Type: [Destination](API_Destination.md) object  
Required: No

 ** [EmailTags](#API_SendEmail_RequestSyntax) **   <a name="SES-SendEmail-request-EmailTags"></a>
A list of tags, in the form of name/value pairs, to apply to an email that you send using the `SendEmail` operation. Tags correspond to characteristics of the email that you define, so that you can publish email sending events.   
Type: Array of [MessageTag](API_MessageTag.md) objects  
Required: No

 ** [EndpointId](#API_SendEmail_RequestSyntax) **   <a name="SES-SendEmail-request-EndpointId"></a>
The ID of the multi-region endpoint (global-endpoint).  
Type: String  
Required: No

 ** [FeedbackForwardingEmailAddress](#API_SendEmail_RequestSyntax) **   <a name="SES-SendEmail-request-FeedbackForwardingEmailAddress"></a>
The address that you want bounce and complaint notifications to be sent to.  
Type: String  
Required: No

 ** [FeedbackForwardingEmailAddressIdentityArn](#API_SendEmail_RequestSyntax) **   <a name="SES-SendEmail-request-FeedbackForwardingEmailAddressIdentityArn"></a>
This parameter is used only for sending authorization. It is the ARN of the identity that is associated with the sending authorization policy that permits you to use the email address specified in the `FeedbackForwardingEmailAddress` parameter.  
For example, if the owner of example.com (which has ARN arn:aws:ses:us-east-1:123456789012:identity/example.com) attaches a policy to it that authorizes you to use feedback@example.com, then you would specify the `FeedbackForwardingEmailAddressIdentityArn` to be arn:aws:ses:us-east-1:123456789012:identity/example.com, and the `FeedbackForwardingEmailAddress` to be feedback@example.com.  
For more information about sending authorization, see the [Amazon SES Developer Guide](https://docs.aws.amazon.com/ses/latest/DeveloperGuide/sending-authorization.html).  
Type: String  
Length Constraints: Minimum length of 1.  
Required: No

 ** [FromEmailAddress](#API_SendEmail_RequestSyntax) **   <a name="SES-SendEmail-request-FromEmailAddress"></a>
The email address to use as the "From" address for the email. The address that you specify has to be verified.   
Type: String  
Required: No

 ** [FromEmailAddressIdentityArn](#API_SendEmail_RequestSyntax) **   <a name="SES-SendEmail-request-FromEmailAddressIdentityArn"></a>
This parameter is used only for sending authorization. It is the ARN of the identity that is associated with the sending authorization policy that permits you to use the email address specified in the `FromEmailAddress` parameter.  
For example, if the owner of example.com (which has ARN arn:aws:ses:us-east-1:123456789012:identity/example.com) attaches a policy to it that authorizes you to use sender@example.com, then you would specify the `FromEmailAddressIdentityArn` to be arn:aws:ses:us-east-1:123456789012:identity/example.com, and the `FromEmailAddress` to be sender@example.com.  
For more information about sending authorization, see the [Amazon SES Developer Guide](https://docs.aws.amazon.com/ses/latest/DeveloperGuide/sending-authorization.html).  
For Raw emails, the `FromEmailAddressIdentityArn` value overrides the X-SES-SOURCE-ARN and X-SES-FROM-ARN headers specified in raw email message content.  
Type: String  
Length Constraints: Minimum length of 1.  
Required: No

 ** [ListManagementOptions](#API_SendEmail_RequestSyntax) **   <a name="SES-SendEmail-request-ListManagementOptions"></a>
An object used to specify a list or topic to which an email belongs, which will be used when a contact chooses to unsubscribe.  
Type: [ListManagementOptions](API_ListManagementOptions.md) object  
Required: No

 ** [ReplyToAddresses](#API_SendEmail_RequestSyntax) **   <a name="SES-SendEmail-request-ReplyToAddresses"></a>
The "Reply-to" email addresses for the message. When the recipient replies to the message, each Reply-to address receives the reply.  
Type: Array of strings  
Required: No

 ** [TenantName](#API_SendEmail_RequestSyntax) **   <a name="SES-SendEmail-request-TenantName"></a>
The name of the tenant through which this email will be sent.  
The email sending operation will only succeed if all referenced resources (identities, configuration sets, and templates) are associated with this tenant. 
Type: String  
Length Constraints: Minimum length of 1.  
Required: No

## Response Syntax
<a name="API_SendEmail_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "MessageId": "string"
}
```

## Response Elements
<a name="API_SendEmail_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [MessageId](#API_SendEmail_ResponseSyntax) **   <a name="SES-SendEmail-response-MessageId"></a>
A unique identifier for the message that is generated when the message is accepted.  
It's possible for Amazon SES to accept a message without sending it. For example, this can happen when the message that you're trying to send has an attachment that contains a virus, or when you send a templated email that contains invalid personalization content.
Type: String

## Errors
<a name="API_SendEmail_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccountSuspendedException **   
The message can't be sent because the account's ability to send email has been permanently restricted.  
HTTP Status Code: 400

 ** BadRequestException **   
The input you provided is invalid.  
HTTP Status Code: 400

 ** LimitExceededException **   
There are too many instances of the specified resource type.  
HTTP Status Code: 400

 ** MailFromDomainNotVerifiedException **   
The message can't be sent because the sending domain isn't verified.  
HTTP Status Code: 400

 ** MessageRejected **   
The message can't be sent because it contains invalid content.  
HTTP Status Code: 400

 ** NotFoundException **   
The resource you attempted to access doesn't exist.  
HTTP Status Code: 404

 ** SendingPausedException **   
The message can't be sent because the account's ability to send email is currently paused.  
HTTP Status Code: 400

 ** TooManyRequestsException **   
Too many requests have been made to the operation.  
HTTP Status Code: 429

## See Also
<a name="API_SendEmail_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/sesv2-2019-09-27/SendEmail) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/sesv2-2019-09-27/SendEmail) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sesv2-2019-09-27/SendEmail) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/sesv2-2019-09-27/SendEmail) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sesv2-2019-09-27/SendEmail) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/sesv2-2019-09-27/SendEmail) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/sesv2-2019-09-27/SendEmail) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/sesv2-2019-09-27/SendEmail) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/sesv2-2019-09-27/SendEmail) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sesv2-2019-09-27/SendEmail) 