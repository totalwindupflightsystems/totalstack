---
id: "@specs/aws/cloudtrail/docs/API_Destination"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Destination"
status: active
depends_on:
  - "@specs/aws/cloudtrail/meta"
---

# Destination

> **source:** AWS Documentation
> **spec:id:** @specs/aws/cloudtrail/docs/API_Destination
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Destination
<a name="API_Destination"></a>

Contains information about the destination receiving events.

## Contents
<a name="API_Destination_Contents"></a>

 ** Location **   <a name="awscloudtrail-Type-Destination-Location"></a>
 For channels used for a CloudTrail Lake integration, the location is the ARN of an event data store that receives events from a channel. For service-linked channels, the location is the name of the AWS service.  
Type: String  
Length Constraints: Minimum length of 3. Maximum length of 1024.  
Pattern: `^[a-zA-Z0-9._/\-:*]+$`   
Required: Yes

 ** Type **   <a name="awscloudtrail-Type-Destination-Type"></a>
The type of destination for events arriving from a channel. For channels used for a CloudTrail Lake integration, the value is `EVENT_DATA_STORE`. For service-linked channels, the value is `AWS_SERVICE`.   
Type: String  
Valid Values: `EVENT_DATA_STORE | AWS_SERVICE`   
Required: Yes

## See Also
<a name="API_Destination_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cloudtrail-2013-11-01/Destination) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudtrail-2013-11-01/Destination) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudtrail-2013-11-01/Destination) 