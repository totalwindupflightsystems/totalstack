---
id: "@specs/aws/emr/docs/API_SetKeepJobFlowAliveWhenNoSteps"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS SetKeepJobFlowAliveWhenNoSteps"
status: active
depends_on:
  - "@specs/aws/emr/meta"
---

# SetKeepJobFlowAliveWhenNoSteps

> **source:** AWS Documentation
> **spec:id:** @specs/aws/emr/docs/API_SetKeepJobFlowAliveWhenNoSteps
> **target_lang:** meta — documentation tier. ALL sections preserved.



# SetKeepJobFlowAliveWhenNoSteps
<a name="API_SetKeepJobFlowAliveWhenNoSteps"></a>

You can use the `SetKeepJobFlowAliveWhenNoSteps` to configure a cluster (job flow) to terminate after the step execution, i.e., all your steps are executed. If you want a transient cluster that shuts down after the last of the current executing steps are completed, you can configure `SetKeepJobFlowAliveWhenNoSteps` to false. If you want a long running cluster, configure `SetKeepJobFlowAliveWhenNoSteps` to true.

For more information, see [Managing Cluster Termination](https://docs.aws.amazon.com/emr/latest/ManagementGuide/UsingEMR_TerminationProtection.html) in the *Amazon EMR Management Guide*.

## Request Syntax
<a name="API_SetKeepJobFlowAliveWhenNoSteps_RequestSyntax"></a>

```
{
   "JobFlowIds": [ "{{string}}" ],
   "KeepJobFlowAliveWhenNoSteps": {{boolean}}
}
```

## Request Parameters
<a name="API_SetKeepJobFlowAliveWhenNoSteps_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [JobFlowIds](#API_SetKeepJobFlowAliveWhenNoSteps_RequestSyntax) **   <a name="EMR-SetKeepJobFlowAliveWhenNoSteps-request-JobFlowIds"></a>
A list of strings that uniquely identify the clusters to protect. This identifier is returned by [RunJobFlow](https://docs.aws.amazon.com/emr/latest/APIReference/API_RunJobFlow.html) and can also be obtained from [DescribeJobFlows](https://docs.aws.amazon.com/emr/latest/APIReference/API_DescribeJobFlows.html).  
Type: Array of strings  
Length Constraints: Minimum length of 0. Maximum length of 10280.  
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`   
Required: Yes

 ** [KeepJobFlowAliveWhenNoSteps](#API_SetKeepJobFlowAliveWhenNoSteps_RequestSyntax) **   <a name="EMR-SetKeepJobFlowAliveWhenNoSteps-request-KeepJobFlowAliveWhenNoSteps"></a>
A Boolean that indicates whether to terminate the cluster after all steps are executed.  
Type: Boolean  
Required: Yes

## Response Elements
<a name="API_SetKeepJobFlowAliveWhenNoSteps_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_SetKeepJobFlowAliveWhenNoSteps_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalServerError **   
Indicates that an error occurred while processing the request and that the request was not completed.  
HTTP Status Code: 400

## See Also
<a name="API_SetKeepJobFlowAliveWhenNoSteps_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/elasticmapreduce-2009-03-31/SetKeepJobFlowAliveWhenNoSteps) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/elasticmapreduce-2009-03-31/SetKeepJobFlowAliveWhenNoSteps) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/elasticmapreduce-2009-03-31/SetKeepJobFlowAliveWhenNoSteps) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/elasticmapreduce-2009-03-31/SetKeepJobFlowAliveWhenNoSteps) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/elasticmapreduce-2009-03-31/SetKeepJobFlowAliveWhenNoSteps) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/elasticmapreduce-2009-03-31/SetKeepJobFlowAliveWhenNoSteps) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/elasticmapreduce-2009-03-31/SetKeepJobFlowAliveWhenNoSteps) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/elasticmapreduce-2009-03-31/SetKeepJobFlowAliveWhenNoSteps) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/elasticmapreduce-2009-03-31/SetKeepJobFlowAliveWhenNoSteps) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/elasticmapreduce-2009-03-31/SetKeepJobFlowAliveWhenNoSteps) 