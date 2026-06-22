---
id: "@specs/aws/eks/docs/API_DeleteFargateProfile"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS DeleteFargateProfile"
status: active
depends_on:
  - "@specs/aws/eks/meta"
---

# DeleteFargateProfile

> **source:** AWS Documentation
> **spec:id:** @specs/aws/eks/docs/API_DeleteFargateProfile
> **target_lang:** meta — documentation tier. ALL sections preserved.



# DeleteFargateProfile
<a name="API_DeleteFargateProfile"></a>

Deletes an AWS Fargate profile.

When you delete a Fargate profile, any `Pod` running on Fargate that was created with the profile is deleted. If the `Pod` matches another Fargate profile, then it is scheduled on Fargate with that profile. If it no longer matches any Fargate profiles, then it's not scheduled on Fargate and may remain in a pending state.

Only one Fargate profile in a cluster can be in the `DELETING` status at a time. You must wait for a Fargate profile to finish deleting before you can delete any other profiles in that cluster.

## Request Syntax
<a name="API_DeleteFargateProfile_RequestSyntax"></a>

```
DELETE /clusters/{{name}}/fargate-profiles/{{fargateProfileName}} HTTP/1.1
```

## URI Request Parameters
<a name="API_DeleteFargateProfile_RequestParameters"></a>

The request uses the following URI parameters.

 ** [name](#API_DeleteFargateProfile_RequestSyntax) **   <a name="AmazonEKS-DeleteFargateProfile-request-uri-clusterName"></a>
The name of your cluster.  
Required: Yes

 ** [fargateProfileName](#API_DeleteFargateProfile_RequestSyntax) **   <a name="AmazonEKS-DeleteFargateProfile-request-uri-fargateProfileName"></a>
The name of the Fargate profile to delete.  
Required: Yes

## Request Body
<a name="API_DeleteFargateProfile_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_DeleteFargateProfile_ResponseSyntax"></a>

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
<a name="API_DeleteFargateProfile_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [fargateProfile](#API_DeleteFargateProfile_ResponseSyntax) **   <a name="AmazonEKS-DeleteFargateProfile-response-fargateProfile"></a>
The deleted Fargate profile.  
Type: [FargateProfile](API_FargateProfile.md) object

## Errors
<a name="API_DeleteFargateProfile_Errors"></a>

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
<a name="API_DeleteFargateProfile_Examples"></a>

In the following example or examples, the Authorization header contents (`AUTHPARAMS`) must be replaced with an AWS Signature Version 4 signature. For more information about creating these signatures, see [Signature Version 4 Signing Process](https://docs.aws.amazon.com/general/latest/gr/signature-version-4.html) in the *Amazon EKS General Reference*.

You need to learn how to sign HTTP requests only if you intend to manually create them. When you use the [AWS Command Line Interface (AWS CLI)](http://aws.amazon.com/cli/) or one of the [AWS SDKs](http://aws.amazon.com/tools/) to make requests to AWS, these tools automatically sign the requests for you with the access key that you specify when you configure the tools. When you use these tools, you don't need to learn how to sign requests yourself.

### Example
<a name="API_DeleteFargateProfile_Example_1"></a>

The following example deletes a Fargate profile called `compute-label` in the `fargate` cluster.

#### Sample Request
<a name="API_DeleteFargateProfile_Example_1_Request"></a>

```
DELETE /clusters/fargate/fargate-profiles/compute-label HTTP/1.1
Host: eks.us-west-2.amazonaws.com
Accept-Encoding: identity
User-Agent: aws-cli/1.16.284 Python/3.7.5 Darwin/18.7.0 botocore/1.13.20
X-Amz-Date: 20191120T203729Z
Authorization: AUTHPARAMS
Content-Length: 0
```

#### Sample Response
<a name="API_DeleteFargateProfile_Example_1_Response"></a>

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
    "status": "DELETING",
    "tags": {}
  }
}
```

## See Also
<a name="API_DeleteFargateProfile_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/eks-2017-11-01/DeleteFargateProfile) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/eks-2017-11-01/DeleteFargateProfile) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/eks-2017-11-01/DeleteFargateProfile) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/eks-2017-11-01/DeleteFargateProfile) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/eks-2017-11-01/DeleteFargateProfile) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/eks-2017-11-01/DeleteFargateProfile) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/eks-2017-11-01/DeleteFargateProfile) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/eks-2017-11-01/DeleteFargateProfile) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/eks-2017-11-01/DeleteFargateProfile) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/eks-2017-11-01/DeleteFargateProfile) 