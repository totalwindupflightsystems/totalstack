---
id: "@specs/aws/eks/docs/API_UpdateClusterVersion"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS UpdateClusterVersion"
status: active
depends_on:
  - "@specs/aws/eks/meta"
---

# UpdateClusterVersion

> **source:** AWS Documentation
> **spec:id:** @specs/aws/eks/docs/API_UpdateClusterVersion
> **target_lang:** meta — documentation tier. ALL sections preserved.



# UpdateClusterVersion
<a name="API_UpdateClusterVersion"></a>

Updates an Amazon EKS cluster to the specified Kubernetes version. Your cluster continues to function during the update. The response output includes an update ID that you can use to track the status of your cluster update with the [https://docs.aws.amazon.com/eks/latest/APIReference/API_DescribeUpdate.html](https://docs.aws.amazon.com/eks/latest/APIReference/API_DescribeUpdate.html) API operation.

Cluster updates are asynchronous, and they should finish within a few minutes. During an update, the cluster status moves to `UPDATING` (this status transition is eventually consistent). When the update is complete (either `Failed` or `Successful`), the cluster status moves to `Active`.

If your cluster has managed node groups attached to it, all of your node groups' Kubernetes versions must match the cluster's Kubernetes version in order to update the cluster to a new Kubernetes version.

## Request Syntax
<a name="API_UpdateClusterVersion_RequestSyntax"></a>

```
POST /clusters/{{name}}/updates HTTP/1.1
Content-type: application/json

{
   "clientRequestToken": "{{string}}",
   "force": {{boolean}},
   "version": "{{string}}"
}
```

## URI Request Parameters
<a name="API_UpdateClusterVersion_RequestParameters"></a>

The request uses the following URI parameters.

 ** [name](#API_UpdateClusterVersion_RequestSyntax) **   <a name="AmazonEKS-UpdateClusterVersion-request-uri-name"></a>
The name of the Amazon EKS cluster to update.  
Required: Yes

## Request Body
<a name="API_UpdateClusterVersion_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [clientRequestToken](#API_UpdateClusterVersion_RequestSyntax) **   <a name="AmazonEKS-UpdateClusterVersion-request-clientRequestToken"></a>
A unique, case-sensitive identifier that you provide to ensure the idempotency of the request.  
Type: String  
Required: No

 ** [force](#API_UpdateClusterVersion_RequestSyntax) **   <a name="AmazonEKS-UpdateClusterVersion-request-force"></a>
Set this value to `true` to override upgrade-blocking readiness checks when updating a cluster.  
Type: Boolean  
Required: No

 ** [version](#API_UpdateClusterVersion_RequestSyntax) **   <a name="AmazonEKS-UpdateClusterVersion-request-version"></a>
The desired Kubernetes version following a successful update.  
Type: String  
Required: Yes

## Response Syntax
<a name="API_UpdateClusterVersion_ResponseSyntax"></a>

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
<a name="API_UpdateClusterVersion_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [update](#API_UpdateClusterVersion_ResponseSyntax) **   <a name="AmazonEKS-UpdateClusterVersion-response-update"></a>
The full description of the specified update  
Type: [Update](API_Update.md) object

## Errors
<a name="API_UpdateClusterVersion_Errors"></a>

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

 ** InvalidStateException **   
Amazon EKS detected upgrade readiness issues. Call the [https://docs.aws.amazon.com/eks/latest/APIReference/API_ListInsights.html](https://docs.aws.amazon.com/eks/latest/APIReference/API_ListInsights.html) API to view detected upgrade blocking issues. Pass the [https://docs.aws.amazon.com/eks/latest/APIReference/API_UpdateClusterVersion.html#API_UpdateClusterVersion_RequestBody](https://docs.aws.amazon.com/eks/latest/APIReference/API_UpdateClusterVersion.html#API_UpdateClusterVersion_RequestBody) flag when updating to override upgrade readiness errors.    
 ** clusterName **   
The Amazon EKS cluster associated with the exception.
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

 ** ThrottlingException **   
The request or operation couldn't be performed because a service is throttling requests.    
 ** clusterName **   
The Amazon EKS cluster associated with the exception.
HTTP Status Code: 429

## Examples
<a name="API_UpdateClusterVersion_Examples"></a>

In the following example or examples, the Authorization header contents (`AUTHPARAMS`) must be replaced with an AWS Signature Version 4 signature. For more information about creating these signatures, see [Signature Version 4 Signing Process](https://docs.aws.amazon.com/general/latest/gr/signature-version-4.html) in the *Amazon EKS General Reference*.

You need to learn how to sign HTTP requests only if you intend to manually create them. When you use the [AWS Command Line Interface (AWS CLI)](http://aws.amazon.com/cli/) or one of the [AWS SDKs](http://aws.amazon.com/tools/) to make requests to AWS, these tools automatically sign the requests for you with the access key that you specify when you configure the tools. When you use these tools, you don't need to learn how to sign requests yourself.

### Example
<a name="API_UpdateClusterVersion_Example_1"></a>

The following example updates the `devel` cluster to Kubernetes version 1.11.

#### Sample Request
<a name="API_UpdateClusterVersion_Example_1_Request"></a>

```
POST /clusters/devel/updates HTTP/1.1
Host: eks.us-west-2.amazonaws.com
Accept-Encoding: identity
User-Agent: aws-cli/1.16.56 Python/3.7.0 Darwin/17.7.0 botocore/1.12.46
X-Amz-Date: 20181129T172834Z
Authorization: AUTHPARAMS

{
  "version": "1.11",
  "clientRequestToken": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx"
}
```

#### Sample Response
<a name="API_UpdateClusterVersion_Example_1_Response"></a>

```
HTTP/1.1 200 OK
Date: Thu, 29 Nov 2018 17:28:35 GMT
Content-Type: application/json
Content-Length: 228
x-amzn-RequestId: xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxx
x-amz-apigw-id: RIo2bEs8vHcFXoA=
X-Amzn-Trace-Id: Root=1-xxxxxxxxx-xxxxxxxxxxxxxxxxxxxxxxxx
Connection: keep-alive

{
	"update": {
		"errors": [],
		"params": [{
			"value": "1.11",
			"type": "Version"
		}, {
			"value": "eks.1",
			"type": "PlatformVersion"
		}],
		"status": "InProgress",
		"id": "9f771284-9e30-4886-b5b1-3789b6bea4dc",
		"createdAt": 1543512515.848,
		"type": "VersionUpdate"
	}
}
```

## See Also
<a name="API_UpdateClusterVersion_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/eks-2017-11-01/UpdateClusterVersion) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/eks-2017-11-01/UpdateClusterVersion) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/eks-2017-11-01/UpdateClusterVersion) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/eks-2017-11-01/UpdateClusterVersion) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/eks-2017-11-01/UpdateClusterVersion) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/eks-2017-11-01/UpdateClusterVersion) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/eks-2017-11-01/UpdateClusterVersion) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/eks-2017-11-01/UpdateClusterVersion) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/eks-2017-11-01/UpdateClusterVersion) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/eks-2017-11-01/UpdateClusterVersion) 