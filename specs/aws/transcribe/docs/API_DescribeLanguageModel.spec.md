---
id: "@specs/aws/transcribe/docs/API_DescribeLanguageModel"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS DescribeLanguageModel"
status: active
depends_on:
  - "@specs/aws/transcribe/meta"
---

# DescribeLanguageModel

> **source:** AWS Documentation
> **spec:id:** @specs/aws/transcribe/docs/API_DescribeLanguageModel
> **target_lang:** meta — documentation tier. ALL sections preserved.



# DescribeLanguageModel
<a name="API_DescribeLanguageModel"></a>

Provides information about the specified custom language model.

This operation also shows if the base language model that you used to create your custom language model has been updated. If Amazon Transcribe has updated the base model, you can create a new custom language model using the updated base model.

If you tried to create a new custom language model and the request wasn't successful, you can use `DescribeLanguageModel` to help identify the reason for this failure.

To get a list of your custom language models, use the [ListLanguageModels](API_ListLanguageModels.md) operation.

## Request Syntax
<a name="API_DescribeLanguageModel_RequestSyntax"></a>

```
{
   "ModelName": "{{string}}"
}
```

## Request Parameters
<a name="API_DescribeLanguageModel_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [ModelName](#API_DescribeLanguageModel_RequestSyntax) **   <a name="transcribe-DescribeLanguageModel-request-ModelName"></a>
The name of the custom language model you want information about. Model names are case sensitive.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 200.  
Pattern: `^[0-9a-zA-Z._-]+`   
Required: Yes

## Response Syntax
<a name="API_DescribeLanguageModel_ResponseSyntax"></a>

```
{
   "LanguageModel": { 
      "BaseModelName": "string",
      "CreateTime": number,
      "FailureReason": "string",
      "InputDataConfig": { 
         "DataAccessRoleArn": "string",
         "S3Uri": "string",
         "TuningDataS3Uri": "string"
      },
      "LanguageCode": "string",
      "LastModifiedTime": number,
      "ModelName": "string",
      "ModelStatus": "string",
      "UpgradeAvailability": boolean
   }
}
```

## Response Elements
<a name="API_DescribeLanguageModel_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [LanguageModel](#API_DescribeLanguageModel_ResponseSyntax) **   <a name="transcribe-DescribeLanguageModel-response-LanguageModel"></a>
Provides information about the specified custom language model.  
This parameter also shows if the base language model you used to create your custom language model has been updated. If Amazon Transcribe has updated the base model, you can create a new custom language model using the updated base model.  
If you tried to create a new custom language model and the request wasn't successful, you can use this `DescribeLanguageModel` to help identify the reason for this failure.  
Type: [LanguageModel](API_LanguageModel.md) object

## Errors
<a name="API_DescribeLanguageModel_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** BadRequestException **   
Your request didn't pass one or more validation tests. This can occur when the entity you're trying to delete doesn't exist or if it's in a non-terminal state (such as `IN PROGRESS`). See the exception message field for more information.  
HTTP Status Code: 400

 ** InternalFailureException **   
There was an internal error. Check the error message, correct the issue, and try your request again.  
HTTP Status Code: 500

 ** LimitExceededException **   
You've either sent too many requests or your input file is too long. Wait before retrying your request, or use a smaller file and try your request again.  
HTTP Status Code: 400

 ** NotFoundException **   
We can't find the requested resource. Check that the specified name is correct and try your request again.  
HTTP Status Code: 400

## See Also
<a name="API_DescribeLanguageModel_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/transcribe-2017-10-26/DescribeLanguageModel) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/transcribe-2017-10-26/DescribeLanguageModel) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/transcribe-2017-10-26/DescribeLanguageModel) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/transcribe-2017-10-26/DescribeLanguageModel) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/transcribe-2017-10-26/DescribeLanguageModel) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/transcribe-2017-10-26/DescribeLanguageModel) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/transcribe-2017-10-26/DescribeLanguageModel) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/transcribe-2017-10-26/DescribeLanguageModel) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/transcribe-2017-10-26/DescribeLanguageModel) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/transcribe-2017-10-26/DescribeLanguageModel) 