---
id: "@specs/aws/emr/docs/API_PutAutoTerminationPolicy"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS PutAutoTerminationPolicy"
status: active
depends_on:
  - "@specs/aws/emr/meta"
---

# PutAutoTerminationPolicy

> **source:** AWS Documentation
> **spec:id:** @specs/aws/emr/docs/API_PutAutoTerminationPolicy
> **target_lang:** meta — documentation tier. ALL sections preserved.



# PutAutoTerminationPolicy
<a name="API_PutAutoTerminationPolicy"></a>

**Note**  
Auto-termination is supported in Amazon EMR releases 5.30.0 and 6.1.0 and later. For more information, see [Using an auto-termination policy](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-auto-termination-policy.html).

Creates or updates an auto-termination policy for an Amazon EMR cluster. An auto-termination policy defines the amount of idle time in seconds after which a cluster automatically terminates. For alternative cluster termination options, see [Control cluster termination](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-plan-termination.html).

## Request Syntax
<a name="API_PutAutoTerminationPolicy_RequestSyntax"></a>

```
{
   "AutoTerminationPolicy": { 
      "IdleTimeout": {{number}}
   },
   "ClusterId": "{{string}}"
}
```

## Request Parameters
<a name="API_PutAutoTerminationPolicy_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [AutoTerminationPolicy](#API_PutAutoTerminationPolicy_RequestSyntax) **   <a name="EMR-PutAutoTerminationPolicy-request-AutoTerminationPolicy"></a>
Specifies the auto-termination policy to attach to the cluster.  
Type: [AutoTerminationPolicy](API_AutoTerminationPolicy.md) object  
Required: No

 ** [ClusterId](#API_PutAutoTerminationPolicy_RequestSyntax) **   <a name="EMR-PutAutoTerminationPolicy-request-ClusterId"></a>
Specifies the ID of the Amazon EMR cluster to which the auto-termination policy will be attached.  
Type: String  
Length Constraints: Maximum length of 256.  
Required: Yes

## Response Elements
<a name="API_PutAutoTerminationPolicy_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_PutAutoTerminationPolicy_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## See Also
<a name="API_PutAutoTerminationPolicy_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/elasticmapreduce-2009-03-31/PutAutoTerminationPolicy) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/elasticmapreduce-2009-03-31/PutAutoTerminationPolicy) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/elasticmapreduce-2009-03-31/PutAutoTerminationPolicy) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/elasticmapreduce-2009-03-31/PutAutoTerminationPolicy) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/elasticmapreduce-2009-03-31/PutAutoTerminationPolicy) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/elasticmapreduce-2009-03-31/PutAutoTerminationPolicy) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/elasticmapreduce-2009-03-31/PutAutoTerminationPolicy) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/elasticmapreduce-2009-03-31/PutAutoTerminationPolicy) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/elasticmapreduce-2009-03-31/PutAutoTerminationPolicy) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/elasticmapreduce-2009-03-31/PutAutoTerminationPolicy) 