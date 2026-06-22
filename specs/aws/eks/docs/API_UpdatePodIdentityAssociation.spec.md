---
id: "@specs/aws/eks/docs/API_UpdatePodIdentityAssociation"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS UpdatePodIdentityAssociation"
status: active
depends_on:
  - "@specs/aws/eks/meta"
---

# UpdatePodIdentityAssociation

> **source:** AWS Documentation
> **spec:id:** @specs/aws/eks/docs/API_UpdatePodIdentityAssociation
> **target_lang:** meta — documentation tier. ALL sections preserved.



# UpdatePodIdentityAssociation
<a name="API_UpdatePodIdentityAssociation"></a>

Updates a EKS Pod Identity association. In an update, you can change the IAM role, the target IAM role, or `disableSessionTags`. You must change at least one of these in an update. An association can't be moved between clusters, namespaces, or service accounts. If you need to edit the namespace or service account, you need to delete the association and then create a new association with your desired settings.

Similar to AWS IAM behavior, EKS Pod Identity associations are eventually consistent, and may take several seconds to be effective after the initial API call returns successfully. You must design your applications to account for these potential delays. We recommend that you don’t include association create/updates in the critical, high-availability code paths of your application. Instead, make changes in a separate initialization or setup routine that you run less frequently.

You can set a *target IAM role* in the same or a different account for advanced scenarios. With a target role, EKS Pod Identity automatically performs two role assumptions in sequence: first assuming the role in the association that is in this account, then using those credentials to assume the target IAM role. This process provides your Pod with temporary credentials that have the permissions defined in the target role, allowing secure access to resources in another AWS account.

## Request Syntax
<a name="API_UpdatePodIdentityAssociation_RequestSyntax"></a>

```
POST /clusters/{{name}}/pod-identity-associations/{{associationId}} HTTP/1.1
Content-type: application/json

{
   "clientRequestToken": "{{string}}",
   "disableSessionTags": {{boolean}},
   "policy": "{{string}}",
   "roleArn": "{{string}}",
   "targetRoleArn": "{{string}}"
}
```

## URI Request Parameters
<a name="API_UpdatePodIdentityAssociation_RequestParameters"></a>

The request uses the following URI parameters.

 ** [associationId](#API_UpdatePodIdentityAssociation_RequestSyntax) **   <a name="AmazonEKS-UpdatePodIdentityAssociation-request-uri-associationId"></a>
The ID of the association to be updated.  
Required: Yes

 ** [name](#API_UpdatePodIdentityAssociation_RequestSyntax) **   <a name="AmazonEKS-UpdatePodIdentityAssociation-request-uri-clusterName"></a>
The name of the cluster that you want to update the association in.  
Required: Yes

## Request Body
<a name="API_UpdatePodIdentityAssociation_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [clientRequestToken](#API_UpdatePodIdentityAssociation_RequestSyntax) **   <a name="AmazonEKS-UpdatePodIdentityAssociation-request-clientRequestToken"></a>
A unique, case-sensitive identifier that you provide to ensure the idempotency of the request.  
Type: String  
Required: No

 ** [disableSessionTags](#API_UpdatePodIdentityAssociation_RequestSyntax) **   <a name="AmazonEKS-UpdatePodIdentityAssociation-request-disableSessionTags"></a>
Disable the automatic sessions tags that are appended by EKS Pod Identity.  
EKS Pod Identity adds a pre-defined set of session tags when it assumes the role. You can use these tags to author a single role that can work across resources by allowing access to AWS resources based on matching tags. By default, EKS Pod Identity attaches six tags, including tags for cluster name, namespace, and service account name. For the list of tags added by EKS Pod Identity, see [List of session tags added by EKS Pod Identity](https://docs.aws.amazon.com/eks/latest/userguide/pod-id-abac.html#pod-id-abac-tags) in the *Amazon EKS User Guide*.  
 AWS compresses inline session policies, managed policy ARNs, and session tags into a packed binary format that has a separate limit. If you receive a `PackedPolicyTooLarge` error indicating the packed binary format has exceeded the size limit, you can attempt to reduce the size by disabling the session tags added by EKS Pod Identity.  
Type: Boolean  
Required: No

 ** [policy](#API_UpdatePodIdentityAssociation_RequestSyntax) **   <a name="AmazonEKS-UpdatePodIdentityAssociation-request-policy"></a>
An optional IAM policy in JSON format (as an escaped string) that applies additional restrictions to this pod identity association beyond the IAM policies attached to the IAM role. This policy is applied as the intersection of the role's policies and this policy, allowing you to reduce the permissions that applications in the pods can use. Use this policy to enforce least privilege access while still leveraging a shared IAM role across multiple applications.  
 **Important considerations**   
+  **Session tags:** When using this policy, `disableSessionTags` must be set to `true`.
+  **Target role permissions:** If you specify both a `TargetRoleArn` and a policy, the policy restrictions apply only to the target role's permissions, not to the initial role used for assuming the target role.
Type: String  
Required: No

 ** [roleArn](#API_UpdatePodIdentityAssociation_RequestSyntax) **   <a name="AmazonEKS-UpdatePodIdentityAssociation-request-roleArn"></a>
The new IAM role to change in the association.  
Type: String  
Required: No

 ** [targetRoleArn](#API_UpdatePodIdentityAssociation_RequestSyntax) **   <a name="AmazonEKS-UpdatePodIdentityAssociation-request-targetRoleArn"></a>
The Amazon Resource Name (ARN) of the target IAM role to associate with the service account. This role is assumed by using the EKS Pod Identity association role, then the credentials for this role are injected into the Pod.  
When you run applications on Amazon EKS, your application might need to access AWS resources from a different role that exists in the same or different AWS account. For example, your application running in “Account A” might need to access resources, such as buckets in “Account B” or within “Account A” itself. You can create a association to access AWS resources in “Account B” by creating two IAM roles: a role in “Account A” and a role in “Account B” (which can be the same or different account), each with the necessary trust and permission policies. After you provide these roles in the *IAM role* and *Target IAM role* fields, EKS will perform role chaining to ensure your application gets the required permissions. This means Role A will assume Role B, allowing your Pods to securely access resources like S3 buckets in the target account.  
Type: String  
Required: No

## Response Syntax
<a name="API_UpdatePodIdentityAssociation_ResponseSyntax"></a>

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
<a name="API_UpdatePodIdentityAssociation_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [association](#API_UpdatePodIdentityAssociation_ResponseSyntax) **   <a name="AmazonEKS-UpdatePodIdentityAssociation-response-association"></a>
The full description of the association that was updated.  
Type: [PodIdentityAssociation](API_PodIdentityAssociation.md) object

## Errors
<a name="API_UpdatePodIdentityAssociation_Errors"></a>

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

## See Also
<a name="API_UpdatePodIdentityAssociation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/eks-2017-11-01/UpdatePodIdentityAssociation) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/eks-2017-11-01/UpdatePodIdentityAssociation) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/eks-2017-11-01/UpdatePodIdentityAssociation) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/eks-2017-11-01/UpdatePodIdentityAssociation) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/eks-2017-11-01/UpdatePodIdentityAssociation) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/eks-2017-11-01/UpdatePodIdentityAssociation) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/eks-2017-11-01/UpdatePodIdentityAssociation) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/eks-2017-11-01/UpdatePodIdentityAssociation) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/eks-2017-11-01/UpdatePodIdentityAssociation) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/eks-2017-11-01/UpdatePodIdentityAssociation) 