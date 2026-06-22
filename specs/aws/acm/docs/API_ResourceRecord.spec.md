---
id: "@specs/aws/acm/docs/API_ResourceRecord"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS ResourceRecord"
status: active
depends_on:
  - "@specs/aws/acm/meta"
---

# ResourceRecord

> **source:** AWS Documentation
> **spec:id:** @specs/aws/acm/docs/API_ResourceRecord
> **target_lang:** meta — documentation tier. ALL sections preserved.



# ResourceRecord
<a name="API_ResourceRecord"></a>

Contains a DNS record value that you can use to validate ownership or control of a domain. This is used by the [DescribeCertificate](API_DescribeCertificate.md) action. 

## Contents
<a name="API_ResourceRecord_Contents"></a>

**Note**  
In the following list, the required parameters are described first.

 ** Name **   <a name="ACM-Type-ResourceRecord-Name"></a>
The name of the DNS record to create in your domain. This is supplied by ACM.  
Type: String  
Required: Yes

 ** Type **   <a name="ACM-Type-ResourceRecord-Type"></a>
The type of DNS record. Currently this can be `CNAME`.  
Type: String  
Valid Values: `CNAME`   
Required: Yes

 ** Value **   <a name="ACM-Type-ResourceRecord-Value"></a>
The value of the CNAME record to add to your DNS database. This is supplied by ACM.  
Type: String  
Required: Yes

## See Also
<a name="API_ResourceRecord_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/acm-2015-12-08/ResourceRecord) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/acm-2015-12-08/ResourceRecord) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/acm-2015-12-08/ResourceRecord) 