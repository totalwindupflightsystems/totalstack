---
id: "@specs/aws/cloudfront/docs/API_AnycastIpListSummary"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS AnycastIpListSummary"
status: active
depends_on:
  - "@specs/aws/cloudfront/meta"
---

# AnycastIpListSummary

> **source:** AWS Documentation
> **spec:id:** @specs/aws/cloudfront/docs/API_AnycastIpListSummary
> **target_lang:** meta — documentation tier. ALL sections preserved.



# AnycastIpListSummary
<a name="API_AnycastIpListSummary"></a>

An abbreviated version of the [AnycastIpList](API_AnycastIpList.md) structure. Omits the allocated static IP addresses ([AnycastIpList:AnycastIps](API_AnycastIpList.md#cloudfront-Type-AnycastIpList-AnycastIps)).

## Contents
<a name="API_AnycastIpListSummary_Contents"></a>

 ** Arn **   <a name="cloudfront-Type-AnycastIpListSummary-Arn"></a>
The Amazon Resource Name (ARN) of the Anycast static IP list.  
Type: String  
Required: Yes

 ** Id **   <a name="cloudfront-Type-AnycastIpListSummary-Id"></a>
The ID of the Anycast static IP list.  
Type: String  
Required: Yes

 ** IpCount **   <a name="cloudfront-Type-AnycastIpListSummary-IpCount"></a>
The number of IP addresses in the Anycast static IP list.  
Type: Integer  
Required: Yes

 ** LastModifiedTime **   <a name="cloudfront-Type-AnycastIpListSummary-LastModifiedTime"></a>
The last time the Anycast static IP list was modified.  
Type: Timestamp  
Required: Yes

 ** Name **   <a name="cloudfront-Type-AnycastIpListSummary-Name"></a>
The name of the Anycast static IP list.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 64.  
Pattern: `[a-zA-Z0-9-_]{1,64}`   
Required: Yes

 ** Status **   <a name="cloudfront-Type-AnycastIpListSummary-Status"></a>
The deployment status of the Anycast static IP list. Valid values: Deployed, Deploying, or Failed.  
Type: String  
Required: Yes

 ** ETag **   <a name="cloudfront-Type-AnycastIpListSummary-ETag"></a>
The current version (ETag value) of the Anycast static IP list.  
Type: String  
Required: No

 ** IpAddressType **   <a name="cloudfront-Type-AnycastIpListSummary-IpAddressType"></a>
The IP address type for the Anycast static IP list.  
Type: String  
Valid Values: `ipv4 | ipv6 | dualstack`   
Required: No

 ** IpamConfig **   <a name="cloudfront-Type-AnycastIpListSummary-IpamConfig"></a>
The IPAM configuration for the Anycast static IP list, that contains the quantity and list of IPAM CIDR configurations.  
Type: [IpamConfig](API_IpamConfig.md) object  
Required: No

## See Also
<a name="API_AnycastIpListSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cloudfront-2020-05-31/AnycastIpListSummary) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudfront-2020-05-31/AnycastIpListSummary) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudfront-2020-05-31/AnycastIpListSummary) 