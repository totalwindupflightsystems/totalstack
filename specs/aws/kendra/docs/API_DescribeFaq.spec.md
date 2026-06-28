---
id: "@specs/aws/kendra/docs/API_DescribeFaq"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS DescribeFaq"
status: active
depends_on:
  - "@specs/aws/kendra/meta"
---

# DescribeFaq

> **source:** AWS Documentation
> **spec:id:** @specs/aws/kendra/docs/API_DescribeFaq
> **target_lang:** meta — documentation tier. ALL sections preserved.



# DescribeFaq
<a name="API_DescribeFaq"></a>

Gets information about a FAQ.

## Request Syntax
<a name="API_DescribeFaq_RequestSyntax"></a>

```
{
   "Id": "{{string}}",
   "IndexId": "{{string}}"
}
```

## Request Parameters
<a name="API_DescribeFaq_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [Id](#API_DescribeFaq_RequestSyntax) **   <a name="kendra-DescribeFaq-request-Id"></a>
The identifier of the FAQ you want to get information on.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 100.  
Pattern: `[a-zA-Z0-9][a-zA-Z0-9_-]*`   
Required: Yes

 ** [IndexId](#API_DescribeFaq_RequestSyntax) **   <a name="kendra-DescribeFaq-request-IndexId"></a>
The identifier of the index for the FAQ.  
Type: String  
Length Constraints: Fixed length of 36.  
Pattern: `[a-zA-Z0-9][a-zA-Z0-9-]*`   
Required: Yes

## Response Syntax
<a name="API_DescribeFaq_ResponseSyntax"></a>

```
{
   "CreatedAt": number,
   "Description": "string",
   "ErrorMessage": "string",
   "FileFormat": "string",
   "Id": "string",
   "IndexId": "string",
   "LanguageCode": "string",
   "Name": "string",
   "RoleArn": "string",
   "S3Path": { 
      "Bucket": "string",
      "Key": "string"
   },
   "Status": "string",
   "UpdatedAt": number
}
```

## Response Elements
<a name="API_DescribeFaq_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [CreatedAt](#API_DescribeFaq_ResponseSyntax) **   <a name="kendra-DescribeFaq-response-CreatedAt"></a>
The Unix timestamp when the FAQ was created.  
Type: Timestamp

 ** [Description](#API_DescribeFaq_ResponseSyntax) **   <a name="kendra-DescribeFaq-response-Description"></a>
The description of the FAQ that you provided when it was created.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 1000.  
Pattern: `^\P{C}*$` 

 ** [ErrorMessage](#API_DescribeFaq_ResponseSyntax) **   <a name="kendra-DescribeFaq-response-ErrorMessage"></a>
If the `Status` field is `FAILED`, the `ErrorMessage` field contains the reason why the FAQ failed.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 2048.  
Pattern: `^\P{C}*$` 

 ** [FileFormat](#API_DescribeFaq_ResponseSyntax) **   <a name="kendra-DescribeFaq-response-FileFormat"></a>
The file format used for the FAQ file.  
Type: String  
Valid Values: `CSV | CSV_WITH_HEADER | JSON` 

 ** [Id](#API_DescribeFaq_ResponseSyntax) **   <a name="kendra-DescribeFaq-response-Id"></a>
The identifier of the FAQ.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 100.  
Pattern: `[a-zA-Z0-9][a-zA-Z0-9_-]*` 

 ** [IndexId](#API_DescribeFaq_ResponseSyntax) **   <a name="kendra-DescribeFaq-response-IndexId"></a>
The identifier of the index for the FAQ.  
Type: String  
Length Constraints: Fixed length of 36.  
Pattern: `[a-zA-Z0-9][a-zA-Z0-9-]*` 

 ** [LanguageCode](#API_DescribeFaq_ResponseSyntax) **   <a name="kendra-DescribeFaq-response-LanguageCode"></a>
The code for a language. This shows a supported language for the FAQ document. English is supported by default. For more information on supported languages, including their codes, see [Adding documents in languages other than English](https://docs.aws.amazon.com/kendra/latest/dg/in-adding-languages.html).  
Type: String  
Length Constraints: Minimum length of 2. Maximum length of 10.  
Pattern: `[a-zA-Z-]*` 

 ** [Name](#API_DescribeFaq_ResponseSyntax) **   <a name="kendra-DescribeFaq-response-Name"></a>
The name that you gave the FAQ when it was created.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 100.  
Pattern: `[a-zA-Z0-9][a-zA-Z0-9_-]*` 

 ** [RoleArn](#API_DescribeFaq_ResponseSyntax) **   <a name="kendra-DescribeFaq-response-RoleArn"></a>
The Amazon Resource Name (ARN) of the IAM role that provides access to the S3 bucket containing the FAQ file.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 1284.  
Pattern: `arn:[a-z0-9-\.]{1,63}:[a-z0-9-\.]{0,63}:[a-z0-9-\.]{0,63}:[a-z0-9-\.]{0,63}:[^/].{0,1023}` 

 ** [S3Path](#API_DescribeFaq_ResponseSyntax) **   <a name="kendra-DescribeFaq-response-S3Path"></a>
Information required to find a specific file in an Amazon S3 bucket.  
Type: [S3Path](API_S3Path.md) object

 ** [Status](#API_DescribeFaq_ResponseSyntax) **   <a name="kendra-DescribeFaq-response-Status"></a>
The status of the FAQ. It is ready to use when the status is `ACTIVE`.  
Type: String  
Valid Values: `CREATING | UPDATING | ACTIVE | DELETING | FAILED` 

 ** [UpdatedAt](#API_DescribeFaq_ResponseSyntax) **   <a name="kendra-DescribeFaq-response-UpdatedAt"></a>
The Unix timestamp when the FAQ was last updated.  
Type: Timestamp

## Errors
<a name="API_DescribeFaq_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **   
You don't have sufficient access to perform this action. Please ensure you have the required permission policies and user accounts and try again.  
HTTP Status Code: 400

 ** InternalServerException **   
An issue occurred with the internal server used for your Amazon Kendra service. Please wait a few minutes and try again, or contact [Support](http://aws.amazon.com/contact-us/) for help.  
HTTP Status Code: 500

 ** ResourceNotFoundException **   
The resource you want to use doesn’t exist. Please check you have provided the correct resource and try again.  
HTTP Status Code: 400

 ** ThrottlingException **   
The request was denied due to request throttling. Please reduce the number of requests and try again.  
HTTP Status Code: 400

 ** ValidationException **   
The input fails to satisfy the constraints set by the Amazon Kendra service. Please provide the correct input and try again.  
HTTP Status Code: 400

## See Also
<a name="API_DescribeFaq_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/kendra-2019-02-03/DescribeFaq) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/kendra-2019-02-03/DescribeFaq) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/kendra-2019-02-03/DescribeFaq) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/kendra-2019-02-03/DescribeFaq) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/kendra-2019-02-03/DescribeFaq) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/kendra-2019-02-03/DescribeFaq) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/kendra-2019-02-03/DescribeFaq) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/kendra-2019-02-03/DescribeFaq) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/kendra-2019-02-03/DescribeFaq) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/kendra-2019-02-03/DescribeFaq) 