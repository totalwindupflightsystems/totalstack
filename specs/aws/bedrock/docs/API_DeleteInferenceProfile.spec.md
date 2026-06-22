---
id: "@specs/aws/bedrock/docs/API_DeleteInferenceProfile"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS DeleteInferenceProfile"
status: active
depends_on:
  - "@specs/aws/bedrock/meta"
---

# DeleteInferenceProfile

> **source:** AWS Documentation
> **spec:id:** @specs/aws/bedrock/docs/API_DeleteInferenceProfile
> **target_lang:** meta — documentation tier. ALL sections preserved.



# DeleteInferenceProfile
<a name="API_DeleteInferenceProfile"></a>

Deletes an application inference profile. For more information, see [Increase throughput and resilience with cross-region inference in Amazon Bedrock](https://docs.aws.amazon.com/bedrock/latest/userguide/cross-region-inference.html). in the Amazon Bedrock User Guide.

## Request Syntax
<a name="API_DeleteInferenceProfile_RequestSyntax"></a>

```
DELETE /inference-profiles/{{inferenceProfileIdentifier}} HTTP/1.1
```

## URI Request Parameters
<a name="API_DeleteInferenceProfile_RequestParameters"></a>

The request uses the following URI parameters.

 ** [inferenceProfileIdentifier](#API_DeleteInferenceProfile_RequestSyntax) **   <a name="bedrock-DeleteInferenceProfile-request-uri-inferenceProfileIdentifier"></a>
The Amazon Resource Name (ARN) or ID of the application inference profile to delete.  
Length Constraints: Minimum length of 1. Maximum length of 2048.  
Pattern: `(arn:aws(|-us-gov|-cn|-iso|-iso-b):bedrock:(|[0-9a-z-]{0,20}):(|[0-9]{12}):(inference-profile|application-inference-profile)/)?[a-zA-Z0-9-:.]+`   
Required: Yes

## Request Body
<a name="API_DeleteInferenceProfile_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_DeleteInferenceProfile_ResponseSyntax"></a>

```
HTTP/1.1 200
```

## Response Elements
<a name="API_DeleteInferenceProfile_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_DeleteInferenceProfile_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **   
The request is denied because of missing access permissions.  
HTTP Status Code: 403

 ** ConflictException **   
Error occurred because of a conflict while performing an operation.  
HTTP Status Code: 400

 ** InternalServerException **   
An internal server error occurred. Retry your request.  
HTTP Status Code: 500

 ** ResourceNotFoundException **   
The specified resource Amazon Resource Name (ARN) was not found. Check the Amazon Resource Name (ARN) and try your request again.  
HTTP Status Code: 404

 ** ThrottlingException **   
The number of requests exceeds the limit. Resubmit your request later.  
HTTP Status Code: 429

 ** ValidationException **   
Input validation failed. Check your request parameters and retry the request.  
HTTP Status Code: 400

## Examples
<a name="API_DeleteInferenceProfile_Examples"></a>

### Delete an application inference profile
<a name="API_DeleteInferenceProfile_Example_1"></a>

Assuming you've created an application inference profile called `USClaudeSonnetApplicationIP`, run the following example to delete it:

#### Sample Request
<a name="API_DeleteInferenceProfile_Example_1_Request"></a>

```
DELETE /inference-profiles/USClaudeSonnetApplicationIP HTTP/1.1
```

## See Also
<a name="API_DeleteInferenceProfile_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/bedrock-2023-04-20/DeleteInferenceProfile) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/bedrock-2023-04-20/DeleteInferenceProfile) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-2023-04-20/DeleteInferenceProfile) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/bedrock-2023-04-20/DeleteInferenceProfile) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-2023-04-20/DeleteInferenceProfile) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/bedrock-2023-04-20/DeleteInferenceProfile) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/bedrock-2023-04-20/DeleteInferenceProfile) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/bedrock-2023-04-20/DeleteInferenceProfile) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/bedrock-2023-04-20/DeleteInferenceProfile) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-2023-04-20/DeleteInferenceProfile) 