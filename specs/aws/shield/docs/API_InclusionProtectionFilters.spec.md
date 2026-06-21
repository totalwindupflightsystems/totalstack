---
id: "@specs/aws/shield/docs/API_InclusionProtectionFilters"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS InclusionProtectionFilters"
status: active
depends_on:
  - "@specs/aws/shield/meta"
---

# InclusionProtectionFilters

> **source:** AWS Documentation
> **spec:id:** @specs/aws/shield/docs/API_InclusionProtectionFilters
> **target_lang:** meta — documentation tier. ALL sections preserved.



# InclusionProtectionFilters
<a name="API_InclusionProtectionFilters"></a>

Narrows the set of protections that the call retrieves. You can retrieve a single protection by providing its name or the ARN (Amazon Resource Name) of its protected resource. You can also retrieve all protections for a specific resource type. You can provide up to one criteria per filter type. Shield Advanced returns protections that exactly match all of the filter criteria that you provide.

## Contents
<a name="API_InclusionProtectionFilters_Contents"></a>

 ** ProtectionNames **   <a name="AWSShield-Type-InclusionProtectionFilters-ProtectionNames"></a>
The name of the protection that you want to retrieve.   
Type: Array of strings  
Array Members: Fixed number of 1 item.  
Length Constraints: Minimum length of 1. Maximum length of 128.  
Pattern: `[ a-zA-Z0-9_\\.\\-]*`   
Required: No

 ** ResourceArns **   <a name="AWSShield-Type-InclusionProtectionFilters-ResourceArns"></a>
The ARN (Amazon Resource Name) of the resource whose protection you want to retrieve.   
Type: Array of strings  
Array Members: Fixed number of 1 item.  
Length Constraints: Minimum length of 1. Maximum length of 2048.  
Pattern: `^arn:aws.*`   
Required: No

 ** ResourceTypes **   <a name="AWSShield-Type-InclusionProtectionFilters-ResourceTypes"></a>
The type of protected resource whose protections you want to retrieve.   
Type: Array of strings  
Array Members: Fixed number of 1 item.  
Valid Values: `CLOUDFRONT_DISTRIBUTION | ROUTE_53_HOSTED_ZONE | ELASTIC_IP_ALLOCATION | CLASSIC_LOAD_BALANCER | APPLICATION_LOAD_BALANCER | GLOBAL_ACCELERATOR`   
Required: No

## See Also
<a name="API_InclusionProtectionFilters_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/shield-2016-06-02/InclusionProtectionFilters) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/shield-2016-06-02/InclusionProtectionFilters) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/shield-2016-06-02/InclusionProtectionFilters) 