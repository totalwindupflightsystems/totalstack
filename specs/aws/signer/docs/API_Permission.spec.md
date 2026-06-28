---
id: "@specs/aws/signer/docs/API_Permission"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Permission"
status: active
depends_on:
  - "@specs/aws/signer/meta"
---

# Permission

> **source:** AWS Documentation
> **spec:id:** @specs/aws/signer/docs/API_Permission
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Permission
<a name="API_Permission"></a>

A cross-account permission for a signing profile.

## Contents
<a name="API_Permission_Contents"></a>

 ** action **   <a name="signer-Type-Permission-action"></a>
An AWS Signer action permitted as part of cross-account permissions.  
Type: String  
Required: No

 ** principal **   <a name="signer-Type-Permission-principal"></a>
The AWS principal that has been granted a cross-account permission.  
Type: String  
Required: No

 ** profileVersion **   <a name="signer-Type-Permission-profileVersion"></a>
The signing profile version that a permission applies to.  
Type: String  
Length Constraints: Fixed length of 10.  
Pattern: `^[a-zA-Z0-9]{10}$`   
Required: No

 ** statementId **   <a name="signer-Type-Permission-statementId"></a>
A unique identifier for a cross-account permission statement.  
Type: String  
Required: No

## See Also
<a name="API_Permission_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/signer-2017-08-25/Permission) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/signer-2017-08-25/Permission) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/signer-2017-08-25/Permission) 