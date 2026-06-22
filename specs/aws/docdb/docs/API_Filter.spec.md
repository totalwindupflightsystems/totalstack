---
id: "@specs/aws/docdb/docs/API_Filter"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Filter"
status: active
depends_on:
  - "@specs/aws/docdb/meta"
---

# Filter

> **source:** AWS Documentation
> **spec:id:** @specs/aws/docdb/docs/API_Filter
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Filter
<a name="API_Filter"></a>

A named set of filter values, used to return a more specific list of results. You can use a filter to match a set of resources by specific criteria, such as IDs.

Wildcards are not supported in filters.

## Contents
<a name="API_Filter_Contents"></a>

**Note**  
In the following list, the required parameters are described first.

 ** Name **   
The name of the filter. Filter names are case sensitive.  
Type: String  
Required: Yes

 ** Values.Value.N **   
One or more filter values. Filter values are case sensitive.  
Type: Array of strings  
Required: Yes

## See Also
<a name="API_Filter_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/docdb-2014-10-31/Filter) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/docdb-2014-10-31/Filter) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/docdb-2014-10-31/Filter) 