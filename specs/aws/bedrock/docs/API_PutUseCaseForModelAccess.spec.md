---
id: "@specs/aws/bedrock/docs/API_PutUseCaseForModelAccess"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS PutUseCaseForModelAccess"
status: active
depends_on:
  - "@specs/aws/bedrock/meta"
---

# PutUseCaseForModelAccess

> **source:** AWS Documentation
> **spec:id:** @specs/aws/bedrock/docs/API_PutUseCaseForModelAccess
> **target_lang:** meta — documentation tier. ALL sections preserved.



# PutUseCaseForModelAccess
<a name="API_PutUseCaseForModelAccess"></a>

 Returns the use case for model access. The example shown below under *Examples* shows the form data json configuration.

## Request Syntax
<a name="API_PutUseCaseForModelAccess_RequestSyntax"></a>

```
POST /use-case-for-model-access HTTP/1.1
Content-type: application/json

{
   "formData": {{blob}}
}
```

## URI Request Parameters
<a name="API_PutUseCaseForModelAccess_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_PutUseCaseForModelAccess_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [formData](#API_PutUseCaseForModelAccess_RequestSyntax) **   <a name="bedrock-PutUseCaseForModelAccess-request-formData"></a>
 Returns the form data from the Anthropic first time user request.  
Type: Base64-encoded binary data object  
Length Constraints: Minimum length of 10. Maximum length of 16384.  
Required: Yes

## Response Syntax
<a name="API_PutUseCaseForModelAccess_ResponseSyntax"></a>

```
HTTP/1.1 201
```

## Response Elements
<a name="API_PutUseCaseForModelAccess_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 201 response with an empty HTTP body.

## Errors
<a name="API_PutUseCaseForModelAccess_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **   
The request is denied because of missing access permissions.  
HTTP Status Code: 403

 ** InternalServerException **   
An internal server error occurred. Retry your request.  
HTTP Status Code: 500

 ** ThrottlingException **   
The number of requests exceeds the limit. Resubmit your request later.  
HTTP Status Code: 429

 ** ValidationException **   
Input validation failed. Check your request parameters and retry the request.  
HTTP Status Code: 400

## Examples
<a name="API_PutUseCaseForModelAccess_Examples"></a>

### Example
<a name="API_PutUseCaseForModelAccess_Example_1"></a>

This example illustrates one usage of PutUseCaseForModelAccess.

```
form_data = {
    "companyName": COMPANY_NAME,
    "companyWebsite": COMPANY_WEBSITE,
    "intendedUsers": INTENDED_USERS,
    "industryOption": INDUSTRY_OPTION,
    "otherIndustryOption": OTHER_INDUSTRY_OPTION,
    "useCases": USE_CASES
}
```

## See Also
<a name="API_PutUseCaseForModelAccess_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/bedrock-2023-04-20/PutUseCaseForModelAccess) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/bedrock-2023-04-20/PutUseCaseForModelAccess) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-2023-04-20/PutUseCaseForModelAccess) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/bedrock-2023-04-20/PutUseCaseForModelAccess) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-2023-04-20/PutUseCaseForModelAccess) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/bedrock-2023-04-20/PutUseCaseForModelAccess) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/bedrock-2023-04-20/PutUseCaseForModelAccess) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/bedrock-2023-04-20/PutUseCaseForModelAccess) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/bedrock-2023-04-20/PutUseCaseForModelAccess) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-2023-04-20/PutUseCaseForModelAccess) 