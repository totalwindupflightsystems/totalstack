---
id: "@specs/aws/quicksight/docs/API_ListNamespaces"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS ListNamespaces"
status: active
depends_on:
  - "@specs/aws/quicksight/meta"
---

# ListNamespaces

> **source:** AWS Documentation
> **spec:id:** @specs/aws/quicksight/docs/API_ListNamespaces
> **target_lang:** meta — documentation tier. ALL sections preserved.



# ListNamespaces
<a name="API_ListNamespaces"></a>

Lists the namespaces for the specified AWS account. This operation doesn't list deleted namespaces.

## Request Syntax
<a name="API_ListNamespaces_RequestSyntax"></a>

```
GET /accounts/{{AwsAccountId}}/namespaces?max-results={{MaxResults}}&next-token={{NextToken}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListNamespaces_RequestParameters"></a>

The request uses the following URI parameters.

 ** [AwsAccountId](#API_ListNamespaces_RequestSyntax) **   <a name="QS-ListNamespaces-request-uri-AwsAccountId"></a>
The ID for the AWS account that contains the Quick Sight namespaces that you want to list.  
Length Constraints: Fixed length of 12.  
Pattern: `^[0-9]{12}$`   
Required: Yes

 ** [MaxResults](#API_ListNamespaces_RequestSyntax) **   <a name="QS-ListNamespaces-request-uri-MaxResults"></a>
The maximum number of results to return.  
Valid Range: Minimum value of 1. Maximum value of 100.

 ** [NextToken](#API_ListNamespaces_RequestSyntax) **   <a name="QS-ListNamespaces-request-uri-NextToken"></a>
A unique pagination token that can be used in a subsequent request. You will receive a pagination token in the response body of a previous `ListNameSpaces` API call if there is more data that can be returned. To receive the data, make another `ListNamespaces` API call with the returned token to retrieve the next page of data. Each token is valid for 24 hours. If you try to make a `ListNamespaces` API call with an expired token, you will receive a `HTTP 400 InvalidNextTokenException` error.

## Request Body
<a name="API_ListNamespaces_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListNamespaces_ResponseSyntax"></a>

```
HTTP/1.1 {{Status}}
Content-type: application/json

{
   "Namespaces": [ 
      { 
         "Arn": "string",
         "CapacityRegion": "string",
         "CreationStatus": "string",
         "IamIdentityCenterApplicationArn": "string",
         "IamIdentityCenterInstanceArn": "string",
         "IdentityStore": "string",
         "Name": "string",
         "NamespaceError": { 
            "Message": "string",
            "Type": "string"
         }
      }
   ],
   "NextToken": "string",
   "RequestId": "string"
}
```

## Response Elements
<a name="API_ListNamespaces_ResponseElements"></a>

If the action is successful, the service sends back the following HTTP response.

 ** [Status](#API_ListNamespaces_ResponseSyntax) **   <a name="QS-ListNamespaces-response-Status"></a>
The HTTP status of the request.

The following data is returned in JSON format by the service.

 ** [Namespaces](#API_ListNamespaces_ResponseSyntax) **   <a name="QS-ListNamespaces-response-Namespaces"></a>
The information about the namespaces in this AWS account. The response includes the namespace ARN, name, AWS Region, notification email address, creation status, and identity store.  
Type: Array of [NamespaceInfoV2](API_NamespaceInfoV2.md) objects

 ** [NextToken](#API_ListNamespaces_ResponseSyntax) **   <a name="QS-ListNamespaces-response-NextToken"></a>
A unique pagination token that can be used in a subsequent request. Receiving `NextToken` in your response inticates that there is more data that can be returned. To receive the data, make another `ListNamespaces` API call with the returned token to retrieve the next page of data. Each token is valid for 24 hours. If you try to make a `ListNamespaces` API call with an expired token, you will receive a `HTTP 400 InvalidNextTokenException` error.  
Type: String

 ** [RequestId](#API_ListNamespaces_ResponseSyntax) **   <a name="QS-ListNamespaces-response-RequestId"></a>
The AWS request ID for this operation.  
Type: String

## Errors
<a name="API_ListNamespaces_Errors"></a>

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
<a name="API_ListNamespaces_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/quicksight-2018-04-01/ListNamespaces) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/quicksight-2018-04-01/ListNamespaces) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/ListNamespaces) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/quicksight-2018-04-01/ListNamespaces) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/ListNamespaces) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/quicksight-2018-04-01/ListNamespaces) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/quicksight-2018-04-01/ListNamespaces) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/quicksight-2018-04-01/ListNamespaces) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/quicksight-2018-04-01/ListNamespaces) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/ListNamespaces) 