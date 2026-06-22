---
id: "@specs/aws/emr/docs/API_ExecutionEngineConfig"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS ExecutionEngineConfig"
status: active
depends_on:
  - "@specs/aws/emr/meta"
---

# ExecutionEngineConfig

> **source:** AWS Documentation
> **spec:id:** @specs/aws/emr/docs/API_ExecutionEngineConfig
> **target_lang:** meta — documentation tier. ALL sections preserved.



# ExecutionEngineConfig
<a name="API_ExecutionEngineConfig"></a>

Specifies the execution engine (cluster) to run the notebook and perform the notebook execution, for example, an Amazon EMR cluster.

## Contents
<a name="API_ExecutionEngineConfig_Contents"></a>

 ** Id **   <a name="EMR-Type-ExecutionEngineConfig-Id"></a>
The unique identifier of the execution engine. For an Amazon EMR cluster, this is the cluster ID.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 256.  
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`   
Required: Yes

 ** ExecutionRoleArn **   <a name="EMR-Type-ExecutionEngineConfig-ExecutionRoleArn"></a>
The execution role ARN required for the notebook execution.  
Type: String  
Length Constraints: Minimum length of 20. Maximum length of 2048.  
Pattern: `^arn:(aws[a-zA-Z0-9-]*):iam::(\d{12})?:(role((\u002F)|(\u002F[\u0021-\u007F]+\u002F))[\w+=,.@-]+)$`   
Required: No

 ** MasterInstanceSecurityGroupId **   <a name="EMR-Type-ExecutionEngineConfig-MasterInstanceSecurityGroupId"></a>
An optional unique ID of an Amazon EC2 security group to associate with the master instance of the Amazon EMR cluster for this notebook execution. For more information see [Specifying Amazon EC2 Security Groups for Amazon EMR Notebooks](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-managed-notebooks-security-groups.html) in the *EMR Management Guide*.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 256.  
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`   
Required: No

 ** Type **   <a name="EMR-Type-ExecutionEngineConfig-Type"></a>
The type of execution engine. A value of `EMR` specifies an Amazon EMR cluster.  
Type: String  
Valid Values: `EMR`   
Required: No

## See Also
<a name="API_ExecutionEngineConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/elasticmapreduce-2009-03-31/ExecutionEngineConfig) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/elasticmapreduce-2009-03-31/ExecutionEngineConfig) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/elasticmapreduce-2009-03-31/ExecutionEngineConfig) 