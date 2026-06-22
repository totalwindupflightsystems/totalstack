---
id: "@specs/aws/eks/docs/API_DescribeIdentityProviderConfig"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS DescribeIdentityProviderConfig"
status: active
depends_on:
  - "@specs/aws/eks/meta"
---

# DescribeIdentityProviderConfig

> **source:** AWS Documentation
> **spec:id:** @specs/aws/eks/docs/API_DescribeIdentityProviderConfig
> **target_lang:** meta — documentation tier. ALL sections preserved.



# DescribeIdentityProviderConfig
<a name="API_DescribeIdentityProviderConfig"></a>

Describes an identity provider configuration.

## Request Syntax
<a name="API_DescribeIdentityProviderConfig_RequestSyntax"></a>

```
POST /clusters/{{name}}/identity-provider-configs/describe HTTP/1.1
Content-type: application/json

{
   "identityProviderConfig": { 
      "name": "{{string}}",
      "type": "{{string}}"
   }
}
```

## URI Request Parameters
<a name="API_DescribeIdentityProviderConfig_RequestParameters"></a>

The request uses the following URI parameters.

 ** [name](#API_DescribeIdentityProviderConfig_RequestSyntax) **   <a name="AmazonEKS-DescribeIdentityProviderConfig-request-uri-clusterName"></a>
The name of your cluster.  
Required: Yes

## Request Body
<a name="API_DescribeIdentityProviderConfig_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [identityProviderConfig](#API_DescribeIdentityProviderConfig_RequestSyntax) **   <a name="AmazonEKS-DescribeIdentityProviderConfig-request-identityProviderConfig"></a>
An object representing an identity provider configuration.  
Type: [IdentityProviderConfig](API_IdentityProviderConfig.md) object  
Required: Yes

## Response Syntax
<a name="API_DescribeIdentityProviderConfig_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "identityProviderConfig": { 
      "oidc": { 
         "clientId": "string",
         "clusterName": "string",
         "groupsClaim": "string",
         "groupsPrefix": "string",
         "identityProviderConfigArn": "string",
         "identityProviderConfigName": "string",
         "issuerUrl": "string",
         "requiredClaims": { 
            "string" : "string" 
         },
         "status": "string",
         "tags": { 
            "string" : "string" 
         },
         "usernameClaim": "string",
         "usernamePrefix": "string"
      }
   }
}
```

## Response Elements
<a name="API_DescribeIdentityProviderConfig_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [identityProviderConfig](#API_DescribeIdentityProviderConfig_ResponseSyntax) **   <a name="AmazonEKS-DescribeIdentityProviderConfig-response-identityProviderConfig"></a>
The object that represents an OpenID Connect (OIDC) identity provider configuration.  
Type: [IdentityProviderConfigResponse](API_IdentityProviderConfigResponse.md) object

## Errors
<a name="API_DescribeIdentityProviderConfig_Errors"></a>

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

 ** ServiceUnavailableException **   
The service is unavailable. Back off and retry the operation.    
 ** message **   
The request has failed due to a temporary failure of the server.
HTTP Status Code: 503

## See Also
<a name="API_DescribeIdentityProviderConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/eks-2017-11-01/DescribeIdentityProviderConfig) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/eks-2017-11-01/DescribeIdentityProviderConfig) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/eks-2017-11-01/DescribeIdentityProviderConfig) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/eks-2017-11-01/DescribeIdentityProviderConfig) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/eks-2017-11-01/DescribeIdentityProviderConfig) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/eks-2017-11-01/DescribeIdentityProviderConfig) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/eks-2017-11-01/DescribeIdentityProviderConfig) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/eks-2017-11-01/DescribeIdentityProviderConfig) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/eks-2017-11-01/DescribeIdentityProviderConfig) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/eks-2017-11-01/DescribeIdentityProviderConfig) 