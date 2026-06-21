---
id: "@specs/aws/cloudfront/docs/API_AnycastIpList"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS AnycastIpList"
status: active
depends_on:
  - "@specs/aws/cloudfront/meta"
---

# AnycastIpList

> **source:** AWS Documentation
> **spec:id:** @specs/aws/cloudfront/docs/API_AnycastIpList
> **target_lang:** meta — documentation tier. ALL sections preserved.



# AnycastIpList
<a name="API_AnycastIpList"></a>

An Anycast static IP list. For more information, see [Request Anycast static IPs to use for allowlisting](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/request-static-ips.html) in the *Amazon CloudFront Developer Guide*.

## Contents
<a name="API_AnycastIpList_Contents"></a>

 ** AnycastIps **   <a name="cloudfront-Type-AnycastIpList-AnycastIps"></a>
The static IP addresses that are allocated to the Anycast static IP list.  
Type: Array of strings  
Required: Yes

 ** Arn **   <a name="cloudfront-Type-AnycastIpList-Arn"></a>
The Amazon Resource Name (ARN) of the Anycast static IP list.  
Type: String  
Required: Yes

 ** Id **   <a name="cloudfront-Type-AnycastIpList-Id"></a>
The ID of the Anycast static IP list.  
Type: String  
Required: Yes

 ** IpCount **   <a name="cloudfront-Type-AnycastIpList-IpCount"></a>
The number of IP addresses in the Anycast static IP list.  
Type: Integer  
Required: Yes

 ** LastModifiedTime **   <a name="cloudfront-Type-AnycastIpList-LastModifiedTime"></a>
The last time the Anycast static IP list was modified.  
Type: Timestamp  
Required: Yes

 ** Name **   <a name="cloudfront-Type-AnycastIpList-Name"></a>
The name of the Anycast static IP list.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 64.  
Pattern: `[a-zA-Z0-9-_]{1,64}`   
Required: Yes

 ** Status **   <a name="cloudfront-Type-AnycastIpList-Status"></a>
The status of the Anycast static IP list. Valid values: `Deployed`, `Deploying`, or `Failed`.  
Type: String  
Required: Yes

 ** IpAddressType **   <a name="cloudfront-Type-AnycastIpList-IpAddressType"></a>
The IP address type for the Anycast static IP list.  
Type: String  
Valid Values: `ipv4 | ipv6 | dualstack`   
Required: No

 ** IpamConfig **   <a name="cloudfront-Type-AnycastIpList-IpamConfig"></a>
The IPAM configuration for the Anycast static IP list, that contains the quantity and list of IPAM CIDR configurations.  
Type: [IpamConfig](API_IpamConfig.md) object  
Required: No

## See Also
<a name="API_AnycastIpList_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cloudfront-2020-05-31/AnycastIpList) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudfront-2020-05-31/AnycastIpList) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudfront-2020-05-31/AnycastIpList) 