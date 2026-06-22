---
id: "@specs/aws/docdb/docs/API_Event"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Event"
status: active
depends_on:
  - "@specs/aws/docdb/meta"
---

# Event

> **source:** AWS Documentation
> **spec:id:** @specs/aws/docdb/docs/API_Event
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Event
<a name="API_Event"></a>

Detailed information about an event.

## Contents
<a name="API_Event_Contents"></a>

**Note**  
In the following list, the required parameters are described first.

 ** Date **   
Specifies the date and time of the event.  
Type: Timestamp  
Required: No

 ** EventCategories.EventCategory.N **   
Specifies the category for the event.  
Type: Array of strings  
Required: No

 ** Message **   
Provides the text of this event.  
Type: String  
Required: No

 ** SourceArn **   
The Amazon Resource Name (ARN) for the event.  
Type: String  
Required: No

 ** SourceIdentifier **   
Provides the identifier for the source of the event.  
Type: String  
Required: No

 ** SourceType **   
Specifies the source type for this event.  
Type: String  
Valid Values: `db-instance | db-parameter-group | db-security-group | db-snapshot | db-cluster | db-cluster-snapshot`   
Required: No

## See Also
<a name="API_Event_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/docdb-2014-10-31/Event) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/docdb-2014-10-31/Event) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/docdb-2014-10-31/Event) 