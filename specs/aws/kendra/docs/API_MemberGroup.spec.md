---
id: "@specs/aws/kendra/docs/API_MemberGroup"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS MemberGroup"
status: active
depends_on:
  - "@specs/aws/kendra/meta"
---

# MemberGroup

> **source:** AWS Documentation
> **spec:id:** @specs/aws/kendra/docs/API_MemberGroup
> **target_lang:** meta — documentation tier. ALL sections preserved.



# MemberGroup
<a name="API_MemberGroup"></a>

The sub groups that belong to a group.

## Contents
<a name="API_MemberGroup_Contents"></a>

 ** GroupId **   <a name="kendra-Type-MemberGroup-GroupId"></a>
The identifier of the sub group you want to map to a group.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 1024.  
Pattern: `^\P{C}*$`   
Required: Yes

 ** DataSourceId **   <a name="kendra-Type-MemberGroup-DataSourceId"></a>
The identifier of the data source for the sub group you want to map to a group.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 100.  
Pattern: `[a-zA-Z0-9][a-zA-Z0-9_-]*`   
Required: No

## See Also
<a name="API_MemberGroup_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/kendra-2019-02-03/MemberGroup) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/kendra-2019-02-03/MemberGroup) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/kendra-2019-02-03/MemberGroup) 