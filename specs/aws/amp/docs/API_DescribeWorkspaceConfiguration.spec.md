---
id: "@specs/aws/amp/docs/API_DescribeWorkspaceConfiguration"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS DescribeWorkspaceConfiguration"
status: active
depends_on:
  - "@specs/aws/amp/meta"
---

# DescribeWorkspaceConfiguration

> **source:** AWS Documentation
> **spec:id:** @specs/aws/amp/docs/API_DescribeWorkspaceConfiguration
> **target_lang:** meta — documentation tier. ALL sections preserved.



# DescribeWorkspaceConfiguration
<a name="API_DescribeWorkspaceConfiguration"></a>

Use this operation to return information about the configuration of a workspace. The configuration details returned include workspace configuration status, label set limits, and retention period.

## Request Syntax
<a name="API_DescribeWorkspaceConfiguration_RequestSyntax"></a>

```
GET /workspaces/{{workspaceId}}/configuration HTTP/1.1
```

## URI Request Parameters
<a name="API_DescribeWorkspaceConfiguration_RequestParameters"></a>

The request uses the following URI parameters.

 ** [workspaceId](#API_DescribeWorkspaceConfiguration_RequestSyntax) **   <a name="prometheus-DescribeWorkspaceConfiguration-request-uri-workspaceId"></a>
The ID of the workspace that you want to retrieve information for. To find the IDs of your workspaces, use the [ListWorkspaces](https://docs.aws.amazon.com/prometheus/latest/APIReference/API_ListWorkspaces.htm) operation.  
Length Constraints: Minimum length of 1. Maximum length of 64.  
Pattern: `.*[0-9A-Za-z][-.0-9A-Z_a-z]*.*`   
Required: Yes

## Request Body
<a name="API_DescribeWorkspaceConfiguration_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_DescribeWorkspaceConfiguration_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "workspaceConfiguration": { 
      "limitsPerLabelSet": [ 
         { 
            "labelSet": { 
               "string" : "string" 
            },
            "limits": { 
               "maxSeries": number
            }
         }
      ],
      "retentionPeriodInDays": number,
      "status": { 
         "statusCode": "string",
         "statusReason": "string"
      }
   }
}
```

## Response Elements
<a name="API_DescribeWorkspaceConfiguration_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [workspaceConfiguration](#API_DescribeWorkspaceConfiguration_ResponseSyntax) **   <a name="prometheus-DescribeWorkspaceConfiguration-response-workspaceConfiguration"></a>
This structure contains the information about the workspace configuration.  
Type: [WorkspaceConfigurationDescription](API_WorkspaceConfigurationDescription.md) object

## Errors
<a name="API_DescribeWorkspaceConfiguration_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **   
You do not have sufficient access to perform this action.    
 ** message **   
Description of the error.
HTTP Status Code: 403

 ** InternalServerException **   
An unexpected error occurred during the processing of the request.    
 ** message **   
Description of the error.  
 ** retryAfterSeconds **   
Advice to clients on when the call can be safely retried.
HTTP Status Code: 500

 ** ResourceNotFoundException **   
The request references a resources that doesn't exist.    
 ** message **   
Description of the error.  
 ** resourceId **   
Identifier of the resource affected.  
 ** resourceType **   
Type of the resource affected.
HTTP Status Code: 404

 ** ThrottlingException **   
The request was denied due to request throttling.    
 ** message **   
Description of the error.  
 ** quotaCode **   
Service quotas code for the originating quota.  
 ** retryAfterSeconds **   
Advice to clients on when the call can be safely retried.  
 ** serviceCode **   
Service quotas code for the originating service.
HTTP Status Code: 429

 ** ValidationException **   
The input fails to satisfy the constraints specified by an AWS service.    
 ** fieldList **   
The field that caused the error, if applicable.  
 ** message **   
Description of the error.  
 ** reason **   
Reason the request failed validation.
HTTP Status Code: 400

## See Also
<a name="API_DescribeWorkspaceConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/amp-2020-08-01/DescribeWorkspaceConfiguration) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/amp-2020-08-01/DescribeWorkspaceConfiguration) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/amp-2020-08-01/DescribeWorkspaceConfiguration) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/amp-2020-08-01/DescribeWorkspaceConfiguration) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/amp-2020-08-01/DescribeWorkspaceConfiguration) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/amp-2020-08-01/DescribeWorkspaceConfiguration) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/amp-2020-08-01/DescribeWorkspaceConfiguration) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/amp-2020-08-01/DescribeWorkspaceConfiguration) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/amp-2020-08-01/DescribeWorkspaceConfiguration) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/amp-2020-08-01/DescribeWorkspaceConfiguration) 