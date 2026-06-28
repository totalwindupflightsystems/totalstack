---
id: "@specs/aws/quicksight/docs/API_SearchGroups"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS SearchGroups"
status: active
depends_on:
  - "@specs/aws/quicksight/meta"
---

# SearchGroups

> **source:** AWS Documentation
> **spec:id:** @specs/aws/quicksight/docs/API_SearchGroups
> **target_lang:** meta — documentation tier. ALL sections preserved.



# SearchGroups
<a name="API_SearchGroups"></a>

Use the `SearchGroups` operation to search groups in a specified Quick Sight namespace using the supplied filters.

## Request Syntax
<a name="API_SearchGroups_RequestSyntax"></a>

```
POST /accounts/{{AwsAccountId}}/namespaces/{{Namespace}}/groups-search?max-results={{MaxResults}}&next-token={{NextToken}} HTTP/1.1
Content-type: application/json

{
   "Filters": [ 
      { 
         "Name": "{{string}}",
         "Operator": "{{string}}",
         "Value": "{{string}}"
      }
   ]
}
```

## URI Request Parameters
<a name="API_SearchGroups_RequestParameters"></a>

The request uses the following URI parameters.

 ** [AwsAccountId](#API_SearchGroups_RequestSyntax) **   <a name="QS-SearchGroups-request-uri-AwsAccountId"></a>
The ID for the AWS account that the group is in. Currently, you use the ID for the AWS account that contains your Amazon Quick Sight account.  
Length Constraints: Fixed length of 12.  
Pattern: `^[0-9]{12}$`   
Required: Yes

 ** [MaxResults](#API_SearchGroups_RequestSyntax) **   <a name="QS-SearchGroups-request-uri-MaxResults"></a>
The maximum number of results to return from this request.  
Valid Range: Minimum value of 1. Maximum value of 100.

 ** [Namespace](#API_SearchGroups_RequestSyntax) **   <a name="QS-SearchGroups-request-uri-Namespace"></a>
The namespace that you want to search.  
Length Constraints: Maximum length of 64.  
Pattern: `^[a-zA-Z0-9._-]*$`   
Required: Yes

 ** [NextToken](#API_SearchGroups_RequestSyntax) **   <a name="QS-SearchGroups-request-uri-NextToken"></a>
A pagination token that can be used in a subsequent request.

## Request Body
<a name="API_SearchGroups_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [Filters](#API_SearchGroups_RequestSyntax) **   <a name="QS-SearchGroups-request-Filters"></a>
The structure for the search filters that you want to apply to your search.  
Type: Array of [GroupSearchFilter](API_GroupSearchFilter.md) objects  
Array Members: Fixed number of 1 item.  
Required: Yes

## Response Syntax
<a name="API_SearchGroups_ResponseSyntax"></a>

```
HTTP/1.1 {{Status}}
Content-type: application/json

{
   "GroupList": [ 
      { 
         "Arn": "string",
         "Description": "string",
         "GroupName": "string",
         "PrincipalId": "string"
      }
   ],
   "NextToken": "string",
   "RequestId": "string"
}
```

## Response Elements
<a name="API_SearchGroups_ResponseElements"></a>

If the action is successful, the service sends back the following HTTP response.

 ** [Status](#API_SearchGroups_ResponseSyntax) **   <a name="QS-SearchGroups-response-Status"></a>
The HTTP status of the request.

The following data is returned in JSON format by the service.

 ** [GroupList](#API_SearchGroups_ResponseSyntax) **   <a name="QS-SearchGroups-response-GroupList"></a>
A list of groups in a specified namespace that match the filters you set in your `SearchGroups` request.  
Type: Array of [Group](API_Group.md) objects

 ** [NextToken](#API_SearchGroups_ResponseSyntax) **   <a name="QS-SearchGroups-response-NextToken"></a>
A pagination token that can be used in a subsequent request.  
Type: String

 ** [RequestId](#API_SearchGroups_ResponseSyntax) **   <a name="QS-SearchGroups-response-RequestId"></a>
The AWS request ID for this operation.  
Type: String

## Errors
<a name="API_SearchGroups_Errors"></a>

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
<a name="API_SearchGroups_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/quicksight-2018-04-01/SearchGroups) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/quicksight-2018-04-01/SearchGroups) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/SearchGroups) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/quicksight-2018-04-01/SearchGroups) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/SearchGroups) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/quicksight-2018-04-01/SearchGroups) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/quicksight-2018-04-01/SearchGroups) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/quicksight-2018-04-01/SearchGroups) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/quicksight-2018-04-01/SearchGroups) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/SearchGroups) 