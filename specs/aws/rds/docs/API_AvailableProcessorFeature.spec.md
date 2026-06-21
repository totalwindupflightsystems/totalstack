---
id: "@specs/aws/rds/docs/API_AvailableProcessorFeature"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS AvailableProcessorFeature"
status: active
depends_on:
  - "@specs/aws/rds/meta"
---

# AvailableProcessorFeature

> **source:** AWS Documentation
> **spec:id:** @specs/aws/rds/docs/API_AvailableProcessorFeature
> **target_lang:** meta — documentation tier. ALL sections preserved.



# AvailableProcessorFeature
<a name="API_AvailableProcessorFeature"></a>

Contains the available processor feature information for the DB instance class of a DB instance.

For more information, see [Configuring the Processor of the DB Instance Class](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Concepts.DBInstanceClass.html#USER_ConfigureProcessor) in the *Amazon RDS User Guide. * 

## Contents
<a name="API_AvailableProcessorFeature_Contents"></a>

**Note**  
In the following list, the required parameters are described first.

 ** AllowedValues **   
The allowed values for the processor feature of the DB instance class.  
Type: String  
Required: No

 ** DefaultValue **   
The default value for the processor feature of the DB instance class.  
Type: String  
Required: No

 ** Name **   
The name of the processor feature. Valid names are `coreCount` and `threadsPerCore`.  
Type: String  
Required: No

## See Also
<a name="API_AvailableProcessorFeature_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/rds-2014-10-31/AvailableProcessorFeature) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/rds-2014-10-31/AvailableProcessorFeature) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/rds-2014-10-31/AvailableProcessorFeature) 