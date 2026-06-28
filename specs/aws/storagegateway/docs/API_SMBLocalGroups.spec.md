---
id: "@specs/aws/storagegateway/docs/API_SMBLocalGroups"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS SMBLocalGroups"
status: active
depends_on:
  - "@specs/aws/storagegateway/meta"
---

# SMBLocalGroups

> **source:** AWS Documentation
> **spec:id:** @specs/aws/storagegateway/docs/API_SMBLocalGroups
> **target_lang:** meta — documentation tier. ALL sections preserved.



# SMBLocalGroups
<a name="API_SMBLocalGroups"></a>

A list of Active Directory users and groups that have special permissions for SMB file shares on the gateway.

## Contents
<a name="API_SMBLocalGroups_Contents"></a>

 ** GatewayAdmins **   <a name="StorageGateway-Type-SMBLocalGroups-GatewayAdmins"></a>
A list of Active Directory users and groups that have local Gateway Admin permissions. Acceptable formats include: `DOMAIN\User1`, `user1`, `DOMAIN\group1`, and `group1`.  
Gateway Admins can use the Shared Folders Microsoft Management Console snap-in to force-close files that are open and locked.  
Type: Array of strings  
Array Members: Minimum number of 0 items. Maximum number of 100 items.  
Length Constraints: Minimum length of 1. Maximum length of 64.  
Required: No

## See Also
<a name="API_SMBLocalGroups_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/storagegateway-2013-06-30/SMBLocalGroups) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/storagegateway-2013-06-30/SMBLocalGroups) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/storagegateway-2013-06-30/SMBLocalGroups) 