---
id: "@specs/aws/eks/docs/API_ListEksAnywhereSubscriptions"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS ListEksAnywhereSubscriptions"
status: active
depends_on:
  - "@specs/aws/eks/meta"
---

# ListEksAnywhereSubscriptions

> **source:** AWS Documentation
> **spec:id:** @specs/aws/eks/docs/API_ListEksAnywhereSubscriptions
> **target_lang:** meta — documentation tier. ALL sections preserved.



# ListEksAnywhereSubscriptions
<a name="API_ListEksAnywhereSubscriptions"></a>

Displays the full description of the subscription.

## Request Syntax
<a name="API_ListEksAnywhereSubscriptions_RequestSyntax"></a>

```
GET /eks-anywhere-subscriptions?includeStatus={{includeStatus}}&maxResults={{maxResults}}&nextToken={{nextToken}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListEksAnywhereSubscriptions_RequestParameters"></a>

The request uses the following URI parameters.

 ** [includeStatus](#API_ListEksAnywhereSubscriptions_RequestSyntax) **   <a name="AmazonEKS-ListEksAnywhereSubscriptions-request-uri-includeStatus"></a>
An array of subscription statuses to filter on.  
Valid Values: `CREATING | ACTIVE | UPDATING | EXPIRING | EXPIRED | DELETING` 

 ** [maxResults](#API_ListEksAnywhereSubscriptions_RequestSyntax) **   <a name="AmazonEKS-ListEksAnywhereSubscriptions-request-uri-maxResults"></a>
The maximum number of cluster results returned by ListEksAnywhereSubscriptions in paginated output. When you use this parameter, ListEksAnywhereSubscriptions returns only maxResults results in a single page along with a nextToken response element. You can see the remaining results of the initial request by sending another ListEksAnywhereSubscriptions request with the returned nextToken value. This value can be between 1 and 100. If you don't use this parameter, ListEksAnywhereSubscriptions returns up to 10 results and a nextToken value if applicable.  
Valid Range: Minimum value of 1. Maximum value of 100.

 ** [nextToken](#API_ListEksAnywhereSubscriptions_RequestSyntax) **   <a name="AmazonEKS-ListEksAnywhereSubscriptions-request-uri-nextToken"></a>
The `nextToken` value returned from a previous paginated `ListEksAnywhereSubscriptions` request where `maxResults` was used and the results exceeded the value of that parameter. Pagination continues from the end of the previous results that returned the `nextToken` value.

## Request Body
<a name="API_ListEksAnywhereSubscriptions_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListEksAnywhereSubscriptions_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "nextToken": "string",
   "subscriptions": [ 
      { 
         "arn": "string",
         "autoRenew": boolean,
         "createdAt": number,
         "effectiveDate": number,
         "expirationDate": number,
         "id": "string",
         "licenseArns": [ "string" ],
         "licenseQuantity": number,
         "licenses": [ 
            { 
               "id": "string",
               "token": "string"
            }
         ],
         "licenseType": "string",
         "status": "string",
         "tags": { 
            "string" : "string" 
         },
         "term": { 
            "duration": number,
            "unit": "string"
         }
      }
   ]
}
```

## Response Elements
<a name="API_ListEksAnywhereSubscriptions_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [nextToken](#API_ListEksAnywhereSubscriptions_ResponseSyntax) **   <a name="AmazonEKS-ListEksAnywhereSubscriptions-response-nextToken"></a>
The nextToken value to include in a future ListEksAnywhereSubscriptions request. When the results of a ListEksAnywhereSubscriptions request exceed maxResults, you can use this value to retrieve the next page of results. This value is null when there are no more results to return.  
Type: String

 ** [subscriptions](#API_ListEksAnywhereSubscriptions_ResponseSyntax) **   <a name="AmazonEKS-ListEksAnywhereSubscriptions-response-subscriptions"></a>
A list of all subscription objects in the region, filtered by includeStatus and paginated by nextToken and maxResults.  
Type: Array of [EksAnywhereSubscription](API_EksAnywhereSubscription.md) objects

## Errors
<a name="API_ListEksAnywhereSubscriptions_Errors"></a>

For information about the errors that are common to all actions, see [Common Errors](CommonErrors.md).

 ** ClientException **   
These errors are usually caused by a client action. Actions can include using an action or resource on behalf of an [IAM principal](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_terms-and-concepts.html) that doesn't have permissions to use the action or resource or specifying an identifier that is not valid.    
 ** addonName **   
The Amazon EKS add-on name associated with the exception.  
 ** clusterName **   
The Amazon EKS cluster associated with the exception.  
 ** message **   
These errors are usually caused by a client action. Actions can include using an action or resource on behalf of an [IAM principal](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_terms-and-concepts.html) that doesn't have permissions to use the action or resource or specifying an identifier that is not valid.  
 ** nodegroupName **   
The Amazon EKS managed node group associated with the exception.  
 ** subscriptionId **   
The Amazon EKS subscription ID with the exception.
HTTP Status Code: 400

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

 ** ServiceUnavailableException **   
The service is unavailable. Back off and retry the operation.    
 ** message **   
The request has failed due to a temporary failure of the server.
HTTP Status Code: 503

## See Also
<a name="API_ListEksAnywhereSubscriptions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/eks-2017-11-01/ListEksAnywhereSubscriptions) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/eks-2017-11-01/ListEksAnywhereSubscriptions) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/eks-2017-11-01/ListEksAnywhereSubscriptions) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/eks-2017-11-01/ListEksAnywhereSubscriptions) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/eks-2017-11-01/ListEksAnywhereSubscriptions) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/eks-2017-11-01/ListEksAnywhereSubscriptions) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/eks-2017-11-01/ListEksAnywhereSubscriptions) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/eks-2017-11-01/ListEksAnywhereSubscriptions) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/eks-2017-11-01/ListEksAnywhereSubscriptions) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/eks-2017-11-01/ListEksAnywhereSubscriptions) 