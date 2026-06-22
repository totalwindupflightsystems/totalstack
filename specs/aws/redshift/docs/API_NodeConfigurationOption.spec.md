---
id: "@specs/aws/redshift/docs/API_NodeConfigurationOption"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS NodeConfigurationOption"
status: active
depends_on:
  - "@specs/aws/redshift/meta"
---

# NodeConfigurationOption

> **source:** AWS Documentation
> **spec:id:** @specs/aws/redshift/docs/API_NodeConfigurationOption
> **target_lang:** meta — documentation tier. ALL sections preserved.



# NodeConfigurationOption
<a name="API_NodeConfigurationOption"></a>

A list of node configurations.

## Contents
<a name="API_NodeConfigurationOption_Contents"></a>

**Note**  
In the following list, the required parameters are described first.

 ** EstimatedDiskUtilizationPercent **   
The estimated disk utilizaton percentage.  
Type: Double  
Required: No

 ** Mode **   
The category of the node configuration recommendation.  
Type: String  
Valid Values: `standard | high-performance`   
Required: No

 ** NodeType **   
The node type, such as, "ra3.4xlarge".  
Type: String  
Length Constraints: Maximum length of 2147483647.  
Required: No

 ** NumberOfNodes **   
The number of nodes.  
Type: Integer  
Required: No

## See Also
<a name="API_NodeConfigurationOption_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/redshift-2012-12-01/NodeConfigurationOption) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/redshift-2012-12-01/NodeConfigurationOption) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/redshift-2012-12-01/NodeConfigurationOption) 