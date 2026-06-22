---
id: "@specs/aws/eks/docs/API_DeleteCluster"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS DeleteCluster"
status: active
depends_on:
  - "@specs/aws/eks/meta"
---

# DeleteCluster

> **source:** AWS Documentation
> **spec:id:** @specs/aws/eks/docs/API_DeleteCluster
> **target_lang:** meta — documentation tier. ALL sections preserved.



# DeleteCluster
<a name="API_DeleteCluster"></a>

Deletes an Amazon EKS cluster control plane.

If you have active services and ingress resources in your cluster that are associated with a load balancer, you must delete those services before deleting the cluster so that the load balancers are deleted properly. Otherwise, you can have orphaned resources in your VPC that prevent you from being able to delete the VPC. For more information, see [Deleting a cluster](https://docs.aws.amazon.com/eks/latest/userguide/delete-cluster.html) in the *Amazon EKS User Guide*.

If you have managed node groups or Fargate profiles attached to the cluster, you must delete them first. For more information, see `DeleteNodgroup` and `DeleteFargateProfile`.

## Request Syntax
<a name="API_DeleteCluster_RequestSyntax"></a>

```
DELETE /clusters/{{name}} HTTP/1.1
```

## URI Request Parameters
<a name="API_DeleteCluster_RequestParameters"></a>

The request uses the following URI parameters.

 ** [name](#API_DeleteCluster_RequestSyntax) **   <a name="AmazonEKS-DeleteCluster-request-uri-name"></a>
The name of the cluster to delete.  
Required: Yes

## Request Body
<a name="API_DeleteCluster_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_DeleteCluster_ResponseSyntax"></a>

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
<a name="API_DeleteCluster_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [cluster](#API_DeleteCluster_ResponseSyntax) **   <a name="AmazonEKS-DeleteCluster-response-cluster"></a>
The full description of the cluster to delete.  
Type: [Cluster](API_Cluster.md) object

## Errors
<a name="API_DeleteCluster_Errors"></a>

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

## Examples
<a name="API_DeleteCluster_Examples"></a>

In the following example or examples, the Authorization header contents (`AUTHPARAMS`) must be replaced with an AWS Signature Version 4 signature. For more information about creating these signatures, see [Signature Version 4 Signing Process](https://docs.aws.amazon.com/general/latest/gr/signature-version-4.html) in the *Amazon EKS General Reference*.

You need to learn how to sign HTTP requests only if you intend to manually create them. When you use the [AWS Command Line Interface (AWS CLI)](http://aws.amazon.com/cli/) or one of the [AWS SDKs](http://aws.amazon.com/tools/) to make requests to AWS, these tools automatically sign the requests for you with the access key that you specify when you configure the tools. When you use these tools, you don't need to learn how to sign requests yourself.

### Example
<a name="API_DeleteCluster_Example_1"></a>

The following example deletes a cluster called `my-cluster`.

#### Sample Request
<a name="API_DeleteCluster_Example_1_Request"></a>

```
DELETE /clusters/my-cluster HTTP/1.1
Host: eks.us-west-2.amazonaws.com
Accept-Encoding: identity
User-Agent: aws-cli/1.15.0 Python/3.6.5 Darwin/16.7.0 botocore/1.10.0
X-Amz-Date: 20180531T231840Z
Authorization: AUTHPARAMS
```

#### Sample Response
<a name="API_DeleteCluster_Example_1_Response"></a>

```
HTTP/1.1 200 OK
Date: Thu, 31 May 2018 23:18:41 GMT
Content-Type: application/json
Content-Length: 1895
x-amzn-RequestId: xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxx
x-amz-apigw-id: HxlgjH_rPHcF7ag=
X-Amzn-Trace-Id: Root=1-xxxxxxxxx-xxxxxxxxxxxxxxxxxxxxxxxx
Connection: keep-alive

{
    "cluster": {
        "name": "dev",
        "arn": "arn:aws:eks:us-west-2:012345678910:cluster/my-cluster",
        "createdAt": 1573244832.203,
        "version": "1.14",
        "endpoint": "https://A0DCCD80A04F01705DD065655C30CC3D.yl4.us-west-2.eks.amazonaws.com",
        "roleArn": "arn:aws:iam::012345678910:role/eksClusterRole",
        "resourcesVpcConfig": {
            "subnetIds": [
                "subnet-xxxxxxxxxxxxxxxxx",
                "subnet-yyyyyyyyyyyyyyyyy",
                "subnet-zzzzzzzzzzzzzzzzz"
            ],
            "securityGroupIds": [
                "sg-xxxxxxxxxxxxxxxxx"
            ],
            "clusterSecurityGroupId": "sg-yyyyyyyyyyyyyyyyy",
            "vpcId": "vpc-xxxxxxxxxxxxxxxxx",
            "endpointPublicAccess": true,
            "endpointPrivateAccess": false
        },
        "logging": {
            "clusterLogging": [
                {
                    "types": [
                        "api",
                        "audit",
                        "authenticator",
                        "controllerManager",
                        "scheduler"
                    ],
                    "enabled": false
                }
            ]
        },
        "identity": {
            "oidc": {
                "issuer": "https://oidc.eks.us-west-2.amazonaws.com/id/XXXXXXXXXXXXX097E4AC3A07B6B79B9C"
            }
        },
        "status": "DELETING",
        "certificateAuthority": {
            "data": "HERE_BE_SOME_CERT_DATA==="
        },
        "platformVersion": "eks.3",
        "tags": {}
    }
}
```

## See Also
<a name="API_DeleteCluster_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/eks-2017-11-01/DeleteCluster) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/eks-2017-11-01/DeleteCluster) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/eks-2017-11-01/DeleteCluster) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/eks-2017-11-01/DeleteCluster) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/eks-2017-11-01/DeleteCluster) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/eks-2017-11-01/DeleteCluster) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/eks-2017-11-01/DeleteCluster) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/eks-2017-11-01/DeleteCluster) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/eks-2017-11-01/DeleteCluster) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/eks-2017-11-01/DeleteCluster) 