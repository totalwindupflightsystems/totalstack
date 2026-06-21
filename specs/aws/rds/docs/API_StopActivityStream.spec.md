---
id: "@specs/aws/rds/docs/API_StopActivityStream"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS StopActivityStream"
status: active
depends_on:
  - "@specs/aws/rds/meta"
---

# StopActivityStream

> **source:** AWS Documentation
> **spec:id:** @specs/aws/rds/docs/API_StopActivityStream
> **target_lang:** meta — documentation tier. ALL sections preserved.



# StopActivityStream
<a name="API_StopActivityStream"></a>

Stops a database activity stream that was started using the AWS console, the `start-activity-stream` AWS CLI command, or the `StartActivityStream` operation.

For more information, see [ Monitoring Amazon Aurora with Database Activity Streams](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/DBActivityStreams.html) in the *Amazon Aurora User Guide* or [ Monitoring Amazon RDS with Database Activity Streams](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/DBActivityStreams.html) in the *Amazon RDS User Guide*.

## Request Parameters
<a name="API_StopActivityStream_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 ** ResourceArn **   
The Amazon Resource Name (ARN) of the DB cluster for the database activity stream. For example, `arn:aws:rds:us-east-1:12345667890:cluster:das-cluster`.  
Type: String  
Required: Yes

 ** ApplyImmediately **   
Specifies whether or not the database activity stream is to stop as soon as possible, regardless of the maintenance window for the database.  
Type: Boolean  
Required: No

## Response Elements
<a name="API_StopActivityStream_ResponseElements"></a>

The following elements are returned by the service.

 ** KinesisStreamName **   
The name of the Amazon Kinesis data stream used for the database activity stream.  
Type: String

 ** KmsKeyId **   
The AWS KMS key identifier used for encrypting messages in the database activity stream.  
The AWS KMS key identifier is the key ARN, key ID, alias ARN, or alias name for the KMS key.  
Type: String

 ** Status **   
The status of the database activity stream.  
Type: String  
Valid Values: `stopped | starting | started | stopping` 

## Errors
<a name="API_StopActivityStream_Errors"></a>

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

 ** ResourceNotFoundFault **   
The specified resource ID was not found.  
HTTP Status Code: 404

## See Also
<a name="API_StopActivityStream_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/rds-2014-10-31/StopActivityStream) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/rds-2014-10-31/StopActivityStream) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/rds-2014-10-31/StopActivityStream) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/rds-2014-10-31/StopActivityStream) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/rds-2014-10-31/StopActivityStream) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/rds-2014-10-31/StopActivityStream) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/rds-2014-10-31/StopActivityStream) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/rds-2014-10-31/StopActivityStream) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/rds-2014-10-31/StopActivityStream) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/rds-2014-10-31/StopActivityStream) 