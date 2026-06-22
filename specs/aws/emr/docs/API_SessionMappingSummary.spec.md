---
id: "@specs/aws/emr/docs/API_SessionMappingSummary"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS SessionMappingSummary"
status: active
depends_on:
  - "@specs/aws/emr/meta"
---

# SessionMappingSummary

> **source:** AWS Documentation
> **spec:id:** @specs/aws/emr/docs/API_SessionMappingSummary
> **target_lang:** meta — documentation tier. ALL sections preserved.



# SessionMappingSummary
<a name="API_SessionMappingSummary"></a>

Details for an Amazon EMR Studio session mapping. The details do not include the time the session mapping was last modified.

## Contents
<a name="API_SessionMappingSummary_Contents"></a>

 ** CreationTime **   <a name="EMR-Type-SessionMappingSummary-CreationTime"></a>
The time the session mapping was created.  
Type: Timestamp  
Required: No

 ** IdentityId **   <a name="EMR-Type-SessionMappingSummary-IdentityId"></a>
The globally unique identifier (GUID) of the user or group from the IAM Identity Center Identity Store.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 256.  
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`   
Required: No

 ** IdentityName **   <a name="EMR-Type-SessionMappingSummary-IdentityName"></a>
The name of the user or group. For more information, see [UserName](https://docs.aws.amazon.com/singlesignon/latest/IdentityStoreAPIReference/API_User.html#singlesignon-Type-User-UserName) and [DisplayName](https://docs.aws.amazon.com/singlesignon/latest/IdentityStoreAPIReference/API_Group.html#singlesignon-Type-Group-DisplayName) in the *IAM Identity Center Identity Store API Reference*.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 256.  
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`   
Required: No

 ** IdentityType **   <a name="EMR-Type-SessionMappingSummary-IdentityType"></a>
Specifies whether the identity mapped to the Amazon EMR Studio is a user or a group.  
Type: String  
Valid Values: `USER | GROUP`   
Required: No

 ** SessionPolicyArn **   <a name="EMR-Type-SessionMappingSummary-SessionPolicyArn"></a>
The Amazon Resource Name (ARN) of the session policy associated with the user or group.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 256.  
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`   
Required: No

 ** StudioId **   <a name="EMR-Type-SessionMappingSummary-StudioId"></a>
The ID of the Amazon EMR Studio.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 256.  
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`   
Required: No

## See Also
<a name="API_SessionMappingSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/elasticmapreduce-2009-03-31/SessionMappingSummary) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/elasticmapreduce-2009-03-31/SessionMappingSummary) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/elasticmapreduce-2009-03-31/SessionMappingSummary) 