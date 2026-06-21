---
id: "@specs/aws/shield/docs/API_AttackProperty"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS AttackProperty"
status: active
depends_on:
  - "@specs/aws/shield/meta"
---

# AttackProperty

> **source:** AWS Documentation
> **spec:id:** @specs/aws/shield/docs/API_AttackProperty
> **target_lang:** meta — documentation tier. ALL sections preserved.



# AttackProperty
<a name="API_AttackProperty"></a>

Details of a AWS Shield event. This is provided as part of an [AttackDetail](API_AttackDetail.md).

## Contents
<a name="API_AttackProperty_Contents"></a>

 ** AttackLayer **   <a name="AWSShield-Type-AttackProperty-AttackLayer"></a>
The type of AWS Shield event that was observed. `NETWORK` indicates layer 3 and layer 4 events and `APPLICATION` indicates layer 7 events.  
For infrastructure layer events (L3 and L4 events), you can view metrics for top contributors in Amazon CloudWatch metrics. For more information, see [AWS Shield metrics and alarms](https://docs.aws.amazon.com/waf/latest/developerguide/monitoring-cloudwatch.html#set-ddos-alarms) in the * AWS WAF Developer Guide*.   
Type: String  
Valid Values: `NETWORK | APPLICATION`   
Required: No

 ** AttackPropertyIdentifier **   <a name="AWSShield-Type-AttackProperty-AttackPropertyIdentifier"></a>
Defines the AWS Shield event property information that is provided. The `WORDPRESS_PINGBACK_REFLECTOR` and `WORDPRESS_PINGBACK_SOURCE` values are valid only for WordPress reflective pingback events.  
Type: String  
Valid Values: `DESTINATION_URL | REFERRER | SOURCE_ASN | SOURCE_COUNTRY | SOURCE_IP_ADDRESS | SOURCE_USER_AGENT | WORDPRESS_PINGBACK_REFLECTOR | WORDPRESS_PINGBACK_SOURCE`   
Required: No

 ** TopContributors **   <a name="AWSShield-Type-AttackProperty-TopContributors"></a>
Contributor objects for the top five contributors to a Shield event. A contributor is a source of traffic that Shield Advanced identifies as responsible for some or all of an event.  
Type: Array of [Contributor](API_Contributor.md) objects  
Required: No

 ** Total **   <a name="AWSShield-Type-AttackProperty-Total"></a>
The total contributions made to this Shield event by all contributors.  
Type: Long  
Required: No

 ** Unit **   <a name="AWSShield-Type-AttackProperty-Unit"></a>
The unit used for the `Contributor` `Value` property.   
Type: String  
Valid Values: `BITS | BYTES | PACKETS | REQUESTS`   
Required: No

## See Also
<a name="API_AttackProperty_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/shield-2016-06-02/AttackProperty) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/shield-2016-06-02/AttackProperty) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/shield-2016-06-02/AttackProperty) 