---
id: "@specs/aws/kendra/docs/API_CollapseConfiguration"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS CollapseConfiguration"
status: active
depends_on:
  - "@specs/aws/kendra/meta"
---

# CollapseConfiguration

> **source:** AWS Documentation
> **spec:id:** @specs/aws/kendra/docs/API_CollapseConfiguration
> **target_lang:** meta — documentation tier. ALL sections preserved.



# CollapseConfiguration
<a name="API_CollapseConfiguration"></a>

Specifies how to group results by document attribute value, and how to display them collapsed/expanded under a designated primary document for each group.

## Contents
<a name="API_CollapseConfiguration_Contents"></a>

 ** DocumentAttributeKey **   <a name="kendra-Type-CollapseConfiguration-DocumentAttributeKey"></a>
The document attribute used to group search results. You can use any attribute that has the `Sortable` flag set to true. You can also sort by any of the following built-in attributes:"\_category","\_created\_at", "\_last\_updated\_at", "\_version", "\_view\_count".  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 200.  
Pattern: `[a-zA-Z0-9_][a-zA-Z0-9_-]*`   
Required: Yes

 ** Expand **   <a name="kendra-Type-CollapseConfiguration-Expand"></a>
Specifies whether to expand the collapsed results.  
Type: Boolean  
Required: No

 ** ExpandConfiguration **   <a name="kendra-Type-CollapseConfiguration-ExpandConfiguration"></a>
Provides configuration information to customize expansion options for a collapsed group.  
Type: [ExpandConfiguration](API_ExpandConfiguration.md) object  
Required: No

 ** MissingAttributeKeyStrategy **   <a name="kendra-Type-CollapseConfiguration-MissingAttributeKeyStrategy"></a>
Specifies the behavior for documents without a value for the collapse attribute.  
Amazon Kendra offers three customization options:  
+ Choose to `COLLAPSE` all documents with null or missing values in one group. This is the default configuration.
+ Choose to `IGNORE` documents with null or missing values. Ignored documents will not appear in query results.
+ Choose to `EXPAND` each document with a null or missing value into a group of its own.
Type: String  
Valid Values: `IGNORE | COLLAPSE | EXPAND`   
Required: No

 ** SortingConfigurations **   <a name="kendra-Type-CollapseConfiguration-SortingConfigurations"></a>
A prioritized list of document attributes/fields that determine the primary document among those in a collapsed group.  
Type: Array of [SortingConfiguration](API_SortingConfiguration.md) objects  
Array Members: Minimum number of 1 item.  
Required: No

## See Also
<a name="API_CollapseConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/kendra-2019-02-03/CollapseConfiguration) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/kendra-2019-02-03/CollapseConfiguration) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/kendra-2019-02-03/CollapseConfiguration) 