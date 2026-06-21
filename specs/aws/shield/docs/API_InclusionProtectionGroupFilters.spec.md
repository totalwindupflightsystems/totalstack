---
id: "@specs/aws/shield/docs/API_InclusionProtectionGroupFilters"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS InclusionProtectionGroupFilters"
status: active
depends_on:
  - "@specs/aws/shield/meta"
---

# InclusionProtectionGroupFilters

> **source:** AWS Documentation
> **spec:id:** @specs/aws/shield/docs/API_InclusionProtectionGroupFilters
> **target_lang:** meta — documentation tier. ALL sections preserved.



# InclusionProtectionGroupFilters
<a name="API_InclusionProtectionGroupFilters"></a>

Narrows the set of protection groups that the call retrieves. You can retrieve a single protection group by its name and you can retrieve all protection groups that are configured with a specific pattern, aggregation, or resource type. You can provide up to one criteria per filter type. Shield Advanced returns the protection groups that exactly match all of the search criteria that you provide.

## Contents
<a name="API_InclusionProtectionGroupFilters_Contents"></a>

 ** Aggregations **   <a name="AWSShield-Type-InclusionProtectionGroupFilters-Aggregations"></a>
The aggregation setting of the protection groups that you want to retrieve.   
Type: Array of strings  
Array Members: Fixed number of 1 item.  
Valid Values: `SUM | MEAN | MAX`   
Required: No

 ** Patterns **   <a name="AWSShield-Type-InclusionProtectionGroupFilters-Patterns"></a>
The pattern specification of the protection groups that you want to retrieve.   
Type: Array of strings  
Array Members: Fixed number of 1 item.  
Valid Values: `ALL | ARBITRARY | BY_RESOURCE_TYPE`   
Required: No

 ** ProtectionGroupIds **   <a name="AWSShield-Type-InclusionProtectionGroupFilters-ProtectionGroupIds"></a>
The ID of the protection group that you want to retrieve.   
Type: Array of strings  
Array Members: Fixed number of 1 item.  
Length Constraints: Minimum length of 1. Maximum length of 36.  
Pattern: `[a-zA-Z0-9\\-]*`   
Required: No

 ** ResourceTypes **   <a name="AWSShield-Type-InclusionProtectionGroupFilters-ResourceTypes"></a>
The resource type configuration of the protection groups that you want to retrieve. In the protection group configuration, you specify the resource type when you set the group's `Pattern` to `BY_RESOURCE_TYPE`.   
Type: Array of strings  
Array Members: Fixed number of 1 item.  
Valid Values: `CLOUDFRONT_DISTRIBUTION | ROUTE_53_HOSTED_ZONE | ELASTIC_IP_ALLOCATION | CLASSIC_LOAD_BALANCER | APPLICATION_LOAD_BALANCER | GLOBAL_ACCELERATOR`   
Required: No

## See Also
<a name="API_InclusionProtectionGroupFilters_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/shield-2016-06-02/InclusionProtectionGroupFilters) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/shield-2016-06-02/InclusionProtectionGroupFilters) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/shield-2016-06-02/InclusionProtectionGroupFilters) 