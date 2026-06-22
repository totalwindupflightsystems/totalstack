---
id: "@specs/aws/eks/docs/API_DescribeCluster"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS DescribeCluster"
status: active
depends_on:
  - "@specs/aws/eks/meta"
---

# DescribeCluster

> **source:** AWS Documentation
> **spec:id:** @specs/aws/eks/docs/API_DescribeCluster
> **target_lang:** meta — documentation tier. ALL sections preserved.



# DescribeCluster
<a name="API_DescribeCluster"></a>

Describes an Amazon EKS cluster.

The API server endpoint and certificate authority data returned by this operation are required for `kubelet` and `kubectl` to communicate with your Kubernetes API server. For more information, see [Creating or updating a `kubeconfig` file for an Amazon EKS cluster](https://docs.aws.amazon.com/eks/latest/userguide/create-kubeconfig.html).

**Note**  
The API server endpoint and certificate authority data aren't available until the cluster reaches the `ACTIVE` state.

## Request Syntax
<a name="API_DescribeCluster_RequestSyntax"></a>

```
GET /clusters/{{name}} HTTP/1.1
```

## URI Request Parameters
<a name="API_DescribeCluster_RequestParameters"></a>

The request uses the following URI parameters.

 ** [name](#API_DescribeCluster_RequestSyntax) **   <a name="AmazonEKS-DescribeCluster-request-uri-name"></a>
The name of your cluster.  
Required: Yes

## Request Body
<a name="API_DescribeCluster_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_DescribeCluster_ResponseSyntax"></a>

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
<a name="API_DescribeCluster_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [cluster](#API_DescribeCluster_ResponseSyntax) **   <a name="AmazonEKS-DescribeCluster-response-cluster"></a>
The full description of your specified cluster.  
Type: [Cluster](API_Cluster.md) object

## Errors
<a name="API_DescribeCluster_Errors"></a>

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
<a name="API_DescribeCluster_Examples"></a>

In the following example or examples, the Authorization header contents (`AUTHPARAMS`) must be replaced with an AWS Signature Version 4 signature. For more information about creating these signatures, see [Signature Version 4 Signing Process](https://docs.aws.amazon.com/general/latest/gr/signature-version-4.html) in the *Amazon EKS General Reference*.

You need to learn how to sign HTTP requests only if you intend to manually create them. When you use the [AWS Command Line Interface (AWS CLI)](http://aws.amazon.com/cli/) or one of the [AWS SDKs](http://aws.amazon.com/tools/) to make requests to AWS, these tools automatically sign the requests for you with the access key that you specify when you configure the tools. When you use these tools, you don't need to learn how to sign requests yourself.

### Example
<a name="API_DescribeCluster_Example_1"></a>

The following example describes a cluster named `my-cluster`.

#### Sample Request
<a name="API_DescribeCluster_Example_1_Request"></a>

```
GET /clusters/my-cluster HTTP/1.1
Host: eks.us-west-2.amazonaws.com
Accept-Encoding: identity
User-Agent: aws-cli/1.16.120 Python/3.7.0 Darwin/18.2.0 botocore/1.12.110
X-Amz-Date: 20190322T161109Z
Authorization: AUTHPARAMS
```

#### Sample Response
<a name="API_DescribeCluster_Example_1_Response"></a>

```
HTTP/1.1 200 OK
Date: Fri, 22 Mar 2019 16:11:07 GMT
Content-Type: application/json
Content-Length: 682
x-amzn-RequestId: xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxx
x-amz-apigw-id: W85cPGkVvHcFa4g=
X-Amzn-Trace-Id: Root=1-xxxxxxxxx-xxxxxxxxxxxxxxxxxxxxxxxx
Connection: keep-alive

{
    "cluster": {
        "name": "my-cluster",
        "arn": "arn:aws:eks:us-west-2:012345678910:cluster/my-cluster",
        "createdAt": 1553270518.433,
        "version": "1.11",
        "endpoint": null,
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
            "vpcId": "vpc-xxxxxxxxxxxxxxxxx",
            "endpointPublicAccess": true,
            "endpointPrivateAccess": true
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
                "issuer": null
            }
        },
        "status": "CREATING",
        "certificateAuthority": {
            "data": null
        },
        "clientRequestToken": null,
        "platformVersion": "eks.2"
    }
}
```

## See Also
<a name="API_DescribeCluster_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/eks-2017-11-01/DescribeCluster) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/eks-2017-11-01/DescribeCluster) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/eks-2017-11-01/DescribeCluster) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/eks-2017-11-01/DescribeCluster) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/eks-2017-11-01/DescribeCluster) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/eks-2017-11-01/DescribeCluster) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/eks-2017-11-01/DescribeCluster) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/eks-2017-11-01/DescribeCluster) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/eks-2017-11-01/DescribeCluster) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/eks-2017-11-01/DescribeCluster) 