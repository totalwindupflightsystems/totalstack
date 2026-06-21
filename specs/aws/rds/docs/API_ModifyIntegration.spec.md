---
id: "@specs/aws/rds/docs/API_ModifyIntegration"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS ModifyIntegration"
status: active
depends_on:
  - "@specs/aws/rds/meta"
---

# ModifyIntegration

> **source:** AWS Documentation
> **spec:id:** @specs/aws/rds/docs/API_ModifyIntegration
> **target_lang:** meta — documentation tier. ALL sections preserved.



# ModifyIntegration
<a name="API_ModifyIntegration"></a>

Modifies a zero-ETL integration with Amazon Redshift.

## Request Parameters
<a name="API_ModifyIntegration_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 ** IntegrationIdentifier **   
The unique identifier of the integration to modify.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 255.  
Pattern: `[a-zA-Z0-9_:\-\/]+`   
Required: Yes

 ** DataFilter **   
A new data filter for the integration. For more information, see [Data filtering for Aurora zero-ETL integrations with Amazon Redshift](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/USER_Zero_ETL_Filtering.html) or [Data filtering for Amazon RDS zero-ETL integrations with Amazon Redshift](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/zero-etl.filtering.html).  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 25600.  
Pattern: `[a-zA-Z0-9_ "\\\-$,*.:?+\/]*`   
Required: No

 ** Description **   
A new description for the integration.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 1000.  
Pattern: `.*`   
Required: No

 ** IntegrationName **   
A new name for the integration.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 63.  
Pattern: `[a-zA-Z](?:-?[a-zA-Z0-9]+)*`   
Required: No

## Response Elements
<a name="API_ModifyIntegration_ResponseElements"></a>

The following elements are returned by the service.

 **AdditionalEncryptionContext** AdditionalEncryptionContext.entry.N.key (key)AdditionalEncryptionContext.entry.N.value (value)  
