---
id: "@specs/aws/transcribe/docs/API_ListTagsForResource"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS ListTagsForResource"
status: active
depends_on:
  - "@specs/aws/transcribe/meta"
---

# ListTagsForResource

> **source:** AWS Documentation
> **spec:id:** @specs/aws/transcribe/docs/API_ListTagsForResource
> **target_lang:** meta — documentation tier. ALL sections preserved.



# ListTagsForResource
<a name="API_ListTagsForResource"></a>

Lists all tags associated with the specified transcription job, vocabulary, model, or resource.

To learn more about using tags with Amazon Transcribe, refer to [Tagging resources](https://docs.aws.amazon.com/transcribe/latest/dg/tagging.html).

## Request Syntax
<a name="API_ListTagsForResource_RequestSyntax"></a>

```
{
   "ResourceArn": "{{string}}"
}
```

## Request Parameters
<a name="API_ListTagsForResource_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [ResourceArn](#API_ListTagsForResource_RequestSyntax) **   <a name="transcribe-ListTagsForResource-request-ResourceArn"></a>
Returns a list of all tags associated with the specified Amazon Resource Name (ARN). ARNs have the format `arn:partition:service:region:account-id:resource-type/resource-id`.  
For example, `arn:aws:transcribe:us-west-2:111122223333:transcription-job/transcription-job-name`.  
Valid values for `resource-type` are: `transcription-job`, `medical-transcription-job`, `vocabulary`, `medical-vocabulary`, `vocabulary-filter`, and `language-model`.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 1011.  
Pattern: `arn:aws(-[^:]+)?:transcribe:[a-zA-Z0-9-]*:[0-9]{12}:[a-zA-Z-]*/[0-9a-zA-Z._-]+`   
Required: Yes

## Response Syntax
<a name="API_ListTagsForResource_ResponseSyntax"></a>

```
{
   "ResourceArn": "string",
   "Tags": [ 
      { 
         "Key": "string",
         "Value": "string"
      }
   ]
}
```

## Response Elements
<a name="API_ListTagsForResource_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ResourceArn](#API_ListTagsForResource_ResponseSyntax) **   <a name="transcribe-ListTagsForResource-response-ResourceArn"></a>
The Amazon Resource Name (ARN) specified in your request.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 1011.  
Pattern: `arn:aws(-[^:]+)?:transcribe:[a-zA-Z0-9-]*:[0-9]{12}:[a-zA-Z-]*/[0-9a-zA-Z._-]+` 

 ** [Tags](#API_ListTagsForResource_ResponseSyntax) **   <a name="transcribe-ListTagsForResource-response-Tags"></a>
Lists all tags associated with the given transcription job, vocabulary, model, or resource.  
Type: Array of [Tag](API_Tag.md) objects  
Array Members: Minimum number of 1 item. Maximum number of 200 items.

## Errors
<a name="API_ListTagsForResource_Errors"></a>

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
<a name="API_ListTagsForResource_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/transcribe-2017-10-26/ListTagsForResource) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/transcribe-2017-10-26/ListTagsForResource) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/transcribe-2017-10-26/ListTagsForResource) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/transcribe-2017-10-26/ListTagsForResource) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/transcribe-2017-10-26/ListTagsForResource) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/transcribe-2017-10-26/ListTagsForResource) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/transcribe-2017-10-26/ListTagsForResource) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/transcribe-2017-10-26/ListTagsForResource) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/transcribe-2017-10-26/ListTagsForResource) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/transcribe-2017-10-26/ListTagsForResource) 