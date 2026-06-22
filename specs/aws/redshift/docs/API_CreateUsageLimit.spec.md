---
id: "@specs/aws/redshift/docs/API_CreateUsageLimit"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS CreateUsageLimit"
status: active
depends_on:
  - "@specs/aws/redshift/meta"
---

# CreateUsageLimit

> **source:** AWS Documentation
> **spec:id:** @specs/aws/redshift/docs/API_CreateUsageLimit
> **target_lang:** meta — documentation tier. ALL sections preserved.



# CreateUsageLimit
<a name="API_CreateUsageLimit"></a>

Creates a usage limit for a specified Amazon Redshift feature on a cluster. The usage limit is identified by the returned usage limit identifier.

## Request Parameters
<a name="API_CreateUsageLimit_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 ** Amount **   
The limit amount. If time-based, this amount is in minutes. If data-based, this amount is in terabytes (TB). The value must be a positive number.   
Type: Long  
Required: Yes

 ** ClusterIdentifier **   
The identifier of the cluster that you want to limit usage.  
Type: String  
Length Constraints: Maximum length of 2147483647.  
Required: Yes

 ** FeatureType **   
The Amazon Redshift feature that you want to limit.  
Type: String  
Valid Values: `spectrum | concurrency-scaling | cross-region-datasharing | extra-compute-for-automatic-optimization`   
Required: Yes

 ** LimitType **   
The type of limit. Depending on the feature type, this can be based on a time duration or data size. If `FeatureType` is `spectrum`, then `LimitType` must be `data-scanned`. If `FeatureType` is `concurrency-scaling`, then `LimitType` must be `time`. If `FeatureType` is `cross-region-datasharing`, then `LimitType` must be `data-scanned`. If `FeatureType` is `extra-compute-for-automatic-optimization`, then `LimitType` must be `time`.   
Type: String  
Valid Values: `time | data-scanned`   
Required: Yes

 ** BreachAction **   
The action that Amazon Redshift takes when the limit is reached. The default is log. For more information about this parameter, see [UsageLimit](API_UsageLimit.md).  
Type: String  
Valid Values: `log | emit-metric | disable`   
Required: No

 ** Period **   
The time period that the amount applies to. A `weekly` period begins on Sunday. The default is `monthly`.   
Type: String  
Valid Values: `daily | weekly | monthly`   
Required: No

 **Tags.Tag.N**   
A list of tag instances.  
Type: Array of [Tag](API_Tag.md) objects  
Required: No

## Response Elements
<a name="API_CreateUsageLimit_ResponseElements"></a>

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
<a name="API_CreateUsageLimit_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ClusterNotFound **   
The `ClusterIdentifier` parameter does not refer to an existing cluster.   
HTTP Status Code: 404

 ** InvalidClusterState **   
The specified cluster is not in the `available` state.   
HTTP Status Code: 400

 ** InvalidUsageLimit **   
The usage limit is not valid.  
HTTP Status Code: 400

 ** LimitExceededFault **   
The encryption key has exceeded its grant limit in AWS KMS.  
HTTP Status Code: 400

 ** TagLimitExceededFault **   
You have exceeded the number of tags allowed.  
HTTP Status Code: 400

 ** UnsupportedOperation **   
The requested operation isn't supported.  
HTTP Status Code: 400

 ** UsageLimitAlreadyExists **   
The usage limit already exists.   
HTTP Status Code: 400

## See Also
<a name="API_CreateUsageLimit_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/redshift-2012-12-01/CreateUsageLimit) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/redshift-2012-12-01/CreateUsageLimit) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/redshift-2012-12-01/CreateUsageLimit) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/redshift-2012-12-01/CreateUsageLimit) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/redshift-2012-12-01/CreateUsageLimit) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/redshift-2012-12-01/CreateUsageLimit) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/redshift-2012-12-01/CreateUsageLimit) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/redshift-2012-12-01/CreateUsageLimit) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/redshift-2012-12-01/CreateUsageLimit) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/redshift-2012-12-01/CreateUsageLimit) 