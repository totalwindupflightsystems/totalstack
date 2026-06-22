---
id: "@specs/aws/emr/docs/API_RemoveManagedScalingPolicy"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS RemoveManagedScalingPolicy"
status: active
depends_on:
  - "@specs/aws/emr/meta"
---

# RemoveManagedScalingPolicy

> **source:** AWS Documentation
> **spec:id:** @specs/aws/emr/docs/API_RemoveManagedScalingPolicy
> **target_lang:** meta — documentation tier. ALL sections preserved.



# RemoveManagedScalingPolicy
<a name="API_RemoveManagedScalingPolicy"></a>

 Removes a managed scaling policy from a specified Amazon EMR cluster. 

## Request Syntax
<a name="API_RemoveManagedScalingPolicy_RequestSyntax"></a>

```
{
   "ClusterId": "{{string}}"
}
```

## Request Parameters
<a name="API_RemoveManagedScalingPolicy_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [ClusterId](#API_RemoveManagedScalingPolicy_RequestSyntax) **   <a name="EMR-RemoveManagedScalingPolicy-request-ClusterId"></a>
 Specifies the ID of the cluster from which the managed scaling policy will be removed.   
Type: String  
Length Constraints: Maximum length of 256.  
Required: Yes

## Response Elements
<a name="API_RemoveManagedScalingPolicy_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_RemoveManagedScalingPolicy_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## See Also
<a name="API_RemoveManagedScalingPolicy_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/elasticmapreduce-2009-03-31/RemoveManagedScalingPolicy) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/elasticmapreduce-2009-03-31/RemoveManagedScalingPolicy) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/elasticmapreduce-2009-03-31/RemoveManagedScalingPolicy) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/elasticmapreduce-2009-03-31/RemoveManagedScalingPolicy) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/elasticmapreduce-2009-03-31/RemoveManagedScalingPolicy) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/elasticmapreduce-2009-03-31/RemoveManagedScalingPolicy) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/elasticmapreduce-2009-03-31/RemoveManagedScalingPolicy) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/elasticmapreduce-2009-03-31/RemoveManagedScalingPolicy) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/elasticmapreduce-2009-03-31/RemoveManagedScalingPolicy) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/elasticmapreduce-2009-03-31/RemoveManagedScalingPolicy) 