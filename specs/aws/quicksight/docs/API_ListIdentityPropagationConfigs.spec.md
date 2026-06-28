---
id: "@specs/aws/quicksight/docs/API_ListIdentityPropagationConfigs"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS ListIdentityPropagationConfigs"
status: active
depends_on:
  - "@specs/aws/quicksight/meta"
---

# ListIdentityPropagationConfigs

> **source:** AWS Documentation
> **spec:id:** @specs/aws/quicksight/docs/API_ListIdentityPropagationConfigs
> **target_lang:** meta — documentation tier. ALL sections preserved.



# ListIdentityPropagationConfigs
<a name="API_ListIdentityPropagationConfigs"></a>

Lists all services and authorized targets that the Quick Sight IAM Identity Center application can access.

This operation is only supported for Quick Sight accounts that use IAM Identity Center.

## Request Syntax
<a name="API_ListIdentityPropagationConfigs_RequestSyntax"></a>

```
GET /accounts/{{AwsAccountId}}/identity-propagation-config?max-results={{MaxResults}}&next-token={{NextToken}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListIdentityPropagationConfigs_RequestParameters"></a>

The request uses the following URI parameters.

 ** [AwsAccountId](#API_ListIdentityPropagationConfigs_RequestSyntax) **   <a name="QS-ListIdentityPropagationConfigs-request-uri-AwsAccountId"></a>
The ID of the AWS account that contain the identity propagation configurations of.  
Length Constraints: Fixed length of 12.  
Pattern: `^[0-9]{12}$`   
Required: Yes

 ** [MaxResults](#API_ListIdentityPropagationConfigs_RequestSyntax) **   <a name="QS-ListIdentityPropagationConfigs-request-uri-MaxResults"></a>
The maximum number of results to be returned.  
Valid Range: Minimum value of 1. Maximum value of 10.

 ** [NextToken](#API_ListIdentityPropagationConfigs_RequestSyntax) **   <a name="QS-ListIdentityPropagationConfigs-request-uri-NextToken"></a>
The token for the next set of results, or null if there are no more results.

## Request Body
<a name="API_ListIdentityPropagationConfigs_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListIdentityPropagationConfigs_ResponseSyntax"></a>

```
HTTP/1.1 {{Status}}
Content-type: application/json

{
   "NextToken": "string",
   "RequestId": "string",
   "Services": [ 
      { 
         "AuthorizedTargets": [ "string" ],
         "Service": "string"
      }
   ]
}
```

## Response Elements
<a name="API_ListIdentityPropagationConfigs_ResponseElements"></a>

If the action is successful, the service sends back the following HTTP response.

 ** [Status](#API_ListIdentityPropagationConfigs_ResponseSyntax) **   <a name="QS-ListIdentityPropagationConfigs-response-Status"></a>
The HTTP status of the request.

The following data is returned in JSON format by the service.

 ** [NextToken](#API_ListIdentityPropagationConfigs_ResponseSyntax) **   <a name="QS-ListIdentityPropagationConfigs-response-NextToken"></a>
The token for the next set of results, or null if there are no more results.  
Type: String

 ** [RequestId](#API_ListIdentityPropagationConfigs_ResponseSyntax) **   <a name="QS-ListIdentityPropagationConfigs-response-RequestId"></a>
The AWS request ID for this operation.  
Type: String

 ** [Services](#API_ListIdentityPropagationConfigs_ResponseSyntax) **   <a name="QS-ListIdentityPropagationConfigs-response-Services"></a>
A list of services and their authorized targets that the Quick Sight IAM Identity Center application can access.  
Type: Array of [AuthorizedTargetsByService](API_AuthorizedTargetsByService.md) objects

## Errors
<a name="API_ListIdentityPropagationConfigs_Errors"></a>

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
<a name="API_ListIdentityPropagationConfigs_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/quicksight-2018-04-01/ListIdentityPropagationConfigs) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/quicksight-2018-04-01/ListIdentityPropagationConfigs) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/ListIdentityPropagationConfigs) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/quicksight-2018-04-01/ListIdentityPropagationConfigs) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/ListIdentityPropagationConfigs) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/quicksight-2018-04-01/ListIdentityPropagationConfigs) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/quicksight-2018-04-01/ListIdentityPropagationConfigs) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/quicksight-2018-04-01/ListIdentityPropagationConfigs) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/quicksight-2018-04-01/ListIdentityPropagationConfigs) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/ListIdentityPropagationConfigs) 