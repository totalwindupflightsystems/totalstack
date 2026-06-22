---
id: "@specs/aws/eks/docs/API_UpdateAccessEntry"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS UpdateAccessEntry"
status: active
depends_on:
  - "@specs/aws/eks/meta"
---

# UpdateAccessEntry

> **source:** AWS Documentation
> **spec:id:** @specs/aws/eks/docs/API_UpdateAccessEntry
> **target_lang:** meta — documentation tier. ALL sections preserved.



# UpdateAccessEntry
<a name="API_UpdateAccessEntry"></a>

Updates an access entry.

## Request Syntax
<a name="API_UpdateAccessEntry_RequestSyntax"></a>

```
POST /clusters/{{name}}/access-entries/{{principalArn}} HTTP/1.1
Content-type: application/json

{
   "clientRequestToken": "{{string}}",
   "kubernetesGroups": [ "{{string}}" ],
   "username": "{{string}}"
}
```

## URI Request Parameters
<a name="API_UpdateAccessEntry_RequestParameters"></a>

The request uses the following URI parameters.

 ** [name](#API_UpdateAccessEntry_RequestSyntax) **   <a name="AmazonEKS-UpdateAccessEntry-request-uri-clusterName"></a>
The name of your cluster.  
Required: Yes

 ** [principalArn](#API_UpdateAccessEntry_RequestSyntax) **   <a name="AmazonEKS-UpdateAccessEntry-request-uri-principalArn"></a>
The ARN of the IAM principal for the `AccessEntry`.  
Required: Yes

## Request Body
<a name="API_UpdateAccessEntry_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [clientRequestToken](#API_UpdateAccessEntry_RequestSyntax) **   <a name="AmazonEKS-UpdateAccessEntry-request-clientRequestToken"></a>
A unique, case-sensitive identifier that you provide to ensure the idempotency of the request.  
Type: String  
Required: No

 ** [kubernetesGroups](#API_UpdateAccessEntry_RequestSyntax) **   <a name="AmazonEKS-UpdateAccessEntry-request-kubernetesGroups"></a>
The value for `name` that you've specified for `kind: Group` as a `subject` in a Kubernetes `RoleBinding` or `ClusterRoleBinding` object. Amazon EKS doesn't confirm that the value for `name` exists in any bindings on your cluster. You can specify one or more names.  
Kubernetes authorizes the `principalArn` of the access entry to access any cluster objects that you've specified in a Kubernetes `Role` or `ClusterRole` object that is also specified in a binding's `roleRef`. For more information about creating Kubernetes `RoleBinding`, `ClusterRoleBinding`, `Role`, or `ClusterRole` objects, see [Using RBAC Authorization in the Kubernetes documentation](https://kubernetes.io/docs/reference/access-authn-authz/rbac/).  
If you want Amazon EKS to authorize the `principalArn` (instead of, or in addition to Kubernetes authorizing the `principalArn`), you can associate one or more access policies to the access entry using `AssociateAccessPolicy`. If you associate any access policies, the `principalARN` has all permissions assigned in the associated access policies and all permissions in any Kubernetes `Role` or `ClusterRole` objects that the group names are bound to.  
Type: Array of strings  
Required: No

 ** [username](#API_UpdateAccessEntry_RequestSyntax) **   <a name="AmazonEKS-UpdateAccessEntry-request-username"></a>
The username to authenticate to Kubernetes with. We recommend not specifying a username and letting Amazon EKS specify it for you. For more information about the value Amazon EKS specifies for you, or constraints before specifying your own username, see [Creating access entries](https://docs.aws.amazon.com/eks/latest/userguide/access-entries.html#creating-access-entries) in the *Amazon EKS User Guide*.  
Type: String  
Required: No

## Response Syntax
<a name="API_UpdateAccessEntry_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "accessEntry": { 
      "accessEntryArn": "string",
      "clusterName": "string",
      "createdAt": number,
      "kubernetesGroups": [ "string" ],
      "modifiedAt": number,
      "principalArn": "string",
      "tags": { 
         "string" : "string" 
      },
      "type": "string",
      "username": "string"
   }
}
```

## Response Elements
<a name="API_UpdateAccessEntry_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [accessEntry](#API_UpdateAccessEntry_ResponseSyntax) **   <a name="AmazonEKS-UpdateAccessEntry-response-accessEntry"></a>
The ARN of the IAM principal for the `AccessEntry`.  
Type: [AccessEntry](API_AccessEntry.md) object

## Errors
<a name="API_UpdateAccessEntry_Errors"></a>

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
<a name="API_UpdateAccessEntry_Examples"></a>

In the following example or examples, the Authorization header contents (`AUTHPARAMS`) must be replaced with an AWS Signature Version 4 signature. For more information about creating these signatures, see [Signature Version 4 Signing Process](https://docs.aws.amazon.com/general/latest/gr/signature-version-4.html) in the *Amazon EKS General Reference*.

You need to learn how to sign HTTP requests only if you intend to manually create them. When you use the [AWS Command Line Interface (AWS CLI)](http://aws.amazon.com/cli/) or one of the [AWS SDKs](http://aws.amazon.com/tools/) to make requests to AWS, these tools automatically sign the requests for you with the access key that you specify when you configure the tools. When you use these tools, you don't need to learn how to sign requests yourself.

### Example
<a name="API_UpdateAccessEntry_Example_1"></a>

The following example updates an access entry by adding a value for `kubernetesGroups`.

#### Sample Request
<a name="API_UpdateAccessEntry_Example_1_Request"></a>

```
POST /clusters/my-cluster/access-entries/arn%3Aaws%3Aiam%3A%3A012345678910%3Arole%2Fmy-role HTTP/1.1
Host: eks.us-west-2.amazonaws.com
Accept-Encoding: identity
Content-Type: application/json
User-Agent: aws-cli/2.9.0 Python/3.9.11 Windows/10 exe/AMD64 prompt/off command/eks.update-access-entry
X-Amz-Date: 20230531T132743Z
Authorization: AUTHPARAMS
Content-Length: 107


{
	"kubernetesGroups": ["my-kubernetes-group"],
	"clientRequestToken": "x111xxx1-111x-11xx-xxx1-x11x1111xxx1"
}
```

#### Sample Response
<a name="API_UpdateAccessEntry_Example_1_Response"></a>

```
HTTP/1.1 200 OK
Date: Wed, 31 May 2023 13:27:45 GMT
Content-Type: application/json
Content-Length: 507
x-amzn-RequestId: xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxx
Access-Control-Allow-Origin: *
Access-Control-Allow-Headers: *,Authorization,Date,X-Amz-Date,X-Amz-Security-Token,X-Amz-Target,content-type,x-amz-content-sha256,x-amz-user-agent,x-amzn-platform-id,x-amzn-trace-id
x-amz-apigw-id: Fyi0rHRUPHcFyTA=
Access-Control-Allow-Methods: GET,HEAD,PUT,POST,DELETE,OPTIONS
Access-Control-Expose-Headers: x-amzn-errortype,x-amzn-errormessage,x-amzn-trace-id,x-amzn-requestid,x-amz-apigw-id,date
X-Amzn-Trace-Id: Root=1-xxxxxxxxx-xxxxxxxxxxxxxxxxxxxxxxxx
Connection: keep-alive

{
	"accessEntry": {
		"clusterName": "my-cluster",
		"principalArn": "arn:aws:iam::012345678910:role/my-role",
		"kubernetesGroups": ["my-kubernetes-group"],
		"accessEntryArn": "arn:aws:eks:us-west-2:012345678910:accessEntry/my-cluster/role/012345678910/my-role/fec43712-ee5b-dd95-5f88-edb855c578b2",
		"createdAt": 1.685475163532E9,
		"modifiedAt": 1.685539665508E9,
		"tags": {},
		"username": "arn:aws:sts::012345678910:assumed-role/my-role/{{SessionName}}",
		"type": "STANDARD"
	}
}
```

## See Also
<a name="API_UpdateAccessEntry_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/eks-2017-11-01/UpdateAccessEntry) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/eks-2017-11-01/UpdateAccessEntry) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/eks-2017-11-01/UpdateAccessEntry) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/eks-2017-11-01/UpdateAccessEntry) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/eks-2017-11-01/UpdateAccessEntry) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/eks-2017-11-01/UpdateAccessEntry) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/eks-2017-11-01/UpdateAccessEntry) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/eks-2017-11-01/UpdateAccessEntry) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/eks-2017-11-01/UpdateAccessEntry) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/eks-2017-11-01/UpdateAccessEntry) 