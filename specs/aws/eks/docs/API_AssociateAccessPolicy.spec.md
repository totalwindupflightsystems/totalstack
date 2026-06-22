---
id: "@specs/aws/eks/docs/API_AssociateAccessPolicy"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS AssociateAccessPolicy"
status: active
depends_on:
  - "@specs/aws/eks/meta"
---

# AssociateAccessPolicy

> **source:** AWS Documentation
> **spec:id:** @specs/aws/eks/docs/API_AssociateAccessPolicy
> **target_lang:** meta — documentation tier. ALL sections preserved.



# AssociateAccessPolicy
<a name="API_AssociateAccessPolicy"></a>

Associates an access policy and its scope to an access entry. For more information about associating access policies, see [Associating and disassociating access policies to and from access entries](https://docs.aws.amazon.com/eks/latest/userguide/access-policies.html) in the *Amazon EKS User Guide*.

## Request Syntax
<a name="API_AssociateAccessPolicy_RequestSyntax"></a>

```
POST /clusters/{{name}}/access-entries/{{principalArn}}/access-policies HTTP/1.1
Content-type: application/json

{
   "accessScope": { 
      "namespaces": [ "{{string}}" ],
      "type": "{{string}}"
   },
   "policyArn": "{{string}}"
}
```

## URI Request Parameters
<a name="API_AssociateAccessPolicy_RequestParameters"></a>

The request uses the following URI parameters.

 ** [name](#API_AssociateAccessPolicy_RequestSyntax) **   <a name="AmazonEKS-AssociateAccessPolicy-request-uri-clusterName"></a>
The name of your cluster.  
Required: Yes

 ** [principalArn](#API_AssociateAccessPolicy_RequestSyntax) **   <a name="AmazonEKS-AssociateAccessPolicy-request-uri-principalArn"></a>
The Amazon Resource Name (ARN) of the IAM user or role for the `AccessEntry` that you're associating the access policy to.   
Required: Yes

## Request Body
<a name="API_AssociateAccessPolicy_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [accessScope](#API_AssociateAccessPolicy_RequestSyntax) **   <a name="AmazonEKS-AssociateAccessPolicy-request-accessScope"></a>
The scope for the `AccessPolicy`. You can scope access policies to an entire cluster or to specific Kubernetes namespaces.  
Type: [AccessScope](API_AccessScope.md) object  
Required: Yes

 ** [policyArn](#API_AssociateAccessPolicy_RequestSyntax) **   <a name="AmazonEKS-AssociateAccessPolicy-request-policyArn"></a>
The ARN of the `AccessPolicy` that you're associating. For a list of ARNs, use `ListAccessPolicies`.  
Type: String  
Required: Yes

## Response Syntax
<a name="API_AssociateAccessPolicy_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "associatedAccessPolicy": { 
      "accessScope": { 
         "namespaces": [ "string" ],
         "type": "string"
      },
      "associatedAt": number,
      "modifiedAt": number,
      "policyArn": "string"
   },
   "clusterName": "string",
   "principalArn": "string"
}
```

## Response Elements
<a name="API_AssociateAccessPolicy_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [associatedAccessPolicy](#API_AssociateAccessPolicy_ResponseSyntax) **   <a name="AmazonEKS-AssociateAccessPolicy-response-associatedAccessPolicy"></a>
The `AccessPolicy` and scope associated to the `AccessEntry`.  
Type: [AssociatedAccessPolicy](API_AssociatedAccessPolicy.md) object

 ** [clusterName](#API_AssociateAccessPolicy_ResponseSyntax) **   <a name="AmazonEKS-AssociateAccessPolicy-response-clusterName"></a>
The name of your cluster.  
Type: String

 ** [principalArn](#API_AssociateAccessPolicy_ResponseSyntax) **   <a name="AmazonEKS-AssociateAccessPolicy-response-principalArn"></a>
The ARN of the IAM principal for the `AccessEntry`.  
Type: String

## Errors
<a name="API_AssociateAccessPolicy_Errors"></a>

For information about the errors that are common to all actions, see [Common Errors](CommonErrors.md).

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
<a name="API_AssociateAccessPolicy_Examples"></a>

In the following example or examples, the Authorization header contents (`AUTHPARAMS`) must be replaced with an AWS Signature Version 4 signature. For more information about creating these signatures, see [Signature Version 4 Signing Process](https://docs.aws.amazon.com/general/latest/gr/signature-version-4.html) in the *Amazon EKS General Reference*.

You need to learn how to sign HTTP requests only if you intend to manually create them. When you use the [AWS Command Line Interface (AWS CLI)](http://aws.amazon.com/cli/) or one of the [AWS SDKs](http://aws.amazon.com/tools/) to make requests to AWS, these tools automatically sign the requests for you with the access key that you specify when you configure the tools. When you use these tools, you don't need to learn how to sign requests yourself.

### Example
<a name="API_AssociateAccessPolicy_Example_1"></a>

The following example associates the `AmazonEKSAdminPolicy` access policy to an access entry with the IAM role named `my-role`. The IAM role has the permissions in this policy across all namespaces on the cluster.

#### Sample Request
<a name="API_AssociateAccessPolicy_Example_1_Request"></a>

```
POST /clusters/my-cluster/access-entries/arn%3Aaws%3Aiam%3A%3A012345678910%3Arole%2Fmy-role/access-policies HTTP/1.1
Host: eks.us-west-2.amazonaws.com
Accept-Encoding: identity
Content-Type: application/json
User-Agent: aws-cli/2.9.0 Python/3.9.11 Windows/10 exe/AMD64 prompt/off command/eks.associate-access-policy
X-Amz-Date: 20230531T134532Z
Authorization: AUTHPARAMS
Content-Length: 112

{
	"policyArn": "arn:aws:eks::aws:cluster-access-policy/AmazonEKSAdminPolicy",
	"accessScope": {
		"type": "cluster"
	}
}
```

#### Sample Response
<a name="API_AssociateAccessPolicy_Example_1_Response"></a>

```
HTTP/1.1 200 OK
Date: Wed, 31 May 2023 13:45:47 GMT
Content-Type: application/json
Content-Length: 285
x-amzn-RequestId: xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxx
Access-Control-Allow-Origin: *
Access-Control-Allow-Headers: *,Authorization,Date,X-Amz-Date,X-Amz-Security-Token,X-Amz-Target,content-type,x-amz-content-sha256,x-amz-user-agent,x-amzn-platform-id,x-amzn-trace-id
x-amz-apigw-id: FylbjHLcPHcFaiA=
Access-Control-Allow-Methods: GET,HEAD,PUT,POST,DELETE,OPTIONS
Access-Control-Expose-Headers: x-amzn-errortype,x-amzn-errormessage,x-amzn-trace-id,x-amzn-requestid,x-amz-apigw-id,date
X-Amzn-Trace-Id: Root=1-xxxxxxxxx-xxxxxxxxxxxxxxxxxxxxxxxx
Connection: keep-alive

{
	"clusterName": "my-cluster                                                                                                                                                                                                                                                                                                                                                  ",
	"principalArn": "arn:aws:iam::012345678910:role/my-role",
	"associatedAccessPolicy": {
		"policyArn": "arn:aws:eks::aws:cluster-access-policy/AmazonEKSAdminPolicy",
		"accessScope": {
			"type": "cluster",
			"namespaces": []
		},
		"associatedAt": 1685540747.281,
		"modifiedAt": 1685540747.281
	}
}
```

## See Also
<a name="API_AssociateAccessPolicy_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/eks-2017-11-01/AssociateAccessPolicy) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/eks-2017-11-01/AssociateAccessPolicy) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/eks-2017-11-01/AssociateAccessPolicy) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/eks-2017-11-01/AssociateAccessPolicy) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/eks-2017-11-01/AssociateAccessPolicy) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/eks-2017-11-01/AssociateAccessPolicy) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/eks-2017-11-01/AssociateAccessPolicy) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/eks-2017-11-01/AssociateAccessPolicy) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/eks-2017-11-01/AssociateAccessPolicy) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/eks-2017-11-01/AssociateAccessPolicy) 