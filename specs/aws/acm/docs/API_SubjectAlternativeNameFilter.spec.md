---
id: "@specs/aws/acm/docs/API_SubjectAlternativeNameFilter"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS SubjectAlternativeNameFilter"
status: active
depends_on:
  - "@specs/aws/acm/meta"
---

# SubjectAlternativeNameFilter

> **source:** AWS Documentation
> **spec:id:** @specs/aws/acm/docs/API_SubjectAlternativeNameFilter
> **target_lang:** meta — documentation tier. ALL sections preserved.



# SubjectAlternativeNameFilter
<a name="API_SubjectAlternativeNameFilter"></a>

Filters certificates by subject alternative name attributes.

## Contents
<a name="API_SubjectAlternativeNameFilter_Contents"></a>

**Note**  
In the following list, the required parameters are described first.

**Important**  
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** DnsName **   <a name="ACM-Type-SubjectAlternativeNameFilter-DnsName"></a>
Filter by DNS name in subject alternative names.  
Type: [DnsNameFilter](API_DnsNameFilter.md) object  
Required: No

## See Also
<a name="API_SubjectAlternativeNameFilter_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/acm-2015-12-08/SubjectAlternativeNameFilter) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/acm-2015-12-08/SubjectAlternativeNameFilter) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/acm-2015-12-08/SubjectAlternativeNameFilter) 