---
id: "@specs/aws/eks/docs/API_UpdateNodegroupConfig"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS UpdateNodegroupConfig"
status: active
depends_on:
  - "@specs/aws/eks/meta"
---

# UpdateNodegroupConfig

> **source:** AWS Documentation
> **spec:id:** @specs/aws/eks/docs/API_UpdateNodegroupConfig
> **target_lang:** meta — documentation tier. ALL sections preserved.



# UpdateNodegroupConfig
<a name="API_UpdateNodegroupConfig"></a>

Updates an Amazon EKS managed node group configuration. Your node group continues to function during the update. The response output includes an update ID that you can use to track the status of your node group update with the [https://docs.aws.amazon.com/eks/latest/APIReference/API_DescribeUpdate.html](https://docs.aws.amazon.com/eks/latest/APIReference/API_DescribeUpdate.html) API operation. You can update the Kubernetes labels and taints for a node group and the scaling and version update configuration.

## Request Syntax
<a name="API_UpdateNodegroupConfig_RequestSyntax"></a>

```
POST /clusters/{{name}}/node-groups/{{nodegroupName}}/update-config HTTP/1.1
Content-type: application/json

{
   "clientRequestToken": "{{string}}",
   "labels": { 
      "addOrUpdateLabels": { 
         "{{string}}" : "{{string}}" 
      },
      "removeLabels": [ "{{string}}" ]
   },
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
   "scalingConfig": { 
      "desiredSize": {{number}},
      "maxSize": {{number}},
      "minSize": {{number}}
   },
   "taints": { 
      "addOrUpdateTaints": [ 
         { 
            "effect": "{{string}}",
            "key": "{{string}}",
            "value": "{{string}}"
         }
      ],
      "removeTaints": [ 
         { 
            "effect": "{{string}}",
            "key": "{{string}}",
            "value": "{{string}}"
         }
      ]
   },
   "updateConfig": { 
      "maxUnavailable": {{number}},
      "maxUnavailablePercentage": {{number}},
      "updateStrategy": "{{string}}"
   },
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
<a name="API_UpdateNodegroupConfig_RequestParameters"></a>

The request uses the following URI parameters.

 ** [name](#API_UpdateNodegroupConfig_RequestSyntax) **   <a name="AmazonEKS-UpdateNodegroupConfig-request-uri-clusterName"></a>
The name of your cluster.  
Required: Yes

 ** [nodegroupName](#API_UpdateNodegroupConfig_RequestSyntax) **   <a name="AmazonEKS-UpdateNodegroupConfig-request-uri-nodegroupName"></a>
The name of the managed node group to update.  
Required: Yes

## Request Body
<a name="API_UpdateNodegroupConfig_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [clientRequestToken](#API_UpdateNodegroupConfig_RequestSyntax) **   <a name="AmazonEKS-UpdateNodegroupConfig-request-clientRequestToken"></a>
A unique, case-sensitive identifier that you provide to ensure the idempotency of the request.  
Type: String  
Required: No

 ** [labels](#API_UpdateNodegroupConfig_RequestSyntax) **   <a name="AmazonEKS-UpdateNodegroupConfig-request-labels"></a>
The Kubernetes `labels` to apply to the nodes in the node group after the update.  
Type: [UpdateLabelsPayload](API_UpdateLabelsPayload.md) object  
Required: No

 ** [nodeRepairConfig](#API_UpdateNodegroupConfig_RequestSyntax) **   <a name="AmazonEKS-UpdateNodegroupConfig-request-nodeRepairConfig"></a>
The node auto repair configuration for the node group.  
Type: [NodeRepairConfig](API_NodeRepairConfig.md) object  
Required: No

 ** [scalingConfig](#API_UpdateNodegroupConfig_RequestSyntax) **   <a name="AmazonEKS-UpdateNodegroupConfig-request-scalingConfig"></a>
The scaling configuration details for the Auto Scaling group after the update.  
Type: [NodegroupScalingConfig](API_NodegroupScalingConfig.md) object  
Required: No

 ** [taints](#API_UpdateNodegroupConfig_RequestSyntax) **   <a name="AmazonEKS-UpdateNodegroupConfig-request-taints"></a>
The Kubernetes taints to be applied to the nodes in the node group after the update. For more information, see [Node taints on managed node groups](https://docs.aws.amazon.com/eks/latest/userguide/node-taints-managed-node-groups.html).  
Type: [UpdateTaintsPayload](API_UpdateTaintsPayload.md) object  
Required: No

 ** [updateConfig](#API_UpdateNodegroupConfig_RequestSyntax) **   <a name="AmazonEKS-UpdateNodegroupConfig-request-updateConfig"></a>
The node group update configuration.  
Type: [NodegroupUpdateConfig](API_NodegroupUpdateConfig.md) object  
Required: No

 ** [warmPoolConfig](#API_UpdateNodegroupConfig_RequestSyntax) **   <a name="AmazonEKS-UpdateNodegroupConfig-request-warmPoolConfig"></a>
The warm pool configuration to apply to the node group. You can use this to add a warm pool to an existing node group or modify the settings of an existing warm pool.  
Type: [WarmPoolConfig](API_WarmPoolConfig.md) object  
Required: No

## Response Syntax
<a name="API_UpdateNodegroupConfig_ResponseSyntax"></a>

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
<a name="API_UpdateNodegroupConfig_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [update](#API_UpdateNodegroupConfig_ResponseSyntax) **   <a name="AmazonEKS-UpdateNodegroupConfig-response-update"></a>
An object representing an asynchronous update.  
Type: [Update](API_Update.md) object

## Errors
<a name="API_UpdateNodegroupConfig_Errors"></a>

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

## Examples
<a name="API_UpdateNodegroupConfig_Examples"></a>

### Example
<a name="API_UpdateNodegroupConfig_Example_1"></a>

This example updates the scaling configuration for a node group called `standard` in the `my-cluster` cluster.

#### Sample Request
<a name="API_UpdateNodegroupConfig_Example_1_Request"></a>

```
POST /clusters/my-cluster/node-groups/standard/update-config HTTP/1.1
Host: eks.us-west-2.amazonaws.com
Accept-Encoding: identity
User-Agent: aws-cli/1.16.275 Python/3.7.4 Darwin/18.7.0 botocore/1.13.11
X-Amz-Date: 20191111T202415Z
Authorization: AUTHPARAMS
Content-Length: 127

{
  "scalingConfig": {
    "minSize": 2,
    "desiredSize": 4,
    "maxSize": 6
  },
  "clientRequestToken": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx"
}
```

#### Sample Response
<a name="API_UpdateNodegroupConfig_Example_1_Response"></a>

```
HTTP/1.1 200 OK
Date: Mon, 11 Nov 2019 20:24:16 GMT
Content-Type: application/json
Content-Length: 247
x-amzn-RequestId: xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxx
x-amz-apigw-id: DAt5dGkFPHcFzuQ=
X-Amzn-Trace-Id: Root=1-xxxxxxxxx-xxxxxxxxxxxxxxxxxxxxxxxx
Connection: keep-alive

{
  "update": {
    "id": "4c6c3652-9c56-3c76-86e3-8a3930af1bae",
    "status": "InProgress",
    "type": "ConfigUpdate",
    "params": [
      {
        "type": "MinSize",
        "value": "2"
      },
      {
        "type": "MaxSize",
        "value": "6"
      },
      {
        "type": "DesiredSize",
        "value": "4"
      }
    ],
    "createdAt": 1573503855.887,
    "errors": []
  }
}
```

## See Also
<a name="API_UpdateNodegroupConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/eks-2017-11-01/UpdateNodegroupConfig) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/eks-2017-11-01/UpdateNodegroupConfig) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/eks-2017-11-01/UpdateNodegroupConfig) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/eks-2017-11-01/UpdateNodegroupConfig) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/eks-2017-11-01/UpdateNodegroupConfig) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/eks-2017-11-01/UpdateNodegroupConfig) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/eks-2017-11-01/UpdateNodegroupConfig) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/eks-2017-11-01/UpdateNodegroupConfig) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/eks-2017-11-01/UpdateNodegroupConfig) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/eks-2017-11-01/UpdateNodegroupConfig) 