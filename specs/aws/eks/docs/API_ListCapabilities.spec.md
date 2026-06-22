---
id: "@specs/aws/eks/docs/API_ListCapabilities"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS ListCapabilities"
status: active
depends_on:
  - "@specs/aws/eks/meta"
---

# ListCapabilities

> **source:** AWS Documentation
> **spec:id:** @specs/aws/eks/docs/API_ListCapabilities
> **target_lang:** meta — documentation tier. ALL sections preserved.



# ListCapabilities
<a name="API_ListCapabilities"></a>

Lists all managed capabilities in your Amazon EKS cluster. You can use this operation to get an overview of all capabilities and their current status.

## Request Syntax
<a name="API_ListCapabilities_RequestSyntax"></a>

```
GET /clusters/{{name}}/capabilities?maxResults={{maxResults}}&nextToken={{nextToken}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListCapabilities_RequestParameters"></a>

The request uses the following URI parameters.

 ** [name](#API_ListCapabilities_RequestSyntax) **   <a name="AmazonEKS-ListCapabilities-request-uri-clusterName"></a>
The name of the Amazon EKS cluster for which you want to list capabilities.  
Required: Yes

 ** [maxResults](#API_ListCapabilities_RequestSyntax) **   <a name="AmazonEKS-ListCapabilities-request-uri-maxResults"></a>
The maximum number of results to return in a single call. To retrieve the remaining results, make another call with the returned `nextToken` value. If you don't specify a value, the default is 100 results.  
Valid Range: Minimum value of 1. Maximum value of 100.

 ** [nextToken](#API_ListCapabilities_RequestSyntax) **   <a name="AmazonEKS-ListCapabilities-request-uri-nextToken"></a>
The `nextToken` value returned from a previous paginated request, where `maxResults` was used and the results exceeded the value of that parameter. Pagination continues from the end of the previous results that returned the `nextToken` value. This value is null when there are no more results to return.

## Request Body
<a name="API_ListCapabilities_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListCapabilities_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "capabilities": [ 
      { 
         "arn": "string",
         "capabilityName": "string",
         "createdAt": number,
         "modifiedAt": number,
         "status": "string",
         "type": "string",
         "version": "string"
      }
   ],
   "nextToken": "string"
}
```

## Response Elements
<a name="API_ListCapabilities_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [capabilities](#API_ListCapabilities_ResponseSyntax) **   <a name="AmazonEKS-ListCapabilities-response-capabilities"></a>
A list of capability summary objects, each containing basic information about a capability including its name, ARN, type, status, version, and timestamps.  
Type: Array of [CapabilitySummary](API_CapabilitySummary.md) objects

 ** [nextToken](#API_ListCapabilities_ResponseSyntax) **   <a name="AmazonEKS-ListCapabilities-response-nextToken"></a>
The `nextToken` value to include in a future `ListCapabilities` request. When the results of a `ListCapabilities` request exceed `maxResults`, you can use this value to retrieve the next page of results. This value is null when there are no more results to return.  
Type: String

## Errors
<a name="API_ListCapabilities_Errors"></a>

For information about the errors that are common to all actions, see [Common Errors](CommonErrors.md).

 ** InvalidParameterException **   
The specified parameter is invalid. Review the available parameters for the API request.    
 ** addonName **   
The specified parameter for the add-on name is invalid. Review the available parameters for the API request  
 ** clusterName **   
The Amazon EKS cluster associated with the exception.  
 ** fargateProfileName **   
The Fargate profile associated with the exception.  
 ** message **   
The specified parameter is invalid. Review the available parameters for the API request.  
 ** nodegroupName **   
The Amazon EKS managed node group associated with the exception.  
 ** subscriptionId **   
The Amazon EKS subscription ID with the exception.
HTTP Status Code: 400

 ** ServerException **   
These errors are usually caused by a server-side issue.    
 ** addonName **   
The Amazon EKS add-on name associated with the exception.  
 ** clusterName **   
The Amazon EKS cluster associated with the exception.  
 ** message **   
These errors are usually caused by a server-side issue.  
 ** nodegroupName **   
The Amazon EKS managed node group associated with the exception.  
 ** subscriptionId **   
The Amazon EKS subscription ID with the exception.
HTTP Status Code: 500

## See Also
<a name="API_ListCapabilities_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/eks-2017-11-01/ListCapabilities) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/eks-2017-11-01/ListCapabilities) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/eks-2017-11-01/ListCapabilities) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/eks-2017-11-01/ListCapabilities) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/eks-2017-11-01/ListCapabilities) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/eks-2017-11-01/ListCapabilities) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/eks-2017-11-01/ListCapabilities) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/eks-2017-11-01/ListCapabilities) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/eks-2017-11-01/ListCapabilities) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/eks-2017-11-01/ListCapabilities) 