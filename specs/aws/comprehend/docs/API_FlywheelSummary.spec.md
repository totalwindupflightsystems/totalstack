---
id: "@specs/aws/comprehend/docs/API_FlywheelSummary"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS FlywheelSummary"
status: active
depends_on:
  - "@specs/aws/comprehend/meta"
---

# FlywheelSummary

> **source:** AWS Documentation
> **spec:id:** @specs/aws/comprehend/docs/API_FlywheelSummary
> **target_lang:** meta — documentation tier. ALL sections preserved.



# FlywheelSummary
<a name="API_FlywheelSummary"></a>

Flywheel summary information.

## Contents
<a name="API_FlywheelSummary_Contents"></a>

 ** ActiveModelArn **   <a name="comprehend-Type-FlywheelSummary-ActiveModelArn"></a>
ARN of the active model version for the flywheel.  
Type: String  
Length Constraints: Maximum length of 256.  
Pattern: `arn:aws(-[^:]+)?:comprehend:[a-zA-Z0-9-]*:[0-9]{12}:(document-classifier|entity-recognizer)/[a-zA-Z0-9](-*[a-zA-Z0-9])*(/version/[a-zA-Z0-9](-*[a-zA-Z0-9])*)?`   
Required: No

 ** CreationTime **   <a name="comprehend-Type-FlywheelSummary-CreationTime"></a>
Creation time of the flywheel.  
Type: Timestamp  
Required: No

 ** DataLakeS3Uri **   <a name="comprehend-Type-FlywheelSummary-DataLakeS3Uri"></a>
Amazon S3 URI of the data lake location.   
Type: String  
Length Constraints: Maximum length of 1024.  
Pattern: `s3://[a-z0-9][\.\-a-z0-9]{1,61}[a-z0-9](/.*)?`   
Required: No

 ** FlywheelArn **   <a name="comprehend-Type-FlywheelSummary-FlywheelArn"></a>
The Amazon Resource Number (ARN) of the flywheel  
Type: String  
Length Constraints: Maximum length of 256.  
Pattern: `arn:aws(-[^:]+)?:comprehend:[a-zA-Z0-9-]*:[0-9]{12}:flywheel/[a-zA-Z0-9](-*[a-zA-Z0-9])*`   
Required: No

 ** LastModifiedTime **   <a name="comprehend-Type-FlywheelSummary-LastModifiedTime"></a>
Last modified time for the flywheel.  
Type: Timestamp  
Required: No

 ** LatestFlywheelIteration **   <a name="comprehend-Type-FlywheelSummary-LatestFlywheelIteration"></a>
The most recent flywheel iteration.  
Type: String  
Length Constraints: Maximum length of 63.  
Pattern: `[0-9]{8}T[0-9]{6}Z`   
Required: No

 ** Message **   <a name="comprehend-Type-FlywheelSummary-Message"></a>
A description of the status of the flywheel.  
Type: String  
Required: No

 ** ModelType **   <a name="comprehend-Type-FlywheelSummary-ModelType"></a>
Model type of the flywheel's model.  
Type: String  
Valid Values: `DOCUMENT_CLASSIFIER | ENTITY_RECOGNIZER`   
Required: No

 ** Status **   <a name="comprehend-Type-FlywheelSummary-Status"></a>
The status of the flywheel.  
Type: String  
Valid Values: `CREATING | ACTIVE | UPDATING | DELETING | FAILED`   
Required: No

## See Also
<a name="API_FlywheelSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/comprehend-2017-11-27/FlywheelSummary) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/comprehend-2017-11-27/FlywheelSummary) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/comprehend-2017-11-27/FlywheelSummary) 