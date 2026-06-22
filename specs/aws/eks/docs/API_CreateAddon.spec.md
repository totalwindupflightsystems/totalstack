---
id: "@specs/aws/eks/docs/API_CreateAddon"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS CreateAddon"
status: active
depends_on:
  - "@specs/aws/eks/meta"
---

# CreateAddon

> **source:** AWS Documentation
> **spec:id:** @specs/aws/eks/docs/API_CreateAddon
> **target_lang:** meta — documentation tier. ALL sections preserved.



# CreateAddon
<a name="API_CreateAddon"></a>

Creates an Amazon EKS add-on.

Amazon EKS add-ons help to automate the provisioning and lifecycle management of common operational software for Amazon EKS clusters. For more information, see [Amazon EKS add-ons](https://docs.aws.amazon.com/eks/latest/userguide/eks-add-ons.html) in the *Amazon EKS User Guide*.

## Request Syntax
<a name="API_CreateAddon_RequestSyntax"></a>

```
POST /clusters/{{name}}/addons HTTP/1.1
Content-type: application/json

{
   "addonName": "{{string}}",
   "addonVersion": "{{string}}",
   "clientRequestToken": "{{string}}",
   "configurationValues": "{{string}}",
   "namespaceConfig": { 
      "namespace": "{{string}}"
   },
   "podIdentityAssociations": [ 
      { 
         "roleArn": "{{string}}",
         "serviceAccount": "{{string}}"
      }
   ],
   "resolveConflicts": "{{string}}",
   "serviceAccountRoleArn": "{{string}}",
   "tags": { 
      "{{string}}" : "{{string}}" 
   }
}
```

## URI Request Parameters
<a name="API_CreateAddon_RequestParameters"></a>

The request uses the following URI parameters.

 ** [name](#API_CreateAddon_RequestSyntax) **   <a name="AmazonEKS-CreateAddon-request-uri-clusterName"></a>
The name of your cluster.  
Length Constraints: Minimum length of 1. Maximum length of 100.  
Pattern: `^[0-9A-Za-z][A-Za-z0-9\-_]*`   
Required: Yes

## Request Body
<a name="API_CreateAddon_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [addonName](#API_CreateAddon_RequestSyntax) **   <a name="AmazonEKS-CreateAddon-request-addonName"></a>
The name of the add-on. The name must match one of the names returned by `DescribeAddonVersions`.  
Type: String  
Required: Yes

 ** [addonVersion](#API_CreateAddon_RequestSyntax) **   <a name="AmazonEKS-CreateAddon-request-addonVersion"></a>
The version of the add-on. The version must match one of the versions returned by [https://docs.aws.amazon.com/eks/latest/APIReference/API_DescribeAddonVersions.html](https://docs.aws.amazon.com/eks/latest/APIReference/API_DescribeAddonVersions.html).  
Type: String  
Required: No

 ** [clientRequestToken](#API_CreateAddon_RequestSyntax) **   <a name="AmazonEKS-CreateAddon-request-clientRequestToken"></a>
A unique, case-sensitive identifier that you provide to ensure the idempotency of the request.  
Type: String  
Required: No

 ** [configurationValues](#API_CreateAddon_RequestSyntax) **   <a name="AmazonEKS-CreateAddon-request-configurationValues"></a>
The set of configuration values for the add-on that's created. The values that you provide are validated against the schema returned by `DescribeAddonConfiguration`.  
Type: String  
Required: No

 ** [namespaceConfig](#API_CreateAddon_RequestSyntax) **   <a name="AmazonEKS-CreateAddon-request-namespaceConfig"></a>
The namespace configuration for the addon. If specified, this will override the default namespace for the addon.  
Type: [AddonNamespaceConfigRequest](API_AddonNamespaceConfigRequest.md) object  
Required: No

 ** [podIdentityAssociations](#API_CreateAddon_RequestSyntax) **   <a name="AmazonEKS-CreateAddon-request-podIdentityAssociations"></a>
An array of EKS Pod Identity associations to be created. Each association maps a Kubernetes service account to an IAM role.  
For more information, see [Attach an IAM Role to an Amazon EKS add-on using EKS Pod Identity](https://docs.aws.amazon.com/eks/latest/userguide/add-ons-iam.html) in the *Amazon EKS User Guide*.  
Type: Array of [AddonPodIdentityAssociations](API_AddonPodIdentityAssociations.md) objects  
Required: No

 ** [resolveConflicts](#API_CreateAddon_RequestSyntax) **   <a name="AmazonEKS-CreateAddon-request-resolveConflicts"></a>
How to resolve field value conflicts for an Amazon EKS add-on. Conflicts are handled based on the value you choose:  
+  **None** – If the self-managed version of the add-on is installed on your cluster, Amazon EKS doesn't change the value. Creation of the add-on might fail.
+  **Overwrite** – If the self-managed version of the add-on is installed on your cluster and the Amazon EKS default value is different than the existing value, Amazon EKS changes the value to the Amazon EKS default value.
+  **Preserve** – This is similar to the NONE option. If the self-managed version of the add-on is installed on your cluster Amazon EKS doesn't change the add-on resource properties. Creation of the add-on might fail if conflicts are detected. This option works differently during the update operation. For more information, see [https://docs.aws.amazon.com/eks/latest/APIReference/API_UpdateAddon.html](https://docs.aws.amazon.com/eks/latest/APIReference/API_UpdateAddon.html).
If you don't currently have the self-managed version of the add-on installed on your cluster, the Amazon EKS add-on is installed. Amazon EKS sets all values to default values, regardless of the option that you specify.  
Type: String  
Valid Values: `OVERWRITE | NONE | PRESERVE`   
Required: No

 ** [serviceAccountRoleArn](#API_CreateAddon_RequestSyntax) **   <a name="AmazonEKS-CreateAddon-request-serviceAccountRoleArn"></a>
The Amazon Resource Name (ARN) of an existing IAM role to bind to the add-on's service account. The role must be assigned the IAM permissions required by the add-on. If you don't specify an existing IAM role, then the add-on uses the permissions assigned to the node IAM role. For more information, see [Amazon EKS node IAM role](https://docs.aws.amazon.com/eks/latest/userguide/create-node-role.html) in the *Amazon EKS User Guide*.  
To specify an existing IAM role, you must have an IAM OpenID Connect (OIDC) provider created for your cluster. For more information, see [Enabling IAM roles for service accounts on your cluster](https://docs.aws.amazon.com/eks/latest/userguide/enable-iam-roles-for-service-accounts.html) in the *Amazon EKS User Guide*.
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 255.  
Required: No

 ** [tags](#API_CreateAddon_RequestSyntax) **   <a name="AmazonEKS-CreateAddon-request-tags"></a>
Metadata that assists with categorization and organization. Each tag consists of a key and an optional value. You define both. Tags don't propagate to any other cluster or AWS resources.  
Type: String to string map  
Map Entries: Maximum number of 50 items.  
Key Length Constraints: Minimum length of 1. Maximum length of 128.  
Value Length Constraints: Maximum length of 256.  
Required: No

## Response Syntax
<a name="API_CreateAddon_ResponseSyntax"></a>

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
<a name="API_CreateAddon_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [addon](#API_CreateAddon_ResponseSyntax) **   <a name="AmazonEKS-CreateAddon-response-addon"></a>
An Amazon EKS add-on. For more information, see [Amazon EKS add-ons](https://docs.aws.amazon.com/eks/latest/userguide/eks-add-ons.html) in the *Amazon EKS User Guide*.  
Type: [Addon](API_Addon.md) object

## Errors
<a name="API_CreateAddon_Errors"></a>

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
<a name="API_CreateAddon_Examples"></a>

In the following example or examples, the Authorization header contents (`AUTHPARAMS`) must be replaced with an AWS Signature Version 4 signature. For more information about creating these signatures, see [Signature Version 4 Signing Process](https://docs.aws.amazon.com/general/latest/gr/signature-version-4.html) in the *Amazon EKS General Reference*.

You need to learn how to sign HTTP requests only if you intend to manually create them. When you use the [AWS Command Line Interface (AWS CLI)](http://aws.amazon.com/cli/) or one of the [AWS SDKs](http://aws.amazon.com/tools/) to make requests to AWS, these tools automatically sign the requests for you with the access key that you specify when you configure the tools. When you use these tools, you don't need to learn how to sign requests yourself.

### Example
<a name="API_CreateAddon_Example_1"></a>

The following example creates an add-on named `vpc-cni`. The add-on uses an existing IAM role named `AmazonEKSCNIRole`. If the add-on existed prior to creating the Amazon EKS add-on, its settings are overwritten with the Amazon EKS add-on's settings.

#### Sample Request
<a name="API_CreateAddon_Example_1_Request"></a>

```
POST /clusters/my-cluster/addons HTTP/1.1
Host: eks.us-west-2.amazonaws.com
Accept-Encoding: identity
User-Agent: aws-cli/1.16.298 Python/3.6.0 Windows/10 botocore/1.13.34
X-Amz-Date: 20201125T143943Z
Authorization: AUTHPARAMS
Content-Length: 195

{
	"addonName": "vpc-cni",
	"serviceAccountRoleArn": "arn:aws:iam::012345678910:role/AmazonEKSCNIRole",
	"resolveConflicts": "overwrite",
	"clientRequestToken": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx"
}
```

#### Sample Response
<a name="API_CreateAddon_Example_1_Response"></a>

```
HTTP/1.1 200 OK
Date: Wed, 25 Nov 2020 14:39:44 GMT
Content-Type: application/json
Content-Length: 474
x-amzn-RequestId: xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxx
x-amz-apigw-id: WkXriGcavHcFyqw=
X-Amzn-Trace-Id: Root=1-xxxxxxxxx-xxxxxxxxxxxxxxxxxxxxxxxx
Connection: keep-alive

{
  "addon" : {
    "addonName" : "vpc-cni",
    "clusterName" : "1-18",
    "status" : "CREATING",
    "addonVersion" : "v1.7.5-eksbuild.1",
    "health" : {
      "issues" : [ ]
    },
    "addonArn" : "arn:aws:eks:us-west-2:012345678910:addon/my-cluster/vpc-cni/xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
    "createdAt" : 1.606315184255E9,
    "modifiedAt" : 1.606315184274E9,
    "serviceAccountRoleArn" : "arn:aws:iam::012345678910:role/AmazonEKSCNIRole",
    "tags" : { }
  }
}
```

## See Also
<a name="API_CreateAddon_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/eks-2017-11-01/CreateAddon) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/eks-2017-11-01/CreateAddon) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/eks-2017-11-01/CreateAddon) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/eks-2017-11-01/CreateAddon) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/eks-2017-11-01/CreateAddon) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/eks-2017-11-01/CreateAddon) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/eks-2017-11-01/CreateAddon) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/eks-2017-11-01/CreateAddon) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/eks-2017-11-01/CreateAddon) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/eks-2017-11-01/CreateAddon) 