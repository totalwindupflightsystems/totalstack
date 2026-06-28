---
id: "@specs/aws/kendra/docs/API_UpdateFeaturedResultsSet"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS UpdateFeaturedResultsSet"
status: active
depends_on:
  - "@specs/aws/kendra/meta"
---

# UpdateFeaturedResultsSet

> **source:** AWS Documentation
> **spec:id:** @specs/aws/kendra/docs/API_UpdateFeaturedResultsSet
> **target_lang:** meta — documentation tier. ALL sections preserved.



# UpdateFeaturedResultsSet
<a name="API_UpdateFeaturedResultsSet"></a>

Updates a set of featured results. Features results are placed above all other results for certain queries. You map specific queries to specific documents for featuring in the results. If a query contains an exact match of a query, then one or more specific documents are featured in the search results.

## Request Syntax
<a name="API_UpdateFeaturedResultsSet_RequestSyntax"></a>

```
{
   "Description": "{{string}}",
   "FeaturedDocuments": [ 
      { 
         "Id": "{{string}}"
      }
   ],
   "FeaturedResultsSetId": "{{string}}",
   "FeaturedResultsSetName": "{{string}}",
   "IndexId": "{{string}}",
   "QueryTexts": [ "{{string}}" ],
   "Status": "{{string}}"
}
```

## Request Parameters
<a name="API_UpdateFeaturedResultsSet_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [Description](#API_UpdateFeaturedResultsSet_RequestSyntax) **   <a name="kendra-UpdateFeaturedResultsSet-request-Description"></a>
A new description for the set of featured results.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 1000.  
Pattern: `^\P{C}*$`   
Required: No

 ** [FeaturedDocuments](#API_UpdateFeaturedResultsSet_RequestSyntax) **   <a name="kendra-UpdateFeaturedResultsSet-request-FeaturedDocuments"></a>
A list of document IDs for the documents you want to feature at the top of the search results page. For more information on the list of featured documents, see [FeaturedResultsSet](https://docs.aws.amazon.com/kendra/latest/dg/API_FeaturedResultsSet.html).  
Type: Array of [FeaturedDocument](API_FeaturedDocument.md) objects  
Required: No

 ** [FeaturedResultsSetId](#API_UpdateFeaturedResultsSet_RequestSyntax) **   <a name="kendra-UpdateFeaturedResultsSet-request-FeaturedResultsSetId"></a>
The identifier of the set of featured results that you want to update.  
Type: String  
Length Constraints: Fixed length of 36.  
Pattern: `^[a-zA-Z-0-9]*`   
Required: Yes

 ** [FeaturedResultsSetName](#API_UpdateFeaturedResultsSet_RequestSyntax) **   <a name="kendra-UpdateFeaturedResultsSet-request-FeaturedResultsSetName"></a>
A new name for the set of featured results.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 1000.  
Pattern: `[a-zA-Z0-9][ a-zA-Z0-9_-]*`   
Required: No

 ** [IndexId](#API_UpdateFeaturedResultsSet_RequestSyntax) **   <a name="kendra-UpdateFeaturedResultsSet-request-IndexId"></a>
The identifier of the index used for featuring results.  
Type: String  
Length Constraints: Fixed length of 36.  
Pattern: `[a-zA-Z0-9][a-zA-Z0-9-]*`   
Required: Yes

 ** [QueryTexts](#API_UpdateFeaturedResultsSet_RequestSyntax) **   <a name="kendra-UpdateFeaturedResultsSet-request-QueryTexts"></a>
A list of queries for featuring results. For more information on the list of queries, see [FeaturedResultsSet](https://docs.aws.amazon.com/kendra/latest/dg/API_FeaturedResultsSet.html).  
Type: Array of strings  
Array Members: Minimum number of 0 items. Maximum number of 49 items.  
Required: No

 ** [Status](#API_UpdateFeaturedResultsSet_RequestSyntax) **   <a name="kendra-UpdateFeaturedResultsSet-request-Status"></a>
You can set the status to `ACTIVE` or `INACTIVE`. When the value is `ACTIVE`, featured results are ready for use. You can still configure your settings before setting the status to `ACTIVE`. The queries you specify for featured results must be unique per featured results set for each index, whether the status is `ACTIVE` or `INACTIVE`.  
Type: String  
Valid Values: `ACTIVE | INACTIVE`   
Required: No

## Response Syntax
<a name="API_UpdateFeaturedResultsSet_ResponseSyntax"></a>

```
{
   "FeaturedResultsSet": { 
      "CreationTimestamp": number,
      "Description": "string",
      "FeaturedDocuments": [ 
         { 
            "Id": "string"
         }
      ],
      "FeaturedResultsSetId": "string",
      "FeaturedResultsSetName": "string",
      "LastUpdatedTimestamp": number,
      "QueryTexts": [ "string" ],
      "Status": "string"
   }
}
```

## Response Elements
<a name="API_UpdateFeaturedResultsSet_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [FeaturedResultsSet](#API_UpdateFeaturedResultsSet_ResponseSyntax) **   <a name="kendra-UpdateFeaturedResultsSet-response-FeaturedResultsSet"></a>
Information on the set of featured results. This includes the identifier of the featured results set, whether the featured results set is active or inactive, when the featured results set was last updated, and more.  
Type: [FeaturedResultsSet](API_FeaturedResultsSet.md) object

## Errors
<a name="API_UpdateFeaturedResultsSet_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **   
You don't have sufficient access to perform this action. Please ensure you have the required permission policies and user accounts and try again.  
HTTP Status Code: 400

 ** FeaturedResultsConflictException **   
An error message with a list of conflicting queries used across different sets of featured results. This occurred with the request for a new featured results set. Check that the queries you specified for featured results are unique per featured results set for each index.    
 ** ConflictingItems **   
A list of the conflicting queries, including the query text, the name for the featured results set, and the identifier of the featured results set.  
 ** Message **   
An explanation for the conflicting queries.
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
<a name="API_UpdateFeaturedResultsSet_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/kendra-2019-02-03/UpdateFeaturedResultsSet) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/kendra-2019-02-03/UpdateFeaturedResultsSet) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/kendra-2019-02-03/UpdateFeaturedResultsSet) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/kendra-2019-02-03/UpdateFeaturedResultsSet) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/kendra-2019-02-03/UpdateFeaturedResultsSet) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/kendra-2019-02-03/UpdateFeaturedResultsSet) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/kendra-2019-02-03/UpdateFeaturedResultsSet) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/kendra-2019-02-03/UpdateFeaturedResultsSet) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/kendra-2019-02-03/UpdateFeaturedResultsSet) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/kendra-2019-02-03/UpdateFeaturedResultsSet) 