---
id: "@specs/aws/eks/docs/API_UpdateNodegroupVersion"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS UpdateNodegroupVersion"
status: active
depends_on:
  - "@specs/aws/eks/meta"
---

# UpdateNodegroupVersion

> **source:** AWS Documentation
> **spec:id:** @specs/aws/eks/docs/API_UpdateNodegroupVersion
> **target_lang:** meta — documentation tier. ALL sections preserved.



# UpdateNodegroupVersion
<a name="API_UpdateNodegroupVersion"></a>

Updates the Kubernetes version or AMI version of an Amazon EKS managed node group.

You can update a node group using a launch template only if the node group was originally deployed with a launch template. Additionally, the launch template ID or name must match what was used when the node group was created. You can update the launch template version with necessary changes.

If you need to update a custom AMI in a node group that was deployed with a launch template, then update your custom AMI, specify the new ID in a new version of the launch template, and then update the node group to the new version of the launch template.

If you update without a launch template, then you can update to the latest available AMI version of a node group's current Kubernetes version by not specifying a Kubernetes version in the request. You can update to the latest AMI version of your cluster's current Kubernetes version by specifying your cluster's Kubernetes version in the request. For information about Linux versions, see [Amazon EKS optimized Amazon Linux AMI versions](https://docs.aws.amazon.com/eks/latest/userguide/eks-linux-ami-versions.html) in the *Amazon EKS User Guide*. For information about Windows versions, see [Amazon EKS optimized Windows AMI versions](https://docs.aws.amazon.com/eks/latest/userguide/eks-ami-versions-windows.html) in the *Amazon EKS User Guide*. 

You cannot roll back a node group to an earlier Kubernetes version or AMI version.

When a node in a managed node group is terminated due to a scaling action or update, every `Pod` on that node is drained first. Amazon EKS attempts to drain the nodes gracefully and will fail if it is unable to do so. You can `force` the update if Amazon EKS is unable to drain the nodes as a result of a `Pod` disruption budget issue.

## Request Syntax
<a name="API_UpdateNodegroupVersion_RequestSyntax"></a>

```
POST /clusters/{{name}}/node-groups/{{nodegroupName}}/update-version HTTP/1.1
Content-type: application/json

{
   "clientRequestToken": "{{string}}",
   "force": {{boolean}},
   "launchTemplate": { 
      "id": "{{string}}",
      "name": "{{string}}",
      "version": "{{string}}"
   },
   "releaseVersion": "{{string}}",
   "version": "{{string}}"
}
```

## URI Request Parameters
<a name="API_UpdateNodegroupVersion_RequestParameters"></a>

