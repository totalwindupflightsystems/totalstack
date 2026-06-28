---
id: "@specs/aws/quicksight/docs/API_DescribeAnalysisPermissions"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS DescribeAnalysisPermissions"
status: active
depends_on:
  - "@specs/aws/quicksight/meta"
---

# DescribeAnalysisPermissions

> **source:** AWS Documentation
> **spec:id:** @specs/aws/quicksight/docs/API_DescribeAnalysisPermissions
> **target_lang:** meta — documentation tier. ALL sections preserved.



# DescribeAnalysisPermissions
<a name="API_DescribeAnalysisPermissions"></a>

Provides the read and write permissions for an analysis.

## Request Syntax
<a name="API_DescribeAnalysisPermissions_RequestSyntax"></a>

```
GET /accounts/{{AwsAccountId}}/analyses/{{AnalysisId}}/permissions HTTP/1.1
```

## URI Request Parameters
<a name="API_DescribeAnalysisPermissions_RequestParameters"></a>

The request uses the following URI parameters.

 ** [AnalysisId](#API_DescribeAnalysisPermissions_RequestSyntax) **   <a name="QS-DescribeAnalysisPermissions-request-uri-AnalysisId"></a>
The ID of the analysis whose permissions you're describing. The ID is part of the analysis URL.  
Length Constraints: Minimum length of 1. Maximum length of 512.  
Pattern: `[\w\-]+`   
Required: Yes

 ** [AwsAccountId](#API_DescribeAnalysisPermissions_RequestSyntax) **   <a name="QS-DescribeAnalysisPermissions-request-uri-AwsAccountId"></a>
The ID of the AWS account that contains the analysis whose permissions you're describing. You must be using the AWS account that the analysis is in.  
Length Constraints: Fixed length of 12.  
Pattern: `^[0-9]{12}$`   
Required: Yes

## Request Body
<a name="API_DescribeAnalysisPermissions_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_DescribeAnalysisPermissions_ResponseSyntax"></a>

```
HTTP/1.1 {{Status}}
Content-type: application/json

{
   "AnalysisArn": "string",
   "AnalysisId": "string",
   "Permissions": [ 
      { 
         "Actions": [ "string" ],
         "Principal": "string"
      }
   ],
   "RequestId": "string"
}
```

## Response Elements
<a name="API_DescribeAnalysisPermissions_ResponseElements"></a>

If the action is successful, the service sends back the following HTTP response.

 ** [Status](#API_DescribeAnalysisPermissions_ResponseSyntax) **   <a name="QS-DescribeAnalysisPermissions-response-Status"></a>
The HTTP status of the request.

The following data is returned in JSON format by the service.

 ** [AnalysisArn](#API_DescribeAnalysisPermissions_ResponseSyntax) **   <a name="QS-DescribeAnalysisPermissions-response-AnalysisArn"></a>
The Amazon Resource Name (ARN) of the analysis whose permissions you're describing.  
Type: String

 ** [AnalysisId](#API_DescribeAnalysisPermissions_ResponseSyntax) **   <a name="QS-DescribeAnalysisPermissions-response-AnalysisId"></a>
The ID of the analysis whose permissions you're describing.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 512.  
Pattern: `[\w\-]+` 

 ** [Permissions](#API_DescribeAnalysisPermissions_ResponseSyntax) **   <a name="QS-DescribeAnalysisPermissions-response-Permissions"></a>
A structure that describes the principals and the resource-level permissions on an analysis.  
Type: Array of [ResourcePermission](API_ResourcePermission.md) objects  
Array Members: Maximum number of 100 items.

 ** [RequestId](#API_DescribeAnalysisPermissions_ResponseSyntax) **   <a name="QS-DescribeAnalysisPermissions-response-RequestId"></a>
The AWS request ID for this operation.  
Type: String

## Errors
<a name="API_DescribeAnalysisPermissions_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalFailureException **   
An internal failure occurred.    
 ** RequestId **   
The AWS request ID for this request.
HTTP Status Code: 500

 ** InvalidParameterValueException **   
One or more parameters has a value that isn't valid.    
 ** RequestId **   
The AWS request ID for this request.
HTTP Status Code: 400

 ** ResourceNotFoundException **   
One or more resources can't be found.    
 ** RequestId **   
The AWS request ID for this request.  
 ** ResourceType **   
The resource type for this request.
HTTP Status Code: 404

 ** ThrottlingException **   
Access is throttled.    
 ** RequestId **   
The AWS request ID for this request.
HTTP Status Code: 429

 ** UnsupportedUserEditionException **   
This error indicates that you are calling an operation on an Amazon Quick Suite subscription where the edition doesn't include support for that operation. Amazon Quick Suite currently has Standard Edition and Enterprise Edition. Not every operation and capability is available in every edition.    
 ** RequestId **   
The AWS request ID for this request.
HTTP Status Code: 403

## See Also
<a name="API_DescribeAnalysisPermissions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/quicksight-2018-04-01/DescribeAnalysisPermissions) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/quicksight-2018-04-01/DescribeAnalysisPermissions) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/DescribeAnalysisPermissions) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/quicksight-2018-04-01/DescribeAnalysisPermissions) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/DescribeAnalysisPermissions) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/quicksight-2018-04-01/DescribeAnalysisPermissions) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/quicksight-2018-04-01/DescribeAnalysisPermissions) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/quicksight-2018-04-01/DescribeAnalysisPermissions) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/quicksight-2018-04-01/DescribeAnalysisPermissions) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/DescribeAnalysisPermissions) 