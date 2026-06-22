---
id: "@specs/aws/sesv2/docs/API_MetricsDataSource"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS MetricsDataSource"
status: active
depends_on:
  - "@specs/aws/sesv2/meta"
---

# MetricsDataSource

> **source:** AWS Documentation
> **spec:id:** @specs/aws/sesv2/docs/API_MetricsDataSource
> **target_lang:** meta — documentation tier. ALL sections preserved.



# MetricsDataSource
<a name="API_MetricsDataSource"></a>

An object that contains details about the data source for the metrics export.

## Contents
<a name="API_MetricsDataSource_Contents"></a>

 ** Dimensions **   <a name="SES-Type-MetricsDataSource-Dimensions"></a>
An object that contains a mapping between a `MetricDimensionName` and `MetricDimensionValue` to filter metrics by. Must contain a least 1 dimension but no more than 3 unique ones.  
Type: String to array of strings map  
Map Entries: Maximum number of 3 items.  
Valid Keys: `EMAIL_IDENTITY | CONFIGURATION_SET | ISP`   
Array Members: Minimum number of 1 item. Maximum number of 10 items.  
Required: Yes

 ** EndDate **   <a name="SES-Type-MetricsDataSource-EndDate"></a>
Represents the end date for the export interval as a timestamp.  
Type: Timestamp  
Required: Yes

 ** Metrics **   <a name="SES-Type-MetricsDataSource-Metrics"></a>
A list of `ExportMetric` objects to export.  
Type: Array of [ExportMetric](API_ExportMetric.md) objects  
Array Members: Minimum number of 1 item. Maximum number of 10 items.  
Required: Yes

 ** Namespace **   <a name="SES-Type-MetricsDataSource-Namespace"></a>
The metrics namespace - e.g., `VDM`.  
Type: String  
Valid Values: `VDM`   
Required: Yes

 ** StartDate **   <a name="SES-Type-MetricsDataSource-StartDate"></a>
Represents the start date for the export interval as a timestamp.  
Type: Timestamp  
Required: Yes

## See Also
<a name="API_MetricsDataSource_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sesv2-2019-09-27/MetricsDataSource) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sesv2-2019-09-27/MetricsDataSource) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sesv2-2019-09-27/MetricsDataSource) 