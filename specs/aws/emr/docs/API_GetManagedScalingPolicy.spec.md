---
id: "@specs/aws/emr/docs/API_GetManagedScalingPolicy"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS GetManagedScalingPolicy"
status: active
depends_on:
  - "@specs/aws/emr/meta"
---

# GetManagedScalingPolicy

> **source:** AWS Documentation
> **spec:id:** @specs/aws/emr/docs/API_GetManagedScalingPolicy
> **target_lang:** meta — documentation tier. ALL sections preserved.



# GetManagedScalingPolicy
<a name="API_GetManagedScalingPolicy"></a>

Fetches the attached managed scaling policy for an Amazon EMR cluster. 

## Request Syntax
<a name="API_GetManagedScalingPolicy_RequestSyntax"></a>

```
{
   "ClusterId": "{{string}}"
}
```

## Request Parameters
<a name="API_GetManagedScalingPolicy_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [ClusterId](#API_GetManagedScalingPolicy_RequestSyntax) **   <a name="EMR-GetManagedScalingPolicy-request-ClusterId"></a>
Specifies the ID of the cluster for which the managed scaling policy will be fetched.   
Type: String  
Length Constraints: Maximum length of 256.  
Required: Yes

## Response Syntax
<a name="API_GetManagedScalingPolicy_ResponseSyntax"></a>

```
{
   "ManagedScalingPolicy": { 
      "ComputeLimits": { 
         "MaximumCapacityUnits": number,
         "MaximumCoreCapacityUnits": number,
         "MaximumOnDemandCapacityUnits": number,
         "MinimumCapacityUnits": number,
         "UnitType": "string"
      },
      "ScalingStrategy": "string",
      "UtilizationPerformanceIndex": number
   }
}
```

## Response Elements
<a name="API_GetManagedScalingPolicy_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ManagedScalingPolicy](#API_GetManagedScalingPolicy_ResponseSyntax) **   <a name="EMR-GetManagedScalingPolicy-response-ManagedScalingPolicy"></a>
Specifies the managed scaling policy that is attached to an Amazon EMR cluster.   
Type: [ManagedScalingPolicy](API_ManagedScalingPolicy.md) object

## Errors
<a name="API_GetManagedScalingPolicy_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## See Also
<a name="API_GetManagedScalingPolicy_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/elasticmapreduce-2009-03-31/GetManagedScalingPolicy) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/elasticmapreduce-2009-03-31/GetManagedScalingPolicy) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/elasticmapreduce-2009-03-31/GetManagedScalingPolicy) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/elasticmapreduce-2009-03-31/GetManagedScalingPolicy) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/elasticmapreduce-2009-03-31/GetManagedScalingPolicy) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/elasticmapreduce-2009-03-31/GetManagedScalingPolicy) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/elasticmapreduce-2009-03-31/GetManagedScalingPolicy) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/elasticmapreduce-2009-03-31/GetManagedScalingPolicy) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/elasticmapreduce-2009-03-31/GetManagedScalingPolicy) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/elasticmapreduce-2009-03-31/GetManagedScalingPolicy) 