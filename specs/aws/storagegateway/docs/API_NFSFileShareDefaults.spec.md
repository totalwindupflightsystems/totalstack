---
id: "@specs/aws/storagegateway/docs/API_NFSFileShareDefaults"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS NFSFileShareDefaults"
status: active
depends_on:
  - "@specs/aws/storagegateway/meta"
---

# NFSFileShareDefaults

> **source:** AWS Documentation
> **spec:id:** @specs/aws/storagegateway/docs/API_NFSFileShareDefaults
> **target_lang:** meta — documentation tier. ALL sections preserved.



# NFSFileShareDefaults
<a name="API_NFSFileShareDefaults"></a>

Describes Network File System (NFS) file share default values. Files and folders stored as Amazon S3 objects in S3 buckets don't, by default, have Unix file permissions assigned to them. Upon discovery in an S3 bucket by Storage Gateway, the S3 objects that represent files and folders are assigned these default Unix permissions. This operation is only supported for S3 File Gateways.

## Contents
<a name="API_NFSFileShareDefaults_Contents"></a>

 ** DirectoryMode **   <a name="StorageGateway-Type-NFSFileShareDefaults-DirectoryMode"></a>
The Unix directory mode in the form "nnnn". For example, `0666` represents the default access mode for all directories inside the file share. The default value is `0777`.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 4.  
Pattern: `^[0-7]{4}$`   
Required: No

 ** FileMode **   <a name="StorageGateway-Type-NFSFileShareDefaults-FileMode"></a>
The Unix file mode in the form "nnnn". For example, `0666` represents the default file mode inside the file share. The default value is `0666`.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 4.  
Pattern: `^[0-7]{4}$`   
Required: No

 ** GroupId **   <a name="StorageGateway-Type-NFSFileShareDefaults-GroupId"></a>
The default group ID for the file share (unless the files have another group ID specified). The default value is `nfsnobody`.  
Type: Long  
Valid Range: Minimum value of 0. Maximum value of 4294967294.  
Required: No

 ** OwnerId **   <a name="StorageGateway-Type-NFSFileShareDefaults-OwnerId"></a>
The default owner ID for files in the file share (unless the files have another owner ID specified). The default value is `nfsnobody`.  
Type: Long  
Valid Range: Minimum value of 0. Maximum value of 4294967294.  
Required: No

## See Also
<a name="API_NFSFileShareDefaults_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/storagegateway-2013-06-30/NFSFileShareDefaults) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/storagegateway-2013-06-30/NFSFileShareDefaults) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/storagegateway-2013-06-30/NFSFileShareDefaults) 