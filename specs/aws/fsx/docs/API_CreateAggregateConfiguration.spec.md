---
id: "@specs/aws/fsx/docs/API_CreateAggregateConfiguration"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS CreateAggregateConfiguration"
status: active
depends_on:
  - "@specs/aws/fsx/meta"
---

# CreateAggregateConfiguration

> **source:** AWS Documentation
> **spec:id:** @specs/aws/fsx/docs/API_CreateAggregateConfiguration
> **target_lang:** meta — documentation tier. ALL sections preserved.



# CreateAggregateConfiguration
<a name="API_CreateAggregateConfiguration"></a>

Used to specify the configuration options for an FSx for ONTAP volume's storage aggregate or aggregates.

## Contents
<a name="API_CreateAggregateConfiguration_Contents"></a>

 ** Aggregates **   <a name="FSx-Type-CreateAggregateConfiguration-Aggregates"></a>
Used to specify the names of aggregates on which the volume will be created.  
Type: Array of strings  
Array Members: Maximum number of 6 items.  
Length Constraints: Minimum length of 5. Maximum length of 6.  
Pattern: `^(aggr[0-9]{1,2})$`   
Required: No

 ** ConstituentsPerAggregate **   <a name="FSx-Type-CreateAggregateConfiguration-ConstituentsPerAggregate"></a>
Used to explicitly set the number of constituents within the FlexGroup per storage aggregate. This field is optional when creating a FlexGroup volume. If unspecified, the default value will be 8. This field cannot be provided when creating a FlexVol volume.  
Type: Integer  
Valid Range: Minimum value of 1. Maximum value of 200.  
Required: No

## See Also
<a name="API_CreateAggregateConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/fsx-2018-03-01/CreateAggregateConfiguration) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/fsx-2018-03-01/CreateAggregateConfiguration) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/fsx-2018-03-01/CreateAggregateConfiguration) 