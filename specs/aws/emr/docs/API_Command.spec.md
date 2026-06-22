---
id: "@specs/aws/emr/docs/API_Command"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Command"
status: active
depends_on:
  - "@specs/aws/emr/meta"
---

# Command

> **source:** AWS Documentation
> **spec:id:** @specs/aws/emr/docs/API_Command
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Command
<a name="API_Command"></a>

An entity describing an executable that runs on a cluster.

## Contents
<a name="API_Command_Contents"></a>

 ** Args **   <a name="EMR-Type-Command-Args"></a>
Arguments for Amazon EMR to pass to the command for execution.  
Type: Array of strings  
Required: No

 ** Name **   <a name="EMR-Type-Command-Name"></a>
The name of the command.  
Type: String  
Required: No

 ** ScriptPath **   <a name="EMR-Type-Command-ScriptPath"></a>
The Amazon S3 location of the command script.  
Type: String  
Required: No

## See Also
<a name="API_Command_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/elasticmapreduce-2009-03-31/Command) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/elasticmapreduce-2009-03-31/Command) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/elasticmapreduce-2009-03-31/Command) 