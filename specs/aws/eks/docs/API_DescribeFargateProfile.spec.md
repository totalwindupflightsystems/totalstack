---
id: "@specs/aws/eks/docs/API_DescribeFargateProfile"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS DescribeFargateProfile"
status: active
depends_on:
  - "@specs/aws/eks/meta"
---

# DescribeFargateProfile

> **source:** AWS Documentation
> **spec:id:** @specs/aws/eks/docs/API_DescribeFargateProfile
> **target_lang:** meta — documentation tier. ALL sections preserved.



# DescribeFargateProfile
<a name="API_DescribeFargateProfile"></a>

Describes an AWS Fargate profile.

## Request Syntax
<a name="API_DescribeFargateProfile_RequestSyntax"></a>

```
GET /clusters/{{name}}/fargate-profiles/{{fargateProfileName}} HTTP/1.1
```

## URI Request Parameters
<a name="API_DescribeFargateProfile_RequestParameters"></a>

The request uses the following URI parameters.

 ** [name](#API_DescribeFargateProfile_RequestSyntax) **   <a name="AmazonEKS-DescribeFargateProfile-request-uri-clusterName"></a>
The name of your cluster.  
Required: Yes

 ** [fargateProfileName](#API_DescribeFargateProfile_RequestSyntax) **   <a name="AmazonEKS-DescribeFargateProfile-request-uri-fargateProfileName"></a>
The name of the Fargate profile to describe.  
Required: Yes

## Request Body
<a name="API_DescribeFargateProfile_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_DescribeFargateProfile_ResponseSyntax"></a>

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
<a name="API_DescribeFargateProfile_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [fargateProfile](#API_DescribeFargateProfile_ResponseSyntax) **   <a name="AmazonEKS-DescribeFargateProfile-response-fargateProfile"></a>
The full description of your Fargate profile.  
Type: [FargateProfile](API_FargateProfile.md) object

## Errors
<a name="API_DescribeFargateProfile_Errors"></a>

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
<a name="API_DescribeFargateProfile_Examples"></a>

In the following example or examples, the Authorization header contents (`AUTHPARAMS`) must be replaced with an AWS Signature Version 4 signature. For more information about creating these signatures, see [Signature Version 4 Signing Process](https://docs.aws.amazon.com/general/latest/gr/signature-version-4.html) in the *Amazon EKS General Reference*.

You need to learn how to sign HTTP requests only if you intend to manually create them. When you use the [AWS Command Line Interface (AWS CLI)](http://aws.amazon.com/cli/) or one of the [AWS SDKs](http://aws.amazon.com/tools/) to make requests to AWS, these tools automatically sign the requests for you with the access key that you specify when you configure the tools. When you use these tools, you don't need to learn how to sign requests yourself.

### Example
<a name="API_DescribeFargateProfile_Example_1"></a>

The following example describes a Fargate profile named `default-with-infrastructure-label` in the `my-cluster` cluster.

#### Sample Request
<a name="API_DescribeFargateProfile_Example_1_Request"></a>

```
GET /clusters/my-cluster/fargate-profiles/default-with-infrastructure-label HTTP/1.1
Host: eks.us-west-2.amazonaws.com
Accept-Encoding: identity
User-Agent: aws-cli/1.16.284 Python/3.7.5 Darwin/18.7.0 botocore/1.13.20
X-Amz-Date: 20191120T204303Z
Authorization: AUTHPARAMS
```

#### Sample Response
<a name="API_DescribeFargateProfile_Example_1_Response"></a>

```
HTTP/1.1 200 OK
Date: Wed, 20 Nov 2019 20:43:04 GMT
Content-Type: application/json
Content-Length: 651
x-amzn-RequestId: xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxx
x-amz-apigw-id: DebFwF0YPHcFkog=
X-Amzn-Trace-Id: Root=1-xxxxxxxxx-xxxxxxxxxxxxxxxxxxxxxxxx
Connection: keep-alive

{
  "fargateProfile": {
    "fargateProfileName": "default-with-infrastructure-label",
    "fargateProfileArn": "arn:aws:eks:us-west-2:012345678910:fargateprofile/my-cluster/default-with-infrastructure-label/xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
    "clusterName": "fargate",
    "createdAt": 1574281537.866,
    "podExecutionRoleArn": "arn:aws:iam::012345678910:role/AmazonEKSFargatePodExecutionRole",
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
    "status": "ACTIVE",
    "tags": {}
  }
}
```

## See Also
<a name="API_DescribeFargateProfile_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/eks-2017-11-01/DescribeFargateProfile) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/eks-2017-11-01/DescribeFargateProfile) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/eks-2017-11-01/DescribeFargateProfile) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/eks-2017-11-01/DescribeFargateProfile) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/eks-2017-11-01/DescribeFargateProfile) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/eks-2017-11-01/DescribeFargateProfile) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/eks-2017-11-01/DescribeFargateProfile) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/eks-2017-11-01/DescribeFargateProfile) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/eks-2017-11-01/DescribeFargateProfile) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/eks-2017-11-01/DescribeFargateProfile) 