---
id: "@specs/aws/eks/docs/API_ListInsights"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS ListInsights"
status: active
depends_on:
  - "@specs/aws/eks/meta"
---

# ListInsights

> **source:** AWS Documentation
> **spec:id:** @specs/aws/eks/docs/API_ListInsights
> **target_lang:** meta — documentation tier. ALL sections preserved.



# ListInsights
<a name="API_ListInsights"></a>

Returns a list of all insights checked for against the specified cluster. You can filter which insights are returned by category, associated Kubernetes version, and status. The default filter lists all categories and every status.

The following lists the available categories:
+  `UPGRADE_READINESS`: Amazon EKS identifies issues that could impact your ability to upgrade to new versions of Kubernetes. These are called upgrade insights.
+  `MISCONFIGURATION`: Amazon EKS identifies misconfiguration in your EKS Hybrid Nodes setup that could impair functionality of your cluster or workloads. These are called configuration insights.

## Request Syntax
<a name="API_ListInsights_RequestSyntax"></a>

```
POST /clusters/{{name}}/insights HTTP/1.1
Content-type: application/json

{
   "filter": { 
      "categories": [ "{{string}}" ],
      "kubernetesVersions": [ "{{string}}" ],
      "statuses": [ "{{string}}" ]
   },
   "maxResults": {{number}},
   "nextToken": "{{string}}"
}
```

## URI Request Parameters
<a name="API_ListInsights_RequestParameters"></a>

The request uses the following URI parameters.

 ** [name](#API_ListInsights_RequestSyntax) **   <a name="AmazonEKS-ListInsights-request-uri-clusterName"></a>
The name of the Amazon EKS cluster associated with the insights.  
Required: Yes

## Request Body
<a name="API_ListInsights_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [filter](#API_ListInsights_RequestSyntax) **   <a name="AmazonEKS-ListInsights-request-filter"></a>
The criteria to filter your list of insights for your cluster. You can filter which insights are returned by category, associated Kubernetes version, and status.  
Type: [InsightsFilter](API_InsightsFilter.md) object  
Required: No

 ** [maxResults](#API_ListInsights_RequestSyntax) **   <a name="AmazonEKS-ListInsights-request-maxResults"></a>
The maximum number of identity provider configurations returned by `ListInsights` in paginated output. When you use this parameter, `ListInsights` returns only `maxResults` results in a single page along with a `nextToken` response element. You can see the remaining results of the initial request by sending another `ListInsights` request with the returned `nextToken` value. This value can be between 1 and 100. If you don't use this parameter, `ListInsights` returns up to 100 results and a `nextToken` value, if applicable.  
Type: Integer  
Valid Range: Minimum value of 1. Maximum value of 100.  
Required: No

 ** [nextToken](#API_ListInsights_RequestSyntax) **   <a name="AmazonEKS-ListInsights-request-nextToken"></a>
The `nextToken` value returned from a previous paginated `ListInsights` request. When the results of a `ListInsights` request exceed `maxResults`, you can use this value to retrieve the next page of results. This value is `null` when there are no more results to return.  
Type: String  
Required: No

## Response Syntax
<a name="API_ListInsights_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "insights": [ 
      { 
         "category": "string",
         "description": "string",
         "id": "string",
         "insightStatus": { 
            "reason": "string",
            "status": "string"
         },
         "kubernetesVersion": "string",
         "lastRefreshTime": number,
         "lastTransitionTime": number,
         "name": "string"
      }
   ],
   "nextToken": "string"
}
```

## Response Elements
<a name="API_ListInsights_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [insights](#API_ListInsights_ResponseSyntax) **   <a name="AmazonEKS-ListInsights-response-insights"></a>
The returned list of insights.  
Type: Array of [InsightSummary](API_InsightSummary.md) objects

 ** [nextToken](#API_ListInsights_ResponseSyntax) **   <a name="AmazonEKS-ListInsights-response-nextToken"></a>
The `nextToken` value to include in a future `ListInsights` request. When the results of a `ListInsights` request exceed `maxResults`, you can use this value to retrieve the next page of results. This value is `null` when there are no more results to return.  
Type: String

## Errors
<a name="API_ListInsights_Errors"></a>

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

 ** InvalidRequestException **   
The request is invalid given the state of the cluster. Check the state of the cluster and the associated operations.    
 ** addonName **   
The request is invalid given the state of the add-on name. Check the state of the cluster and the associated operations.  
 ** clusterName **   
The Amazon EKS cluster associated with the exception.  
 ** message **   
The Amazon EKS add-on name associated with the exception.  
 ** nodegroupName **   
The Amazon EKS managed node group associated with the exception.  
 ** subscriptionId **   
The Amazon EKS subscription ID with the exception.
HTTP Status Code: 400

 ** ResourceNotFoundException **   
The specified resource could not be found. You can view your available clusters with `ListClusters`. You can view your available managed node groups with `ListNodegroups`. Amazon EKS clusters and node groups are AWS Region specific.    
 ** addonName **   
The Amazon EKS add-on name associated with the exception.  
 ** clusterName **   
The Amazon EKS cluster associated with the exception.  
 ** fargateProfileName **   
The Fargate profile associated with the exception.  
 ** message **   
The Amazon EKS message associated with the exception.  
 ** nodegroupName **   
The Amazon EKS managed node group associated with the exception.  
 ** subscriptionId **   
The Amazon EKS subscription ID with the exception.
HTTP Status Code: 404

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
<a name="API_ListInsights_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/eks-2017-11-01/ListInsights) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/eks-2017-11-01/ListInsights) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/eks-2017-11-01/ListInsights) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/eks-2017-11-01/ListInsights) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/eks-2017-11-01/ListInsights) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/eks-2017-11-01/ListInsights) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/eks-2017-11-01/ListInsights) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/eks-2017-11-01/ListInsights) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/eks-2017-11-01/ListInsights) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/eks-2017-11-01/ListInsights) 