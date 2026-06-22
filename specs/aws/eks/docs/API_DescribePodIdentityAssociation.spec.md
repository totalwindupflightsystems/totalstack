---
id: "@specs/aws/eks/docs/API_DescribePodIdentityAssociation"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS DescribePodIdentityAssociation"
status: active
depends_on:
  - "@specs/aws/eks/meta"
---

# DescribePodIdentityAssociation

> **source:** AWS Documentation
> **spec:id:** @specs/aws/eks/docs/API_DescribePodIdentityAssociation
> **target_lang:** meta — documentation tier. ALL sections preserved.



# DescribePodIdentityAssociation
<a name="API_DescribePodIdentityAssociation"></a>

Returns descriptive information about an EKS Pod Identity association.

This action requires the ID of the association. You can get the ID from the response to the `CreatePodIdentityAssocation` for newly created associations. Or, you can list the IDs for associations with `ListPodIdentityAssociations` and filter the list by namespace or service account.

## Request Syntax
<a name="API_DescribePodIdentityAssociation_RequestSyntax"></a>

```
GET /clusters/{{name}}/pod-identity-associations/{{associationId}} HTTP/1.1
```

## URI Request Parameters
<a name="API_DescribePodIdentityAssociation_RequestParameters"></a>

The request uses the following URI parameters.

 ** [associationId](#API_DescribePodIdentityAssociation_RequestSyntax) **   <a name="AmazonEKS-DescribePodIdentityAssociation-request-uri-associationId"></a>
The ID of the association that you want the description of.  
Required: Yes

 ** [name](#API_DescribePodIdentityAssociation_RequestSyntax) **   <a name="AmazonEKS-DescribePodIdentityAssociation-request-uri-clusterName"></a>
The name of the cluster that the association is in.  
Required: Yes

## Request Body
<a name="API_DescribePodIdentityAssociation_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_DescribePodIdentityAssociation_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "association": { 
      "associationArn": "string",
      "associationId": "string",
      "clusterName": "string",
      "createdAt": number,
      "disableSessionTags": boolean,
      "externalId": "string",
      "modifiedAt": number,
      "namespace": "string",
      "ownerArn": "string",
      "policy": "string",
      "roleArn": "string",
      "serviceAccount": "string",
      "tags": { 
         "string" : "string" 
      },
      "targetRoleArn": "string"
   }
}
```

## Response Elements
<a name="API_DescribePodIdentityAssociation_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [association](#API_DescribePodIdentityAssociation_ResponseSyntax) **   <a name="AmazonEKS-DescribePodIdentityAssociation-response-association"></a>
The full description of the EKS Pod Identity association.  
Type: [PodIdentityAssociation](API_PodIdentityAssociation.md) object

## Errors
<a name="API_DescribePodIdentityAssociation_Errors"></a>

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
<a name="API_DescribePodIdentityAssociation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/eks-2017-11-01/DescribePodIdentityAssociation) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/eks-2017-11-01/DescribePodIdentityAssociation) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/eks-2017-11-01/DescribePodIdentityAssociation) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/eks-2017-11-01/DescribePodIdentityAssociation) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/eks-2017-11-01/DescribePodIdentityAssociation) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/eks-2017-11-01/DescribePodIdentityAssociation) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/eks-2017-11-01/DescribePodIdentityAssociation) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/eks-2017-11-01/DescribePodIdentityAssociation) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/eks-2017-11-01/DescribePodIdentityAssociation) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/eks-2017-11-01/DescribePodIdentityAssociation) 