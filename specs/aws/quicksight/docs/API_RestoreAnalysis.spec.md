---
id: "@specs/aws/quicksight/docs/API_RestoreAnalysis"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS RestoreAnalysis"
status: active
depends_on:
  - "@specs/aws/quicksight/meta"
---

# RestoreAnalysis

> **source:** AWS Documentation
> **spec:id:** @specs/aws/quicksight/docs/API_RestoreAnalysis
> **target_lang:** meta — documentation tier. ALL sections preserved.



# RestoreAnalysis
<a name="API_RestoreAnalysis"></a>

Restores an analysis.

## Request Syntax
<a name="API_RestoreAnalysis_RequestSyntax"></a>

```
POST /accounts/{{AwsAccountId}}/restore/analyses/{{AnalysisId}}?restore-to-folders={{RestoreToFolders}} HTTP/1.1
```

## URI Request Parameters
<a name="API_RestoreAnalysis_RequestParameters"></a>

The request uses the following URI parameters.

 ** [AnalysisId](#API_RestoreAnalysis_RequestSyntax) **   <a name="QS-RestoreAnalysis-request-uri-AnalysisId"></a>
The ID of the analysis that you're restoring.  
Length Constraints: Minimum length of 1. Maximum length of 512.  
Pattern: `[\w\-]+`   
Required: Yes

 ** [AwsAccountId](#API_RestoreAnalysis_RequestSyntax) **   <a name="QS-RestoreAnalysis-request-uri-AwsAccountId"></a>
The ID of the AWS account that contains the analysis.  
Length Constraints: Fixed length of 12.  
Pattern: `^[0-9]{12}$`   
Required: Yes

 ** [RestoreToFolders](#API_RestoreAnalysis_RequestSyntax) **   <a name="QS-RestoreAnalysis-request-uri-RestoreToFolders"></a>
A boolean value that determines if the analysis will be restored to folders that it previously resided in. A `True` value restores analysis back to all folders that it previously resided in. A `False` value restores the analysis but does not restore the analysis back to all previously resided folders. Restoring a restricted analysis requires this parameter to be set to `True`.

## Request Body
<a name="API_RestoreAnalysis_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_RestoreAnalysis_ResponseSyntax"></a>

```
HTTP/1.1 {{Status}}
Content-type: application/json

{
   "AnalysisId": "string",
   "Arn": "string",
   "RequestId": "string",
   "RestorationFailedFolderArns": [ "string" ]
}
```

## Response Elements
<a name="API_RestoreAnalysis_ResponseElements"></a>

If the action is successful, the service sends back the following HTTP response.

 ** [Status](#API_RestoreAnalysis_ResponseSyntax) **   <a name="QS-RestoreAnalysis-response-Status"></a>
The HTTP status of the request.

The following data is returned in JSON format by the service.

 ** [AnalysisId](#API_RestoreAnalysis_ResponseSyntax) **   <a name="QS-RestoreAnalysis-response-AnalysisId"></a>
The ID of the analysis that you're restoring.   
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 512.  
Pattern: `[\w\-]+` 

 ** [Arn](#API_RestoreAnalysis_ResponseSyntax) **   <a name="QS-RestoreAnalysis-response-Arn"></a>
The Amazon Resource Name (ARN) of the analysis that you're restoring.  
Type: String

 ** [RequestId](#API_RestoreAnalysis_ResponseSyntax) **   <a name="QS-RestoreAnalysis-response-RequestId"></a>
The AWS request ID for this operation.  
Type: String

 ** [RestorationFailedFolderArns](#API_RestoreAnalysis_ResponseSyntax) **   <a name="QS-RestoreAnalysis-response-RestorationFailedFolderArns"></a>
A list of folder arns thatthe analysis failed to be restored to.  
Type: Array of strings  
Array Members: Maximum number of 1 item.

## Errors
<a name="API_RestoreAnalysis_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ConflictException **   
Updating or deleting a resource can cause an inconsistent state.    
 ** RequestId **   
The AWS request ID for this request.
HTTP Status Code: 409

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

 ** LimitExceededException **   
A limit is exceeded.    
 ** RequestId **   
The AWS request ID for this request.  
 ** ResourceType **   
Limit exceeded.
HTTP Status Code: 409

 ** PreconditionNotMetException **   
One or more preconditions aren't met.    
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
<a name="API_RestoreAnalysis_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/quicksight-2018-04-01/RestoreAnalysis) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/quicksight-2018-04-01/RestoreAnalysis) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/RestoreAnalysis) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/quicksight-2018-04-01/RestoreAnalysis) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/RestoreAnalysis) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/quicksight-2018-04-01/RestoreAnalysis) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/quicksight-2018-04-01/RestoreAnalysis) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/quicksight-2018-04-01/RestoreAnalysis) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/quicksight-2018-04-01/RestoreAnalysis) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/RestoreAnalysis) 