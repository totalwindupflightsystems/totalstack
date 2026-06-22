---
id: "@specs/aws/redshift/docs/API_Parameter"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Parameter"
status: active
depends_on:
  - "@specs/aws/redshift/meta"
---

# Parameter

> **source:** AWS Documentation
> **spec:id:** @specs/aws/redshift/docs/API_Parameter
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Parameter
<a name="API_Parameter"></a>

Describes a parameter in a cluster parameter group.

## Contents
<a name="API_Parameter_Contents"></a>

**Note**  
In the following list, the required parameters are described first.

 ** AllowedValues **   
The valid range of values for the parameter.  
Type: String  
Length Constraints: Maximum length of 2147483647.  
Required: No

 ** ApplyType **   
Specifies how to apply the WLM configuration parameter. Some properties can be applied dynamically, while other properties require that any associated clusters be rebooted for the configuration changes to be applied. For more information about parameters and parameter groups, go to [Amazon Redshift Parameter Groups](https://docs.aws.amazon.com/redshift/latest/mgmt/working-with-parameter-groups.html) in the *Amazon Redshift Cluster Management Guide*.  
Type: String  
Valid Values: `static | dynamic`   
Required: No

 ** DataType **   
The data type of the parameter.  
Type: String  
Length Constraints: Maximum length of 2147483647.  
Required: No

 ** Description **   
A description of the parameter.  
Type: String  
Length Constraints: Maximum length of 2147483647.  
Required: No

 ** IsModifiable **   
If `true`, the parameter can be modified. Some parameters have security or operational implications that prevent them from being changed.   
Type: Boolean  
Required: No

 ** MinimumEngineVersion **   
The earliest engine version to which the parameter can apply.  
Type: String  
Length Constraints: Maximum length of 2147483647.  
Required: No

 ** ParameterName **   
The name of the parameter.  
Type: String  
Length Constraints: Maximum length of 2147483647.  
Required: No

 ** ParameterValue **   
The value of the parameter. If `ParameterName` is `wlm_json_configuration`, then the maximum size of `ParameterValue` is 8000 characters.  
Type: String  
Length Constraints: Maximum length of 2147483647.  
Required: No

 ** Source **   
The source of the parameter value, such as "engine-default" or "user".  
Type: String  
Length Constraints: Maximum length of 2147483647.  
Required: No

## See Also
<a name="API_Parameter_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/redshift-2012-12-01/Parameter) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/redshift-2012-12-01/Parameter) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/redshift-2012-12-01/Parameter) 