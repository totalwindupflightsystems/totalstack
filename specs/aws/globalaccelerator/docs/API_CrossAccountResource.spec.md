---
id: "@specs/aws/globalaccelerator/docs/API_CrossAccountResource"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS CrossAccountResource"
status: active
depends_on:
  - "@specs/aws/globalaccelerator/meta"
---

# CrossAccountResource

> **source:** AWS Documentation
> **spec:id:** @specs/aws/globalaccelerator/docs/API_CrossAccountResource
> **target_lang:** meta — documentation tier. ALL sections preserved.



# CrossAccountResource
<a name="API_CrossAccountResource"></a>

An endpoint (AWS resource) or an IP address range, in CIDR format, that is listed in a cross-account attachment. A cross-account resource can be added to an accelerator by specified principals, which are also listed in the attachment.

For more information, see [ Working with cross-account attachments and resources in AWS Global Accelerator](https://docs.aws.amazon.com/global-accelerator/latest/dg/cross-account-resources.html) in the * AWS Global Accelerator Developer Guide*.

## Contents
<a name="API_CrossAccountResource_Contents"></a>

 ** AttachmentArn **   <a name="globalaccelerator-Type-CrossAccountResource-AttachmentArn"></a>
The Amazon Resource Name (ARN) of the cross-account attachment that specifies the resources (endpoints or CIDR range) that can be added to accelerators and principals that have permission to add them.  
Type: String  
Length Constraints: Maximum length of 255.  
Required: No

 ** Cidr **   <a name="globalaccelerator-Type-CrossAccountResource-Cidr"></a>
An IP address range, in CIDR format, that is specified as an AWS resource. The address must be provisioned and advertised in AWS Global Accelerator by following the bring your own IP address (BYOIP) process for Global Accelerator.  
 For more information, see [Bring your own IP addresses (BYOIP)](https://docs.aws.amazon.com/global-accelerator/latest/dg/using-byoip.html) in the AWS Global Accelerator Developer Guide.  
Type: String  
Length Constraints: Maximum length of 255.  
Required: No

 ** EndpointId **   <a name="globalaccelerator-Type-CrossAccountResource-EndpointId"></a>
The endpoint ID for the endpoint that is listed in a cross-account attachment and can be added to an accelerator by specified principals.  
Type: String  
Length Constraints: Maximum length of 255.  
Required: No

## See Also
<a name="API_CrossAccountResource_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/globalaccelerator-2018-08-08/CrossAccountResource) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/globalaccelerator-2018-08-08/CrossAccountResource) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/globalaccelerator-2018-08-08/CrossAccountResource) 