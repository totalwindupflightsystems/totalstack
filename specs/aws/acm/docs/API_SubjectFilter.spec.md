---
id: "@specs/aws/acm/docs/API_SubjectFilter"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS SubjectFilter"
status: active
depends_on:
  - "@specs/aws/acm/meta"
---

# SubjectFilter

> **source:** AWS Documentation
> **spec:id:** @specs/aws/acm/docs/API_SubjectFilter
> **target_lang:** meta — documentation tier. ALL sections preserved.



# SubjectFilter
<a name="API_SubjectFilter"></a>

Filters certificates by subject attributes.

## Contents
<a name="API_SubjectFilter_Contents"></a>

**Note**  
In the following list, the required parameters are described first.

**Important**  
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** CommonName **   <a name="ACM-Type-SubjectFilter-CommonName"></a>
Filter by common name in the subject.  
Type: [CommonNameFilter](API_CommonNameFilter.md) object  
Required: No

## See Also
<a name="API_SubjectFilter_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/acm-2015-12-08/SubjectFilter) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/acm-2015-12-08/SubjectFilter) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/acm-2015-12-08/SubjectFilter) 