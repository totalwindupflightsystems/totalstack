---
id: "@specs/aws/eks/docs/API_DescribeInsightsRefresh"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS DescribeInsightsRefresh"
status: active
depends_on:
  - "@specs/aws/eks/meta"
---

# DescribeInsightsRefresh

> **source:** AWS Documentation
> **spec:id:** @specs/aws/eks/docs/API_DescribeInsightsRefresh
> **target_lang:** meta — documentation tier. ALL sections preserved.



# DescribeInsightsRefresh
<a name="API_DescribeInsightsRefresh"></a>

Returns the status of the latest on-demand cluster insights refresh operation.

## Request Syntax
<a name="API_DescribeInsightsRefresh_RequestSyntax"></a>

```
GET /clusters/{{name}}/insights-refresh HTTP/1.1
```

## URI Request Parameters
<a name="API_DescribeInsightsRefresh_RequestParameters"></a>

The request uses the following URI parameters.

 ** [name](#API_DescribeInsightsRefresh_RequestSyntax) **   <a name="AmazonEKS-DescribeInsightsRefresh-request-uri-clusterName"></a>
The name of the cluster associated with the insights refresh operation.  
Required: Yes

## Request Body
<a name="API_DescribeInsightsRefresh_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_DescribeInsightsRefresh_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "endedAt": number,
   "message": "string",
   "startedAt": number,
   "status": "string"
}
```

## Response Elements
<a name="API_DescribeInsightsRefresh_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [endedAt](#API_DescribeInsightsRefresh_ResponseSyntax) **   <a name="AmazonEKS-DescribeInsightsRefresh-response-endedAt"></a>
The date and time when the insights refresh operation ended.  
Type: Timestamp

 ** [message](#API_DescribeInsightsRefresh_ResponseSyntax) **   <a name="AmazonEKS-DescribeInsightsRefresh-response-message"></a>
The message associated with the insights refresh operation.  
Type: String

 ** [startedAt](#API_DescribeInsightsRefresh_ResponseSyntax) **   <a name="AmazonEKS-DescribeInsightsRefresh-response-startedAt"></a>
The date and time when the insights refresh operation started.  
Type: Timestamp

 ** [status](#API_DescribeInsightsRefresh_ResponseSyntax) **   <a name="AmazonEKS-DescribeInsightsRefresh-response-status"></a>
The current status of the insights refresh operation.  
Type: String  
Valid Values: `IN_PROGRESS | FAILED | COMPLETED` 

## Errors
<a name="API_DescribeInsightsRefresh_Errors"></a>

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

## Examples
<a name="API_DescribeInsightsRefresh_Examples"></a>

### Example of refresh in progress
<a name="API_DescribeInsightsRefresh_Example_1"></a>

The following example shows when the cluster insights refresh workflow is in progress.

#### Sample Request
<a name="API_DescribeInsightsRefresh_Example_1_Request"></a>

```
GET /clusters/name/insights-refresh HTTP/1.1
```

#### Sample Response
<a name="API_DescribeInsightsRefresh_Example_1_Response"></a>

```
HTTP/1.1 200
Content-type: application/json

{
    "message": "Cluster insights refresh is in progress.",
    "status": "IN_PROGRESS",
    "startedAt": "2025-08-19T13:45:11-07:00"
}
```

### Example of refresh completion
<a name="API_DescribeInsightsRefresh_Example_2"></a>

The following example shows when the cluster insights refresh workflow completed successfully.

#### Sample Request
<a name="API_DescribeInsightsRefresh_Example_2_Request"></a>

```
GET /clusters/name/insights-refresh HTTP/1.1
```

#### Sample Response
<a name="API_DescribeInsightsRefresh_Example_2_Response"></a>

```
HTTP/1.1 200
Content-type: application/json

{
    "message": "Cluster insights refresh has completed successfully.",
    "status": "COMPLETED",
    "startedAt": "2025-08-19T13:45:11-07:00",
    "endedAt": "2025-08-19T13:45:50-07:00"
}
```

### Example of refresh error
<a name="API_DescribeInsightsRefresh_Example_3"></a>

The following example shows when the cluster insights refresh workflow encountered an error.

#### Sample Request
<a name="API_DescribeInsightsRefresh_Example_3_Request"></a>

```
GET /clusters/name/insights-refresh HTTP/1.1
```

#### Sample Response
<a name="API_DescribeInsightsRefresh_Example_3_Response"></a>

```
HTTP/1.1 200
Content-type: application/json

{
    "message": "The latest cluster insights refresh encountered an error. Try StartInsightsRefresh again.",
    "status": "FAILED",
    "startedAt": "2025-08-19T13:45:11-07:00",
    "endedAt": "2025-08-19T13:45:50-07:00"
}
```

## See Also
<a name="API_DescribeInsightsRefresh_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/eks-2017-11-01/DescribeInsightsRefresh) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/eks-2017-11-01/DescribeInsightsRefresh) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/eks-2017-11-01/DescribeInsightsRefresh) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/eks-2017-11-01/DescribeInsightsRefresh) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/eks-2017-11-01/DescribeInsightsRefresh) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/eks-2017-11-01/DescribeInsightsRefresh) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/eks-2017-11-01/DescribeInsightsRefresh) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/eks-2017-11-01/DescribeInsightsRefresh) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/eks-2017-11-01/DescribeInsightsRefresh) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/eks-2017-11-01/DescribeInsightsRefresh) 