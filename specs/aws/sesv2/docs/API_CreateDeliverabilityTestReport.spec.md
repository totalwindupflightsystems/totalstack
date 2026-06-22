---
id: "@specs/aws/sesv2/docs/API_CreateDeliverabilityTestReport"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS CreateDeliverabilityTestReport"
status: active
depends_on:
  - "@specs/aws/sesv2/meta"
---

# CreateDeliverabilityTestReport

> **source:** AWS Documentation
> **spec:id:** @specs/aws/sesv2/docs/API_CreateDeliverabilityTestReport
> **target_lang:** meta — documentation tier. ALL sections preserved.



# CreateDeliverabilityTestReport
<a name="API_CreateDeliverabilityTestReport"></a>

Create a new predictive inbox placement test. Predictive inbox placement tests can help you predict how your messages will be handled by various email providers around the world. When you perform a predictive inbox placement test, you provide a sample message that contains the content that you plan to send to your customers. Amazon SES then sends that message to special email addresses spread across several major email providers. After about 24 hours, the test is complete, and you can use the `GetDeliverabilityTestReport` operation to view the results of the test.

## Request Syntax
<a name="API_CreateDeliverabilityTestReport_RequestSyntax"></a>

```
POST /v2/email/deliverability-dashboard/test HTTP/1.1
Content-type: application/json

{
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
   "FromEmailAddress": "{{string}}",
   "ReportName": "{{string}}",
   "Tags": [ 
      { 
         "Key": "{{string}}",
         "Value": "{{string}}"
      }
   ]
}
```

## URI Request Parameters
<a name="API_CreateDeliverabilityTestReport_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_CreateDeliverabilityTestReport_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [Content](#API_CreateDeliverabilityTestReport_RequestSyntax) **   <a name="SES-CreateDeliverabilityTestReport-request-Content"></a>
The HTML body of the message that you sent when you performed the predictive inbox placement test.  
Type: [EmailContent](API_EmailContent.md) object  
Required: Yes

 ** [FromEmailAddress](#API_CreateDeliverabilityTestReport_RequestSyntax) **   <a name="SES-CreateDeliverabilityTestReport-request-FromEmailAddress"></a>
The email address that the predictive inbox placement test email was sent from.  
Type: String  
Required: Yes

 ** [ReportName](#API_CreateDeliverabilityTestReport_RequestSyntax) **   <a name="SES-CreateDeliverabilityTestReport-request-ReportName"></a>
A unique name that helps you to identify the predictive inbox placement test when you retrieve the results.  
Type: String  
Required: No

 ** [Tags](#API_CreateDeliverabilityTestReport_RequestSyntax) **   <a name="SES-CreateDeliverabilityTestReport-request-Tags"></a>
An array of objects that define the tags (keys and values) that you want to associate with the predictive inbox placement test.  
Type: Array of [Tag](API_Tag.md) objects  
Required: No

## Response Syntax
<a name="API_CreateDeliverabilityTestReport_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "DeliverabilityTestStatus": "string",
   "ReportId": "string"
}
```

## Response Elements
<a name="API_CreateDeliverabilityTestReport_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [DeliverabilityTestStatus](#API_CreateDeliverabilityTestReport_ResponseSyntax) **   <a name="SES-CreateDeliverabilityTestReport-response-DeliverabilityTestStatus"></a>
The status of the predictive inbox placement test. If the status is `IN_PROGRESS`, then the predictive inbox placement test is currently running. Predictive inbox placement tests are usually complete within 24 hours of creating the test. If the status is `COMPLETE`, then the test is finished, and you can use the `GetDeliverabilityTestReport` to view the results of the test.  
Type: String  
Valid Values: `IN_PROGRESS | COMPLETED` 

 ** [ReportId](#API_CreateDeliverabilityTestReport_ResponseSyntax) **   <a name="SES-CreateDeliverabilityTestReport-response-ReportId"></a>
A unique string that identifies the predictive inbox placement test.  
Type: String

## Errors
<a name="API_CreateDeliverabilityTestReport_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccountSuspendedException **   
The message can't be sent because the account's ability to send email has been permanently restricted.  
HTTP Status Code: 400

 ** BadRequestException **   
The input you provided is invalid.  
HTTP Status Code: 400

 ** ConcurrentModificationException **   
The resource is being modified by another operation or thread.  
HTTP Status Code: 500

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
<a name="API_CreateDeliverabilityTestReport_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/sesv2-2019-09-27/CreateDeliverabilityTestReport) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/sesv2-2019-09-27/CreateDeliverabilityTestReport) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sesv2-2019-09-27/CreateDeliverabilityTestReport) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/sesv2-2019-09-27/CreateDeliverabilityTestReport) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sesv2-2019-09-27/CreateDeliverabilityTestReport) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/sesv2-2019-09-27/CreateDeliverabilityTestReport) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/sesv2-2019-09-27/CreateDeliverabilityTestReport) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/sesv2-2019-09-27/CreateDeliverabilityTestReport) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/sesv2-2019-09-27/CreateDeliverabilityTestReport) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sesv2-2019-09-27/CreateDeliverabilityTestReport) 