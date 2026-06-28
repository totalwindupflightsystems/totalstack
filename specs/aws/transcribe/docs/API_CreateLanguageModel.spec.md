---
id: "@specs/aws/transcribe/docs/API_CreateLanguageModel"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS CreateLanguageModel"
status: active
depends_on:
  - "@specs/aws/transcribe/meta"
---

# CreateLanguageModel

> **source:** AWS Documentation
> **spec:id:** @specs/aws/transcribe/docs/API_CreateLanguageModel
> **target_lang:** meta — documentation tier. ALL sections preserved.



# CreateLanguageModel
<a name="API_CreateLanguageModel"></a>

Creates a new custom language model.

When creating a new custom language model, you must specify:
+ If you want a Wideband (audio sample rates over 16,000 Hz) or Narrowband (audio sample rates under 16,000 Hz) base model
+ The location of your training and tuning files (this must be an Amazon S3 URI)
+ The language of your model
+ A unique name for your model

For more information, see [Custom language models](https://docs.aws.amazon.com/transcribe/latest/dg/custom-language-models.html).

## Request Syntax
<a name="API_CreateLanguageModel_RequestSyntax"></a>

```
{
   "BaseModelName": "{{string}}",
   "InputDataConfig": { 
      "DataAccessRoleArn": "{{string}}",
      "S3Uri": "{{string}}",
      "TuningDataS3Uri": "{{string}}"
   },
   "LanguageCode": "{{string}}",
   "ModelName": "{{string}}",
   "Tags": [ 
      { 
         "Key": "{{string}}",
         "Value": "{{string}}"
      }
   ]
}
```

## Request Parameters
<a name="API_CreateLanguageModel_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [BaseModelName](#API_CreateLanguageModel_RequestSyntax) **   <a name="transcribe-CreateLanguageModel-request-BaseModelName"></a>
The Amazon Transcribe standard language model, or base model, used to create your custom language model. Amazon Transcribe offers two options for base models: Wideband and Narrowband.  
If the audio you want to transcribe has a sample rate of 16,000 Hz or greater, choose `WideBand`. To transcribe audio with a sample rate less than 16,000 Hz, choose `NarrowBand`.  
Type: String  
Valid Values: `NarrowBand | WideBand`   
Required: Yes

 ** [InputDataConfig](#API_CreateLanguageModel_RequestSyntax) **   <a name="transcribe-CreateLanguageModel-request-InputDataConfig"></a>
Contains the Amazon S3 location of the training data you want to use to create a new custom language model, and permissions to access this location.  
When using `InputDataConfig`, you must include these sub-parameters: `S3Uri`, which is the Amazon S3 location of your training data, and `DataAccessRoleArn`, which is the Amazon Resource Name (ARN) of the role that has permission to access your specified Amazon S3 location. You can optionally include `TuningDataS3Uri`, which is the Amazon S3 location of your tuning data. If you specify different Amazon S3 locations for training and tuning data, the ARN you use must have permissions to access both locations.  
Type: [InputDataConfig](API_InputDataConfig.md) object  
Required: Yes

 ** [LanguageCode](#API_CreateLanguageModel_RequestSyntax) **   <a name="transcribe-CreateLanguageModel-request-LanguageCode"></a>
The language code that represents the language of your model. Each custom language model must contain terms in only one language, and the language you select for your custom language model must match the language of your training and tuning data.  
For a list of supported languages and their associated language codes, refer to the [Supported languages](https://docs.aws.amazon.com/transcribe/latest/dg/supported-languages.html) table. Note that US English (`en-US`) is the only language supported with Amazon Transcribe Medical.  
A custom language model can only be used to transcribe files in the same language as the model. For example, if you create a custom language model using US English (`en-US`), you can only apply this model to files that contain English audio.  
Type: String  
Valid Values: `en-US | hi-IN | es-US | en-GB | en-AU | de-DE | ja-JP`   
Required: Yes

 ** [ModelName](#API_CreateLanguageModel_RequestSyntax) **   <a name="transcribe-CreateLanguageModel-request-ModelName"></a>
A unique name, chosen by you, for your custom language model.  
This name is case sensitive, cannot contain spaces, and must be unique within an AWS account. If you try to create a new custom language model with the same name as an existing custom language model, you get a `ConflictException` error.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 200.  
Pattern: `^[0-9a-zA-Z._-]+`   
Required: Yes

 ** [Tags](#API_CreateLanguageModel_RequestSyntax) **   <a name="transcribe-CreateLanguageModel-request-Tags"></a>
Adds one or more custom tags, each in the form of a key:value pair, to a new custom language model at the time you create this new model.  
To learn more about using tags with Amazon Transcribe, refer to [Tagging resources](https://docs.aws.amazon.com/transcribe/latest/dg/tagging.html).  
Type: Array of [Tag](API_Tag.md) objects  
Array Members: Minimum number of 1 item. Maximum number of 200 items.  
Required: No

## Response Syntax
<a name="API_CreateLanguageModel_ResponseSyntax"></a>

```
{
   "BaseModelName": "string",
   "InputDataConfig": { 
      "DataAccessRoleArn": "string",
      "S3Uri": "string",
      "TuningDataS3Uri": "string"
   },
   "LanguageCode": "string",
   "ModelName": "string",
   "ModelStatus": "string"
}
```

## Response Elements
<a name="API_CreateLanguageModel_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [BaseModelName](#API_CreateLanguageModel_ResponseSyntax) **   <a name="transcribe-CreateLanguageModel-response-BaseModelName"></a>
The Amazon Transcribe standard language model, or base model, you specified when creating your custom language model.  
Type: String  
Valid Values: `NarrowBand | WideBand` 

 ** [InputDataConfig](#API_CreateLanguageModel_ResponseSyntax) **   <a name="transcribe-CreateLanguageModel-response-InputDataConfig"></a>
Lists your data access role ARN (Amazon Resource Name) and the Amazon S3 locations you provided for your training (`S3Uri`) and tuning (`TuningDataS3Uri`) data.  
Type: [InputDataConfig](API_InputDataConfig.md) object

 ** [LanguageCode](#API_CreateLanguageModel_ResponseSyntax) **   <a name="transcribe-CreateLanguageModel-response-LanguageCode"></a>
The language code you selected for your custom language model.  
Type: String  
Valid Values: `en-US | hi-IN | es-US | en-GB | en-AU | de-DE | ja-JP` 

 ** [ModelName](#API_CreateLanguageModel_ResponseSyntax) **   <a name="transcribe-CreateLanguageModel-response-ModelName"></a>
The name of your custom language model.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 200.  
Pattern: `^[0-9a-zA-Z._-]+` 

 ** [ModelStatus](#API_CreateLanguageModel_ResponseSyntax) **   <a name="transcribe-CreateLanguageModel-response-ModelStatus"></a>
The status of your custom language model. When the status displays as `COMPLETED`, your model is ready to use.  
Type: String  
Valid Values: `IN_PROGRESS | FAILED | COMPLETED` 

## Errors
<a name="API_CreateLanguageModel_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** BadRequestException **   
Your request didn't pass one or more validation tests. This can occur when the entity you're trying to delete doesn't exist or if it's in a non-terminal state (such as `IN PROGRESS`). See the exception message field for more information.  
HTTP Status Code: 400

 ** ConflictException **   
A resource already exists with this name. Resource names must be unique within an AWS account.  
HTTP Status Code: 400

 ** InternalFailureException **   
There was an internal error. Check the error message, correct the issue, and try your request again.  
HTTP Status Code: 500

 ** LimitExceededException **   
You've either sent too many requests or your input file is too long. Wait before retrying your request, or use a smaller file and try your request again.  
HTTP Status Code: 400

## See Also
<a name="API_CreateLanguageModel_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/transcribe-2017-10-26/CreateLanguageModel) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/transcribe-2017-10-26/CreateLanguageModel) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/transcribe-2017-10-26/CreateLanguageModel) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/transcribe-2017-10-26/CreateLanguageModel) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/transcribe-2017-10-26/CreateLanguageModel) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/transcribe-2017-10-26/CreateLanguageModel) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/transcribe-2017-10-26/CreateLanguageModel) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/transcribe-2017-10-26/CreateLanguageModel) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/transcribe-2017-10-26/CreateLanguageModel) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/transcribe-2017-10-26/CreateLanguageModel) 