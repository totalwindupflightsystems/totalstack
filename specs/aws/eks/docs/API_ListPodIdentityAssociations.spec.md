---
id: "@specs/aws/eks/docs/API_ListPodIdentityAssociations"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS ListPodIdentityAssociations"
status: active
depends_on:
  - "@specs/aws/eks/meta"
---

# ListPodIdentityAssociations

> **source:** AWS Documentation
> **spec:id:** @specs/aws/eks/docs/API_ListPodIdentityAssociations
> **target_lang:** meta — documentation tier. ALL sections preserved.



# ListPodIdentityAssociations
<a name="API_ListPodIdentityAssociations"></a>

List the EKS Pod Identity associations in a cluster. You can filter the list by the namespace that the association is in or the service account that the association uses.

## Request Syntax
<a name="API_ListPodIdentityAssociations_RequestSyntax"></a>

```
GET /clusters/{{name}}/pod-identity-associations?maxResults={{maxResults}}&namespace={{namespace}}&nextToken={{nextToken}}&serviceAccount={{serviceAccount}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListPodIdentityAssociations_RequestParameters"></a>

The request uses the following URI parameters.

 ** [name](#API_ListPodIdentityAssociations_RequestSyntax) **   <a name="AmazonEKS-ListPodIdentityAssociations-request-uri-clusterName"></a>
The name of the cluster that the associations are in.  
Required: Yes

 ** [maxResults](#API_ListPodIdentityAssociations_RequestSyntax) **   <a name="AmazonEKS-ListPodIdentityAssociations-request-uri-maxResults"></a>
The maximum number of EKS Pod Identity association results returned by `ListPodIdentityAssociations` in paginated output. When you use this parameter, `ListPodIdentityAssociations` returns only `maxResults` results in a single page along with a `nextToken` response element. You can see the remaining results of the initial request by sending another `ListPodIdentityAssociations` request with the returned `nextToken` value. This value can be between 1 and 100. If you don't use this parameter, `ListPodIdentityAssociations` returns up to 100 results and a `nextToken` value if applicable.  
Valid Range: Minimum value of 1. Maximum value of 100.

 ** [namespace](#API_ListPodIdentityAssociations_RequestSyntax) **   <a name="AmazonEKS-ListPodIdentityAssociations-request-uri-namespace"></a>
The name of the Kubernetes namespace inside the cluster that the associations are in.

 ** [nextToken](#API_ListPodIdentityAssociations_RequestSyntax) **   <a name="AmazonEKS-ListPodIdentityAssociations-request-uri-nextToken"></a>
The `nextToken` value returned from a previous paginated `ListUpdates` request where `maxResults` was used and the results exceeded the value of that parameter. Pagination continues from the end of the previous results that returned the `nextToken` value.  
This token should be treated as an opaque identifier that is used only to retrieve the next items in a list and not for other programmatic purposes.

 ** [serviceAccount](#API_ListPodIdentityAssociations_RequestSyntax) **   <a name="AmazonEKS-ListPodIdentityAssociations-request-uri-serviceAccount"></a>
The name of the Kubernetes service account that the associations use.

## Request Body
<a name="API_ListPodIdentityAssociations_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListPodIdentityAssociations_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "associations": [ 
      { 
         "associationArn": "string",
         "associationId": "string",
         "clusterName": "string",
         "namespace": "string",
         "ownerArn": "string",
         "serviceAccount": "string"
      }
   ],
   "nextToken": "string"
}
```

## Response Elements
<a name="API_ListPodIdentityAssociations_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [associations](#API_ListPodIdentityAssociations_ResponseSyntax) **   <a name="AmazonEKS-ListPodIdentityAssociations-response-associations"></a>
The list of summarized descriptions of the associations that are in the cluster and match any filters that you provided.  
Each summary is simplified by removing these fields compared to the full [https://docs.aws.amazon.com/eks/latest/APIReference/API_PodIdentityAssociation.html](https://docs.aws.amazon.com/eks/latest/APIReference/API_PodIdentityAssociation.html):  
+ The IAM role: `roleArn` 
+ The timestamp that the association was created at: `createdAt` 
+ The most recent timestamp that the association was modified at:. `modifiedAt` 
+ The tags on the association: `tags` 
Type: Array of [PodIdentityAssociationSummary](API_PodIdentityAssociationSummary.md) objects

 ** [nextToken](#API_ListPodIdentityAssociations_ResponseSyntax) **   <a name="AmazonEKS-ListPodIdentityAssociations-response-nextToken"></a>
The `nextToken` value to include in a future `ListPodIdentityAssociations` request. When the results of a `ListPodIdentityAssociations` request exceed `maxResults`, you can use this value to retrieve the next page of results. This value is `null` when there are no more results to return.  
This token should be treated as an opaque identifier that is used only to retrieve the next items in a list and not for other programmatic purposes.
Type: String

## Errors
<a name="API_ListPodIdentityAssociations_Errors"></a>

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
<a name="API_ListPodIdentityAssociations_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/eks-2017-11-01/ListPodIdentityAssociations) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/eks-2017-11-01/ListPodIdentityAssociations) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/eks-2017-11-01/ListPodIdentityAssociations) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/eks-2017-11-01/ListPodIdentityAssociations) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/eks-2017-11-01/ListPodIdentityAssociations) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/eks-2017-11-01/ListPodIdentityAssociations) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/eks-2017-11-01/ListPodIdentityAssociations) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/eks-2017-11-01/ListPodIdentityAssociations) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/eks-2017-11-01/ListPodIdentityAssociations) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/eks-2017-11-01/ListPodIdentityAssociations) 