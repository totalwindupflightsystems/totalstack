---
id: "@specs/aws/batch/docs/API_ConsumableResourceSummary"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS ConsumableResourceSummary"
status: active
depends_on:
  - "@specs/aws/batch/meta"
---

# ConsumableResourceSummary

> **source:** AWS Documentation
> **spec:id:** @specs/aws/batch/docs/API_ConsumableResourceSummary
> **target_lang:** meta — documentation tier. ALL sections preserved.



# ConsumableResourceSummary
<a name="API_ConsumableResourceSummary"></a>

Current information about a consumable resource.

## Contents
<a name="API_ConsumableResourceSummary_Contents"></a>

 ** consumableResourceArn **   <a name="Batch-Type-ConsumableResourceSummary-consumableResourceArn"></a>
The Amazon Resource Name (ARN) of the consumable resource.  
Type: String  
Required: Yes

 ** consumableResourceName **   <a name="Batch-Type-ConsumableResourceSummary-consumableResourceName"></a>
The name of the consumable resource.  
Type: String  
Required: Yes

 ** inUseQuantity **   <a name="Batch-Type-ConsumableResourceSummary-inUseQuantity"></a>
The amount of the consumable resource that is currently in use.  
Type: Long  
Required: No

 ** resourceType **   <a name="Batch-Type-ConsumableResourceSummary-resourceType"></a>
Indicates whether the resource is available to be re-used after a job completes. Can be one of:   
+  `REPLENISHABLE` 
+  `NON_REPLENISHABLE` 
Type: String  
Required: No

 ** totalQuantity **   <a name="Batch-Type-ConsumableResourceSummary-totalQuantity"></a>
The total amount of the consumable resource that is available.  
Type: Long  
Required: No

## See Also
<a name="API_ConsumableResourceSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/batch-2016-08-10/ConsumableResourceSummary) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/batch-2016-08-10/ConsumableResourceSummary) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/batch-2016-08-10/ConsumableResourceSummary) 