The encryption context for the integration. For more information, see [Encryption context](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#encrypt_context) in the * AWS Key Management Service Developer Guide*.  
Type: String to string map

 ** CreateTime **   
The time when the integration was created, in Universal Coordinated Time (UTC).  
Type: Timestamp

 ** DataFilter **   
Data filters for the integration. These filters determine which tables from the source database are sent to the target Amazon Redshift data warehouse.   
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 25600.  
Pattern: `[a-zA-Z0-9_ "\\\-$,*.:?+\/]*` 

 ** Description **   
A description of the integration.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 1000.  
Pattern: `.*` 

 **Errors.IntegrationError.N**   
Any errors associated with the integration.  
Type: Array of [IntegrationError](API_IntegrationError.md) objects

 ** IntegrationArn **   
The ARN of the integration.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 255.  
Pattern: `arn:aws[a-z\-]*:rds(-[a-z]*)?:[a-z0-9\-]*:[0-9]*:integration:[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}` 

 ** IntegrationName **   
The name of the integration.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 63.  
Pattern: `[a-zA-Z](?:-?[a-zA-Z0-9]+)*` 

 ** KMSKeyId **   
The AWS Key Management System (AWS KMS) key identifier for the key used to to encrypt the integration.   
Type: String

 ** SourceArn **   
The Amazon Resource Name (ARN) of the database used as the source for replication.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 255.  
Pattern: `arn:aws[a-z\-]*:rds(-[a-z]*)?:[a-z0-9\-]*:[0-9]*:(cluster|db):[a-z][a-z0-9]*(-[a-z0-9]+)*` 

 ** Status **   
The current status of the integration.  
Type: String  
Valid Values: `creating | active | modifying | failed | deleting | syncing | needs_attention` 

 **Tags.Tag.N**   
A list of tags.  
For more information, see [Tagging Amazon RDS resources](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_Tagging.html) in the *Amazon RDS User Guide* or [Tagging Amazon Aurora and Amazon RDS resources](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/USER_Tagging.html) in the *Amazon Aurora User Guide*.   
Type: Array of [Tag](API_Tag.md) objects

 ** TargetArn **   
The ARN of the Redshift data warehouse used as the target for replication.  
Type: String  
Length Constraints: Minimum length of 20. Maximum length of 2048.

## Errors
<a name="API_ModifyIntegration_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** IntegrationConflictOperationFault **   
A conflicting conditional operation is currently in progress against this resource. Typically occurs when there are multiple requests being made to the same resource at the same time, and these requests conflict with each other.  
HTTP Status Code: 400

 ** IntegrationNotFoundFault **   
The specified integration could not be found.  
HTTP Status Code: 404

 ** InvalidIntegrationStateFault **   
The integration is in an invalid state and can't perform the requested operation.  
HTTP Status Code: 400

## Examples
<a name="API_ModifyIntegration_Examples"></a>

### Example
<a name="API_ModifyIntegration_Example_1"></a>

This example illustrates one usage of ModifyIntegration.

#### Sample Request
<a name="API_ModifyIntegration_Example_1_Request"></a>

```
https://rds.us-east-1.amazonaws.com/
   ?Action=ModifyIntegration
   &IntegrationIdentifier=a1b2c3d4-5678-90ab-cdef-EXAMPLE11111
   &IntegrationName=my-renamed-integration
   &SignatureMethod=HmacSHA256
   &SignatureVersion=4
   &Version=2014-10-31
   &X-Amz-Algorithm=AWS4-HMAC-SHA256
   &X-Amz-Credential=AKIADQKE4SARGYLE/20140428/us-east-1/rds/aws4_request
   &X-Amz-Date=20140428T183020Z
   &X-Amz-SignedHeaders=content-type;host;user-agent;x-amz-content-sha256;x-amz-date
   &X-Amz-Signature=3d85bdfaf13861e93a9528824d9876ed87e6e01aaf43a962ce6f2a39247cf33a
```

#### Sample Response
<a name="API_ModifyIntegration_Example_1_Response"></a>

```
<ModifyIntegrationResponse xmlns="http://rds.amazonaws.com/doc/2014-10-31/">
    <ModifyIntegrationResult>
        <SourceArn>arn:aws:rds:us-east-1:123456789012:cluster:my-cluster</SourceArn>
        <IntegrationName>my-renamed-integration</IntegrationName>
        <IntegrationArn>arn:aws:rds:us-east-1:123456789012:integration:a1b2c3d4-5678-90ab-cdef-EXAMPLE11111</IntegrationArn>
        <TargetArn>arn:aws:redshift-serverless:us-east-1:123456789012:namespace/a1b2c3d4-5678-90ab-cdef-EXAMPLE22222</TargetArn>
        <Tags/>
        <DataFilter>include: *.*</DataFilter>
        <CreateTime>2023-12-28T17:20:20.629Z</CreateTime>
        <KMSKeyId>arn:aws:kms:us-east-1:123456789012:key/a1b2c3d4-5678-90ab-cdef-EXAMPLEaaaaa</KMSKeyId>
        <Status>active</Status>
    </ModifyIntegrationResult>
    <ResponseMetadata>
        <RequestId>7581f213-c5a1-42a5-b2cd-e151a1e1c129</RequestId>
    </ResponseMetadata>
</ModifyIntegrationResponse>
```

## See Also
<a name="API_ModifyIntegration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/rds-2014-10-31/ModifyIntegration) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/rds-2014-10-31/ModifyIntegration) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/rds-2014-10-31/ModifyIntegration) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/rds-2014-10-31/ModifyIntegration) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/rds-2014-10-31/ModifyIntegration) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/rds-2014-10-31/ModifyIntegration) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/rds-2014-10-31/ModifyIntegration) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/rds-2014-10-31/ModifyIntegration) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/rds-2014-10-31/ModifyIntegration) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/rds-2014-10-31/ModifyIntegration) 