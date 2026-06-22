---
id: "@specs/aws/acm/docs/API_DnsNameFilter"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS DnsNameFilter"
status: active
depends_on:
  - "@specs/aws/acm/meta"
---

# DnsNameFilter

> **source:** AWS Documentation
> **spec:id:** @specs/aws/acm/docs/API_DnsNameFilter
> **target_lang:** meta — documentation tier. ALL sections preserved.



# DnsNameFilter
<a name="API_DnsNameFilter"></a>

Filters certificates by DNS name.

## Contents
<a name="API_DnsNameFilter_Contents"></a>

**Note**  
In the following list, the required parameters are described first.

 ** ComparisonOperator **   <a name="ACM-Type-DnsNameFilter-ComparisonOperator"></a>
The comparison operator to use.  
Type: String  
Valid Values: `CONTAINS | EQUALS`   
Required: Yes

 ** Value **   <a name="ACM-Type-DnsNameFilter-Value"></a>
The DNS name value to match against.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 256.  
Required: Yes

## See Also
<a name="API_DnsNameFilter_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/acm-2015-12-08/DnsNameFilter) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/acm-2015-12-08/DnsNameFilter) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/acm-2015-12-08/DnsNameFilter) 