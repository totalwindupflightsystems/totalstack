---
id: "@specs/aws/acm/docs/API_ExpiryEventsConfiguration"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS ExpiryEventsConfiguration"
status: active
depends_on:
  - "@specs/aws/acm/meta"
---

# ExpiryEventsConfiguration

> **source:** AWS Documentation
> **spec:id:** @specs/aws/acm/docs/API_ExpiryEventsConfiguration
> **target_lang:** meta — documentation tier. ALL sections preserved.



# ExpiryEventsConfiguration
<a name="API_ExpiryEventsConfiguration"></a>

Object containing expiration events options associated with an AWS account.

## Contents
<a name="API_ExpiryEventsConfiguration_Contents"></a>

**Note**  
In the following list, the required parameters are described first.

 ** DaysBeforeExpiry **   <a name="ACM-Type-ExpiryEventsConfiguration-DaysBeforeExpiry"></a>
Specifies the number of days prior to certificate expiration when ACM starts generating `EventBridge` events. ACM sends one event per day per certificate until the certificate expires. By default, accounts receive events starting 45 days before certificate expiration.  
Type: Integer  
Valid Range: Minimum value of 1.  
Required: No

## See Also
<a name="API_ExpiryEventsConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/acm-2015-12-08/ExpiryEventsConfiguration) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/acm-2015-12-08/ExpiryEventsConfiguration) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/acm-2015-12-08/ExpiryEventsConfiguration) 