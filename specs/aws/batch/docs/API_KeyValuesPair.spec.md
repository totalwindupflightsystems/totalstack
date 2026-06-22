---
id: "@specs/aws/batch/docs/API_KeyValuesPair"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS KeyValuesPair"
status: active
depends_on:
  - "@specs/aws/batch/meta"
---

# KeyValuesPair

> **source:** AWS Documentation
> **spec:id:** @specs/aws/batch/docs/API_KeyValuesPair
> **target_lang:** meta — documentation tier. ALL sections preserved.



# KeyValuesPair
<a name="API_KeyValuesPair"></a>

A filter name and value pair that's used to return a more specific list of results from a `ListJobs` or `ListJobsByConsumableResource` API operation.

The filters supported are documented in the `ListJobs` API operation.

## Contents
<a name="API_KeyValuesPair_Contents"></a>

 ** name **   <a name="Batch-Type-KeyValuesPair-name"></a>
The name of the filter. Filter names are case sensitive.  
Type: String  
Required: No

 ** values **   <a name="Batch-Type-KeyValuesPair-values"></a>
The filter values.  
Type: Array of strings  
Required: No

## See Also
<a name="API_KeyValuesPair_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/batch-2016-08-10/KeyValuesPair) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/batch-2016-08-10/KeyValuesPair) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/batch-2016-08-10/KeyValuesPair) 