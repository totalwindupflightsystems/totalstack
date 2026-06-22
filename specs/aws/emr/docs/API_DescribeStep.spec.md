---
id: "@specs/aws/emr/docs/API_DescribeStep"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS DescribeStep"
status: active
depends_on:
  - "@specs/aws/emr/meta"
---

# DescribeStep

> **source:** AWS Documentation
> **spec:id:** @specs/aws/emr/docs/API_DescribeStep
> **target_lang:** meta — documentation tier. ALL sections preserved.



# DescribeStep
<a name="API_DescribeStep"></a>

Provides more detail about the cluster step.

## Request Syntax
<a name="API_DescribeStep_RequestSyntax"></a>

```
{
   "ClusterId": "{{string}}",
   "StepId": "{{string}}"
}
```

## Request Parameters
<a name="API_DescribeStep_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [ClusterId](#API_DescribeStep_RequestSyntax) **   <a name="EMR-DescribeStep-request-ClusterId"></a>
The identifier of the cluster with steps to describe.  
Type: String  
Length Constraints: Maximum length of 256.  
Required: Yes

 ** [StepId](#API_DescribeStep_RequestSyntax) **   <a name="EMR-DescribeStep-request-StepId"></a>
The identifier of the step to describe.  
Type: String  
Required: Yes

## Response Syntax
<a name="API_DescribeStep_ResponseSyntax"></a>

```
{
   "Step": { 
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
      "ExecutionRoleArn": "string",
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
}
```

## Response Elements
<a name="API_DescribeStep_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Step](#API_DescribeStep_ResponseSyntax) **   <a name="EMR-DescribeStep-response-Step"></a>
The step details for the requested step identifier.  
Type: [Step](API_Step.md) object

## Errors
<a name="API_DescribeStep_Errors"></a>

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
<a name="API_DescribeStep_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/elasticmapreduce-2009-03-31/DescribeStep) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/elasticmapreduce-2009-03-31/DescribeStep) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/elasticmapreduce-2009-03-31/DescribeStep) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/elasticmapreduce-2009-03-31/DescribeStep) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/elasticmapreduce-2009-03-31/DescribeStep) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/elasticmapreduce-2009-03-31/DescribeStep) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/elasticmapreduce-2009-03-31/DescribeStep) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/elasticmapreduce-2009-03-31/DescribeStep) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/elasticmapreduce-2009-03-31/DescribeStep) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/elasticmapreduce-2009-03-31/DescribeStep) 