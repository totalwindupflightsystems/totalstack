---
id: "@specs/aws/batch/docs/API_QuotaShareResourceSharingConfiguration"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS QuotaShareResourceSharingConfiguration"
status: active
depends_on:
  - "@specs/aws/batch/meta"
---

# QuotaShareResourceSharingConfiguration

> **source:** AWS Documentation
> **spec:id:** @specs/aws/batch/docs/API_QuotaShareResourceSharingConfiguration
> **target_lang:** meta — documentation tier. ALL sections preserved.



# QuotaShareResourceSharingConfiguration
<a name="API_QuotaShareResourceSharingConfiguration"></a>

Specifies whether a quota share reserves, lends, or both lends and borrows idle compute capacity.

## Contents
<a name="API_QuotaShareResourceSharingConfiguration_Contents"></a>

 ** strategy **   <a name="Batch-Type-QuotaShareResourceSharingConfiguration-strategy"></a>
The resource sharing strategy for the quota share. The `RESERVE` strategy allows a quota share to reserve idle capacity for itself. `LEND` configures the share to lend its idle capacity to another share in need of capacity. The `LEND_AND_BORROW` strategy configures the share to borrow idle capacity from an underutilized share, as well as lend to another share.  
Type: String  
Valid Values: `RESERVE | LEND | LEND_AND_BORROW`   
Required: Yes

 ** borrowLimit **   <a name="Batch-Type-QuotaShareResourceSharingConfiguration-borrowLimit"></a>
The maximum percentage of additional capacity that the quota share can borrow from other shares. `borrowLimit` can only be applied to quota shares with a strategy of `LEND_AND_BORROW`. This value is expressed as a percentage of the quota share's configured [CapacityLimits](https://docs.aws.amazon.com/batch/latest/APIReference/API_QuotaShareCapacityLimit.html).  
The `borrowLimit` is applied uniformly across all capacity units. For example, if the `borrowLimit` is 200, the quota share can borrow up to 200% of its configured `maxCapacity` for each capacity unit. The default `borrowLimit` is -1, which indicates unlimited borrowing.  
Type: Integer  
Required: No

## See Also
<a name="API_QuotaShareResourceSharingConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/batch-2016-08-10/QuotaShareResourceSharingConfiguration) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/batch-2016-08-10/QuotaShareResourceSharingConfiguration) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/batch-2016-08-10/QuotaShareResourceSharingConfiguration) 