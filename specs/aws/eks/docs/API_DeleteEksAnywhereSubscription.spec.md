---
id: "@specs/aws/eks/docs/API_DeleteEksAnywhereSubscription"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS DeleteEksAnywhereSubscription"
status: active
depends_on:
  - "@specs/aws/eks/meta"
---

# DeleteEksAnywhereSubscription

> **source:** AWS Documentation
> **spec:id:** @specs/aws/eks/docs/API_DeleteEksAnywhereSubscription
> **target_lang:** meta — documentation tier. ALL sections preserved.



# DeleteEksAnywhereSubscription
<a name="API_DeleteEksAnywhereSubscription"></a>

Deletes an expired or inactive subscription. Deleting inactive subscriptions removes them from the AWS Management Console view and from list/describe API responses. Subscriptions can only be cancelled within 7 days of creation and are cancelled by creating a ticket in the AWS Support Center. 

## Request Syntax
<a name="API_DeleteEksAnywhereSubscription_RequestSyntax"></a>

```
DELETE /eks-anywhere-subscriptions/{{id}} HTTP/1.1
```

## URI Request Parameters
<a name="API_DeleteEksAnywhereSubscription_RequestParameters"></a>

The request uses the following URI parameters.

 ** [id](#API_DeleteEksAnywhereSubscription_RequestSyntax) **   <a name="AmazonEKS-DeleteEksAnywhereSubscription-request-uri-id"></a>
The ID of the subscription.  
Required: Yes

## Request Body
<a name="API_DeleteEksAnywhereSubscription_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_DeleteEksAnywhereSubscription_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "subscription": { 
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
}
```

## Response Elements
<a name="API_DeleteEksAnywhereSubscription_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [subscription](#API_DeleteEksAnywhereSubscription_ResponseSyntax) **   <a name="AmazonEKS-DeleteEksAnywhereSubscription-response-subscription"></a>
The full description of the subscription to be deleted.  
Type: [EksAnywhereSubscription](API_EksAnywhereSubscription.md) object

## Errors
<a name="API_DeleteEksAnywhereSubscription_Errors"></a>

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
<a name="API_DeleteEksAnywhereSubscription_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/eks-2017-11-01/DeleteEksAnywhereSubscription) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/eks-2017-11-01/DeleteEksAnywhereSubscription) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/eks-2017-11-01/DeleteEksAnywhereSubscription) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/eks-2017-11-01/DeleteEksAnywhereSubscription) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/eks-2017-11-01/DeleteEksAnywhereSubscription) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/eks-2017-11-01/DeleteEksAnywhereSubscription) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/eks-2017-11-01/DeleteEksAnywhereSubscription) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/eks-2017-11-01/DeleteEksAnywhereSubscription) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/eks-2017-11-01/DeleteEksAnywhereSubscription) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/eks-2017-11-01/DeleteEksAnywhereSubscription) 