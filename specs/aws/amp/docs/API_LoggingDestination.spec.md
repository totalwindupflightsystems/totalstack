---
id: "@specs/aws/amp/docs/API_LoggingDestination"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS LoggingDestination"
status: active
depends_on:
  - "@specs/aws/amp/meta"
---

# LoggingDestination

> **source:** AWS Documentation
> **spec:id:** @specs/aws/amp/docs/API_LoggingDestination
> **target_lang:** meta — documentation tier. ALL sections preserved.



# LoggingDestination
<a name="API_LoggingDestination"></a>

Defines a destination and its associated filtering criteria for query logging.

## Contents
<a name="API_LoggingDestination_Contents"></a>

 ** cloudWatchLogs **   <a name="prometheus-Type-LoggingDestination-cloudWatchLogs"></a>
Configuration details for logging to CloudWatch Logs.  
Type: [CloudWatchLogDestination](API_CloudWatchLogDestination.md) object  
Required: Yes

 ** filters **   <a name="prometheus-Type-LoggingDestination-filters"></a>
Filtering criteria that determine which queries are logged.  
Type: [LoggingFilter](API_LoggingFilter.md) object  
Required: Yes

## See Also
<a name="API_LoggingDestination_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/amp-2020-08-01/LoggingDestination) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/amp-2020-08-01/LoggingDestination) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/amp-2020-08-01/LoggingDestination) 