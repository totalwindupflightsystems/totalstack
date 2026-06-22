---
id: "@specs/aws/redshift/docs/API_CreateIntegration"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS CreateIntegration"
status: active
depends_on:
  - "@specs/aws/redshift/meta"
---

# CreateIntegration

> **source:** AWS Documentation
> **spec:id:** @specs/aws/redshift/docs/API_CreateIntegration
> **target_lang:** meta — documentation tier. ALL sections preserved.



# CreateIntegration
<a name="API_CreateIntegration"></a>

Creates a zero-ETL integration or S3 event integration with Amazon Redshift.

## Request Parameters
<a name="API_CreateIntegration_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 ** IntegrationName **   
The name of the integration.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 63.  
Pattern: `^[a-zA-Z][a-zA-Z0-9]*(-[a-zA-Z0-9]+)*$`   
Required: Yes

 ** SourceArn **   
The Amazon Resource Name (ARN) of the database to use as the source for replication.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 255.  
Pattern: `^arn:aws[a-z\-]*:(s3|dynamodb):.*:.*:[a-zA-Z0-9._\-\/]+$`   
Required: Yes

 ** TargetArn **   
The Amazon Resource Name (ARN) of the Amazon Redshift data warehouse to use as the target for replication.  
Type: String  
Length Constraints: Minimum length of 20. Maximum length of 2048.  
Pattern: `^arn:aws[a-z\-]*:redshift(-serverless)?:[a-z0-9\-]+:[0-9]{12}:(namespace\/|namespace:)[a-z0-9\-]+$`   
Required: Yes

 **AdditionalEncryptionContext** AdditionalEncryptionContext.entry.N.key (key)AdditionalEncryptionContext.entry.N.value (value)  
An optional set of non-secret key–value pairs that contains additional contextual information about the data. For more information, see [Encryption context](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#encrypt_context) in the * AWS Key Management Service Developer Guide*.  
You can only include this parameter if you specify the `KMSKeyId` parameter.  
Type: String to string map  
Key Length Constraints: Maximum length of 2147483647.  
Value Length Constraints: Maximum length of 2147483647.  
Required: No

 ** Description **   
A description of the integration.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 1000.  
Pattern: `^.*$`   
Required: No

 ** KMSKeyId **   
An AWS Key Management Service (AWS KMS) key identifier for the key to use to encrypt the integration. If you don't specify an encryption key, the default AWS owned key is used.  
Type: String  
Length Constraints: Maximum length of 2147483647.  
Required: No

 **TagList.Tag.N**   
A list of tags.  
Type: Array of [Tag](API_Tag.md) objects  
Required: No

## Response Elements
<a name="API_CreateIntegration_ResponseElements"></a>

The following elements are returned by the service.

 **AdditionalEncryptionContext** AdditionalEncryptionContext.entry.N.key (key)AdditionalEncryptionContext.entry.N.value (value)  
The encryption context for the integration. For more information, see [Encryption context](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#encrypt_context) in the * AWS Key Management Service Developer Guide*.  
Type: String to string map  
Key Length Constraints: Maximum length of 2147483647.  
Value Length Constraints: Maximum length of 2147483647.

 ** CreateTime **   
The time (UTC) when the integration was created.  
Type: Timestamp

 ** Description **   
The description of the integration.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 1000.  
Pattern: `^.*$` 

 **Errors.IntegrationError.N**   
Any errors associated with the integration.  
Type: Array of [IntegrationError](API_IntegrationError.md) objects

 ** IntegrationArn **   
The Amazon Resource Name (ARN) of the integration.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 255.  
Pattern: `^arn:aws[a-z\-]*:redshift:[a-z0-9\-]*:[0-9]*:integration:[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$` 

 ** IntegrationName **   
The name of the integration.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 63.  
Pattern: `^[a-zA-Z][a-zA-Z0-9]*(-[a-zA-Z0-9]+)*$` 

 ** KMSKeyId **   
The AWS Key Management Service (AWS KMS) key identifier for the key used to encrypt the integration.  
Type: String  
Length Constraints: Maximum length of 2147483647.

 ** SourceArn **   
The Amazon Resource Name (ARN) of the database used as the source for replication.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 255.  
Pattern: `^arn:aws[a-z\-]*:(s3|dynamodb):.*:.*:[a-zA-Z0-9._\-\/]+$` 

 ** Status **   
The current status of the integration.  
Type: String  
Valid Values: `creating | active | modifying | failed | deleting | syncing | needs_attention` 

 **Tags.Tag.N**   
The list of tags associated with the integration.  
Type: Array of [Tag](API_Tag.md) objects

 ** TargetArn **   
The Amazon Resource Name (ARN) of the Amazon Redshift data warehouse to use as the target for replication.  
Type: String  
Length Constraints: Minimum length of 20. Maximum length of 2048.  
Pattern: `^arn:aws[a-z\-]*:redshift(-serverless)?:[a-z0-9\-]+:[0-9]{12}:(namespace\/|namespace:)[a-z0-9\-]+$` 

## Errors
<a name="API_CreateIntegration_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** IntegrationAlreadyExistsFault **   
The integration you are trying to create already exists.  
HTTP Status Code: 400

 ** IntegrationConflictOperationFault **   
A conflicting conditional operation is currently in progress against this resource. This typically occurs when there are multiple requests being made to the same resource at the same time, and these requests conflict with each other.  
HTTP Status Code: 400

 ** IntegrationQuotaExceededFault **   
You can't create any more zero-ETL or S3 event integrations because the quota has been reached.  
HTTP Status Code: 400

 ** IntegrationSourceNotFoundFault **   
The specified integration source can't be found.  
HTTP Status Code: 404

 ** IntegrationTargetNotFoundFault **   
The specified integration target can't be found.  
HTTP Status Code: 404

 ** InvalidClusterState **   
The specified cluster is not in the `available` state.   
HTTP Status Code: 400

 ** InvalidTagFault **   
The tag is invalid.  
HTTP Status Code: 400

 ** TagLimitExceededFault **   
You have exceeded the number of tags allowed.  
HTTP Status Code: 400

 ** UnsupportedOperation **   
The requested operation isn't supported.  
HTTP Status Code: 400

## See Also
<a name="API_CreateIntegration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/redshift-2012-12-01/CreateIntegration) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/redshift-2012-12-01/CreateIntegration) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/redshift-2012-12-01/CreateIntegration) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/redshift-2012-12-01/CreateIntegration) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/redshift-2012-12-01/CreateIntegration) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/redshift-2012-12-01/CreateIntegration) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/redshift-2012-12-01/CreateIntegration) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/redshift-2012-12-01/CreateIntegration) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/redshift-2012-12-01/CreateIntegration) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/redshift-2012-12-01/CreateIntegration) 