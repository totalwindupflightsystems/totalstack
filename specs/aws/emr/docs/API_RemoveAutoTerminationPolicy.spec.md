---
id: "@specs/aws/emr/docs/API_RemoveAutoTerminationPolicy"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS RemoveAutoTerminationPolicy"
status: active
depends_on:
  - "@specs/aws/emr/meta"
---

# RemoveAutoTerminationPolicy

> **source:** AWS Documentation
> **spec:id:** @specs/aws/emr/docs/API_RemoveAutoTerminationPolicy
> **target_lang:** meta — documentation tier. ALL sections preserved.



# RemoveAutoTerminationPolicy
<a name="API_RemoveAutoTerminationPolicy"></a>

Removes an auto-termination policy from an Amazon EMR cluster.

## Request Syntax
<a name="API_RemoveAutoTerminationPolicy_RequestSyntax"></a>

```
{
   "ClusterId": "{{string}}"
}
```

## Request Parameters
<a name="API_RemoveAutoTerminationPolicy_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [ClusterId](#API_RemoveAutoTerminationPolicy_RequestSyntax) **   <a name="EMR-RemoveAutoTerminationPolicy-request-ClusterId"></a>
Specifies the ID of the Amazon EMR cluster from which the auto-termination policy will be removed.  
Type: String  
Length Constraints: Maximum length of 256.  
Required: Yes

## Response Elements
<a name="API_RemoveAutoTerminationPolicy_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_RemoveAutoTerminationPolicy_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## See Also
<a name="API_RemoveAutoTerminationPolicy_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/elasticmapreduce-2009-03-31/RemoveAutoTerminationPolicy) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/elasticmapreduce-2009-03-31/RemoveAutoTerminationPolicy) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/elasticmapreduce-2009-03-31/RemoveAutoTerminationPolicy) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/elasticmapreduce-2009-03-31/RemoveAutoTerminationPolicy) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/elasticmapreduce-2009-03-31/RemoveAutoTerminationPolicy) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/elasticmapreduce-2009-03-31/RemoveAutoTerminationPolicy) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/elasticmapreduce-2009-03-31/RemoveAutoTerminationPolicy) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/elasticmapreduce-2009-03-31/RemoveAutoTerminationPolicy) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/elasticmapreduce-2009-03-31/RemoveAutoTerminationPolicy) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/elasticmapreduce-2009-03-31/RemoveAutoTerminationPolicy) 