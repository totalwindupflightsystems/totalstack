---
id: "@specs/aws/mwaa/docs/API_ListEnvironments"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS ListEnvironments"
status: active
depends_on:
  - "@specs/aws/mwaa/meta"
---

# ListEnvironments

> **source:** AWS Documentation
> **spec:id:** @specs/aws/mwaa/docs/API_ListEnvironments
> **target_lang:** meta — documentation tier. ALL sections preserved.



# ListEnvironments
<a name="API_ListEnvironments"></a>

Lists the Amazon Managed Workflows for Apache Airflow (MWAA) environments.

## Request Syntax
<a name="API_ListEnvironments_RequestSyntax"></a>

```
GET /environments?MaxResults={{MaxResults}}&NextToken={{NextToken}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListEnvironments_RequestParameters"></a>

The request uses the following URI parameters.

 ** [MaxResults](#API_ListEnvironments_RequestSyntax) **   <a name="mwaa-ListEnvironments-request-uri-MaxResults"></a>
The maximum number of results to retrieve per page. For example, `5` environments per page.  
Valid Range: Minimum value of 1. Maximum value of 25.

 ** [NextToken](#API_ListEnvironments_RequestSyntax) **   <a name="mwaa-ListEnvironments-request-uri-NextToken"></a>
Retrieves the next page of the results.  
Length Constraints: Minimum length of 0. Maximum length of 2048.

## Request Body
<a name="API_ListEnvironments_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListEnvironments_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "Environments": [ "string" ],
   "NextToken": "string"
}
```

## Response Elements
<a name="API_ListEnvironments_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Environments](#API_ListEnvironments_ResponseSyntax) **   <a name="mwaa-ListEnvironments-response-Environments"></a>
Returns a list of Amazon MWAA environments.  
Type: Array of strings  
Length Constraints: Minimum length of 1. Maximum length of 80.  
Pattern: `[a-zA-Z][0-9a-zA-Z-_]*` 

 ** [NextToken](#API_ListEnvironments_ResponseSyntax) **   <a name="mwaa-ListEnvironments-response-NextToken"></a>
Retrieves the next page of the results.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 2048.

## Errors
<a name="API_ListEnvironments_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalServerException **   
InternalServerException: An internal error has occurred.  
HTTP Status Code: 500

 ** ValidationException **   
ValidationException: The provided input is not valid.  
HTTP Status Code: 400

## See Also
<a name="API_ListEnvironments_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/mwaa-2020-07-01/ListEnvironments) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/mwaa-2020-07-01/ListEnvironments) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mwaa-2020-07-01/ListEnvironments) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/mwaa-2020-07-01/ListEnvironments) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mwaa-2020-07-01/ListEnvironments) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/mwaa-2020-07-01/ListEnvironments) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/mwaa-2020-07-01/ListEnvironments) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/mwaa-2020-07-01/ListEnvironments) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/mwaa-2020-07-01/ListEnvironments) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mwaa-2020-07-01/ListEnvironments) 