---
id: "@specs/aws/redshift/docs/API_EventCategoriesMap"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS EventCategoriesMap"
status: active
depends_on:
  - "@specs/aws/redshift/meta"
---

# EventCategoriesMap

> **source:** AWS Documentation
> **spec:id:** @specs/aws/redshift/docs/API_EventCategoriesMap
> **target_lang:** meta — documentation tier. ALL sections preserved.



# EventCategoriesMap
<a name="API_EventCategoriesMap"></a>

Describes event categories.

## Contents
<a name="API_EventCategoriesMap_Contents"></a>

**Note**  
In the following list, the required parameters are described first.

 ** Events.EventInfoMap.N **   
The events in the event category.  
Type: Array of [EventInfoMap](API_EventInfoMap.md) objects  
Required: No

 ** SourceType **   
The source type, such as cluster or cluster-snapshot, that the returned categories belong to.  
Type: String  
Length Constraints: Maximum length of 2147483647.  
Required: No

## See Also
<a name="API_EventCategoriesMap_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/redshift-2012-12-01/EventCategoriesMap) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/redshift-2012-12-01/EventCategoriesMap) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/redshift-2012-12-01/EventCategoriesMap) 