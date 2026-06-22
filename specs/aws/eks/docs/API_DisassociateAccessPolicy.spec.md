---
id: "@specs/aws/eks/docs/API_DisassociateAccessPolicy"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS DisassociateAccessPolicy"
status: active
depends_on:
  - "@specs/aws/eks/meta"
---

# DisassociateAccessPolicy

> **source:** AWS Documentation
> **spec:id:** @specs/aws/eks/docs/API_DisassociateAccessPolicy
> **target_lang:** meta — documentation tier. ALL sections preserved.



# DisassociateAccessPolicy
<a name="API_DisassociateAccessPolicy"></a>

Disassociates an access policy from an access entry.

## Request Syntax
<a name="API_DisassociateAccessPolicy_RequestSyntax"></a>

```
DELETE /clusters/{{name}}/access-entries/{{principalArn}}/access-policies/{{policyArn}} HTTP/1.1
```

## URI Request Parameters
<a name="API_DisassociateAccessPolicy_RequestParameters"></a>

The request uses the following URI parameters.

 ** [name](#API_DisassociateAccessPolicy_RequestSyntax) **   <a name="AmazonEKS-DisassociateAccessPolicy-request-uri-clusterName"></a>
The name of your cluster.  
Required: Yes

 ** [policyArn](#API_DisassociateAccessPolicy_RequestSyntax) **   <a name="AmazonEKS-DisassociateAccessPolicy-request-uri-policyArn"></a>
The ARN of the policy to disassociate from the access entry. For a list of associated policies ARNs, use `ListAssociatedAccessPolicies`.  
Required: Yes

 ** [principalArn](#API_DisassociateAccessPolicy_RequestSyntax) **   <a name="AmazonEKS-DisassociateAccessPolicy-request-uri-principalArn"></a>
The ARN of the IAM principal for the `AccessEntry`.  
Required: Yes

## Request Body
<a name="API_DisassociateAccessPolicy_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_DisassociateAccessPolicy_ResponseSyntax"></a>

```
HTTP/1.1 200
```

## Response Elements
<a name="API_DisassociateAccessPolicy_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_DisassociateAccessPolicy_Errors"></a>

For information about the errors that are common to all actions, see [Common Errors](CommonErrors.md).

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
<a name="API_DisassociateAccessPolicy_Examples"></a>

In the following example or examples, the Authorization header contents (`AUTHPARAMS`) must be replaced with an AWS Signature Version 4 signature. For more information about creating these signatures, see [Signature Version 4 Signing Process](https://docs.aws.amazon.com/general/latest/gr/signature-version-4.html) in the *Amazon EKS General Reference*.

You need to learn how to sign HTTP requests only if you intend to manually create them. When you use the [AWS Command Line Interface (AWS CLI)](http://aws.amazon.com/cli/) or one of the [AWS SDKs](http://aws.amazon.com/tools/) to make requests to AWS, these tools automatically sign the requests for you with the access key that you specify when you configure the tools. When you use these tools, you don't need to learn how to sign requests yourself.

### Example
<a name="API_DisassociateAccessPolicy_Example_1"></a>

The following example disassociates the `AmazonEKSAdminPolicy` from an access entry.

#### Sample Request
<a name="API_DisassociateAccessPolicy_Example_1_Request"></a>

```
DELETE /clusters/my-cluster/access-entries/arn%3Aaws%3Aiam%3A%3A012345678910%3Arole%2Fmy-role/access-policies/arn%3Aaws%3Aeks%3A%3Aaws%3Acluster-access-policy%2FAmazonEKSAdminPolicy HTTP/1.1
Host: eks.us-west-2.amazonaws.com
Accept-Encoding: identity
User-Agent: aws-cli/2.9.0 Python/3.9.11 Windows/10 exe/AMD64 prompt/off command/eks.disassociate-access-policy
X-Amz-Date: 20230531T155944Z
Authorization: AUTHPARAMS
Content-Length: 0
```

#### Sample Response
<a name="API_DisassociateAccessPolicy_Example_1_Response"></a>

```
HTTP/1.1 200 OK
Date: Wed, 31 May 2023 16:00:00 GMT
Content-Type: application/json
Content-Length: 2
x-amzn-RequestId: xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxx
Access-Control-Allow-Origin: *
Access-Control-Allow-Headers: *,Authorization,Date,X-Amz-Date,X-Amz-Security-Token,X-Amz-Target,content-type,x-amz-content-sha256,x-amz-user-agent,x-amzn-platform-id,x-amzn-trace-id
x-amz-apigw-id: Fy5FqGDvPHcFgtw=
Access-Control-Allow-Methods: GET,HEAD,PUT,POST,DELETE,OPTIONS
Access-Control-Expose-Headers: x-amzn-errortype,x-amzn-errormessage,x-amzn-trace-id,x-amzn-requestid,x-amz-apigw-id,date
X-Amzn-Trace-Id: Root=1-xxxxxxxxx-xxxxxxxxxxxxxxxxxxxxxxxx
Connection: keep-alive

{}
```

## See Also
<a name="API_DisassociateAccessPolicy_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/eks-2017-11-01/DisassociateAccessPolicy) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/eks-2017-11-01/DisassociateAccessPolicy) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/eks-2017-11-01/DisassociateAccessPolicy) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/eks-2017-11-01/DisassociateAccessPolicy) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/eks-2017-11-01/DisassociateAccessPolicy) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/eks-2017-11-01/DisassociateAccessPolicy) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/eks-2017-11-01/DisassociateAccessPolicy) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/eks-2017-11-01/DisassociateAccessPolicy) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/eks-2017-11-01/DisassociateAccessPolicy) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/eks-2017-11-01/DisassociateAccessPolicy) 