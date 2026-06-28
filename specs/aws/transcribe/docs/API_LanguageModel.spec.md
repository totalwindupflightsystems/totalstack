---
id: "@specs/aws/transcribe/docs/API_LanguageModel"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS LanguageModel"
status: active
depends_on:
  - "@specs/aws/transcribe/meta"
---

# LanguageModel

> **source:** AWS Documentation
> **spec:id:** @specs/aws/transcribe/docs/API_LanguageModel
> **target_lang:** meta — documentation tier. ALL sections preserved.



# LanguageModel
<a name="API_LanguageModel"></a>

Provides information about a custom language model, including:
+ The base model name
+ When the model was created
+ The location of the files used to train the model
+ When the model was last modified
+ The name you chose for the model
+ The model's language
+ The model's processing state
+ Any available upgrades for the base model

## Contents
<a name="API_LanguageModel_Contents"></a>

 ** BaseModelName **   <a name="transcribe-Type-LanguageModel-BaseModelName"></a>
The Amazon Transcribe standard language model, or base model, used to create your custom language model.  
Type: String  
Valid Values: `NarrowBand | WideBand`   
Required: No

 ** CreateTime **   <a name="transcribe-Type-LanguageModel-CreateTime"></a>
The date and time the specified custom language model was created.  
Timestamps are in the format `YYYY-MM-DD'T'HH:MM:SS.SSSSSS-UTC`. For example, `2022-05-04T12:32:58.761000-07:00` represents 12:32 PM UTC-7 on May 4, 2022.  
Type: Timestamp  
Required: No

 ** FailureReason **   <a name="transcribe-Type-LanguageModel-FailureReason"></a>
If `ModelStatus` is `FAILED`, `FailureReason` contains information about why the custom language model request failed. See also: [Common Errors](https://docs.aws.amazon.com/transcribe/latest/APIReference/CommonErrors.html).  
Type: String  
Required: No

 ** InputDataConfig **   <a name="transcribe-Type-LanguageModel-InputDataConfig"></a>
The Amazon S3 location of the input files used to train and tune your custom language model, in addition to the data access role ARN (Amazon Resource Name) that has permissions to access these data.  
Type: [InputDataConfig](API_InputDataConfig.md) object  
Required: No

 ** LanguageCode **   <a name="transcribe-Type-LanguageModel-LanguageCode"></a>
The language code used to create your custom language model. Each custom language model must contain terms in only one language, and the language you select for your custom language model must match the language of your training and tuning data.  
For a list of supported languages and their associated language codes, refer to the [Supported languages](https://docs.aws.amazon.com/transcribe/latest/dg/supported-languages.html) table. Note that US English (`en-US`) is the only language supported with Amazon Transcribe Medical.  
Type: String  
Valid Values: `en-US | hi-IN | es-US | en-GB | en-AU | de-DE | ja-JP`   
Required: No

 ** LastModifiedTime **   <a name="transcribe-Type-LanguageModel-LastModifiedTime"></a>
The date and time the specified custom language model was last modified.  
Timestamps are in the format `YYYY-MM-DD'T'HH:MM:SS.SSSSSS-UTC`. For example, `2022-05-04T12:32:58.761000-07:00` represents 12:32 PM UTC-7 on May 4, 2022.  
Type: Timestamp  
Required: No

 ** ModelName **   <a name="transcribe-Type-LanguageModel-ModelName"></a>
A unique name, chosen by you, for your custom language model.  
This name is case sensitive, cannot contain spaces, and must be unique within an AWS account.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 200.  
Pattern: `^[0-9a-zA-Z._-]+`   
Required: No

 ** ModelStatus **   <a name="transcribe-Type-LanguageModel-ModelStatus"></a>
The status of the specified custom language model. When the status displays as `COMPLETED` the model is ready for use.  
Type: String  
Valid Values: `IN_PROGRESS | FAILED | COMPLETED`   
Required: No

 ** UpgradeAvailability **   <a name="transcribe-Type-LanguageModel-UpgradeAvailability"></a>
Shows if a more current base model is available for use with the specified custom language model.  
If `false`, your custom language model is using the most up-to-date base model.  
If `true`, there is a newer base model available than the one your language model is using.  
Note that to update a base model, you must recreate the custom language model using the new base model. Base model upgrades for existing custom language models are not supported.  
Type: Boolean  
Required: No

## See Also
<a name="API_LanguageModel_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/transcribe-2017-10-26/LanguageModel) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/transcribe-2017-10-26/LanguageModel) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/transcribe-2017-10-26/LanguageModel) 