---
id: "@specs/aws/eks/docs/API_UpdateClusterConfig"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS UpdateClusterConfig"
status: active
depends_on:
  - "@specs/aws/eks/meta"
---

# UpdateClusterConfig

> **source:** AWS Documentation
> **spec:id:** @specs/aws/eks/docs/API_UpdateClusterConfig
> **target_lang:** meta — documentation tier. ALL sections preserved.



# UpdateClusterConfig
<a name="API_UpdateClusterConfig"></a>

Updates an Amazon EKS cluster configuration. Your cluster continues to function during the update. The response output includes an update ID that you can use to track the status of your cluster update with `DescribeUpdate`.

You can use this operation to do the following actions:
+ You can use this API operation to enable or disable exporting the Kubernetes control plane logs for your cluster to CloudWatch Logs. By default, cluster control plane logs aren't exported to CloudWatch Logs. For more information, see [Amazon EKS Cluster control plane logs](https://docs.aws.amazon.com/eks/latest/userguide/control-plane-logs.html) in the * *Amazon EKS User Guide* *.
**Note**  
CloudWatch Logs ingestion, archive storage, and data scanning rates apply to exported control plane logs. For more information, see [CloudWatch Pricing](http://aws.amazon.com/cloudwatch/pricing/).
+ You can also use this API operation to enable or disable public and private access to your cluster's Kubernetes API server endpoint. By default, public access is enabled, and private access is disabled. For more information, see [ Cluster API server endpoint](https://docs.aws.amazon.com/eks/latest/userguide/cluster-endpoint.html) in the * *Amazon EKS User Guide* *.
+ You can also use this API operation to choose different subnets and security groups for the cluster. You must specify at least two subnets that are in different Availability Zones. You can't change which VPC the subnets are from, the subnets must be in the same VPC as the subnets that the cluster was created with. For more information about the VPC requirements, see [https://docs.aws.amazon.com/eks/latest/userguide/network_reqs.html](https://docs.aws.amazon.com/eks/latest/userguide/network_reqs.html) in the * *Amazon EKS User Guide* *.
+ You can also use this API operation to enable or disable ARC zonal shift. If zonal shift is enabled, AWS configures zonal autoshift for the cluster.
+ You can also use this API operation to add, change, or remove the configuration in the cluster for EKS Hybrid Nodes. To remove the configuration, use the `remoteNetworkConfig` key with an object containing both subkeys with empty arrays for each. Here is an inline example: `"remoteNetworkConfig": { "remoteNodeNetworks": [], "remotePodNetworks": [] }`.

Cluster updates are asynchronous, and they should finish within a few minutes. During an update, the cluster status moves to `UPDATING` (this status transition is eventually consistent). When the update is complete (either `Failed` or `Successful`), the cluster status moves to `Active`.

## Request Syntax
<a name="API_UpdateClusterConfig_RequestSyntax"></a>

```
POST /clusters/{{name}}/update-config HTTP/1.1
Content-type: application/json

{
   "accessConfig": { 
      "authenticationMode": "{{string}}"
   },
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
   "storageConfig": { 
      "blockStorage": { 
         "enabled": {{boolean}}
      }
   },
   "upgradePolicy": { 
      "supportType": "{{string}}"
   },
   "zonalShiftConfig": { 
      "enabled": {{boolean}}
   }
}
```

## URI Request Parameters
<a name="API_UpdateClusterConfig_RequestParameters"></a>

The request uses the following URI parameters.

 ** [name](#API_UpdateClusterConfig_RequestSyntax) **   <a name="AmazonEKS-UpdateClusterConfig-request-uri-name"></a>
The name of the Amazon EKS cluster to update.  
Required: Yes

## Request Body
<a name="API_UpdateClusterConfig_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [accessConfig](#API_UpdateClusterConfig_RequestSyntax) **   <a name="AmazonEKS-UpdateClusterConfig-request-accessConfig"></a>
The access configuration for the cluster.  
Type: [UpdateAccessConfigRequest](API_UpdateAccessConfigRequest.md) object  
Required: No

 ** [clientRequestToken](#API_UpdateClusterConfig_RequestSyntax) **   <a name="AmazonEKS-UpdateClusterConfig-request-clientRequestToken"></a>
A unique, case-sensitive identifier that you provide to ensure the idempotency of the request.  
Type: String  
Required: No

 ** [computeConfig](#API_UpdateClusterConfig_RequestSyntax) **   <a name="AmazonEKS-UpdateClusterConfig-request-computeConfig"></a>
Update the configuration of the compute capability of your EKS Auto Mode cluster. For example, enable the capability.  
Type: [ComputeConfigRequest](API_ComputeConfigRequest.md) object  
Required: No

 ** [controlPlaneScalingConfig](#API_UpdateClusterConfig_RequestSyntax) **   <a name="AmazonEKS-UpdateClusterConfig-request-controlPlaneScalingConfig"></a>
The control plane scaling tier configuration. For more information, see EKS Provisioned Control Plane in the Amazon EKS User Guide.  
Type: [ControlPlaneScalingConfig](API_ControlPlaneScalingConfig.md) object  
Required: No

 ** [deletionProtection](#API_UpdateClusterConfig_RequestSyntax) **   <a name="AmazonEKS-UpdateClusterConfig-request-deletionProtection"></a>
Specifies whether to enable or disable deletion protection for the cluster. When enabled (`true`), the cluster cannot be deleted until deletion protection is explicitly disabled. When disabled (`false`), the cluster can be deleted normally.  
Type: Boolean  
Required: No

 ** [kubernetesNetworkConfig](#API_UpdateClusterConfig_RequestSyntax) **   <a name="AmazonEKS-UpdateClusterConfig-request-kubernetesNetworkConfig"></a>
The Kubernetes network configuration for the cluster.  
Type: [KubernetesNetworkConfigRequest](API_KubernetesNetworkConfigRequest.md) object  
Required: No

 ** [logging](#API_UpdateClusterConfig_RequestSyntax) **   <a name="AmazonEKS-UpdateClusterConfig-request-logging"></a>
Enable or disable exporting the Kubernetes control plane logs for your cluster to CloudWatch Logs . By default, cluster control plane logs aren't exported to CloudWatch Logs . For more information, see [Amazon EKS cluster control plane logs](https://docs.aws.amazon.com/eks/latest/userguide/control-plane-logs.html) in the * *Amazon EKS User Guide* *.  
CloudWatch Logs ingestion, archive storage, and data scanning rates apply to exported control plane logs. For more information, see [CloudWatch Pricing](http://aws.amazon.com/cloudwatch/pricing/).
Type: [Logging](API_Logging.md) object  
Required: No

 ** [remoteNetworkConfig](#API_UpdateClusterConfig_RequestSyntax) **   <a name="AmazonEKS-UpdateClusterConfig-request-remoteNetworkConfig"></a>
The configuration in the cluster for EKS Hybrid Nodes. You can add, change, or remove this configuration after the cluster is created.  
Type: [RemoteNetworkConfigRequest](API_RemoteNetworkConfigRequest.md) object  
Required: No

 ** [resourcesVpcConfig](#API_UpdateClusterConfig_RequestSyntax) **   <a name="AmazonEKS-UpdateClusterConfig-request-resourcesVpcConfig"></a>
An object representing the VPC configuration to use for the cluster update. You can use this parameter to update the control plane egress mode, the subnets used by the cluster, the security groups, and the endpoint access settings.  
Type: [VpcConfigRequest](API_VpcConfigRequest.md) object  
Required: No

 ** [storageConfig](#API_UpdateClusterConfig_RequestSyntax) **   <a name="AmazonEKS-UpdateClusterConfig-request-storageConfig"></a>
Update the configuration of the block storage capability of your EKS Auto Mode cluster. For example, enable the capability.  
Type: [StorageConfigRequest](API_StorageConfigRequest.md) object  
Required: No

 ** [upgradePolicy](#API_UpdateClusterConfig_RequestSyntax) **   <a name="AmazonEKS-UpdateClusterConfig-request-upgradePolicy"></a>
You can enable or disable extended support for clusters currently on standard support. You cannot disable extended support once it starts. You must enable extended support before your cluster exits standard support.  
Type: [UpgradePolicyRequest](API_UpgradePolicyRequest.md) object  
Required: No

 ** [zonalShiftConfig](#API_UpdateClusterConfig_RequestSyntax) **   <a name="AmazonEKS-UpdateClusterConfig-request-zonalShiftConfig"></a>
Enable or disable ARC zonal shift for the cluster. If zonal shift is enabled, AWS configures zonal autoshift for the cluster.  
Zonal shift is a feature of Amazon Application Recovery Controller (ARC). ARC zonal shift is designed to be a temporary measure that allows you to move traffic for a resource away from an impaired AZ until the zonal shift expires or you cancel it. You can extend the zonal shift if necessary.  
You can start a zonal shift for an EKS cluster, or you can allow AWS to do it for you by enabling *zonal autoshift*. This shift updates the flow of east-to-west network traffic in your cluster to only consider network endpoints for Pods running on worker nodes in healthy AZs. Additionally, any ALB or NLB handling ingress traffic for applications in your EKS cluster will automatically route traffic to targets in the healthy AZs. For more information about zonal shift in EKS, see [Learn about Amazon Application Recovery Controller (ARC) Zonal Shift in Amazon EKS](https://docs.aws.amazon.com/eks/latest/userguide/zone-shift.html) in the * *Amazon EKS User Guide* *.  
Type: [ZonalShiftConfigRequest](API_ZonalShiftConfigRequest.md) object  
Required: No

## Response Syntax
<a name="API_UpdateClusterConfig_ResponseSyntax"></a>

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
<a name="API_UpdateClusterConfig_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [update](#API_UpdateClusterConfig_ResponseSyntax) **   <a name="AmazonEKS-UpdateClusterConfig-response-update"></a>
An object representing an asynchronous update.  
Type: [Update](API_Update.md) object

## Errors
<a name="API_UpdateClusterConfig_Errors"></a>

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
<a name="API_UpdateClusterConfig_Examples"></a>

In the following example or examples, the Authorization header contents (`AUTHPARAMS`) must be replaced with an AWS Signature Version 4 signature. For more information about creating these signatures, see [Signature Version 4 Signing Process](https://docs.aws.amazon.com/general/latest/gr/signature-version-4.html) in the *Amazon EKS General Reference*.

You need to learn how to sign HTTP requests only if you intend to manually create them. When you use the [AWS Command Line Interface (AWS CLI)](http://aws.amazon.com/cli/) or one of the [AWS SDKs](http://aws.amazon.com/tools/) to make requests to AWS, these tools automatically sign the requests for you with the access key that you specify when you configure the tools. When you use these tools, you don't need to learn how to sign requests yourself.

### Example
<a name="API_UpdateClusterConfig_Example_1"></a>

The following example disables the Amazon EKS public API server endpoint for the `my-cluster` cluster.

#### Sample Request
<a name="API_UpdateClusterConfig_Example_1_Request"></a>

```
POST /clusters/my-cluster/update-config HTTP/1.1
Host: eks.us-west-2.amazonaws.com
Accept-Encoding: identity
User-Agent: aws-cli/1.16.56 Python/3.7.0 Darwin/17.7.0 botocore/1.12.46
X-Amz-Date: 20190228T215632Z
Authorization: AUTHPARAMS

{
  "resourcesVpcConfig": {
    "endpointPublicAccess": false
  },
  "clientRequestToken": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx"
}
```

#### Sample Response
<a name="API_UpdateClusterConfig_Example_1_Response"></a>

```
HTTP/1.1 200 OK
Date: Thu, 28 Feb 2019 21:56:33 GMT
Content-Type: application/json
Content-Length: 254
x-amzn-RequestId: xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxx
x-amz-apigw-id: V1LanEMJPHcFvTg=
X-Amzn-Trace-Id: Root=1-xxxxxxxxx-xxxxxxxxxxxxxxxxxxxxxxxx
Connection: keep-alive

{
  "update": {
    "id": "71abb011-b524-4983-b17f-c30baa1b5530",
    "status": "InProgress",
    "type": "EndpointAccessUpdate",
    "params": [
      {
        "type": "EndpointPublicAccess",
        "value": "false"
      },
      {
        "type": "EndpointPrivateAccess",
        "value": "true"
      }
    ],
    "createdAt": 1551390993.374,
    "errors": []
  }
}
```

### Example
<a name="API_UpdateClusterConfig_Example_2"></a>

The following example enables exporting all cluster control plane logs to CloudWatch Logs.

#### Sample Request
<a name="API_UpdateClusterConfig_Example_2_Request"></a>

```
POST /clusters/my-cluster/update-config HTTP/1.1
Host: eks.us-west-2.amazonaws.com
Accept-Encoding: identity
User-Agent: aws-cli/1.16.120 Python/3.7.0 Darwin/18.2.0 botocore/1.12.110
X-Amz-Date: 20190322T162335Z
Authorization: AUTHPARAMS

{
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
        "enabled": true
      }
    ]
  },
  "clientRequestToken": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx"
}
```

#### Sample Response
<a name="API_UpdateClusterConfig_Example_2_Response"></a>

```
HTTP/1.1 200 OK
Date: Fri, 22 Mar 2019 16:23:34 GMT
Content-Type: application/json
Content-Length: 313
x-amzn-RequestId: xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxx
x-amz-apigw-id: W87Q5HlCvHcFxDA=
X-Amzn-Trace-Id: Root=1-xxxxxxxxx-xxxxxxxxxxxxxxxxxxxxxxxx
Connection: keep-alive

{
  "update": {
    "id": "883405c8-65c6-4758-8cee-2a7c1340a6d9",
    "status": "InProgress",
    "type": "LoggingUpdate",
    "params": [
      {
        "type": "ClusterLogging",
        "value": "{\"clusterLogging\":[{\"types\":[\"api\",\"audit\",\"authenticator\",\"controllerManager\",\"scheduler\"],\"enabled\":true}]}"
      }
    ],
    "createdAt": 1553271814.684,
    "errors": []
  }
}
```

## See Also
<a name="API_UpdateClusterConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/eks-2017-11-01/UpdateClusterConfig) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/eks-2017-11-01/UpdateClusterConfig) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/eks-2017-11-01/UpdateClusterConfig) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/eks-2017-11-01/UpdateClusterConfig) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/eks-2017-11-01/UpdateClusterConfig) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/eks-2017-11-01/UpdateClusterConfig) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/eks-2017-11-01/UpdateClusterConfig) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/eks-2017-11-01/UpdateClusterConfig) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/eks-2017-11-01/UpdateClusterConfig) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/eks-2017-11-01/UpdateClusterConfig) 