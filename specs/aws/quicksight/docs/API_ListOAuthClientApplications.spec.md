---
id: "@specs/aws/quicksight/docs/API_ListOAuthClientApplications"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS ListOAuthClientApplications"
status: active
depends_on:
  - "@specs/aws/quicksight/meta"
---

# ListOAuthClientApplications

> **source:** AWS Documentation
> **spec:id:** @specs/aws/quicksight/docs/API_ListOAuthClientApplications
> **target_lang:** meta — documentation tier. ALL sections preserved.



# ListOAuthClientApplications
<a name="API_ListOAuthClientApplications"></a>

Lists all OAuthClientApplications in the current AWS Region that belong to this AWS account.

## Request Syntax
<a name="API_ListOAuthClientApplications_RequestSyntax"></a>

```
GET /accounts/{{AwsAccountId}}/oauth-client-applications?max-results={{MaxResults}}&next-token={{NextToken}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListOAuthClientApplications_RequestParameters"></a>

The request uses the following URI parameters.

 ** [AwsAccountId](#API_ListOAuthClientApplications_RequestSyntax) **   <a name="QS-ListOAuthClientApplications-request-uri-AwsAccountId"></a>
The AWS account ID.  
Length Constraints: Fixed length of 12.  
Pattern: `^[0-9]{12}$`   
Required: Yes

 ** [MaxResults](#API_ListOAuthClientApplications_RequestSyntax) **   <a name="QS-ListOAuthClientApplications-request-uri-MaxResults"></a>
The maximum number of results to return.  
Valid Range: Minimum value of 1. Maximum value of 100.

 ** [NextToken](#API_ListOAuthClientApplications_RequestSyntax) **   <a name="QS-ListOAuthClientApplications-request-uri-NextToken"></a>
A pagination token that can be used in a subsequent request.

## Request Body
<a name="API_ListOAuthClientApplications_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListOAuthClientApplications_ResponseSyntax"></a>

```
HTTP/1.1 {{Status}}
Content-type: application/json

{
   "NextToken": "string",
   "OAuthClientApplications": [ 
      { 
         "Arn": "string",
         "CreatedTime": number,
         "DataSourceType": "string",
         "IdentityProviderVpcConnectionProperties": { 
            "VpcConnectionArn": "string"
         },
         "LastUpdatedTime": number,
         "Name": "string",
         "OAuthClientApplicationId": "string",
         "OAuthClientAuthenticationType": "string"
      }
   ],
   "RequestId": "string"
}
```

## Response Elements
<a name="API_ListOAuthClientApplications_ResponseElements"></a>

If the action is successful, the service sends back the following HTTP response.

 ** [Status](#API_ListOAuthClientApplications_ResponseSyntax) **   <a name="QS-ListOAuthClientApplications-response-Status"></a>
The HTTP status of the request.

The following data is returned in JSON format by the service.

 ** [NextToken](#API_ListOAuthClientApplications_ResponseSyntax) **   <a name="QS-ListOAuthClientApplications-response-NextToken"></a>
A pagination token that can be used in a subsequent request.  
Type: String

 ** [OAuthClientApplications](#API_ListOAuthClientApplications_ResponseSyntax) **   <a name="QS-ListOAuthClientApplications-response-OAuthClientApplications"></a>
A list of OAuthClientApplication summaries.  
Type: Array of [OAuthClientApplicationSummary](API_OAuthClientApplicationSummary.md) objects

 ** [RequestId](#API_ListOAuthClientApplications_ResponseSyntax) **   <a name="QS-ListOAuthClientApplications-response-RequestId"></a>
The AWS request ID for this operation.  
Type: String

## Errors
<a name="API_ListOAuthClientApplications_Errors"></a>

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

## See Also
<a name="API_ListOAuthClientApplications_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/quicksight-2018-04-01/ListOAuthClientApplications) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/quicksight-2018-04-01/ListOAuthClientApplications) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/ListOAuthClientApplications) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/quicksight-2018-04-01/ListOAuthClientApplications) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/ListOAuthClientApplications) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/quicksight-2018-04-01/ListOAuthClientApplications) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/quicksight-2018-04-01/ListOAuthClientApplications) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/quicksight-2018-04-01/ListOAuthClientApplications) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/quicksight-2018-04-01/ListOAuthClientApplications) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/ListOAuthClientApplications) 