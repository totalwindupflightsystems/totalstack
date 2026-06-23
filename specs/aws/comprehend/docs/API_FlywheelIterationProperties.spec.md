---
id: "@specs/aws/comprehend/docs/API_FlywheelIterationProperties"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS FlywheelIterationProperties"
status: active
depends_on:
  - "@specs/aws/comprehend/meta"
---

# FlywheelIterationProperties

> **source:** AWS Documentation
> **spec:id:** @specs/aws/comprehend/docs/API_FlywheelIterationProperties
> **target_lang:** meta — documentation tier. ALL sections preserved.



# FlywheelIterationProperties
<a name="API_FlywheelIterationProperties"></a>

The configuration properties of a flywheel iteration.

## Contents
<a name="API_FlywheelIterationProperties_Contents"></a>

 ** CreationTime **   <a name="comprehend-Type-FlywheelIterationProperties-CreationTime"></a>
The creation start time of the flywheel iteration.  
Type: Timestamp  
Required: No

 ** EndTime **   <a name="comprehend-Type-FlywheelIterationProperties-EndTime"></a>
The completion time of this flywheel iteration.  
Type: Timestamp  
Required: No

 ** EvaluatedModelArn **   <a name="comprehend-Type-FlywheelIterationProperties-EvaluatedModelArn"></a>
The ARN of the evaluated model associated with this flywheel iteration.  
Type: String  
Length Constraints: Maximum length of 256.  
Pattern: `arn:aws(-[^:]+)?:comprehend:[a-zA-Z0-9-]*:[0-9]{12}:(document-classifier|entity-recognizer)/[a-zA-Z0-9](-*[a-zA-Z0-9])*(/version/[a-zA-Z0-9](-*[a-zA-Z0-9])*)?`   
Required: No

 ** EvaluatedModelMetrics **   <a name="comprehend-Type-FlywheelIterationProperties-EvaluatedModelMetrics"></a>
The evaluation metrics associated with the evaluated model.  
Type: [FlywheelModelEvaluationMetrics](API_FlywheelModelEvaluationMetrics.md) object  
Required: No

 ** EvaluationManifestS3Prefix **   <a name="comprehend-Type-FlywheelIterationProperties-EvaluationManifestS3Prefix"></a>
  
Type: String  
Length Constraints: Maximum length of 1024.  
Pattern: `s3://[a-z0-9][\.\-a-z0-9]{1,61}[a-z0-9](/.*)?`   
Required: No

 ** FlywheelArn **   <a name="comprehend-Type-FlywheelIterationProperties-FlywheelArn"></a>
  
Type: String  
Length Constraints: Maximum length of 256.  
Pattern: `arn:aws(-[^:]+)?:comprehend:[a-zA-Z0-9-]*:[0-9]{12}:flywheel/[a-zA-Z0-9](-*[a-zA-Z0-9])*`   
Required: No

 ** FlywheelIterationId **   <a name="comprehend-Type-FlywheelIterationProperties-FlywheelIterationId"></a>
  
Type: String  
Length Constraints: Maximum length of 63.  
Pattern: `[0-9]{8}T[0-9]{6}Z`   
Required: No

 ** Message **   <a name="comprehend-Type-FlywheelIterationProperties-Message"></a>
A description of the status of the flywheel iteration.  
Type: String  
Required: No

 ** Status **   <a name="comprehend-Type-FlywheelIterationProperties-Status"></a>
The status of the flywheel iteration.  
Type: String  
Valid Values: `TRAINING | EVALUATING | COMPLETED | FAILED | STOP_REQUESTED | STOPPED`   
Required: No

 ** TrainedModelArn **   <a name="comprehend-Type-FlywheelIterationProperties-TrainedModelArn"></a>
The ARN of the trained model associated with this flywheel iteration.  
Type: String  
Length Constraints: Maximum length of 256.  
Pattern: `arn:aws(-[^:]+)?:comprehend:[a-zA-Z0-9-]*:[0-9]{12}:(document-classifier|entity-recognizer)/[a-zA-Z0-9](-*[a-zA-Z0-9])*(/version/[a-zA-Z0-9](-*[a-zA-Z0-9])*)?`   
Required: No

 ** TrainedModelMetrics **   <a name="comprehend-Type-FlywheelIterationProperties-TrainedModelMetrics"></a>
The metrics associated with the trained model.  
Type: [FlywheelModelEvaluationMetrics](API_FlywheelModelEvaluationMetrics.md) object  
Required: No

## See Also
<a name="API_FlywheelIterationProperties_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/comprehend-2017-11-27/FlywheelIterationProperties) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/comprehend-2017-11-27/FlywheelIterationProperties) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/comprehend-2017-11-27/FlywheelIterationProperties) 