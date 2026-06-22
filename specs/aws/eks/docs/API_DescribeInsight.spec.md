---
id: "@specs/aws/eks/docs/API_DescribeInsight"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS DescribeInsight"
status: active
depends_on:
  - "@specs/aws/eks/meta"
---

# DescribeInsight

> **source:** AWS Documentation
> **spec:id:** @specs/aws/eks/docs/API_DescribeInsight
> **target_lang:** meta — documentation tier. ALL sections preserved.



# DescribeInsight
<a name="API_DescribeInsight"></a>

Returns details about an insight that you specify using its ID.

## Request Syntax
<a name="API_DescribeInsight_RequestSyntax"></a>

```
GET /clusters/{{name}}/insights/{{id}} HTTP/1.1
```

## URI Request Parameters
<a name="API_DescribeInsight_RequestParameters"></a>

The request uses the following URI parameters.

 ** [name](#API_DescribeInsight_RequestSyntax) **   <a name="AmazonEKS-DescribeInsight-request-uri-clusterName"></a>
The name of the cluster to describe the insight for.  
Required: Yes

 ** [id](#API_DescribeInsight_RequestSyntax) **   <a name="AmazonEKS-DescribeInsight-request-uri-id"></a>
The identity of the insight to describe.  
Required: Yes

## Request Body
<a name="API_DescribeInsight_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_DescribeInsight_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "insight": { 
      "additionalInfo": { 
         "string" : "string" 
      },
      "category": "string",
      "categorySpecificSummary": { 
         "addonCompatibilityDetails": [ 
            { 
               "compatibleVersions": [ "string" ],
               "name": "string"
            }
         ],
         "deprecationDetails": [ 
            { 
               "clientStats": [ 
                  { 
                     "lastRequestTime": number,
                     "numberOfRequestsLast30Days": number,
                     "userAgent": "string"
                  }
               ],
               "replacedWith": "string",
               "startServingReplacementVersion": "string",
               "stopServingVersion": "string",
               "usage": "string"
            }
         ]
      },
      "description": "string",
      "id": "string",
      "insightStatus": { 
         "reason": "string",
         "status": "string"
      },
      "kubernetesVersion": "string",
      "lastRefreshTime": number,
      "lastTransitionTime": number,
      "name": "string",
      "recommendation": "string",
      "resources": [ 
         { 
            "arn": "string",
            "insightStatus": { 
               "reason": "string",
               "status": "string"
            },
            "kubernetesResourceUri": "string"
         }
      ]
   }
}
```

## Response Elements
<a name="API_DescribeInsight_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [insight](#API_DescribeInsight_ResponseSyntax) **   <a name="AmazonEKS-DescribeInsight-response-insight"></a>
The full description of the insight.  
Type: [Insight](API_Insight.md) object

## Errors
<a name="API_DescribeInsight_Errors"></a>

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
<a name="API_DescribeInsight_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/eks-2017-11-01/DescribeInsight) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/eks-2017-11-01/DescribeInsight) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/eks-2017-11-01/DescribeInsight) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/eks-2017-11-01/DescribeInsight) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/eks-2017-11-01/DescribeInsight) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/eks-2017-11-01/DescribeInsight) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/eks-2017-11-01/DescribeInsight) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/eks-2017-11-01/DescribeInsight) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/eks-2017-11-01/DescribeInsight) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/eks-2017-11-01/DescribeInsight) 