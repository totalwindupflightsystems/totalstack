---
id: "@specs/aws/quicksight/docs/API_ListTemplateVersions"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS ListTemplateVersions"
status: active
depends_on:
  - "@specs/aws/quicksight/meta"
---

# ListTemplateVersions

> **source:** AWS Documentation
> **spec:id:** @specs/aws/quicksight/docs/API_ListTemplateVersions
> **target_lang:** meta — documentation tier. ALL sections preserved.



# ListTemplateVersions
<a name="API_ListTemplateVersions"></a>

Lists all the versions of the templates in the current Amazon Quick Sight account.

## Request Syntax
<a name="API_ListTemplateVersions_RequestSyntax"></a>

```
GET /accounts/{{AwsAccountId}}/templates/{{TemplateId}}/versions?max-results={{MaxResults}}&next-token={{NextToken}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListTemplateVersions_RequestParameters"></a>

The request uses the following URI parameters.

 ** [AwsAccountId](#API_ListTemplateVersions_RequestSyntax) **   <a name="QS-ListTemplateVersions-request-uri-AwsAccountId"></a>
The ID of the AWS account that contains the templates that you're listing.  
Length Constraints: Fixed length of 12.  
Pattern: `^[0-9]{12}$`   
Required: Yes

 ** [MaxResults](#API_ListTemplateVersions_RequestSyntax) **   <a name="QS-ListTemplateVersions-request-uri-MaxResults"></a>
The maximum number of results to be returned per request.  
Valid Range: Minimum value of 1. Maximum value of 100.

 ** [NextToken](#API_ListTemplateVersions_RequestSyntax) **   <a name="QS-ListTemplateVersions-request-uri-NextToken"></a>
The token for the next set of results, or null if there are no more results.

 ** [TemplateId](#API_ListTemplateVersions_RequestSyntax) **   <a name="QS-ListTemplateVersions-request-uri-TemplateId"></a>
The ID for the template.  
Length Constraints: Minimum length of 1. Maximum length of 512.  
Pattern: `[\w\-]+`   
Required: Yes

## Request Body
<a name="API_ListTemplateVersions_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListTemplateVersions_ResponseSyntax"></a>

```
HTTP/1.1 {{Status}}
Content-type: application/json

{
   "NextToken": "string",
   "RequestId": "string",
   "TemplateVersionSummaryList": [ 
      { 
         "Arn": "string",
         "CreatedTime": number,
         "Description": "string",
         "Status": "string",
         "VersionNumber": number
      }
   ]
}
```

## Response Elements
<a name="API_ListTemplateVersions_ResponseElements"></a>

If the action is successful, the service sends back the following HTTP response.

 ** [Status](#API_ListTemplateVersions_ResponseSyntax) **   <a name="QS-ListTemplateVersions-response-Status"></a>
The HTTP status of the request.

The following data is returned in JSON format by the service.

 ** [NextToken](#API_ListTemplateVersions_ResponseSyntax) **   <a name="QS-ListTemplateVersions-response-NextToken"></a>
The token for the next set of results, or null if there are no more results.  
Type: String

 ** [RequestId](#API_ListTemplateVersions_ResponseSyntax) **   <a name="QS-ListTemplateVersions-response-RequestId"></a>
The AWS request ID for this operation.  
Type: String

 ** [TemplateVersionSummaryList](#API_ListTemplateVersions_ResponseSyntax) **   <a name="QS-ListTemplateVersions-response-TemplateVersionSummaryList"></a>
A structure containing a list of all the versions of the specified template.  
Type: Array of [TemplateVersionSummary](API_TemplateVersionSummary.md) objects  
Array Members: Maximum number of 100 items.

## Errors
<a name="API_ListTemplateVersions_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalFailureException **   
An internal failure occurred.    
 ** RequestId **   
The AWS request ID for this request.
HTTP Status Code: 500

 ** InvalidNextTokenException **   
The `NextToken` value isn't valid.    
 ** RequestId **   
The AWS request ID for this request.
HTTP Status Code: 400

 ** InvalidParameterValueException **   
One or more parameters has a value that isn't valid.    
 ** RequestId **   
The AWS request ID for this request.
HTTP Status Code: 400

 ** ResourceNotFoundException **   
One or more resources can't be found.    
 ** RequestId **   
The AWS request ID for this request.  
 ** ResourceType **   
The resource type for this request.
HTTP Status Code: 404

 ** ThrottlingException **   
Access is throttled.    
 ** RequestId **   
The AWS request ID for this request.
HTTP Status Code: 429

 ** UnsupportedUserEditionException **   
This error indicates that you are calling an operation on an Amazon Quick Suite subscription where the edition doesn't include support for that operation. Amazon Quick Suite currently has Standard Edition and Enterprise Edition. Not every operation and capability is available in every edition.    
 ** RequestId **   
The AWS request ID for this request.
HTTP Status Code: 403

## See Also
<a name="API_ListTemplateVersions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/quicksight-2018-04-01/ListTemplateVersions) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/quicksight-2018-04-01/ListTemplateVersions) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/ListTemplateVersions) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/quicksight-2018-04-01/ListTemplateVersions) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/ListTemplateVersions) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/quicksight-2018-04-01/ListTemplateVersions) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/quicksight-2018-04-01/ListTemplateVersions) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/quicksight-2018-04-01/ListTemplateVersions) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/quicksight-2018-04-01/ListTemplateVersions) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/ListTemplateVersions) 