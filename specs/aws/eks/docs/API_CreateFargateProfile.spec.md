---
id: "@specs/aws/eks/docs/API_CreateFargateProfile"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS CreateFargateProfile"
status: active
depends_on:
  - "@specs/aws/eks/meta"
---

# CreateFargateProfile

> **source:** AWS Documentation
> **spec:id:** @specs/aws/eks/docs/API_CreateFargateProfile
> **target_lang:** meta — documentation tier. ALL sections preserved.



# CreateFargateProfile
<a name="API_CreateFargateProfile"></a>

Creates an AWS Fargate profile for your Amazon EKS cluster. You must have at least one Fargate profile in a cluster to be able to run pods on Fargate.

The Fargate profile allows an administrator to declare which pods run on Fargate and specify which pods run on which Fargate profile. This declaration is done through the profile's selectors. Each profile can have up to five selectors that contain a namespace and labels. A namespace is required for every selector. The label field consists of multiple optional key-value pairs. Pods that match the selectors are scheduled on Fargate. If a to-be-scheduled pod matches any of the selectors in the Fargate profile, then that pod is run on Fargate.

When you create a Fargate profile, you must specify a pod execution role to use with the pods that are scheduled with the profile. This role is added to the cluster's Kubernetes [Role Based Access Control](https://kubernetes.io/docs/reference/access-authn-authz/rbac/) (RBAC) for authorization so that the `kubelet` that is running on the Fargate infrastructure can register with your Amazon EKS cluster so that it can appear in your cluster as a node. The pod execution role also provides IAM permissions to the Fargate infrastructure to allow read access to Amazon ECR image repositories. For more information, see [Pod Execution Role](https://docs.aws.amazon.com/eks/latest/userguide/pod-execution-role.html) in the *Amazon EKS User Guide*.

Fargate profiles are immutable. However, you can create a new updated profile to replace an existing profile and then delete the original after the updated profile has finished creating.

If any Fargate profiles in a cluster are in the `DELETING` status, you must wait for that Fargate profile to finish deleting before you can create any other profiles in that cluster.

