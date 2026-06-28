---
id: "@specs/aws/quicksight/docs/API_ListSelfUpgrades"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS ListSelfUpgrades"
status: active
depends_on:
  - "@specs/aws/quicksight/meta"
---

# ListSelfUpgrades

> **source:** AWS Documentation
> **spec:id:** @specs/aws/quicksight/docs/API_ListSelfUpgrades
> **target_lang:** meta — documentation tier. ALL sections preserved.



# ListSelfUpgrades
<a name="API_ListSelfUpgrades"></a>

Lists all self-upgrade requests for a Quick account.

## Request Syntax
<a name="API_ListSelfUpgrades_RequestSyntax"></a>

```
GET /accounts/{{AwsAccountId}}/namespaces/{{Namespace}}/self-upgrade-requests?max-results={{MaxResults}}&next-token={{NextToken}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListSelfUpgrades_RequestParameters"></a>

The request uses the following URI parameters.

 ** [AwsAccountId](#API_ListSelfUpgrades_RequestSyntax) **   <a name="QS-ListSelfUpgrades-request-uri-AwsAccountId"></a>
The ID of the AWS account that contains the self-upgrade requests.  
Length Constraints: Fixed length of 12.  
Pattern: `^[0-9]{12}$`   
Required: Yes

 ** [MaxResults](#API_ListSelfUpgrades_RequestSyntax) **   <a name="QS-ListSelfUpgrades-request-uri-MaxResults"></a>
The maximum number of results to return.  
Valid Range: Minimum value of 1. Maximum value of 100.

 ** [Namespace](#API_ListSelfUpgrades_RequestSyntax) **   <a name="QS-ListSelfUpgrades-request-uri-Namespace"></a>
The Quick namespace for the self-upgrade requests.  
Length Constraints: Maximum length of 64.  
Pattern: `^[a-zA-Z0-9._-]*$`   
Required: Yes

 ** [NextToken](#API_ListSelfUpgrades_RequestSyntax) **   <a name="QS-ListSelfUpgrades-request-uri-NextToken"></a>
The token for the next set of results, or null if there are no more results.

## Request Body
<a name="API_ListSelfUpgrades_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListSelfUpgrades_ResponseSyntax"></a>

```
HTTP/1.1 {{Status}}
Content-type: application/json

{
   "NextToken": "string",
   "RequestId": "string",
   "SelfUpgradeRequestDetails": [ 
      { 
         "CreationTime": number,
         "lastUpdateAttemptTime": number,
         "lastUpdateFailureReason": "string",
         "OriginalRole": "string",
         "RequestedRole": "string",
         "RequestNote": "string",
         "RequestStatus": "string",
         "UpgradeRequestId": "string",
         "UserName": "string"
      }
   ]
}
```

## Response Elements
<a name="API_ListSelfUpgrades_ResponseElements"></a>

If the action is successful, the service sends back the following HTTP response.

 ** [Status](#API_ListSelfUpgrades_ResponseSyntax) **   <a name="QS-ListSelfUpgrades-response-Status"></a>
The HTTP status of the request.

The following data is returned in JSON format by the service.

 ** [NextToken](#API_ListSelfUpgrades_ResponseSyntax) **   <a name="QS-ListSelfUpgrades-response-NextToken"></a>
The token for the next set of results, or null if there are no more results.  
Type: String

 ** [RequestId](#API_ListSelfUpgrades_ResponseSyntax) **   <a name="QS-ListSelfUpgrades-response-RequestId"></a>
The AWS request ID for this operation.  
Type: String

 ** [SelfUpgradeRequestDetails](#API_ListSelfUpgrades_ResponseSyntax) **   <a name="QS-ListSelfUpgrades-response-SelfUpgradeRequestDetails"></a>
A list of self-upgrade request details.  
Type: Array of [SelfUpgradeRequestDetail](API_SelfUpgradeRequestDetail.md) objects

## Errors
<a name="API_ListSelfUpgrades_Errors"></a>

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

 ** LimitExceededException **   
A limit is exceeded.    
 ** RequestId **   
The AWS request ID for this request.  
 ** ResourceType **   
Limit exceeded.
HTTP Status Code: 409

 ** PreconditionNotMetException **   
One or more preconditions aren't met.    
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

 ** ResourceUnavailableException **   
This resource is currently unavailable.    
 ** RequestId **   
The AWS request ID for this request.  
 ** ResourceType **   
The resource type for this request.
HTTP Status Code: 503

 ** ThrottlingException **   
Access is throttled.    
 ** RequestId **   
The AWS request ID for this request.
HTTP Status Code: 429

## See Also
<a name="API_ListSelfUpgrades_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/quicksight-2018-04-01/ListSelfUpgrades) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/quicksight-2018-04-01/ListSelfUpgrades) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/ListSelfUpgrades) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/quicksight-2018-04-01/ListSelfUpgrades) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/ListSelfUpgrades) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/quicksight-2018-04-01/ListSelfUpgrades) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/quicksight-2018-04-01/ListSelfUpgrades) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/quicksight-2018-04-01/ListSelfUpgrades) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/quicksight-2018-04-01/ListSelfUpgrades) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/ListSelfUpgrades) 