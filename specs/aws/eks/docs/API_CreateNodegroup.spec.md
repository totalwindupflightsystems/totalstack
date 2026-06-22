---
id: "@specs/aws/eks/docs/API_CreateNodegroup"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS CreateNodegroup"
status: active
depends_on:
  - "@specs/aws/eks/meta"
---

# CreateNodegroup

> **source:** AWS Documentation
> **spec:id:** @specs/aws/eks/docs/API_CreateNodegroup
> **target_lang:** meta — documentation tier. ALL sections preserved.



# CreateNodegroup
<a name="API_CreateNodegroup"></a>

Creates a managed node group for an Amazon EKS cluster.

You can only create a node group for your cluster that is equal to the current Kubernetes version for the cluster. All node groups are created with the latest AMI release version for the respective minor Kubernetes version of the cluster, unless you deploy a custom AMI using a launch template.

For later updates, you will only be able to update a node group using a launch template only if it was originally deployed with a launch template. Additionally, the launch template ID or name must match what was used when the node group was created. You can update the launch template version with necessary changes. For more information about using launch templates, see [Customizing managed nodes with launch templates](https://docs.aws.amazon.com/eks/latest/userguide/launch-templates.html).

An Amazon EKS managed node group is an Amazon EC2 Auto Scaling group and associated Amazon EC2 instances that are managed by AWS for an Amazon EKS cluster. For more information, see [Managed node groups](https://docs.aws.amazon.com/eks/latest/userguide/managed-node-groups.html) in the *Amazon EKS User Guide*.

**Note**  
Windows AMI types are only supported for commercial AWS Regions that support Windows on Amazon EKS.

## Request Syntax
<a name="API_CreateNodegroup_RequestSyntax"></a>

```
POST /clusters/{{name}}/node-groups HTTP/1.1
Content-type: application/json

{
   "amiType": "{{string}}",
   "capacityType": "{{string}}",
   "clientRequestToken": "{{string}}",
   "diskSize": {{number}},
   "instanceTypes": [ "{{string}}" ],
   "labels": { 
      "{{string}}" : "{{string}}" 
   },
   "launchTemplate": { 
      "id": "{{string}}",
      "name": "{{string}}",
      "version": "{{string}}"
   },
   "nodegroupName": "{{string}}",
   "nodeRepairConfig": { 
      "enabled": {{boolean}},
      "maxParallelNodesRepairedCount": {{number}},
      "maxParallelNodesRepairedPercentage": {{number}},
      "maxUnhealthyNodeThresholdCount": {{number}},
      "maxUnhealthyNodeThresholdPercentage": {{number}},
      "nodeRepairConfigOverrides": [ 
         { 
            "minRepairWaitTimeMins": {{number}},
            "nodeMonitoringCondition": "{{string}}",
            "nodeUnhealthyReason": "{{string}}",
            "repairAction": "{{string}}"
         }
      ]
   },
   "nodeRole": "{{string}}",
   "releaseVersion": "{{string}}",
   "remoteAccess": { 
      "ec2SshKey": "{{string}}",
      "sourceSecurityGroups": [ "{{string}}" ]
   },
   "scalingConfig": { 
      "desiredSize": {{number}},
      "maxSize": {{number}},
      "minSize": {{number}}
   },
   "subnets": [ "{{string}}" ],
   "tags": { 
      "{{string}}" : "{{string}}" 
   },
   "taints": [ 
      { 
         "effect": "{{string}}",
         "key": "{{string}}",
         "value": "{{string}}"
      }
   ],
   "updateConfig": { 
      "maxUnavailable": {{number}},
      "maxUnavailablePercentage": {{number}},
      "updateStrategy": "{{string}}"
   },
   "version": "{{string}}",
   "warmPoolConfig": { 
      "enabled": {{boolean}},
      "maxGroupPreparedCapacity": {{number}},
      "minSize": {{number}},
      "poolState": "{{string}}",
      "reuseOnScaleIn": {{boolean}}
   }
}
```

## URI Request Parameters
<a name="API_CreateNodegroup_RequestParameters"></a>

The request uses the following URI parameters.

 ** [name](#API_CreateNodegroup_RequestSyntax) **   <a name="AmazonEKS-CreateNodegroup-request-uri-clusterName"></a>
The name of your cluster.  
Required: Yes

## Request Body
<a name="API_CreateNodegroup_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [amiType](#API_CreateNodegroup_RequestSyntax) **   <a name="AmazonEKS-CreateNodegroup-request-amiType"></a>
The AMI type for your node group. If you specify `launchTemplate`, and your launch template uses a custom AMI, then don't specify `amiType`, or the node group deployment will fail. If your launch template uses a Windows custom AMI, then add `eks:kube-proxy-windows` to your Windows nodes `rolearn` in the `aws-auth` `ConfigMap`. For more information about using launch templates with Amazon EKS, see [Customizing managed nodes with launch templates](https://docs.aws.amazon.com/eks/latest/userguide/launch-templates.html) in the *Amazon EKS User Guide*.  
Type: String  
Valid Values: `AL2_x86_64 | AL2_x86_64_GPU | AL2_ARM_64 | CUSTOM | BOTTLEROCKET_ARM_64 | BOTTLEROCKET_x86_64 | BOTTLEROCKET_ARM_64_FIPS | BOTTLEROCKET_x86_64_FIPS | BOTTLEROCKET_ARM_64_NVIDIA | BOTTLEROCKET_x86_64_NVIDIA | BOTTLEROCKET_ARM_64_NVIDIA_FIPS | BOTTLEROCKET_x86_64_NVIDIA_FIPS | WINDOWS_CORE_2019_x86_64 | WINDOWS_FULL_2019_x86_64 | WINDOWS_CORE_2022_x86_64 | WINDOWS_FULL_2022_x86_64 | WINDOWS_CORE_2025_x86_64 | WINDOWS_FULL_2025_x86_64 | AL2023_x86_64_STANDARD | AL2023_ARM_64_STANDARD | AL2023_x86_64_NEURON | AL2023_x86_64_NVIDIA | AL2023_ARM_64_NVIDIA`   
Required: No

 ** [capacityType](#API_CreateNodegroup_RequestSyntax) **   <a name="AmazonEKS-CreateNodegroup-request-capacityType"></a>
The capacity type for your node group.  
Type: String  
Valid Values: `ON_DEMAND | SPOT | CAPACITY_BLOCK`   
Required: No

 ** [clientRequestToken](#API_CreateNodegroup_RequestSyntax) **   <a name="AmazonEKS-CreateNodegroup-request-clientRequestToken"></a>
A unique, case-sensitive identifier that you provide to ensure the idempotency of the request.  
Type: String  
Required: No

 ** [diskSize](#API_CreateNodegroup_RequestSyntax) **   <a name="AmazonEKS-CreateNodegroup-request-diskSize"></a>
The root device disk size (in GiB) for your node group instances. The default disk size is 20 GiB for Linux and Bottlerocket. The default disk size is 50 GiB for Windows. If you specify `launchTemplate`, then don't specify `diskSize`, or the node group deployment will fail. For more information about using launch templates with Amazon EKS, see [Customizing managed nodes with launch templates](https://docs.aws.amazon.com/eks/latest/userguide/launch-templates.html) in the *Amazon EKS User Guide*.  
Type: Integer  
Required: No

 ** [instanceTypes](#API_CreateNodegroup_RequestSyntax) **   <a name="AmazonEKS-CreateNodegroup-request-instanceTypes"></a>
Specify the instance types for a node group. If you specify a GPU instance type, make sure to also specify an applicable GPU AMI type with the `amiType` parameter. If you specify `launchTemplate`, then you can specify zero or one instance type in your launch template *or* you can specify 0-20 instance types for `instanceTypes`. If however, you specify an instance type in your launch template *and* specify any `instanceTypes`, the node group deployment will fail. If you don't specify an instance type in a launch template or for `instanceTypes`, then `t3.medium` is used, by default. If you specify `Spot` for `capacityType`, then we recommend specifying multiple values for `instanceTypes`. For more information, see [Managed node group capacity types](https://docs.aws.amazon.com/eks/latest/userguide/managed-node-groups.html#managed-node-group-capacity-types) and [Customizing managed nodes with launch templates](https://docs.aws.amazon.com/eks/latest/userguide/launch-templates.html) in the *Amazon EKS User Guide*.  
Type: Array of strings  
Required: No

 ** [labels](#API_CreateNodegroup_RequestSyntax) **   <a name="AmazonEKS-CreateNodegroup-request-labels"></a>
The Kubernetes `labels` to apply to the nodes in the node group when they are created.  
Type: String to string map  
Key Length Constraints: Minimum length of 1. Maximum length of 63.  
Value Length Constraints: Minimum length of 1. Maximum length of 63.  
Required: No

 ** [launchTemplate](#API_CreateNodegroup_RequestSyntax) **   <a name="AmazonEKS-CreateNodegroup-request-launchTemplate"></a>
An object representing a node group's launch template specification. When using this object, don't directly specify `instanceTypes`, `diskSize`, or `remoteAccess`. You cannot later specify a different launch template ID or name than what was used to create the node group.  
Make sure that the launch template meets the requirements in `launchTemplateSpecification`. Also refer to [Customizing managed nodes with launch templates](https://docs.aws.amazon.com/eks/latest/userguide/launch-templates.html) in the *Amazon EKS User Guide*.  
Type: [LaunchTemplateSpecification](API_LaunchTemplateSpecification.md) object  
Required: No

 ** [nodegroupName](#API_CreateNodegroup_RequestSyntax) **   <a name="AmazonEKS-CreateNodegroup-request-nodegroupName"></a>
The unique name to give your node group.  
Type: String  
Required: Yes

 ** [nodeRepairConfig](#API_CreateNodegroup_RequestSyntax) **   <a name="AmazonEKS-CreateNodegroup-request-nodeRepairConfig"></a>
The node auto repair configuration for the node group.  
Type: [NodeRepairConfig](API_NodeRepairConfig.md) object  
Required: No

 ** [nodeRole](#API_CreateNodegroup_RequestSyntax) **   <a name="AmazonEKS-CreateNodegroup-request-nodeRole"></a>
The Amazon Resource Name (ARN) of the IAM role to associate with your node group. The Amazon EKS worker node `kubelet` daemon makes calls to AWS APIs on your behalf. Nodes receive permissions for these API calls through an IAM instance profile and associated policies. Before you can launch nodes and register them into a cluster, you must create an IAM role for those nodes to use when they are launched. For more information, see [Amazon EKS node IAM role](https://docs.aws.amazon.com/eks/latest/userguide/create-node-role.html) in the * *Amazon EKS User Guide* *. If you specify `launchTemplate`, then don't specify ` [IamInstanceProfile](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_IamInstanceProfile.html) ` in your launch template, or the node group deployment will fail. For more information about using launch templates with Amazon EKS, see [Customizing managed nodes with launch templates](https://docs.aws.amazon.com/eks/latest/userguide/launch-templates.html) in the *Amazon EKS User Guide*.  
Type: String  
Required: Yes

 ** [releaseVersion](#API_CreateNodegroup_RequestSyntax) **   <a name="AmazonEKS-CreateNodegroup-request-releaseVersion"></a>
The AMI version of the Amazon EKS optimized AMI to use with your node group. By default, the latest available AMI version for the node group's current Kubernetes version is used. For information about Linux versions, see [Amazon EKS optimized Amazon Linux AMI versions](https://docs.aws.amazon.com/eks/latest/userguide/eks-linux-ami-versions.html) in the *Amazon EKS User Guide*. Amazon EKS managed node groups support the November 2022 and later releases of the Windows AMIs. For information about Windows versions, see [Amazon EKS optimized Windows AMI versions](https://docs.aws.amazon.com/eks/latest/userguide/eks-ami-versions-windows.html) in the *Amazon EKS User Guide*.  
If you specify `launchTemplate`, and your launch template uses a custom AMI, then don't specify `releaseVersion`, or the node group deployment will fail. For more information about using launch templates with Amazon EKS, see [Customizing managed nodes with launch templates](https://docs.aws.amazon.com/eks/latest/userguide/launch-templates.html) in the *Amazon EKS User Guide*.  
Type: String  
Required: No

 ** [remoteAccess](#API_CreateNodegroup_RequestSyntax) **   <a name="AmazonEKS-CreateNodegroup-request-remoteAccess"></a>
The remote access configuration to use with your node group. For Linux, the protocol is SSH. For Windows, the protocol is RDP. If you specify `launchTemplate`, then don't specify `remoteAccess`, or the node group deployment will fail. For more information about using launch templates with Amazon EKS, see [Customizing managed nodes with launch templates](https://docs.aws.amazon.com/eks/latest/userguide/launch-templates.html) in the *Amazon EKS User Guide*.  
Type: [RemoteAccessConfig](API_RemoteAccessConfig.md) object  
Required: No

 ** [scalingConfig](#API_CreateNodegroup_RequestSyntax) **   <a name="AmazonEKS-CreateNodegroup-request-scalingConfig"></a>
The scaling configuration details for the Auto Scaling group that is created for your node group.  
Type: [NodegroupScalingConfig](API_NodegroupScalingConfig.md) object  
Required: No

 ** [subnets](#API_CreateNodegroup_RequestSyntax) **   <a name="AmazonEKS-CreateNodegroup-request-subnets"></a>
The subnets to use for the Auto Scaling group that is created for your node group. If you specify `launchTemplate`, then don't specify ` [SubnetId](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CreateNetworkInterface.html) ` in your launch template, or the node group deployment will fail. For more information about using launch templates with Amazon EKS, see [Customizing managed nodes with launch templates](https://docs.aws.amazon.com/eks/latest/userguide/launch-templates.html) in the *Amazon EKS User Guide*.  
Type: Array of strings  
Required: Yes

 ** [tags](#API_CreateNodegroup_RequestSyntax) **   <a name="AmazonEKS-CreateNodegroup-request-tags"></a>
Metadata that assists with categorization and organization. Each tag consists of a key and an optional value. You define both. Tags don't propagate to any other cluster or AWS resources.  
Type: String to string map  
Map Entries: Maximum number of 50 items.  
Key Length Constraints: Minimum length of 1. Maximum length of 128.  
Value Length Constraints: Maximum length of 256.  
Required: No

 ** [taints](#API_CreateNodegroup_RequestSyntax) **   <a name="AmazonEKS-CreateNodegroup-request-taints"></a>
The Kubernetes taints to be applied to the nodes in the node group. For more information, see [Node taints on managed node groups](https://docs.aws.amazon.com/eks/latest/userguide/node-taints-managed-node-groups.html).  
Type: Array of [Taint](API_Taint.md) objects  
Required: No

 ** [updateConfig](#API_CreateNodegroup_RequestSyntax) **   <a name="AmazonEKS-CreateNodegroup-request-updateConfig"></a>
The node group update configuration.  
Type: [NodegroupUpdateConfig](API_NodegroupUpdateConfig.md) object  
Required: No

 ** [version](#API_CreateNodegroup_RequestSyntax) **   <a name="AmazonEKS-CreateNodegroup-request-version"></a>
The Kubernetes version to use for your managed nodes. By default, the Kubernetes version of the cluster is used, and this is the only accepted specified value. If you specify `launchTemplate`, and your launch template uses a custom AMI, then don't specify `version`, or the node group deployment will fail. For more information about using launch templates with Amazon EKS, see [Customizing managed nodes with launch templates](https://docs.aws.amazon.com/eks/latest/userguide/launch-templates.html) in the *Amazon EKS User Guide*.  
Type: String  
Required: No

 ** [warmPoolConfig](#API_CreateNodegroup_RequestSyntax) **   <a name="AmazonEKS-CreateNodegroup-request-warmPoolConfig"></a>
The warm pool configuration for the node group. Warm pools maintain pre-initialized EC2 instances that can quickly join your cluster during scale-out events, improving application scaling performance and reducing costs.  
Type: [WarmPoolConfig](API_WarmPoolConfig.md) object  
Required: No

## Response Syntax
<a name="API_CreateNodegroup_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "nodegroup": { 
      "amiType": "string",
      "capacityType": "string",
      "clusterName": "string",
      "createdAt": number,
      "diskSize": number,
      "health": { 
         "issues": [ 
            { 
               "code": "string",
               "message": "string",
               "resourceIds": [ "string" ]
            }
         ]
      },
      "instanceTypes": [ "string" ],
      "labels": { 
         "string" : "string" 
      },
      "launchTemplate": { 
         "id": "string",
         "name": "string",
         "version": "string"
      },
      "modifiedAt": number,
      "nodegroupArn": "string",
      "nodegroupName": "string",
      "nodeRepairConfig": { 
         "enabled": boolean,
         "maxParallelNodesRepairedCount": number,
         "maxParallelNodesRepairedPercentage": number,
         "maxUnhealthyNodeThresholdCount": number,
         "maxUnhealthyNodeThresholdPercentage": number,
         "nodeRepairConfigOverrides": [ 
            { 
               "minRepairWaitTimeMins": number,
               "nodeMonitoringCondition": "string",
               "nodeUnhealthyReason": "string",
               "repairAction": "string"
            }
         ]
      },
      "nodeRole": "string",
      "releaseVersion": "string",
      "remoteAccess": { 
         "ec2SshKey": "string",
         "sourceSecurityGroups": [ "string" ]
      },
      "resources": { 
         "autoScalingGroups": [ 
            { 
               "name": "string"
            }
         ],
         "remoteAccessSecurityGroup": "string"
      },
      "scalingConfig": { 
         "desiredSize": number,
         "maxSize": number,
         "minSize": number
      },
      "status": "string",
      "subnets": [ "string" ],
      "tags": { 
         "string" : "string" 
      },
      "taints": [ 
         { 
            "effect": "string",
            "key": "string",
            "value": "string"
         }
      ],
      "updateConfig": { 
         "maxUnavailable": number,
         "maxUnavailablePercentage": number,
         "updateStrategy": "string"
      },
      "version": "string",
      "warmPoolConfig": { 
         "enabled": boolean,
         "maxGroupPreparedCapacity": number,
         "minSize": number,
         "poolState": "string",
         "reuseOnScaleIn": boolean
      }
   }
}
```

## Response Elements
<a name="API_CreateNodegroup_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [nodegroup](#API_CreateNodegroup_ResponseSyntax) **   <a name="AmazonEKS-CreateNodegroup-response-nodegroup"></a>
The full description of your new node group.  
Type: [Nodegroup](API_Nodegroup.md) object

## Errors
<a name="API_CreateNodegroup_Errors"></a>

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

## Examples
<a name="API_CreateNodegroup_Examples"></a>

In the following example or examples, the Authorization header contents (`AUTHPARAMS`) must be replaced with an AWS Signature Version 4 signature. For more information about creating these signatures, see [Signature Version 4 Signing Process](https://docs.aws.amazon.com/general/latest/gr/signature-version-4.html) in the *Amazon EKS General Reference*.

You need to learn how to sign HTTP requests only if you intend to manually create them. When you use the [AWS Command Line Interface (AWS CLI)](http://aws.amazon.com/cli/) or one of the [AWS SDKs](http://aws.amazon.com/tools/) to make requests to AWS, these tools automatically sign the requests for you with the access key that you specify when you configure the tools. When you use these tools, you don't need to learn how to sign requests yourself.

### Example 1
<a name="API_CreateNodegroup_Example_1"></a>

This example creates a managed node group without a launch template that uses an Amazon EKS optimized AMI with GPU support on `p2.xlarge` instances. 

#### Sample Request
<a name="API_CreateNodegroup_Example_1_Request"></a>

```
POST /clusters/my-cluster/node-groups HTTP/1.1
Host: eks.us-west-2.amazonaws.com
Accept-Encoding: identity
User-Agent: aws-cli/1.16.298 Python/3.6.0 Windows/10 botocore/1.13.34
X-Amz-Date: 20200812T151423Z
Authorization: AUTHPARAMS
Content-Length: 454

{
	"nodegroupName": "my-nodegroup-gpu",
	"scalingConfig": {
		"minSize": 2,
		"maxSize": 2,
		"desiredSize": 2
	},
	"subnets": ["subnet-nnnnnnnnnnnnnnnnn", "subnet-xxxxxxxxxxxxxxxxx", "subnet-yyyyyyyyyyyyyyyyy", "subnet-zzzzzzzzzzzzzzzzz"],
	"instanceTypes": ["p2.xlarge"],
	"amiType": "AL2_x86_64_GPU",
        "remoteAccess": {
          "ec2SshKey": "id_rsa"
         },
	"nodeRole": "arn:aws:iam::012345678910:role/NodeInstanceRole",
	"clientRequestToken": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx"
}
```

#### Sample Response
<a name="API_CreateNodegroup_Example_1_Response"></a>

```
HTTP/1.1 200 OK
Date: Wed, 12 Aug 2020 15:14:24 GMT
Content-Type: application/json
Content-Length: 951
x-amzn-RequestId: xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxx
x-amz-apigw-id: DAc5BGsWvHcF_bw=
X-Amzn-Trace-Id: Root=1-xxxxxxxxx-xxxxxxxxxxxxxxxxxxxxxxxx
Connection: keep-alive

{
	"nodegroup": {
		"nodegroupName": "my-nodegroup-gpu2",
		"nodegroupArn": "arn:aws:eks:us-west-2:012345678910:nodegroup/my-cluster/my-nodegroup-gpu2/xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
		"clusterName": "lt-testing",
		"version": "1.17",
		"releaseVersion": "1.17.9-20200804",
		"createdAt": 1.597245264844E9,
		"modifiedAt": 1.597245264844E9,
		"status": "CREATING",
		"scalingConfig": {
			"minSize": 2,
			"maxSize": 2,
			"desiredSize": 2
		},
		"instanceTypes": ["p2.xlarge"],
		"subnets": ["subnet-nnnnnnnnnnnnnnnnn", "subnet-xxxxxxxxxxxxxxxxx", "subnet-yyyyyyyyyyyyyyyyy", "subnet-zzzzzzzzzzzzzzzzz"],
		"remoteAccess": {
                  "ec2SshKey": "id_rsa",
                  "sourceSecurityGroups": null
                },
		"amiType": "AL2_x86_64_GPU",
		"nodeRole": "arn:aws:iam::012345678910:role/NodeInstanceRole",
		"labels": null,
		"resources": null,
		"diskSize": 20,
		"health": {
			"issues": []
		},
		"launchTemplate": null,
		"tags": {}
	}
}
```

### Example 2
<a name="API_CreateNodegroup_Example_2"></a>

This example creates a managed node group with an Amazon EKS optimized AMI using version `2` of a launch template named `my-launch-template`.

#### Sample Request
<a name="API_CreateNodegroup_Example_2_Request"></a>

```
POST /clusters/lt-testing/node-groups HTTP/1.1
Host: eks.us-west-2.amazonaws.com
Accept-Encoding: identity
User-Agent: aws-cli/1.16.298 Python/3.6.0 Windows/10 botocore/1.13.34
X-Amz-Date: 20200812T135927Z
Authorization: AUTHPARAMS
Content-Length: 433

{
	"nodegroupName": "my-nodegroup",
	"scalingConfig": {
		"minSize": 2,
		"maxSize": 2,
		"desiredSize": 2
	},
	"subnets": ["subnet-nnnnnnnnnnnnnnnnn", "subnet-xxxxxxxxxxxxxxxxx", "subnet-yyyyyyyyyyyyyyyyy", "subnet-zzzzzzzzzzzzzzzzz"],
	"amiType": "AL2_x86_64",
	"nodeRole": "arn:aws:iam::012345678910:role/NodeInstanceRole",
	"launchTemplate": {
		"name": "my-launch-template",
		"version": "2"
	},
	"clientRequestToken": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx"
}
```

#### Sample Response
<a name="API_CreateNodegroup_Example_2_Response"></a>

```
HTTP/1.1 200 OK
Date: Wed, 12 Aug 2020 13:59:32 GMT
Content-Type: application/json
Content-Length: 1028
x-amzn-RequestId: xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxx
x-amz-apigw-id: DAc5BGsWvHcF_bw=
X-Amzn-Trace-Id: Root=1-xxxxxxxxx-xxxxxxxxxxxxxxxxxxxxxxxx
Connection: keep-alive

{
	"nodegroup": {
		"nodegroupName": "my-nodegroup",
		"nodegroupArn": "arn:aws:eks:us-west-2:012345678910:nodegroup/my-cluster/my-nodegroup/xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
		"clusterName": "my-cluster",
		"version": "1.17",
		"releaseVersion": "1.17.9-20200804",
		"createdAt": 1.597240771904E9,
		"modifiedAt": 1.597240771904E9,
		"status": "CREATING",
		"scalingConfig": {
			"minSize": 2,
			"maxSize": 2,
			"desiredSize": 2
		},
		"instanceTypes": null,
		"subnets": ["subnet-nnnnnnnnnnnnnnnnn", "subnet-xxxxxxxxxxxxxxxxx", "subnet-yyyyyyyyyyyyyyyyy", "subnet-zzzzzzzzzzzzzzzzz"],
		"remoteAccess": null,
		"amiType": "AL2_x86_64",
		"nodeRole": "arn:aws:iam::012345678910:role/NodeInstanceRole",
		"labels": null,
		"resources": null,
		"diskSize": null,
		"health": {
			"issues": []
		},
		"launchTemplate": {
			"name": "my-template",
			"version": "2",
			"id": "lt-xxxxxxxxxxxxxxxxx"
		},
		"tags": {}
	}
}
```

## See Also
<a name="API_CreateNodegroup_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/eks-2017-11-01/CreateNodegroup) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/eks-2017-11-01/CreateNodegroup) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/eks-2017-11-01/CreateNodegroup) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/eks-2017-11-01/CreateNodegroup) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/eks-2017-11-01/CreateNodegroup) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/eks-2017-11-01/CreateNodegroup) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/eks-2017-11-01/CreateNodegroup) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/eks-2017-11-01/CreateNodegroup) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/eks-2017-11-01/CreateNodegroup) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/eks-2017-11-01/CreateNodegroup) 