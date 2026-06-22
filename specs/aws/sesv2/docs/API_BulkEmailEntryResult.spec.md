---
id: "@specs/aws/sesv2/docs/API_BulkEmailEntryResult"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS BulkEmailEntryResult"
status: active
depends_on:
  - "@specs/aws/sesv2/meta"
---

# BulkEmailEntryResult

> **source:** AWS Documentation
> **spec:id:** @specs/aws/sesv2/docs/API_BulkEmailEntryResult
> **target_lang:** meta — documentation tier. ALL sections preserved.



# BulkEmailEntryResult
<a name="API_BulkEmailEntryResult"></a>

The result of the `SendBulkEmail` operation of each specified `BulkEmailEntry`.

## Contents
<a name="API_BulkEmailEntryResult_Contents"></a>

 ** Error **   <a name="SES-Type-BulkEmailEntryResult-Error"></a>
A description of an error that prevented a message being sent using the `SendBulkTemplatedEmail` operation.  
Type: String  
Required: No

 ** MessageId **   <a name="SES-Type-BulkEmailEntryResult-MessageId"></a>
The unique message identifier returned from the `SendBulkTemplatedEmail` operation.  
Type: String  
Required: No

 ** Status **   <a name="SES-Type-BulkEmailEntryResult-Status"></a>
The status of a message sent using the `SendBulkTemplatedEmail` operation.  
Possible values for this parameter include:  
+ SUCCESS: Amazon SES accepted the message, and will attempt to deliver it to the recipients.
+ MESSAGE\_REJECTED: The message was rejected because it contained a virus.
+ MAIL\_FROM\_DOMAIN\_NOT\_VERIFIED: The sender's email address or domain was not verified.
+ CONFIGURATION\_SET\_DOES\_NOT\_EXIST: The configuration set you specified does not exist.
+ TEMPLATE\_DOES\_NOT\_EXIST: The template you specified does not exist.
+ ACCOUNT\_SUSPENDED: Your account has been shut down because of issues related to your email sending practices.
+ ACCOUNT\_THROTTLED: The number of emails you can send has been reduced because your account has exceeded its allocated sending limit.
+ ACCOUNT\_DAILY\_QUOTA\_EXCEEDED: You have reached or exceeded the maximum number of emails you can send from your account in a 24-hour period.
+ INVALID\_SENDING\_POOL\_NAME: The configuration set you specified refers to an IP pool that does not exist.
+ ACCOUNT\_SENDING\_PAUSED: Email sending for the Amazon SES account was disabled using the [UpdateAccountSendingEnabled](https://docs.aws.amazon.com/ses/latest/APIReference/API_UpdateAccountSendingEnabled.html) operation.
+ CONFIGURATION\_SET\_SENDING\_PAUSED: Email sending for this configuration set was disabled using the [UpdateConfigurationSetSendingEnabled](https://docs.aws.amazon.com/ses/latest/APIReference/API_UpdateConfigurationSetSendingEnabled.html) operation.
+ INVALID\_PARAMETER\_VALUE: One or more of the parameters you specified when calling this operation was invalid. See the error message for additional information.
+ TRANSIENT\_FAILURE: Amazon SES was unable to process your request because of a temporary issue.
+ FAILED: Amazon SES was unable to process your request. See the error message for additional information.
Type: String  
Valid Values: `SUCCESS | MESSAGE_REJECTED | MAIL_FROM_DOMAIN_NOT_VERIFIED | CONFIGURATION_SET_NOT_FOUND | TEMPLATE_NOT_FOUND | ACCOUNT_SUSPENDED | ACCOUNT_THROTTLED | ACCOUNT_DAILY_QUOTA_EXCEEDED | INVALID_SENDING_POOL_NAME | ACCOUNT_SENDING_PAUSED | CONFIGURATION_SET_SENDING_PAUSED | INVALID_PARAMETER | TRANSIENT_FAILURE | FAILED`   
Required: No

## See Also
<a name="API_BulkEmailEntryResult_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sesv2-2019-09-27/BulkEmailEntryResult) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sesv2-2019-09-27/BulkEmailEntryResult) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sesv2-2019-09-27/BulkEmailEntryResult) 