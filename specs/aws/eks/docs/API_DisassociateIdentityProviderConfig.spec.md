---
id: "@specs/aws/eks/docs/API_DisassociateIdentityProviderConfig"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS DisassociateIdentityProviderConfig"
status: active
depends_on:
  - "@specs/aws/eks/meta"
---

# DisassociateIdentityProviderConfig

> **source:** AWS Documentation
> **spec:id:** @specs/aws/eks/docs/API_DisassociateIdentityProviderConfig
> **target_lang:** meta — documentation tier. ALL sections preserved.



# DisassociateIdentityProviderConfig
<a name="API_DisassociateIdentityProviderConfig"></a>

Disassociates an identity provider configuration from a cluster.

If you disassociate an identity provider from your cluster, users included in the provider can no longer access the cluster. However, you can still access the cluster with IAM principals.

## Request Syntax
<a name="API_DisassociateIdentityProviderConfig_RequestSyntax"></a>

```
POST /clusters/{{name}}/identity-provider-configs/disassociate HTTP/1.1
Content-type: application/json

{
   "clientRequestToken": "{{string}}",
   "identityProviderConfig": { 
      "name": "{{string}}",
      "type": "{{string}}"
   }
}
```

## URI Request Parameters
<a name="API_DisassociateIdentityProviderConfig_RequestParameters"></a>

The request uses the following URI parameters.

 ** [name](#API_DisassociateIdentityProviderConfig_RequestSyntax) **   <a name="AmazonEKS-DisassociateIdentityProviderConfig-request-uri-clusterName"></a>
The name of your cluster.  
Required: Yes

## Request Body
<a name="API_DisassociateIdentityProviderConfig_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [clientRequestToken](#API_DisassociateIdentityProviderConfig_RequestSyntax) **   <a name="AmazonEKS-DisassociateIdentityProviderConfig-request-clientRequestToken"></a>
A unique, case-sensitive identifier that you provide to ensure the idempotency of the request.  
Type: String  
Required: No

 ** [identityProviderConfig](#API_DisassociateIdentityProviderConfig_RequestSyntax) **   <a name="AmazonEKS-DisassociateIdentityProviderConfig-request-identityProviderConfig"></a>
An object representing an identity provider configuration.  
Type: [IdentityProviderConfig](API_IdentityProviderConfig.md) object  
Required: Yes

## Response Syntax
<a name="API_DisassociateIdentityProviderConfig_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
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
<a name="API_DisassociateIdentityProviderConfig_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [update](#API_DisassociateIdentityProviderConfig_ResponseSyntax) **   <a name="AmazonEKS-DisassociateIdentityProviderConfig-response-update"></a>
An object representing an asynchronous update.  
Type: [Update](API_Update.md) object

## Errors
<a name="API_DisassociateIdentityProviderConfig_Errors"></a>

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

## Examples
<a name="API_DisassociateIdentityProviderConfig_Examples"></a>

In the following example or examples, the Authorization header contents (`AUTHPARAMS`) must be replaced with an AWS Signature Version 4 signature. For more information about creating these signatures, see [Signature Version 4 Signing Process](https://docs.aws.amazon.com/general/latest/gr/signature-version-4.html) in the *Amazon EKS General Reference*.

You need to learn how to sign HTTP requests only if you intend to manually create them. When you use the [AWS Command Line Interface (AWS CLI)](http://aws.amazon.com/cli/) or one of the [AWS SDKs](http://aws.amazon.com/tools/) to make requests to AWS, these tools automatically sign the requests for you with the access key that you specify when you configure the tools. When you use these tools, you don't need to learn how to sign requests yourself.

### Example
<a name="API_DisassociateIdentityProviderConfig_Example_1"></a>

The following example disassociates an OIDC identity provider named `my-config` from a cluster.

#### Sample Request
<a name="API_DisassociateIdentityProviderConfig_Example_1_Request"></a>

```
POST /clusters/my-cluster/identity-provider-configs/disassociate HTTP/1.1
Host: eks.us-west-2.amazonaws.com
Accept-Encoding: identity
User-Agent: aws-cli/1.16.298 Python/3.6.0 Windows/10 botocore/1.13.34
X-Amz-Date: 20201215T211826Z
Authorization: AUTHPARAMS
Content-Length: 127

{
	"identityProviderConfig": {
		"type": "oidc",
		"name": "my-config"
	},
	"clientRequestToken": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx"
}
```

#### Sample Response
<a name="API_DisassociateIdentityProviderConfig_Example_1_Response"></a>

```
HTTP/1.1 200 OK
Date: Tue, 15 Dec 2020 21:18:27 GMT
Content-Type: application/json
Content-Length: 297
x-amzn-RequestId: xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxx
x-amz-apigw-id: XnM1dE8TvHcFn8Q=
X-Amzn-Trace-Id: Root=1-xxxxxxxxx-xxxxxxxxxxxxxxxxxxxxxxxx
Connection: keep-alive

{
  "update" : {
    "id" : "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
    "status" : "InProgress",
    "type" : "DisassociateIdentityProviderConfig",
    "params" : [ {
      "type" : "IdentityProviderConfig",
      "value" : "[]"
    } ],
    "createdAt" : 1.60806710785E9,
    "errors" : [ ]
  }
}
```

## See Also
<a name="API_DisassociateIdentityProviderConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/eks-2017-11-01/DisassociateIdentityProviderConfig) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/eks-2017-11-01/DisassociateIdentityProviderConfig) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/eks-2017-11-01/DisassociateIdentityProviderConfig) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/eks-2017-11-01/DisassociateIdentityProviderConfig) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/eks-2017-11-01/DisassociateIdentityProviderConfig) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/eks-2017-11-01/DisassociateIdentityProviderConfig) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/eks-2017-11-01/DisassociateIdentityProviderConfig) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/eks-2017-11-01/DisassociateIdentityProviderConfig) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/eks-2017-11-01/DisassociateIdentityProviderConfig) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/eks-2017-11-01/DisassociateIdentityProviderConfig) 