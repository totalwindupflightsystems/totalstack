---
id: "@specs/aws/docdb/docs/API_Parameter"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Parameter"
status: active
depends_on:
  - "@specs/aws/docdb/meta"
---

# Parameter

> **source:** AWS Documentation
> **spec:id:** @specs/aws/docdb/docs/API_Parameter
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Parameter
<a name="API_Parameter"></a>

Detailed information about an individual parameter.

## Contents
<a name="API_Parameter_Contents"></a>

**Note**  
In the following list, the required parameters are described first.

 ** AllowedValues **   
Specifies the valid range of values for the parameter.  
Type: String  
Required: No

 ** ApplyMethod **   
Indicates when to apply parameter updates.  
Type: String  
Valid Values: `immediate | pending-reboot`   
Required: No

 ** ApplyType **   
Specifies the engine-specific parameters type.  
Type: String  
Required: No

 ** DataType **   
Specifies the valid data type for the parameter.  
Type: String  
Required: No

 ** Description **   
Provides a description of the parameter.  
Type: String  
Required: No

 ** IsModifiable **   
 Indicates whether (`true`) or not (`false`) the parameter can be modified. Some parameters have security or operational implications that prevent them from being changed.   
Type: Boolean  
Required: No

 ** MinimumEngineVersion **   
The earliest engine version to which the parameter can apply.  
Type: String  
Required: No

 ** ParameterName **   
Specifies the name of the parameter.  
Type: String  
Required: No

 ** ParameterValue **   
Specifies the value of the parameter. Must be one or more of the cluster parameter's `AllowedValues` in CSV format:  
Valid values are:  
+  `enabled`: The cluster accepts secure connections using TLS version 1.0 through 1.3. 
+  `disabled`: The cluster does not accept secure connections using TLS. 
+  `fips-140-3`: The cluster only accepts secure connections per the requirements of the Federal Information Processing Standards (FIPS) publication 140-3. Only supported starting with Amazon DocumentDB 5.0 (engine version 3.0.3727) clusters in these regions: ca-central-1, us-west-2, us-east-1, us-east-2, us-gov-east-1, us-gov-west-1.
+  `tls1.2+`: The cluster accepts secure connections using TLS version 1.2 and above. Only supported starting with Amazon DocumentDB 4.0 (engine version 2.0.10980) and Amazon DocumentDB 5.0 (engine version 3.0.11051).
+  `tls1.3+`: The cluster accepts secure connections using TLS version 1.3 and above. Only supported starting with Amazon DocumentDB 4.0 (engine version 2.0.10980) and Amazon DocumentDB 5.0 (engine version 3.0.11051).
Type: String  
Required: No

 ** Source **   
Indicates the source of the parameter value.  
Type: String  
Required: No

## See Also
<a name="API_Parameter_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/docdb-2014-10-31/Parameter) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/docdb-2014-10-31/Parameter) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/docdb-2014-10-31/Parameter) 