---
id: "@specs/aws/eks/docs/API_CreateAccessEntry"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS CreateAccessEntry"
status: active
depends_on:
  - "@specs/aws/eks/meta"
---

# CreateAccessEntry

> **source:** AWS Documentation
> **spec:id:** @specs/aws/eks/docs/API_CreateAccessEntry
> **target_lang:** meta — documentation tier. ALL sections preserved.



# CreateAccessEntry
<a name="API_CreateAccessEntry"></a>

Creates an access entry.

An access entry allows an IAM principal to access your cluster. Access entries can replace the need to maintain entries in the `aws-auth` `ConfigMap` for authentication. You have the following options for authorizing an IAM principal to access Kubernetes objects on your cluster: Kubernetes role-based access control (RBAC), Amazon EKS, or both. Kubernetes RBAC authorization requires you to create and manage Kubernetes `Role`, `ClusterRole`, `RoleBinding`, and `ClusterRoleBinding` objects, in addition to managing access entries. If you use Amazon EKS authorization exclusively, you don't need to create and manage Kubernetes `Role`, `ClusterRole`, `RoleBinding`, and `ClusterRoleBinding` objects.

For more information about access entries, see [Access entries](https://docs.aws.amazon.com/eks/latest/userguide/access-entries.html) in the *Amazon EKS User Guide*.

## Request Syntax
<a name="API_CreateAccessEntry_RequestSyntax"></a>

```
POST /clusters/{{name}}/access-entries HTTP/1.1
Content-type: application/json

{
   "clientRequestToken": "{{string}}",
   "kubernetesGroups": [ "{{string}}" ],
   "principalArn": "{{string}}",
   "tags": { 
      "{{string}}" : "{{string}}" 
   },
   "type": "{{string}}",
   "username": "{{string}}"
}
```

## URI Request Parameters
<a name="API_CreateAccessEntry_RequestParameters"></a>

The request uses the following URI parameters.

 ** [name](#API_CreateAccessEntry_RequestSyntax) **   <a name="AmazonEKS-CreateAccessEntry-request-uri-clusterName"></a>
The name of your cluster.  
Required: Yes

## Request Body
<a name="API_CreateAccessEntry_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [clientRequestToken](#API_CreateAccessEntry_RequestSyntax) **   <a name="AmazonEKS-CreateAccessEntry-request-clientRequestToken"></a>
A unique, case-sensitive identifier that you provide to ensure the idempotency of the request.  
Type: String  
Required: No

 ** [kubernetesGroups](#API_CreateAccessEntry_RequestSyntax) **   <a name="AmazonEKS-CreateAccessEntry-request-kubernetesGroups"></a>
The value for `name` that you've specified for `kind: Group` as a `subject` in a Kubernetes `RoleBinding` or `ClusterRoleBinding` object. Amazon EKS doesn't confirm that the value for `name` exists in any bindings on your cluster. You can specify one or more names.  
Kubernetes authorizes the `principalArn` of the access entry to access any cluster objects that you've specified in a Kubernetes `Role` or `ClusterRole` object that is also specified in a binding's `roleRef`. For more information about creating Kubernetes `RoleBinding`, `ClusterRoleBinding`, `Role`, or `ClusterRole` objects, see [Using RBAC Authorization in the Kubernetes documentation](https://kubernetes.io/docs/reference/access-authn-authz/rbac/).  
If you want Amazon EKS to authorize the `principalArn` (instead of, or in addition to Kubernetes authorizing the `principalArn`), you can associate one or more access policies to the access entry using `AssociateAccessPolicy`. If you associate any access policies, the `principalARN` has all permissions assigned in the associated access policies and all permissions in any Kubernetes `Role` or `ClusterRole` objects that the group names are bound to.  
Type: Array of strings  
Required: No

 ** [principalArn](#API_CreateAccessEntry_RequestSyntax) **   <a name="AmazonEKS-CreateAccessEntry-request-principalArn"></a>
The ARN of the IAM principal for the `AccessEntry`. You can specify one ARN for each access entry. You can't specify the same ARN in more than one access entry. This value can't be changed after access entry creation.  
The valid principals differ depending on the type of the access entry in the `type` field. For `STANDARD` access entries, you can use every IAM principal type. For nodes (`EC2` (for EKS Auto Mode), `EC2_LINUX`, `EC2_WINDOWS`, `FARGATE_LINUX`, and `HYBRID_LINUX`), the only valid ARN is IAM roles. You can't use the STS session principal type with access entries because this is a temporary principal for each session and not a permanent identity that can be assigned permissions.  
 [IAM best practices](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html#bp-users-federation-idp) recommend using IAM roles with temporary credentials, rather than IAM users with long-term credentials.   
Type: String  
Required: Yes

 ** [tags](#API_CreateAccessEntry_RequestSyntax) **   <a name="AmazonEKS-CreateAccessEntry-request-tags"></a>
Metadata that assists with categorization and organization. Each tag consists of a key and an optional value. You define both. Tags don't propagate to any other cluster or AWS resources.  
Type: String to string map  
Map Entries: Maximum number of 50 items.  
Key Length Constraints: Minimum length of 1. Maximum length of 128.  
Value Length Constraints: Maximum length of 256.  
Required: No

 ** [type](#API_CreateAccessEntry_RequestSyntax) **   <a name="AmazonEKS-CreateAccessEntry-request-type"></a>
The type of the new access entry. Valid values are `STANDARD`, `FARGATE_LINUX`, `EC2_LINUX`, `EC2_WINDOWS`, `EC2` (for EKS Auto Mode), `HYBRID_LINUX`, and `HYPERPOD_LINUX`.   
If the `principalArn` is for an IAM role that's used for self-managed Amazon EC2 nodes, specify `EC2_LINUX` or `EC2_WINDOWS`. Amazon EKS grants the necessary permissions to the node for you. If the `principalArn` is for any other purpose, specify `STANDARD`. If you don't specify a value, Amazon EKS sets the value to `STANDARD`. If you have the access mode of the cluster set to `API_AND_CONFIG_MAP`, it's unnecessary to create access entries for IAM roles used with Fargate profiles or managed Amazon EC2 nodes, because Amazon EKS creates entries in the `aws-auth` `ConfigMap` for the roles. You can't change this value once you've created the access entry.  
If you set the value to `EC2_LINUX` or `EC2_WINDOWS`, you can't specify values for `kubernetesGroups`, or associate an `AccessPolicy` to the access entry.  
Type: String  
Required: No

 ** [username](#API_CreateAccessEntry_RequestSyntax) **   <a name="AmazonEKS-CreateAccessEntry-request-username"></a>
The username to authenticate to Kubernetes with. We recommend not specifying a username and letting Amazon EKS specify it for you. For more information about the value Amazon EKS specifies for you, or constraints before specifying your own username, see [Creating access entries](https://docs.aws.amazon.com/eks/latest/userguide/access-entries.html#creating-access-entries) in the *Amazon EKS User Guide*.  
Type: String  
Required: No

## Response Syntax
<a name="API_CreateAccessEntry_ResponseSyntax"></a>

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
<a name="API_CreateAccessEntry_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [accessEntry](#API_CreateAccessEntry_ResponseSyntax) **   <a name="AmazonEKS-CreateAccessEntry-response-accessEntry"></a>
An access entry allows an IAM principal (user or role) to access your cluster. Access entries can replace the need to maintain the `aws-auth` `ConfigMap` for authentication. For more information about access entries, see [Access entries](https://docs.aws.amazon.com/eks/latest/userguide/access-entries.html) in the *Amazon EKS User Guide*.  
Type: [AccessEntry](API_AccessEntry.md) object

## Errors
<a name="API_CreateAccessEntry_Errors"></a>

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
<a name="API_CreateAccessEntry_Examples"></a>

In the following example or examples, the Authorization header contents (`AUTHPARAMS`) must be replaced with an AWS Signature Version 4 signature. For more information about creating these signatures, see [Signature Version 4 Signing Process](https://docs.aws.amazon.com/general/latest/gr/signature-version-4.html) in the *Amazon EKS General Reference*.

You need to learn how to sign HTTP requests only if you intend to manually create them. When you use the [AWS Command Line Interface (AWS CLI)](http://aws.amazon.com/cli/) or one of the [AWS SDKs](http://aws.amazon.com/tools/) to make requests to AWS, these tools automatically sign the requests for you with the access key that you specify when you configure the tools. When you use these tools, you don't need to learn how to sign requests yourself.

### Example
<a name="API_CreateAccessEntry_Example_1"></a>

The following example creates an access entry for an IAM role with the name `my-role`. Since a `type` isn't specified, it's created as type `Standard`. Since a `username` isn't specified, Amazon EKS sets the value for `username`.

#### Sample Request
<a name="API_CreateAccessEntry_Example_1_Request"></a>

```
POST /clusters/my-cluster/access-entries HTTP/1.1
Host: eks.us-west-2.amazonaws.com
Accept-Encoding: identity
User-Agent: aws-cli/2.9.0 Python/3.9.11 Windows/10 exe/AMD64 prompt/off command/eks.create-access-entry
X-Amz-Date: 20230530T193227Z
Authorization: AUTHPARAMS
Content-Length: 120

{
	"principalArn": "arn:aws:iam::012345678910:role/my-role",
	"clientRequestToken": "5a8578bd-b6c1-4624-9e65-d0b70f857835"
}
```

#### Sample Response
<a name="API_CreateAccessEntry_Example_1_Response"></a>

```
HTTP/1.1 200 OK
Date: Tue, 30 May 2023 19:32:43 GMT
Content-Type: application/json
Content-Length: 485
x-amzn-RequestId: xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxx
Access-Control-Allow-Origin: *
Access-Control-Allow-Headers: *,Authorization,Date,X-Amz-Date,X-Amz-Security-Token,X-Amz-Target,content-type,x-amz-content-sha256,x-amz-user-agent,x-amzn-platform-id,x-amzn-trace-id
x-amz-apigw-id: FwFUDEhlPHcF4WQ=
Access-Control-Allow-Methods: GET,HEAD,PUT,POST,DELETE,OPTIONS
Access-Control-Expose-Headers: x-amzn-errortype,x-amzn-errormessage,x-amzn-trace-id,x-amzn-requestid,x-amz-apigw-id,date
X-Amzn-Trace-Id: Root=1-xxxxxxxxx-xxxxxxxxxxxxxxxxxxxxxxxx
Connection: keep-alive

{
	"accessEntry": {
		"clusterName": "my-cluster",
		"principalArn": "arn:aws:iam::012345678910:role/my-role",
		"kubernetesGroups": [],
		"accessEntryArn": "arn:aws:eks:us-west-2:012345678910:accessEntry/my-cluster/role/012345678910/my-role/xxx11111-xx1x-xx9115-1x11-xxx111x111x1",
		"createdAt": 1.685475163532E9,
		"modifiedAt": 1.685475163532E9,
		"tags": {},
		"username": "arn:aws:sts::012345678910:assumed-role/my-role/{{SessionName}}",
		"type": "STANDARD"
	}
}
```

## See Also
<a name="API_CreateAccessEntry_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/eks-2017-11-01/CreateAccessEntry) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/eks-2017-11-01/CreateAccessEntry) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/eks-2017-11-01/CreateAccessEntry) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/eks-2017-11-01/CreateAccessEntry) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/eks-2017-11-01/CreateAccessEntry) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/eks-2017-11-01/CreateAccessEntry) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/eks-2017-11-01/CreateAccessEntry) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/eks-2017-11-01/CreateAccessEntry) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/eks-2017-11-01/CreateAccessEntry) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/eks-2017-11-01/CreateAccessEntry) 