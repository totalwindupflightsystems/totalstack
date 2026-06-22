---
id: "@specs/aws/eks/docs/API_AssociateIdentityProviderConfig"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS AssociateIdentityProviderConfig"
status: active
depends_on:
  - "@specs/aws/eks/meta"
---

# AssociateIdentityProviderConfig

> **source:** AWS Documentation
> **spec:id:** @specs/aws/eks/docs/API_AssociateIdentityProviderConfig
> **target_lang:** meta — documentation tier. ALL sections preserved.



# AssociateIdentityProviderConfig
<a name="API_AssociateIdentityProviderConfig"></a>

Associates an identity provider configuration to a cluster.

If you want to authenticate identities using an identity provider, you can create an identity provider configuration and associate it to your cluster. After configuring authentication to your cluster you can create Kubernetes `Role` and `ClusterRole` objects, assign permissions to them, and then bind them to the identities using Kubernetes `RoleBinding` and `ClusterRoleBinding` objects. For more information see [Using RBAC Authorization](https://kubernetes.io/docs/reference/access-authn-authz/rbac/) in the Kubernetes documentation.

## Request Syntax
<a name="API_AssociateIdentityProviderConfig_RequestSyntax"></a>

```
POST /clusters/{{name}}/identity-provider-configs/associate HTTP/1.1
Content-type: application/json

{
   "clientRequestToken": "{{string}}",
   "oidc": { 
      "clientId": "{{string}}",
      "groupsClaim": "{{string}}",
      "groupsPrefix": "{{string}}",
      "identityProviderConfigName": "{{string}}",
      "issuerUrl": "{{string}}",
      "requiredClaims": { 
         "{{string}}" : "{{string}}" 
      },
      "usernameClaim": "{{string}}",
      "usernamePrefix": "{{string}}"
   },
   "tags": { 
      "{{string}}" : "{{string}}" 
   }
}
```

## URI Request Parameters
<a name="API_AssociateIdentityProviderConfig_RequestParameters"></a>

The request uses the following URI parameters.

 ** [name](#API_AssociateIdentityProviderConfig_RequestSyntax) **   <a name="AmazonEKS-AssociateIdentityProviderConfig-request-uri-clusterName"></a>
The name of your cluster.  
Required: Yes

## Request Body
<a name="API_AssociateIdentityProviderConfig_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [clientRequestToken](#API_AssociateIdentityProviderConfig_RequestSyntax) **   <a name="AmazonEKS-AssociateIdentityProviderConfig-request-clientRequestToken"></a>
A unique, case-sensitive identifier that you provide to ensure the idempotency of the request.  
Type: String  
Required: No

 ** [oidc](#API_AssociateIdentityProviderConfig_RequestSyntax) **   <a name="AmazonEKS-AssociateIdentityProviderConfig-request-oidc"></a>
An object representing an OpenID Connect (OIDC) identity provider configuration.  
Type: [OidcIdentityProviderConfigRequest](API_OidcIdentityProviderConfigRequest.md) object  
Required: Yes

 ** [tags](#API_AssociateIdentityProviderConfig_RequestSyntax) **   <a name="AmazonEKS-AssociateIdentityProviderConfig-request-tags"></a>
Metadata that assists with categorization and organization. Each tag consists of a key and an optional value. You define both. Tags don't propagate to any other cluster or AWS resources.  
Type: String to string map  
Map Entries: Maximum number of 50 items.  
Key Length Constraints: Minimum length of 1. Maximum length of 128.  
Value Length Constraints: Maximum length of 256.  
Required: No

## Response Syntax
<a name="API_AssociateIdentityProviderConfig_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "tags": { 
      "string" : "string" 
   },
   "update": { 
      "createdAt": number,
      "errors": [ 
         { 
            "errorCode": "string",
            "errorMessage": "string",
            "resourceIds": [ "string" ]
         }
      ],
      "id": "string",
      "params": [ 
         { 
            "type": "string",
            "value": "string"
         }
      ],
      "status": "string",
      "type": "string"
   }
}
```

## Response Elements
<a name="API_AssociateIdentityProviderConfig_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [tags](#API_AssociateIdentityProviderConfig_ResponseSyntax) **   <a name="AmazonEKS-AssociateIdentityProviderConfig-response-tags"></a>
The tags for the resource.  
Type: String to string map  
Map Entries: Maximum number of 50 items.  
Key Length Constraints: Minimum length of 1. Maximum length of 128.  
Value Length Constraints: Maximum length of 256.

 ** [update](#API_AssociateIdentityProviderConfig_ResponseSyntax) **   <a name="AmazonEKS-AssociateIdentityProviderConfig-response-update"></a>
An object representing an asynchronous update.  
Type: [Update](API_Update.md) object

## Errors
<a name="API_AssociateIdentityProviderConfig_Errors"></a>

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

 ** ResourceInUseException **   
The specified resource is in use.    
 ** addonName **   
The specified add-on name is in use.  
 ** clusterName **   
The Amazon EKS cluster associated with the exception.  
 ** message **   
The Amazon EKS message associated with the exception.  
 ** nodegroupName **   
The Amazon EKS managed node group associated with the exception.
HTTP Status Code: 409

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

 ** ThrottlingException **   
The request or operation couldn't be performed because a service is throttling requests.    
 ** clusterName **   
The Amazon EKS cluster associated with the exception.
HTTP Status Code: 429

## See Also
<a name="API_AssociateIdentityProviderConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/eks-2017-11-01/AssociateIdentityProviderConfig) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/eks-2017-11-01/AssociateIdentityProviderConfig) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/eks-2017-11-01/AssociateIdentityProviderConfig) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/eks-2017-11-01/AssociateIdentityProviderConfig) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/eks-2017-11-01/AssociateIdentityProviderConfig) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/eks-2017-11-01/AssociateIdentityProviderConfig) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/eks-2017-11-01/AssociateIdentityProviderConfig) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/eks-2017-11-01/AssociateIdentityProviderConfig) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/eks-2017-11-01/AssociateIdentityProviderConfig) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/eks-2017-11-01/AssociateIdentityProviderConfig) 