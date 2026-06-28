---
id: "@specs/aws/quicksight/docs/API_ListThemeVersions"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS ListThemeVersions"
status: active
depends_on:
  - "@specs/aws/quicksight/meta"
---

# ListThemeVersions

> **source:** AWS Documentation
> **spec:id:** @specs/aws/quicksight/docs/API_ListThemeVersions
> **target_lang:** meta — documentation tier. ALL sections preserved.



# ListThemeVersions
<a name="API_ListThemeVersions"></a>

Lists all the versions of the themes in the current AWS account.

## Request Syntax
<a name="API_ListThemeVersions_RequestSyntax"></a>

```
GET /accounts/{{AwsAccountId}}/themes/{{ThemeId}}/versions?max-results={{MaxResults}}&next-token={{NextToken}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListThemeVersions_RequestParameters"></a>

The request uses the following URI parameters.

 ** [AwsAccountId](#API_ListThemeVersions_RequestSyntax) **   <a name="QS-ListThemeVersions-request-uri-AwsAccountId"></a>
The ID of the AWS account that contains the themes that you're listing.  
Length Constraints: Fixed length of 12.  
Pattern: `^[0-9]{12}$`   
Required: Yes

 ** [MaxResults](#API_ListThemeVersions_RequestSyntax) **   <a name="QS-ListThemeVersions-request-uri-MaxResults"></a>
The maximum number of results to be returned per request.  
Valid Range: Minimum value of 1. Maximum value of 100.

 ** [NextToken](#API_ListThemeVersions_RequestSyntax) **   <a name="QS-ListThemeVersions-request-uri-NextToken"></a>
The token for the next set of results, or null if there are no more results.

 ** [ThemeId](#API_ListThemeVersions_RequestSyntax) **   <a name="QS-ListThemeVersions-request-uri-ThemeId"></a>
The ID for the theme.  
Length Constraints: Minimum length of 1. Maximum length of 512.  
Pattern: `[\w\-]+`   
Required: Yes

## Request Body
<a name="API_ListThemeVersions_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListThemeVersions_ResponseSyntax"></a>

```
HTTP/1.1 {{Status}}
Content-type: application/json

{
   "NextToken": "string",
   "RequestId": "string",
   "ThemeVersionSummaryList": [ 
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
<a name="API_ListThemeVersions_ResponseElements"></a>

If the action is successful, the service sends back the following HTTP response.

 ** [Status](#API_ListThemeVersions_ResponseSyntax) **   <a name="QS-ListThemeVersions-response-Status"></a>
The HTTP status of the request.

The following data is returned in JSON format by the service.

 ** [NextToken](#API_ListThemeVersions_ResponseSyntax) **   <a name="QS-ListThemeVersions-response-NextToken"></a>
The token for the next set of results, or null if there are no more results.  
Type: String

 ** [RequestId](#API_ListThemeVersions_ResponseSyntax) **   <a name="QS-ListThemeVersions-response-RequestId"></a>
The AWS request ID for this operation.  
Type: String

 ** [ThemeVersionSummaryList](#API_ListThemeVersions_ResponseSyntax) **   <a name="QS-ListThemeVersions-response-ThemeVersionSummaryList"></a>
A structure containing a list of all the versions of the specified theme.  
Type: Array of [ThemeVersionSummary](API_ThemeVersionSummary.md) objects  
Array Members: Maximum number of 100 items.

## Errors
<a name="API_ListThemeVersions_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **   
You don't have access to this item. The provided credentials couldn't be validated. You might not be authorized to carry out the request. Make sure that your account is authorized to use the Amazon Quick Sight service, that your policies have the correct permissions, and that you are using the correct credentials.    
 ** RequestId **   
The AWS request ID for this request.
HTTP Status Code: 401

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
<a name="API_ListThemeVersions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/quicksight-2018-04-01/ListThemeVersions) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/quicksight-2018-04-01/ListThemeVersions) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/ListThemeVersions) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/quicksight-2018-04-01/ListThemeVersions) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/ListThemeVersions) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/quicksight-2018-04-01/ListThemeVersions) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/quicksight-2018-04-01/ListThemeVersions) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/quicksight-2018-04-01/ListThemeVersions) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/quicksight-2018-04-01/ListThemeVersions) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/ListThemeVersions) 