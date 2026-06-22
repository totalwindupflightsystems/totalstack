---
id: "@specs/aws/sesv2/docs/API_DeliveryOptions"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS DeliveryOptions"
status: active
depends_on:
  - "@specs/aws/sesv2/meta"
---

# DeliveryOptions

> **source:** AWS Documentation
> **spec:id:** @specs/aws/sesv2/docs/API_DeliveryOptions
> **target_lang:** meta — documentation tier. ALL sections preserved.



# DeliveryOptions
<a name="API_DeliveryOptions"></a>

Used to associate a configuration set with a dedicated IP pool.

## Contents
<a name="API_DeliveryOptions_Contents"></a>

 ** MaxDeliverySeconds **   <a name="SES-Type-DeliveryOptions-MaxDeliverySeconds"></a>
The maximum amount of time, in seconds, that Amazon SES API v2 will attempt delivery of email. If specified, the value must greater than or equal to 300 seconds (5 minutes) and less than or equal to 50400 seconds (840 minutes).   
Type: Long  
Valid Range: Minimum value of 300. Maximum value of 50400.  
Required: No

 ** SendingPoolName **   <a name="SES-Type-DeliveryOptions-SendingPoolName"></a>
The name of the dedicated IP pool to associate with the configuration set.  
Type: String  
Required: No

 ** TlsPolicy **   <a name="SES-Type-DeliveryOptions-TlsPolicy"></a>
Specifies whether messages that use the configuration set are required to use Transport Layer Security (TLS). If the value is `Require`, messages are only delivered if a TLS connection can be established. If the value is `Optional`, messages can be delivered in plain text if a TLS connection can't be established.  
Type: String  
Valid Values: `REQUIRE | OPTIONAL`   
Required: No

## See Also
<a name="API_DeliveryOptions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sesv2-2019-09-27/DeliveryOptions) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sesv2-2019-09-27/DeliveryOptions) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sesv2-2019-09-27/DeliveryOptions) 