For more information, see [AWS Fargate profile](https://docs.aws.amazon.com/eks/latest/userguide/fargate-profile.html) in the *Amazon EKS User Guide*.

## Request Syntax
<a name="API_CreateFargateProfile_RequestSyntax"></a>

```
POST /clusters/{{name}}/fargate-profiles HTTP/1.1
Content-type: application/json

{
   "clientRequestToken": "{{string}}",
   "fargateProfileName": "{{string}}",
   "podExecutionRoleArn": "{{string}}",
   "selectors": [ 
      { 
         "labels": { 
            "{{string}}" : "{{string}}" 
         },
         "namespace": "{{string}}"
      }
   ],
   "subnets": [ "{{string}}" ],
   "tags": { 
      "{{string}}" : "{{string}}" 
   }
}
```

## URI Request Parameters
<a name="API_CreateFargateProfile_RequestParameters"></a>

The request uses the following URI parameters.

 ** [name](#API_CreateFargateProfile_RequestSyntax) **   <a name="AmazonEKS-CreateFargateProfile-request-uri-clusterName"></a>
The name of your cluster.  
Required: Yes

## Request Body
<a name="API_CreateFargateProfile_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [clientRequestToken](#API_CreateFargateProfile_RequestSyntax) **   <a name="AmazonEKS-CreateFargateProfile-request-clientRequestToken"></a>
A unique, case-sensitive identifier that you provide to ensure the idempotency of the request.  
Type: String  
Required: No

 ** [fargateProfileName](#API_CreateFargateProfile_RequestSyntax) **   <a name="AmazonEKS-CreateFargateProfile-request-fargateProfileName"></a>
The name of the Fargate profile.  
Type: String  
Required: Yes

 ** [podExecutionRoleArn](#API_CreateFargateProfile_RequestSyntax) **   <a name="AmazonEKS-CreateFargateProfile-request-podExecutionRoleArn"></a>
The Amazon Resource Name (ARN) of the `Pod` execution role to use for a `Pod` that matches the selectors in the Fargate profile. The `Pod` execution role allows Fargate infrastructure to register with your cluster as a node, and it provides read access to Amazon ECR image repositories. For more information, see [`Pod` execution role](https://docs.aws.amazon.com/eks/latest/userguide/pod-execution-role.html) in the *Amazon EKS User Guide*.  
Type: String  
Required: Yes

 ** [selectors](#API_CreateFargateProfile_RequestSyntax) **   <a name="AmazonEKS-CreateFargateProfile-request-selectors"></a>
The selectors to match for a `Pod` to use this Fargate profile. Each selector must have an associated Kubernetes `namespace`. Optionally, you can also specify `labels` for a `namespace`. You may specify up to five selectors in a Fargate profile.  
Type: Array of [FargateProfileSelector](API_FargateProfileSelector.md) objects  
Required: No

 ** [subnets](#API_CreateFargateProfile_RequestSyntax) **   <a name="AmazonEKS-CreateFargateProfile-request-subnets"></a>
The IDs of subnets to launch a `Pod` into. A `Pod` running on Fargate isn't assigned a public IP address, so only private subnets (with no direct route to an Internet Gateway) are accepted for this parameter.  
Type: Array of strings  
Required: No

 ** [tags](#API_CreateFargateProfile_RequestSyntax) **   <a name="AmazonEKS-CreateFargateProfile-request-tags"></a>
Metadata that assists with categorization and organization. Each tag consists of a key and an optional value. You define both. Tags don't propagate to any other cluster or AWS resources.  
Type: String to string map  
Map Entries: Maximum number of 50 items.  
Key Length Constraints: Minimum length of 1. Maximum length of 128.  
Value Length Constraints: Maximum length of 256.  
Required: No

## Response Syntax
<a name="API_CreateFargateProfile_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "fargateProfile": { 
      "clusterName": "string",
      "createdAt": number,
      "fargateProfileArn": "string",
      "fargateProfileName": "string",
      "health": { 
         "issues": [ 
            { 
               "code": "string",
               "message": "string",
               "resourceIds": [ "string" ]
            }
         ]
      },
      "podExecutionRoleArn": "string",
      "selectors": [ 
         { 
            "labels": { 
               "string" : "string" 
            },
            "namespace": "string"
         }
      ],
      "status": "string",
      "subnets": [ "string" ],
      "tags": { 
         "string" : "string" 
      }
   }
}
```

## Response Elements
<a name="API_CreateFargateProfile_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [fargateProfile](#API_CreateFargateProfile_ResponseSyntax) **   <a name="AmazonEKS-CreateFargateProfile-response-fargateProfile"></a>
The full description of your new Fargate profile.  
Type: [FargateProfile](API_FargateProfile.md) object

## Errors
<a name="API_CreateFargateProfile_Errors"></a>

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
<a name="API_CreateFargateProfile_Examples"></a>

In the following example or examples, the Authorization header contents (`AUTHPARAMS`) must be replaced with an AWS Signature Version 4 signature. For more information about creating these signatures, see [Signature Version 4 Signing Process](https://docs.aws.amazon.com/general/latest/gr/signature-version-4.html) in the *Amazon EKS General Reference*.

You need to learn how to sign HTTP requests only if you intend to manually create them. When you use the [AWS Command Line Interface (AWS CLI)](http://aws.amazon.com/cli/) or one of the [AWS SDKs](http://aws.amazon.com/tools/) to make requests to AWS, these tools automatically sign the requests for you with the access key that you specify when you configure the tools. When you use these tools, you don't need to learn how to sign requests yourself.

### Example
<a name="API_CreateFargateProfile_Example_1"></a>

The following example creates a Fargate profile called `default-with-infrastructure-label` in the `fargate` cluster. Any `Pod` launched in the `default` `namespace` with the Kubernetes `label` `"infrastructure": "fargate"` is run on Fargate.

#### Sample Request
<a name="API_CreateFargateProfile_Example_1_Request"></a>

```
POST /clusters/fargate/fargate-profiles HTTP/1.1
Host: eks.us-west-2.amazonaws.com
Accept-Encoding: identity
User-Agent: aws-cli/1.16.284 Python/3.7.5 Darwin/18.7.0 botocore/1.13.20
X-Amz-Date: 20191120T202529Z
Authorization: AUTHPARAMS
Content-Length: 355

{
  "fargateProfileName": "default-with-infrastructure-label",
  "podExecutionRoleArn": "arn:aws:iam::012345678910:role/AmazonEKSPodExecutionRole",
  "subnets": [
    "subnet-xxxxxxxxxxxxxxxxx",
    "subnet-yyyyyyyyyyyyyyyyy"
  ],
  "selectors": [
    {
      "namespace": "default",
      "labels": {
        "infrastructure": "fargate"
      }
    }
  ],
  "clientRequestToken": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx"
}
```

#### Sample Response
<a name="API_CreateFargateProfile_Example_1_Response"></a>

```
HTTP/1.1 200 OK
Date: Wed, 20 Nov 2019 20:37:30 GMT
Content-Type: application/json
Content-Length: 610
x-amzn-RequestId: xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxx
x-amz-apigw-id: DeaRjFWPvHcFcXw=
X-Amzn-Trace-Id: Root=1-xxxxxxxxx-xxxxxxxxxxxxxxxxxxxxxxxx
Connection: keep-alive

{
  "fargateProfile": {
    "fargateProfileName": "compute-label",
    "fargateProfileArn": "arn:aws:eks:us-west-2:012345678910:fargateprofile/fargate/compute-label/xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
    "clusterName": "fargate",
    "createdAt": 1574206849.791,
    "podExecutionRoleArn": "arn:aws:iam::012345678910:role/AmazonEKSPodExecutionRole",
    "subnets": [
      "subnet-xxxxxxxxxxxxxxxxx",
      "subnet-yyyyyyyyyyyyyyyyy"
    ],
    "selectors": [
      {
        "namespace": "kube-system",
        "labels": {
          "compute": "fargate"
        }
      }
    ],
    "status": "CREATING",
    "tags": {}
  }
}
```

## See Also
<a name="API_CreateFargateProfile_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/eks-2017-11-01/CreateFargateProfile) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/eks-2017-11-01/CreateFargateProfile) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/eks-2017-11-01/CreateFargateProfile) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/eks-2017-11-01/CreateFargateProfile) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/eks-2017-11-01/CreateFargateProfile) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/eks-2017-11-01/CreateFargateProfile) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/eks-2017-11-01/CreateFargateProfile) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/eks-2017-11-01/CreateFargateProfile) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/eks-2017-11-01/CreateFargateProfile) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/eks-2017-11-01/CreateFargateProfile) 