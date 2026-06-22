---
id: "@specs/aws/batch/docs/API_ServiceEnvironmentDetail"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS ServiceEnvironmentDetail"
status: active
depends_on:
  - "@specs/aws/batch/meta"
---

# ServiceEnvironmentDetail

> **source:** AWS Documentation
> **spec:id:** @specs/aws/batch/docs/API_ServiceEnvironmentDetail
> **target_lang:** meta — documentation tier. ALL sections preserved.



# ServiceEnvironmentDetail
<a name="API_ServiceEnvironmentDetail"></a>

Detailed information about a service environment, including its configuration, state, and capacity limits.

## Contents
<a name="API_ServiceEnvironmentDetail_Contents"></a>

 ** capacityLimits **   <a name="Batch-Type-ServiceEnvironmentDetail-capacityLimits"></a>
The capacity limits for the service environment. This defines the maximum resources that can be used by service jobs in this environment.  
Type: Array of [CapacityLimit](API_CapacityLimit.md) objects  
Required: Yes

 ** serviceEnvironmentArn **   <a name="Batch-Type-ServiceEnvironmentDetail-serviceEnvironmentArn"></a>
The Amazon Resource Name (ARN) of the service environment.  
Type: String  
Required: Yes

 ** serviceEnvironmentName **   <a name="Batch-Type-ServiceEnvironmentDetail-serviceEnvironmentName"></a>
The name of the service environment.  
Type: String  
Required: Yes

 ** serviceEnvironmentType **   <a name="Batch-Type-ServiceEnvironmentDetail-serviceEnvironmentType"></a>
The type of service environment. For SageMaker Training jobs, this value is `SAGEMAKER_TRAINING`.  
Type: String  
Valid Values: `SAGEMAKER_TRAINING`   
Required: Yes

 ** state **   <a name="Batch-Type-ServiceEnvironmentDetail-state"></a>
The state of the service environment. Valid values are `ENABLED` and `DISABLED`.  
Type: String  
Valid Values: `ENABLED | DISABLED`   
Required: No

 ** status **   <a name="Batch-Type-ServiceEnvironmentDetail-status"></a>
The current status of the service environment.  
Type: String  
Valid Values: `CREATING | UPDATING | DELETING | DELETED | VALID | INVALID`   
Required: No

 ** tags **   <a name="Batch-Type-ServiceEnvironmentDetail-tags"></a>
The tags associated with the service environment. Each tag consists of a key and an optional value. For more information, see [Tagging your AWS Batch resources](https://docs.aws.amazon.com/batch/latest/userguide/using-tags.html).  
Type: String to string map  
Map Entries: Maximum number of 50 items.  
Key Length Constraints: Minimum length of 1. Maximum length of 128.  
Value Length Constraints: Maximum length of 256.  
Required: No

## See Also
<a name="API_ServiceEnvironmentDetail_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/batch-2016-08-10/ServiceEnvironmentDetail) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/batch-2016-08-10/ServiceEnvironmentDetail) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/batch-2016-08-10/ServiceEnvironmentDetail) 