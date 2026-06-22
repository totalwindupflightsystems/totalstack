---
id: "@specs/aws/emr/docs/API_JobFlowDetail"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS JobFlowDetail"
status: active
depends_on:
  - "@specs/aws/emr/meta"
---

# JobFlowDetail

> **source:** AWS Documentation
> **spec:id:** @specs/aws/emr/docs/API_JobFlowDetail
> **target_lang:** meta — documentation tier. ALL sections preserved.



# JobFlowDetail
<a name="API_JobFlowDetail"></a>

A description of a cluster (job flow).

## Contents
<a name="API_JobFlowDetail_Contents"></a>

 ** ExecutionStatusDetail **   <a name="EMR-Type-JobFlowDetail-ExecutionStatusDetail"></a>
Describes the execution status of the job flow.  
Type: [JobFlowExecutionStatusDetail](API_JobFlowExecutionStatusDetail.md) object  
Required: Yes

 ** Instances **   <a name="EMR-Type-JobFlowDetail-Instances"></a>
Describes the Amazon EC2 instances of the job flow.  
Type: [JobFlowInstancesDetail](API_JobFlowInstancesDetail.md) object  
Required: Yes

 ** JobFlowId **   <a name="EMR-Type-JobFlowDetail-JobFlowId"></a>
The job flow identifier.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 256.  
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`   
Required: Yes

 ** Name **   <a name="EMR-Type-JobFlowDetail-Name"></a>
The name of the job flow.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 256.  
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`   
Required: Yes

 ** AmiVersion **   <a name="EMR-Type-JobFlowDetail-AmiVersion"></a>
Applies only to Amazon EMR AMI versions 3.x and 2.x. For Amazon EMR releases 4.0 and later, `ReleaseLabel` is used. To specify a custom AMI, use `CustomAmiID`.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 256.  
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`   
Required: No

 ** AutoScalingRole **   <a name="EMR-Type-JobFlowDetail-AutoScalingRole"></a>
An IAM role for automatic scaling policies. The default role is `EMR_AutoScaling_DefaultRole`. The IAM role provides a way for the automatic scaling feature to get the required permissions it needs to launch and terminate Amazon EC2 instances in an instance group.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 10280.  
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`   
Required: No

 ** BootstrapActions **   <a name="EMR-Type-JobFlowDetail-BootstrapActions"></a>
A list of the bootstrap actions run by the job flow.  
Type: Array of [BootstrapActionDetail](API_BootstrapActionDetail.md) objects  
Required: No

 ** JobFlowRole **   <a name="EMR-Type-JobFlowDetail-JobFlowRole"></a>
The IAM role that was specified when the job flow was launched. The Amazon EC2 instances of the job flow assume this role.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 10280.  
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`   
Required: No

 ** LogEncryptionKmsKeyId **   <a name="EMR-Type-JobFlowDetail-LogEncryptionKmsKeyId"></a>
The AWS KMS key used for encrypting log files. This attribute is only available with Amazon EMR 5.30.0 and later, excluding 6.0.0.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 10280.  
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`   
Required: No

 ** LogUri **   <a name="EMR-Type-JobFlowDetail-LogUri"></a>
The location in Amazon S3 where log files for the job are stored.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 10280.  
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`   
Required: No

 ** ScaleDownBehavior **   <a name="EMR-Type-JobFlowDetail-ScaleDownBehavior"></a>
The way that individual Amazon EC2 instances terminate when an automatic scale-in activity occurs or an instance group is resized. `TERMINATE_AT_INSTANCE_HOUR` indicates that Amazon EMR terminates nodes at the instance-hour boundary, regardless of when the request to terminate the instance was submitted. This option is only available with Amazon EMR 5.1.0 and later and is the default for clusters created using that version. `TERMINATE_AT_TASK_COMPLETION` indicates that Amazon EMR adds nodes to a deny list and drains tasks from nodes before terminating the Amazon EC2 instances, regardless of the instance-hour boundary. With either behavior, Amazon EMR removes the least active nodes first and blocks instance termination if it could lead to HDFS corruption. `TERMINATE_AT_TASK_COMPLETION` available only in Amazon EMR releases 4.1.0 and later, and is the default for releases of Amazon EMR earlier than 5.1.0.  
Type: String  
Valid Values: `TERMINATE_AT_INSTANCE_HOUR | TERMINATE_AT_TASK_COMPLETION`   
Required: No

 ** ServiceRole **   <a name="EMR-Type-JobFlowDetail-ServiceRole"></a>
The IAM role that is assumed by the Amazon EMR service to access AWS resources on your behalf.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 10280.  
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`   
Required: No

 ** Steps **   <a name="EMR-Type-JobFlowDetail-Steps"></a>
A list of steps run by the job flow.  
Type: Array of [StepDetail](API_StepDetail.md) objects  
Required: No

 ** SupportedProducts **   <a name="EMR-Type-JobFlowDetail-SupportedProducts"></a>
A list of strings set by third-party software when the job flow is launched. If you are not using third-party software to manage the job flow, this value is empty.  
Type: Array of strings  
Length Constraints: Minimum length of 0. Maximum length of 256.  
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`   
Required: No

 ** VisibleToAllUsers **   <a name="EMR-Type-JobFlowDetail-VisibleToAllUsers"></a>
Indicates whether the cluster is visible to IAM principals in the AWS account associated with the cluster. When `true`, IAM principals in the AWS account can perform Amazon EMR cluster actions that their IAM policies allow. When `false`, only the IAM principal that created the cluster and the AWS account root user can perform Amazon EMR actions, regardless of IAM permissions policies attached to other IAM principals.  
The default value is `true` if a value is not provided when creating a cluster using the Amazon EMR API [RunJobFlow](API_RunJobFlow.md) command, the AWS CLI [create-cluster](https://docs.aws.amazon.com/cli/latest/reference/emr/create-cluster.html) command, or the AWS Management Console.  
Type: Boolean  
Required: No

## See Also
<a name="API_JobFlowDetail_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/elasticmapreduce-2009-03-31/JobFlowDetail) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/elasticmapreduce-2009-03-31/JobFlowDetail) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/elasticmapreduce-2009-03-31/JobFlowDetail) 