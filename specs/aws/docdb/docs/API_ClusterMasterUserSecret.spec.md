---
id: "@specs/aws/docdb/docs/API_ClusterMasterUserSecret"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS ClusterMasterUserSecret"
status: active
depends_on:
  - "@specs/aws/docdb/meta"
---

# ClusterMasterUserSecret

> **source:** AWS Documentation
> **spec:id:** @specs/aws/docdb/docs/API_ClusterMasterUserSecret
> **target_lang:** meta — documentation tier. ALL sections preserved.



# ClusterMasterUserSecret
<a name="API_ClusterMasterUserSecret"></a>

Contains the secret managed by Amazon DocumentDB in AWS Secrets Manager for the master user password.

## Contents
<a name="API_ClusterMasterUserSecret_Contents"></a>

**Note**  
In the following list, the required parameters are described first.

 ** KmsKeyId **   
The AWS KMS key identifier that is used to encrypt the secret.  
Type: String  
Required: No

 ** SecretArn **   
The Amazon Resource Name (ARN) of the secret.  
Type: String  
Required: No

 ** SecretStatus **   
The status of the secret.  
The possible status values include the following:  
+ creating - The secret is being created.
+ active - The secret is available for normal use and rotation.
+ rotating - The secret is being rotated.
+ impaired - The secret can be used to access database credentials, but it can't be rotated. A secret might have this status if, for example, permissions are changed so that Amazon DocumentDB can no longer access either the secret or the KMS key for the secret.

  When a secret has this status, you can correct the condition that caused the status. Alternatively, modify the instance to turn off automatic management of database credentials, and then modify the instance again to turn on automatic management of database credentials.
Type: String  
Required: No

## See Also
<a name="API_ClusterMasterUserSecret_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/docdb-2014-10-31/ClusterMasterUserSecret) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/docdb-2014-10-31/ClusterMasterUserSecret) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/docdb-2014-10-31/ClusterMasterUserSecret) 