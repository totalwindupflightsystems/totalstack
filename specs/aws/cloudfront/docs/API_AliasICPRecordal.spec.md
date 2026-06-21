---
id: "@specs/aws/cloudfront/docs/API_AliasICPRecordal"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS AliasICPRecordal"
status: active
depends_on:
  - "@specs/aws/cloudfront/meta"
---

# AliasICPRecordal

> **source:** AWS Documentation
> **spec:id:** @specs/aws/cloudfront/docs/API_AliasICPRecordal
> **target_lang:** meta — documentation tier. ALL sections preserved.



# AliasICPRecordal
<a name="API_AliasICPRecordal"></a>

 AWS services in China customers must file for an Internet Content Provider (ICP) recordal if they want to serve content publicly on an alternate domain name, also known as a CNAME, that they've added to CloudFront. AliasICPRecordal provides the ICP recordal status for CNAMEs associated with distributions. The status is returned in the CloudFront response; you can't configure it yourself.

For more information about ICP recordals, see [ Signup, Accounts, and Credentials](https://docs.amazonaws.cn/en_us/aws/latest/userguide/accounts-and-credentials.html) in *Getting Started with AWS services in China*.

## Contents
<a name="API_AliasICPRecordal_Contents"></a>

 ** CNAME **   <a name="cloudfront-Type-AliasICPRecordal-CNAME"></a>
A domain name associated with a distribution.  
Type: String  
Required: No

 ** ICPRecordalStatus **   <a name="cloudfront-Type-AliasICPRecordal-ICPRecordalStatus"></a>
The Internet Content Provider (ICP) recordal status for a CNAME. The ICPRecordalStatus is set to APPROVED for all CNAMEs (aliases) in AWS Regions outside of China.  
The status values returned are the following:  
+  **APPROVED** indicates that the associated CNAME has a valid ICP recordal number. Multiple CNAMEs can be associated with a distribution, and CNAMEs can correspond to different ICP recordals. To be marked as APPROVED, that is, valid to use with the China Regions, a CNAME must have one ICP recordal number associated with it.
+  **SUSPENDED** indicates that the associated CNAME does not have a valid ICP recordal number.
+  **PENDING** indicates that CloudFront can't determine the ICP recordal status of the CNAME associated with the distribution because there was an error in trying to determine the status. You can try again to see if the error is resolved in which case CloudFront returns an APPROVED or SUSPENDED status.
Type: String  
Valid Values: `APPROVED | SUSPENDED | PENDING`   
Required: No

## See Also
<a name="API_AliasICPRecordal_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cloudfront-2020-05-31/AliasICPRecordal) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudfront-2020-05-31/AliasICPRecordal) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudfront-2020-05-31/AliasICPRecordal) 