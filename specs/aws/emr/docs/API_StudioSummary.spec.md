---
id: "@specs/aws/emr/docs/API_StudioSummary"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS StudioSummary"
status: active
depends_on:
  - "@specs/aws/emr/meta"
---

# StudioSummary

> **source:** AWS Documentation
> **spec:id:** @specs/aws/emr/docs/API_StudioSummary
> **target_lang:** meta — documentation tier. ALL sections preserved.



# StudioSummary
<a name="API_StudioSummary"></a>

Details for an Amazon EMR Studio, including ID, Name, VPC, and Description. To fetch additional details such as subnets, IAM roles, security groups, and tags for the Studio, use the [DescribeStudio](API_DescribeStudio.md) API.

## Contents
<a name="API_StudioSummary_Contents"></a>

 ** AuthMode **   <a name="EMR-Type-StudioSummary-AuthMode"></a>
Specifies whether the Studio authenticates users using IAM or IAM Identity Center.  
Type: String  
Valid Values: `SSO | IAM`   
Required: No

 ** CreationTime **   <a name="EMR-Type-StudioSummary-CreationTime"></a>
The time when the Amazon EMR Studio was created.  
Type: Timestamp  
Required: No

 ** Description **   <a name="EMR-Type-StudioSummary-Description"></a>
The detailed description of the Amazon EMR Studio.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 256.  
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`   
Required: No

 ** Name **   <a name="EMR-Type-StudioSummary-Name"></a>
The name of the Amazon EMR Studio.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 256.  
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`   
Required: No

 ** StudioId **   <a name="EMR-Type-StudioSummary-StudioId"></a>
The ID of the Amazon EMR Studio.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 256.  
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`   
Required: No

 ** Url **   <a name="EMR-Type-StudioSummary-Url"></a>
The unique access URL of the Amazon EMR Studio.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 256.  
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`   
Required: No

 ** VpcId **   <a name="EMR-Type-StudioSummary-VpcId"></a>
The ID of the Virtual Private Cloud (Amazon VPC) associated with the Amazon EMR Studio.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 256.  
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`   
Required: No

## See Also
<a name="API_StudioSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/elasticmapreduce-2009-03-31/StudioSummary) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/elasticmapreduce-2009-03-31/StudioSummary) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/elasticmapreduce-2009-03-31/StudioSummary) 