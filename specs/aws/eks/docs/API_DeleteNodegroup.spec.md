---
id: "@specs/aws/eks/docs/API_DeleteNodegroup"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS DeleteNodegroup"
status: active
depends_on:
  - "@specs/aws/eks/meta"
---

# DeleteNodegroup

> **source:** AWS Documentation
> **spec:id:** @specs/aws/eks/docs/API_DeleteNodegroup
> **target_lang:** meta — documentation tier. ALL sections preserved.



# DeleteNodegroup
<a name="API_DeleteNodegroup"></a>

Deletes a managed node group.

## Request Syntax
<a name="API_DeleteNodegroup_RequestSyntax"></a>

```
DELETE /clusters/{{name}}/node-groups/{{nodegroupName}} HTTP/1.1
```

## URI Request Parameters
<a name="API_DeleteNodegroup_RequestParameters"></a>

The request uses the following URI parameters.

 ** [name](#API_DeleteNodegroup_RequestSyntax) **   <a name="AmazonEKS-DeleteNodegroup-request-uri-clusterName"></a>
The name of your cluster.  
Required: Yes

 ** [nodegroupName](#API_DeleteNodegroup_RequestSyntax) **   <a name="AmazonEKS-DeleteNodegroup-request-uri-nodegroupName"></a>
The name of the node group to delete.  
Required: Yes

## Request Body
<a name="API_DeleteNodegroup_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_DeleteNodegroup_ResponseSyntax"></a>

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
<a name="API_DeleteNodegroup_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [nodegroup](#API_DeleteNodegroup_ResponseSyntax) **   <a name="AmazonEKS-DeleteNodegroup-response-nodegroup"></a>
The full description of your deleted node group.  
Type: [Nodegroup](API_Nodegroup.md) object

## Errors
<a name="API_DeleteNodegroup_Errors"></a>

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
<a name="API_DeleteNodegroup_Examples"></a>

In the following example or examples, the Authorization header contents (`AUTHPARAMS`) must be replaced with an AWS Signature Version 4 signature. For more information about creating these signatures, see [Signature Version 4 Signing Process](https://docs.aws.amazon.com/general/latest/gr/signature-version-4.html) in the *Amazon EKS General Reference*.

You need to learn how to sign HTTP requests only if you intend to manually create them. When you use the [AWS Command Line Interface (AWS CLI)](http://aws.amazon.com/cli/) or one of the [AWS SDKs](http://aws.amazon.com/tools/) to make requests to AWS, these tools automatically sign the requests for you with the access key that you specify when you configure the tools. When you use these tools, you don't need to learn how to sign requests yourself.

### Example
<a name="API_DeleteNodegroup_Example_1"></a>

This example deletes a managed node group called `standard` in the `my-cluster` cluster.

#### Sample Request
<a name="API_DeleteNodegroup_Example_1_Request"></a>

```
DELETE /clusters/my-cluster/node-groups/standard HTTP/1.1
Host: eks.us-west-2.amazonaws.com
Accept-Encoding: identity
User-Agent: aws-cli/1.16.275 Python/3.7.4 Darwin/18.7.0 botocore/1.13.11
X-Amz-Date: 20191111T202821Z
Authorization: AUTHPARAMS
Content-Length: 0
```

#### Sample Response
<a name="API_DeleteNodegroup_Example_1_Response"></a>

```
HTTP/1.1 200 OK
Date: Mon, 11 Nov 2019 20:28:22 GMT
Content-Type: application/json
Content-Length: 1121
x-amzn-RequestId: xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxx
x-amz-apigw-id: DAuf9GbEPHcFxNw=
X-Amzn-Trace-Id: Root=1-xxxxxxxxx-xxxxxxxxxxxxxxxxxxxxxxxx
Connection: keep-alive

{
  "nodegroup" : {
    "nodegroupName" : "standard",
    "nodegroupArn" : "arn:aws:eks:us-west-2:012345678910:nodegroup/my-cluster/standard/xxxxxxxx-xxxx-xxxx-xxxxxxxxxxxxxxxxx",
    "clusterName" : "my-cluster",
    "version" : "1.14",
    "releaseVersion" : "1.14.7-20190927",
    "createdAt" : 1.573496875151E9,
    "modifiedAt" : 1.573504102097E9,
    "status" : "DELETING",
    "scalingConfig" : {
      "minSize" : 2,
      "maxSize" : 6,
      "desiredSize" : 4
    },
    "instanceTypes" : [ "t3.medium" ],
    "subnets" : [ "subnet-xxxxxxxxxxxxxxxxx", "subnet-yyyyyyyyyyyyyyyyy", "subnet-zzzzzzzzzzzzzzzzz" ],
    "remoteAccess" : {
      "ec2SshKey" : "id_rsa",
      "sourceSecurityGroups" : null
    },
    "amiType" : "AL2_x86_64",
    "nodeRole" : "arn:aws:iam::012345678910:role/managed-NodeInstanceRole-1V94UAUPQY7GS",
    "labels" : { },
    "resources" : {
      "autoScalingGroups" : [ {
        "name" : "eks-xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx"
      } ],
      "remoteAccessSecurityGroup" : "sg-xxxxxxxxxxxxxxxxx"
    },
    "diskSize" : 20,
    "health" : {
      "issues" : [ ]
    },
    "tags" : { }
  }
}
```

## See Also
<a name="API_DeleteNodegroup_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/eks-2017-11-01/DeleteNodegroup) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/eks-2017-11-01/DeleteNodegroup) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/eks-2017-11-01/DeleteNodegroup) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/eks-2017-11-01/DeleteNodegroup) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/eks-2017-11-01/DeleteNodegroup) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/eks-2017-11-01/DeleteNodegroup) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/eks-2017-11-01/DeleteNodegroup) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/eks-2017-11-01/DeleteNodegroup) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/eks-2017-11-01/DeleteNodegroup) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/eks-2017-11-01/DeleteNodegroup) 