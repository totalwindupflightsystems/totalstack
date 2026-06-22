---
id: "@specs/aws/redshift/docs/API_DefaultClusterParameters"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS DefaultClusterParameters"
status: active
depends_on:
  - "@specs/aws/redshift/meta"
---

# DefaultClusterParameters

> **source:** AWS Documentation
> **spec:id:** @specs/aws/redshift/docs/API_DefaultClusterParameters
> **target_lang:** meta — documentation tier. ALL sections preserved.



# DefaultClusterParameters
<a name="API_DefaultClusterParameters"></a>

Describes the default cluster parameters for a parameter group family.

## Contents
<a name="API_DefaultClusterParameters_Contents"></a>

**Note**  
In the following list, the required parameters are described first.

 ** Marker **   
A value that indicates the starting point for the next set of response records in a subsequent request. If a value is returned in a response, you can retrieve the next set of records by providing this returned marker value in the `Marker` parameter and retrying the command. If the `Marker` field is empty, all response records have been retrieved for the request.   
Type: String  
Length Constraints: Maximum length of 2147483647.  
Required: No

 ** ParameterGroupFamily **   
The name of the cluster parameter group family to which the engine default parameters apply.  
Type: String  
Length Constraints: Maximum length of 2147483647.  
Required: No

 ** Parameters.Parameter.N **   
The list of cluster default parameters.  
Type: Array of [Parameter](API_Parameter.md) objects  
Required: No

## See Also
<a name="API_DefaultClusterParameters_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/redshift-2012-12-01/DefaultClusterParameters) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/redshift-2012-12-01/DefaultClusterParameters) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/redshift-2012-12-01/DefaultClusterParameters) 