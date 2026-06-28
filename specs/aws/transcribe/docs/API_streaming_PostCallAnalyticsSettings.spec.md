---
id: "@specs/aws/transcribe/docs/API_streaming_PostCallAnalyticsSettings"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS PostCallAnalyticsSettings"
status: active
depends_on:
  - "@specs/aws/transcribe/meta"
---

# PostCallAnalyticsSettings

> **source:** AWS Documentation
> **spec:id:** @specs/aws/transcribe/docs/API_streaming_PostCallAnalyticsSettings
> **target_lang:** meta — documentation tier. ALL sections preserved.



# PostCallAnalyticsSettings
<a name="API_streaming_PostCallAnalyticsSettings"></a>

Allows you to specify additional settings for your Call Analytics post-call request, including output locations for your redacted transcript, which IAM role to use, and which encryption key to use.

 `DataAccessRoleArn` and `OutputLocation` are required fields.

 `PostCallAnalyticsSettings` provides you with the same insights as a Call Analytics post-call transcription. Refer to [Post-call analytics](https://docs.aws.amazon.com/transcribe/latest/dg/tca-post-call.html) for more information on this feature.

## Contents
<a name="API_streaming_PostCallAnalyticsSettings_Contents"></a>

 ** DataAccessRoleArn **   <a name="transcribe-Type-streaming_PostCallAnalyticsSettings-DataAccessRoleArn"></a>
The Amazon Resource Name (ARN) of an IAM role that has permissions to access the Amazon S3 bucket that contains your input files. If the role that you specify doesn’t have the appropriate permissions to access the specified Amazon S3 location, your request fails.  
IAM role ARNs have the format `arn:partition:iam::account:role/role-name-with-path`. For example: `arn:aws:iam::111122223333:role/Admin`. For more information, see [IAM ARNs](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_identifiers.html#identifiers-arns).  
Type: String  
Required: Yes

 ** OutputLocation **   <a name="transcribe-Type-streaming_PostCallAnalyticsSettings-OutputLocation"></a>
The Amazon S3 location where you want your Call Analytics post-call transcription output stored. You can use any of the following formats to specify the output location:  

1. s3://DOC-EXAMPLE-BUCKET

1. s3://DOC-EXAMPLE-BUCKET/my-output-folder/

1. s3://DOC-EXAMPLE-BUCKET/my-output-folder/my-call-analytics-job.json
Type: String  
Required: Yes

 ** ContentRedactionOutput **   <a name="transcribe-Type-streaming_PostCallAnalyticsSettings-ContentRedactionOutput"></a>
Specify whether you want only a redacted transcript or both a redacted and an unredacted transcript. If you choose redacted and unredacted, two JSON files are generated and stored in the Amazon S3 output location you specify.  
Note that to include `ContentRedactionOutput` in your request, you must enable content redaction (`ContentRedactionType`).  
Type: String  
Valid Values: `redacted | redacted_and_unredacted`   
Required: No

 ** OutputEncryptionKMSKeyId **   <a name="transcribe-Type-streaming_PostCallAnalyticsSettings-OutputEncryptionKMSKeyId"></a>
The KMS key you want to use to encrypt your Call Analytics post-call output.  
If using a key located in the **current** AWS account, you can specify your KMS key in one of four ways:  

1. Use the KMS key ID itself. For example, `1234abcd-12ab-34cd-56ef-1234567890ab`.

1. Use an alias for the KMS key ID. For example, `alias/ExampleAlias`.

1. Use the Amazon Resource Name (ARN) for the KMS key ID. For example, `arn:aws:kms:region:account-ID:key/1234abcd-12ab-34cd-56ef-1234567890ab`.

1. Use the ARN for the KMS key alias. For example, `arn:aws:kms:region:account-ID:alias/ExampleAlias`.
If using a key located in a **different** AWS account than the current AWS account, you can specify your KMS key in one of two ways:  

1. Use the ARN for the KMS key ID. For example, `arn:aws:kms:region:account-ID:key/1234abcd-12ab-34cd-56ef-1234567890ab`.

1. Use the ARN for the KMS key alias. For example, `arn:aws:kms:region:account-ID:alias/ExampleAlias`.
Note that the role making the [StartCallAnalyticsStreamTranscription](API_streaming_StartCallAnalyticsStreamTranscription.md) request must have permission to use the specified KMS key.  
Type: String  
Required: No

## See Also
<a name="API_streaming_PostCallAnalyticsSettings_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/transcribe-streaming-2017-10-26/PostCallAnalyticsSettings) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/transcribe-streaming-2017-10-26/PostCallAnalyticsSettings) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/transcribe-streaming-2017-10-26/PostCallAnalyticsSettings) 