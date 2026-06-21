---
id: "@specs/aws/cloudtrail/docs/API_Widget"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Widget"
status: active
depends_on:
  - "@specs/aws/cloudtrail/meta"
---

# Widget

> **source:** AWS Documentation
> **spec:id:** @specs/aws/cloudtrail/docs/API_Widget
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Widget
<a name="API_Widget"></a>

 A widget on a CloudTrail Lake dashboard. 

## Contents
<a name="API_Widget_Contents"></a>

 ** QueryAlias **   <a name="awscloudtrail-Type-Widget-QueryAlias"></a>
The query alias used to identify the query for the widget.   
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 256.  
Pattern: `^[a-zA-Z][a-zA-Z0-9._\-]*$`   
Required: No

 ** QueryParameters **   <a name="awscloudtrail-Type-Widget-QueryParameters"></a>
 The query parameters for the widget.   
Type: Array of strings  
Array Members: Minimum number of 1 item. Maximum number of 10 items.  
Length Constraints: Minimum length of 1. Maximum length of 1024.  
Pattern: `.*`   
Required: No

 ** QueryStatement **   <a name="awscloudtrail-Type-Widget-QueryStatement"></a>
 The SQL query statement for the widget.   
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 10000.  
Pattern: `(?s).*`   
Required: No

 ** ViewProperties **   <a name="awscloudtrail-Type-Widget-ViewProperties"></a>
 The view properties for the widget. For more information about view properties, see [ View properties for widgets ](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/lake-widget-properties.html) in the * AWS CloudTrail User Guide*..   
Type: String to string map  
Key Length Constraints: Minimum length of 3. Maximum length of 128.  
Key Pattern: `^[a-zA-Z0-9._\-]+$`   
Value Length Constraints: Minimum length of 1. Maximum length of 128.  
Value Pattern: `^[a-zA-Z0-9._\- ]+$`   
Required: No

## See Also
<a name="API_Widget_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cloudtrail-2013-11-01/Widget) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudtrail-2013-11-01/Widget) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudtrail-2013-11-01/Widget) 