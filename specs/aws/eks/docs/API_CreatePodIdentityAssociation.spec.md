---
id: "@specs/aws/eks/docs/API_CreatePodIdentityAssociation"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS CreatePodIdentityAssociation"
status: active
depends_on:
  - "@specs/aws/eks/meta"
---

# CreatePodIdentityAssociation

> **source:** AWS Documentation
> **spec:id:** @specs/aws/eks/docs/API_CreatePodIdentityAssociation
> **target_lang:** meta — documentation tier. ALL sections preserved.



# CreatePodIdentityAssociation
<a name="API_CreatePodIdentityAssociation"></a>

Creates an EKS Pod Identity association between a service account in an Amazon EKS cluster and an IAM role with *EKS Pod Identity*. Use EKS Pod Identity to give temporary IAM credentials to Pods and the credentials are rotated automatically.

Amazon EKS Pod Identity associations provide the ability to manage credentials for your applications, similar to the way that Amazon EC2 instance profiles provide credentials to Amazon EC2 instances.

If a Pod uses a service account that has an association, Amazon EKS sets environment variables in the containers of the Pod. The environment variables configure the AWS SDKs, including the AWS Command Line Interface, to use the EKS Pod Identity credentials.

EKS Pod Identity is a simpler method than *IAM roles for service accounts*, as this method doesn't use OIDC identity providers. Additionally, you can configure a role for EKS Pod Identity once, and reuse it across clusters.

Similar to AWS IAM behavior, EKS Pod Identity associations are eventually consistent, and may take several seconds to be effective after the initial API call returns successfully. You must design your applications to account for these potential delays. We recommend that you don’t include association create/updates in the critical, high-availability code paths of your application. Instead, make changes in a separate initialization or setup routine that you run less frequently.

You can set a *target IAM role* in the same or a different account for advanced scenarios. With a target role, EKS Pod Identity automatically performs two role assumptions in sequence: first assuming the role in the association that is in this account, then using those credentials to assume the target IAM role. This process provides your Pod with temporary credentials that have the permissions defined in the target role, allowing secure access to resources in another AWS account.

## Request Syntax
<a name="API_CreatePodIdentityAssociation_RequestSyntax"></a>

```
POST /clusters/{{name}}/pod-identity-associations HTTP/1.1
Content-type: application/json

{
   "clientRequestToken": "{{string}}",
   "disableSessionTags": {{boolean}},
   "namespace": "{{string}}",
   "policy": "{{string}}",
   "roleArn": "{{string}}",
   "serviceAccount": "{{string}}",
   "tags": { 
      "{{string}}" : "{{string}}" 
   },
   "targetRoleArn": "{{string}}"
}
```

## URI Request Parameters
<a name="API_CreatePodIdentityAssociation_RequestParameters"></a>

