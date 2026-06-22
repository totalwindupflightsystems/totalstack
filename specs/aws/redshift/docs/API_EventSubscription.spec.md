---
id: "@specs/aws/redshift/docs/API_EventSubscription"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS EventSubscription"
status: active
depends_on:
  - "@specs/aws/redshift/meta"
---

# EventSubscription

> **source:** AWS Documentation
> **spec:id:** @specs/aws/redshift/docs/API_EventSubscription
> **target_lang:** meta — documentation tier. ALL sections preserved.



# EventSubscription
<a name="API_EventSubscription"></a>

Describes event subscriptions.

## Contents
<a name="API_EventSubscription_Contents"></a>

**Note**  
In the following list, the required parameters are described first.

 ** CustomerAwsId **   
The AWS account associated with the Amazon Redshift event notification subscription.  
Type: String  
Length Constraints: Maximum length of 2147483647.  
Required: No

 ** CustSubscriptionId **   
The name of the Amazon Redshift event notification subscription.  
Type: String  
Length Constraints: Maximum length of 2147483647.  
Required: No

 ** Enabled **   
A boolean value indicating whether the subscription is enabled; `true` indicates that the subscription is enabled.  
Type: Boolean  
Required: No

 ** EventCategoriesList.EventCategory.N **   
The list of Amazon Redshift event categories specified in the event notification subscription.  
Values: Configuration, Management, Monitoring, Security, Pending  
Type: Array of strings  
Length Constraints: Maximum length of 2147483647.  
Required: No

 ** Severity **   
The event severity specified in the Amazon Redshift event notification subscription.  
Values: ERROR, INFO  
Type: String  
Length Constraints: Maximum length of 2147483647.  
Required: No

 ** SnsTopicArn **   
The Amazon Resource Name (ARN) of the Amazon SNS topic used by the event notification subscription.  
Type: String  
Length Constraints: Maximum length of 2147483647.  
Required: No

 ** SourceIdsList.SourceId.N **   
A list of the sources that publish events to the Amazon Redshift event notification subscription.  
Type: Array of strings  
Length Constraints: Maximum length of 2147483647.  
Required: No

 ** SourceType **   
The source type of the events returned by the Amazon Redshift event notification, such as cluster, cluster-snapshot, cluster-parameter-group, cluster-security-group, or scheduled-action.   
Type: String  
Length Constraints: Maximum length of 2147483647.  
Required: No

 ** Status **   
The status of the Amazon Redshift event notification subscription.  
Constraints:  
+ Can be one of the following: active \| no-permission \| topic-not-exist
+ The status "no-permission" indicates that Amazon Redshift no longer has permission to post to the Amazon SNS topic. The status "topic-not-exist" indicates that the topic was deleted after the subscription was created.
Type: String  
Length Constraints: Maximum length of 2147483647.  
Required: No

 ** SubscriptionCreationTime **   
The date and time the Amazon Redshift event notification subscription was created.  
Type: Timestamp  
Required: No

 ** Tags.Tag.N **   
The list of tags for the event subscription.  
Type: Array of [Tag](API_Tag.md) objects  
Required: No

## See Also
<a name="API_EventSubscription_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/redshift-2012-12-01/EventSubscription) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/redshift-2012-12-01/EventSubscription) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/redshift-2012-12-01/EventSubscription) 