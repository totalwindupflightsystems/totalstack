---
id: "@specs/aws/redshift/docs/API_Event"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Event"
status: active
depends_on:
  - "@specs/aws/redshift/meta"
---

# Event

> **source:** AWS Documentation
> **spec:id:** @specs/aws/redshift/docs/API_Event
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Event
<a name="API_Event"></a>

Describes an event.

## Contents
<a name="API_Event_Contents"></a>

**Note**  
In the following list, the required parameters are described first.

 ** Date **   
The date and time of the event.  
Type: Timestamp  
Required: No

 ** EventCategories.EventCategory.N **   
A list of the event categories.  
Values: Configuration, Management, Monitoring, Security, Pending  
Type: Array of strings  
Length Constraints: Maximum length of 2147483647.  
Required: No

 ** EventId **   
The identifier of the event.  
Type: String  
Length Constraints: Maximum length of 2147483647.  
Required: No

 ** Message **   
The text of this event.  
Type: String  
Length Constraints: Maximum length of 2147483647.  
Required: No

 ** Severity **   
The severity of the event.  
Values: ERROR, INFO  
Type: String  
Length Constraints: Maximum length of 2147483647.  
Required: No

 ** SourceIdentifier **   
The identifier for the source of the event.  
Type: String  
Length Constraints: Maximum length of 2147483647.  
Required: No

 ** SourceType **   
The source type for this event.  
Type: String  
Valid Values: `cluster | cluster-parameter-group | cluster-security-group | cluster-snapshot | scheduled-action`   
Required: No

## See Also
<a name="API_Event_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/redshift-2012-12-01/Event) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/redshift-2012-12-01/Event) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/redshift-2012-12-01/Event) 