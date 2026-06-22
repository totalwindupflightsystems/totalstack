---
id: "@specs/aws/eks/docs/API_CreateEksAnywhereSubscription"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS CreateEksAnywhereSubscription"
status: active
depends_on:
  - "@specs/aws/eks/meta"
---

# CreateEksAnywhereSubscription

> **source:** AWS Documentation
> **spec:id:** @specs/aws/eks/docs/API_CreateEksAnywhereSubscription
> **target_lang:** meta — documentation tier. ALL sections preserved.



# CreateEksAnywhereSubscription
<a name="API_CreateEksAnywhereSubscription"></a>

Creates an EKS Anywhere subscription. When a subscription is created, it is a contract agreement for the length of the term specified in the request. Licenses that are used to validate support are provisioned in AWS License Manager and the caller account is granted access to EKS Anywhere Curated Packages.

## Request Syntax
<a name="API_CreateEksAnywhereSubscription_RequestSyntax"></a>

```
POST /eks-anywhere-subscriptions HTTP/1.1
Content-type: application/json

{
   "autoRenew": {{boolean}},
   "clientRequestToken": "{{string}}",
   "licenseQuantity": {{number}},
   "licenseType": "{{string}}",
   "name": "{{string}}",
   "tags": { 
      "{{string}}" : "{{string}}" 
   },
   "term": { 
      "duration": {{number}},
      "unit": "{{string}}"
   }
}
```

## URI Request Parameters
<a name="API_CreateEksAnywhereSubscription_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_CreateEksAnywhereSubscription_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [autoRenew](#API_CreateEksAnywhereSubscription_RequestSyntax) **   <a name="AmazonEKS-CreateEksAnywhereSubscription-request-autoRenew"></a>
A boolean indicating whether the subscription auto renews at the end of the term.  
Type: Boolean  
Required: No

 ** [clientRequestToken](#API_CreateEksAnywhereSubscription_RequestSyntax) **   <a name="AmazonEKS-CreateEksAnywhereSubscription-request-clientRequestToken"></a>
A unique, case-sensitive identifier that you provide to ensure the idempotency of the request.  
Type: String  
Required: No

 ** [licenseQuantity](#API_CreateEksAnywhereSubscription_RequestSyntax) **   <a name="AmazonEKS-CreateEksAnywhereSubscription-request-licenseQuantity"></a>
The number of licenses to purchase with the subscription. Valid values are between 1 and 100. This value can't be changed after creating the subscription.  
Type: Integer  
Required: No

 ** [licenseType](#API_CreateEksAnywhereSubscription_RequestSyntax) **   <a name="AmazonEKS-CreateEksAnywhereSubscription-request-licenseType"></a>
The license type for all licenses in the subscription. Valid value is CLUSTER. With the CLUSTER license type, each license covers support for a single EKS Anywhere cluster.  
Type: String  
Valid Values: `Cluster`   
Required: No

 ** [name](#API_CreateEksAnywhereSubscription_RequestSyntax) **   <a name="AmazonEKS-CreateEksAnywhereSubscription-request-name"></a>
The unique name for your subscription. It must be unique in your AWS account in the AWS Region you're creating the subscription in. The name can contain only alphanumeric characters (case-sensitive), hyphens, and underscores. It must start with an alphabetic character and can't be longer than 100 characters.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 100.  
Pattern: `^[0-9A-Za-z][A-Za-z0-9\-_]*`   
Required: Yes

 ** [tags](#API_CreateEksAnywhereSubscription_RequestSyntax) **   <a name="AmazonEKS-CreateEksAnywhereSubscription-request-tags"></a>
The metadata for a subscription to assist with categorization and organization. Each tag consists of a key and an optional value. Subscription tags don't propagate to any other resources associated with the subscription.  
Type: String to string map  
Map Entries: Maximum number of 50 items.  
Key Length Constraints: Minimum length of 1. Maximum length of 128.  
Value Length Constraints: Maximum length of 256.  
Required: No

 ** [term](#API_CreateEksAnywhereSubscription_RequestSyntax) **   <a name="AmazonEKS-CreateEksAnywhereSubscription-request-term"></a>
An object representing the term duration and term unit type of your subscription. This determines the term length of your subscription. Valid values are MONTHS for term unit and 12 or 36 for term duration, indicating a 12 month or 36 month subscription. This value cannot be changed after creating the subscription.  
Type: [EksAnywhereSubscriptionTerm](API_EksAnywhereSubscriptionTerm.md) object  
Required: Yes

## Response Syntax
<a name="API_CreateEksAnywhereSubscription_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "subscription": { 
      "arn": "string",
      "autoRenew": boolean,
      "createdAt": number,
      "effectiveDate": number,
      "expirationDate": number,
      "id": "string",
      "licenseArns": [ "string" ],
      "licenseQuantity": number,
      "licenses": [ 
         { 
            "id": "string",
            "token": "string"
         }
      ],
      "licenseType": "string",
      "status": "string",
      "tags": { 
         "string" : "string" 
      },
      "term": { 
         "duration": number,
         "unit": "string"
      }
   }
}
```

## Response Elements
<a name="API_CreateEksAnywhereSubscription_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [subscription](#API_CreateEksAnywhereSubscription_ResponseSyntax) **   <a name="AmazonEKS-CreateEksAnywhereSubscription-response-subscription"></a>
The full description of the subscription.  
Type: [EksAnywhereSubscription](API_EksAnywhereSubscription.md) object

## Errors
<a name="API_CreateEksAnywhereSubscription_Errors"></a>

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

 ** ServiceUnavailableException **   
The service is unavailable. Back off and retry the operation.    
 ** message **   
The request has failed due to a temporary failure of the server.
HTTP Status Code: 503

## See Also
<a name="API_CreateEksAnywhereSubscription_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/eks-2017-11-01/CreateEksAnywhereSubscription) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/eks-2017-11-01/CreateEksAnywhereSubscription) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/eks-2017-11-01/CreateEksAnywhereSubscription) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/eks-2017-11-01/CreateEksAnywhereSubscription) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/eks-2017-11-01/CreateEksAnywhereSubscription) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/eks-2017-11-01/CreateEksAnywhereSubscription) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/eks-2017-11-01/CreateEksAnywhereSubscription) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/eks-2017-11-01/CreateEksAnywhereSubscription) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/eks-2017-11-01/CreateEksAnywhereSubscription) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/eks-2017-11-01/CreateEksAnywhereSubscription) 