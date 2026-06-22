---
id: "@specs/aws/sesv2/docs/API_SOARecord"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS SOARecord"
status: active
depends_on:
  - "@specs/aws/sesv2/meta"
---

# SOARecord

> **source:** AWS Documentation
> **spec:id:** @specs/aws/sesv2/docs/API_SOARecord
> **target_lang:** meta — documentation tier. ALL sections preserved.



# SOARecord
<a name="API_SOARecord"></a>

An object that contains information about the start of authority (SOA) record associated with the identity.

## Contents
<a name="API_SOARecord_Contents"></a>

 ** AdminEmail **   <a name="SES-Type-SOARecord-AdminEmail"></a>
Administrative contact email from the SOA record.  
Type: String  
Required: No

 ** PrimaryNameServer **   <a name="SES-Type-SOARecord-PrimaryNameServer"></a>
Primary name server specified in the SOA record.  
Type: String  
Required: No

 ** SerialNumber **   <a name="SES-Type-SOARecord-SerialNumber"></a>
Serial number from the SOA record.  
Type: Long  
Required: No

## See Also
<a name="API_SOARecord_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sesv2-2019-09-27/SOARecord) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sesv2-2019-09-27/SOARecord) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sesv2-2019-09-27/SOARecord) 