---
id: "@specs/aws/redshift/docs/API_OrderableClusterOption"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS OrderableClusterOption"
status: active
depends_on:
  - "@specs/aws/redshift/meta"
---

# OrderableClusterOption

> **source:** AWS Documentation
> **spec:id:** @specs/aws/redshift/docs/API_OrderableClusterOption
> **target_lang:** meta — documentation tier. ALL sections preserved.



# OrderableClusterOption
<a name="API_OrderableClusterOption"></a>

Describes an orderable cluster option.

## Contents
<a name="API_OrderableClusterOption_Contents"></a>

**Note**  
In the following list, the required parameters are described first.

 ** AvailabilityZones.AvailabilityZone.N **   
A list of availability zones for the orderable cluster.  
Type: Array of [AvailabilityZone](API_AvailabilityZone.md) objects  
Required: No

 ** ClusterType **   
The cluster type, for example `multi-node`.   
Type: String  
Length Constraints: Maximum length of 2147483647.  
Required: No

 ** ClusterVersion **   
The version of the orderable cluster.  
Type: String  
Length Constraints: Maximum length of 2147483647.  
Required: No

 ** NodeType **   
The node type for the orderable cluster.  
Type: String  
Length Constraints: Maximum length of 2147483647.  
Required: No

## See Also
<a name="API_OrderableClusterOption_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/redshift-2012-12-01/OrderableClusterOption) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/redshift-2012-12-01/OrderableClusterOption) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/redshift-2012-12-01/OrderableClusterOption) 