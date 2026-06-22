---
id: "@specs/aws/eks/docs/API_RegisterCluster"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS RegisterCluster"
status: active
depends_on:
  - "@specs/aws/eks/meta"
---

# RegisterCluster

> **source:** AWS Documentation
> **spec:id:** @specs/aws/eks/docs/API_RegisterCluster
> **target_lang:** meta — documentation tier. ALL sections preserved.



# RegisterCluster
<a name="API_RegisterCluster"></a>

Connects a Kubernetes cluster to the Amazon EKS control plane. 

Any Kubernetes cluster can be connected to the Amazon EKS control plane to view current information about the cluster and its nodes. 

Cluster connection requires two steps. First, send a [https://docs.aws.amazon.com/eks/latest/APIReference/API_RegisterClusterRequest.html](https://docs.aws.amazon.com/eks/latest/APIReference/API_RegisterClusterRequest.html) to add it to the Amazon EKS control plane.

Second, a [Manifest](https://amazon-eks.s3.us-west-2.amazonaws.com/eks-connector/manifests/eks-connector/latest/eks-connector.yaml) containing the `activationID` and `activationCode` must be applied to the Kubernetes cluster through it's native provider to provide visibility.

After the manifest is updated and applied, the connected cluster is visible to the Amazon EKS control plane. If the manifest isn't applied within three days, the connected cluster will no longer be visible and must be deregistered using `DeregisterCluster`.

## Request Syntax
<a name="API_RegisterCluster_RequestSyntax"></a>

```
POST /cluster-registrations HTTP/1.1
Content-type: application/json

{
   "clientRequestToken": "{{string}}",
   "connectorConfig": { 
      "provider": "{{string}}",
      "roleArn": "{{string}}"
   },
   "name": "{{string}}",
   "tags": { 
      "{{string}}" : "{{string}}" 
   }
}
```

## URI Request Parameters
<a name="API_RegisterCluster_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_RegisterCluster_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [clientRequestToken](#API_RegisterCluster_RequestSyntax) **   <a name="AmazonEKS-RegisterCluster-request-clientRequestToken"></a>
A unique, case-sensitive identifier that you provide to ensure the idempotency of the request.  
Type: String  
Required: No

 ** [connectorConfig](#API_RegisterCluster_RequestSyntax) **   <a name="AmazonEKS-RegisterCluster-request-connectorConfig"></a>
The configuration settings required to connect the Kubernetes cluster to the Amazon EKS control plane.  
Type: [ConnectorConfigRequest](API_ConnectorConfigRequest.md) object  
Required: Yes

 ** [name](#API_RegisterCluster_RequestSyntax) **   <a name="AmazonEKS-RegisterCluster-request-name"></a>
A unique name for this cluster in your AWS Region.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 100.  
Pattern: `^[0-9A-Za-z][A-Za-z0-9\-_]*`   
Required: Yes

 ** [tags](#API_RegisterCluster_RequestSyntax) **   <a name="AmazonEKS-RegisterCluster-request-tags"></a>
Metadata that assists with categorization and organization. Each tag consists of a key and an optional value. You define both. Tags don't propagate to any other cluster or AWS resources.  
Type: String to string map  
Map Entries: Maximum number of 50 items.  
Key Length Constraints: Minimum length of 1. Maximum length of 128.  
Value Length Constraints: Maximum length of 256.  
Required: No

## Response Syntax
<a name="API_RegisterCluster_ResponseSyntax"></a>

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
<a name="API_RegisterCluster_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [cluster](#API_RegisterCluster_ResponseSyntax) **   <a name="AmazonEKS-RegisterCluster-response-cluster"></a>
An object representing an Amazon EKS cluster.  
Type: [Cluster](API_Cluster.md) object

## Errors
<a name="API_RegisterCluster_Errors"></a>

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

 ** ResourcePropagationDelayException **   
Required resources (such as service-linked roles) were created and are still propagating. Retry later.    
 ** message **   
Required resources (such as service-linked roles) were created and are still propagating. Retry later.
HTTP Status Code: 428

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

## Examples
<a name="API_RegisterCluster_Examples"></a>

In the following example or examples, the Authorization header contents (`AUTHPARAMS`) must be replaced with an AWS Signature Version 4 signature. For more information about creating these signatures, see [Signature Version 4 Signing Process](https://docs.aws.amazon.com/general/latest/gr/signature-version-4.html) in the *Amazon EKS General Reference*.

You need to learn how to sign HTTP requests only if you intend to manually create them. When you use the [AWS Command Line Interface (AWS CLI)](http://aws.amazon.com/cli/) or one of the [AWS SDKs](http://aws.amazon.com/tools/) to make requests to AWS, these tools automatically sign the requests for you with the access key that you specify when you configure the tools. When you use these tools, you don't need to learn how to sign requests yourself.

### Example
<a name="API_RegisterCluster_Example_1"></a>

The following example connects a Kubernetes cluster named `my-api-created-external-cluster`.

#### Sample Request
<a name="API_RegisterCluster_Example_1_Request"></a>

```
POST /clusters HTTP/1.1
Host: eks.us-west-2.amazonaws.com
Accept-Encoding: identity
User-Agent: aws-cli/1.16.120 Python/3.7.0 Darwin/18.2.0 botocore/1.12.110
X-Amz-Date: 20190322T160158Z
Authorization: AUTHPARAMS
Content-Length: 368

{
    "name": "my-api-created-external-cluster",
    "connectorConfig": {
        "roleArn": "arn:aws:iam::ACCOUNT_ID:role/eks-connector-agent",
        "provider" : "OTHER"
    }
}
```

## See Also
<a name="API_RegisterCluster_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/eks-2017-11-01/RegisterCluster) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/eks-2017-11-01/RegisterCluster) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/eks-2017-11-01/RegisterCluster) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/eks-2017-11-01/RegisterCluster) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/eks-2017-11-01/RegisterCluster) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/eks-2017-11-01/RegisterCluster) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/eks-2017-11-01/RegisterCluster) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/eks-2017-11-01/RegisterCluster) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/eks-2017-11-01/RegisterCluster) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/eks-2017-11-01/RegisterCluster) 