---
id: "@specs/aws/emr/docs/API_ListSteps"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS ListSteps"
status: active
depends_on:
  - "@specs/aws/emr/meta"
---

# ListSteps

> **source:** AWS Documentation
> **spec:id:** @specs/aws/emr/docs/API_ListSteps
> **target_lang:** meta — documentation tier. ALL sections preserved.



# ListSteps
<a name="API_ListSteps"></a>

Provides a list of steps for the cluster in reverse order unless you specify `stepIds` with the request or filter by `StepStates`. You can specify a maximum of 10 `stepIDs`. The AWS CLI automatically paginates results to return a list greater than 50 steps. To return more than 50 steps using the AWS CLI, specify a `Marker`, which is a pagination token that indicates the next set of steps to retrieve.

## Request Syntax
<a name="API_ListSteps_RequestSyntax"></a>

```
{
   "ClusterId": "{{string}}",
   "Marker": "{{string}}",
   "StepIds": [ "{{string}}" ],
   "StepStates": [ "{{string}}" ]
}
```

## Request Parameters
<a name="API_ListSteps_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [ClusterId](#API_ListSteps_RequestSyntax) **   <a name="EMR-ListSteps-request-ClusterId"></a>
The identifier of the cluster for which to list the steps.  
Type: String  
Length Constraints: Maximum length of 256.  
Required: Yes

 ** [Marker](#API_ListSteps_RequestSyntax) **   <a name="EMR-ListSteps-request-Marker"></a>
The maximum number of steps that a single `ListSteps` action returns is 50. To return a longer list of steps, use multiple `ListSteps` actions along with the `Marker` parameter, which is a pagination token that indicates the next set of results to retrieve.  
Type: String  
Required: No

 ** [StepIds](#API_ListSteps_RequestSyntax) **   <a name="EMR-ListSteps-request-StepIds"></a>
The filter to limit the step list based on the identifier of the steps. You can specify a maximum of ten Step IDs. The character constraint applies to the overall length of the array.  
Type: Array of strings  
Length Constraints: Minimum length of 0. Maximum length of 10280.  
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`   
Required: No

 ** [StepStates](#API_ListSteps_RequestSyntax) **   <a name="EMR-ListSteps-request-StepStates"></a>
The filter to limit the step list based on certain states.  
Type: Array of strings  
Valid Values: `PENDING | CANCEL_PENDING | RUNNING | COMPLETED | CANCELLED | FAILED | INTERRUPTED`   
Required: No

## Response Syntax
<a name="API_ListSteps_ResponseSyntax"></a>

```
{
   "Marker": "string",
   "Steps": [ 
      { 
         "ActionOnFailure": "string",
         "Config": { 
            "Args": [ "string" ],
            "Jar": "string",
            "MainClass": "string",
            "Properties": { 
               "string" : "string" 
            }
         },
         "EncryptionKeyArn": "string",
         "Id": "string",
         "LogUri": "string",
         "Name": "string",
         "Status": { 
            "FailureDetails": { 
               "LogFile": "string",
               "Message": "string",
               "Reason": "string"
            },
            "State": "string",
            "StateChangeReason": { 
               "Code": "string",
               "Message": "string"
            },
            "Timeline": { 
               "CreationDateTime": number,
               "EndDateTime": number,
               "StartDateTime": number
            }
         }
      }
   ]
}
```

## Response Elements
<a name="API_ListSteps_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Marker](#API_ListSteps_ResponseSyntax) **   <a name="EMR-ListSteps-response-Marker"></a>
The maximum number of steps that a single `ListSteps` action returns is 50. To return a longer list of steps, use multiple `ListSteps` actions along with the `Marker` parameter, which is a pagination token that indicates the next set of results to retrieve.  
Type: String

 ** [Steps](#API_ListSteps_ResponseSyntax) **   <a name="EMR-ListSteps-response-Steps"></a>
The filtered list of steps for the cluster.  
Type: Array of [StepSummary](API_StepSummary.md) objects

## Errors
<a name="API_ListSteps_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalServerException **   
This exception occurs when there is an internal failure in the Amazon EMR service.    
 ** Message **   
The message associated with the exception.
HTTP Status Code: 500

 ** InvalidRequestException **   
This exception occurs when there is something wrong with user input.    
 ** ErrorCode **   
The error code associated with the exception.  
 ** Message **   
The message associated with the exception.
HTTP Status Code: 400

## See Also
<a name="API_ListSteps_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/elasticmapreduce-2009-03-31/ListSteps) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/elasticmapreduce-2009-03-31/ListSteps) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/elasticmapreduce-2009-03-31/ListSteps) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/elasticmapreduce-2009-03-31/ListSteps) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/elasticmapreduce-2009-03-31/ListSteps) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/elasticmapreduce-2009-03-31/ListSteps) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/elasticmapreduce-2009-03-31/ListSteps) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/elasticmapreduce-2009-03-31/ListSteps) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/elasticmapreduce-2009-03-31/ListSteps) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/elasticmapreduce-2009-03-31/ListSteps) 