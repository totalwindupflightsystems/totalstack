---
id: "@specs/aws/redshift/docs/API_EnableLogging"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS EnableLogging"
status: active
depends_on:
  - "@specs/aws/redshift/meta"
---

# EnableLogging

> **source:** AWS Documentation
> **spec:id:** @specs/aws/redshift/docs/API_EnableLogging
> **target_lang:** meta — documentation tier. ALL sections preserved.



# EnableLogging
<a name="API_EnableLogging"></a>

Starts logging information, such as queries and connection attempts, for the specified Amazon Redshift cluster.

## Request Parameters
<a name="API_EnableLogging_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 ** ClusterIdentifier **   
The identifier of the cluster on which logging is to be started.  
Example: `examplecluster`   
Type: String  
Length Constraints: Maximum length of 2147483647.  
Required: Yes

 ** BucketName **   
The name of an existing S3 bucket where the log files are to be stored.  
Constraints:  
+ Must be in the same region as the cluster
+ The cluster must have read bucket and put object permissions
Type: String  
Length Constraints: Maximum length of 2147483647.  
Required: No

 ** LogDestinationType **   
The log destination type. An enum with possible values of `s3` and `cloudwatch`.  
Type: String  
Valid Values: `s3 | cloudwatch`   
Required: No

 **LogExports.member.N**   
The collection of exported log types. Possible values are `connectionlog`, `useractivitylog`, and `userlog`.  
Type: Array of strings  
Length Constraints: Maximum length of 2147483647.  
Required: No

 ** S3KeyPrefix **   
The prefix applied to the log file names.  
Valid characters are any letter from any language, any whitespace character, any numeric character, and the following characters: underscore (`_`), period (`.`), colon (`:`), slash (`/`), equal (`=`), plus (`+`), backslash (`\`), hyphen (`-`), at symbol (`@`).  
Type: String  
Length Constraints: Maximum length of 256.  
Pattern: `[\p{L}\p{Z}\p{N}_.:/=+\-@]*`   
Required: No

## Response Elements
<a name="API_EnableLogging_ResponseElements"></a>

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
<a name="API_EnableLogging_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** BucketNotFoundFault **   
Could not find the specified S3 bucket.  
HTTP Status Code: 400

 ** ClusterNotFound **   
The `ClusterIdentifier` parameter does not refer to an existing cluster.   
HTTP Status Code: 404

 ** InsufficientS3BucketPolicyFault **   
The cluster does not have read bucket or put object permissions on the S3 bucket specified when enabling logging.  
HTTP Status Code: 400

 ** InvalidClusterState **   
The specified cluster is not in the `available` state.   
HTTP Status Code: 400

 ** InvalidS3BucketNameFault **   
The S3 bucket name is invalid. For more information about naming rules, go to [Bucket Restrictions and Limitations](https://docs.aws.amazon.com/AmazonS3/latest/dev/BucketRestrictions.html) in the Amazon Simple Storage Service (S3) Developer Guide.  
HTTP Status Code: 400

 ** InvalidS3KeyPrefixFault **   
The string specified for the logging S3 key prefix does not comply with the documented constraints.  
HTTP Status Code: 400

 ** UnsupportedOperation **   
The requested operation isn't supported.  
HTTP Status Code: 400

## See Also
<a name="API_EnableLogging_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/redshift-2012-12-01/EnableLogging) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/redshift-2012-12-01/EnableLogging) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/redshift-2012-12-01/EnableLogging) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/redshift-2012-12-01/EnableLogging) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/redshift-2012-12-01/EnableLogging) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/redshift-2012-12-01/EnableLogging) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/redshift-2012-12-01/EnableLogging) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/redshift-2012-12-01/EnableLogging) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/redshift-2012-12-01/EnableLogging) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/redshift-2012-12-01/EnableLogging) 