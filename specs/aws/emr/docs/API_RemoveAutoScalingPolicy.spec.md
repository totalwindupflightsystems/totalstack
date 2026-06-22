---
id: "@specs/aws/emr/docs/API_RemoveAutoScalingPolicy"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS RemoveAutoScalingPolicy"
status: active
depends_on:
  - "@specs/aws/emr/meta"
---

# RemoveAutoScalingPolicy

> **source:** AWS Documentation
> **spec:id:** @specs/aws/emr/docs/API_RemoveAutoScalingPolicy
> **target_lang:** meta — documentation tier. ALL sections preserved.



# RemoveAutoScalingPolicy
<a name="API_RemoveAutoScalingPolicy"></a>

Removes an automatic scaling policy from a specified instance group within an Amazon EMR cluster.

## Request Syntax
<a name="API_RemoveAutoScalingPolicy_RequestSyntax"></a>

```
{
   "ClusterId": "{{string}}",
   "InstanceGroupId": "{{string}}"
}
```

## Request Parameters
<a name="API_RemoveAutoScalingPolicy_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [ClusterId](#API_RemoveAutoScalingPolicy_RequestSyntax) **   <a name="EMR-RemoveAutoScalingPolicy-request-ClusterId"></a>
Specifies the ID of a cluster. The instance group to which the automatic scaling policy is applied is within this cluster.  
Type: String  
Length Constraints: Maximum length of 256.  
Required: Yes

 ** [InstanceGroupId](#API_RemoveAutoScalingPolicy_RequestSyntax) **   <a name="EMR-RemoveAutoScalingPolicy-request-InstanceGroupId"></a>
Specifies the ID of the instance group to which the scaling policy is applied.  
Type: String  
Length Constraints: Maximum length of 256.  
Required: Yes

## Response Elements
<a name="API_RemoveAutoScalingPolicy_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_RemoveAutoScalingPolicy_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## See Also
<a name="API_RemoveAutoScalingPolicy_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/elasticmapreduce-2009-03-31/RemoveAutoScalingPolicy) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/elasticmapreduce-2009-03-31/RemoveAutoScalingPolicy) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/elasticmapreduce-2009-03-31/RemoveAutoScalingPolicy) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/elasticmapreduce-2009-03-31/RemoveAutoScalingPolicy) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/elasticmapreduce-2009-03-31/RemoveAutoScalingPolicy) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/elasticmapreduce-2009-03-31/RemoveAutoScalingPolicy) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/elasticmapreduce-2009-03-31/RemoveAutoScalingPolicy) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/elasticmapreduce-2009-03-31/RemoveAutoScalingPolicy) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/elasticmapreduce-2009-03-31/RemoveAutoScalingPolicy) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/elasticmapreduce-2009-03-31/RemoveAutoScalingPolicy) 