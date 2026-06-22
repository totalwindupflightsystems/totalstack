---
id: "@specs/aws/redshift/docs/API_EventInfoMap"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS EventInfoMap"
status: active
depends_on:
  - "@specs/aws/redshift/meta"
---

# EventInfoMap

> **source:** AWS Documentation
> **spec:id:** @specs/aws/redshift/docs/API_EventInfoMap
> **target_lang:** meta — documentation tier. ALL sections preserved.



# EventInfoMap
<a name="API_EventInfoMap"></a>

Describes event information.

## Contents
<a name="API_EventInfoMap_Contents"></a>

**Note**  
In the following list, the required parameters are described first.

 ** EventCategories.EventCategory.N **   
The category of an Amazon Redshift event.  
Type: Array of strings  
Length Constraints: Maximum length of 2147483647.  
Required: No

 ** EventDescription **   
The description of an Amazon Redshift event.  
Type: String  
Length Constraints: Maximum length of 2147483647.  
Required: No

 ** EventId **   
The identifier of an Amazon Redshift event.  
Type: String  
Length Constraints: Maximum length of 2147483647.  
Required: No

 ** Severity **   
The severity of the event.  
Values: ERROR, INFO  
Type: String  
Length Constraints: Maximum length of 2147483647.  
Required: No

## See Also
<a name="API_EventInfoMap_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/redshift-2012-12-01/EventInfoMap) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/redshift-2012-12-01/EventInfoMap) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/redshift-2012-12-01/EventInfoMap) 