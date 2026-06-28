---
id: "@specs/aws/fsx/docs/API_AggregateConfiguration"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS AggregateConfiguration"
status: active
depends_on:
  - "@specs/aws/fsx/meta"
---

# AggregateConfiguration

> **source:** AWS Documentation
> **spec:id:** @specs/aws/fsx/docs/API_AggregateConfiguration
> **target_lang:** meta — documentation tier. ALL sections preserved.



# AggregateConfiguration
<a name="API_AggregateConfiguration"></a>

Used to specify configuration options for a volume’s storage aggregate or aggregates.

## Contents
<a name="API_AggregateConfiguration_Contents"></a>

 ** Aggregates **   <a name="FSx-Type-AggregateConfiguration-Aggregates"></a>
The list of aggregates that this volume resides on. Aggregates are storage pools which make up your primary storage tier. Each high-availability (HA) pair has one aggregate. The names of the aggregates map to the names of the aggregates in the ONTAP CLI and REST API. For FlexVols, there will always be a single entry.  
Amazon FSx responds with an HTTP status code 400 (Bad Request) for the following conditions:  
+ The strings in the value of `Aggregates` are not are not formatted as `aggrX`, where X is a number between 1 and 12.
+ The value of `Aggregates` contains aggregates that are not present.
+ One or more of the aggregates supplied are too close to the volume limit to support adding more volumes.
Type: Array of strings  
Array Members: Maximum number of 6 items.  
Length Constraints: Minimum length of 5. Maximum length of 6.  
Pattern: `^(aggr[0-9]{1,2})$`   
Required: No

 ** TotalConstituents **   <a name="FSx-Type-AggregateConfiguration-TotalConstituents"></a>
The total number of constituents this FlexGroup volume has. Not applicable for FlexVols.  
Type: Integer  
Valid Range: Minimum value of 1. Maximum value of 200.  
Required: No

## See Also
<a name="API_AggregateConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/fsx-2018-03-01/AggregateConfiguration) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/fsx-2018-03-01/AggregateConfiguration) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/fsx-2018-03-01/AggregateConfiguration) 