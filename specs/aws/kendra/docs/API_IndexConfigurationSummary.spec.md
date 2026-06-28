---
id: "@specs/aws/kendra/docs/API_IndexConfigurationSummary"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS IndexConfigurationSummary"
status: active
depends_on:
  - "@specs/aws/kendra/meta"
---

# IndexConfigurationSummary

> **source:** AWS Documentation
> **spec:id:** @specs/aws/kendra/docs/API_IndexConfigurationSummary
> **target_lang:** meta — documentation tier. ALL sections preserved.



# IndexConfigurationSummary
<a name="API_IndexConfigurationSummary"></a>

Summary information on the configuration of an index.

## Contents
<a name="API_IndexConfigurationSummary_Contents"></a>

 ** CreatedAt **   <a name="kendra-Type-IndexConfigurationSummary-CreatedAt"></a>
The Unix timestamp when the index was created.  
Type: Timestamp  
Required: Yes

 ** Status **   <a name="kendra-Type-IndexConfigurationSummary-Status"></a>
The current status of the index. When the status is `ACTIVE`, the index is ready to search.  
Type: String  
Valid Values: `CREATING | ACTIVE | DELETING | FAILED | UPDATING | SYSTEM_UPDATING`   
Required: Yes

 ** UpdatedAt **   <a name="kendra-Type-IndexConfigurationSummary-UpdatedAt"></a>
The Unix timestamp when the index was last updated.  
Type: Timestamp  
Required: Yes

 ** Edition **   <a name="kendra-Type-IndexConfigurationSummary-Edition"></a>
Indicates whether the index is a Enterprise Edition index or a Developer Edition index.   
Type: String  
Valid Values: `DEVELOPER_EDITION | ENTERPRISE_EDITION | GEN_AI_ENTERPRISE_EDITION`   
Required: No

 ** Id **   <a name="kendra-Type-IndexConfigurationSummary-Id"></a>
A identifier for the index. Use this to identify the index when you are using APIs such as `Query`, `DescribeIndex`, `UpdateIndex`, and `DeleteIndex`.  
Type: String  
Length Constraints: Fixed length of 36.  
Pattern: `[a-zA-Z0-9][a-zA-Z0-9-]*`   
Required: No

 ** Name **   <a name="kendra-Type-IndexConfigurationSummary-Name"></a>
The name of the index.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 1000.  
Pattern: `[a-zA-Z0-9][a-zA-Z0-9_-]*`   
Required: No

## See Also
<a name="API_IndexConfigurationSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/kendra-2019-02-03/IndexConfigurationSummary) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/kendra-2019-02-03/IndexConfigurationSummary) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/kendra-2019-02-03/IndexConfigurationSummary) 