---
id: "@specs/aws/eks/docs/API_CreateCluster"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS CreateCluster"
status: active
depends_on:
  - "@specs/aws/eks/meta"
---

# CreateCluster

> **source:** AWS Documentation
> **spec:id:** @specs/aws/eks/docs/API_CreateCluster
> **target_lang:** meta — documentation tier. ALL sections preserved.



# CreateCluster
<a name="API_CreateCluster"></a>

Creates an Amazon EKS control plane.

The Amazon EKS control plane consists of control plane instances that run the Kubernetes software, such as `etcd` and the API server. The control plane runs in an account managed by AWS, and the Kubernetes API is exposed by the Amazon EKS API server endpoint. Each Amazon EKS cluster control plane is single tenant and unique. It runs on its own set of Amazon EC2 instances.

The cluster control plane is provisioned across multiple Availability Zones and fronted by an Elastic Load Balancing Network Load Balancer. Amazon EKS also provisions elastic network interfaces in your VPC subnets to provide connectivity from the control plane instances to the nodes (for example, to support `kubectl exec`, `logs`, and `proxy` data flows).

Amazon EKS nodes run in your AWS account and connect to your cluster's control plane over the Kubernetes API server endpoint and a certificate file that is created for your cluster.

You can use the `endpointPublicAccess` and `endpointPrivateAccess` parameters to enable or disable public and private access to your cluster's Kubernetes API server endpoint. By default, public access is enabled, and private access is disabled. The endpoint domain name and IP address family depends on the value of the `ipFamily` for the cluster. For more information, see [Amazon EKS Cluster Endpoint Access Control](https://docs.aws.amazon.com/eks/latest/userguide/cluster-endpoint.html) in the * *Amazon EKS User Guide* *. 

You can use the `logging` parameter to enable or disable exporting the Kubernetes control plane logs for your cluster to CloudWatch Logs. By default, cluster control plane logs aren't exported to CloudWatch Logs. For more information, see [Amazon EKS Cluster Control Plane Logs](https://docs.aws.amazon.com/eks/latest/userguide/control-plane-logs.html) in the * *Amazon EKS User Guide* *.

