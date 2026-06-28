---
id: "@specs/aws/kendra/docs/API_ExpandConfiguration"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS ExpandConfiguration"
status: active
depends_on:
  - "@specs/aws/kendra/meta"
---

# ExpandConfiguration

> **source:** AWS Documentation
> **spec:id:** @specs/aws/kendra/docs/API_ExpandConfiguration
> **target_lang:** meta — documentation tier. ALL sections preserved.



# ExpandConfiguration
<a name="API_ExpandConfiguration"></a>

Specifies the configuration information needed to customize how collapsed search result groups expand.

## Contents
<a name="API_ExpandConfiguration_Contents"></a>

 ** MaxExpandedResultsPerItem **   <a name="kendra-Type-ExpandConfiguration-MaxExpandedResultsPerItem"></a>
The number of expanded results to show per collapsed primary document. For instance, if you set this value to 3, then at most 3 results per collapsed group will be displayed.  
Type: Integer  
Required: No

 ** MaxResultItemsToExpand **   <a name="kendra-Type-ExpandConfiguration-MaxResultItemsToExpand"></a>
The number of collapsed search result groups to expand. If you set this value to 10, for example, only the first 10 out of 100 result groups will have expand functionality.   
Type: Integer  
Required: No

## See Also
<a name="API_ExpandConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/kendra-2019-02-03/ExpandConfiguration) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/kendra-2019-02-03/ExpandConfiguration) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/kendra-2019-02-03/ExpandConfiguration) 