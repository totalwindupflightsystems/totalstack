---
id: "@specs/aws/sesv2/docs/API_MessageInsightsFilters"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS MessageInsightsFilters"
status: active
depends_on:
  - "@specs/aws/sesv2/meta"
---

# MessageInsightsFilters

> **source:** AWS Documentation
> **spec:id:** @specs/aws/sesv2/docs/API_MessageInsightsFilters
> **target_lang:** meta — documentation tier. ALL sections preserved.



# MessageInsightsFilters
<a name="API_MessageInsightsFilters"></a>

An object containing Message Insights filters.

If you specify multiple filters, the filters are joined by AND.

If you specify multiple values for a filter, the values are joined by OR. Filter values are case-sensitive.

 `FromEmailAddress`, `Destination`, and `Subject` filters support partial match. A partial match is performed by using the `*` wildcard character placed at the beginning (suffix match), the end (prefix match) or both ends of the string (contains match). In order to match the literal characters `*` or `\`, they must be escaped using the `\` character. If no wildcard character is present, an exact match is performed. 

## Contents
<a name="API_MessageInsightsFilters_Contents"></a>

 ** Destination **   <a name="SES-Type-MessageInsightsFilters-Destination"></a>
The recipient's email address.  
Type: Array of strings  
Array Members: Maximum number of 5 items.  
Length Constraints: Minimum length of 1. Maximum length of 320.  
Required: No

 ** FromEmailAddress **   <a name="SES-Type-MessageInsightsFilters-FromEmailAddress"></a>
The from address used to send the message.  
Type: Array of strings  
Array Members: Maximum number of 5 items.  
Length Constraints: Minimum length of 1. Maximum length of 320.  
Required: No

 ** Isp **   <a name="SES-Type-MessageInsightsFilters-Isp"></a>
The recipient's ISP (e.g., `Gmail`, `Yahoo`, etc.).  
Type: Array of strings  
Array Members: Maximum number of 5 items.  
Required: No

 ** LastDeliveryEvent **   <a name="SES-Type-MessageInsightsFilters-LastDeliveryEvent"></a>
 The last delivery-related event for the email, where the ordering is as follows: `SEND` < `BOUNCE` < `DELIVERY` < `COMPLAINT`.   
Type: Array of strings  
Array Members: Maximum number of 5 items.  
Valid Values: `SEND | DELIVERY | TRANSIENT_BOUNCE | PERMANENT_BOUNCE | UNDETERMINED_BOUNCE | COMPLAINT`   
Required: No

 ** LastEngagementEvent **   <a name="SES-Type-MessageInsightsFilters-LastEngagementEvent"></a>
 The last engagement-related event for the email, where the ordering is as follows: `OPEN` < `CLICK`.   
 Engagement events are only available if [Engagement tracking](https://docs.aws.amazon.com/ses/latest/dg/vdm-settings.html) is enabled.   
Type: Array of strings  
Array Members: Maximum number of 2 items.  
Valid Values: `OPEN | CLICK`   
Required: No

 ** Subject **   <a name="SES-Type-MessageInsightsFilters-Subject"></a>
The subject line of the message.  
Type: Array of strings  
Array Members: Maximum number of 1 item.  
Length Constraints: Minimum length of 1. Maximum length of 998.  
Required: No

## See Also
<a name="API_MessageInsightsFilters_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sesv2-2019-09-27/MessageInsightsFilters) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sesv2-2019-09-27/MessageInsightsFilters) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sesv2-2019-09-27/MessageInsightsFilters) 