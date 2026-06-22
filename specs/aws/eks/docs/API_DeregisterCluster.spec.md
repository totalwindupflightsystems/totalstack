---
id: "@specs/aws/eks/docs/API_DeregisterCluster"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS DeregisterCluster"
status: active
depends_on:
  - "@specs/aws/eks/meta"
---

# DeregisterCluster

> **source:** AWS Documentation
> **spec:id:** @specs/aws/eks/docs/API_DeregisterCluster
> **target_lang:** meta — documentation tier. ALL sections preserved.



# DeregisterCluster
<a name="API_DeregisterCluster"></a>

Deregisters a connected cluster to remove it from the Amazon EKS control plane.

A connected cluster is a Kubernetes cluster that you've connected to your control plane using the [Amazon EKS Connector](https://docs.aws.amazon.com/eks/latest/userguide/eks-connector.html).

## Request Syntax
<a name="API_DeregisterCluster_RequestSyntax"></a>

```
DELETE /cluster-registrations/{{name}} HTTP/1.1
```

## URI Request Parameters
<a name="API_DeregisterCluster_RequestParameters"></a>

The request uses the following URI parameters.

 ** [name](#API_DeregisterCluster_RequestSyntax) **   <a name="AmazonEKS-DeregisterCluster-request-uri-name"></a>
The name of the connected cluster to deregister.  
Required: Yes

## Request Body
<a name="API_DeregisterCluster_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_DeregisterCluster_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "cluster": { 
      "accessConfig": { 
         "authenticationMode": "string",
         "bootstrapClusterCreatorAdminPermissions": boolean
      },
      "arn": "string",
      "certificateAuthority": { 
         "data": "string"
      },
      "clientRequestToken": "string",
      "computeConfig": { 
         "enabled": boolean,
         "nodePools": [ "string" ],
         "nodeRoleArn": "string"
      },
      "connectorConfig": { 
         "activationCode": "string",
         "activationExpiry": number,
         "activationId": "string",
         "provider": "string",
         "roleArn": "string"
      },
      "controlPlaneScalingConfig": { 
         "tier": "string"
      },
      "createdAt": number,
      "deletionProtection": boolean,
      "encryptionConfig": [ 
         { 
            "provider": { 
               "keyArn": "string"
            },
            "resources": [ "string" ]
         }
      ],
      "endpoint": "string",
      "health": { 
         "issues": [ 
            { 
               "code": "string",
               "message": "string",
               "resourceIds": [ "string" ]
            }
         ]
      },
      "id": "string",
      "identity": { 
         "oidc": { 
            "issuer": "string"
         }
      },
      "kubernetesNetworkConfig": { 
         "elasticLoadBalancing": { 
            "enabled": boolean
         },
         "ipFamily": "string",
         "serviceIpv4Cidr": "string",
         "serviceIpv6Cidr": "string"
      },
      "logging": { 
         "clusterLogging": [ 
            { 
               "enabled": boolean,
               "types": [ "string" ]
            }
         ]
      },
      "name": "string",
      "outpostConfig": { 
         "controlPlaneInstanceType": "string",
         "controlPlanePlacement": { 
            "groupName": "string",
            "spreadLevel": "string"
         },
         "etcdInstanceType": "string",
         "etcdPlacement": { 
            "spreadLevel": "string"
         },
         "outpostArns": [ "string" ]
      },
      "platformVersion": "string",
      "remoteNetworkConfig": { 
         "remoteNodeNetworks": [ 
            { 
               "cidrs": [ "string" ]
            }
         ],
         "remotePodNetworks": [ 
            { 
               "cidrs": [ "string" ]
            }
         ]
      },
      "resourcesVpcConfig": { 
         "clusterSecurityGroupId": "string",
         "controlPlaneEgressMode": "string",
         "endpointPrivateAccess": boolean,
         "endpointPublicAccess": boolean,
         "publicAccessCidrs": [ "string" ],
         "securityGroupIds": [ "string" ],
         "subnetIds": [ "string" ],
         "vpcId": "string"
      },
      "roleArn": "string",
      "status": "string",
      "storageConfig": { 
         "blockStorage": { 
            "enabled": boolean
         }
      },
      "tags": { 
         "string" : "string" 
      },
      "upgradePolicy": { 
         "supportType": "string"
      },
      "version": "string",
      "zonalShiftConfig": { 
         "enabled": boolean
      }
   }
}
```

## Response Elements
<a name="API_DeregisterCluster_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [cluster](#API_DeregisterCluster_ResponseSyntax) **   <a name="AmazonEKS-DeregisterCluster-response-cluster"></a>
An object representing an Amazon EKS cluster.  
Type: [Cluster](API_Cluster.md) object

## Errors
<a name="API_DeregisterCluster_Errors"></a>

For information about the errors that are common to all actions, see [Common Errors](CommonErrors.md).

 ** AccessDeniedException **   
You don't have permissions to perform the requested operation. The [IAM principal](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_terms-and-concepts.html) making the request must have at least one IAM permissions policy attached that grants the required permissions. For more information, see [Access management](https://docs.aws.amazon.com/IAM/latest/UserGuide/access.html) in the *IAM User Guide*.     
 ** message **   
You do not have sufficient access to perform this action.
HTTP Status Code: 403

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

 ** ServiceUnavailableException **   
The service is unavailable. Back off and retry the operation.    
 ** message **   
The request has failed due to a temporary failure of the server.
HTTP Status Code: 503

## See Also
<a name="API_DeregisterCluster_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/eks-2017-11-01/DeregisterCluster) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/eks-2017-11-01/DeregisterCluster) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/eks-2017-11-01/DeregisterCluster) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/eks-2017-11-01/DeregisterCluster) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/eks-2017-11-01/DeregisterCluster) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/eks-2017-11-01/DeregisterCluster) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/eks-2017-11-01/DeregisterCluster) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/eks-2017-11-01/DeregisterCluster) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/eks-2017-11-01/DeregisterCluster) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/eks-2017-11-01/DeregisterCluster) 