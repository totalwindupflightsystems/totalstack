---
id: "@specs/aws/eks/docs/API_DescribeAddonConfiguration"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS DescribeAddonConfiguration"
status: active
depends_on:
  - "@specs/aws/eks/meta"
---

# DescribeAddonConfiguration

> **source:** AWS Documentation
> **spec:id:** @specs/aws/eks/docs/API_DescribeAddonConfiguration
> **target_lang:** meta — documentation tier. ALL sections preserved.



# DescribeAddonConfiguration
<a name="API_DescribeAddonConfiguration"></a>

Returns configuration options.

## Request Syntax
<a name="API_DescribeAddonConfiguration_RequestSyntax"></a>

```
GET /addons/configuration-schemas?addonName={{addonName}}&addonVersion={{addonVersion}} HTTP/1.1
```

## URI Request Parameters
<a name="API_DescribeAddonConfiguration_RequestParameters"></a>

The request uses the following URI parameters.

 ** [addonName](#API_DescribeAddonConfiguration_RequestSyntax) **   <a name="AmazonEKS-DescribeAddonConfiguration-request-uri-addonName"></a>
The name of the add-on. The name must match one of the names returned by `DescribeAddonVersions`.  
Required: Yes

 ** [addonVersion](#API_DescribeAddonConfiguration_RequestSyntax) **   <a name="AmazonEKS-DescribeAddonConfiguration-request-uri-addonVersion"></a>
The version of the add-on. The version must match one of the versions returned by [https://docs.aws.amazon.com/eks/latest/APIReference/API_DescribeAddonVersions.html](https://docs.aws.amazon.com/eks/latest/APIReference/API_DescribeAddonVersions.html).  
Required: Yes

## Request Body
<a name="API_DescribeAddonConfiguration_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_DescribeAddonConfiguration_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "addonName": "string",
   "addonVersion": "string",
   "configurationSchema": "string",
   "podIdentityConfiguration": [ 
      { 
         "recommendedManagedPolicies": [ "string" ],
         "serviceAccount": "string"
      }
   ]
}
```

## Response Elements
<a name="API_DescribeAddonConfiguration_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [addonName](#API_DescribeAddonConfiguration_ResponseSyntax) **   <a name="AmazonEKS-DescribeAddonConfiguration-response-addonName"></a>
The name of the add-on.  
Type: String

 ** [addonVersion](#API_DescribeAddonConfiguration_ResponseSyntax) **   <a name="AmazonEKS-DescribeAddonConfiguration-response-addonVersion"></a>
The version of the add-on. The version must match one of the versions returned by [https://docs.aws.amazon.com/eks/latest/APIReference/API_DescribeAddonVersions.html](https://docs.aws.amazon.com/eks/latest/APIReference/API_DescribeAddonVersions.html).  
Type: String

 ** [configurationSchema](#API_DescribeAddonConfiguration_ResponseSyntax) **   <a name="AmazonEKS-DescribeAddonConfiguration-response-configurationSchema"></a>
A JSON schema that's used to validate the configuration values you provide when an add-on is created or updated.  
Type: String

 ** [podIdentityConfiguration](#API_DescribeAddonConfiguration_ResponseSyntax) **   <a name="AmazonEKS-DescribeAddonConfiguration-response-podIdentityConfiguration"></a>
The Kubernetes service account name used by the add-on, and any suggested IAM policies. Use this information to create an IAM Role for the add-on.  
Type: Array of [AddonPodIdentityConfiguration](API_AddonPodIdentityConfiguration.md) objects

## Errors
<a name="API_DescribeAddonConfiguration_Errors"></a>

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
<a name="API_DescribeAddonConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/eks-2017-11-01/DescribeAddonConfiguration) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/eks-2017-11-01/DescribeAddonConfiguration) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/eks-2017-11-01/DescribeAddonConfiguration) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/eks-2017-11-01/DescribeAddonConfiguration) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/eks-2017-11-01/DescribeAddonConfiguration) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/eks-2017-11-01/DescribeAddonConfiguration) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/eks-2017-11-01/DescribeAddonConfiguration) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/eks-2017-11-01/DescribeAddonConfiguration) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/eks-2017-11-01/DescribeAddonConfiguration) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/eks-2017-11-01/DescribeAddonConfiguration) 