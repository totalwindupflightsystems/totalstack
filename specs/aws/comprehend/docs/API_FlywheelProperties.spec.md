---
id: "@specs/aws/comprehend/docs/API_FlywheelProperties"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS FlywheelProperties"
status: active
depends_on:
  - "@specs/aws/comprehend/meta"
---

# FlywheelProperties

> **source:** AWS Documentation
> **spec:id:** @specs/aws/comprehend/docs/API_FlywheelProperties
> **target_lang:** meta — documentation tier. ALL sections preserved.



# FlywheelProperties
<a name="API_FlywheelProperties"></a>

The flywheel properties.

## Contents
<a name="API_FlywheelProperties_Contents"></a>

 ** ActiveModelArn **   <a name="comprehend-Type-FlywheelProperties-ActiveModelArn"></a>
The Amazon Resource Number (ARN) of the active model version.  
Type: String  
Length Constraints: Maximum length of 256.  
Pattern: `arn:aws(-[^:]+)?:comprehend:[a-zA-Z0-9-]*:[0-9]{12}:(document-classifier|entity-recognizer)/[a-zA-Z0-9](-*[a-zA-Z0-9])*(/version/[a-zA-Z0-9](-*[a-zA-Z0-9])*)?`   
Required: No

 ** CreationTime **   <a name="comprehend-Type-FlywheelProperties-CreationTime"></a>
Creation time of the flywheel.  
Type: Timestamp  
Required: No

 ** DataAccessRoleArn **   <a name="comprehend-Type-FlywheelProperties-DataAccessRoleArn"></a>
The Amazon Resource Name (ARN) of the IAM role that grants Amazon Comprehend permission to access the flywheel data.  
Type: String  
Length Constraints: Minimum length of 20. Maximum length of 2048.  
Pattern: `arn:aws(-[^:]+)?:iam::[0-9]{12}:role/.+`   
Required: No

 ** DataLakeS3Uri **   <a name="comprehend-Type-FlywheelProperties-DataLakeS3Uri"></a>
Amazon S3 URI of the data lake location.   
Type: String  
Length Constraints: Maximum length of 1024.  
Pattern: `s3://[a-z0-9][\.\-a-z0-9]{1,61}[a-z0-9](/.*)?`   
Required: No

 ** DataSecurityConfig **   <a name="comprehend-Type-FlywheelProperties-DataSecurityConfig"></a>
Data security configuration.  
Type: [DataSecurityConfig](API_DataSecurityConfig.md) object  
Required: No

 ** FlywheelArn **   <a name="comprehend-Type-FlywheelProperties-FlywheelArn"></a>
The Amazon Resource Number (ARN) of the flywheel.  
Type: String  
Length Constraints: Maximum length of 256.  
Pattern: `arn:aws(-[^:]+)?:comprehend:[a-zA-Z0-9-]*:[0-9]{12}:flywheel/[a-zA-Z0-9](-*[a-zA-Z0-9])*`   
Required: No

 ** LastModifiedTime **   <a name="comprehend-Type-FlywheelProperties-LastModifiedTime"></a>
Last modified time for the flywheel.  
Type: Timestamp  
Required: No

 ** LatestFlywheelIteration **   <a name="comprehend-Type-FlywheelProperties-LatestFlywheelIteration"></a>
The most recent flywheel iteration.  
Type: String  
Length Constraints: Maximum length of 63.  
Pattern: `[0-9]{8}T[0-9]{6}Z`   
Required: No

 ** Message **   <a name="comprehend-Type-FlywheelProperties-Message"></a>
A description of the status of the flywheel.  
Type: String  
Required: No

 ** ModelType **   <a name="comprehend-Type-FlywheelProperties-ModelType"></a>
Model type of the flywheel's model.  
Type: String  
Valid Values: `DOCUMENT_CLASSIFIER | ENTITY_RECOGNIZER`   
Required: No

 ** Status **   <a name="comprehend-Type-FlywheelProperties-Status"></a>
The status of the flywheel.  
Type: String  
Valid Values: `CREATING | ACTIVE | UPDATING | DELETING | FAILED`   
Required: No

 ** TaskConfig **   <a name="comprehend-Type-FlywheelProperties-TaskConfig"></a>
Configuration about the model associated with a flywheel.  
Type: [TaskConfig](API_TaskConfig.md) object  
Required: No

## See Also
<a name="API_FlywheelProperties_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/comprehend-2017-11-27/FlywheelProperties) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/comprehend-2017-11-27/FlywheelProperties) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/comprehend-2017-11-27/FlywheelProperties) 