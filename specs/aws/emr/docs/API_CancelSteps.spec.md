---
id: "@specs/aws/emr/docs/API_CancelSteps"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS CancelSteps"
status: active
depends_on:
  - "@specs/aws/emr/meta"
---

# CancelSteps

> **source:** AWS Documentation
> **spec:id:** @specs/aws/emr/docs/API_CancelSteps
> **target_lang:** meta — documentation tier. ALL sections preserved.



# CancelSteps
<a name="API_CancelSteps"></a>

Cancels a pending step or steps in a running cluster. Available only in Amazon EMR versions 4.8.0 and later, excluding version 5.0.0. A maximum of 256 steps are allowed in each CancelSteps request. CancelSteps is idempotent but asynchronous; it does not guarantee that a step will be canceled, even if the request is successfully submitted. When you use Amazon EMR releases 5.28.0 and later, you can cancel steps that are in a `PENDING` or `RUNNING` state. In earlier versions of Amazon EMR, you can only cancel steps that are in a `PENDING` state. 

## Request Syntax
<a name="API_CancelSteps_RequestSyntax"></a>

```
{
   "ClusterId": "{{string}}",
   "StepCancellationOption": "{{string}}",
   "StepIds": [ "{{string}}" ]
}
```

## Request Parameters
<a name="API_CancelSteps_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [ClusterId](#API_CancelSteps_RequestSyntax) **   <a name="EMR-CancelSteps-request-ClusterId"></a>
The `ClusterID` for the specified steps that will be canceled. Use [RunJobFlow](API_RunJobFlow.md) and [ListClusters](API_ListClusters.md) to get ClusterIDs.   
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 256.  
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`   
Required: Yes

 ** [StepCancellationOption](#API_CancelSteps_RequestSyntax) **   <a name="EMR-CancelSteps-request-StepCancellationOption"></a>
The option to choose to cancel `RUNNING` steps. By default, the value is `SEND_INTERRUPT`.  
Type: String  
Valid Values: `SEND_INTERRUPT | TERMINATE_PROCESS`   
Required: No

 ** [StepIds](#API_CancelSteps_RequestSyntax) **   <a name="EMR-CancelSteps-request-StepIds"></a>
The list of `StepIDs` to cancel. Use [ListSteps](API_ListSteps.md) to get steps and their states for the specified cluster.  
Type: Array of strings  
Length Constraints: Minimum length of 0. Maximum length of 256.  
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`   
Required: Yes

## Response Syntax
<a name="API_CancelSteps_ResponseSyntax"></a>

```
{
   "CancelStepsInfoList": [ 
      { 
         "Reason": "string",
         "Status": "string",
         "StepId": "string"
      }
   ]
}
```

## Response Elements
<a name="API_CancelSteps_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [CancelStepsInfoList](#API_CancelSteps_ResponseSyntax) **   <a name="EMR-CancelSteps-response-CancelStepsInfoList"></a>
A list of [CancelStepsInfo](API_CancelStepsInfo.md), which shows the status of specified cancel requests for each `StepID` specified.  
Type: Array of [CancelStepsInfo](API_CancelStepsInfo.md) objects

## Errors
<a name="API_CancelSteps_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalServerError **   
Indicates that an error occurred while processing the request and that the request was not completed.  
HTTP Status Code: 400

 ** InvalidRequestException **   
This exception occurs when there is something wrong with user input.    
 ** ErrorCode **   
The error code associated with the exception.  
 ** Message **   
The message associated with the exception.
HTTP Status Code: 400

## Examples
<a name="API_CancelSteps_Examples"></a>

### Example
<a name="API_CancelSteps_Example_1"></a>

This example illustrates one usage of CancelSteps.

#### Sample Request
<a name="API_CancelSteps_Example_1_Request"></a>

```
POST / HTTP/1.1
Content-Type: application/x-amz-json-1.1
X-Amz-Target: ElasticMapReduce.CancelSteps
User-Agent: aws-sdk-ruby/1.9.2 ruby/1.9.3 i386-mingw32
Host: us-east-1.elasticmapreduce.amazonaws.com
X-Amz-Date: 20160719T224800Z
X-Amz-Content-Sha256: 9e5ad0a93c22224947ce98eea94f766103d91b28fa82eb60d0cb8b6f9555a6b2
Authorization: AWS4-HMAC-SHA256 Credential=AKIAIOSFODNN7EXAMPLE/20160719/us-east-1/elasticmapreduce/aws4_request, SignedHeaders=content-length;content-type;host;user-agent;x-amz-content-sha256;x-amz-date;x-amz-target, Signature=2a2393390760ae85eb74ee3a539e1d758bfdd8815a1a6d6f14d4a2fbcfdcd5b7
Accept: */*

{
  "ClusterId": "j-2G7RS6DJZE39D",
  "StepIds":
  [
    "s-11B5G7VIKHCZQ", "s-23PUT0NR3XF6O", "s-2NUYMUZ3ADACC", "s-10O5XO5JUY9OE", "s-CS88G2XK4N7X", "s-2M366D3KU4OTZ"
  ]
}
```

#### Sample Response
<a name="API_CancelSteps_Example_1_Response"></a>

```
HTTP/1.1 200 OK
x-amzn-RequestId: 84931a23-4e03-11e6-b2bd-0db72d19890a
Content-Type: application/x-amz-json-1.1
Date: Tue, 19 Jul 2016 15:31:01 GMT

{
  "CancelStepsInfoList":
  [
    {"Reason": "This step cannot be cancelled.",
     "Status": "FAILED",
     "StepId": "s-11B5G7VIKHCZQ"},
    {"Reason": "Cannot cancel the step. It is already COMPLETED.",
     "Status": "FAILED",
     "StepId": "s-23PUT0NR3XF6O"},
    {"Reason": "Cannot cancel the step. It is already CANCELLED.",
     "Status": "FAILED",
     "StepId": "s-2NUYMUZ3ADACC"},
    {"Reason": "Cannot cancel the step. It is already RUNNING.",
     "Status": "FAILED",
     "StepId": "s-10O5XO5JUY9OE"},
    {"Reason": "Cannot cancel the step. It is already FAILED.",
     "Status": "FAILED",
     "StepId": "s-CS88G2XK4N7X"},
    {"Reason": "",
     "Status": "SUBMITTED",
     "StepId": "s-2M366D3KU4OTZ"}
  ]
}
```

## See Also
<a name="API_CancelSteps_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/elasticmapreduce-2009-03-31/CancelSteps) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/elasticmapreduce-2009-03-31/CancelSteps) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/elasticmapreduce-2009-03-31/CancelSteps) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/elasticmapreduce-2009-03-31/CancelSteps) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/elasticmapreduce-2009-03-31/CancelSteps) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/elasticmapreduce-2009-03-31/CancelSteps) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/elasticmapreduce-2009-03-31/CancelSteps) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/elasticmapreduce-2009-03-31/CancelSteps) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/elasticmapreduce-2009-03-31/CancelSteps) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/elasticmapreduce-2009-03-31/CancelSteps) 