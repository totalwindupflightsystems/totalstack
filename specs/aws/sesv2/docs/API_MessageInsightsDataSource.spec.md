---
id: "@specs/aws/sesv2/docs/API_MessageInsightsDataSource"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS MessageInsightsDataSource"
status: active
depends_on:
  - "@specs/aws/sesv2/meta"
---

# MessageInsightsDataSource

> **source:** AWS Documentation
> **spec:id:** @specs/aws/sesv2/docs/API_MessageInsightsDataSource
> **target_lang:** meta — documentation tier. ALL sections preserved.



# MessageInsightsDataSource
<a name="API_MessageInsightsDataSource"></a>

An object that contains filters applied when performing the Message Insights export.

## Contents
<a name="API_MessageInsightsDataSource_Contents"></a>

 ** EndDate **   <a name="SES-Type-MessageInsightsDataSource-EndDate"></a>
Represents the end date for the export interval as a timestamp. The end date is inclusive.  
Type: Timestamp  
Required: Yes

 ** StartDate **   <a name="SES-Type-MessageInsightsDataSource-StartDate"></a>
Represents the start date for the export interval as a timestamp. The start date is inclusive.  
Type: Timestamp  
Required: Yes

 ** Exclude **   <a name="SES-Type-MessageInsightsDataSource-Exclude"></a>
Filters for results to be excluded from the export file.  
Type: [MessageInsightsFilters](API_MessageInsightsFilters.md) object  
Required: No

 ** Include **   <a name="SES-Type-MessageInsightsDataSource-Include"></a>
Filters for results to be included in the export file.  
Type: [MessageInsightsFilters](API_MessageInsightsFilters.md) object  
Required: No

 ** MaxResults **   <a name="SES-Type-MessageInsightsDataSource-MaxResults"></a>
The maximum number of results.  
Type: Integer  
Valid Range: Minimum value of 1. Maximum value of 10000.  
Required: No

## See Also
<a name="API_MessageInsightsDataSource_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sesv2-2019-09-27/MessageInsightsDataSource) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sesv2-2019-09-27/MessageInsightsDataSource) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sesv2-2019-09-27/MessageInsightsDataSource) 