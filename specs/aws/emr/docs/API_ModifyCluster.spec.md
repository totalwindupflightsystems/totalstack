---
id: "@specs/aws/emr/docs/API_ModifyCluster"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS ModifyCluster"
status: active
depends_on:
  - "@specs/aws/emr/meta"
---

# ModifyCluster

> **source:** AWS Documentation
> **spec:id:** @specs/aws/emr/docs/API_ModifyCluster
> **target_lang:** meta — documentation tier. ALL sections preserved.



# ModifyCluster
<a name="API_ModifyCluster"></a>

Modifies the number of steps that can be executed concurrently for the cluster specified using ClusterID.

## Request Syntax
<a name="API_ModifyCluster_RequestSyntax"></a>

```
{
   "ClusterId": "{{string}}",
   "ExtendedSupport": {{boolean}},
   "StepConcurrencyLevel": {{number}}
}
```

## Request Parameters
<a name="API_ModifyCluster_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [ClusterId](#API_ModifyCluster_RequestSyntax) **   <a name="EMR-ModifyCluster-request-ClusterId"></a>
The unique identifier of the cluster.  
Type: String  
Required: Yes

 ** [ExtendedSupport](#API_ModifyCluster_RequestSyntax) **   <a name="EMR-ModifyCluster-request-ExtendedSupport"></a>
Reserved.  
Type: Boolean  
Required: No

 ** [StepConcurrencyLevel](#API_ModifyCluster_RequestSyntax) **   <a name="EMR-ModifyCluster-request-StepConcurrencyLevel"></a>
The number of steps that can be executed concurrently. You can specify a minimum of 1 step and a maximum of 256 steps. We recommend that you do not change this parameter while steps are running or the `ActionOnFailure` setting may not behave as expected. For more information see [Step:ActionOnFailure](API_Step.md#EMR-Type-Step-ActionOnFailure).  
Type: Integer  
Required: No

## Response Syntax
<a name="API_ModifyCluster_ResponseSyntax"></a>

```
{
   "ExtendedSupport": boolean,
   "StepConcurrencyLevel": number
}
```

## Response Elements
<a name="API_ModifyCluster_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ExtendedSupport](#API_ModifyCluster_ResponseSyntax) **   <a name="EMR-ModifyCluster-response-ExtendedSupport"></a>
Reserved.  
Type: Boolean

 ** [StepConcurrencyLevel](#API_ModifyCluster_ResponseSyntax) **   <a name="EMR-ModifyCluster-response-StepConcurrencyLevel"></a>
The number of steps that can be executed concurrently.  
Type: Integer

## Errors
<a name="API_ModifyCluster_Errors"></a>

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

## See Also
<a name="API_ModifyCluster_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/elasticmapreduce-2009-03-31/ModifyCluster) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/elasticmapreduce-2009-03-31/ModifyCluster) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/elasticmapreduce-2009-03-31/ModifyCluster) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/elasticmapreduce-2009-03-31/ModifyCluster) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/elasticmapreduce-2009-03-31/ModifyCluster) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/elasticmapreduce-2009-03-31/ModifyCluster) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/elasticmapreduce-2009-03-31/ModifyCluster) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/elasticmapreduce-2009-03-31/ModifyCluster) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/elasticmapreduce-2009-03-31/ModifyCluster) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/elasticmapreduce-2009-03-31/ModifyCluster) 