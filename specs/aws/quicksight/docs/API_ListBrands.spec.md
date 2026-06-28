---
id: "@specs/aws/quicksight/docs/API_ListBrands"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS ListBrands"
status: active
depends_on:
  - "@specs/aws/quicksight/meta"
---

# ListBrands

> **source:** AWS Documentation
> **spec:id:** @specs/aws/quicksight/docs/API_ListBrands
> **target_lang:** meta — documentation tier. ALL sections preserved.



# ListBrands
<a name="API_ListBrands"></a>

Lists all brands in an Quick Sight account.

## Request Syntax
<a name="API_ListBrands_RequestSyntax"></a>

```
GET /accounts/{{AwsAccountId}}/brands?max-results={{MaxResults}}&next-token={{NextToken}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListBrands_RequestParameters"></a>

The request uses the following URI parameters.

 ** [AwsAccountId](#API_ListBrands_RequestSyntax) **   <a name="QS-ListBrands-request-uri-AwsAccountId"></a>
The ID of the AWS account that owns the brands that you want to list.  
Length Constraints: Fixed length of 12.  
Pattern: `^[0-9]{12}$`   
Required: Yes

 ** [MaxResults](#API_ListBrands_RequestSyntax) **   <a name="QS-ListBrands-request-uri-MaxResults"></a>
The maximum number of results to be returned in a single request.  
Valid Range: Minimum value of 1. Maximum value of 100.

 ** [NextToken](#API_ListBrands_RequestSyntax) **   <a name="QS-ListBrands-request-uri-NextToken"></a>
The token for the next set of results, or null if there are no more results.

## Request Body
<a name="API_ListBrands_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListBrands_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "Brands": [ 
      { 
         "Arn": "string",
         "BrandId": "string",
         "BrandName": "string",
         "BrandStatus": "string",
         "CreatedTime": number,
         "Description": "string",
         "LastUpdatedTime": number
      }
   ],
   "NextToken": "string"
}
```

## Response Elements
<a name="API_ListBrands_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Brands](#API_ListBrands_ResponseSyntax) **   <a name="QS-ListBrands-response-Brands"></a>
A list of all brands in your AWS account. This structure provides basic information about each brand.  
Type: Array of [BrandSummary](API_BrandSummary.md) objects

 ** [NextToken](#API_ListBrands_ResponseSyntax) **   <a name="QS-ListBrands-response-NextToken"></a>
The token for the next set of results, or null if there are no more results.  
Type: String

## Errors
<a name="API_ListBrands_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **   
You don't have access to this item. The provided credentials couldn't be validated. You might not be authorized to carry out the request. Make sure that your account is authorized to use the Amazon Quick Sight service, that your policies have the correct permissions, and that you are using the correct credentials.    
 ** RequestId **   
The AWS request ID for this request.
HTTP Status Code: 401

 ** InternalServerException **   
An internal service exception.  
HTTP Status Code: 500

 ** InvalidRequestException **   
You don't have this feature activated for your account. To fix this issue, contact AWS support.    
 ** RequestId **   
The AWS request ID for this request.
HTTP Status Code: 400

 ** ThrottlingException **   
Access is throttled.    
 ** RequestId **   
The AWS request ID for this request.
HTTP Status Code: 429

## See Also
<a name="API_ListBrands_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/quicksight-2018-04-01/ListBrands) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/quicksight-2018-04-01/ListBrands) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/ListBrands) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/quicksight-2018-04-01/ListBrands) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/ListBrands) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/quicksight-2018-04-01/ListBrands) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/quicksight-2018-04-01/ListBrands) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/quicksight-2018-04-01/ListBrands) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/quicksight-2018-04-01/ListBrands) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/ListBrands) 