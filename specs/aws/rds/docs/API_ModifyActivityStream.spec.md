---
id: "@specs/aws/rds/docs/API_ModifyActivityStream"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS ModifyActivityStream"
status: active
depends_on:
  - "@specs/aws/rds/meta"
---

# ModifyActivityStream

> **source:** AWS Documentation
> **spec:id:** @specs/aws/rds/docs/API_ModifyActivityStream
> **target_lang:** meta — documentation tier. ALL sections preserved.



# ModifyActivityStream
<a name="API_ModifyActivityStream"></a>

Changes the audit policy state of a database activity stream to either locked (default) or unlocked. A locked policy is read-only, whereas an unlocked policy is read/write. If your activity stream is started and locked, you can unlock it, customize your audit policy, and then lock your activity stream. Restarting the activity stream isn't required. For more information, see [ Modifying a database activity stream](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/DBActivityStreams.Modifying.html) in the *Amazon RDS User Guide*. 

This operation is supported for RDS for Oracle and Microsoft SQL Server.

## Request Parameters
<a name="API_ModifyActivityStream_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 ** AuditPolicyState **   
The audit policy state. When a policy is unlocked, it is read/write. When it is locked, it is read-only. You can edit your audit policy only when the activity stream is unlocked or stopped.  
Type: String  
Valid Values: `locked | unlocked`   
Required: No

 ** ResourceArn **   
The Amazon Resource Name (ARN) of the RDS for Oracle or Microsoft SQL Server DB instance. For example, `arn:aws:rds:us-east-1:12345667890:db:my-orcl-db`.  
Type: String  
Required: No

## Response Elements
<a name="API_ModifyActivityStream_ResponseElements"></a>

The following elements are returned by the service.

 ** EngineNativeAuditFieldsIncluded **   
Indicates whether engine-native audit fields are included in the database activity stream.  
Type: Boolean

 ** KinesisStreamName **   
The name of the Amazon Kinesis data stream to be used for the database activity stream.  
Type: String

 ** KmsKeyId **   
The AWS KMS key identifier for encryption of messages in the database activity stream.  
Type: String

 ** Mode **   
The mode of the database activity stream.  
Type: String  
Valid Values: `sync | async` 

 ** PolicyStatus **   
The status of the modification to the policy state of the database activity stream.  
Type: String  
Valid Values: `locked | unlocked | locking-policy | unlocking-policy` 

 ** Status **   
The status of the modification to the database activity stream.  
Type: String  
Valid Values: `stopped | starting | started | stopping` 

## Errors
<a name="API_ModifyActivityStream_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** DBInstanceNotFound **   
 `DBInstanceIdentifier` doesn't refer to an existing DB instance.  
HTTP Status Code: 404

 ** InvalidDBInstanceState **   
The DB instance isn't in a valid state.  
HTTP Status Code: 400

 ** ResourceNotFoundFault **   
The specified resource ID was not found.  
HTTP Status Code: 404

## See Also
<a name="API_ModifyActivityStream_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/rds-2014-10-31/ModifyActivityStream) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/rds-2014-10-31/ModifyActivityStream) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/rds-2014-10-31/ModifyActivityStream) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/rds-2014-10-31/ModifyActivityStream) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/rds-2014-10-31/ModifyActivityStream) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/rds-2014-10-31/ModifyActivityStream) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/rds-2014-10-31/ModifyActivityStream) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/rds-2014-10-31/ModifyActivityStream) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/rds-2014-10-31/ModifyActivityStream) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/rds-2014-10-31/ModifyActivityStream) 