---
id: "@specs/aws/emr/docs/API_PutManagedScalingPolicy"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS PutManagedScalingPolicy"
status: active
depends_on:
  - "@specs/aws/emr/meta"
---

# PutManagedScalingPolicy

> **source:** AWS Documentation
> **spec:id:** @specs/aws/emr/docs/API_PutManagedScalingPolicy
> **target_lang:** meta — documentation tier. ALL sections preserved.



# PutManagedScalingPolicy
<a name="API_PutManagedScalingPolicy"></a>

Creates or updates a managed scaling policy for an Amazon EMR cluster. The managed scaling policy defines the limits for resources, such as Amazon EC2 instances that can be added or terminated from a cluster. The policy only applies to the core and task nodes. The master node cannot be scaled after initial configuration. 

## Request Syntax
<a name="API_PutManagedScalingPolicy_RequestSyntax"></a>

```
{
   "ClusterId": "{{string}}",
   "ManagedScalingPolicy": { 
      "ComputeLimits": { 
         "MaximumCapacityUnits": {{number}},
         "MaximumCoreCapacityUnits": {{number}},
         "MaximumOnDemandCapacityUnits": {{number}},
         "MinimumCapacityUnits": {{number}},
         "UnitType": "{{string}}"
      },
      "ScalingStrategy": "{{string}}",
      "UtilizationPerformanceIndex": {{number}}
   }
}
```

## Request Parameters
<a name="API_PutManagedScalingPolicy_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [ClusterId](#API_PutManagedScalingPolicy_RequestSyntax) **   <a name="EMR-PutManagedScalingPolicy-request-ClusterId"></a>
Specifies the ID of an Amazon EMR cluster where the managed scaling policy is attached.   
Type: String  
Length Constraints: Maximum length of 256.  
Required: Yes

 ** [ManagedScalingPolicy](#API_PutManagedScalingPolicy_RequestSyntax) **   <a name="EMR-PutManagedScalingPolicy-request-ManagedScalingPolicy"></a>
Specifies the constraints for the managed scaling policy.   
Type: [ManagedScalingPolicy](API_ManagedScalingPolicy.md) object  
Required: Yes

## Response Elements
<a name="API_PutManagedScalingPolicy_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_PutManagedScalingPolicy_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## See Also
<a name="API_PutManagedScalingPolicy_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/elasticmapreduce-2009-03-31/PutManagedScalingPolicy) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/elasticmapreduce-2009-03-31/PutManagedScalingPolicy) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/elasticmapreduce-2009-03-31/PutManagedScalingPolicy) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/elasticmapreduce-2009-03-31/PutManagedScalingPolicy) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/elasticmapreduce-2009-03-31/PutManagedScalingPolicy) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/elasticmapreduce-2009-03-31/PutManagedScalingPolicy) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/elasticmapreduce-2009-03-31/PutManagedScalingPolicy) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/elasticmapreduce-2009-03-31/PutManagedScalingPolicy) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/elasticmapreduce-2009-03-31/PutManagedScalingPolicy) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/elasticmapreduce-2009-03-31/PutManagedScalingPolicy) 