---
id: "@specs/aws/storagegateway/docs/API_FileSystemAssociationSummary"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS FileSystemAssociationSummary"
status: active
depends_on:
  - "@specs/aws/storagegateway/meta"
---

# FileSystemAssociationSummary

> **source:** AWS Documentation
> **spec:id:** @specs/aws/storagegateway/docs/API_FileSystemAssociationSummary
> **target_lang:** meta — documentation tier. ALL sections preserved.



# FileSystemAssociationSummary
<a name="API_FileSystemAssociationSummary"></a>

Gets the summary returned by `ListFileSystemAssociation`, which is a summary of a created file system association.

## Contents
<a name="API_FileSystemAssociationSummary_Contents"></a>

 ** FileSystemAssociationARN **   <a name="StorageGateway-Type-FileSystemAssociationSummary-FileSystemAssociationARN"></a>
The Amazon Resource Name (ARN) of the file system association.  
Type: String  
Length Constraints: Minimum length of 50. Maximum length of 500.  
Required: No

 ** FileSystemAssociationId **   <a name="StorageGateway-Type-FileSystemAssociationSummary-FileSystemAssociationId"></a>
The ID of the file system association.  
Type: String  
Length Constraints: Minimum length of 10. Maximum length of 30.  
Required: No

 ** FileSystemAssociationStatus **   <a name="StorageGateway-Type-FileSystemAssociationSummary-FileSystemAssociationStatus"></a>
The status of the file share. Valid Values: `AVAILABLE` \| `CREATING` \| `DELETING` \| `FORCE_DELETING` \| `UPDATING` \| `ERROR`   
Type: String  
Length Constraints: Minimum length of 3. Maximum length of 50.  
Required: No

 ** GatewayARN **   <a name="StorageGateway-Type-FileSystemAssociationSummary-GatewayARN"></a>
The Amazon Resource Name (ARN) of the gateway. Use the [ListGateways](API_ListGateways.md) operation to return a list of gateways for your account and AWS Region.  
Type: String  
Length Constraints: Minimum length of 50. Maximum length of 500.  
Required: No

## See Also
<a name="API_FileSystemAssociationSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/storagegateway-2013-06-30/FileSystemAssociationSummary) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/storagegateway-2013-06-30/FileSystemAssociationSummary) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/storagegateway-2013-06-30/FileSystemAssociationSummary) 