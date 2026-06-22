---
id: "@specs/aws/docdb/docs/API_EventSubscription"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS EventSubscription"
status: active
depends_on:
  - "@specs/aws/docdb/meta"
---

# EventSubscription

> **source:** AWS Documentation
> **spec:id:** @specs/aws/docdb/docs/API_EventSubscription
> **target_lang:** meta — documentation tier. ALL sections preserved.



# EventSubscription
<a name="API_EventSubscription"></a>

Detailed information about an event to which you have subscribed.

## Contents
<a name="API_EventSubscription_Contents"></a>

**Note**  
In the following list, the required parameters are described first.

 ** CustomerAwsId **   
The AWS customer account that is associated with the Amazon DocumentDB event notification subscription.  
Type: String  
Required: No

 ** CustSubscriptionId **   
The Amazon DocumentDB event notification subscription ID.  
Type: String  
Required: No

 ** Enabled **   
A Boolean value indicating whether the subscription is enabled. A value of `true` indicates that the subscription is enabled.  
Type: Boolean  
Required: No

 ** EventCategoriesList.EventCategory.N **   
A list of event categories for the Amazon DocumentDB event notification subscription.  
Type: Array of strings  
Required: No

 ** EventSubscriptionArn **   
The Amazon Resource Name (ARN) for the event subscription.  
Type: String  
Required: No

 ** SnsTopicArn **   
The topic ARN of the Amazon DocumentDB event notification subscription.  
Type: String  
Required: No

 ** SourceIdsList.SourceId.N **   
A list of source IDs for the Amazon DocumentDB event notification subscription.  
Type: Array of strings  
Required: No

 ** SourceType **   
The source type for the Amazon DocumentDB event notification subscription.  
Type: String  
Required: No

 ** Status **   
The status of the Amazon DocumentDB event notification subscription.  
Constraints:  
Can be one of the following: `creating`, `modifying`, `deleting`, `active`, `no-permission`, `topic-not-exist`   
The `no-permission` status indicates that Amazon DocumentDB no longer has permission to post to the SNS topic. The `topic-not-exist` status indicates that the topic was deleted after the subscription was created.  
Type: String  
Required: No

 ** SubscriptionCreationTime **   
The time at which the Amazon DocumentDB event notification subscription was created.  
Type: String  
Required: No

## See Also
<a name="API_EventSubscription_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/docdb-2014-10-31/EventSubscription) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/docdb-2014-10-31/EventSubscription) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/docdb-2014-10-31/EventSubscription) 