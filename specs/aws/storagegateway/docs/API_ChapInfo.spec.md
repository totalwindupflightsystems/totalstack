---
id: "@specs/aws/storagegateway/docs/API_ChapInfo"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS ChapInfo"
status: active
depends_on:
  - "@specs/aws/storagegateway/meta"
---

# ChapInfo

> **source:** AWS Documentation
> **spec:id:** @specs/aws/storagegateway/docs/API_ChapInfo
> **target_lang:** meta — documentation tier. ALL sections preserved.



# ChapInfo
<a name="API_ChapInfo"></a>

Describes Challenge-Handshake Authentication Protocol (CHAP) information that supports authentication between your gateway and iSCSI initiators.

## Contents
<a name="API_ChapInfo_Contents"></a>

 ** InitiatorName **   <a name="StorageGateway-Type-ChapInfo-InitiatorName"></a>
The iSCSI initiator that connects to the target.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 255.  
Pattern: `[0-9a-z:.-]+`   
Required: No

 ** SecretToAuthenticateInitiator **   <a name="StorageGateway-Type-ChapInfo-SecretToAuthenticateInitiator"></a>
The secret key that the initiator (for example, the Windows client) must provide to participate in mutual CHAP with the target.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 100.  
Required: No

 ** SecretToAuthenticateTarget **   <a name="StorageGateway-Type-ChapInfo-SecretToAuthenticateTarget"></a>
The secret key that the target must provide to participate in mutual CHAP with the initiator (e.g., Windows client).  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 100.  
Required: No

 ** TargetARN **   <a name="StorageGateway-Type-ChapInfo-TargetARN"></a>
The Amazon Resource Name (ARN) of the volume.  
Valid Values: 50 to 500 lowercase letters, numbers, periods (.), and hyphens (-).  
Type: String  
Length Constraints: Minimum length of 50. Maximum length of 800.  
Required: No

## See Also
<a name="API_ChapInfo_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/storagegateway-2013-06-30/ChapInfo) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/storagegateway-2013-06-30/ChapInfo) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/storagegateway-2013-06-30/ChapInfo) 