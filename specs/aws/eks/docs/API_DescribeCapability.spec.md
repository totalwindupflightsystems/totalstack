---
id: "@specs/aws/eks/docs/API_DescribeCapability"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS DescribeCapability"
status: active
depends_on:
  - "@specs/aws/eks/meta"
---

# DescribeCapability

> **source:** AWS Documentation
> **spec:id:** @specs/aws/eks/docs/API_DescribeCapability
> **target_lang:** meta — documentation tier. ALL sections preserved.



# DescribeCapability
<a name="API_DescribeCapability"></a>

Returns detailed information about a specific managed capability in your Amazon EKS cluster, including its current status, configuration, health information, and any issues that may be affecting its operation.

## Request Syntax
<a name="API_DescribeCapability_RequestSyntax"></a>

```
GET /clusters/{{name}}/capabilities/{{capabilityName}} HTTP/1.1
```

## URI Request Parameters
<a name="API_DescribeCapability_RequestParameters"></a>

The request uses the following URI parameters.

 ** [capabilityName](#API_DescribeCapability_RequestSyntax) **   <a name="AmazonEKS-DescribeCapability-request-uri-capabilityName"></a>
The name of the capability to describe.  
Required: Yes

 ** [name](#API_DescribeCapability_RequestSyntax) **   <a name="AmazonEKS-DescribeCapability-request-uri-clusterName"></a>
The name of the Amazon EKS cluster that contains the capability you want to describe.  
Required: Yes

## Request Body
<a name="API_DescribeCapability_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_DescribeCapability_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "capability": { 
      "arn": "string",
      "capabilityName": "string",
      "clusterName": "string",
      "configuration": { 
         "argoCd": { 
            "awsIdc": { 
               "idcInstanceArn": "string",
               "idcManagedApplicationArn": "string",
               "idcRegion": "string"
            },
            "namespace": "string",
            "networkAccess": { 
               "vpceIds": [ "string" ]
            },
            "rbacRoleMappings": [ 
               { 
                  "identities": [ 
                     { 
                        "id": "string",
                        "type": "string"
                     }
                  ],
                  "role": "string"
               }
            ],
            "serverUrl": "string"
         }
      },
      "createdAt": number,
      "deletePropagationPolicy": "string",
      "health": { 
         "issues": [ 
            { 
               "code": "string",
               "message": "string"
            }
         ]
      },
      "modifiedAt": number,
      "roleArn": "string",
      "status": "string",
      "tags": { 
         "string" : "string" 
      },
      "type": "string",
      "version": "string"
   }
}
```

## Response Elements
<a name="API_DescribeCapability_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [capability](#API_DescribeCapability_ResponseSyntax) **   <a name="AmazonEKS-DescribeCapability-response-capability"></a>
An object containing detailed information about the capability, including its name, ARN, type, status, version, configuration, health status, and timestamps for when it was created and last modified.  
Type: [Capability](API_Capability.md) object

## Errors
<a name="API_DescribeCapability_Errors"></a>

For information about the errors that are common to all actions, see [Common Errors](CommonErrors.md).

 ** AccessDeniedException **   
You don't have permissions to perform the requested operation. The [IAM principal](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_terms-and-concepts.html) making the request must have at least one IAM permissions policy attached that grants the required permissions. For more information, see [Access management](https://docs.aws.amazon.com/IAM/latest/UserGuide/access.html) in the *IAM User Guide*.     
 ** message **   
You do not have sufficient access to perform this action.
HTTP Status Code: 403

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
<a name="API_DescribeCapability_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/eks-2017-11-01/DescribeCapability) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/eks-2017-11-01/DescribeCapability) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/eks-2017-11-01/DescribeCapability) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/eks-2017-11-01/DescribeCapability) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/eks-2017-11-01/DescribeCapability) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/eks-2017-11-01/DescribeCapability) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/eks-2017-11-01/DescribeCapability) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/eks-2017-11-01/DescribeCapability) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/eks-2017-11-01/DescribeCapability) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/eks-2017-11-01/DescribeCapability) 