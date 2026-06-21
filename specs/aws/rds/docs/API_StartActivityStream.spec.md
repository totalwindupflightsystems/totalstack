---
id: "@specs/aws/rds/docs/API_StartActivityStream"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS StartActivityStream"
status: active
depends_on:
  - "@specs/aws/rds/meta"
---

# StartActivityStream

> **source:** AWS Documentation
> **spec:id:** @specs/aws/rds/docs/API_StartActivityStream
> **target_lang:** meta — documentation tier. ALL sections preserved.



# StartActivityStream
<a name="API_StartActivityStream"></a>

Starts a database activity stream to monitor activity on the database. For more information, see [ Monitoring Amazon Aurora with Database Activity Streams](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/DBActivityStreams.html) in the *Amazon Aurora User Guide* or [ Monitoring Amazon RDS with Database Activity Streams](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/DBActivityStreams.html) in the *Amazon RDS User Guide*.

## Request Parameters
<a name="API_StartActivityStream_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 ** KmsKeyId **   
The AWS KMS key identifier for encrypting messages in the database activity stream. The AWS KMS key identifier is the key ARN, key ID, alias ARN, or alias name for the KMS key.  
Type: String  
Required: Yes

 ** Mode **   
Specifies the mode of the database activity stream. Database events such as a change or access generate an activity stream event. The database session can handle these events either synchronously or asynchronously.  
Type: String  
Valid Values: `sync | async`   
Required: Yes

 ** ResourceArn **   
The Amazon Resource Name (ARN) of the DB cluster, for example, `arn:aws:rds:us-east-1:12345667890:cluster:das-cluster`.  
Type: String  
Required: Yes

 ** ApplyImmediately **   
Specifies whether or not the database activity stream is to start as soon as possible, regardless of the maintenance window for the database.  
Type: Boolean  
Required: No

 ** EngineNativeAuditFieldsIncluded **   
Specifies whether the database activity stream includes engine-native audit fields. This option applies to an Oracle or Microsoft SQL Server DB instance. By default, no engine-native audit fields are included.  
Type: Boolean  
Required: No

## Response Elements
<a name="API_StartActivityStream_ResponseElements"></a>

The following elements are returned by the service.

 ** ApplyImmediately **   
Indicates whether or not the database activity stream will start as soon as possible, regardless of the maintenance window for the database.  
Type: Boolean

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

 ** Status **   
The status of the database activity stream.  
Type: String  
Valid Values: `stopped | starting | started | stopping` 

## Errors
<a name="API_StartActivityStream_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** DBClusterNotFoundFault **   
 `DBClusterIdentifier` doesn't refer to an existing DB cluster.  
HTTP Status Code: 404

 ** DBInstanceNotFound **   
 `DBInstanceIdentifier` doesn't refer to an existing DB instance.  
HTTP Status Code: 404

 ** InvalidDBClusterStateFault **   
The requested operation can't be performed while the cluster is in this state.  
HTTP Status Code: 400

 ** InvalidDBInstanceState **   
The DB instance isn't in a valid state.  
HTTP Status Code: 400

 ** KMSKeyNotAccessibleFault **   
An error occurred accessing an AWS KMS key.  
HTTP Status Code: 400

 ** ResourceNotFoundFault **   
The specified resource ID was not found.  
HTTP Status Code: 404

## See Also
<a name="API_StartActivityStream_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/rds-2014-10-31/StartActivityStream) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/rds-2014-10-31/StartActivityStream) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/rds-2014-10-31/StartActivityStream) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/rds-2014-10-31/StartActivityStream) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/rds-2014-10-31/StartActivityStream) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/rds-2014-10-31/StartActivityStream) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/rds-2014-10-31/StartActivityStream) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/rds-2014-10-31/StartActivityStream) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/rds-2014-10-31/StartActivityStream) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/rds-2014-10-31/StartActivityStream) 