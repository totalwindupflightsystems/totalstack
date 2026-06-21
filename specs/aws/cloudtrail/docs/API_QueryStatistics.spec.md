---
id: "@specs/aws/cloudtrail/docs/API_QueryStatistics"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS QueryStatistics"
status: active
depends_on:
  - "@specs/aws/cloudtrail/meta"
---

# QueryStatistics

> **source:** AWS Documentation
> **spec:id:** @specs/aws/cloudtrail/docs/API_QueryStatistics
> **target_lang:** meta — documentation tier. ALL sections preserved.



# QueryStatistics
<a name="API_QueryStatistics"></a>

Metadata about a query, such as the number of results.

## Contents
<a name="API_QueryStatistics_Contents"></a>

 ** BytesScanned **   <a name="awscloudtrail-Type-QueryStatistics-BytesScanned"></a>
The total bytes that the query scanned in the event data store. This value matches the number of bytes for which your account is billed for the query, unless the query is still running.  
Type: Long  
Required: No

 ** ResultsCount **   <a name="awscloudtrail-Type-QueryStatistics-ResultsCount"></a>
The number of results returned.  
Type: Integer  
Required: No

 ** TotalResultsCount **   <a name="awscloudtrail-Type-QueryStatistics-TotalResultsCount"></a>
The total number of results returned by a query.  
Type: Integer  
Required: No

## See Also
<a name="API_QueryStatistics_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cloudtrail-2013-11-01/QueryStatistics) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudtrail-2013-11-01/QueryStatistics) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudtrail-2013-11-01/QueryStatistics) 