---
id: "@specs/aws/eks/docs/API_CreateCapability"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS CreateCapability"
status: active
depends_on:
  - "@specs/aws/eks/meta"
---

# CreateCapability

> **source:** AWS Documentation
> **spec:id:** @specs/aws/eks/docs/API_CreateCapability
> **target_lang:** meta — documentation tier. ALL sections preserved.



# CreateCapability
<a name="API_CreateCapability"></a>

Creates a managed capability resource for an Amazon EKS cluster.

Capabilities provide fully managed capabilities to build and scale with Kubernetes. When you create a capability, Amazon EKSprovisions and manages the infrastructure required to run the capability outside of your cluster. This approach reduces operational overhead and preserves cluster resources.

You can only create one Capability of each type on a given Amazon EKS cluster. Valid types are Argo CD for declarative GitOps deployment, AWS Controllers for Kubernetes (ACK) for resource management, and Kube Resource Orchestrator (KRO) for Kubernetes custom resource orchestration.

For more information, see [EKS Capabilities](https://docs.aws.amazon.com/eks/latest/userguide/capabilities.html) in the *Amazon EKS User Guide*.

## Request Syntax
<a name="API_CreateCapability_RequestSyntax"></a>

```
POST /clusters/{{name}}/capabilities HTTP/1.1
Content-type: application/json

{
   "capabilityName": "{{string}}",
   "clientRequestToken": "{{string}}",
   "configuration": { 
      "argoCd": { 
         "awsIdc": { 
            "idcInstanceArn": "{{string}}",
            "idcRegion": "{{string}}"
         },
         "namespace": "{{string}}",
         "networkAccess": { 
            "vpceIds": [ "{{string}}" ]
         },
         "rbacRoleMappings": [ 
            { 
               "identities": [ 
                  { 
                     "id": "{{string}}",
                     "type": "{{string}}"
                  }
               ],
               "role": "{{string}}"
            }
         ]
      }
   },
   "deletePropagationPolicy": "{{string}}",
   "roleArn": "{{string}}",
   "tags": { 
      "{{string}}" : "{{string}}" 
   },
   "type": "{{string}}"
}
```

## URI Request Parameters
<a name="API_CreateCapability_RequestParameters"></a>

The request uses the following URI parameters.

 ** [name](#API_CreateCapability_RequestSyntax) **   <a name="AmazonEKS-CreateCapability-request-uri-clusterName"></a>
The name of the Amazon EKS cluster where you want to create the capability.  
Required: Yes

## Request Body
<a name="API_CreateCapability_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [capabilityName](#API_CreateCapability_RequestSyntax) **   <a name="AmazonEKS-CreateCapability-request-capabilityName"></a>
A unique name for the capability. The name must be unique within your cluster and can contain alphanumeric characters, hyphens, and underscores.  
Type: String  
Required: Yes

 ** [clientRequestToken](#API_CreateCapability_RequestSyntax) **   <a name="AmazonEKS-CreateCapability-request-clientRequestToken"></a>
A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. This token is valid for 24 hours after creation. If you retry a request with the same client request token and the same parameters after the original request has completed successfully, the result of the original request is returned.  
Type: String  
Required: No

 ** [configuration](#API_CreateCapability_RequestSyntax) **   <a name="AmazonEKS-CreateCapability-request-configuration"></a>
The configuration settings for the capability. The structure of this object varies depending on the capability type. For Argo CD capabilities, you can configure IAM Identity CenterIAM; Identity Center integration, RBAC role mappings, and network access settings.  
Type: [CapabilityConfigurationRequest](API_CapabilityConfigurationRequest.md) object  
Required: No

 ** [deletePropagationPolicy](#API_CreateCapability_RequestSyntax) **   <a name="AmazonEKS-CreateCapability-request-deletePropagationPolicy"></a>
Specifies how Kubernetes resources managed by the capability should be handled when the capability is deleted. Currently, the only supported value is `RETAIN` which retains all Kubernetes resources managed by the capability when the capability is deleted.  
Because resources are retained, all Kubernetes resources created by the capability should be deleted from the cluster before deleting the capability itself. After the capability is deleted, these resources become difficult to manage because the controller is no longer available.  
Type: String  
Valid Values: `RETAIN`   
Required: Yes

 ** [roleArn](#API_CreateCapability_RequestSyntax) **   <a name="AmazonEKS-CreateCapability-request-roleArn"></a>
The Amazon Resource Name (ARN) of the IAM role that the capability uses to interact with AWS services. This role must have a trust policy that allows the EKS service principal to assume it, and it must have the necessary permissions for the capability type you're creating.  
For ACK capabilities, the role needs permissions to manage the resources you want to control through Kubernetes. For Argo CD capabilities, the role needs permissions to access Git repositories and Secrets Manager. For KRO capabilities, the role needs permissions based on the resources you'll be orchestrating.  
Type: String  
Required: Yes

 ** [tags](#API_CreateCapability_RequestSyntax) **   <a name="AmazonEKS-CreateCapability-request-tags"></a>
The metadata that you apply to a resource to help you categorize and organize them. Each tag consists of a key and an optional value. You define them.  
The following basic restrictions apply to tags:  
+ Maximum number of tags per resource – 50
+ For each resource, each tag key must be unique, and each tag key can have only one value.
+ Maximum key length – 128 Unicode characters in UTF-8
+ Maximum value length – 256 Unicode characters in UTF-8
+ If your tagging schema is used across multiple services and resources, remember that other services may have restrictions on allowed characters. Generally allowed characters are: letters, numbers, and spaces representable in UTF-8, and the following characters: \+ - = . \_ : / @.
+ Tag keys and values are case-sensitive.
+ Do not use `aws:`, `AWS:`, or any upper or lowercase combination of such as a prefix for either keys or values as it is reserved for AWS use. You cannot edit or delete tag keys or values with this prefix. Tags with this prefix do not count against your tags per resource limit.
Type: String to string map  
Map Entries: Maximum number of 50 items.  
Key Length Constraints: Minimum length of 1. Maximum length of 128.  
Value Length Constraints: Maximum length of 256.  
Required: No

 ** [type](#API_CreateCapability_RequestSyntax) **   <a name="AmazonEKS-CreateCapability-request-type"></a>
The type of capability to create. Valid values are:  
+  `ACK` – AWS Controllers for Kubernetes (ACK), which lets you manage resources directly from Kubernetes.
+  `ARGOCD` – Argo CD for GitOps-based continuous delivery.
+  `KRO` – Kube Resource Orchestrator (KRO) for composing and managing custom Kubernetes resources.
Type: String  
Valid Values: `ACK | KRO | ARGOCD`   
Required: Yes

## Response Syntax
<a name="API_CreateCapability_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "capability": { 
      "arn": "string",
      "capabilityName": "string",
      "clusterName": "string",
      "configuration": { 
         "argoCd": { 
            "awsIdc": { 
               "idcInstanceArn": "string",
               "idcManagedApplicationArn": "string",
               "idcRegion": "string"
            },
            "namespace": "string",
            "networkAccess": { 
               "vpceIds": [ "string" ]
            },
            "rbacRoleMappings": [ 
               { 
                  "identities": [ 
                     { 
                        "id": "string",
                        "type": "string"
                     }
                  ],
                  "role": "string"
               }
            ],
            "serverUrl": "string"
         }
      },
      "createdAt": number,
      "deletePropagationPolicy": "string",
      "health": { 
         "issues": [ 
            { 
               "code": "string",
               "message": "string"
            }
         ]
      },
      "modifiedAt": number,
      "roleArn": "string",
      "status": "string",
      "tags": { 
         "string" : "string" 
      },
      "type": "string",
      "version": "string"
   }
}
```

## Response Elements
<a name="API_CreateCapability_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [capability](#API_CreateCapability_ResponseSyntax) **   <a name="AmazonEKS-CreateCapability-response-capability"></a>
An object containing information about the newly created capability, including its name, ARN, status, and configuration.  
Type: [Capability](API_Capability.md) object

## Errors
<a name="API_CreateCapability_Errors"></a>

For information about the errors that are common to all actions, see [Common Errors](CommonErrors.md).

 ** AccessDeniedException **   
You don't have permissions to perform the requested operation. The [IAM principal](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_terms-and-concepts.html) making the request must have at least one IAM permissions policy attached that grants the required permissions. For more information, see [Access management](https://docs.aws.amazon.com/IAM/latest/UserGuide/access.html) in the *IAM User Guide*.     
 ** message **   
You do not have sufficient access to perform this action.
HTTP Status Code: 403

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

 ** ResourceLimitExceededException **   
You have encountered a service limit on the specified resource.    
 ** clusterName **   
The Amazon EKS cluster associated with the exception.  
 ** message **   
The Amazon EKS message associated with the exception.  
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

 ** ThrottlingException **   
The request or operation couldn't be performed because a service is throttling requests.    
 ** clusterName **   
The Amazon EKS cluster associated with the exception.
HTTP Status Code: 429

## See Also
<a name="API_CreateCapability_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/eks-2017-11-01/CreateCapability) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/eks-2017-11-01/CreateCapability) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/eks-2017-11-01/CreateCapability) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/eks-2017-11-01/CreateCapability) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/eks-2017-11-01/CreateCapability) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/eks-2017-11-01/CreateCapability) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/eks-2017-11-01/CreateCapability) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/eks-2017-11-01/CreateCapability) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/eks-2017-11-01/CreateCapability) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/eks-2017-11-01/CreateCapability) 