**Note**  
CloudWatch Logs ingestion, archive storage, and data scanning rates apply to exported control plane logs. For more information, see [CloudWatch Pricing](http://aws.amazon.com/cloudwatch/pricing/).

In most cases, it takes several minutes to create a cluster. After you create an Amazon EKS cluster, you must configure your Kubernetes tooling to communicate with the API server and launch nodes into your cluster. For more information, see [Allowing users to access your cluster](https://docs.aws.amazon.com/eks/latest/userguide/cluster-auth.html) and [Launching Amazon EKS nodes](https://docs.aws.amazon.com/eks/latest/userguide/launch-workers.html) in the *Amazon EKS User Guide*.

## Request Syntax
<a name="API_CreateCluster_RequestSyntax"></a>

```
POST /clusters HTTP/1.1
Content-type: application/json

{
   "accessConfig": { 
      "authenticationMode": "{{string}}",
      "bootstrapClusterCreatorAdminPermissions": {{boolean}}
   },
   "bootstrapSelfManagedAddons": {{boolean}},
   "clientRequestToken": "{{string}}",
   "computeConfig": { 
      "enabled": {{boolean}},
      "nodePools": [ "{{string}}" ],
      "nodeRoleArn": "{{string}}"
   },
   "controlPlaneScalingConfig": { 
      "tier": "{{string}}"
   },
   "deletionProtection": {{boolean}},
   "encryptionConfig": [ 
      { 
         "provider": { 
            "keyArn": "{{string}}"
         },
         "resources": [ "{{string}}" ]
      }
   ],
   "kubernetesNetworkConfig": { 
      "elasticLoadBalancing": { 
         "enabled": {{boolean}}
      },
      "ipFamily": "{{string}}",
      "serviceIpv4Cidr": "{{string}}"
   },
   "logging": { 
      "clusterLogging": [ 
         { 
            "enabled": {{boolean}},
            "types": [ "{{string}}" ]
         }
      ]
   },
   "name": "{{string}}",
   "outpostConfig": { 
      "controlPlaneInstanceType": "{{string}}",
      "controlPlanePlacement": { 
         "groupName": "{{string}}",
         "spreadLevel": "{{string}}"
      },
      "etcdInstanceType": "{{string}}",
      "etcdPlacement": { 
         "spreadLevel": "{{string}}"
      },
      "outpostArns": [ "{{string}}" ]
   },
   "remoteNetworkConfig": { 
      "remoteNodeNetworks": [ 
         { 
            "cidrs": [ "{{string}}" ]
         }
      ],
      "remotePodNetworks": [ 
         { 
            "cidrs": [ "{{string}}" ]
         }
      ]
   },
   "resourcesVpcConfig": { 
      "controlPlaneEgressMode": "{{string}}",
      "endpointPrivateAccess": {{boolean}},
      "endpointPublicAccess": {{boolean}},
      "publicAccessCidrs": [ "{{string}}" ],
      "securityGroupIds": [ "{{string}}" ],
      "subnetIds": [ "{{string}}" ]
   },
   "roleArn": "{{string}}",
   "storageConfig": { 
      "blockStorage": { 
         "enabled": {{boolean}}
      }
   },
   "tags": { 
      "{{string}}" : "{{string}}" 
   },
   "upgradePolicy": { 
      "supportType": "{{string}}"
   },
   "version": "{{string}}",
   "zonalShiftConfig": { 
      "enabled": {{boolean}}
   }
}
```

## URI Request Parameters
<a name="API_CreateCluster_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_CreateCluster_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [accessConfig](#API_CreateCluster_RequestSyntax) **   <a name="AmazonEKS-CreateCluster-request-accessConfig"></a>
The access configuration for the cluster.  
Type: [CreateAccessConfigRequest](API_CreateAccessConfigRequest.md) object  
Required: No

 ** [bootstrapSelfManagedAddons](#API_CreateCluster_RequestSyntax) **   <a name="AmazonEKS-CreateCluster-request-bootstrapSelfManagedAddons"></a>
If you set this value to `False` when creating a cluster, the default networking add-ons will not be installed.  
The default networking add-ons include `vpc-cni`, `coredns`, and `kube-proxy`.  
Use this option when you plan to install third-party alternative add-ons or self-manage the default networking add-ons.  
Type: Boolean  
Required: No

 ** [clientRequestToken](#API_CreateCluster_RequestSyntax) **   <a name="AmazonEKS-CreateCluster-request-clientRequestToken"></a>
A unique, case-sensitive identifier that you provide to ensure the idempotency of the request.  
Type: String  
Required: No

 ** [computeConfig](#API_CreateCluster_RequestSyntax) **   <a name="AmazonEKS-CreateCluster-request-computeConfig"></a>
Enable or disable the compute capability of EKS Auto Mode when creating your EKS Auto Mode cluster. If the compute capability is enabled, EKS Auto Mode will create and delete EC2 Managed Instances in your AWS account  
Type: [ComputeConfigRequest](API_ComputeConfigRequest.md) object  
Required: No

 ** [controlPlaneScalingConfig](#API_CreateCluster_RequestSyntax) **   <a name="AmazonEKS-CreateCluster-request-controlPlaneScalingConfig"></a>
The control plane scaling tier configuration. For more information, see EKS Provisioned Control Plane in the Amazon EKS User Guide.  
Type: [ControlPlaneScalingConfig](API_ControlPlaneScalingConfig.md) object  
Required: No

 ** [deletionProtection](#API_CreateCluster_RequestSyntax) **   <a name="AmazonEKS-CreateCluster-request-deletionProtection"></a>
Indicates whether to enable deletion protection for the cluster. When enabled, the cluster cannot be deleted unless deletion protection is first disabled. This helps prevent accidental cluster deletion. Default value is `false`.  
Type: Boolean  
Required: No

 ** [encryptionConfig](#API_CreateCluster_RequestSyntax) **   <a name="AmazonEKS-CreateCluster-request-encryptionConfig"></a>
The encryption configuration for the cluster.  
Type: Array of [EncryptionConfig](API_EncryptionConfig.md) objects  
Array Members: Maximum number of 1 item.  
Required: No

 ** [kubernetesNetworkConfig](#API_CreateCluster_RequestSyntax) **   <a name="AmazonEKS-CreateCluster-request-kubernetesNetworkConfig"></a>
The Kubernetes network configuration for the cluster.  
Type: [KubernetesNetworkConfigRequest](API_KubernetesNetworkConfigRequest.md) object  
Required: No

 ** [logging](#API_CreateCluster_RequestSyntax) **   <a name="AmazonEKS-CreateCluster-request-logging"></a>
Enable or disable exporting the Kubernetes control plane logs for your cluster to CloudWatch Logs . By default, cluster control plane logs aren't exported to CloudWatch Logs . For more information, see [Amazon EKS Cluster control plane logs](https://docs.aws.amazon.com/eks/latest/userguide/control-plane-logs.html) in the * *Amazon EKS User Guide* *.  
CloudWatch Logs ingestion, archive storage, and data scanning rates apply to exported control plane logs. For more information, see [CloudWatch Pricing](http://aws.amazon.com/cloudwatch/pricing/).
Type: [Logging](API_Logging.md) object  
Required: No

 ** [name](#API_CreateCluster_RequestSyntax) **   <a name="AmazonEKS-CreateCluster-request-name"></a>
The unique name to give to your cluster. The name can contain only alphanumeric characters (case-sensitive), hyphens, and underscores. It must start with an alphanumeric character and can't be longer than 100 characters. The name must be unique within the AWS Region and AWS account that you're creating the cluster in.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 100.  
Pattern: `^[0-9A-Za-z][A-Za-z0-9\-_]*`   
Required: Yes

 ** [outpostConfig](#API_CreateCluster_RequestSyntax) **   <a name="AmazonEKS-CreateCluster-request-outpostConfig"></a>
An object representing the configuration of your local Amazon EKS cluster on an AWS Outpost. Before creating a local cluster on an Outpost, review [Local clusters for Amazon EKS on AWS Outposts](https://docs.aws.amazon.com/eks/latest/userguide/eks-outposts-local-cluster-overview.html) in the *Amazon EKS User Guide*. This object isn't available for creating Amazon EKS clusters on the AWS cloud.  
Type: [OutpostConfigRequest](API_OutpostConfigRequest.md) object  
Required: No

 ** [remoteNetworkConfig](#API_CreateCluster_RequestSyntax) **   <a name="AmazonEKS-CreateCluster-request-remoteNetworkConfig"></a>
The configuration in the cluster for EKS Hybrid Nodes. You can add, change, or remove this configuration after the cluster is created.  
Type: [RemoteNetworkConfigRequest](API_RemoteNetworkConfigRequest.md) object  
Required: No

 ** [resourcesVpcConfig](#API_CreateCluster_RequestSyntax) **   <a name="AmazonEKS-CreateCluster-request-resourcesVpcConfig"></a>
The VPC configuration that's used by the cluster control plane. Amazon EKS VPC resources have specific requirements to work properly with Kubernetes. For more information, see [Cluster VPC Considerations](https://docs.aws.amazon.com/eks/latest/userguide/network_reqs.html) and [Cluster Security Group Considerations](https://docs.aws.amazon.com/eks/latest/userguide/sec-group-reqs.html) in the *Amazon EKS User Guide*. You must specify at least two subnets. You can specify up to five security groups. However, we recommend that you use a dedicated security group for your cluster control plane.  
Type: [VpcConfigRequest](API_VpcConfigRequest.md) object  
Required: Yes

 ** [roleArn](#API_CreateCluster_RequestSyntax) **   <a name="AmazonEKS-CreateCluster-request-roleArn"></a>
The Amazon Resource Name (ARN) of the IAM role that provides permissions for the Kubernetes control plane to make calls to AWS API operations on your behalf. For more information, see [Amazon EKS Service IAM Role](https://docs.aws.amazon.com/eks/latest/userguide/service_IAM_role.html) in the * *Amazon EKS User Guide* *.  
Type: String  
Required: Yes

 ** [storageConfig](#API_CreateCluster_RequestSyntax) **   <a name="AmazonEKS-CreateCluster-request-storageConfig"></a>
Enable or disable the block storage capability of EKS Auto Mode when creating your EKS Auto Mode cluster. If the block storage capability is enabled, EKS Auto Mode will create and delete EBS volumes in your AWS account.  
Type: [StorageConfigRequest](API_StorageConfigRequest.md) object  
Required: No

 ** [tags](#API_CreateCluster_RequestSyntax) **   <a name="AmazonEKS-CreateCluster-request-tags"></a>
Metadata that assists with categorization and organization. Each tag consists of a key and an optional value. You define both. Tags don't propagate to any other cluster or AWS resources.  
Type: String to string map  
Map Entries: Maximum number of 50 items.  
Key Length Constraints: Minimum length of 1. Maximum length of 128.  
Value Length Constraints: Maximum length of 256.  
Required: No

 ** [upgradePolicy](#API_CreateCluster_RequestSyntax) **   <a name="AmazonEKS-CreateCluster-request-upgradePolicy"></a>
New clusters, by default, have extended support enabled. You can disable extended support when creating a cluster by setting this value to `STANDARD`.  
Type: [UpgradePolicyRequest](API_UpgradePolicyRequest.md) object  
Required: No

 ** [version](#API_CreateCluster_RequestSyntax) **   <a name="AmazonEKS-CreateCluster-request-version"></a>
The desired Kubernetes version for your cluster. If you don't specify a value here, the default version available in Amazon EKS is used.  
The default version might not be the latest version available.
Type: String  
Required: No

 ** [zonalShiftConfig](#API_CreateCluster_RequestSyntax) **   <a name="AmazonEKS-CreateCluster-request-zonalShiftConfig"></a>
Enable or disable ARC zonal shift for the cluster. If zonal shift is enabled, AWS configures zonal autoshift for the cluster.  
Zonal shift is a feature of Amazon Application Recovery Controller (ARC). ARC zonal shift is designed to be a temporary measure that allows you to move traffic for a resource away from an impaired AZ until the zonal shift expires or you cancel it. You can extend the zonal shift if necessary.  
You can start a zonal shift for an Amazon EKS cluster, or you can allow AWS to do it for you by enabling *zonal autoshift*. This shift updates the flow of east-to-west network traffic in your cluster to only consider network endpoints for Pods running on worker nodes in healthy AZs. Additionally, any ALB or NLB handling ingress traffic for applications in your Amazon EKS cluster will automatically route traffic to targets in the healthy AZs. For more information about zonal shift in EKS, see [Learn about Amazon Application Recovery Controller (ARC) Zonal Shift in Amazon EKS](https://docs.aws.amazon.com/eks/latest/userguide/zone-shift.html) in the * *Amazon EKS User Guide* *.  
Type: [ZonalShiftConfigRequest](API_ZonalShiftConfigRequest.md) object  
Required: No

## Response Syntax
<a name="API_CreateCluster_ResponseSyntax"></a>

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
<a name="API_CreateCluster_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [cluster](#API_CreateCluster_ResponseSyntax) **   <a name="AmazonEKS-CreateCluster-response-cluster"></a>
The full description of your new cluster.  
Type: [Cluster](API_Cluster.md) object

## Errors
<a name="API_CreateCluster_Errors"></a>

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

 ** ServiceUnavailableException **   
The service is unavailable. Back off and retry the operation.    
 ** message **   
The request has failed due to a temporary failure of the server.
HTTP Status Code: 503

 ** UnsupportedAvailabilityZoneException **   
At least one of your specified cluster subnets is in an Availability Zone that does not support Amazon EKS. The exception output specifies the supported Availability Zones for your account, from which you can choose subnets for your cluster.    
 ** clusterName **   
The Amazon EKS cluster associated with the exception.  
 ** message **   
At least one of your specified cluster subnets is in an Availability Zone that does not support Amazon EKS. The exception output specifies the supported Availability Zones for your account, from which you can choose subnets for your cluster.  
 ** nodegroupName **   
The Amazon EKS managed node group associated with the exception.  
 ** validZones **   
The supported Availability Zones for your account. Choose subnets in these Availability Zones for your cluster.
HTTP Status Code: 400

## Examples
<a name="API_CreateCluster_Examples"></a>

In the following example or examples, the Authorization header contents (`AUTHPARAMS`) must be replaced with an AWS Signature Version 4 signature. For more information about creating these signatures, see [Signature Version 4 Signing Process](https://docs.aws.amazon.com/general/latest/gr/signature-version-4.html) in the *Amazon EKS General Reference*.

You need to learn how to sign HTTP requests only if you intend to manually create them. When you use the [AWS Command Line Interface (AWS CLI)](http://aws.amazon.com/cli/) or one of the [AWS SDKs](http://aws.amazon.com/tools/) to make requests to AWS, these tools automatically sign the requests for you with the access key that you specify when you configure the tools. When you use these tools, you don't need to learn how to sign requests yourself.

### Example
<a name="API_CreateCluster_Example_1"></a>

The following example creates an Amazon EKS cluster named `my-cluster` with endpoint public and private access enabled.

#### Sample Request
<a name="API_CreateCluster_Example_1_Request"></a>

```
POST /clusters HTTP/1.1
Host: eks.us-west-2.amazonaws.com
Accept-Encoding: identity
User-Agent: aws-cli/1.16.120 Python/3.7.0 Darwin/18.2.0 botocore/1.12.110
X-Amz-Date: 20190322T160158Z
Authorization: AUTHPARAMS
Content-Length: 368

{
    "name": "my-cluster",
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
        "endpointPublicAccess": true,
        "endpointPrivateAccess": true
    },
    "clientRequestToken": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx"
}
```

#### Sample Response
<a name="API_CreateCluster_Example_1_Response"></a>

```
HTTP/1.1 200 OK
Date: Fri, 22 Mar 2019 16:01:58 GMT
Content-Type: application/json
Content-Length: 682
x-amzn-RequestId: xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxx
x-amz-apigw-id: W84GUEIbPHcFW2Q=
X-Amzn-Trace-Id: Root=1-xxxxxxxxx-xxxxxxxxxxxxxxxxxxxxxxxx
Connection: keep-alive

{
  "cluster": {
    "name": "my-cluster",
    "arn": "arn:aws:eks:us-west-2:012345678910:cluster/my-cluster",
    "createdAt": 1573484658.211,
    "version": "1.14",
    "roleArn": "arn:aws:iam::012345678910:role/eksClusterRole",
    "resourcesVpcConfig": {
      "subnetIds": [
        "subnet-xxxxxxxxxxxxxxxxx",
        "subnet-yyyyyyyyyyyyyyyyy",
        "subnet-zzzzzzzzzzzzzzzzz"
      ],
      "securityGroupIds": [],
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
    "status": "CREATING",
    "certificateAuthority": {},
    "platformVersion": "eks.3",
    "tags": {}
  }
}
```

## See Also
<a name="API_CreateCluster_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/eks-2017-11-01/CreateCluster) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/eks-2017-11-01/CreateCluster) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/eks-2017-11-01/CreateCluster) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/eks-2017-11-01/CreateCluster) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/eks-2017-11-01/CreateCluster) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/eks-2017-11-01/CreateCluster) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/eks-2017-11-01/CreateCluster) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/eks-2017-11-01/CreateCluster) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/eks-2017-11-01/CreateCluster) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/eks-2017-11-01/CreateCluster) 