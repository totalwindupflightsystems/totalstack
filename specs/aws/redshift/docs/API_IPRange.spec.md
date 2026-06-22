---
id: "@specs/aws/redshift/docs/API_IPRange"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS IPRange"
status: active
depends_on:
  - "@specs/aws/redshift/meta"
---

# IPRange

> **source:** AWS Documentation
> **spec:id:** @specs/aws/redshift/docs/API_IPRange
> **target_lang:** meta — documentation tier. ALL sections preserved.



# IPRange
<a name="API_IPRange"></a>

Describes an IP range used in a security group.

## Contents
<a name="API_IPRange_Contents"></a>

**Note**  
In the following list, the required parameters are described first.

 ** CIDRIP **   
The IP range in Classless Inter-Domain Routing (CIDR) notation.  
Type: String  
Length Constraints: Maximum length of 2147483647.  
Required: No

 ** Status **   
The status of the IP range, for example, "authorized".  
Type: String  
Length Constraints: Maximum length of 2147483647.  
Required: No

 ** Tags.Tag.N **   
The list of tags for the IP range.  
Type: Array of [Tag](API_Tag.md) objects  
Required: No

## See Also
<a name="API_IPRange_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/redshift-2012-12-01/IPRange) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/redshift-2012-12-01/IPRange) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/redshift-2012-12-01/IPRange) 