The request uses the following URI parameters.

 ** [name](#API_UpdateNodegroupVersion_RequestSyntax) **   <a name="AmazonEKS-UpdateNodegroupVersion-request-uri-clusterName"></a>
The name of your cluster.  
Required: Yes

 ** [nodegroupName](#API_UpdateNodegroupVersion_RequestSyntax) **   <a name="AmazonEKS-UpdateNodegroupVersion-request-uri-nodegroupName"></a>
The name of the managed node group to update.  
Required: Yes

## Request Body
<a name="API_UpdateNodegroupVersion_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [clientRequestToken](#API_UpdateNodegroupVersion_RequestSyntax) **   <a name="AmazonEKS-UpdateNodegroupVersion-request-clientRequestToken"></a>
A unique, case-sensitive identifier that you provide to ensure the idempotency of the request.  
Type: String  
Required: No

 ** [force](#API_UpdateNodegroupVersion_RequestSyntax) **   <a name="AmazonEKS-UpdateNodegroupVersion-request-force"></a>
Force the update if any `Pod` on the existing node group can't be drained due to a `Pod` disruption budget issue. If an update fails because all Pods can't be drained, you can force the update after it fails to terminate the old node whether or not any `Pod` is running on the node.  
Type: Boolean  
Required: No

 ** [launchTemplate](#API_UpdateNodegroupVersion_RequestSyntax) **   <a name="AmazonEKS-UpdateNodegroupVersion-request-launchTemplate"></a>
An object representing a node group's launch template specification. You can only update a node group using a launch template if the node group was originally deployed with a launch template. When updating, you must specify the same launch template ID or name that was used to create the node group.  
Type: [LaunchTemplateSpecification](API_LaunchTemplateSpecification.md) object  
Required: No

 ** [releaseVersion](#API_UpdateNodegroupVersion_RequestSyntax) **   <a name="AmazonEKS-UpdateNodegroupVersion-request-releaseVersion"></a>
The AMI version of the Amazon EKS optimized AMI to use for the update. By default, the latest available AMI version for the node group's Kubernetes version is used. For information about Linux versions, see [Amazon EKS optimized Amazon Linux AMI versions](https://docs.aws.amazon.com/eks/latest/userguide/eks-linux-ami-versions.html) in the *Amazon EKS User Guide*. Amazon EKS managed node groups support the November 2022 and later releases of the Windows AMIs. For information about Windows versions, see [Amazon EKS optimized Windows AMI versions](https://docs.aws.amazon.com/eks/latest/userguide/eks-ami-versions-windows.html) in the *Amazon EKS User Guide*.  
If you specify `launchTemplate`, and your launch template uses a custom AMI, then don't specify `releaseVersion`, or the node group update will fail. For more information about using launch templates with Amazon EKS, see [Customizing managed nodes with launch templates](https://docs.aws.amazon.com/eks/latest/userguide/launch-templates.html) in the *Amazon EKS User Guide*.  
Type: String  
Required: No

 ** [version](#API_UpdateNodegroupVersion_RequestSyntax) **   <a name="AmazonEKS-UpdateNodegroupVersion-request-version"></a>
The Kubernetes version to update to. If no version is specified, then the node group will be updated to match the cluster's current Kubernetes version, and the latest available AMI for that version will be used. You can also specify the Kubernetes version of the cluster to update the node group to the latest AMI version of the cluster's Kubernetes version. If you specify `launchTemplate`, and your launch template uses a custom AMI, then don't specify `version`, or the node group update will fail. For more information about using launch templates with Amazon EKS, see [Customizing managed nodes with launch templates](https://docs.aws.amazon.com/eks/latest/userguide/launch-templates.html) in the *Amazon EKS User Guide*.  
Type: String  
Required: No

## Response Syntax
<a name="API_UpdateNodegroupVersion_ResponseSyntax"></a>

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
<a name="API_UpdateNodegroupVersion_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [update](#API_UpdateNodegroupVersion_ResponseSyntax) **   <a name="AmazonEKS-UpdateNodegroupVersion-response-update"></a>
An object representing an asynchronous update.  
Type: [Update](API_Update.md) object

## Errors
<a name="API_UpdateNodegroupVersion_Errors"></a>

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

## Examples
<a name="API_UpdateNodegroupVersion_Examples"></a>

In the following example or examples, the Authorization header contents (`AUTHPARAMS`) must be replaced with an AWS Signature Version 4 signature. For more information about creating these signatures, see [Signature Version 4 Signing Process](https://docs.aws.amazon.com/general/latest/gr/signature-version-4.html) in the *Amazon EKS General Reference*.

You need to learn how to sign HTTP requests only if you intend to manually create them. When you use the [AWS Command Line Interface (AWS CLI)](http://aws.amazon.com/cli/) or one of the [AWS SDKs](http://aws.amazon.com/tools/) to make requests to AWS, these tools automatically sign the requests for you with the access key that you specify when you configure the tools. When you use these tools, you don't need to learn how to sign requests yourself.

### Example 1
<a name="API_UpdateNodegroupVersion_Example_1"></a>

This example updates a node group that was deployed without a launch template to the latest available node group AMI version for the node group's current Kubernetes version. The example node group is named `standard` and is in the `prod` cluster.

#### Sample Request
<a name="API_UpdateNodegroupVersion_Example_1_Request"></a>

```
POST /clusters/prod/node-groups/standard/update-version HTTP/1.1
Host: eks.us-west-2.amazonaws.com
Accept-Encoding: identity
User-Agent: aws-cli/1.16.275 Python/3.7.4 Darwin/18.7.0 botocore/1.13.11
X-Amz-Date: 20191111T184043Z
Authorization: AUTHPARAMS
Content-Length: 62

{
  "clientRequestToken": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx"
}
```

#### Sample Response
<a name="API_UpdateNodegroupVersion_Example_1_Response"></a>

```
HTTP/1.1 200 OK
Date: Mon, 11 Nov 2019 18:40:43 GMT
Content-Type: application/json
Content-Length: 237
x-amzn-RequestId: xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxx
x-amz-apigw-id: DAeuxEBkvHcF1sg=
X-Amzn-Trace-Id: Root=1-xxxxxxxxx-xxxxxxxxxxxxxxxxxxxxxxxx
Connection: keep-alive

{
  "update": {
    "id": "079be772-956e-37c4-a966-960c1a6755a5",
    "status": "InProgress",
    "type": "VersionUpdate",
    "params": [
      {
        "type": "Version",
        "value": "1.14"
      },
      {
        "type": "ReleaseVersion",
        "value": "1.14.7-20190927"
      }
    ],
    "createdAt": 1573497643.374,
    "errors": []
  }
}
```

### Example 2
<a name="API_UpdateNodegroupVersion_Example_2"></a>

This example updates a node group that was deployed with a launch template to version `3` of a launch template named `my-launch-template`.

#### Sample Request
<a name="API_UpdateNodegroupVersion_Example_2_Request"></a>

```
POST /clusters/my-cluster/node-groups/my-nodegroup/update-version HTTP/1.1
Host: eks.us-west-2.amazonaws.com
Accept-Encoding: identity
User-Agent: aws-cli/1.16.298 Python/3.6.0 Windows/10 botocore/1.13.34
X-Amz-Date: 20200812T144111Z
Authorization: AUTHPARAMS
Content-Length: 121

{
	"launchTemplate": {
		"name": "my-template",
		"version": "3"
	},
	"clientRequestToken": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx"
}
```

#### Sample Response
<a name="API_UpdateNodegroupVersion_Example_2_Response"></a>

```
HTTP/1.1 200 OK
Date: Wed, 12 Aug 2020 14:41:12 GMT
Content-Type: application/json
Content-Length: 248
x-amzn-RequestId: xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxx
x-amz-apigw-id: DAeuxEBkvHcF1sg=
X-Amzn-Trace-Id: Root=1-xxxxxxxxx-xxxxxxxxxxxxxxxxxxxxxxxx
Connection: keep-alive

{
	"update": {
		"id": "8f63ed58-f571-3bf9-87bc-a35f5e3d7687",
		"status": "InProgress",
		"type": "VersionUpdate",
		"params": [{
			"type": "LaunchTemplateName",
			"value": "my-launch-template"
		}, {
			"type": "LaunchTemplateVersion",
			"value": "3"
		}],
		"createdAt": 1597243272.809,
		"errors": []
	}
}
```

## See Also
<a name="API_UpdateNodegroupVersion_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/eks-2017-11-01/UpdateNodegroupVersion) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/eks-2017-11-01/UpdateNodegroupVersion) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/eks-2017-11-01/UpdateNodegroupVersion) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/eks-2017-11-01/UpdateNodegroupVersion) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/eks-2017-11-01/UpdateNodegroupVersion) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/eks-2017-11-01/UpdateNodegroupVersion) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/eks-2017-11-01/UpdateNodegroupVersion) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/eks-2017-11-01/UpdateNodegroupVersion) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/eks-2017-11-01/UpdateNodegroupVersion) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/eks-2017-11-01/UpdateNodegroupVersion) 