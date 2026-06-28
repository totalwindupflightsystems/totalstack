---
id: "@specs/aws/kendra/docs/API_ListThesauri"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS ListThesauri"
status: active
depends_on:
  - "@specs/aws/kendra/meta"
---

# ListThesauri

> **source:** AWS Documentation
> **spec:id:** @specs/aws/kendra/docs/API_ListThesauri
> **target_lang:** meta — documentation tier. ALL sections preserved.



# ListThesauri
<a name="API_ListThesauri"></a>

Lists the thesauri for an index.

## Request Syntax
<a name="API_ListThesauri_RequestSyntax"></a>

```
{
   "IndexId": "{{string}}",
   "MaxResults": {{number}},
   "NextToken": "{{string}}"
}
```

## Request Parameters
<a name="API_ListThesauri_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [IndexId](#API_ListThesauri_RequestSyntax) **   <a name="kendra-ListThesauri-request-IndexId"></a>
The identifier of the index with one or more thesauri.  
Type: String  
Length Constraints: Fixed length of 36.  
Pattern: `[a-zA-Z0-9][a-zA-Z0-9-]*`   
Required: Yes

 ** [MaxResults](#API_ListThesauri_RequestSyntax) **   <a name="kendra-ListThesauri-request-MaxResults"></a>
The maximum number of thesauri to return.  
Type: Integer  
Valid Range: Minimum value of 1. Maximum value of 100.  
Required: No

 ** [NextToken](#API_ListThesauri_RequestSyntax) **   <a name="kendra-ListThesauri-request-NextToken"></a>
If the previous response was incomplete (because there is more data to retrieve), Amazon Kendra returns a pagination token in the response. You can use this pagination token to retrieve the next set of thesauri (`ThesaurusSummaryItems`).   
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 800.  
Required: No

## Response Syntax
<a name="API_ListThesauri_ResponseSyntax"></a>

```
{
   "NextToken": "string",
   "ThesaurusSummaryItems": [ 
      { 
         "CreatedAt": number,
         "Id": "string",
         "Name": "string",
         "Status": "string",
         "UpdatedAt": number
      }
   ]
}
```

## Response Elements
<a name="API_ListThesauri_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [NextToken](#API_ListThesauri_ResponseSyntax) **   <a name="kendra-ListThesauri-response-NextToken"></a>
If the response is truncated, Amazon Kendra returns this token that you can use in the subsequent request to retrieve the next set of thesauri.   
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 800.

 ** [ThesaurusSummaryItems](#API_ListThesauri_ResponseSyntax) **   <a name="kendra-ListThesauri-response-ThesaurusSummaryItems"></a>
An array of summary information for a thesaurus or multiple thesauri.  
Type: Array of [ThesaurusSummary](API_ThesaurusSummary.md) objects

## Errors
<a name="API_ListThesauri_Errors"></a>

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
<a name="API_ListThesauri_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/kendra-2019-02-03/ListThesauri) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/kendra-2019-02-03/ListThesauri) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/kendra-2019-02-03/ListThesauri) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/kendra-2019-02-03/ListThesauri) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/kendra-2019-02-03/ListThesauri) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/kendra-2019-02-03/ListThesauri) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/kendra-2019-02-03/ListThesauri) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/kendra-2019-02-03/ListThesauri) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/kendra-2019-02-03/ListThesauri) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/kendra-2019-02-03/ListThesauri) 