---
id: "@specs/aws/sesv2/docs/API_Bounce"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Bounce"
status: active
depends_on:
  - "@specs/aws/sesv2/meta"
---

# Bounce

> **source:** AWS Documentation
> **spec:id:** @specs/aws/sesv2/docs/API_Bounce
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Bounce
<a name="API_Bounce"></a>

Information about a `Bounce` event.

## Contents
<a name="API_Bounce_Contents"></a>

 ** BounceSubType **   <a name="SES-Type-Bounce-BounceSubType"></a>
The subtype of the bounce, as determined by SES.  
Type: String  
Required: No

 ** BounceType **   <a name="SES-Type-Bounce-BounceType"></a>
The type of the bounce, as determined by SES. Can be one of `UNDETERMINED`, `TRANSIENT`, or `PERMANENT`   
Type: String  
Valid Values: `UNDETERMINED | TRANSIENT | PERMANENT`   
Required: No

 ** DiagnosticCode **   <a name="SES-Type-Bounce-DiagnosticCode"></a>
The status code issued by the reporting Message Transfer Authority (MTA). This field only appears if a delivery status notification (DSN) was attached to the bounce and the `Diagnostic-Code` was provided in the DSN.   
Type: String  
Required: No

## See Also
<a name="API_Bounce_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sesv2-2019-09-27/Bounce) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sesv2-2019-09-27/Bounce) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sesv2-2019-09-27/Bounce) 