The request uses the following URI parameters.

 ** [name](#API_CreatePodIdentityAssociation_RequestSyntax) **   <a name="AmazonEKS-CreatePodIdentityAssociation-request-uri-clusterName"></a>
The name of the cluster to create the EKS Pod Identity association in.  
Required: Yes

## Request Body
<a name="API_CreatePodIdentityAssociation_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [clientRequestToken](#API_CreatePodIdentityAssociation_RequestSyntax) **   <a name="AmazonEKS-CreatePodIdentityAssociation-request-clientRequestToken"></a>
A unique, case-sensitive identifier that you provide to ensure the idempotency of the request.  
Type: String  
Required: No

 ** [disableSessionTags](#API_CreatePodIdentityAssociation_RequestSyntax) **   <a name="AmazonEKS-CreatePodIdentityAssociation-request-disableSessionTags"></a>
Disable the automatic sessions tags that are appended by EKS Pod Identity.  
EKS Pod Identity adds a pre-defined set of session tags when it assumes the role. You can use these tags to author a single role that can work across resources by allowing access to AWS resources based on matching tags. By default, EKS Pod Identity attaches six tags, including tags for cluster name, namespace, and service account name. For the list of tags added by EKS Pod Identity, see [List of session tags added by EKS Pod Identity](https://docs.aws.amazon.com/eks/latest/userguide/pod-id-abac.html#pod-id-abac-tags) in the *Amazon EKS User Guide*.  
 AWS compresses inline session policies, managed policy ARNs, and session tags into a packed binary format that has a separate limit. If you receive a `PackedPolicyTooLarge` error indicating the packed binary format has exceeded the size limit, you can attempt to reduce the size by disabling the session tags added by EKS Pod Identity.  
Type: Boolean  
Required: No

 ** [namespace](#API_CreatePodIdentityAssociation_RequestSyntax) **   <a name="AmazonEKS-CreatePodIdentityAssociation-request-namespace"></a>
The name of the Kubernetes namespace inside the cluster to create the EKS Pod Identity association in. The service account and the Pods that use the service account must be in this namespace.  
Type: String  
Required: Yes

 ** [policy](#API_CreatePodIdentityAssociation_RequestSyntax) **   <a name="AmazonEKS-CreatePodIdentityAssociation-request-policy"></a>
An optional IAM policy in JSON format (as an escaped string) that applies additional restrictions to this pod identity association beyond the IAM policies attached to the IAM role. This policy is applied as the intersection of the role's policies and this policy, allowing you to reduce the permissions that applications in the pods can use. Use this policy to enforce least privilege access while still leveraging a shared IAM role across multiple applications.  
 **Important considerations**   
+  **Session tags:** When using this policy, `disableSessionTags` must be set to `true`.
+  **Target role permissions:** If you specify both a `TargetRoleArn` and a policy, the policy restrictions apply only to the target role's permissions, not to the initial role used for assuming the target role.
Type: String  
Required: No

 ** [roleArn](#API_CreatePodIdentityAssociation_RequestSyntax) **   <a name="AmazonEKS-CreatePodIdentityAssociation-request-roleArn"></a>
The Amazon Resource Name (ARN) of the IAM role to associate with the service account. The EKS Pod Identity agent manages credentials to assume this role for applications in the containers in the Pods that use this service account.  
Type: String  
Required: Yes

 ** [serviceAccount](#API_CreatePodIdentityAssociation_RequestSyntax) **   <a name="AmazonEKS-CreatePodIdentityAssociation-request-serviceAccount"></a>
The name of the Kubernetes service account inside the cluster to associate the IAM credentials with.  
Type: String  
Required: Yes

 ** [tags](#API_CreatePodIdentityAssociation_RequestSyntax) **   <a name="AmazonEKS-CreatePodIdentityAssociation-request-tags"></a>
Metadata that assists with categorization and organization. Each tag consists of a key and an optional value. You define both. Tags don't propagate to any other cluster or AWS resources.  
The following basic restrictions apply to tags:  
+ Maximum number of tags per resource – 50
+ For each resource, each tag key must be unique, and each tag key can have only one value.
+ Maximum key length – 128 Unicode characters in UTF-8
+ Maximum value length – 256 Unicode characters in UTF-8
+ If your tagging schema is used across multiple services and resources, remember that other services may have restrictions on allowed characters. Generally allowed characters are: letters, numbers, and spaces representable in UTF-8, and the following characters: \+ - = . \_ : / @.
+ Tag keys and values are case-sensitive.
+ Do not use `aws:`, `AWS:`, or any upper or lowercase combination of such as a prefix for either keys or values as it is reserved for AWS use. You cannot edit or delete tag keys or values with this prefix. Tags with this prefix do not count against your tags per resource limit.
Type: String to string map  
Map Entries: Maximum number of 50 items.  
Key Length Constraints: Minimum length of 1. Maximum length of 128.  
Value Length Constraints: Maximum length of 256.  
Required: No

 ** [targetRoleArn](#API_CreatePodIdentityAssociation_RequestSyntax) **   <a name="AmazonEKS-CreatePodIdentityAssociation-request-targetRoleArn"></a>
The Amazon Resource Name (ARN) of the target IAM role to associate with the service account. This role is assumed by using the EKS Pod Identity association role, then the credentials for this role are injected into the Pod.  
When you run applications on Amazon EKS, your application might need to access AWS resources from a different role that exists in the same or different AWS account. For example, your application running in “Account A” might need to access resources, such as Amazon S3 buckets in “Account B” or within “Account A” itself. You can create a association to access AWS resources in “Account B” by creating two IAM roles: a role in “Account A” and a role in “Account B” (which can be the same or different account), each with the necessary trust and permission policies. After you provide these roles in the *IAM role* and *Target IAM role* fields, EKS will perform role chaining to ensure your application gets the required permissions. This means Role A will assume Role B, allowing your Pods to securely access resources like S3 buckets in the target account.  
Type: String  
Required: No

## Response Syntax
<a name="API_CreatePodIdentityAssociation_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "association": { 
      "associationArn": "string",
      "associationId": "string",
      "clusterName": "string",
      "createdAt": number,
      "disableSessionTags": boolean,
      "externalId": "string",
      "modifiedAt": number,
      "namespace": "string",
      "ownerArn": "string",
      "policy": "string",
      "roleArn": "string",
      "serviceAccount": "string",
      "tags": { 
         "string" : "string" 
      },
      "targetRoleArn": "string"
   }
}
```

## Response Elements
<a name="API_CreatePodIdentityAssociation_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [association](#API_CreatePodIdentityAssociation_ResponseSyntax) **   <a name="AmazonEKS-CreatePodIdentityAssociation-response-association"></a>
The full description of your new association.  
The description includes an ID for the association. Use the ID of the association in further actions to manage the association.  
Type: [PodIdentityAssociation](API_PodIdentityAssociation.md) object

## Errors
<a name="API_CreatePodIdentityAssociation_Errors"></a>

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

## See Also
<a name="API_CreatePodIdentityAssociation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/eks-2017-11-01/CreatePodIdentityAssociation) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/eks-2017-11-01/CreatePodIdentityAssociation) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/eks-2017-11-01/CreatePodIdentityAssociation) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/eks-2017-11-01/CreatePodIdentityAssociation) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/eks-2017-11-01/CreatePodIdentityAssociation) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/eks-2017-11-01/CreatePodIdentityAssociation) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/eks-2017-11-01/CreatePodIdentityAssociation) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/eks-2017-11-01/CreatePodIdentityAssociation) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/eks-2017-11-01/CreatePodIdentityAssociation) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/eks-2017-11-01/CreatePodIdentityAssociation) 