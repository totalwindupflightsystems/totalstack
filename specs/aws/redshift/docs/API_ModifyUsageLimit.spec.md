---
id: "@specs/aws/redshift/docs/API_ModifyUsageLimit"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS ModifyUsageLimit"
status: active
depends_on:
  - "@specs/aws/redshift/meta"
---

# ModifyUsageLimit

> **source:** AWS Documentation
> **spec:id:** @specs/aws/redshift/docs/API_ModifyUsageLimit
> **target_lang:** meta — documentation tier. ALL sections preserved.



# ModifyUsageLimit
<a name="API_ModifyUsageLimit"></a>

Modifies a usage limit in a cluster. You can't modify the feature type or period of a usage limit.

## Request Parameters
<a name="API_ModifyUsageLimit_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 ** UsageLimitId **   
The identifier of the usage limit to modify.  
Type: String  
Length Constraints: Maximum length of 2147483647.  
Required: Yes

 ** Amount **   
The new limit amount. For more information about this parameter, see [UsageLimit](API_UsageLimit.md).   
Type: Long  
Required: No

 ** BreachAction **   
The new action that Amazon Redshift takes when the limit is reached. For more information about this parameter, see [UsageLimit](API_UsageLimit.md).   
Type: String  
Valid Values: `log | emit-metric | disable`   
Required: No

## Response Elements
<a name="API_ModifyUsageLimit_ResponseElements"></a>

The following elements are returned by the service.

 ** Amount **   
The limit amount. If time-based, this amount is in minutes. If data-based, this amount is in terabytes (TB).  
Type: Long

 ** BreachAction **   
The action that Amazon Redshift takes when the limit is reached. Possible values are:   
+  **log** - To log an event in a system table. The default is log.
+  **emit-metric** - To emit CloudWatch metrics.
+  **disable** - To disable the feature until the next usage period begins.
Type: String  
Valid Values: `log | emit-metric | disable` 

 ** ClusterIdentifier **   
The identifier of the cluster with a usage limit.  
Type: String  
Length Constraints: Maximum length of 2147483647.

 ** FeatureType **   
The Amazon Redshift feature to which the limit applies.  
Type: String  
Valid Values: `spectrum | concurrency-scaling | cross-region-datasharing | extra-compute-for-automatic-optimization` 

 ** LimitType **   
The type of limit. Depending on the feature type, this can be based on a time duration or data size.  
Type: String  
Valid Values: `time | data-scanned` 

 ** Period **   
The time period that the amount applies to. A `weekly` period begins on Sunday. The default is `monthly`.   
Type: String  
Valid Values: `daily | weekly | monthly` 

 **Tags.Tag.N**   
A list of tag instances.  
Type: Array of [Tag](API_Tag.md) objects

 ** UsageLimitId **   
The identifier of the usage limit.  
Type: String  
Length Constraints: Maximum length of 2147483647.

## Errors
<a name="API_ModifyUsageLimit_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InvalidUsageLimit **   
The usage limit is not valid.  
HTTP Status Code: 400

 ** UnsupportedOperation **   
The requested operation isn't supported.  
HTTP Status Code: 400

 ** UsageLimitNotFound **   
The usage limit identifier can't be found.  
HTTP Status Code: 404

## See Also
<a name="API_ModifyUsageLimit_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/redshift-2012-12-01/ModifyUsageLimit) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/redshift-2012-12-01/ModifyUsageLimit) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/redshift-2012-12-01/ModifyUsageLimit) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/redshift-2012-12-01/ModifyUsageLimit) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/redshift-2012-12-01/ModifyUsageLimit) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/redshift-2012-12-01/ModifyUsageLimit) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/redshift-2012-12-01/ModifyUsageLimit) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/redshift-2012-12-01/ModifyUsageLimit) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/redshift-2012-12-01/ModifyUsageLimit) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/redshift-2012-12-01/ModifyUsageLimit) 