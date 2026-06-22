---
id: "@specs/aws/redshift/docs/API_DescribeLoggingStatus"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS DescribeLoggingStatus"
status: active
depends_on:
  - "@specs/aws/redshift/meta"
---

# DescribeLoggingStatus

> **source:** AWS Documentation
> **spec:id:** @specs/aws/redshift/docs/API_DescribeLoggingStatus
> **target_lang:** meta — documentation tier. ALL sections preserved.



# DescribeLoggingStatus
<a name="API_DescribeLoggingStatus"></a>

Describes whether information, such as queries and connection attempts, is being logged for the specified Amazon Redshift cluster.

## Request Parameters
<a name="API_DescribeLoggingStatus_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 ** ClusterIdentifier **   
The identifier of the cluster from which to get the logging status.  
Example: `examplecluster`   
Type: String  
Length Constraints: Maximum length of 2147483647.  
Required: Yes

## Response Elements
<a name="API_DescribeLoggingStatus_ResponseElements"></a>

The following elements are returned by the service.

 ** BucketName **   
The name of the S3 bucket where the log files are stored.  
Type: String  
Length Constraints: Maximum length of 2147483647.

 ** LastFailureMessage **   
The message indicating that logs failed to be delivered.  
Type: String  
Length Constraints: Maximum length of 2147483647.

 ** LastFailureTime **   
The last time when logs failed to be delivered.  
Type: Timestamp

 ** LastSuccessfulDeliveryTime **   
The last time that logs were delivered.  
Type: Timestamp

 ** LogDestinationType **   
The log destination type. An enum with possible values of `s3` and `cloudwatch`.  
Type: String  
Valid Values: `s3 | cloudwatch` 

 **LogExports.member.N**   
The collection of exported log types. Possible values are `connectionlog`, `useractivitylog`, and `userlog`.  
Type: Array of strings  
Length Constraints: Maximum length of 2147483647.

 ** LoggingEnabled **   
 `true` if logging is on, `false` if logging is off.  
Type: Boolean

 ** S3KeyPrefix **   
The prefix applied to the log file names.  
Type: String  
Length Constraints: Maximum length of 256.  
Pattern: `[\p{L}\p{Z}\p{N}_.:/=+\-@]*` 

## Errors
<a name="API_DescribeLoggingStatus_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ClusterNotFound **   
The `ClusterIdentifier` parameter does not refer to an existing cluster.   
HTTP Status Code: 404

 ** UnsupportedOperation **   
The requested operation isn't supported.  
HTTP Status Code: 400

## Examples
<a name="API_DescribeLoggingStatus_Examples"></a>

### Example
<a name="API_DescribeLoggingStatus_Example_1"></a>

This example illustrates one usage of DescribeLoggingStatus.

#### Sample Request
<a name="API_DescribeLoggingStatus_Example_1_Request"></a>

```
https://redshift.us-east-2.amazonaws.com/
       ?Action=DescribeLoggingStatus
&ClusterIdentifier=mycluster
&SignatureMethod=HmacSHA256&SignatureVersion=4
&Version=2012-12-01
&X-Amz-Algorithm=AWS4-HMAC-SHA256
&X-Amz-Credential=AKIAIOSFODNN7EXAMPLE/20190817/us-east-2/redshift/aws4_request
&X-Amz-Date=20190825T160000Z
&X-Amz-SignedHeaders=content-type;host;user-agent;x-amz-content-sha256;x-amz-date
&X-Amz-Signature=0aa1234bb5cc678ddddd901ee2ff3aa45678b90c12d345e6ff789012345a6b7b
```

#### Sample Response
<a name="API_DescribeLoggingStatus_Example_1_Response"></a>

```
<DescribeLoggingStatusResponse xmlns="http://redshift.amazonaws.com/doc/2012-12-01/">
  <DescribeLoggingStatusResult>
    <LoggingEnabled>false</LoggingEnabled>
  </DescribeLoggingStatusResult>
  <ResponseMetadata>
    <RequestId>9ed2dcec-28cc-11ea-b6af-7126da6f11af</RequestId>
  </ResponseMetadata>
</DescribeLoggingStatusResponse>
```

## See Also
<a name="API_DescribeLoggingStatus_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/redshift-2012-12-01/DescribeLoggingStatus) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/redshift-2012-12-01/DescribeLoggingStatus) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/redshift-2012-12-01/DescribeLoggingStatus) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/redshift-2012-12-01/DescribeLoggingStatus) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/redshift-2012-12-01/DescribeLoggingStatus) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/redshift-2012-12-01/DescribeLoggingStatus) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/redshift-2012-12-01/DescribeLoggingStatus) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/redshift-2012-12-01/DescribeLoggingStatus) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/redshift-2012-12-01/DescribeLoggingStatus) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/redshift-2012-12-01/DescribeLoggingStatus) 