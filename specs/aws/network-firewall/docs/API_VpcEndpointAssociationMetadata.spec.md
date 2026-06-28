---
id: "@specs/aws/network-firewall/docs/API_VpcEndpointAssociationMetadata"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS VpcEndpointAssociationMetadata"
status: active
depends_on:
  - "@specs/aws/network-firewall/meta"
---

# VpcEndpointAssociationMetadata

> **source:** AWS Documentation
> **spec:id:** @specs/aws/network-firewall/docs/API_VpcEndpointAssociationMetadata
> **target_lang:** meta — documentation tier. ALL sections preserved.



# VpcEndpointAssociationMetadata
<a name="API_VpcEndpointAssociationMetadata"></a>

High-level information about a VPC endpoint association, returned by `ListVpcEndpointAssociations`. You can use the information provided in the metadata to retrieve and manage a VPC endpoint association.

## Contents
<a name="API_VpcEndpointAssociationMetadata_Contents"></a>

 ** VpcEndpointAssociationArn **   <a name="networkfirewall-Type-VpcEndpointAssociationMetadata-VpcEndpointAssociationArn"></a>
The Amazon Resource Name (ARN) of a VPC endpoint association.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 256.  
Pattern: `^arn:aws.*`   
Required: No

## See Also
<a name="API_VpcEndpointAssociationMetadata_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/network-firewall-2020-11-12/VpcEndpointAssociationMetadata) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/network-firewall-2020-11-12/VpcEndpointAssociationMetadata) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/network-firewall-2020-11-12/VpcEndpointAssociationMetadata) 