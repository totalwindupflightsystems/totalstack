---
id: "@specs/aws/redshift/docs/API_Integration"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Integration"
status: active
depends_on:
  - "@specs/aws/redshift/meta"
---

# Integration

> **source:** AWS Documentation
> **spec:id:** @specs/aws/redshift/docs/API_Integration
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Integration
<a name="API_Integration"></a>

## Contents
<a name="API_Integration_Contents"></a>

**Note**  
In the following list, the required parameters are described first.

 ** AdditionalEncryptionContext **  AdditionalEncryptionContext.entry.N.key (key)  AdditionalEncryptionContext.entry.N.value (value)   
The encryption context for the integration. For more information, see [Encryption context](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#encrypt_context) in the * AWS Key Management Service Developer Guide*.  
Type: String to string map  
Key Length Constraints: Maximum length of 2147483647.  
Value Length Constraints: Maximum length of 2147483647.  
Required: No

 ** CreateTime **   
The time (UTC) when the integration was created.  
Type: Timestamp  
Required: No

 ** Description **   
The description of the integration.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 1000.  
Pattern: `^.*$`   
Required: No

 ** Errors.IntegrationError.N **   
Any errors associated with the integration.  
Type: Array of [IntegrationError](API_IntegrationError.md) objects  
Required: No

 ** IntegrationArn **   
The Amazon Resource Name (ARN) of the integration.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 255.  
Pattern: `^arn:aws[a-z\-]*:redshift:[a-z0-9\-]*:[0-9]*:integration:[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$`   
Required: No

 ** IntegrationName **   
The name of the integration.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 63.  
Pattern: `^[a-zA-Z][a-zA-Z0-9]*(-[a-zA-Z0-9]+)*$`   
Required: No

 ** KMSKeyId **   
The AWS Key Management Service (AWS KMS) key identifier for the key used to encrypt the integration.  
Type: String  
Length Constraints: Maximum length of 2147483647.  
Required: No

 ** SourceArn **   
The Amazon Resource Name (ARN) of the database used as the source for replication.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 255.  
Pattern: `^arn:aws[a-z\-]*:(s3|dynamodb):.*:.*:[a-zA-Z0-9._\-\/]+$`   
Required: No

 ** Status **   
The current status of the integration.  
Type: String  
Valid Values: `creating | active | modifying | failed | deleting | syncing | needs_attention`   
Required: No

 ** Tags.Tag.N **   
The list of tags associated with the integration.  
Type: Array of [Tag](API_Tag.md) objects  
Required: No

 ** TargetArn **   
The Amazon Resource Name (ARN) of the Amazon Redshift data warehouse to use as the target for replication.  
Type: String  
Length Constraints: Minimum length of 20. Maximum length of 2048.  
Pattern: `^arn:aws[a-z\-]*:redshift(-serverless)?:[a-z0-9\-]+:[0-9]{12}:(namespace\/|namespace:)[a-z0-9\-]+$`   
Required: No

## See Also
<a name="API_Integration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/redshift-2012-12-01/Integration) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/redshift-2012-12-01/Integration) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/redshift-2012-12-01/Integration) 