---
id: "@specs/aws/sesv2/docs/API_ResourceTenantMetadata"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS ResourceTenantMetadata"
status: active
depends_on:
  - "@specs/aws/sesv2/meta"
---

# ResourceTenantMetadata

> **source:** AWS Documentation
> **spec:id:** @specs/aws/sesv2/docs/API_ResourceTenantMetadata
> **target_lang:** meta — documentation tier. ALL sections preserved.



# ResourceTenantMetadata
<a name="API_ResourceTenantMetadata"></a>

A structure that contains information about a tenant associated with a resource.

## Contents
<a name="API_ResourceTenantMetadata_Contents"></a>

 ** AssociatedTimestamp **   <a name="SES-Type-ResourceTenantMetadata-AssociatedTimestamp"></a>
The date and time when the resource was associated with the tenant.  
Type: Timestamp  
Required: No

 ** ResourceArn **   <a name="SES-Type-ResourceTenantMetadata-ResourceArn"></a>
The Amazon Resource Name (ARN) of the resource.  
Type: String  
Length Constraints: Minimum length of 1.  
Required: No

 ** TenantId **   <a name="SES-Type-ResourceTenantMetadata-TenantId"></a>
A unique identifier for the tenant associated with the resource.  
Type: String  
Required: No

 ** TenantName **   <a name="SES-Type-ResourceTenantMetadata-TenantName"></a>
The name of the tenant associated with the resource.  
Type: String  
Length Constraints: Minimum length of 1.  
Required: No

## See Also
<a name="API_ResourceTenantMetadata_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sesv2-2019-09-27/ResourceTenantMetadata) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sesv2-2019-09-27/ResourceTenantMetadata) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sesv2-2019-09-27/ResourceTenantMetadata) 