---
id: "@specs/aws/kendra/docs/API_ListQuerySuggestionsBlockLists"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS ListQuerySuggestionsBlockLists"
status: active
depends_on:
  - "@specs/aws/kendra/meta"
---

# ListQuerySuggestionsBlockLists

> **source:** AWS Documentation
> **spec:id:** @specs/aws/kendra/docs/API_ListQuerySuggestionsBlockLists
> **target_lang:** meta — documentation tier. ALL sections preserved.



# ListQuerySuggestionsBlockLists
<a name="API_ListQuerySuggestionsBlockLists"></a>

Lists the block lists used for query suggestions for an index.

For information on the current quota limits for block lists, see [Quotas for Amazon Kendra](https://docs.aws.amazon.com/kendra/latest/dg/quotas.html).

 `ListQuerySuggestionsBlockLists` is currently not supported in the AWS GovCloud (US-West) region.

## Request Syntax
<a name="API_ListQuerySuggestionsBlockLists_RequestSyntax"></a>

```
{
   "IndexId": "{{string}}",
   "MaxResults": {{number}},
   "NextToken": "{{string}}"
}
```

## Request Parameters
<a name="API_ListQuerySuggestionsBlockLists_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [IndexId](#API_ListQuerySuggestionsBlockLists_RequestSyntax) **   <a name="kendra-ListQuerySuggestionsBlockLists-request-IndexId"></a>
The identifier of the index for a list of all block lists that exist for that index.  
For information on the current quota limits for block lists, see [Quotas for Amazon Kendra](https://docs.aws.amazon.com/kendra/latest/dg/quotas.html).  
Type: String  
Length Constraints: Fixed length of 36.  
Pattern: `[a-zA-Z0-9][a-zA-Z0-9-]*`   
Required: Yes

 ** [MaxResults](#API_ListQuerySuggestionsBlockLists_RequestSyntax) **   <a name="kendra-ListQuerySuggestionsBlockLists-request-MaxResults"></a>
The maximum number of block lists to return.  
Type: Integer  
Valid Range: Minimum value of 1. Maximum value of 100.  
Required: No

 ** [NextToken](#API_ListQuerySuggestionsBlockLists_RequestSyntax) **   <a name="kendra-ListQuerySuggestionsBlockLists-request-NextToken"></a>
If the previous response was incomplete (because there is more data to retrieve), Amazon Kendra returns a pagination token in the response. You can use this pagination token to retrieve the next set of block lists (`BlockListSummaryItems`).  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 800.  
Required: No

## Response Syntax
<a name="API_ListQuerySuggestionsBlockLists_ResponseSyntax"></a>

```
{
   "BlockListSummaryItems": [ 
      { 
         "CreatedAt": number,
         "Id": "string",
         "ItemCount": number,
         "Name": "string",
         "Status": "string",
         "UpdatedAt": number
      }
   ],
   "NextToken": "string"
}
```

## Response Elements
<a name="API_ListQuerySuggestionsBlockLists_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [BlockListSummaryItems](#API_ListQuerySuggestionsBlockLists_ResponseSyntax) **   <a name="kendra-ListQuerySuggestionsBlockLists-response-BlockListSummaryItems"></a>
Summary items for a block list.  
This includes summary items on the block list ID, block list name, when the block list was created, when the block list was last updated, and the count of block words/phrases in the block list.  
For information on the current quota limits for block lists, see [Quotas for Amazon Kendra](https://docs.aws.amazon.com/kendra/latest/dg/quotas.html).  
Type: Array of [QuerySuggestionsBlockListSummary](API_QuerySuggestionsBlockListSummary.md) objects

 ** [NextToken](#API_ListQuerySuggestionsBlockLists_ResponseSyntax) **   <a name="kendra-ListQuerySuggestionsBlockLists-response-NextToken"></a>
If the response is truncated, Amazon Kendra returns this token that you can use in the subsequent request to retrieve the next set of block lists.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 800.

## Errors
<a name="API_ListQuerySuggestionsBlockLists_Errors"></a>

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
<a name="API_ListQuerySuggestionsBlockLists_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/kendra-2019-02-03/ListQuerySuggestionsBlockLists) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/kendra-2019-02-03/ListQuerySuggestionsBlockLists) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/kendra-2019-02-03/ListQuerySuggestionsBlockLists) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/kendra-2019-02-03/ListQuerySuggestionsBlockLists) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/kendra-2019-02-03/ListQuerySuggestionsBlockLists) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/kendra-2019-02-03/ListQuerySuggestionsBlockLists) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/kendra-2019-02-03/ListQuerySuggestionsBlockLists) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/kendra-2019-02-03/ListQuerySuggestionsBlockLists) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/kendra-2019-02-03/ListQuerySuggestionsBlockLists) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/kendra-2019-02-03/ListQuerySuggestionsBlockLists) 