---
id: "@specs/aws/storagegateway/docs/API_FileShareInfo"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS FileShareInfo"
status: active
depends_on:
  - "@specs/aws/storagegateway/meta"
---

# FileShareInfo

> **source:** AWS Documentation
> **spec:id:** @specs/aws/storagegateway/docs/API_FileShareInfo
> **target_lang:** meta — documentation tier. ALL sections preserved.



# FileShareInfo
<a name="API_FileShareInfo"></a>

Describes a file share. Only supported S3 File Gateway.

## Contents
<a name="API_FileShareInfo_Contents"></a>

 ** FileShareARN **   <a name="StorageGateway-Type-FileShareInfo-FileShareARN"></a>
The Amazon Resource Name (ARN) of the file share.  
Type: String  
Length Constraints: Minimum length of 50. Maximum length of 500.  
Required: No

 ** FileShareId **   <a name="StorageGateway-Type-FileShareInfo-FileShareId"></a>
The ID of the file share.  
Type: String  
Length Constraints: Minimum length of 12. Maximum length of 30.  
Required: No

 ** FileShareStatus **   <a name="StorageGateway-Type-FileShareInfo-FileShareStatus"></a>
The status of the file share.  
Valid Values: `CREATING` \| `UPDATING` \| `AVAILABLE` \| `DELETING`   
Type: String  
Length Constraints: Minimum length of 3. Maximum length of 50.  
Required: No

 ** FileShareType **   <a name="StorageGateway-Type-FileShareInfo-FileShareType"></a>
The type of the file share.  
Type: String  
Valid Values: `NFS | SMB`   
Required: No

 ** GatewayARN **   <a name="StorageGateway-Type-FileShareInfo-GatewayARN"></a>
The Amazon Resource Name (ARN) of the gateway. Use the [ListGateways](API_ListGateways.md) operation to return a list of gateways for your account and AWS Region.  
Type: String  
Length Constraints: Minimum length of 50. Maximum length of 500.  
Required: No

## See Also
<a name="API_FileShareInfo_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/storagegateway-2013-06-30/FileShareInfo) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/storagegateway-2013-06-30/FileShareInfo) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/storagegateway-2013-06-30/FileShareInfo) 