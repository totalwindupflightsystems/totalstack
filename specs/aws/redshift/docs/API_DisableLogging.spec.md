---
id: "@specs/aws/redshift/docs/API_DisableLogging"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS DisableLogging"
status: active
depends_on:
  - "@specs/aws/redshift/meta"
---

# DisableLogging

> **source:** AWS Documentation
> **spec:id:** @specs/aws/redshift/docs/API_DisableLogging
> **target_lang:** meta — documentation tier. ALL sections preserved.



# DisableLogging
<a name="API_DisableLogging"></a>

Stops logging information, such as queries and connection attempts, for the specified Amazon Redshift cluster.

## Request Parameters
<a name="API_DisableLogging_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 ** ClusterIdentifier **   
The identifier of the cluster on which logging is to be stopped.  
Example: `examplecluster`   
Type: String  
Length Constraints: Maximum length of 2147483647.  
Required: Yes

## Response Elements
<a name="API_DisableLogging_ResponseElements"></a>

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
<a name="API_DisableLogging_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ClusterNotFound **   
The `ClusterIdentifier` parameter does not refer to an existing cluster.   
HTTP Status Code: 404

 ** InvalidClusterState **   
The specified cluster is not in the `available` state.   
HTTP Status Code: 400

 ** UnsupportedOperation **   
The requested operation isn't supported.  
HTTP Status Code: 400

## See Also
<a name="API_DisableLogging_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/redshift-2012-12-01/DisableLogging) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/redshift-2012-12-01/DisableLogging) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/redshift-2012-12-01/DisableLogging) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/redshift-2012-12-01/DisableLogging) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/redshift-2012-12-01/DisableLogging) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/redshift-2012-12-01/DisableLogging) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/redshift-2012-12-01/DisableLogging) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/redshift-2012-12-01/DisableLogging) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/redshift-2012-12-01/DisableLogging) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/redshift-2012-12-01/DisableLogging) 