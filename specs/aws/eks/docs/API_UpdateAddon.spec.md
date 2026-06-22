---
id: "@specs/aws/eks/docs/API_UpdateAddon"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS UpdateAddon"
status: active
depends_on:
  - "@specs/aws/eks/meta"
---

# UpdateAddon

> **source:** AWS Documentation
> **spec:id:** @specs/aws/eks/docs/API_UpdateAddon
> **target_lang:** meta — documentation tier. ALL sections preserved.



# UpdateAddon
<a name="API_UpdateAddon"></a>

Updates an Amazon EKS add-on.

## Request Syntax
<a name="API_UpdateAddon_RequestSyntax"></a>

```
POST /clusters/{{name}}/addons/{{addonName}}/update HTTP/1.1
Content-type: application/json

{
   "addonVersion": "{{string}}",
   "clientRequestToken": "{{string}}",
   "configurationValues": "{{string}}",
   "podIdentityAssociations": [ 
      { 
         "roleArn": "{{string}}",
         "serviceAccount": "{{string}}"
      }
   ],
   "resolveConflicts": "{{string}}",
   "serviceAccountRoleArn": "{{string}}"
}
```

## URI Request Parameters
<a name="API_UpdateAddon_RequestParameters"></a>

The request uses the following URI parameters.

 ** [addonName](#API_UpdateAddon_RequestSyntax) **   <a name="AmazonEKS-UpdateAddon-request-uri-addonName"></a>
The name of the add-on. The name must match one of the names returned by [https://docs.aws.amazon.com/eks/latest/APIReference/API_ListAddons.html](https://docs.aws.amazon.com/eks/latest/APIReference/API_ListAddons.html).  
Required: Yes

 ** [name](#API_UpdateAddon_RequestSyntax) **   <a name="AmazonEKS-UpdateAddon-request-uri-clusterName"></a>
The name of your cluster.  
Length Constraints: Minimum length of 1. Maximum length of 100.  
Pattern: `^[0-9A-Za-z][A-Za-z0-9\-_]*`   
Required: Yes

## Request Body
<a name="API_UpdateAddon_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [addonVersion](#API_UpdateAddon_RequestSyntax) **   <a name="AmazonEKS-UpdateAddon-request-addonVersion"></a>
The version of the add-on. The version must match one of the versions returned by [https://docs.aws.amazon.com/eks/latest/APIReference/API_DescribeAddonVersions.html](https://docs.aws.amazon.com/eks/latest/APIReference/API_DescribeAddonVersions.html).  
Type: String  
Required: No

 ** [clientRequestToken](#API_UpdateAddon_RequestSyntax) **   <a name="AmazonEKS-UpdateAddon-request-clientRequestToken"></a>
A unique, case-sensitive identifier that you provide to ensure the idempotency of the request.  
Type: String  
Required: No

 ** [configurationValues](#API_UpdateAddon_RequestSyntax) **   <a name="AmazonEKS-UpdateAddon-request-configurationValues"></a>
The set of configuration values for the add-on that's created. The values that you provide are validated against the schema returned by `DescribeAddonConfiguration`.  
Type: String  
Required: No

 ** [podIdentityAssociations](#API_UpdateAddon_RequestSyntax) **   <a name="AmazonEKS-UpdateAddon-request-podIdentityAssociations"></a>
An array of EKS Pod Identity associations to be updated. Each association maps a Kubernetes service account to an IAM role. If this value is left blank, no change. If an empty array is provided, existing associations owned by the add-on are deleted.  
For more information, see [Attach an IAM Role to an Amazon EKS add-on using EKS Pod Identity](https://docs.aws.amazon.com/eks/latest/userguide/add-ons-iam.html) in the *Amazon EKS User Guide*.  
Type: Array of [AddonPodIdentityAssociations](API_AddonPodIdentityAssociations.md) objects  
Required: No

 ** [resolveConflicts](#API_UpdateAddon_RequestSyntax) **   <a name="AmazonEKS-UpdateAddon-request-resolveConflicts"></a>
How to resolve field value conflicts for an Amazon EKS add-on if you've changed a value from the Amazon EKS default value. Conflicts are handled based on the option you choose:  
+  **None** – Amazon EKS doesn't change the value. The update might fail.
+  **Overwrite** – Amazon EKS overwrites the changed value back to the Amazon EKS default value.
+  **Preserve** – Amazon EKS preserves the value. If you choose this option, we recommend that you test any field and value changes on a non-production cluster before updating the add-on on your production cluster.
Type: String  
Valid Values: `OVERWRITE | NONE | PRESERVE`   
Required: No

 ** [serviceAccountRoleArn](#API_UpdateAddon_RequestSyntax) **   <a name="AmazonEKS-UpdateAddon-request-serviceAccountRoleArn"></a>
The Amazon Resource Name (ARN) of an existing IAM role to bind to the add-on's service account. The role must be assigned the IAM permissions required by the add-on. If you don't specify an existing IAM role, then the add-on uses the permissions assigned to the node IAM role. For more information, see [Amazon EKS node IAM role](https://docs.aws.amazon.com/eks/latest/userguide/create-node-role.html) in the *Amazon EKS User Guide*.  
To specify an existing IAM role, you must have an IAM OpenID Connect (OIDC) provider created for your cluster. For more information, see [Enabling IAM roles for service accounts on your cluster](https://docs.aws.amazon.com/eks/latest/userguide/enable-iam-roles-for-service-accounts.html) in the *Amazon EKS User Guide*.
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 255.  
Required: No

## Response Syntax
<a name="API_UpdateAddon_ResponseSyntax"></a>

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
<a name="API_UpdateAddon_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [update](#API_UpdateAddon_ResponseSyntax) **   <a name="AmazonEKS-UpdateAddon-response-update"></a>
An object representing an asynchronous update.  
Type: [Update](API_Update.md) object

## Errors
<a name="API_UpdateAddon_Errors"></a>

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
<a name="API_UpdateAddon_Examples"></a>

In the following example or examples, the Authorization header contents (`AUTHPARAMS`) must be replaced with an AWS Signature Version 4 signature. For more information about creating these signatures, see [Signature Version 4 Signing Process](https://docs.aws.amazon.com/general/latest/gr/signature-version-4.html) in the *Amazon EKS General Reference*.

You need to learn how to sign HTTP requests only if you intend to manually create them. When you use the [AWS Command Line Interface (AWS CLI)](http://aws.amazon.com/cli/) or one of the [AWS SDKs](http://aws.amazon.com/tools/) to make requests to AWS, these tools automatically sign the requests for you with the access key that you specify when you configure the tools. When you use these tools, you don't need to learn how to sign requests yourself.

### Example
<a name="API_UpdateAddon_Example_1"></a>

The following example updates an add-on named `vpc-cni` to use an IAM role named `AmazonEKSCNIRole` and to overwrite the add-on's existing configuration with the Amazon EKS add-on's configuration.

#### Sample Request
<a name="API_UpdateAddon_Example_1_Request"></a>

```
POST /clusters/my-cluster/addons/vpc-cni/update HTTP/1.1
Host: eks.us-west-2.amazonaws.com
Accept-Encoding: identity
User-Agent: aws-cli/1.16.298 Python/3.6.0 Windows/10 botocore/1.13.34
X-Amz-Date: 20201125T145528Z
Authorization: AUTHPARAMS

{
	"serviceAccountRoleArn": "arn:aws:iam::012345678910:role/AmazonEKSCNIRole",
	"resolveConflicts": "overwrite",
	"clientRequestToken": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx"
}
```

#### Sample Response
<a name="API_UpdateAddon_Example_1_Response"></a>

```
HTTP/1.1 200 OK
Date: Wed, 25 Nov 2020 14:55:29 GMT
Content-Type: application/json
Content-Length: 288
x-amzn-RequestId: xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxx
x-amz-apigw-id: WkZ_KGiBvHcFhtw=
X-Amzn-Trace-Id: Root=1-xxxxxxxxx-xxxxxxxxxxxxxxxxxxxxxxxx
Connection: keep-alive

{
	"update": {
		"id": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
		"status": "InProgress",
		"type": "AddonUpdate",
		"params": [{
			"type": "ServiceAccountRoleArn",
			"value": "arn:aws:iam::012345678910:role/AmazonEKSCNIRole"
		}, {
			"type": "ResolveConflicts",
			"value": "overwrite"
		}],
		"createdAt": 1606316129.051,
		"errors": []
	}
}
```

## See Also
<a name="API_UpdateAddon_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/eks-2017-11-01/UpdateAddon) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/eks-2017-11-01/UpdateAddon) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/eks-2017-11-01/UpdateAddon) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/eks-2017-11-01/UpdateAddon) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/eks-2017-11-01/UpdateAddon) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/eks-2017-11-01/UpdateAddon) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/eks-2017-11-01/UpdateAddon) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/eks-2017-11-01/UpdateAddon) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/eks-2017-11-01/UpdateAddon) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/eks-2017-11-01/UpdateAddon) 