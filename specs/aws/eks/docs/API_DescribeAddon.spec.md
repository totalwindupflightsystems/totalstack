---
id: "@specs/aws/eks/docs/API_DescribeAddon"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS DescribeAddon"
status: active
depends_on:
  - "@specs/aws/eks/meta"
---

# DescribeAddon

> **source:** AWS Documentation
> **spec:id:** @specs/aws/eks/docs/API_DescribeAddon
> **target_lang:** meta — documentation tier. ALL sections preserved.



# DescribeAddon
<a name="API_DescribeAddon"></a>

Describes an Amazon EKS add-on.

## Request Syntax
<a name="API_DescribeAddon_RequestSyntax"></a>

```
GET /clusters/{{name}}/addons/{{addonName}} HTTP/1.1
```

## URI Request Parameters
<a name="API_DescribeAddon_RequestParameters"></a>

The request uses the following URI parameters.

 ** [addonName](#API_DescribeAddon_RequestSyntax) **   <a name="AmazonEKS-DescribeAddon-request-uri-addonName"></a>
The name of the add-on. The name must match one of the names returned by [https://docs.aws.amazon.com/eks/latest/APIReference/API_ListAddons.html](https://docs.aws.amazon.com/eks/latest/APIReference/API_ListAddons.html).  
Required: Yes

 ** [name](#API_DescribeAddon_RequestSyntax) **   <a name="AmazonEKS-DescribeAddon-request-uri-clusterName"></a>
The name of your cluster.  
Length Constraints: Minimum length of 1. Maximum length of 100.  
Pattern: `^[0-9A-Za-z][A-Za-z0-9\-_]*`   
Required: Yes

## Request Body
<a name="API_DescribeAddon_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_DescribeAddon_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "addon": { 
      "addonArn": "string",
      "addonName": "string",
      "addonVersion": "string",
      "clusterName": "string",
      "configurationValues": "string",
      "createdAt": number,
      "health": { 
         "issues": [ 
            { 
               "code": "string",
               "message": "string",
               "resourceIds": [ "string" ]
            }
         ]
      },
      "marketplaceInformation": { 
         "productId": "string",
         "productUrl": "string"
      },
      "modifiedAt": number,
      "namespaceConfig": { 
         "namespace": "string"
      },
      "owner": "string",
      "podIdentityAssociations": [ "string" ],
      "publisher": "string",
      "serviceAccountRoleArn": "string",
      "status": "string",
      "tags": { 
         "string" : "string" 
      }
   }
}
```

## Response Elements
<a name="API_DescribeAddon_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [addon](#API_DescribeAddon_ResponseSyntax) **   <a name="AmazonEKS-DescribeAddon-response-addon"></a>
An Amazon EKS add-on. For more information, see [Amazon EKS add-ons](https://docs.aws.amazon.com/eks/latest/userguide/eks-add-ons.html) in the *Amazon EKS User Guide*.  
Type: [Addon](API_Addon.md) object

## Errors
<a name="API_DescribeAddon_Errors"></a>

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
<a name="API_DescribeAddon_Examples"></a>

In the following example or examples, the Authorization header contents (`AUTHPARAMS`) must be replaced with an AWS Signature Version 4 signature. For more information about creating these signatures, see [Signature Version 4 Signing Process](https://docs.aws.amazon.com/general/latest/gr/signature-version-4.html) in the *Amazon EKS General Reference*.

You need to learn how to sign HTTP requests only if you intend to manually create them. When you use the [AWS Command Line Interface (AWS CLI)](http://aws.amazon.com/cli/) or one of the [AWS SDKs](http://aws.amazon.com/tools/) to make requests to AWS, these tools automatically sign the requests for you with the access key that you specify when you configure the tools. When you use these tools, you don't need to learn how to sign requests yourself.

### Example
<a name="API_DescribeAddon_Example_1"></a>

The following example describes an add-on named `vpc-cni`.

#### Sample Request
<a name="API_DescribeAddon_Example_1_Request"></a>

```
GET /clusters/1-18/addons/vpc-cni HTTP/1.1
Host: eks.us-west-2.amazonaws.com
Accept-Encoding: identity
User-Agent: aws-cli/1.16.298 Python/3.6.0 Windows/10 botocore/1.13.34
X-Amz-Date: 20201125T144831Z
Authorization: AUTHPARAMS
```

#### Sample Response
<a name="API_DescribeAddon_Example_1_Response"></a>

```
HTTP/1.1 200 OK
Date: Wed, 25 Nov 2020 14:48:32 GMT
Content-Type: application/json
Content-Length: 472
x-amzn-RequestId: xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxx
x-amz-apigw-id: WkY-BEEPPHcFwEg=
X-Amzn-Trace-Id: Root=1-xxxxxxxxx-xxxxxxxxxxxxxxxxxxxxxxxx
Connection: keep-alive

{
  "addon" : {
    "addonName" : "vpc-cni",
    "clusterName" : "1-18",
    "status" : "ACTIVE",
    "addonVersion" : "v1.7.5-eksbuild.1",
    "health" : {
      "issues" : [ ]
    },
    "addonArn" : "arn:aws:eks:us-west-2:012345678910:addon/my-cluster/vpc-cni/xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
    "createdAt" : 1.606315184255E9,
    "modifiedAt" : 1.606315202754E9,
    "serviceAccountRoleArn" : "arn:aws:iam::012345678910:role/AmazonEKSCNIRole",
    "tags" : { }
  }
}
```

## See Also
<a name="API_DescribeAddon_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/eks-2017-11-01/DescribeAddon) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/eks-2017-11-01/DescribeAddon) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/eks-2017-11-01/DescribeAddon) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/eks-2017-11-01/DescribeAddon) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/eks-2017-11-01/DescribeAddon) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/eks-2017-11-01/DescribeAddon) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/eks-2017-11-01/DescribeAddon) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/eks-2017-11-01/DescribeAddon) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/eks-2017-11-01/DescribeAddon) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/eks-2017-11-01/DescribeAddon) 